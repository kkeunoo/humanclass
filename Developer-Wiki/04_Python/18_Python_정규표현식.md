---
title: Python 정규표현식
version: v2.0-final
last_updated: 2026-08-06
status: Completed
---

# Python 정규표현식

## 문서 정보

| 항목 | 내용 |
| --- | --- |
| 문서 | `18_Python_정규표현식.md` |
| 분류 | `04_Python` |
| 권장 선수 학습 | `03_Python_문자열.md`, `08_Python_조건문.md`, `09_Python_반복문.md`, `11_Python_함수.md` |
| 다음 학습 | `19_Python_실무_코딩스타일.md` |
| 문서 성격 | Python 확장 학습 문서 |
| 핵심 범위 | 정규표현식, 메타문자, 문자 클래스, 수량자, 그룹, 앵커, 이스케이프, `re` 모듈 |
| 실습 범위 | 문자열 검색, 형식 검사, 데이터 추출, 문자열 치환, 전화번호·이메일·로그 패턴 |
| 종합 실습 | 별도 문서 `20_Python_종합실습.md`에서 관리 |
| 문서 형식 | Python Developer-Wiki V2 확정 형식 |

> 정규표현식은 문자열 패턴을 검색·검사·추출·치환하기 위한 문법이다.  
> 이 문서는 패턴을 외우는 것보다, **각 기호가 문자열에서 어떤 역할을 하는지 읽는 방법**에 집중한다.

---

# 개요

문자열에서 특정 값을 찾는 일은 자주 발생한다.

예:

- 이메일 형식인지 확인
- 전화번호 찾기
- 숫자만 추출
- 여러 공백을 하나로 변경
- 로그에서 날짜와 상태 코드 추출
- 특정 단어가 포함된 줄 찾기

일반 문자열 메서드로도 일부 작업은 가능하다.

```python
text = "문의 전화: 010-1234-5678"

print("010" in text)
```

하지만 패턴이 복잡해지면 조건문과 반복문이 길어질 수 있다.

```text
숫자 3자리
-
숫자 4자리
-
숫자 4자리
```

정규표현식을 사용하면 이 구조를 하나의 패턴으로 표현할 수 있다.

```python
r"\d{3}-\d{4}-\d{4}"
```

```text
\d{3}
→ 숫자 3개

-
→ 하이픈 문자

\d{4}
→ 숫자 4개
```

> [!IMPORTANT]
> 정규표현식은 문자열 자체가 아니라 **문자열의 형식과 규칙**을 표현한다.

---

# 핵심 개념

| 개념 | 핵심 역할 |
| --- | --- |
| 정규표현식 | 문자열 패턴을 표현하는 문법 |
| 패턴 | 찾거나 검사할 문자열 규칙 |
| 메타문자 | 특별한 의미를 가지는 기호 |
| 문자 클래스 | 특정 문자 종류나 범위를 표현 |
| 수량자 | 앞 패턴의 반복 횟수를 표현 |
| 그룹 | 여러 패턴을 하나의 단위로 묶음 |
| 앵커 | 문자열의 시작·끝 위치를 지정 |
| 캡처 | 그룹에 일치한 문자열을 저장 |
| 원시 문자열 | 백슬래시를 편하게 작성하는 `r"..."` 문자열 |
| `re` 모듈 | Python 정규표현식 기능을 제공하는 표준 라이브러리 |

---

# 학습 목표

이 문서를 학습한 뒤 다음 내용을 설명하고 작성할 수 있어야 한다.

- 정규표현식이 필요한 상황을 설명할 수 있다.
- `re` 모듈을 import하여 사용할 수 있다.
- 원시 문자열 `r"..."`을 사용하는 이유를 이해한다.
- `.`·`\d`·`\w`·`\s` 같은 기본 메타문자를 읽을 수 있다.
- `[]` 문자 클래스와 범위를 작성할 수 있다.
- `*`, `+`, `?`, `{m,n}` 수량자의 차이를 설명할 수 있다.
- `^`와 `$`로 문자열 전체 형식을 검사할 수 있다.
- `()` 그룹과 `|` 선택 패턴을 사용할 수 있다.
- `search()`, `match()`, `fullmatch()`의 차이를 구분할 수 있다.
- `findall()`과 `finditer()`로 여러 결과를 추출할 수 있다.
- `sub()`로 문자열을 치환할 수 있다.
- `split()`으로 패턴 기준 문자열 분리가 가능함을 이해한다.
- 캡처 그룹과 비캡처 그룹을 구분할 수 있다.
- 탐욕적·비탐욕적 수량자의 차이를 이해한다.
- 정규표현식을 과도하게 사용하면 가독성이 떨어질 수 있음을 안다.
- 입력 검증에서 정규표현식만으로 완전한 유효성을 보장할 수 없음을 이해한다.

---

# 1. `re` 모듈

Python에서는 표준 라이브러리 `re` 모듈을 사용한다.

```python
import re
```

기본 흐름:

```text
패턴 작성
    ↓
문자열 전달
    ↓
re 함수 실행
    ↓
일치 결과 확인
```

예:

```python
import re


text = "Python 3.12"
match = re.search(r"\d+", text)

print(match.group())
```

출력:

```text
3
```

`\d+`는 숫자가 하나 이상 이어진 패턴을 의미한다.

