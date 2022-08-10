from typing import List
import os
from fastapi import FastAPI,UploadFile,File
import shutil

app = FastAPI()

@app.post("/")
async def root(file: UploadFile = File(...)):
    with open(f'{file.filename}',"wb") as buffer:
        shutil.copyfileobj(file.file, buffer)


    return {"file_name": file.file_name}

#이미지만 가능!
@app.post("/img")
async def upload_image(files: List[UploadFile] = File(...)):
    for img in files:
        with open(f'{img.filename}',"wb") as buffer:
            shutil.copyfileobj(img.file, buffer)

    return {"file_name": "Good"}


#모든 파일 종류 다올릴수있다!
@app.post("/uploadfiles")
async def upload_all_files(files: List[UploadFile] = File(...)):
    UPLOAD_DIRECTORY = "./tmp"
    for file in files:
        contents = await file.read()
        with open(os.path.join(UPLOAD_DIRECTORY, file.filename), "wb") as fp:
            fp.write(contents)
        print(file.filename)


