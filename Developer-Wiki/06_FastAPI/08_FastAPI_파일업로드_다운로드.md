# 08. 파일 업로드와 다운로드

[FastAPI 목차](README.md) · [이전: 비밀번호 해시](07-02_비밀번호_해시_실습.md) · [다음: 쿠키와 세션](09_FastAPI_Cookie_Session_로그인.md)

근거는 양쪽의 `04_fileupload/api.py`다. 업로드 폼 입력을 받고, 파일을 `uploads` 폴더에 저장하고, 저장된 파일을 내려주는 **실제 실습 흐름**을 따라간다.

## 먼저: 파일 하나가 오가는 순서

다음은 파일 `photo.png`를 `file1`에 선택했다고 **가정한 설명용 흐름**이다. 실제 저장 이름의 UUID 부분은 실행할 때 만들어지므로 고정된 문자열로 외우지 않는다.

| 단계 | 수업 코드에서 확인할 것 |
| --- | --- |
| HTML 폼 전송 | `name="file1"`로 선택한 파일을 `POST /upload`에 보냄 |
| 서버 입력 | `file1: UploadFile`을 강사님은 `File(None)`, 나는 `File()`로 받음 |
| 디스크 저장 | UUID가 붙은 새 이름으로 `uploads` 안에 바이너리 저장 |
| 다운로드 | 저장된 이름을 `GET /download?file_name=...`에 전달 |

원본의 `file2`는 여러 파일을 선택하지만 **이름만 출력**한다. 따라서 `file1`과 같은 방식으로 모두 저장된다고 예상하면 안 된다. 아래 두 원본의 실제 코드에서 저장하는 파일이 무엇인지 확인하자.

## HTML 폼의 이름이 어디로 가는가

### 강사님 코드

출처: `teacher/workspace_python/04_fileupload/upload.html` 13–27행 · **원본 발췌**

```html
    <form
        method="post" 
        action="http://127.0.0.1:8000/upload"
        enctype="multipart/form-data"
    >
        제목 : <input type="text" name="title"><br>
        내용<br>
        <textarea name="content"></textarea>
        <br>
        파일 첨부 : <input type="file" name="file1">
        <br>
        파일 첨부2 : <input type="file" name="file2" multiple>
        <br><br>
        <input type="submit" value="전송">
    </form>
```

### 내 코드

출처: `me/workspace_python/04_fileupload/upload.html` 14–25행 · **원본 발췌**

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

`action`은 요청 주소 `/upload`, `method="post"`는 요청 방식이다. 파일을 보내는 폼에는 `enctype="multipart/form-data"`를 적었다. 각 입력의 `name="title"`, `name="content"`, `name="file1"`, `name="file2"`가 아래 Python 함수의 매개변수 이름과 맞는다. 두 번째 파일 입력의 `multiple`은 브라우저에서 여러 파일을 선택하게 한다. 이 HTML의 다운로드 `<img>`는 미리 적어 둔 파일 이름을 사용하므로 새 업로드 결과와 자동 연결되지는 않는다.

## 폼 값과 파일 매개변수

### 강사님 코드

출처: `teacher/workspace_python/04_fileupload/api.py` 15–22행 · **원본 발췌**

```python
@app.post('/upload')
async def upload(
    # title = Form(...),    # ... : 명시적으로 필수 값 표시
    title = Form(),         # ...은 생략 가능하다
    content = Form(None),    # None : 필수 아님
    # file1 = Form(None) # 알아서 잘 들어오긴 하지만...
    file1: UploadFile = File(None), # 파일 전용
    file2: list[UploadFile] = File(None) # 파일 여러개
```

### 내 코드

출처: `me/workspace_python/04_fileupload/api.py` 18–24행 · **원본 발췌**

```python
@app.post('/upload')
async def upload(
    # title = Form(...), # '...'을 쓰면 Form에서 필수 값이며 평시엔 생략되어 보임
    title = Form(),
    content = Form(None), # 'None'은 필수값이 아니기에 없어도 된다
    file1 : UploadFile = File(), # Form() 으로도 가능하지만, UploadFile로 받아주는게 좋음
    file2 : list[UploadFile] = File() # type=file이 'multiple'일 때 list로 받을 수 있음
```

