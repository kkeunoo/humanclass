from passlib.context import CryptContext

ctx_pw = CryptContext(
    schemes=['argon2'],
    deprecated='auto'
)

pw = 'abcd1234'

# argon2 암호화 방식(단방향)
def crypt(txt) :
    return ctx_pw.hash(txt)

# print(crypt(pw))

hashed = crypt(pw)
print( hashed )

# 암호화 된 대상 비교
def verify(orig, hashed) :
    return ctx_pw.verify(orig, hashed)

print(1, verify(pw, hashed) )
print(2, verify('abcd1235', hashed) )
    