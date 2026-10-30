# 13-01. 상속과 super — 같은 인스턴스의 부모 초기화 이어가기

[Python 목차](README.md) · [읽기 안내](00-00_Python_V3_동작_백과_읽기법.md)

상속은 부모 객체 하나를 자식 안에 몰래 추가하는 문법이 아니다. 자식 인스턴스가 부모의 기능을 찾고, 필요한 초기화 작업을 이어 실행하는 관계다. 어떤 메서드를 새로 정의했는지가 호출 순서를 바꾼다.

**이 장의 목차:** [목표](#learn) · [개념](#concepts) · [예제](#example) · [내 코드](#my-code) · [연결](#connections) · [평가](#review) · [비교](#teacher) · [결과·실험](#results) · [TIP·출처](#tips) · [복습](#practice)

<a id="learn"></a>

## 1. 이 장에서 배울 것

부모 메서드 조회와 자식 초기화를 설명한다. 자식이 __init__을 정의한 경우와 물려받는 경우, 부모의 필수 인자를 넘기는 두 방법을 비교한다.

실제 원본·새 예제·개선안·선택 학습을 구분하고 입력·실행 순서·반환값·출력을 연결한다.

<a id="concepts"></a>

## 2. 무엇이며, 왜 필요한가

class Student(Person)은 Student가 Person의 동작을 사용할 수 있는 관계를 정의한다. Student에 greeting이 없어도 부모 Person에서 찾아 호출할 수 있다. 부모 메서드를 호출할 때도 현재 인스턴스가 self로 전달된다.

| 자식의 정의 | 생성 호출에서 사용하는 초기화 | 필요한 일 |
| --- | --- | --- |
| 자식 __init__ 없음 | 물려받은 부모 __init__ | 부모가 요구한 인자를 생성 호출에 전달 |
| 자식 __init__ 있음 | 자식의 __init__ | 필요한 부모 준비를 명시적으로 호출 |
| 자식에서 super().__init__(name) | 이 단일 상속의 부모 초기화 | 같은 인스턴스에 부모 속성 준비 |

부모가 name을 요구한다고 자식이 반드시 __init__을 새로 정의해야 하는 것은 아니다. 자식이 그대로 물려받으면 Student('민지')처럼 필요한 인자를 넘길 수 있다. 새 인자가 필요하거나 생성 호출의 형태를 바꾸고 싶다면 자식 초기화를 정의하고 부모에게 필요한 값을 전달한다.

자식 __init__ 안에서 super를 부르면 새 부모 객체를 하나 더 만드는 것이 아니라 현재 자식 인스턴스의 준비 작업을 이어간다. 원본의 단일 상속에서는 부모 기능 호출로 읽는다. 여러 부모가 있을 때의 탐색 순서는 추가 학습이다.

> 📚 **출처 · 본문 설명 확인:** [Python 상속](https://docs.python.org/ko/3/tutorial/classes.html#inheritance), [super](https://docs.python.org/ko/3/library/functions.html#super). 실제 배운 문법의 의미를 확인한 근거다. 예제·표·풀이 자체는 수업 자료를 바탕으로 새로 구성했다. 외부 문장을 직접 인용하지 않았다. 이번 문법 확인 기간: 2026-10-28~29.

<a id="example"></a>

## 3. 작은 예제로 먼저 이해하기

**새 설명 예제 · 전체 코드.** [실행 파일](실습/책형_복습/13-01_Python_상속과_super.py)을 제공한다. Python이 설치된 환경에서 새 .py 파일로 저장해 실행한다. 터미널은 그 파일이 있는 폴더에서 열고 `python 파일이름.py`를 실행한다. VS Code의 Python 실행 기능을 사용해도 된다. 결과는 터미널에 표시된다.



```python
class Person:
    def __init__(self, name):
        print('부모 초기화', name)
        self.name = name
    def greeting(self):
        print('안녕하세요', self.name)
class Student(Person):
    def __init__(self, name, grade):
        print('자식 초기화 시작')
        super().__init__(name)
        self.grade = grade
        print('자식 초기화 끝')
    def study(self):
        self.greeting()
        print(self.grade, '학년 공부')
class InheritedStudent(Person):
    pass
a = Student('민지', 3)
a.study()
b = InheritedStudent('준호')
b.greeting()
```

Student는 자기 초기화를 정의하므로 시작 문구 뒤 super로 Person 초기화를 호출하고 grade를 넣어 끝낸다. greeting은 Student에 없지만 Person에서 찾아 self.name을 읽는다. InheritedStudent는 초기화를 정의하지 않아 Person의 것을 사용하며 이름 인자 준호를 정상 전달한다. 이 둘을 함께 보면 부모의 필수 인자 때문에 자식 초기화가 무조건 필요하다는 오해를 피할 수 있다.

**예상 출력 또는 관찰:**

```text
자식 초기화 시작
부모 초기화 민지
자식 초기화 끝
안녕하세요 민지
3 학년 공부
부모 초기화 준호
안녕하세요 준호
```

<a id="my-code"></a>

## 4. 내가 작성한 코드를 따라 읽기

아래는 원본 발췌다. 주석의 잘못된 설명도 원문을 보존하고 풀이에서 교정한다. 필요한 선언·호출·다른 파일의 정의는 다음 절까지 연결해 읽는다.

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_python/13_상속.py` 4–15행

```python
class Person :
    def greeting(self) :
        print('안녕하세요')

class Student(Person) : # class에 클래스명()로 상속을 받아올 수 있음
    def study(self) :
        print('공부하기')
        self.greeting() # 상속을 받으면, 부모에 있는것도 self로 가져올 수 있음

s1 = Student()
s1.study()
s1.greeting()
```

**발췌 바로 풀이:** `Student`에는 `study()`만 직접 정의했지만 `Person`을 상속했으므로 `self.greeting()`과 `s1.greeting()`을 호출할 수 있다. `study()`를 한 번 호출하면 `공부하기`와 `안녕하세요`가 나오고, 이어 `s1.greeting()`으로 `안녕하세요`가 한 번 더 나온다. 내 주석의 `s1.hello`는 부모 클래스에도 없는 속성이므로 실행하지 않는다.

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_python/13_상속.py` 18–52행

```python
class Person2 :
    def __init__(self) :
        print('Person2 __init__ 실행')
        self.hello = '방가'

class Student2(Person2) :
    def __init__(self) :
        print('Student2 __init__ 실행')
        super().__init__() # 자식도 init을 쓰고 부모의 init이 있을 경우, 가져와서 실행시켜줘야 함
        self.school = '휴먼'
'''
자식이 init(기본 생성자)을 생성하지 않았을 때 
class Person :
    def __init__(self) :
        print('Person2 __init__ 실행')
class Student(Person) :
    pass
    
       ↓

class Student(Person) :
    def __init__(self) :
        super().__init__()

이 자동으로 생성 됨

단, 부모 생성자에 전달 인자가 필수인 경우
직접 __init__을 정의해서 사용해야 한다
'''

s2 = Student2()
print( s2.school )
print( s2.hello )
# print( s2.hello ) # 부모의 init을 실행하기 전이면, 에러 발생 
# (AttributeError: 'Student2' object has no attribute 'hello')
```

**발췌 바로 풀이:** `Student2`가 자기 `__init__`을 정의하면 그 안에서 `super().__init__()`을 호출해 부모가 만드는 `hello`를 준비한다. 따라서 `Student2 __init__ 실행` 뒤 `Person2 __init__ 실행`이 출력되고 `s2.hello`를 읽을 수 있다. 반면 강사님 `Student3`은 자기 생성자를 정의하지 않아 부모 `Person2.__init__`이 그대로 사용된다. 내 파일에서는 이 경우를 삼중 따옴표 **설명 메모**로 적었고, 실제 `Student3` 클래스를 만들지는 않았다.

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_python/13_상속.py` 56–70행

```python
class Person3 :
    def __init__(self, str) : # 부모가 명백하게 전달인자가 있는 경우, 생략 불가
        print('Person3 __init__ 실행')
        self.hello = '방가'
        self.str = str

class Student4(Person3) :
    # 기본 생성자 super의 __init__ 전달인자는 없으므로,
    # 전달 인자가 필수인 경우 생략할 수 없음
    def __init__(self) :
        super().__init__(None)
    pass

s4 = Student4()
print(s4.hello)
```

**발췌 바로 풀이:** Person3는 인자 하나를 요구하고 Student4는 자기 인자 없는 __init__에서 None을 넘겨 그 요구를 채운다. 부모가 필수 인자를 갖는 모든 경우에 자식 __init__을 반드시 새로 정의해야 한다는 규칙은 아니다. 자식이 물려받은 초기화를 생성 호출의 인자로 사용할 수도 있다.

내 Student는 study 안에서 부모 greeting을 호출하고 밖에서 다시 greeting을 호출하여 인사가 두 번 나온다. Student2는 자기 __init__ 안에서 먼저 자식 문구를 출력하고 super를 호출하여 부모 hello를 만든다. 내 메모의 자동 생성은 새 코드가 합성된다는 뜻보다 부모 초기화를 물려받는 것으로 읽는다. Student4는 매개변수 없는 생성 호출을 택하고 부모에게 None을 넘기는 별도 선택이다.

<a id="connections"></a>

## 5. 선언·호출·파일이 연결되는 흐름

Student2 정의 → Student2() → 자식 __init__ → super().__init__ → 같은 인스턴스 self.hello 대입 → 자식 self.school 대입 → 생성 결과를 s2에 연결 → 각 속성 출력이다. 강사님 Student3은 자기 초기화가 없어 부모 것을 사용하지만 내 파일에는 같은 실클래스 대신 설명 문자열만 있다. 설명 속 코드와 실제 클래스 정의를 구별한다.

<a id="review"></a>

## 6. 잘한 점·아쉬운 점·개선 방향

**잘한 점:** 내 주석은 super 전후 속성 유무를 관찰하고 부모가 요구한 인자를 의식했다. **교정:** 부모 필수 인자가 있으면 자식 초기화를 반드시 정의해야 한다는 문구는 양쪽에서 교정한다. **이름 개선:** 부모 매개변수 str은 내장 str과 겹치므로 message 등 목적 이름을 쓰면 덜 헷갈린다. **설계 선택:** None을 넘겼다고 값의 의미까지 타당한 것은 아니며 이 원본은 형식상 인자를 채운 실습이다.

개선안은 D 드라이브 원본을 수정한 결과가 아니다. 실제 오류·수업용 단순화·목적에 따른 선택을 구별한다.

<a id="teacher"></a>

## 7. 강사님 코드가 도움이 되는 비교



두 원본의 Student2·Student4 흐름은 같아 중복 인용하지 않는다. 강사님만 실제 Student3을 만들었고 내 파일은 메모로 적었다. 부모 초기화를 물려받는 결과와 자식이 명시 호출하는 결과를 새 예제에서 공정하게 비교했다.

<a id="results"></a>

## 8. 결과를 추적하고 한 가지 바꾸기

| 원본 동작 | 생성되는 속성 | 출력 순서 |
| --- | --- | --- |
| Student2 초기화 진입 | 아직 school·hello 준비 전 | 자식 초기화 문구 |
| 부모 초기화 호출 | hello='방가' | 부모 초기화 문구 |
| 자식의 다음 대입 | school='휴먼' | 이후 두 속성 출력 |
| Student4에서 None 전달 | hello·str=None | 부모 문구와 방가 |

super 호출을 지운다고 모든 부모 메서드가 사라지는 것은 아니다. 다만 부모 초기화가 만들던 속성이 준비되지 않을 수 있다. 메서드를 상속하는 것과 그 메서드가 사용할 데이터의 준비는 연결해서 확인해야 한다.

| 한 가지만 변경 | 예상 | 이유 |
| --- | --- | --- |
| Student의 super 호출 제거 | greeting 때 name 조회 오류 | 준비한 대입 누락 |
| InheritedStudent 호출의 이름 생략 | 필수 인자 오류 | 물려받은 초기화도 인자 필요 |
| 자식 grade만 변경 | 부모 name 그대로 | 별도 속성 |
| greeting을 자식에 정의 | 자식 동작 사용 | 재정의는 다음 장에서 연결 |

속성이 없으면 어느 초기화가 그것을 만드는지 찾아 호출 여부를 본다. 생성 인수 오류는 실제 사용하는 __init__ 정의를 확인한다. 부모를 쓴다는 이유만으로 별도 부모 인스턴스가 자동 생겼다고 그리지 않는다.

<a id="tips"></a>

## 9. 추가로 알면 좋은 것과 출처

> 💡 **TIP · 수업 범위 밖:** 다중 상속·MRO·협력적 super 설계·상속과 조합의 선택은 추가 학습이다. 기본은 단일 상속의 조회와 초기화 순서를 추적한다.

TIP은 기본 문제의 필수 조건이 아니다. 배운 문법을 확인한 📚 출처와 선택 확장을 구별한다.

<a id="practice"></a>

## 10. 복습과 빠른 정리

1. 자식에 greeting이 없어도 호출되는 이유는?
2. 부모가 name을 요구하면 자식 __init__ 정의가 항상 필수인가?
3. super 초기화는 새 부모 객체를 추가로 만드는가?

<details>
<summary>풀이 — 먼저 자신의 답을 적은 뒤 펼치기</summary>

부모에서 메서드를 찾아 사용한다. 물려받은 초기화에 생성 인자를 전달할 수 있어 항상 필수는 아니다. 같은 자식 인스턴스에 부모의 준비 작업을 수행한다.

</details>

| 질문 | 확인 |
| --- | --- |
| 어떤 초기화? | 자식 정의 유무 |
| 어떤 인자? | 부모·자식의 요구 |
| 어떤 상태? | 실제 대입한 속성 |
| 어떤 호출? | 같은 인스턴스의 메서드 |

[장별 연습문제](실습/연습문제/13-01_Python_상속과_super_연습문제.md) · 다음은 [재정의·추상 클래스](13-02_Python_메서드재정의와_추상클래스.md)다.

<!-- 이전 명시 앵커 보존 -->
<a id="section-1"></a>
<a id="section-2"></a>
<a id="section-3"></a>
<a id="section-4"></a>
<a id="section-5"></a>
