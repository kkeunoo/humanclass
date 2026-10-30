for table in range(2, 4):
    for number in range(1, 4):
        print(f'{table}x{number}={table * number}', end=' ')
    print()
height = 3
for line in range(1, height + 1):
    print(' ' * (height - line) + '*' * (line * 2 - 1))
for number in range(1, 7):
    if number % 3 == 0 and number % 5 == 0:
        print('FizzBuzz', end=' ')
    elif number % 3 == 0:
        print('Fizz', end=' ')
    elif number % 5 == 0:
        print('Buzz', end=' ')
    else:
        print(number, end=' ')
print()
