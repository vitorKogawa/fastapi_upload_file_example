"upload routes module"
import uuid
import json
from aiofiles import open
from typing import List
from fastapi import APIRouter
from fastapi import File, UploadFile
from src.functions import encryptFilename, factory, path

from src.database.database_function import exec
from src.database.queries import query_select

upload_route = APIRouter(prefix='/upload', tags=['upload'])

@upload_route.post('/single/file')
async def uploadSingleFile(file: UploadFile = File(...)):
    print(file.filename)
    
    return { 'teste' : 'teste' }
    # filename = f'{encryptFilename(file.filename)}'
    # destination_file_path = path(f'../img/{filename}')
    # async with open(destination_file_path, 'wb') as buffer:
    #     while content := await file.read(1024):
    #         await buffer.write(content)
            
    # newData = {
    #     'id': f'{uuid.uuid4()}',
    #     'screen': 'home',
    #     'filename': filename
    # }
    
    # return { json.dumps(newData) }


@upload_route.post('/multiple/file')
async def uploadMultipleFile(files: List[UploadFile] = File(...)):
    print(files)
    
    for file in files:
        print(file.file)
    
    return { 'chegou' : 'ihuuuul!!!' }
    # newData = []
    # for file in files:
    #     filename = f'{encryptFilename(file.filename)}'
    #     destination_file_path = path(f'../img/{filename}')
    #     async with open(destination_file_path, 'wb') as buffer:
    #         while content := await file.read(1024):
    #             await buffer.write(content)
            
    #     newData.append(json.dumps({ "id": f'{uuid.uuid4()}', "screen": "cronograma", "filename" : filename }))
            
    # return { json.dumps(newData) }

@upload_route.get('/all/files')
def getAllFiles():    
    return { json.dumps(factory(exec(query_select, None)[0])) }