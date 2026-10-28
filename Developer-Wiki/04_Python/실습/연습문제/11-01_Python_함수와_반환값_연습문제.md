# 11-01 Python 함수와 반환값 — 연습문제

[원본 비교 본문](../../11-01_Python_함수와_반환값.md) · [연습문제 목차](README.md)

**새로 구성한 복습 문제**다. 강사님이 낸 원본 문제나 내 당시 풀이가 아니다. 본문에서 강사님 코드와 내 코드를 먼저 읽고, 결과를 예상한 다음 답을 펼친다.

## 문제

함수 `add(a,b)`가 안에서 `print(a+b)`만 하면 `result=add(1,2)`의 result는?

<details>
<summary>정답과 확인할 점</summary>

```python
def add(a, b):
    print(a + b)

result = add(1, 2)  # 호출 중 3 출력
print(result)        # None
```

화면에 보인 3은 **함수 안의 출력**이고, 호출 결과로 받은 값은 `None`이다. 뒤 계산에 3을 사용하려면 함수가 `return a + b`를 해야 한다. 강사님·내 원본의 `print`와 `return`도 이 구분으로 읽자.


</details>

