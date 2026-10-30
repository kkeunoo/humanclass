def show_sum(a, b):
    "두 값의 합을 화면에 출력한다."
    print(a + b)
def return_sum(a, b):
    return a + b
def add_sub(a, b):
    return a + b, a - b
def append_four(items):
    items.append(4)
def times_ten(value):
    return value * 10
shown = show_sum(2, 3)
returned = return_sum(2, 3)
print('출력 함수 결과', shown)
print('반환 함수 결과', returned, returned * 2)
pair = add_sub(1, 2)
left, right = pair
print(pair, left, right)
numbers = [1, 2, 3]
changed = append_four(numbers)
print(numbers, changed)
print(times_ten(return_sum(2, 3)))
function_value = return_sum
print(function_value(4, 5))
print(show_sum.__doc__)