`title`·`content`는 `Form()`으로, 파일은 `UploadFile`과 `File()`로 받는다. 여러 파일은 `list[UploadFile]`로 받는다. **차이:** 강사님은 `file1`, `file2`에 `File(None)`을 써서 누락을 허용하고, 나는 `File()`을 써서 필수로 받는다. 그러나 강사님 함수 본문은 곧바로 `file1.filename`에 접근하고 `file2`를 순회한다. 파일이 실제로 빠지면 `None` 처리 없이 오류가 날 수 있으므로 선택 입력으로 완성된 예제가 아니다.

## 이름을 붙이고 바이너리로 저장

### 강사님 코드

출처: `teacher/workspace_python/04_fileupload/api.py` 37–60행 · **원본 발췌**

```python

    print('uuid.uuid4 : ', uuid.uuid4())
    filename_safe = f'{uuid.uuid4().hex}_{filename_orig}'
    

    # 경로 합치기
    # "/" : Path가 지정한 결합 연산자
    target_path = dir / filename_safe
    # w : 쓰기
    # b : binary 즉 파일 그 자체
    # with open(target, 'wb') as buffer :
    with target_path.open('wb') as buffer :
        # buffer.write를 사용해도 되지만 큰 파일의 경우 메모리 등의 문제가 있다

        # buffer.write(file1.read())

        # while True :
        #     chunk = await file1.read(8 * 1024)
        #     if not chunk :
        #         break
        #     buffer.write(chunk)

        # shutil.copyfileobj는 조금씩 쪼개서 안전하고 효율적으로 저장할 수 있다
        shutil.copyfileobj(file1.file, buffer)
```

### 내 코드

출처: `me/workspace_python/04_fileupload/api.py` 40–55행 · **원본 발췌**

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

원래 파일 이름 앞에 UUID를 붙여 같은 이름의 업로드가 충돌할 가능성을 줄인다. `Path`의 `/`로 저장 경로를 만들고 `open('wb')`로 바이너리 파일을 연다. `shutil.copyfileobj(file1.file, buffer)`가 업로드 파일 객체의 내용을 저장 파일로 복사한다. 내 코드의 ‘조금씩 쪼개서 안전’이라는 주석은 복사 방식을 설명하려는 것이지, 파일 크기·보안 제한까지 구현했다는 뜻은 아니다.

## 여러 파일과 다운로드

### 강사님 코드

출처: `teacher/workspace_python/04_fileupload/api.py` 63–82행 · **원본 발췌**

```python
    # file2 처리
    for f in file2 :
        print(f.filename)


@app.get('/download')
def download(file_name) :
    file_path = dir / file_name

    if not file_path.exists() :
        raise HTTPException(
            status_code=404,
            detail="파일을 찾을 수 없습니다"
        )

    return FileResponse(
        path=file_path, 
        filename=file_name, 
        # filename='a.txt', 
        media_type='application/octet-stream')
```

### 내 코드

출처: `me/workspace_python/04_fileupload/api.py` 57–79행 · **원본 발췌**

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

두 코드 모두 `file2`의 이름만 출력한다. **두 번째 파일 목록은 저장하지 않는다.** 다운로드에서는 요청의 `file_name`으로 경로를 만들고, 파일이 없으면 404를 발생시키며 있으면 `FileResponse`를 반환한다. 따라서 저장한 이름(UUID가 붙은 이름)을 알아야 그 파일을 요청할 수 있다.

## 직접 확인할 질문

1. `File(None)`과 `File()`의 입력 누락 동작은 어떻게 다른가?
2. `file2`의 각 파일은 실제로 디스크에 저장되는가?
3. 업로드 때 만든 `filename_safe`와 다운로드의 `file_name`은 어떻게 연결해야 하는가?

## 추가로 알면 좋은 것

원본의 다운로드 경로는 전달받은 이름을 그대로 `dir / file_name`에 붙인다. 실서비스에서는 허용한 파일만 내려주도록 이름과 경로를 검증해야 한다. 업로드 크기·형식 제한과 저장 후 목록 관리도 이 수업 파일에는 없다.

**이 장을 읽은 뒤:** [장별 연습문제 풀기](실습/연습문제/08_FastAPI_파일업로드_다운로드_연습문제.md) → [09. 쿠키와 세션](09_FastAPI_Cookie_Session_로그인.md)
