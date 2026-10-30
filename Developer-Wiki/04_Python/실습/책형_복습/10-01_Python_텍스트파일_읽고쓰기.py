with open('book_text.txt', 'w', encoding='utf-8') as file:
    written = file.write('가나다라')
print('쓴 문자', written)
with open('book_text.txt', 'r', encoding='utf-8') as file:
    print('첫 읽기', file.read(2))
    print('다음 읽기', file.read(2))
    print('끝 [' + file.read(2) + ']')
with open('book_text.txt', 'a', encoding='utf-8') as file:
    file.write('\n마')
with open('book_text.txt', 'r', encoding='utf-8') as file:
    text = ''
    while True:
        chunk = file.read(2)
        if not chunk:
            break
        text += chunk
print(text)
print(type(text))
