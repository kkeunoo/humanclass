# 00-02 Python 오류와 예외 — 연습문제

[원본 비교 본문](../../00-02_Python_오류와_예외.md) · [연습문제 목차](README.md)

**새로 구성한 복습 문제**다. 강사님이 낸 원본 문제나 내 당시 풀이가 아니다. 본문에서 강사님 코드와 내 코드를 먼저 읽고, 결과를 예상한 다음 답을 펼친다.

## 문제

다음 코드에서 어떤 글자가 출력되는가? 오류가 난 줄 뒤의 `print('끝')`도 실행되는지 예상하자.

```python
try:
    print(10 / 0)
    print('끝')
except ZeroDivisionError:
    print('0으로 나눌 수 없음')
```

<details>
<summary>정답과 확인할 점</summary>

`10 / 0`에서 `ZeroDivisionError`가 나므로 숫자는 출력되지 않는다. 같은 `try` 블록의 `print('끝')`도 건너뛰고, `except`의 `0으로 나눌 수 없음`만 출력된다. 수업 원본에서도 **어디서 멈췄는지**를 먼저 찾는다.


</details>

