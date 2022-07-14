"function module"
import os
import shutil
import datetime
from cryptography.fernet import Fernet


def path(filepath): 
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), filepath)

def encryptFilename(originalFilename: str):
    print(originalFilename)
    
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