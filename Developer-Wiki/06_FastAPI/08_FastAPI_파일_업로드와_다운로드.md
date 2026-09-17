# FastAPI 파일 업로드와 다운로드

<a id="section-1"></a>

## 문서 정보

| 항목 | 내용 |
| --- | --- |
| 내·강사님 코드 | workspace_python/04_fileupload/api.py, upload.html |
| 핵심 | multipart Form, UploadFile, 바이너리 저장, UUID, FileResponse |
| 보강 표시 | 안전한 저장명·경로 검증·크기 제한은 💡 개선 내용 |
| 주의 | 원본 import도 uploads 폴더를 만들 수 있다. 검증은 별도 임시 경로에서 한다. |

<a id="section-2"></a>

## 학습 목표

- 브라우저가 첨부 파일을 보내는 위치와 UploadFile의 역할을 이해한다.
- 저장명·원본명·파일 내용·다운로드 응답을 구분한다.
- 선택 파일과 경로·용량 검증을 명시한다.

<a id="section-3"></a>

## 1. 파일은 왜 JSON이나 Query와 다르게 보내는가?

파일 입력은 파일명의 텍스트뿐 아니라 실제 파일 바이트를 전송해야 한다. HTML Form의 enctype="multipart/form-data"는 텍스트·파일을 여러 부분으로 나눠 하나의 Body에 담는다. boundary는 각 부분을 구분하는 표식이다. 서버는 같은 name으로 등록한 Form()/File() 선언에 데이터를 연결한다. [공식 파일 요청 안내](https://fastapi.tiangolo.com/tutorial/request-files/)

```html
<!-- 서버가 같은 origin에서 제공한 페이지에 적용하는 개선 예시 -->
<form method="post" action="/upload" enctype="multipart/form-data">
  <input name="title" value="수업 자료">
  <textarea name="content">복습용</textarea>
  <input type="file" name="file1">
  <input type="file" name="file2" multiple>
  <button>전송</button>
</form>
```


LiveServer에서 이 상대 action을 쓰면 LiveServer /upload로 간다. 수업 원본의 http://127.0.0.1:8000/upload는 API 서버를 명시한 것이다. 상대 URL 개선은 API 서버가 HTML도 제공하는 구성 기준이다. 파일을 선택하지 않은 경우 누락·빈 파일 부분의 해석을 실제 요청에서 확인해야 한다.

<a id="section-4"></a>

## 2. UploadFile은 무엇을 가지고 있는가?

filename은 사용자 제공 원본명, content_type은 선언된 MIME type, size는 읽힌 크기 정보, file은 서버가 처리할 수 있는 임시 파일 객체다. await upload.read()는 바이트를 읽고 upload.file은 동기 파일 인터페이스다. 큰 파일을 모두 bytes로 읽는 방식보다 UploadFile의 spool 임시 저장 방식이 메모리 사용에 유리할 수 있지만 업로드 용량을 무제한 허용해도 된다는 뜻은 아니다.

```text
sample.txt 내용 ABC 선택
→ multipart part name=file1, filename=sample.txt
→ UploadFile 객체 생성
→ file1.filename은 "sample.txt", 내용은 b"ABC"
→ 서버 저장 코드가 실제 경로에 3바이트 기록
```

입력 파일 객체와 서버에 영구 저장된 파일은 별개다. 요청으로 UploadFile을 받았다고 uploads에 자동 저장되는 것은 아니다.

<a id="section-5"></a>

## 3. 내 코드와 강사님 코드 비교

| 항목 | 내 api.py | 강사님 api.py |
| --- | --- | --- |
| file1 | File() 필수 | File(None) 선택 |
| file2 | list[UploadFile] = File() 필수 | File(None) 선택 |
| file1 처리 | 즉시 filename·size 접근 | 선택인데도 즉시 filename·size 접근 |
| 실제 저장 | file1 하나 저장 | file1 하나 저장 |
| file2 | 파일명을 print만 함 | 파일명을 print만 함 |
| 응답 | return 없음 → 기본 null | 동일 |
| 다운로드 | 사용자명으로 uploads 경로 결합 | 동일 |

강사님은 선택 파일이 없으면 file1=None에서 AttributeError, file2=None 순회에서 TypeError가 날 수 있다. 내 코드는 파일 누락 때 보통 422 입력 오류이며 '선택 첨부'가 아니다. 두 코드 모두 file2를 여러 개 받지만 실제로 저장하지 않는다. multi upload 완성이라고 해설하면 안 된다.

<a id="section-6"></a>

## 4. wb·copyfileobj·UUID가 하는 일

```python
# 양쪽 수업의 저장 핵심 조각

## 목차

- [문서 정보](#section-1)
- [학습 목표](#section-2)
- [1. 파일은 왜 JSON이나 Query와 다르게 보내는가?](#section-3)
- [2. UploadFile은 무엇을 가지고 있는가?](#section-4)
- [3. 내 코드와 강사님 코드 비교](#section-5)
- [4. wb·copyfileobj·UUID가 하는 일](#section-6)
- [5. 개선된 제한 업로드 — 처리 순서와 결과](#section-7)
- [6. 다운로드: exists만 확인하면 충분한가?](#section-8)
- [7. 실제 확인·실무 지침·디버깅](#section-9)
- [8. 종합실습](#section-10)
- [9. 정답과 해설](#section-11)
- [최종 체크리스트](#section-12)
- [핵심 요약](#section-13)

filename_safe = f"{uuid.uuid4().hex}_{file1.filename}"
target_path = dir / filename_safe
with target_path.open("wb") as buffer:
    shutil.copyfileobj(file1.file, buffer)
```


Path의 /는 경로 결합 연산이고 wb는 바이너리 쓰기 모드다. w가 텍스트 모드인 것은 맞지만 wb도 기존 파일이 있으면 덮어쓸 수 있다. UUID 접두사는 충돌 가능성을 크게 줄이지만 원본 filename의 경로 조각을 무조건 안전하게 만들지는 않는다. copyfileobj는 소스 파일에서 목적 파일로 내용을 복사한다. async def 내부에서 이 동기 복사를 직접 실행하면 event loop를 막을 수 있다.

UUID 출력의 print(uuid.uuid4())와 저장명 생성의 uuid.uuid4()는 서로 다른 호출이므로 출력 UUID와 파일명 접두사가 같지 않을 수 있다. 저장명을 확인하려면 filename_safe 자체를 print한다.

<a id="section-7"></a>

## 5. 개선된 제한 업로드 — 처리 순서와 결과

💡 아래는 수업에 없는 안전 보강용 별도 api.py 예제다. 같은 폴더에 상대 uploads가 생기므로 전용 연습 폴더에서 실행한다.

```python
from pathlib import Path
from uuid import uuid4
from fastapi import FastAPI, UploadFile, File, Form, HTTPException

app = FastAPI()
ROOT = Path("uploads").resolve()
ROOT.mkdir(exist_ok=True)

@app.post("/upload", status_code=201)
async def upload(title: str = Form(), file1: UploadFile = File()):
    target = ROOT / (uuid4().hex + ".bin")
    size = 0
    try:
        with target.open("xb") as output:
            while chunk := await file1.read(8192):
                size += len(chunk)
                if size > 1024 * 1024:
                    raise HTTPException(413, "1 MiB 초과")
                output.write(chunk)
        return {"title": title, "saved_name": target.name, "size": size}
    except Exception:
        target.unlink(missing_ok=True)
        raise
    finally:
        await file1.close()
```


원본명을 저장 경로에서 제외하고 UUID만 쓴다. xb는 기존 파일 충돌 때 오류를 내는 모드다. 읽기 chunk는 8192바이트이며 '2byte씩'이라는 내 주석과 다르다. size는 읽은 바이트 누적값이고 1 MiB=1048576바이트를 넘으면 413, 중간 저장 파일은 삭제한다. 제목 수업 자료와 ABC인 파일이면 201, size=3, saved_name은 매번 다른 UUID.bin이다. 이는 원본의 null 응답과 다른 개선 계약이다.

이 예제도 네트워크·프록시 단계 용량 제한, 디스크 한도, MIME 실제 검사, 권한·악성 파일 검사까지 완성한 운영 시스템은 아니다. 동기 파일 쓰기를 threadpool로 분리하는 보강도 대량 작업에서는 검토한다. 저장된 파일을 HTML로 직접 실행하지 않도록 제공 방식도 제한한다.

<a id="section-8"></a>

## 6. 다운로드: exists만 확인하면 충분한가?

원본 /download?file_name=...은 dir/file_name을 그대로 사용한다. ../이나 절대 경로를 이용하면 저장 영역 밖의 경로를 가리킬 수 있다. exists()는 존재만 검사하지 허용 영역·파일 타입·사용자 권한을 검사하지 않는다. 아래 조각은 부모 경로를 검사한다.

```python
# ROOT와 app은 앞 예제의 것을 사용
from fastapi.responses import FileResponse

@app.get("/download")
def download(file_name: str):
    path = (ROOT / file_name).resolve()
    if path.parent != ROOT or not path.is_file():
        raise HTTPException(404, "파일을 찾을 수 없습니다")
    return FileResponse(
        path, filename=path.name,
        media_type="application/octet-stream",
    )
```


여기서는 ROOT 바로 아래 파일만 허용한다. 실제 서비스는 사용자가 저장 경로를 직접 정하지 못하게 파일 ID와 소유권을 조회하는 방식이 좋다. 심볼릭 링크·검사 이후 교체 같은 상황까지 일반 예제로 모두 방어됐다고 주장하지 않는다.

FileResponse는 응답에 파일 바이트를 넣고 filename을 지정하면 Content-Disposition에 다운로드 이름을 설정할 수 있다. application/octet-stream은 일반 바이너리 MIME type이다. 이미지가 img 태그에서 보이는지는 MIME·브라우저 처리·헤더에 영향받으므로 '모든 파일을 항상 이미지처럼 표시'한다고 보지 않는다.

<a id="section-9"></a>

## 7. 실제 확인·실무 지침·디버깅

Network에서 POST /upload, multipart Content-Type, file1/file2 이름을 본다. 터미널 원본명·size와 저장 파일명·실제 디스크 크기를 대조한다. 원본 uploads는 현재 실행 폴더 기준이라 파일이 예상 위치에 없으면 작업 폴더부터 확인한다. 파일 업로드 입력에서 accept 속성은 UI 선택 제한이지 서버 보안 검사 대체가 아니다.

| 실패 | 원본/개선 원인 | 결과 |
| --- | --- | --- |
| python-multipart 없음 | Form parser 의존성 누락 | 시작/처리 오류 |
| 필수 파일 누락 | 내 File() 선언 | 422 |
| 선택 파일 미검사 | 강사님 None 접근 | 내부 500 가능 |
| 파일2 저장 안 됨 | print만 실행 | 원본 의도 확인 필요 |
| 용량 초과 | 개선 누적 검사 | 413·중간 파일 삭제 |
| 없는 파일/상위 경로 | 개선 경로 검사 | 404 |

<a id="section-10"></a>

## 8. 종합실습

3바이트 파일을 업로드해 size=3과 디스크 내용을 확인한다. 다운로드 후 바이트가 ABC인지 확인한다. 파일 누락, 1 MiB 초과, ../ 요청, 같은 원본명 두 번 업로드를 시험한다. 다중 파일은 각 파일별 저장·실패 정리 규칙을 별도로 설계한다.

<a id="section-11"></a>

## 9. 정답과 해설

<details><summary>업로드가 정상인데 화면에 null이 보이는 이유는?</summary>

원본은 복사 후 return이 없다. 저장 성공 여부와 응답 본문은 별개다. 저장 경로의 바이트를 확인하고 개선처럼 저장명·크기를 반환하면 확인이 쉽다. 큰 파일 제한에서는 중간 실패 파일을 정리하고 예외를 다시 전달해야 한다.

</details>

<details><summary>파일 이름에 UUID를 붙이면 경로 검증이 필요 없을까?</summary>

아니다. 원본 사용자 filename과 다운로드 Query를 신뢰하지 않는다. 서버 저장명은 서버가 만들고 다운로드는 저장 영역·권한을 확인한다.

</details>

<a id="section-12"></a>

## 최종 체크리스트

- [ ] name·enctype·File 선언을 서로 연결한다.
- [ ] UploadFile 수신과 실제 저장을 구분한다.
- [ ] 선택 파일의 None과 필수 누락 422를 구분한다.
- [ ] 파일2는 원본에서 저장하지 않는다는 점을 안다.
- [ ] 서버 저장명·용량·다운로드 경로를 검사한다.
- [ ] 요청 파일 객체와 실패 중간 파일을 정리한다.

<a id="section-13"></a>

## 핵심 요약

multipart Body → UploadFile → 서버가 정한 저장명 → 바이트 복사 → 응답. FileResponse는 저장 파일을 읽어 HTTP 응답으로 보낸다. UUID와 exists만으로 보안 검증이 끝나지 않는다.
