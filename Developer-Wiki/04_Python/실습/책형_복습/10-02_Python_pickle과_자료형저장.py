import pickle
numbers = [1, 2]
profile = {'이름': '민지', '나이': 20}
with open('book_values.p', 'wb') as file:
    pickle.dump(numbers, file)
    pickle.dump(profile, file)
with open('book_values.p', 'rb') as file:
    first = pickle.load(file)
    second = pickle.load(file)
print(first, type(first))
print(second, type(second))
print(second['나이'], type(second['나이']))
text = str(numbers)
print(text, type(text))
print(list(text))
