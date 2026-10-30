# 08. 파일 업로드·다운로드 — 폼의 파일 객체에서 디스크와 응답까지

[FastAPI 목차](README.md) · [읽기 안내](00_FastAPI_상세백과_읽기법.md)

파일 이름을 받는 것과 파일 내용을 저장하는 것은 다르다. HTML의 name·전송 형식·UploadFile·바이너리 저장·저장 이름·다운로드 응답을 끝까지 연결한다. 원본에서 여러 파일은 이름만 출력한다는 사실도 구별한다.

**이 장의 목차:** [목표](#learn) · [개념](#concepts) · [예제](#example) · [내 코드](#my-code) · [연결](#connections) · [평가](#review) · [비교](#teacher) · [결과·실험](#results) · [TIP·출처](#tips) · [복습](#practice)

<a id="learn"></a>

## 1. 이 장에서 배울 것

multipart 폼과 일반 문자열 입력을 구분한다. 필수·선택 파일의 차이, 업로드 객체와 실제 파일 경로, 원래 이름과 저장 이름, copyfileobj의 입력·출력, 없는 파일의404를 설명한다.

<a id="concepts"></a>

## 2. 무엇이며, 왜 필요한가

브라우저에서 파일을 선택하면 서버에 로컬 파일 경로를 그대로 넘겨 읽게 하는 것이 아니다. 폼이 파일 내용을 요청 본문에 보내고 서버는 업로드된 파일을 다루는 객체를 받는다. multipart/form-data는 여러 폼 항목과 파일을 구분해 보내는 형식이다.

| 자리 | 의미 | 원본 연결 |
| --- | --- | --- |
| input type=file | 브라우저 파일 선택 | name=file1 |
| multiple | 여러 파일 선택 가능 | name=file2 |
| Form | 일반 폼 값 | title·content |
| UploadFile | 업로드 파일 정보·내용 접근 | filename·size·file |
| File() | 파일 입력 선언 | 필수 입력 |
| File(None) | 누락 허용 선언 | 본문에서도 None처리 필요 |
| Path·wb | 서버 저장 위치·바이너리 쓰기 | uploads내 파일 |
| FileResponse | 저장 파일을 응답 | 다운로드 경로 |

filename은 받은 이름이고 file은 내용을 읽는 파일 객체다. 이름을 print했다고 내용을 저장한 것은 아니다. copyfileobj(원본객체,대상객체)는 원본에서 읽은 바이트를 대상으로 복사한다. 조금씩 읽는 방식이 모든 파일의 크기·형식·보안을 검증한다는 뜻은 아니다.

텍스트모드w는 문자열, 바이너리모드wb는 바이트를 쓰는 맥락이다. 사진·문서·텍스트파일 모두 원래 바이트를 옮길 때wb를 쓸 수 있다. 다운로드하려면 브라우저의 원래 이름과 서버에서 저장한 이름이 다를 수 있다는 점을 알아야 한다.

> 📚 **출처 · 본문 설명 확인:** [FastAPI 파일 입력](https://fastapi.tiangolo.com/tutorial/request-files/), [Python copyfileobj](https://docs.python.org/ko/3/library/shutil.html#shutil.copyfileobj), [pathlib](https://docs.python.org/ko/3/library/pathlib.html). 배운 의미 확인 근거다. 아래 표·전체 예제·풀이를 외부 문장 그대로 옮기지 않았다. 확인일: 2026-10-30.

<a id="example"></a>

## 3. 작은 예제로 먼저 이해하기

**새 설명 예제 · 필요한 파일 전체.** 같은 장의 폴더 구조를 유지한다. api.py와 upload.html을 같은 폴더에 둔다. FastAPI·Uvicorn·python-multipart가 필요하다. `uvicorn api:app --port 8000 --reload`로 실행해 /form을 연다. 새 예제는 uploads에 UUID.bin으로 저장하고 원래 이름은 별도 메모리dict에 둔다. 이 저장명 연결은 교재에서 새로 만든 보완이며 원본의 UUID_원래이름과 다르다. 서버를 재시작하면 파일은 남아도 메모리 연결은 사라지는 한계가 있다.



**[api.py](실습/책형_복습/08_FastAPI_파일업로드_다운로드/api.py) — 새 예제 전체 파일**

```python
from fastapi import FastAPI, Form, File, UploadFile, HTTPException
from fastapi.responses import FileResponse
from pathlib import Path
import uuid
import shutil

app = FastAPI()
upload_dir = Path('uploads')
upload_dir.mkdir(exist_ok=True)
saved_files = {}

@app.get('/form')
def form_page():
    return FileResponse('upload.html')

@app.post('/upload')
async def upload(title: str = Form(), content: str = Form(''),
                 file1: UploadFile = File(), file2: list[UploadFile] | None = File(None)):
    stored_name = uuid.uuid4().hex + '.bin'
    target = upload_dir / stored_name
    with target.open('wb') as output:
        shutil.copyfileobj(file1.file, output)
    saved_files[stored_name] = {'path': target, 'original_name': file1.filename}
    return {'title': title, 'saved_name': stored_name,
            'original_name': file1.filename,
            'other_names': [file.filename for file in (file2 or [])]}

@app.get('/download')
def download(file_name: str):
    saved = saved_files.get(file_name)
    if saved is None or not saved['path'].is_file():
        raise HTTPException(status_code=404, detail='파일을 찾을 수 없습니다')
    return FileResponse(path=saved['path'], filename=saved['original_name'],
                        media_type='application/octet-stream')
```

**[upload.html](실습/책형_복습/08_FastAPI_파일업로드_다운로드/upload.html) — 새 예제 전체 파일**

```html
<!DOCTYPE html><html lang="ko"><head><meta charset="UTF-8"><title>파일 복습</title></head><body>
<form method="post" action="/upload" enctype="multipart/form-data">
<label>제목 <input name="title" required></label>
<textarea name="content"></textarea>
<label>저장할 파일 <input type="file" name="file1" required></label>
<label>이름만 볼 여러 파일 <input type="file" name="file2" multiple></label>
<button type="submit">전송</button>
</form><p>응답의 saved_name을 복사해 /download?file_name=저장된이름 으로 요청한다.</p>
</body></html>
```

폼 file1의 내용은 UUID.bin으로 복사하고 응답의 saved_name으로 다음 다운로드를 찾는다. 다운로드는 그 이름에 연결한 경로를 읽고 원래 note.txt라는 파일명으로 응답한다. file2 두 개는 other_names에 이름만 돌려주고 저장하지 않는다. 선택 파일이 없으면 빈 목록이고 필수 file1이 없으면422다. UUID는 실행마다 달라 고정 문자열이 아닌 업로드 응답값으로 다음 요청을 만든다.

**요청과 예상 결과:**

| 요청 | 결과 |
| --- | --- |
|file1 note.txt·file2 두 개 | 새 saved_name·원래이름·추가이름2개 |
|saved_name다운로드 | 처음 보낸 공부 파일과 같은 내용 |
|file2누락 | 정상·other_names=[] |
|file1누락 |422 |
|없는 저장이름 |404 |

<a id="my-code"></a>

## 4. 내가 작성한 코드를 따라 읽기

### 내 코드 — 원본

출처: `D:/workspace/workspace_python/04_fileupload/upload.html` 14–25행 · **원본 발췌**

```html
        <form
            method="post"
            action="http://127.0.0.1:8000/upload"
            enctype="multipart/form-data"
        >
            제목 : <input type="text" name="title"><br>
            내용<br>
            <textarea name="content"></textarea><br>
            파일 첨부1 : <input type="file" name="file1"><br>
            파일 첨부2 : <input type="file" name="file2" multiple="multiple"><br><br>
            <input type="submit" value="전송">
        </form>
```

**발췌 바로 풀이:** `action`은 요청 주소 `/upload`, `method="post"`는 요청 방식이다. 파일을 보내는 폼에는 `enctype="multipart/form-data"`를 적었다. 각 입력의 `name="title"`, `name="content"`, `name="file1"`, `name="file2"`가 아래 Python 함수의 매개변수 이름과 맞는다. 두 번째 파일 입력의 `multiple`은 브라우저에서 여러 파일을 선택하게 한다. 이 HTML의 다운로드 `<img>`는 미리 적어 둔 파일 이름을 사용하므로 새 업로드 결과와 자동 연결되지는 않는다.
### 내 코드 — 원본

출처: `D:/workspace/workspace_python/04_fileupload/api.py` 18–24행 · **원본 발췌**

```python
@app.post('/upload')
async def upload(
    # title = Form(...), # '...'을 쓰면 Form에서 필수 값이며 평시엔 생략되어 보임
    title = Form(),
    content = Form(None), # 'None'은 필수값이 아니기에 없어도 된다
    file1 : UploadFile = File(), # Form() 으로도 가능하지만, UploadFile로 받아주는게 좋음
    file2 : list[UploadFile] = File() # type=file이 'multiple'일 때 list로 받을 수 있음
```

**발췌 바로 풀이:** 학생은 file1·file2 모두 필수다. 강사님은 None을 기본값으로 두었지만 본문에서 None분기를 처리하지 않아 선택 입력 완성 예제가 아니다. 새 예제는 file2만 선택으로 바꾸고 누락을 빈 목록으로 처리한다.
### 내 코드 — 원본

출처: `D:/workspace/workspace_python/04_fileupload/api.py` 40–55행 · **원본 발췌**

```python

    # uuid를 import해서 파일명에 uuid를 붙일수도 있음
    print('uuid.uuid4 : ', uuid.uuid4())
    filename_safe = f'{uuid.uuid4().hex}_{filename_orig}'

    # Path Class에서는 '/' 를 쓰게 되면 경로가 됨(경로 합치기)
    # '/' 는 Path가 지정 한 결합 연산자
    # target_path = dir / file1.filename
    target_path = dir / filename_safe
    # w는 Text형태로 저장하기 때문에 wb로 binary(2진수)형태의 파일 그 자체로 저장
    with target_path.open('wb') as buffer :
        # shutil을 import 해서 손쉽게 저장할 수 있다
        # 기존엔 buffer.write() 로 해도 되지만 큰 파일은 메모리 등의 문제가 많음
        # 해서 chunk라는 변수에 담아 2byte씩 읽어와 넣기도 했지만 
        # shutil은 조금씩 쪼개서 안전하고 효율적으로 저장할 수 있기에 사용
        shutil.copyfileobj(file1.file, buffer)
```

**발췌 바로 풀이:** copyfileobj가 읽는 대상은 UploadFile.file이고 쓰는 대상은 Path.open으로 얻은 바이너리 파일 객체다. 주석의 chunk2byte는 활성 코드가 아니며 copyfileobj의 실제 고정 읽기 크기를2바이트라고 설명하지 않는다.
### 내 코드 — 원본

출처: `D:/workspace/workspace_python/04_fileupload/api.py` 57–79행 · **원본 발췌**

```python
    # file2 multiple처리 part
    for f in file2 :
        print('filename : ', f.filename)

# 첨부파일 download
@app.get('/download')
def download(file_name):
    file_path = dir / file_name

    # 아래처럼 사용하면 파일 유무에 따라 True,False로 반환
    # file_path.exists() = [파일경로].exists()
    if not file_path.exists() :
        # raise와 import HTTPException을 활용해 err코드 출력
        raise HTTPException(
            status_code=404,
            detail='파일을 찾을 수 없습니다'
        )

    return FileResponse(
        path=file_path, 
        filename=file_name, 
        # filename='a.txt', # 이것과 같이 초기 파일명을 지정할 수 있음
        media_type='application/octet-stream')
```

**발췌 바로 풀이:** 두 코드 모두 `file2`의 이름만 출력한다. **두 번째 파일 목록은 저장하지 않는다.** 다운로드에서는 요청의 `file_name`으로 경로를 만들고, 파일이 없으면 404를 발생시키며 있으면 `FileResponse`를 반환한다. 따라서 저장한 이름(UUID가 붙은 이름)을 알아야 그 파일을 요청할 수 있다.
### 내 코드 — 원본

출처: `D:/workspace/workspace_python/04_fileupload/api.py` 3–16행 · **원본 발췌**

```python
from fastapi import FastAPI, Form, UploadFile, File, HTTPException
# 파일을 download받기 위해 'FileResponse' 필요
from fastapi.responses import FileResponse
from pathlib import Path
import shutil
from datetime import datetime
import uuid

app = FastAPI()

# uploads라는 폴더 생성
dir = Path('uploads')
dir.mkdir(exist_ok=True) # 없으면 만들어주고, 있으면 만들지 않음(exist_ok=True)

```
### 내 코드 — 원본

출처: `D:/workspace/workspace_python/04_fileupload/api.py` 25–32행 · **원본 발췌**

```python
):
    print('title : ',title)
    print('content : ',content)

    print('filename : ', file1.filename)
    print('filesize : ', file1.size) # Byte단위

    filename_orig = file1.filename
```

**발췌 바로 풀이:** 실제로 원래 이름·바이트 크기를 읽는 부분이다. filename_orig정의가 있어야 뒤의 UUID이름 생성을 읽을 수 있다.

내 HTML폼 name과 Python인자 이름을 연결했다. uploads폴더를 mkdir하고 UUID_원래이름을 만든 뒤 wb로 저장한다. 화면의 고정 img다운로드 주소는 새 업로드 응답과 자동 연결되지 않는다. 원본 함수는 파일1을 저장하지만 명시적 return이 없어 성공 본문이 null이며 저장명을 응답으로 돌려주지 않는다. file2는 이름만 출력하므로 모든 파일이 저장됐다고 말하면 틀리다.

<a id="connections"></a>

## 5. import·함수·화면·저장이 연결되는 흐름

upload.html폼 → POST /upload의 title·content·file1·file2 → filename_orig → UUID저장명 → Path결합 → wb파일 열기 → copyfileobj → 디스크다. 다운로드는 요청 저장명 → 파일 조회 → 존재 검사 → HTTPException 또는 FileResponse다. 새 예제는 업로드 응답의 saved_name과 메모리 dict를 추가해 연결을 눈으로 확인하게 했다. 각 함수·import·입력 HTML이 위에 전부 있다.

<a id="review"></a>

## 6. 잘한 점·아쉬운 점·개선 방향

**잘한 점:** 내 코드는 파일 이름 충돌을 줄이려 UUID를 붙이고 바이너리 저장과 다운로드를 실제로 연결했다. **구분:** 복사 방식이 효율적이라는 설명과 크기·형식 검증은 다르다. **원본 한계:** 다운로드 입력명을 그대로 경로에 붙이고 저장명 반환·파일 목록 관리도 없다. **새 보완:** 저장 경로에 원래 파일명을 사용하지 않고 서버가 생성한 이름과 연결된 파일만 찾는다. 이 보완도 실서비스의 권한·용량·동시성 정책까지 완성한 것은 아니다.

원본 오류·수업용 단순화·목적에 따른 설계를 나눈다. 새 개선안은 당시 내 코드나 D 드라이브 수정본이 아니다.

<a id="teacher"></a>

## 7. 강사님 코드가 도움이 되는 비교



같은 wb·copyfileobj코드는 중복 인용하지 않는다. 강사님의 File(None)은 선택처럼 보이지만 None본문 처리가 빠져 있고 내 File()은 필수 검증이 먼저 이뤄진다. 무엇을 선택으로 받을지와 실제 본문이 그 누락을 처리하는지를 같이 평가한다.

<a id="results"></a>

## 8. 결과를 추적하고 한 가지 바꾸기

| 자료 | 브라우저·요청 | 서버 |
| --- | --- | --- |
|이름 | note.txt | 원래 이름 메타정보 |
|내용 | 공부 파일 바이트 | UUID.bin저장 |
|다음 주소 | saved_name사용 | 저장 경로 찾기 |
|추가 파일 | file2이름 둘 | 이름만 읽음 |

| 한 가지만 변경 | 예상 | 이유 |
| --- | --- | --- |
|file2선택 없음 | 새 예제 정상 | None→빈 목록 |
|file1이름만 동일하게 재업로드 | 다른 UUID저장명 | 새 식별자 생성 |
|다운로드값을 원래 이름으로 |404 | 서버 저장 키와 다름 |
|title키 제거 |422 | 필수 폼 값 |

422면 enctype·name·필수 파일을 본다. 저장 실패면 현재 작업 위치·uploads폴더·쓰기 경로를 확인한다. 다운로드404면 원래 이름 대신 저장명을 썼는지 본다. 서버 재시작 뒤 새 예제 목록이 없다면 디스크 파일과 메모리 메타정보의 차이를 구별한다.

**확인 범위:** 새 앱을 별도 임시 폴더에 복사해 프레임워크 요청·응답 흐름으로 확인한다. 실제 외부 서비스·운영 DB·브라우저 공개 서버에 요청한 결과와 구별한다. 원본 전체 앱을 무조건 실행하지 않으며 별도 확인한 원본 구간은 검증 보고서에 기록한다. 사용자의 가상환경은 검사에 읽기만 사용하고 파일을 설치·수정하지 않는다.

<a id="tips"></a>

## 9. 추가로 알면 좋은 것과 출처

> 💡 **TIP · 수업 범위 밖:** 업로드 크기·형식·허용 이름·경로 검사·다운로드 권한·메타정보 DB저장·큰 파일의 비동기 처리는 추가 학습이다. UploadFile의 비동기 읽기와 동기 디스크 복사도 별도 성능 주제다. 원본의 filename_safe라는 변수명만으로 안전성을 입증하지 않는다.

request.headers 직접 읽기와 response_model은 미학습으로 확인된 선택 확장이다. 본문에서 이 기능을 선행 조건으로 요구하지 않는다. 응답·입력 타입 표시와 response_model 설정도 구별한다.

<a id="practice"></a>

## 10. 복습과 빠른 정리

1. filename과 file은 같은가?
2. multiple만 적으면 모두 저장되는가?
3. UUID붙인 뒤 다운로드에는 어떤 이름을 써야 하는가?
4. 선택 File(None)이면 본문도 자동 None처리되는가?
5. 원본 성공 업로드는 저장명을 응답하는가?

<details>
<summary>풀이 — 먼저 결과와 이유를 적은 뒤 펼치기</summary>

이름 문자열과 파일 객체다. 서버 본문이 저장해야 한다. 서버에서 찾는 저장명이다. 본문 분기가 필요하다. return이 없어 null이고 새 예제에서 저장명을 반환하도록 보완했다.

</details>

| 단계 | 핵심 |
| --- | --- |
|전송 | enctype·name |
|입력 | UploadFile·필수/선택 |
|저장 | 바이트·경로·저장명 |
|응답 | 저장명 연결·파일 응답 |

[장별 연습문제](실습/연습문제/08_FastAPI_파일업로드_다운로드_연습문제.md) · 다음은 [쿠키·세션](09_FastAPI_Cookie_Session_로그인.md)이다.
