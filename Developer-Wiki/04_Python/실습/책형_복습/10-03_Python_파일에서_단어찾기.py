with open('book_words.txt', 'w', encoding='utf-8') as file:
    file.write('Cat, dog, clock. C++!')
found = []
with open('book_words.txt', 'r', encoding='utf-8') as file:
    for word in file.read().split(' '):
        if 'c' in word.lower():
            cleaned = word.replace(',', '').replace('.', '')
            found.append(cleaned)
print(' | '.join(found))
print('개수', len(found))
