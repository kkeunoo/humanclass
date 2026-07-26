---
title: Python List와 range
category: Python
last_updated: 2026-07-27
status: Active
---

# Python List와 range


```python
numbers = [1, 2, 3]
numbers.append(4)
print(numbers[0])
```

## 반복

```python
for number in numbers:
    print(number)

for i in range(1, 6):
    print(i)
```

`range(1, 6)`은 1부터 5까지 만든다. 끝 값은 포함하지 않는다.

## 슬라이싱

```python
print(numbers[1:3])
```

## 주의사항

`list.sort()`는 원본을 변경하고 반환값은 None이다.