---

# 2. 원시 문자열 `r"..."`

정규표현식에서는 백슬래시(`\`)를 자주 사용한다.

```python
r"\d+"
```

`r`이 붙은 문자열을 원시 문자열이라고 한다.

## 2-1. 일반 문자열

```python
pattern = "\\d+"
```

백슬래시를 두 번 작성해야 한다.

## 2-2. 원시 문자열

```python
pattern = r"\d+"
```

정규표현식 패턴을 읽기 쉽게 작성할 수 있다.

## 2-3. 왜 사용할까?

Python 문자열과 정규표현식 모두 백슬래시를 특별하게 해석할 수 있다.

원시 문자열을 사용하면 Python 문자열 단계의 이스케이프 처리를 줄일 수 있다.

> [!IMPORTANT]
> 정규표현식 패턴은 특별한 이유가 없다면 `r"..."` 형태로 작성하는 것이 일반적이다.

---

# 3. 일반 문자 일치

정규표현식의 일반 문자는 같은 문자와 일치한다.

```python
import re


text = "I like Python"
match = re.search(r"Python", text)

print(match.group())
```

출력:

```text
Python
```

## 3-1. 일치하지 않는 경우

```python
match = re.search(r"Java", text)

print(match)
```

출력:

```text
None
```

> [!TIP]
> 정규표현식 함수는 일치 결과가 없을 때 `None`을 반환하는 경우가 많으므로 사용 전 확인해야 한다.

---

# 4. `.` 메타문자

`.`은 일반적으로 줄바꿈을 제외한 임의의 문자 하나와 일치한다.

```python
import re


print(re.search(r"c.t", "cat").group())
print(re.search(r"c.t", "cut").group())
```

출력:

```text
cat
cut
```

```text
c
→ 문자 c

.
→ 임의의 문자 하나

t
→ 문자 t
```

## 4-1. 실제 점과 일치하려면

`.` 자체를 찾으려면 이스케이프한다.

```python
pattern = r"\."
```

예:

```python
text = "Python 3.12"

print(re.search(r"\.", text).group())
```

출력:

```text
.
```

> [!WARNING]
> `.`은 일반 점 문자가 아니라 특별한 의미를 가진 메타문자다.
>
> 실제 점을 찾으려면 `\.`을 사용한다.

---

# 5. 숫자 패턴 `\d`

`\d`는 숫자 한 글자와 일치한다.

```python
import re


text = "Room 7"

print(re.search(r"\d", text).group())
```

출력:

```text
7
```

숫자가 여러 개 이어진 경우:

```python
text = "Order 20260806"

print(re.search(r"\d+", text).group())
```

출력:

```text
20260806
```

## 5-1. 반대 패턴 `\D`

`\D`는 숫자가 아닌 문자 하나와 일치한다.

```python
print(re.search(r"\D", "123A").group())
```

출력:

```text
A
```

---

# 6. 단어 문자 `\w`

`\w`는 일반적으로 문자, 숫자, 밑줄과 일치한다.

```python
text = "user_01"

print(re.findall(r"\w", text))
```

출력:

```text
['u', 's', 'e', 'r', '_', '0', '1']
```

`\w+`를 사용하면 연속된 단어 문자를 가져온다.

```python
text = "user_01 logged in"

print(re.findall(r"\w+", text))
```

출력:

```text
['user_01', 'logged', 'in']
```

## 6-1. 반대 패턴 `\W`

`\W`는 단어 문자가 아닌 문자와 일치한다.

```python
print(re.findall(r"\W", "user_01!"))
```

출력:

```text
['!']
```

> [!TIP]
> Unicode 문자열에서는 `\w`가 영문자뿐 아니라 한글 같은 문자도 포함할 수 있다.
>
> 영문자만 필요하다면 `[A-Za-z]`처럼 범위를 명시한다.

---

# 7. 공백 문자 `\s`

`\s`는 공백, 탭, 줄바꿈 같은 공백 문자와 일치한다.

```python
text = "Python\tJava\nSQL"

print(re.findall(r"\s", text))
```

출력 형태:

```text
['\t', '\n']
```

`\s+`는 연속된 공백을 찾을 때 사용할 수 있다.

```python
text = "Python     Java"

result = re.sub(r"\s+", " ", text)

print(result)
```

출력:

```text
Python Java
```

## 7-1. 반대 패턴 `\S`

`\S`는 공백이 아닌 문자와 일치한다.

---

# 8. 문자 클래스 `[]`

대괄호 안에 여러 문자를 작성하면 그중 한 문자와 일치한다.

```python
pattern = r"[abc]"
```

```text
a 또는 b 또는 c
```

실행:

```python
text = "cat bat dog"

print(re.findall(r"[abc]", text))
```

출력:

```text
['c', 'a', 'b', 'a']
```

---

# 9. 문자 범위

하이픈을 사용해 문자 범위를 표현할 수 있다.

```text
[a-z]
→ 영문 소문자 한 글자

[A-Z]
→ 영문 대문자 한 글자

[0-9]
→ 숫자 한 글자

[가-힣]
→ 한글 완성형 한 글자
```

예:

```python
text = "Python 파이썬 123"

print(re.findall(r"[A-Za-z]+", text))
print(re.findall(r"[가-힣]+", text))
print(re.findall(r"[0-9]+", text))
```

출력:

```text
['Python']
['파이썬']
['123']
```

> [!IMPORTANT]
> 문자 클래스 안의 `-`는 범위를 의미할 수 있다.
>
> 실제 하이픈을 찾으려면 맨 앞이나 맨 뒤에 두거나 `\-`로 이스케이프한다.

---

# 10. 부정 문자 클래스 `[^...]`

문자 클래스 안에서 첫 번째 `^`는 해당 문자를 제외한다는 의미다.

```python
pattern = r"[^0-9]"
```

숫자가 아닌 문자와 일치한다.

```python
text = "A1-B2"

print(re.findall(r"[^0-9]", text))
```

출력:

```text
['A', '-', 'B']
```

> [!WARNING]
> `^`는 위치에 따라 의미가 다르다.
>
> 문자 클래스 밖에서는 문자열 시작, 문자 클래스 첫 위치에서는 제외를 의미한다.

---

# 11. 수량자 `*`

`*`는 앞 패턴이 0회 이상 반복되는 경우와 일치한다.

```python
pattern = r"ab*"
```

일치 예:

```text
a
ab
abb
abbb
```

실행:

```python
text = "a ab abb"

print(re.findall(r"ab*", text))
```

출력:

```text
['a', 'ab', 'abb']
```

> [!TIP]
> `*`는 0회도 허용하므로 앞 문자가 없어도 일치할 수 있다.

---

# 12. 수량자 `+`

`+`는 앞 패턴이 1회 이상 반복되는 경우와 일치한다.

```python
pattern = r"ab+"
```

일치 예:

```text
ab
abb
abbb
```

`a`만 있는 경우는 일치하지 않는다.

```python
text = "a ab abb"

print(re.findall(r"ab+", text))
```

출력:

```text
['ab', 'abb']
```

---

# 13. 수량자 `?`

`?`는 앞 패턴이 0회 또는 1회 나타나는 경우와 일치한다.

```python
pattern = r"colou?r"
```

다음 두 문자열과 모두 일치한다.

```text
color
colour
```

실행:

```python
text = "color colour"

print(re.findall(r"colou?r", text))
```

출력:

```text
['color', 'colour']
```

---

# 14. 정확한 반복 횟수 `{n}`

```python
pattern = r"\d{3}"
```

숫자 3개와 일치한다.

```python
text = "123 45 6789"

print(re.findall(r"\d{3}", text))
```

출력:

```text
['123', '678']
```

`6789`에서 앞의 세 자리 `678`이 일치한다.

문자열 전체가 정확히 세 자리인지 확인하려면 `fullmatch()`를 사용한다.

```python
print(re.fullmatch(r"\d{3}", "123"))
print(re.fullmatch(r"\d{3}", "1234"))
```

---

# 15. 반복 범위 `{m,n}`

```text
{m,n}
→ 최소 m회, 최대 n회
```

예:

```python
pattern = r"\d{2,4}"
```

숫자 2개부터 4개까지 일치한다.

```python
text = "1 12 123 1234 12345"

print(re.findall(r"\d{2,4}", text))
```

출력:

```text
['12', '123', '1234', '1234']
```

`12345`에서는 최대 4자리까지 일치한다.

## 15-1. 한쪽 생략

```text
{2,}
→ 2회 이상

{,4}
→ 최대 4회
```

---

# 16. 문자열 시작 `^`

`^`는 문자열 시작 위치와 일치한다.

```python
import re


print(bool(re.search(r"^Python", "Python is easy")))
print(bool(re.search(r"^Python", "I like Python")))
```

출력:

```text
True
False
```

첫 번째 문자열은 `Python`으로 시작하지만 두 번째 문자열은 그렇지 않다.

---

# 17. 문자열 끝 `$`

`$`는 문자열 끝 위치와 일치한다.

```python
print(bool(re.search(r"Python$", "I like Python")))
print(bool(re.search(r"Python$", "Python is easy")))
```

출력:

```text
True
False
```

## 17-1. 전체 형식 검사

```python
pattern = r"^\d{3}-\d{4}-\d{4}$"
```

```text
문자열 시작
숫자 3자리
하이픈
숫자 4자리
하이픈
숫자 4자리
문자열 끝
```

---

# 18. 선택 패턴 `|`

`|`는 여러 패턴 중 하나를 의미한다.

```python
pattern = r"Python|Java|SQL"
```

실행:

```python
text = "Python and SQL"

print(re.findall(pattern, text))
```

출력:

```text
['Python', 'SQL']
```

```text
Python 또는 Java 또는 SQL
```

---

# 19. 그룹 `()`

괄호는 여러 패턴을 하나의 단위로 묶는다.

```python
pattern = r"(ab)+"
```

```text
ab
abab
ababab
```

그룹은 일치한 일부 문자열을 따로 가져올 때도 사용한다.

```python
text = "2026-08-06"
match = re.search(
    r"(\d{4})-(\d{2})-(\d{2})",
    text,
)

print(match.group(1))
print(match.group(2))
print(match.group(3))
```

출력:

```text
2026
08
06
```

## 19-1. 그룹 번호

```text
group(0)
→ 전체 일치 문자열

group(1)
→ 첫 번째 그룹

group(2)
→ 두 번째 그룹
```

---

# 20. 이름 있는 그룹

그룹에 이름을 붙일 수 있다.

```python
pattern = (
    r"(?P<year>\d{4})-"
    r"(?P<month>\d{2})-"
    r"(?P<day>\d{2})"
)
```

실행:

```python
match = re.search(
    pattern,
    "2026-08-06",
)

print(match.group("year"))
print(match.group("month"))
print(match.group("day"))
```

출력:

```text
2026
08
06
```

> [!TIP]
> 그룹이 많아질수록 숫자 번호보다 이름 있는 그룹이 읽기 쉽다.

---

# 21. 비캡처 그룹 `(?:...)`

그룹으로 묶기는 하지만 결과를 따로 저장할 필요가 없을 때 사용한다.

```python
pattern = r"(?:https?|ftp)://"
```

```text
http://
https://
ftp://
```

일반 그룹:

```python
(http|https)
```

비캡처 그룹:

```text
(?:http|https)
```

> [!TIP]
> 단순히 패턴을 묶기 위한 목적이라면 비캡처 그룹을 사용하면 그룹 번호가 불필요하게 늘어나는 것을 막을 수 있다.

---

# 22. `search()`

`search()`는 문자열 전체에서 첫 번째 일치 위치를 찾는다.

```python
import re


text = "Order number: 12345"
match = re.search(r"\d+", text)

print(match.group())
```

출력:

```text
12345
```

문자열 중간에 있어도 찾는다.

---

# 23. `match()`

`match()`는 문자열 시작 위치에서 패턴이 일치하는지 확인한다.

```python
print(re.match(r"Python", "Python is easy"))
print(re.match(r"Python", "I like Python"))
```

첫 번째는 일치 객체, 두 번째는 `None`이다.

## 23-1. `search()`와 비교

```text
match()
→ 문자열 시작에서 검사

search()
→ 문자열 전체에서 검색
```

> [!WARNING]
> `match()`라는 이름 때문에 문자열 전체 일치 검사로 오해하기 쉽다.
>
> 전체 일치는 `fullmatch()`를 사용한다.

---

# 24. `fullmatch()`

`fullmatch()`는 문자열 전체가 패턴과 정확히 일치하는지 검사한다.

```python
pattern = r"\d{3}-\d{4}-\d{4}"

print(bool(re.fullmatch(pattern, "010-1234-5678")))
print(bool(re.fullmatch(pattern, "전화 010-1234-5678")))
```

출력:

```text
True
False
```

## 24-1. 언제 사용할까?

- 전화번호 형식 검사
- 사번 형식 검사
- 날짜 문자열 검사
- 정해진 코드 형식 검사
- 사용자 입력 전체 검증

---

# 25. `findall()`

`findall()`은 일치하는 모든 결과를 리스트로 반환한다.

```python
text = "A12 B34 C56"

numbers = re.findall(r"\d+", text)

print(numbers)
```

출력:

```text
['12', '34', '56']
```

## 25-1. 그룹이 있는 경우 주의

```python
text = "2026-08-06 2026-08-07"

result = re.findall(
    r"(\d{4})-(\d{2})-(\d{2})",
    text,
)

print(result)
```

출력:

```text
[('2026', '08', '06'), ('2026', '08', '07')]
```

캡처 그룹이 있으면 그룹 결과가 반환된다.

전체 문자열 목록이 필요하면 비캡처 그룹을 사용하거나 패턴 구조를 조정한다.

---

# 26. `finditer()`

`finditer()`는 일치 객체를 이터레이터로 반환한다.

```python
text = "A12 B34 C56"

matches = re.finditer(r"\d+", text)

for match in matches:
    print(
        match.group(),
        match.start(),
        match.end(),
    )
```

출력:

```text
12 1 3
34 5 7
56 9 11
```

## 26-1. `findall()`과 비교

| 함수 | 결과 |
| --- | --- |
| `findall()` | 문자열 또는 튜플 리스트 |
| `finditer()` | 일치 객체 이터레이터 |

위치 정보나 그룹 메서드가 필요하면 `finditer()`가 유용하다.

---

# 27. 일치 객체의 주요 메서드

```python
match = re.search(
    r"\d+",
    "Order 12345",
)
```

| 메서드 | 의미 |
| --- | --- |
| `group()` | 일치한 문자열 |
| `start()` | 시작 인덱스 |
| `end()` | 끝 인덱스 |
| `span()` | `(시작, 끝)` 튜플 |
| `groups()` | 모든 캡처 그룹 |
| `groupdict()` | 이름 있는 그룹 딕셔너리 |

실행:

```python
print(match.group())
print(match.start())
print(match.end())
print(match.span())
```

출력:

```text
12345
6
11
(6, 11)
```

---

# 28. `sub()` 문자열 치환

`sub()`는 패턴과 일치한 문자열을 다른 값으로 바꾼다.

```python
text = "전화번호: 010-1234-5678"

result = re.sub(
    r"\d",
    "*",
    text,
)

print(result)
```

출력:

```text
전화번호: ***-****-****
```

## 28-1. 여러 공백 정리

```python
text = "Python     Java   SQL"

result = re.sub(
    r"\s+",
    " ",
    text,
)

print(result)
```

출력:

```text
Python Java SQL
```

---

# 29. 그룹을 이용한 치환

전화번호 일부를 마스킹할 수 있다.

```python
text = "010-1234-5678"

result = re.sub(
    r"(\d{3})-(\d{4})-(\d{4})",
    r"\1-****-\3",
    text,
)

print(result)
```

출력:

```text
010-****-5678
```

```text
\1
→ 첫 번째 그룹

\3
→ 세 번째 그룹
```

## 29-1. 이름 있는 그룹 치환

```python
pattern = (
    r"(?P<front>\d{3})-"
    r"(?P<middle>\d{4})-"
    r"(?P<back>\d{4})"
)

result = re.sub(
    pattern,
    r"\g<front>-****-\g<back>",
    text,
)
```

---

# 30. 함수로 치환하기

`sub()`의 두 번째 인자로 함수를 전달할 수 있다.

```python
def double_number(match):
    number = int(match.group())
    return str(number * 2)
```

```python
text = "1 2 3"

result = re.sub(
    r"\d+",
    double_number,
    text,
)

print(result)
```

출력:

```text
2 4 6
```

> [!TIP]
> 단순 문자열 교체가 아니라 계산이나 조건 처리가 필요하면 치환 함수를 사용할 수 있다.

---

# 31. `split()`

`re.split()`은 정규표현식 패턴을 기준으로 문자열을 나눈다.

```python
text = "Python,Java;SQL HTML"

result = re.split(
    r"[,;\s]+",
    text,
)

print(result)
```

출력:

```text
['Python', 'Java', 'SQL', 'HTML']
```

쉼표, 세미콜론, 공백 중 하나 이상을 구분자로 사용한다.

---

# 32. 탐욕적 수량자

수량자는 기본적으로 가능한 한 많이 일치하려고 한다.

```python
text = "<p>첫 번째</p><p>두 번째</p>"

result = re.findall(
    r"<p>.*</p>",
    text,
)

print(result)
```

출력:

```text
['<p>첫 번째</p><p>두 번째</p>']
```

`.*`가 가능한 많은 문자를 가져갔다.

이를 탐욕적(Greedy) 일치라고 한다.

---

# 33. 비탐욕적 수량자

수량자 뒤에 `?`를 붙이면 가능한 짧게 일치한다.

```python
text = "<p>첫 번째</p><p>두 번째</p>"

result = re.findall(
    r"<p>.*?</p>",
    text,
)

print(result)
```

출력:

```text
['<p>첫 번째</p>', '<p>두 번째</p>']
```

```text
.*
→ 가능한 많이

.*?
→ 가능한 적게
```

> [!WARNING]
> HTML이나 XML 전체 구조를 정규표현식만으로 안정적으로 파싱하는 것은 어렵다.
>
> 실제 문서 파싱에는 전용 파서를 사용하는 것이 좋다.

---

# 34. 플래그

정규표현식 동작 방식을 플래그로 변경할 수 있다.

## 34-1. 대소문자 무시 `re.IGNORECASE`

```python
text = "Python PYTHON python"

result = re.findall(
    r"python",
    text,
    re.IGNORECASE,
)

print(result)
```

출력:

```text
['Python', 'PYTHON', 'python']
```

## 34-2. 여러 줄 시작·끝 `re.MULTILINE`

```python
text = """Python
Java
Python"""
```

```python
result = re.findall(
    r"^Python$",
    text,
    re.MULTILINE,
)

print(result)
```

출력:

```text
['Python', 'Python']
```

## 34-3. 점이 줄바꿈도 포함 `re.DOTALL`

```python
text = "A\nB"

print(bool(re.search(
    r"A.B",
    text,
    re.DOTALL,
)))
```

출력:

```text
True
```

---

# 35. 패턴 컴파일 `re.compile()`

같은 패턴을 여러 번 사용할 때 미리 컴파일할 수 있다.

```python
phone_pattern = re.compile(
    r"\d{3}-\d{4}-\d{4}"
)
```

사용:

```python
print(bool(phone_pattern.fullmatch(
    "010-1234-5678"
)))

print(phone_pattern.findall(
    "문의: 010-1234-5678"
))
```

## 35-1. 장점

- 긴 패턴에 의미 있는 이름을 붙일 수 있다.
- 같은 패턴을 반복 사용할 때 코드가 읽기 쉬워진다.
- 플래그를 패턴과 함께 묶어둘 수 있다.

> [!TIP]
> 한두 번만 사용하는 짧은 패턴은 `re.search()`처럼 바로 사용해도 충분하다.
>
> 반복 사용하거나 긴 패턴은 `re.compile()`로 이름을 붙이는 편이 좋다.

---

# 36. 전화번호 형식 검사

```python
import re


PHONE_PATTERN = re.compile(
    r"^01[016789]-\d{3,4}-\d{4}$"
)
```

## 36-1. 실행

```python
phone_numbers = [
    "010-1234-5678",
    "011-123-4567",
    "01012345678",
    "020-1234-5678",
]

for phone_number in phone_numbers:
    is_valid = bool(
        PHONE_PATTERN.fullmatch(phone_number)
    )

    print(phone_number, is_valid)
```

## 36-2. 출력 결과

```text
010-1234-5678 True
011-123-4567 True
01012345678 False
020-1234-5678 False
```

## 36-3. 패턴 해설

```text
^
→ 문자열 시작

01[016789]
→ 010, 011, 016, 017, 018, 019

-
→ 하이픈

\d{3,4}
→ 중간 번호 3~4자리

-
→ 하이픈

\d{4}
→ 마지막 번호 4자리

$
→ 문자열 끝
```

> [!IMPORTANT]
> 실제 전화번호 정책은 변경될 수 있다.
>
> 서비스에서는 최신 정책과 입력 요구사항을 기준으로 패턴을 관리해야 한다.

---

# 37. 이메일 형식 검사

간단한 학습용 패턴:

```python
EMAIL_PATTERN = re.compile(
    r"^[A-Za-z0-9._%+-]+"
    r"@[A-Za-z0-9.-]+"
    r"\.[A-Za-z]{2,}$"
)
```

## 37-1. 실행

```python
emails = [
    "user@example.com",
    "hello.world@company.co.kr",
    "invalid-email",
    "user@",
]

for email in emails:
    print(
        email,
        bool(EMAIL_PATTERN.fullmatch(email)),
    )
```

## 37-2. 출력 결과

```text
user@example.com True
hello.world@company.co.kr True
invalid-email False
user@ False
```

## 37-3. 주의점

이메일 주소 표준은 매우 복잡하다.

위 패턴은 모든 정상 이메일을 완벽하게 검증하지 않는다.

> [!WARNING]
> 정규표현식 하나로 실제 이메일 존재 여부까지 확인할 수 없다.
>
> 실무에서는 기본 형식 검사 후 인증 메일 전송으로 실제 소유 여부를 확인한다.

---

# 38. 날짜 형식 추출

```python
DATE_PATTERN = re.compile(
    r"(?P<year>\d{4})-"
    r"(?P<month>\d{2})-"
    r"(?P<day>\d{2})"
)
```

## 38-1. 실행

```python
text = "작업일: 2026-08-06"

match = DATE_PATTERN.search(text)

if match:
    print(match.group("year"))
    print(match.group("month"))
    print(match.group("day"))
```

출력:

```text
2026
08
06
```

## 38-2. 형식과 실제 날짜는 다르다

패턴은 다음 문자열도 형식상 일치시킬 수 있다.

```text
2026-99-99
```

실제 날짜 유효성은 `datetime`으로 확인하는 편이 좋다.

```python
from datetime import datetime


datetime.strptime(
    "2026-08-06",
    "%Y-%m-%d",
)
```

> [!IMPORTANT]
> 정규표현식은 문자열 형식을 검사할 수 있지만, 날짜의 실제 존재 여부까지 자동으로 보장하지 않는다.

---

# 39. 로그 데이터 추출

예시 로그:

```text
2026-08-06 10:30:15 INFO Login success
```

패턴:

```python
LOG_PATTERN = re.compile(
    r"(?P<date>\d{4}-\d{2}-\d{2})\s+"
    r"(?P<time>\d{2}:\d{2}:\d{2})\s+"
    r"(?P<level>[A-Z]+)\s+"
    r"(?P<message>.+)"
)
```

## 39-1. 실행

```python
log = (
    "2026-08-06 10:30:15 "
    "INFO Login success"
)

match = LOG_PATTERN.fullmatch(log)

if match:
    print(match.groupdict())
```

출력:

```text
{
    'date': '2026-08-06',
    'time': '10:30:15',
    'level': 'INFO',
    'message': 'Login success'
}
```

---

# 40. 실무에서는 어떻게 사용할까?

정규표현식은 다음 용도로 자주 사용한다.

- 입력 형식의 1차 검사
- 로그 데이터 추출
- 텍스트 전처리
- 문자열 치환
- 파일명 패턴 검색
- 크롤링 전 간단한 문자열 정리
- 코드·문서 검색
- 개인정보 마스킹

하지만 다음 상황에서는 다른 도구가 더 적합할 수 있다.

| 작업 | 더 적합한 도구 |
| --- | --- |
| JSON 파싱 | `json` 모듈 |
| HTML 파싱 | HTML 파서 |
| 날짜 유효성 검사 | `datetime` |
| CSV 처리 | `csv`, `pandas` |
| URL 구조 분석 | `urllib.parse` |
| 복잡한 이메일 검증 | 검증 라이브러리 + 인증 절차 |

> [!TIP]
> 정규표현식은 “문자열 패턴” 문제에 사용한다.
>
> 구조화된 데이터를 정규표현식으로 억지로 해석하지 않는다.

---

# 41. 패턴을 읽기 쉽게 작성하기

긴 정규표현식은 한 줄로 작성하면 읽기 어렵다.

```python
pattern = r"^(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})$"
```

여러 문자열로 나눌 수 있다.

```python
pattern = (
    r"^(?P<year>\d{4})-"
    r"(?P<month>\d{2})-"
    r"(?P<day>\d{2})$"
)
```

또는 `re.VERBOSE`를 사용할 수 있다.

```python
pattern = re.compile(
    r"""
    ^
    (?P<year>\d{4})
    -
    (?P<month>\d{2})
    -
    (?P<day>\d{2})
    $
    """,
    re.VERBOSE,
)
```

## 41-1. 장점

- 패턴을 줄 단위로 분리
- 주석 작성 가능
- 복잡한 패턴의 유지보수 향상

---

# 42. 정규표현식과 성능

정규표현식은 강력하지만 패턴에 따라 성능 문제가 발생할 수 있다.

특히 중첩된 탐욕적 수량자는 주의한다.

```python
pattern = r"(a+)+$"
```

입력에 따라 매우 많은 비교가 발생할 수 있다.

## 42-1. 개선 방향

- 패턴을 단순하게 유지
- 입력 길이 제한
- 불필요한 중첩 수량자 제거
- 전체 검사에는 `fullmatch()` 활용
- 복잡한 구조는 전용 파서 사용
- 성능이 중요한 패턴은 테스트

> [!WARNING]
> 사용자 입력에 복잡한 정규표현식을 적용할 때는 성능 문제도 고려해야 한다.

---

# 43. 대표 오류로 이해하기

## 43-1. 일치 결과가 없는데 `group()` 호출

잘못된 코드:

```python
match = re.search(
    r"\d+",
    "Python",
)

print(match.group())
```

발생 결과:

```text
AttributeError
```

개선:

```python
if match:
    print(match.group())
```

---

## 43-2. 실제 점을 `.`으로 검색

```python
re.search(
    r"3.12",
    "3X12",
)
```

`.`이 임의 문자와 일치하므로 `3X12`도 일치할 수 있다.

개선:

```python
re.search(
    r"3\.12",
    "3.12",
)
```

---

## 43-3. `match()`를 전체 일치 검사로 착각

```python
re.match(
    r"\d+",
    "123abc",
)
```

앞부분 `123`이 일치하므로 성공한다.

전체가 숫자인지 확인하려면:

```python
re.fullmatch(
    r"\d+",
    "123abc",
)
```

---

## 43-4. 그룹 때문에 `findall()` 결과가 달라짐

```python
re.findall(
    r"(\d{4})-(\d{2})-(\d{2})",
    "2026-08-06",
)
```

문자열 하나가 아니라 그룹 튜플이 반환된다.

전체 문자열만 필요하면 비캡처 그룹 또는 `finditer()`를 고려한다.

---

## 43-5. 탐욕적 패턴으로 너무 많이 일치

```python
re.findall(
    r"<p>.*</p>",
    html,
)
```

여러 태그를 한 번에 잡을 수 있다.

```python
re.findall(
    r"<p>.*?</p>",
    html,
)
```

다만 실제 HTML 파싱에는 전용 파서를 사용한다.

---

## 43-6. 원시 문자열을 사용하지 않아 이스케이프 혼란

```python
pattern = "\\d+"
```

동작할 수 있지만 읽기 어렵다.

권장:

```python
pattern = r"\d+"
```

---

# 44. 정규표현식 구조 읽기

패턴:

```python
r"^01[016789]-\d{3,4}-\d{4}$"
```

읽는 순서:

```text
^
→ 문자열 시작

01
→ 01로 시작

[016789]
→ 0, 1, 6, 7, 8, 9 중 하나

-
→ 하이픈

\d{3,4}
→ 숫자 3~4자리

-
→ 하이픈

\d{4}
→ 숫자 4자리

$
→ 문자열 끝
```

복잡한 패턴은 기호별로 나누어 읽는다.

---

# 45. 기존 방식에서 개선된 이해

## 45-1. 정규표현식을 암기 과목으로 이해

기존 이해:

```text
\d
\w
+
*
?
```

개선된 이해:

```text
문자 종류
+
반복 횟수
+
위치 조건
+
그룹 구조
```

패턴을 구성 요소로 나누어 읽는다.

## 45-2. 입력 검증을 정규표현식 하나로 끝냄

개선된 이해:

```text
정규표현식
→ 기본 형식 검사

추가 로직
→ 실제 값 유효성 검사

인증 절차
→ 실제 소유·존재 여부 확인
```

## 45-3. 모든 문자열 문제에 정규표현식 사용

단순 포함 검사나 접두사 검사는 문자열 메서드가 더 읽기 쉽다.

```python
text.startswith("Python")
"Python" in text
text.replace(" ", "")
```

---

# 46. 자주 하는 실수

## 46-1. `.`을 일반 점으로 생각

실제 점은 `\.`을 사용한다.

## 46-2. `*`와 `+` 차이 혼동

`*`는 0회 이상, `+`는 1회 이상이다.

## 46-3. `match()`와 `fullmatch()` 혼동

`match()`는 시작 부분, `fullmatch()`는 전체 문자열을 검사한다.

## 46-4. 일치 결과가 `None`일 수 있음을 무시

`group()` 호출 전 결과를 확인한다.

## 46-5. 캡처 그룹 때문에 `findall()` 결과 형태가 바뀜

그룹이 필요 없으면 `(?:...)`를 사용한다.

## 46-6. 탐욕적 수량자로 너무 넓게 일치

필요하면 비탐욕적 수량자를 사용한다.

## 46-7. 원시 문자열을 사용하지 않음

백슬래시가 많은 패턴은 `r"..."`로 작성한다.

## 46-8. 정규표현식으로 실제 이메일 존재 여부까지 검증

형식 검사와 실제 인증은 별개다.

## 46-9. HTML·JSON 같은 구조화 데이터를 정규표현식으로 파싱

전용 파서를 사용한다.

## 46-10. 지나치게 긴 패턴을 한 줄로 작성

문자열 분리나 `re.VERBOSE`를 사용한다.

## 46-11. 패턴 의미를 설명하지 않음

복잡한 패턴에는 변수명과 주석을 추가한다.

## 46-12. 사용자 입력 길이와 성능을 고려하지 않음

복잡한 패턴은 성능 테스트와 입력 제한이 필요할 수 있다.

---

# 47. 면접·복습 포인트

## Q1. 정규표현식이란 무엇인가요?

문자열의 특정 형식과 패턴을 표현하여 검색·검사·추출·치환하는 문법이다.

## Q2. Python에서 정규표현식은 어떤 모듈을 사용하나요?

표준 라이브러리 `re` 모듈을 사용한다.

## Q3. 원시 문자열을 사용하는 이유는 무엇인가요?

백슬래시가 많은 정규표현식 패턴을 이스케이프 혼란 없이 읽기 쉽게 작성하기 위해 사용한다.

## Q4. `\d`, `\w`, `\s`는 무엇을 의미하나요?

각각 숫자 문자, 단어 문자, 공백 문자를 의미한다.

## Q5. `*`, `+`, `?`의 차이는 무엇인가요?

`*`는 0회 이상, `+`는 1회 이상, `?`는 0회 또는 1회 반복을 의미한다.

## Q6. `search()`, `match()`, `fullmatch()`의 차이는 무엇인가요?

`search()`는 전체에서 첫 일치, `match()`는 시작 위치, `fullmatch()`는 문자열 전체 일치를 검사한다.

## Q7. `findall()`과 `finditer()`의 차이는 무엇인가요?

`findall()`은 결과 리스트를 반환하고, `finditer()`는 일치 객체 이터레이터를 반환한다.

## Q8. 캡처 그룹이란 무엇인가요?

괄호로 묶은 패턴의 일치 결과를 따로 저장하여 `group()`으로 가져올 수 있게 하는 기능이다.

## Q9. 비캡처 그룹은 언제 사용하나요?

패턴은 묶어야 하지만 그룹 결과를 저장할 필요가 없을 때 사용한다.

## Q10. 탐욕적과 비탐욕적 일치의 차이는 무엇인가요?

탐욕적 수량자는 가능한 많이, 비탐욕적 수량자는 가능한 적게 일치한다.

## Q11. `re.compile()`은 왜 사용하나요?

같은 패턴을 반복 사용하거나 긴 패턴에 의미 있는 이름을 붙여 재사용하기 위해 사용한다.

## Q12. 정규표현식만으로 이메일 유효성을 완전히 검증할 수 있나요?

기본 형식은 검사할 수 있지만 실제 존재 여부나 모든 이메일 표준을 완전히 보장하지는 못한다.

---

# 48. 핵심 요약

```text
정규표현식
→ 문자열 패턴 표현

re.search()
→ 전체에서 첫 일치 검색

re.match()
→ 시작 위치 검사

re.fullmatch()
→ 전체 문자열 검사

re.findall()
→ 모든 결과 리스트

re.finditer()
→ 일치 객체 이터레이터

re.sub()
→ 문자열 치환
```

```text
\d
→ 숫자

\w
→ 단어 문자

\s
→ 공백

[]
→ 문자 종류

*
→ 0회 이상

+
→ 1회 이상

?
→ 0회 또는 1회

{m,n}
→ 반복 범위

^
→ 시작

$
→ 끝
```

---

# 49. 최종 체크리스트

- [ ] 패턴을 원시 문자열 `r"..."`로 작성했는가?
- [ ] 일반 문자와 메타문자를 구분했는가?
- [ ] 실제 점을 찾을 때 `\.`을 사용했는가?
- [ ] `*`, `+`, `?`의 반복 횟수를 정확히 이해했는가?
- [ ] 문자열 전체 검증에 `fullmatch()`를 고려했는가?
- [ ] 일치 결과가 `None`일 가능성을 확인했는가?
- [ ] 캡처 그룹이 실제로 필요한가?
- [ ] 필요 없는 그룹은 `(?:...)`로 작성했는가?
- [ ] 탐욕적 패턴이 너무 넓게 일치하지 않는가?
- [ ] 긴 패턴에 의미 있는 변수명을 붙였는가?
- [ ] 복잡한 패턴은 여러 줄 또는 `re.VERBOSE`로 작성했는가?
- [ ] 정규표현식이 아닌 문자열 메서드가 더 적합하지 않은가?
- [ ] 구조화된 데이터는 전용 파서를 사용하고 있는가?
- [ ] 형식 검사와 실제 유효성 검사를 구분했는가?
- [ ] 사용자 입력 길이와 패턴 성능을 고려했는가?

---

# 마무리

정규표현식의 핵심은 기호를 무작정 외우는 것이 아니다.

```text
어떤 문자를 찾을지 정하고
    ↓
몇 번 반복되는지 표현하고
    ↓
문자열의 어느 위치인지 지정하고
    ↓
필요한 부분을 그룹으로 묶고
    ↓
검색·검사·추출·치환 목적에 맞는 함수를 선택하는 것
```

이 원리를 이해하면 복잡해 보이는 패턴도 작은 단위로 나누어 읽고 작성할 수 있다.
