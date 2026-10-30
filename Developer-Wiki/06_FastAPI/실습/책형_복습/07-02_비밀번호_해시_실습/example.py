from hash_tools import crypt, verify

saved_hash = crypt('연습용문자')
another_hash = crypt('연습용문자')
print(verify('연습용문자', saved_hash))
print(verify('다른문자', saved_hash))
print(verify('연습용문자', another_hash))
