"function module"
import os
import shutil
import datetime
from cryptography.fernet import Fernet


def fileExistsInRoot(filename):
    if os.path.exists(f'./{filename}'):
        return True
    else: 
        return False
    
def removeFileInRoot(filename):
    if fileExistsInRoot(filename):
        os.remove(f'{filename}')
        return True
    else:
        return False
    
def moveFile(filename):
    if fileExistsInRoot(filename):
        shutil.move(f'./{filename}', f'./img/{filename}')
        removeFileInRoot(filename)
        return True
    else:
        return False

def encryptFilename(originalFilename: str):
    print(originalFilename)
    print(originalFilename.split('.')[1])
    
    key = Fernet.generate_key()
    f = Fernet(key)
    
    secretMessage = f'{originalFilename}{datetime.datetime.now()}'
    extensionFile = originalFilename.split('.')[1]
    
    filename = f.encrypt(f'{secretMessage}'.encode()) 

    return f'{filename}.{extensionFile}'

def factory(data: tuple):    
    newDict = []
    for item in data:
        newData = {}
        newData['id'] = item[0]
        newData['screen'] = item[1]
        newData['filename'] = item[2]
        
        newDict.append(newData)
    
    return newDict