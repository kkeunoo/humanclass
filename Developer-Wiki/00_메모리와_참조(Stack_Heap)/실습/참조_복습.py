"""책의 설명용 새 예제. 같은 폴더의 reference_tools.py와 함께 실행한다."""

from reference_tools import append_in_place, with_added_item

original = [1, 2]
same = original
copied = original.copy()
same.append(3)
copied[0] = 9
print('original:', original)
print('same is original:', same is original)
print('copied:', copied)

numbers = [1, 2]
result = append_in_place(numbers, 3)
print('changed:', numbers)
print('returned:', result)

numbers = [1, 2]
result = with_added_item(numbers, 3)
print('kept:', numbers)
print('new:', result)
