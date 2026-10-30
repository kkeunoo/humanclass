def double(number):
    return number * 2
double_short = lambda number: number * 2
print(double(3), double_short(3))
print(list(map(lambda number: number + 10, [1, 2])))
people = [{'age': 25}, {'age': 23}, {'age': 30}]
people.sort(key=lambda person: person['age'])
print([person['age'] for person in people])
x = 10
def local_example():
    x = 20
    print('지역', x)
local_example()
print('밖', x)
def change_global():
    global x
    x = 20
change_global()
print('변경 뒤', x)
def outer():
    x = 10
    y = 20
    def middle():
        x = 30
        def inner():
            nonlocal x, y
            print('가까운 x', x)
            print('찾은 y', y)
        inner()
    middle()
outer()
