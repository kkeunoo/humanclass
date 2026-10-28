# 12-02 Python 클래스속성과 메서드 — 연습문제

[원본 비교 본문](../../12-02_Python_클래스속성과_메서드.md) · [연습문제 목차](README.md)

**새로 구성한 복습 문제**다. 강사님이 낸 원본 문제나 내 당시 풀이가 아니다. 본문에서 강사님 코드와 내 코드를 먼저 읽고, 결과를 예상한 다음 답을 펼친다.

## 문제

다음 코드에서 `a.name`, `b.name`, `a.kind`, `b.kind`를 예상하자. `a.name`만 새 값으로 바꾼 뒤 다른 객체의 이름도 달라지는가?

```python
class Person:
    kind = '사람'
    def __init__(self, name):
        self.name = name

a = Person('봄')
b = Person('여름')
```

<details>
<summary>정답과 확인할 점</summary>

`a.name`은 `'봄'`, `b.name`은 `'여름'`이다. `a.kind`와 `b.kind`는 모두 클래스에 정의된 `'사람'`을 읽는다. `a.name = '가을'`로 바꿔도 `b.name`은 `'여름'`이다. 강사님·내 원본의 **클래스 속성과 인스턴스 속성**을 같은 기준으로 분리해 보자.


</details>

