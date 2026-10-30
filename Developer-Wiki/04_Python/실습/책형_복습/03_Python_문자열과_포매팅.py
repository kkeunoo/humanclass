temperature = 32.5
print('온도: ' + str(temperature))
print(f'온도: {temperature:.1f}')
text = '_hello'
changed = text.replace('l', 'w')
print(text, changed)
print(text.find('l'), text.rfind('l'), text.find('z'))
parts = 'a-b-c'.split('-')
print(parts)
print('/'.join(parts))
phrase = '  a b  '
print('[' + phrase.strip() + ']')
print('[' + phrase.strip().replace(' ', '') + ']')
print('Back'.upper().find('back'.upper()))
print('35'.zfill(4), '35000'.zfill(4))
number = 7
print(f'..{number:>3}..')
print(f'{3.14:08.3f}')
print(f'{15000:,}')
