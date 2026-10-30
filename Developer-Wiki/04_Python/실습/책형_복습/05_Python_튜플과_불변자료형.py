empty = ()
single_number = (3)
single_tuple = (3,)
point = 10, 20
print(empty, type(empty))
print(single_number, type(single_number))
print(single_tuple, type(single_tuple))
print(point[0], point[1])
values = [1, 2, 3]
converted = tuple(values)
print(converted, type(values))
editable = list(converted)
editable[0] = 100
print(converted, editable)
point = (30, 40)
print(point)
