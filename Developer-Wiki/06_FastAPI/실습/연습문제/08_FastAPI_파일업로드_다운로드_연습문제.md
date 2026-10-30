# 08. 파일 업로드·다운로드 — 폼의 파일 객체에서 디스크와 응답까지 — 연습문제

[본문](../../08_FastAPI_파일업로드_다운로드.md) · [문제 목차](README.md)

실제 수업 내용을 바탕으로 **새로 구성한 연습문제**다. 원본·당시 내 코드·새 개선안을 구별한다. 예상 → 이유 → 한 가지 변경 순서로 푼다.

## 목표와 준비

multipart 폼과 일반 문자열 입력을 구분한다. 필수·선택 파일의 차이, 업로드 객체와 실제 파일 경로, 원래 이름과 저장 이름, copyfileobj의 입력·출력, 없는 파일의404를 설명한다.

[본문 3절](../../08_FastAPI_파일업로드_다운로드.md#example)의 폴더·설치·입력·실행 조건부터 확인한다. 아래 필요한 파일 전체를 같은 구조로 저장한다. 가져오는 함수·모델 정의도 빠뜨리지 않는다.

## 문제 1. 요청과 결과 예상

**api.py**

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

**upload.html**

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

실행 전에 결과를 먼저 적는다. 상태·응답·서버 출력·변경된 자료를 구별한다.

<details>
<summary>풀이</summary>

| 요청 | 결과 |
| --- | --- |
|file1 note.txt·file2 두 개 | 새 saved_name·원래이름·추가이름2개 |
|saved_name다운로드 | 처음 보낸 공부 파일과 같은 내용 |
|file2누락 | 정상·other_names=[] |
|file1누락 |422 |
|없는 저장이름 |404 |

폼 file1의 내용은 UUID.bin으로 복사하고 응답의 saved_name으로 다음 다운로드를 찾는다. 다운로드는 그 이름에 연결한 경로를 읽고 원래 note.txt라는 파일명으로 응답한다. file2 두 개는 other_names에 이름만 돌려주고 저장하지 않는다. 선택 파일이 없으면 빈 목록이고 필수 file1이 없으면422다. UUID는 실행마다 달라 고정 문자열이 아닌 업로드 응답값으로 다음 요청을 만든다.

| 자료 | 브라우저·요청 | 서버 |
| --- | --- | --- |
|이름 | note.txt | 원래 이름 메타정보 |
|내용 | 공부 파일 바이트 | UUID.bin저장 |
|다음 주소 | saved_name사용 | 저장 경로 찾기 |
|추가 파일 | file2이름 둘 | 이름만 읽음 |

</details>

## 문제 2. 이유 설명

1. filename과 file은 같은가?
2. multiple만 적으면 모두 저장되는가?
3. UUID붙인 뒤 다운로드에는 어떤 이름을 써야 하는가?
4. 선택 File(None)이면 본문도 자동 None처리되는가?
5. 원본 성공 업로드는 저장명을 응답하는가?

<details>
<summary>풀이</summary>

이름 문자열과 파일 객체다. 서버 본문이 저장해야 한다. 서버에서 찾는 저장명이다. 본문 분기가 필요하다. return이 없어 null이고 새 예제에서 저장명을 반환하도록 보완했다.

</details>

## 문제 3. 한 가지만 바꾸기

| 한 가지만 변경 | 예상 | 이유 |
| --- | --- | --- |
|file2선택 없음 | 새 예제 정상 | None→빈 목록 |
|file1이름만 동일하게 재업로드 | 다른 UUID저장명 | 새 식별자 생성 |
|다운로드값을 원래 이름으로 |404 | 서버 저장 키와 다름 |
|title키 제거 |422 | 필수 폼 값 |

<details>
<summary>막힐 때 확인</summary>

422면 enctype·name·필수 파일을 본다. 저장 실패면 현재 작업 위치·uploads폴더·쓰기 경로를 확인한다. 다운로드404면 원래 이름 대신 저장명을 썼는지 본다. 서버 재시작 뒤 새 예제 목록이 없다면 디스크 파일과 메모리 메타정보의 차이를 구별한다.

</details>

## 채점과 복습

정상 값만 보지 말고 누락·잘못된 타입·없는 대상의 흐름도 설명한다. 새 예제는 별도 앱에서 확인하며 원본 DB나 외부 서비스의 성공을 대신 주장하지 않는다. TIP 확장은 필수 조건이 아니다. 정의→등록→입력→호출→반환→다음 요청을 연결할 수 있는지 검토한다.
