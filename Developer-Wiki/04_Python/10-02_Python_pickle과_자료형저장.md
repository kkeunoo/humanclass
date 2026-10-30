# 10-02. pickle — 문자열 모양이 아니라 Python 값을 저장하기

[Python 목차](README.md) · [읽기 안내](00-00_Python_V3_동작_백과_읽기법.md)

리스트를 str로 바꿔 파일에 쓴 뒤 읽으면 숫자 리스트가 자동으로 돌아오지 않는다. pickle 실습은 Python 값의 구조를 저장하고 다시 읽는 다른 방법을 보여 준다. 저장한 순서·읽는 순서와 반환 자료형을 확인한다.

**이 장의 목차:** [목표](#learn) · [개념](#concepts) · [예제](#example) · [내 코드](#my-code) · [연결](#connections) · [평가](#review) · [비교](#teacher) · [결과·실험](#results) · [TIP·출처](#tips) · [복습](#practice)

<a id="learn"></a>

## 1. 이 장에서 배울 것

문자열 저장과 직렬화의 차이를 설명한다. import·dump·load·wb·rb를 연결하고 여러 값을 순서대로 읽는 흐름, 파일 끝과 원본 주석의 과도한 일반화를 구별한다.

실제 원본·새 예제·개선안·선택 학습을 구분하고 입력·실행 순서·반환값·출력을 연결한다.

<a id="concepts"></a>

## 2. 무엇이며, 왜 필요한가

직렬화는 값을 저장하거나 전달할 표현으로 바꾸는 작업이다. pickle은 Python 객체 구조를 바이트 표현으로 만들고 다시 Python 값으로 읽는 모듈이다. 파일 확장자가 .p여서 자동으로 자료형을 복원하는 것이 아니라 pickle.load가 그 형식을 해석한다.

| 처리 | 저장·읽기의 단위 | 읽은 결과 |
| --- | --- | --- |
| write(str([1,2])) → read | 글자 | 문자열 '[1, 2]' |
| 그 문자열에 list 적용 | 글자 하나씩 | 대괄호·숫자·공백 문자 목록 |
| pickle.dump → pickle.load | Python 값의 직렬화 표현 | 이 예제에서는 리스트 [1,2] |

dump는 값과 열린 바이너리 파일을 받아 저장하고, load는 열린 바이너리 파일에서 다음 값을 읽어 반환한다. 한 파일에 값을 두 번 dump했다면 load도 각 저장 단위의 순서를 따라간다. 읽는 변수 이름을 name이나 age라고 정했다고 파일에서 원하는 종류를 이름으로 검색하는 것은 아니다.

실행 예제는 직접 만든 파일만 곧바로 다시 읽는다. pickle은 불특정 출처 파일을 안전하게 검사하는 형식이 아니며 load 과정에서 코드가 실행될 수 있다. 외부에서 받은 파일의 범용 변환 도구로 이 실습을 적용하지 않는다.

> 📚 **출처 · 본문 설명 확인:** [Python pickle 공식 문서](https://docs.python.org/ko/3/library/pickle.html). 실제 배운 문법의 의미를 확인한 근거다. 예제·표·풀이 자체는 수업 자료를 바탕으로 새로 구성했다. 외부 문장을 직접 인용하지 않았다. 이번 문법 확인 기간: 2026-10-28~29.

<a id="example"></a>

## 3. 작은 예제로 먼저 이해하기

**새 설명 예제 · 전체 코드.** [실행 파일](실습/책형_복습/10-02_Python_pickle과_자료형저장.py)을 제공한다. 별도 복습 폴더에서 실행한다. book_values.p를 wb로 새로 저장하며 기존 같은 이름의 연습 파일은 바뀐다. 원본 pickle.p를 사용하지 않는다. 이 코드가 직접 만든 파일을 바로 읽는 조건이다.



```python
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
```

numbers를 먼저 저장하고 profile을 다음에 저장했으므로 first는 리스트, second는 딕셔너리다. 숫자 나이는 정수로 돌아온다. 반면 str(numbers)의 화면 모양이 같아도 type은 str이며 list(text)는 글자별 목록이다. 현재 예제는 두 값 저장·두 번 읽기를 확인하며 파일의 바이너리 바이트 모양을 고정 정답으로 적지는 않는다.

**예상 출력 또는 관찰:**

```text
[1, 2] <class 'list'>
{'이름': '민지', '나이': 20} <class 'dict'>
20 <class 'int'>
[1, 2] <class 'str'>
['[', '1', ',', ' ', '2', ']']
```

<a id="my-code"></a>

## 4. 내가 작성한 코드를 따라 읽기

아래는 원본 발췌다. 주석의 잘못된 설명도 원문을 보존하고 풀이에서 교정한다. 필요한 선언·호출·다른 파일의 정의는 다음 절까지 연결해 읽는다.

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_python/10_file.py` 86–119행

```python
import pickle

name = 'eng'
age = 20
address = '한글'
arr = [1,2,3,4]
scores = {
    'k' : 1,
    'k2' : 'val'
}

# dump 함수에는 'wirte'가 내재되어있음
# 실무에서는 dump 1개만 사용함, 여러개로 하면 그 줄을 계속 넘어가야 하기 때문에
with open('pickle.p', 'wb') as f :
    pickle.dump(name, f)
    pickle.dump(age, f)
    pickle.dump(address, f)
    pickle.dump(arr, f)
    pickle.dump(scores, f)

with open('pickle.p', 'rb') as f :
    p1 = pickle.load(f)
    print(p1)
    p2 = pickle.load(f) # 저장 한 'int' 형태가 그대로 돌아옴
    print(p2, type(p2))
    p2 = pickle.load(f) 
    print(p2, type(p2))
    p2 = pickle.load(f) 
    print(p2, type(p2))
    p2 = pickle.load(f) 
    print(p2['k'], type(p2))
    # p2 = pickle.load(f) # EOFError: Ran out of input , 파일을 다 읽었는데 지나갈 때 End of File Error 출력
    # print(p2, type(p2))

```

**발췌 바로 풀이:** `'wb'`는 바이너리 쓰기, `'rb'`는 바이너리 읽기다. 두 코드 모두 `name` → `age` → `address` → `arr` → `score` 또는 `scores` 순서로 **다섯 번** `dump`하고, 같은 순서로 **다섯 번** `load`한다. `age=20`은 다시 읽어도 정수이고, `arr`는 리스트, 마지막 값은 딕셔너리다. 강사님은 마지막 딕셔너리에서 `p2['k']`, 나는 `p2['k']`와 `type(p2)`를 출력한다.

내 원본은 name→age→address→arr→scores 순서로 다섯 번 dump하고 같은 순서로 load한다. p2라는 같은 이름을 여러 번 대입해도 각각 파일의 다음 값을 받는다. 마지막 p2는 딕셔너리라 키 k를 읽을 수 있다. 내 dump 한 개만 사용한다는 메모는 값을 한 묶음으로 저장하는 대안을 떠올리게 하지만 보편적 필수 규칙은 아니다.

<a id="connections"></a>

## 5. 선언·호출·파일이 연결되는 흐름

import pickle → Python이 제공하는 모듈 이름 사용 → open의 바이너리 파일 객체 → pickle.dump(값,파일) → 닫기 → rb로 다시 열기 → pickle.load의 반환값 → 변수에 대입 → type·내용 확인 순서다. dump와 load는 모듈이 제공하는 함수이며 여기에서 직접 정의한 함수가 아니다. 실제 처리할 값들은 본문 코드에 모두 준비했다.

<a id="review"></a>

## 6. 잘한 점·아쉬운 점·개선 방향

**잘한 점:** 내 코드가 복원 뒤 type까지 출력하여 단순 문자열과 차이를 확인한다. **교정:** dump가 여러 번이면 무조건 실무에서 틀린다는 규칙은 아니다. 저장 단위와 읽기 약속을 일관되게 정해야 한다. **원본의 한계:** 값마다 순서를 외워 읽으므로 구조가 커지면 약속이 흐려질 수 있다. **개선 대안:** 관련 값들을 딕셔너리 하나로 묶어 저장하면 읽은 뒤 키로 구별할 수 있지만 원본이 이미 그렇게 했던 것은 아니다.

개선안은 D 드라이브 원본을 수정한 결과가 아니다. 실제 오류·수업용 단순화·목적에 따른 선택을 구별한다.

<a id="teacher"></a>

## 7. 강사님 코드가 도움이 되는 비교



양쪽 저장 순서는 같아 강사님 전체 코드를 반복하지 않는다. 마지막 출력에서 강사님은 딕셔너리 전체·키 값을, 나는 키 값과 딕셔너리 type을 확인한다. 변수 이름 score와 scores의 차이는 해당 파일 안에서 일치하면 오류가 아니다.

<a id="results"></a>

## 8. 결과를 추적하고 한 가지 바꾸기

| 원본 load 차례 | 저장 당시 값 | 읽은 종류 |
| --- | --- | --- |
| 1 | name='eng' | 문자열 |
| 2 | age=20 | 정수 |
| 3 | address='한글' | 문자열 |
| 4 | arr=[1,2,3,4] | 리스트 |
| 5 | scores 딕셔너리 | 딕셔너리 |

여섯 번째 load는 저장한 값이 더 없어 EOFError가 날 수 있다. 원본은 그 줄을 주석으로 두었다. 파일 끝이라고 자동으로 None을 반환하는 일반 조회로 이해하지 않는다. 새로 rb로 열면 다시 처음 값부터 읽는다.

| 한 가지만 변경 | 예상 | 이유 |
| --- | --- | --- |
| 저장 순서만 교환 | first가 딕셔너리 | 읽는 변수명이 종류를 고르지 않음 |
| load 한 번 추가 | EOFError | 저장 단위를 모두 읽음 |
| profile 나이를 문자열로 | 복원 뒤 str | 저장한 자료형 차이 |
| 두 값을 하나의 dict로 묶어 dump | 한 번 읽은 뒤 키로 구별 | 별도 개선한 저장 약속 |

자료형이 예상과 다르면 dump 순서를 본다. 바이너리 파일을 텍스트 read로 읽는 오류와 pickle 자체의 load를 구별한다. EOFError는 읽은 횟수와 파일 내용을 확인한다. 파일 이름을 바꾸었다면 저장과 읽기 경로도 같은지 확인한다.

<a id="tips"></a>

## 9. 추가로 알면 좋은 것과 출처

> 💡 **TIP · 수업 범위 밖:** 다른 언어와의 JSON 교환·버전 호환 정책·사용자 정의 클래스 직렬화·joblib 상세 사용은 추가 학습이다. 직접 만든 기본 자료형을 저장하고 복원하는 범위를 먼저 확인한다.

TIP은 기본 문제의 필수 조건이 아니다. 배운 문법을 확인한 📚 출처와 선택 확장을 구별한다.

<a id="practice"></a>

## 10. 복습과 빠른 정리

1. 저장한 .p 이름만으로 리스트가 복원되는가?
2. 읽을 변수 이름 age를 쓰면 정수를 골라 읽는가?
3. str(리스트)와 pickle 복원의 종류는?
4. 저장 횟수보다 더 load하면?

<details>
<summary>풀이 — 먼저 자신의 답을 적은 뒤 펼치기</summary>

pickle.load가 형식을 읽어야 한다. 변수 이름은 검색 조건이 아니며 파일 순서대로 읽는다. 앞은 문자열이고 pickle 예제는 리스트를 복원한다. 파일 끝이면 EOFError가 날 수 있다.

</details>

| 단계 | 확인 |
| --- | --- |
| 저장 | 값·순서·wb |
| 복원 | 다음 값·rb |
| 관찰 | 내용과 type |
| 조건 | 직접 만든 신뢰 가능한 파일 |

[장별 연습문제](실습/연습문제/10-02_Python_pickle과_자료형저장_연습문제.md) · 다음은 [파일 단어 찾기](10-03_Python_파일에서_단어찾기.md)다.

<!-- 이전 명시 앵커 보존 -->
<a id="section-1"></a>
<a id="section-2"></a>
<a id="section-3"></a>
