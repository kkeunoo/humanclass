#pip install fastapi python-multipart uvicorn

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

# 첨부파일 Upload
@app.post('/upload')
async def upload(
    # title = Form(...), # '...'을 쓰면 Form에서 필수 값이며 평시엔 생략되어 보임
    title = Form(),
    content = Form(None), # 'None'은 필수값이 아니기에 없어도 된다
    file1 : UploadFile = File(), # Form() 으로도 가능하지만, UploadFile로 받아주는게 좋음
    file2 : list[UploadFile] = File() # type=file이 'multiple'일 때 list로 받을 수 있음
):
    print('title : ',title)
    print('content : ',content)

    print('filename : ', file1.filename)
    print('filesize : ', file1.size) # Byte단위

    filename_orig = file1.filename

    # 아래처럼 filename에 시간을 붙여 같은 파일이 들어가도 이름이 바뀌어
    # 연속으로 저장되게 할 수 있음
    # print('now', datetime.now())
    # # 년월일_시간분초_마이크로초
    # t = datetime.now().strftime('%Y%m%d_%H%M%S_%f')
    # filename_safe = f'{t}_{filename_orig}'

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

if __name__ == '__main__' :
    import uvicorn
    uvicorn.run('api:app', port=8000, reload=True, host="0.0.0.0")