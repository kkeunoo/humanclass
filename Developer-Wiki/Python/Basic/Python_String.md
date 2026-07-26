---
title: Python 문자열
category: Python
last_updated: 2026-07-27
status: Active
---

# Python 문자열


```python
text = 'Python Study'
print(text[0])
print(text[0:6])
print(len(text))
```

## 자주 사용하는 기능

```python
print(text.lower())
print(text.upper())
print(text.replace('Study', 'Class'))
print(text.split(' '))
```

## f-string

```python
name = '홍길동'
age = 20
print(f'{name}님의 나이는 {age}세입니다.')
```

## 주의사항

인덱스는 0부터 시작하며 범위를 벗어나면 오류가 발생한다.
