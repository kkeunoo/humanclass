def minus(x, y):
    return x - y
def show_numbers(*values):
    print(values, type(values))
def info(age, name):
    print(age, name)
def show_keywords(**values):
    for key, value in values.items():
        print(key, value)
def greet(name, address='비공개'):
    print(name, address)
print(minus(5, 2))
print(minus(y=5, x=2))
numbers = [1, 2, 3]
show_numbers(*numbers)
show_numbers()
profile = {'name': '민지', 'age': 20}
info(*profile)
info(**profile)
show_keywords(**profile)
greet('민지')
greet('민지', '서울')
