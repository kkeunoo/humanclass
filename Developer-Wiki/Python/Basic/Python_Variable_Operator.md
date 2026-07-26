---
title: Python 변수와 연산
category: Python
last_updated: 2026-07-27
status: Active
---

# Python 변수와 연산


```python
name = 'kim'
age = 20
price = 12000
quantity = 2
print(price * quantity)
```

변수 선언 키워드 없이 이름에 값을 대입한다.

## 연산

```python
print(10 + 3)
print(10 - 3)
print(10 * 3)
print(10 / 3)
print(10 // 3)
print(10 % 3)
print(2 ** 3)
```

- `/`: 실수 나눗셈
- `//`: 몫
- `%`: 나머지
- `**`: 거듭제곱

## 주의사항

문자열과 숫자를 직접 더할 수 없다. `str()` 또는 `int()` 등으로 변환한다.
