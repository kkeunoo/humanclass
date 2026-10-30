values = list(range(10))
print(values[1:4])
print(values[1:9:2])
print(values[7:3])
print(values[7:3:-1])
print(values[-4:-2])
print(values[4:100])
piece = values[2:5]
piece[0] = 100
print(values[2], piece)
values[2:5] = [10, 20, 30, 40, 50]
print(values, len(values))
word = '안녕'
encoded = word.encode('utf-8')
print(len(word), len(encoded))
print('hello'[::-1])
ko = ['책', '알약']
en = ['book', 'pill']
view = ko
view = en
print(view[0])
