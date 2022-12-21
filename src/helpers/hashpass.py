import hashlib

def getHashed(text):
    salt = "ITSASECRET"
    hashed = text + salt 
    hashed = hashlib.md5(hashed.encode())
    hashed = hashed.hexdigest()
    return hashed 