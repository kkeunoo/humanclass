---
title: "Python List와 range"
area: "Python"
version: "v4.3"
last_updated: "2026-07-27"
difficulty: "★★★☆☆☆"
estimated_time: "40~60분"
---

# Python List와 range

## 학습 목표

- 리스트에 여러 값을 저장하고 for와 range로 반복한다.
- 터미널 또는 Python 실행 환경에서 직접 결과를 확인한다.
- 오류 메시지의 줄 번호와 원인을 확인한다.

## 왜 배우는가

Python은 데이터를 저장하고 처리하는 문법을 간결하게 표현합니다. 직접 실행하고 출력 결과를 확인하는 과정이 개념 이해의 핵심입니다.

## 기본 개념

```python
fruits = ['사과', '바나나', '포도']
fruits.append('딸기')

for fruit in fruits:
    print(fruit)

for number in range(1, 6):
    print(number)
```

## 수업 예제

예제를 실행한 뒤 변수의 값이나 코드 일부를 한 번에 하나씩 바꾸고 결과 차이를 확인합니다.

## 수업 문제

### 문제

과일 리스트를 한 줄씩 출력하고 1부터 5까지 숫자를 출력하세요.

### 요구사항

- for문을 두 번 사용합니다.
- 리스트의 모든 값을 출력합니다.
- `range(1, 6)`을 사용합니다.

### 직접 풀어 보기

해설을 열기 전에 실행 결과를 먼저 예상하고 코드를 작성합니다.

<details>
<summary>해설 보기</summary>

```python
fruits = ['사과', '바나나', '포도']

for fruit in fruits:
    print(fruit)

for number in range(1, 6):
    print(number)
```

### 풀이 설명

현재 문서까지 배운 문법만 사용했습니다. 코드를 위에서 아래로 읽으며 각 변수와 출력문의 역할을 확인합니다.

</details>

## 자주 하는 실수

- range의 끝값도 포함된다고 생각하는 경우
- for문 본문의 들여쓰기를 맞추지 않는 경우
- 리스트 인덱스를 범위 밖으로 사용하는 경우

## 실무 연결

여러 데이터를 순서대로 저장하고 같은 작업을 반복 적용할 때 사용합니다.

## 📌 더 알아보기

### sort()의 반환값

```python
numbers = [3, 1, 2]
result = numbers.sort()

print(numbers)
print(result)  # None
```

`sort()`는 원본 리스트를 정렬하며 정렬된 새 리스트를 반환하지 않습니다.

## 직접 해보기

- 변수값이나 문자열을 변경하고 결과를 예상한다.
- `print()`와 `type()`으로 값과 자료형을 확인한다.
- 오류를 한 번 직접 만들고 메시지와 줄 번호를 읽는다.

## Check Point

- [ ] 리스트에 값을 추가하고 읽을 수 있다.
- [ ] for문으로 리스트를 반복할 수 있다.
- [ ] range의 시작·끝 규칙을 설명할 수 있다.

## 최종 요약

리스트에 여러 값을 저장하고 for와 range로 반복한다.

## 복습 기록

- [ ] 예제를 직접 실행했다.
- [ ] 문제를 해설 없이 풀었다.
- [ ] 오류 메시지를 읽고 수정했다.

## 이전 · 다음 학습

| 구분 | 문서 |
|---|---|
| 이전 학습 | [Python 문자열](Python_String.md) |
| 다음 학습 | [Python Tuple](Python_Tuple.md) |
