# 03. 문자열과 포매팅 — 글자를 찾고 새 표현을 만들기

[Python 목차](README.md) · [읽기 안내](00-00_Python_V3_동작_백과_읽기법.md)

문자열 메서드를 이름만 외우면 원래 값이 바뀌었는지, 새 값이 반환되었는지 놓치기 쉽다. 이 장에서는 문장에 값을 넣고 필요한 글자를 찾고 나누고 다시 합치면서 각 작업의 입력과 결과를 구분한다.

**이 장의 목차:** [목표](#learn) · [개념](#concepts) · [예제](#example) · [내 코드](#my-code) · [연결](#connections) · [평가](#review) · [비교](#teacher) · [결과·실험](#results) · [TIP·출처](#tips) · [복습](#practice)

<a id="learn"></a>

## 1. 이 장에서 배울 것

str·f-string·format·% 표시를 읽고 검색 실패의 find·index 차이를 설명한다. replace·strip·upper의 새 문자열, split의 리스트, join의 문자열을 연결하고 폭·정렬·소수 표시를 해석한다.

실제 원본·새 예제·개선안·선택 학습을 구분하고 입력·실행 순서·반환값·출력을 연결한다.

<a id="concepts"></a>

## 2. 무엇이며, 왜 필요한가

문자열은 글자의 순서가 있는 값이다. 숫자 32.5와 문자열 '32.5'는 화면에서 비슷해도 같은 자료형이 아니다. 문자열과 숫자를 +로 바로 더하지 않고 str로 바꾸거나 f-string 안에 값을 넣어 표현한다. 포매팅은 원래 숫자를 반드시 바꾸는 작업이 아니라 값을 어떤 글자 모양으로 보여 줄지 정하는 작업이다.

| 작업 | 예 | 돌려주는 것 |
| --- | --- | --- |
| 위치 찾기 | text.find('l') | 첫 위치, 없으면 -1 |
| 없는 값 확인 | text.index('z') | 있으면 위치, 없으면 ValueError |
| 횟수 | text.count('l') | 나타난 횟수 |
| 치환 | text.replace('l','w') | 바뀐 새 문자열 |
| 분리 | text.split('-') | 문자열들을 담은 리스트 |
| 합치기 | '-'.join(parts) | 구분자로 이은 문자열 |
| 앞뒤 공백 | text.strip() | 앞뒤를 정리한 새 문자열 |

문자열은 내용을 그 자리에서 바꾸는 자료형이 아니다. text.replace를 호출해도 반환값을 저장하지 않으면 text는 그대로다. 연속 호출 text.strip().replace(' ','')는 먼저 앞뒤를 정리한 결과에 다시 치환을 적용한다. 가운데 공백까지 없애는 것은 strip의 역할이 아니다.

인덱스는 0부터 센다. rfind는 뒤에서 찾아도 결과를 오른쪽 끝부터 센 번호로 바꾸는 것이 아니라 왼쪽 기준의 위치를 돌려준다. 대소문자도 구분하므로 Back과 back은 그대로는 같지 않다.

> 📚 **출처 · 본문 설명 확인:** [Python 문자열 메서드](https://docs.python.org/ko/3/library/stdtypes.html#string-methods), [입출력 포매팅](https://docs.python.org/ko/3/tutorial/inputoutput.html#fancier-output-formatting). 실제 배운 문법의 의미를 확인한 근거다. 예제·표·풀이 자체는 수업 자료를 바탕으로 새로 구성했다. 외부 문장을 직접 인용하지 않았다. 이번 문법 확인 기간: 2026-10-28~29.

<a id="example"></a>

## 3. 작은 예제로 먼저 이해하기

**새 설명 예제 · 전체 코드.** [실행 파일](실습/책형_복습/03_Python_문자열과_포매팅.py)을 제공한다. Python이 설치된 환경에서 새 .py 파일로 저장해 실행한다. 터미널은 그 파일이 있는 폴더에서 열고 `python 파일이름.py`를 실행한다. VS Code의 Python 실행 기능을 사용해도 된다. 결과는 터미널에 표시된다.



```python
temperature = 32.5
print('온도: ' + str(temperature))
print(f'온도: {temperature:.1f}')
text = '_hello'
changed = text.replace('l', 'w')
print(text, changed)
print(text.find('l'), text.rfind('l'), text.find('z'))
parts = 'a-b-c'.split('-')
print(parts)
print('/'.join(parts))
phrase = '  a b  '
print('[' + phrase.strip() + ']')
print('[' + phrase.strip().replace(' ', '') + ']')
print('Back'.upper().find('back'.upper()))
print('35'.zfill(4), '35000'.zfill(4))
number = 7
print(f'..{number:>3}..')
print(f'{3.14:08.3f}')
print(f'{15000:,}')
```

replace 결과는 changed에 저장하였으므로 text는 _hello로 남는다. l의 첫 위치는 3, 마지막 위치는 4다. split 뒤 parts는 리스트이고 join 뒤에는 문자열이 된다. 대괄호를 출력에 붙여 strip 뒤에도 가운데 공백은 남는다는 것을 보이게 했다. 08.3f는 소수 세 자리로 표시하고 전체 폭 8을 0으로 채워 0003.140을 만든다. 숫자 자체에 쉼표를 저장한 것이 아니라 출력 문자열을 만든 것이다.

**예상 출력 또는 관찰:**

```text
온도: 32.5
온도: 32.5
_hello _hewwo
3 4 -1
['a', 'b', 'c']
a/b/c
[a b]
[ab]
0
0035 35000
..  7..
0003.140
15,000
```

<a id="my-code"></a>

## 4. 내가 작성한 코드를 따라 읽기

아래는 원본 발췌다. 주석의 잘못된 설명도 원문을 보존하고 풀이에서 교정한다. 필요한 선언·호출·다른 파일의 정의는 다음 절까지 연결해 읽는다.

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_python/03_string.py` 14–14행

```python
b = 32.5
```

**발췌 바로 풀이:** 앞 포매팅 발췌의 b는 여기서 숫자 32.5로 준비한다. str·f-string·format·% 방식이 읽는 값은 이 변수다.

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_python/03_string.py` 15–40행

```python
# c = "지금 온도는 " + b +"도 입니다." # 이것처럼 하면 str + int + str이기에 안 됨
c = "지금 온도는 " + str(b) +"도 입니다."
print(c)

# f를 사용하면 벡틱처럼 사용할 수 있음(fomentic)
d = f"지금 온도는 {b}도 입니다."
print(d)

# 아래처럼 {index}를 사용하고 해당 자리에 format(index)이 들어가도록 사용 가능
e = "지금 온도는 {0}도 입니다".format(b)
print(e)

f = f'''
<div>
    지금 온도는 {b}도 입니다
</div>
'''
print(f)

# 정수로 값이 나옴
g = '지금 온도는 %d도 입니다' % b
print(g)

# float으로 선언 가능
h = '지금 온도는 %f도 입니다' % b
print(h)
```

**발췌 바로 풀이:** 숫자 `b`와 문자열을 `+`로 이어 붙이려면 먼저 `str(b)`로 바꾼다. f-string의 `{b}`는 현재 값을 글자 안에 넣고, `.format(b)`도 자리 표시자에 값을 넣는다. 오래된 `%d`, `%f` 방식도 두 원본에 있으므로 **읽을 수 있게** 다룬다. `%d`는 이 예제의 `32.5`를 정수 모양으로 표시하므로 f-string 출력과 같다고 생각하지 않는다. HTML 모양의 여러 줄 f-string `f`는 양쪽 모두 만들었지만 **강사님은 출력하지 않고, 나는 `print(f)`로 출력했다.**

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_python/03_string.py` 42–42행

```python
i = '_hello'
```

**발췌 바로 풀이:** 아래 위치 찾기 발췌의 i는 문자열 _hello다. 맨 앞 밑줄도 한 글자이므로 첫 l의 인덱스는 3이다.

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_python/03_string.py` 43–60행

```python
print(len(i))

# 'l' 이 몇 개인지 셀 수 있음
print( i.count('l') )
print( i.find('l') ) # find는 indexOf처럼 자리수를 볼 수 있음
print( i.find('z') ) # indexOf와 동일하게 값이 없을 때 -1 반환

print( i.index('l') )
# print( i.index('z') ) # index는 없으면 err msg가 나옴, ValueError: substring not found

print( i.rfind('l') ) # right 우측부터 indexOf

print( i.replace('l','w') ) # replace는 모두 바꿔줌

j = '그럼 저기서 하나만 바꾸고 싶으면요?'
k = j.split()
print(k)

```

**발췌 바로 풀이:** `len`은 글자 수를 세고 `count`는 찾는 글자의 횟수를 센다. `find('z')`는 없을 때 `-1`을 돌려주지만, `index('z')`를 실행하면 오류가 나므로 원본에서는 주석 처리됐다. `rfind`는 오른쪽에서부터 찾되 **돌려주는 인덱스는 여전히 문자열의 왼쪽부터 센 위치**다. `replace('l','w')`는 바뀐 문자열을 돌려주며 원래 문자열 `i`를 자동 변경하지 않는다. `split()`은 여기서 공백을 기준으로 단어를 나눈다.

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_python/03_string.py` 61–81행

```python
m = [1,2,3]
a,b,c = m

a = ['a','b','c','d','e']
b = '-'.join(a) # b = '-'.join(map(str, a))
'-'.join( str(data) for data in a )

print(b)
c = b.split('-')
print(c)

# 대소문자 구분 없이 검색할 때 upper,lower를 주로 사용 함
a = "Don't Look Back is Anger"
b = a.find('back')
print(b)

c = a.upper()
print(c)

d = a.upper().find('back'.upper())
print(d)
```

**발췌 바로 풀이:** 내 a는문자열 리스트를 가리킨 상태에서 join한다. 숫자 리스트로 다시 대입하는 줄은 강사님에게만 있다. 독립 join 표현식의 결과는 저장·출력하지 않으며, b에는 앞에서 만든 a-b-c-d-e가 남는다. Back과 back은 그대로 찾지 못하므로 양쪽을 대문자로 만든 새 문자열에서 위치를 찾는다.

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_python/03_string.py` 83–104행

```python
# strip을 사용하면 양 쪽 공백을 제거해 줌
a = '   a b   '
print(a.strip())
print(a.strip().replace(' ',''))

# zfill을 사용하면 앞에 '0'을 추가할 수 있음
# 모자르면 채워주고, 자리수가 넘으면 그대로 둠
print('35'.zfill(4))
print('35000'.zfill(4))

a = 7
print( f'{a:03}' ) # 007
print( f'..{a:3}..' ) # ..  7.. [3자리로 만들어줌]
print( f'..{a:<3}..' ) # ..7  .. [좌측에 정렬]
print( f'..{a:>3}..' ) # ..  7.. [우측에 정렬]
print( f'..{a:^10}..' ) # ..    7     .. [가운데 정렬]

a = 3.14
print( f'{a:08.3f}' ) # 0003.140

a = 15000
print( f'{a:,}' ) # 15,000 [3자리마다 , 찍어줌]
```

**발췌 바로 풀이:** `strip()`은 양끝 공백을 없애고, 내 코드는 이어 `replace(' ','')`로 중간 공백도 지워 본다. `zfill(4)`는 글자 길이가 4보다 짧을 때 왼쪽을 `0`으로 채운다. 이미 긴 `'35000'`은 줄이지 않는다. f-string의 폭·정렬 지정은 출력 모양을 맞추는 연습이다. `f'{a:08.3f}'`는 실수를 소수 셋째 자리까지 표시하고, `f'{a:,}'`는 큰 정수에 쉼표를 넣는다.

내 포매팅 발췌에서 b=32.5의 준비와 i=_hello의 준비를 함께 실었다. 함수·메서드가 읽는 값이 어디서 왔는지 숨기지 않는다. 양쪽은 여러 줄 HTML 모양의 f-string을 만들지만 강사님은 출력하지 않고 나는 print(f)로 출력한다. %d는 정수 모양의 32, %f는 기본 소수 여섯 자리의 32.500000을 표시하므로 모든 포매팅 결과가 같다고 묶지 않는다. HTML 모양 글자를 출력해도 Python 터미널이 웹페이지로 렌더링하는 것은 아니다.

<a id="connections"></a>

## 5. 선언·호출·파일이 연결되는 흐름

b의 숫자 값 → str 또는 자리 표시자로 문자열 만들기 → print에 전달한다. i 문자열 → 검색 메서드 → 위치·횟수, replace → 새 문자열이다. join(a)는 구분자 문자열의 메서드에 문자열 항목 목록을 넘긴다. 숫자 목록은 각 값을 문자열로 바꾸어야 한다. 원본의 map·제너레이터 표현식은 짧은 사용을 읽는 수준이며 그 내부 구현을 이 장의 필수 조건으로 확장하지 않는다.

<a id="review"></a>

## 6. 잘한 점·아쉬운 점·개선 방향

**잘한 점:** 내 코드는 검색 실패·원본 문자열·치환 결과·공백과 폭을 직접 비교한다. **교정:** f-string은 백틱의 다른 이름이 아니라 Python의 포매팅 문자열이다. b는 float라서 오류 설명도 숫자와 문자열 연결의 차이로 읽는다. **원본 해설 교정:** 내 join 직전의 a는 이미 문자열 리스트다. 그곳의 str(data) 표현식을 숫자 리스트 변환 실행 결과라고 설명하면 현재 값과 다르다. 강사님 쪽에만 별도 a=[1,2,3,4,5]가 있다.

개선안은 D 드라이브 원본을 수정한 결과가 아니다. 실제 오류·수업용 단순화·목적에 따른 선택을 구별한다.

<a id="teacher"></a>

## 7. 강사님 코드가 도움이 되는 비교



HTML 모양 f의 출력 유무와 join 직전 값 차이는 실제 결과·맥락 차이라 설명하되 두 파일 전체를 반복하지 않는다. 내 문장의 is와 강사님 문장의 in도 서로 다른 원문이다. 대소문자 검색 실습의 원리는 같아도 원문 전체가 동일하다고 하지 않는다.

<a id="results"></a>

## 8. 결과를 추적하고 한 가지 바꾸기

| 원본 관찰 | 강사님 | 내 코드 |
| --- | --- | --- |
| 여러 줄 f 생성 | 생성만 | 생성 후 print |
| join 앞 a | 뒤에서 숫자 리스트로 재대입 | 문자열 리스트 유지 |
| join의 새 표현식 | 결과 저장·출력 안 함 | 결과 저장·출력 안 함 |
| strip 뒤 중간 공백 | 남음 | 별도 replace로도 제거 실험 |

zfill(4)는 최소 길이를 채우며 긴 문자열을 자르지 않는다. 정렬 폭도 최대 길이를 강제하는 자르기 규칙이 아니다. strip에 반환값이 있다고 원래 문자열이 변경된 것은 아니며, 이후 같은 a를 새 숫자로 대입한 부분은 별도 대입이다.

| 한 가지만 변경 | 예상 | 이유 |
| --- | --- | --- |
| find('z')를 index('z')로 | ValueError | 없는 값 정책 차이 |
| changed 저장을 text 저장으로 | 이후 text가 새 문자열을 가리킴 | 반환값 재대입 |
| join 구분자를 빈 문자열로 | abc | 항목 사이 문구만 변경 |
| 정렬 폭 3을 5로 | 앞 공백 증가 | 문자열 표시 폭 변경 |

검색 위치가 하나 밀리면 밑줄·공백도 포함해 0부터 센다. 메서드 뒤 원본이 그대로면 반환값을 어디에 저장했는지 확인한다. join 오류는 항목이 문자열인지 본다. 들여쓴 공백·줄바꿈이 출력에 보이면 여러 줄 문자열 내부의 실제 글자도 확인한다.

<a id="tips"></a>

## 9. 추가로 알면 좋은 것과 출처

> 💡 **TIP · 수업 범위 밖:** casefold·복잡한 문자 정규화·정규표현식 전체와 국제화 포매팅은 추가 학습이다. 기본은 원본의 검색·분리·합치기·공백·포매팅으로 구성한다.

TIP은 기본 문제의 필수 조건이 아니다. 배운 문법을 확인한 📚 출처와 선택 확장을 구별한다.

<a id="practice"></a>

## 10. 복습과 빠른 정리

1. replace 뒤 원래 text도 자동으로 바뀌는가?
2. find와 index는 없을 때 어떻게 다른가?
3. 숫자 리스트를 join하기 전에 무엇을 해야 하는가?
4. 내 원본의 join 표현식 직전 a는 숫자 리스트인가?

<details>
<summary>풀이 — 먼저 자신의 답을 적은 뒤 펼치기</summary>

원래 문자열을 자동 변경하지 않는다. find는 -1, index는 예외다. 숫자를 문자열로 바꿔야 한다. 내 a는 그 시점에 문자열 리스트이며 숫자 재대입이 있는 강사님 코드와 다르다.

</details>

| 작업 | 확인할 값 |
| --- | --- |
| 포매팅 | 숫자와 표시 문자열 |
| 검색 | 위치와 실패 정책 |
| 변환 | 문자열·리스트 구분 |
| 변경 | 반환값의 저장 위치 |

[장별 연습문제](실습/연습문제/03_Python_문자열과_포매팅_연습문제.md) · 다음은 [리스트](04_Python_리스트와_데이터처리.md)다.

<!-- 이전 명시 앵커 보존 -->
<a id="section-1"></a>
<a id="section-2"></a>
<a id="section-3"></a>
<a id="section-4"></a>
<a id="section-5"></a>
<a id="section-6"></a>
