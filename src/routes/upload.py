"upload routes module"
import uuid
import json
import shutil
from typing import List
from fastapi import APIRouter
from fastapi import File, UploadFile
from src.functions import encryptFilename, moveFile, factory

from src.database.database_function import exec
from src.database.queries import query_select

upload_route = APIRouter(prefix='/upload', tags=['upload'])

@upload_route.post('/single/file')
def uploadSingleFile(file: UploadFile = File(...)):
    filename = f'{encryptFilename(file.filename)}'
    with open(filename, 'wb') as buffer:
        shutil.copyfileobj(file.file, buffer)
        moveFile(filename)
        
    newData = {
        "id" : f'{uuid.uuid4()}',
        "screen": "home",
        "filename" : filename
    }
        
    return { json.dumps(newData) }


@upload_route.post('/multiple/file')
def uploadMultipleFile(files: List[UploadFile] = File(...)):
    newData = []
    for file in files:
        filename = f'{encryptFilename(file.filename)}'
        with open(filename, 'wb') as buffer:
            shutil.copyfileobj(file.file, buffer)
            moveFile(filename)
            
            newData.append(json.dumps({ "id": f'{uuid.uuid4()}', "screen": "cronograma", "filename" : filename }))
            
    return { json.dumps(newData) }

@upload_route.get('/all/files')
def getAllFiles():    
    return { json.dumps(factory(exec(query_select, None)[0])) }