a = [1, 2]
b = a
b.append(3)
print(a, b, a is b)
c = a.copy()
c[0] = 100
print(a, c, a is c)
same_values = a.copy()
print(a == same_values, a is same_values)
colors = ['빨강', '파랑']
for number, value in enumerate(colors, start=100):
    print(number, value)
by_loop = []
for number in range(6):
    if number % 2 == 0:
        by_loop.append(number * 2)
by_expression = [number * 2 for number in range(6) if number % 2 == 0]
print(by_loop)
print(by_expression)
print(list(map(int, [1.2, -3.5])))
matrix = [[10, 20], [30, 40], [50, 60]]
print(len(matrix), matrix[1][0])
print([0] * 4)
