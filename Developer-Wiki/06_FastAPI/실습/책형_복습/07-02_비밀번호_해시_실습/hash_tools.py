from passlib.context import CryptContext

ctx_pw = CryptContext(schemes=['argon2'], deprecated='auto')

def crypt(text):
    return ctx_pw.hash(text)

def verify(original, hashed):
    return ctx_pw.verify(original, hashed)
