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
