# 실습 01-2. 자료형 퀴즈 — 숫자 맞히기와 투표

[Python 목차](README.md) · [이전: 집계와 로그인](실습-01a_Python_자료형_퀴즈_집계와_로그인.md) · [다음: 주문 파일 과제](실습-02_Python_주문파일_평가실습.md)

같은 수업 퀴즈의 3·5번은 난수 때문에 실행마다 숫자가 다르다. 여기서는 **고정된 출력 숫자** 대신 반복 횟수를 세는 위치와 후보의 득표를 읽는 방식을 비교한다.

<!-- chapter-toc -->

- [1. UP/DOWN의 “몇 번째” 계산](#section-1)
- [2. 100표 집계와 최다 득표자](#section-2)
- [직접 확인할 질문](#section-3)
- [추가로 알면 좋은 것](#section-4)

<a id="section-1"></a>

## 1. UP/DOWN의 “몇 번째” 계산

### 강사님 코드

출처: `teacher/workspace_python/퀴즈/문제-자료형.py` 57–78행 · **원본 발췌**

```python
print('문제3')

import random as r
q3 = r.randint(1, 100)
print('정답', q3)
count = 0

while True :
    # num = int( input('예상은? : ') )
    num = q3
    count += 1

    if not (1 <= num <= 100) :
        print('1~100임')
    else :
        if num == q3 :
            print('정답! 시도 횟수 : ', count)
            break
        elif num < q3 :
            print("UP")
        elif num > q3 :
            print("DOWN")
```

### 내 코드

출처: `me/workspace_python/quiz/01_quiz.py` 89–105행 · **원본 발췌**

```python
print('\n문제3','- - '*10)
import random
com = random.randint(1,100)
user = -1
count = 0

# 시간 날 때 문자 입력받는 방어코드도 넣기
while com != user :
    user = int(input('숫자를 입력하세요.'))
    if com > user :
        print('UP 입니다.')
        count += 1
    elif com < user :
        print('DOWN 입니다.')
        count += 1
    elif com == user :
        print(f'정답입니다! 시도횟수 : {count}')
```

강사님은 `while True` 안에서 `count += 1`을 **정답 비교 전에** 하므로 첫 번째 시도에 맞히면 1회다. 다만 입력 줄은 주석 처리하고 `num=q3`으로 정답을 바로 넣어 두어 **실제 입력 게임으로 실행되지는 않는다**. 내 코드는 `input()`을 받아 UP/DOWN을 보여 주지만 `count`를 **틀렸을 때만** 늘린다. 따라서 처음에 맞히면 `시도횟수 : 0`, 두 번 틀리고 맞히면 2가 나온다. 문제의 “몇 번째에 맞췄는지”라면 정답 시도까지 세는 강사님의 위치가 더 맞는다. 내 주석에 있는 숫자 아닌 입력의 방어 코드는 아직 구현되지 않았다.

<a id="section-2"></a>

## 2. 100표 집계와 최다 득표자

### 강사님 코드

출처: `teacher/workspace_python/퀴즈/문제-자료형.py` 173–187행 · **원본 발췌**

```python
후보 = ['a', 'b', 'c']
득표 = {}

# if 투표 in 득표 :
#     득표[투표] = 득표[투표] + 1
# else :
#     득표[투표] = 1
# print(득표)
for i in range(100):
    투표 = random.choice(후보)

    득표[투표] = 득표.get(투표, 0) + 1
print(득표)

print(max(득표), 득표[max(득표)])
```

### 내 코드

출처: `me/workspace_python/quiz/01_quiz.py` 177–199행 · **원본 발췌**

```python
print('\n문제5','- - '*10)
import random
keys = input('나나')
key = keys.split(' ')

a = 0 # 랜덤 값 1일때 투표
b = 0 # 랜덤 값 2일때 투표
c = 0 # 랜덤 값 3일때 투표

for i in range(0,100) :
    vote = random.randint(1, 3)
    if vote == 1 :
        a += 1
    elif vote == 2 :
        b += 1
    elif vote == 3 :
        c += 1

print(a, b, c)
print(keys)
print(key)

print(vote)
```

강사님은 `random.choice(후보)`로 100번 뽑아 `득표.get(투표,0)+1`로 후보별 횟수를 센다. 내 실행 코드는 난수 1·2·3에 맞춰 `a`, `b`, `c` 수를 올리고 세 값을 출력한다. 나는 후보 이름을 추가로 입력받아 `key` 목록으로 나누지만, 그 이름과 세 카운터를 **연결해 최다 득표자의 이름·표 수를 구하는 부분은 없다**. 마지막의 `print(vote)`도 마지막으로 뽑은 숫자 하나를 보여 줄 뿐이다.

강사님 마지막의 `max(득표)`는 딕셔너리의 **키** 중 가장 큰 문자열을 돌려주므로, 투표 수가 가장 큰 후보를 찾는 코드가 아니다. 내 별도 `test.py`에도 같은 `max(voteGet)` 방식의 시도가 남아 있다. 따라서 두 파일 모두 **100표 집계는 했지만 “최다 득표자” 요구는 정확하게 끝내지 못했다**. 이 차이를 숨기고 정답 완성본으로 소개하지 않는다.

### 내 코드 — 별도 시도

출처: `me/workspace_python/test.py` 166–176행 · **원본 발췌**

```python
import random
candidate = ['a','b','c']
voteGet = {}

for i in range(100) :
    vote = random.choice(candidate)

    voteGet[vote] = voteGet.get(vote, 0) + 1

print(voteGet)
print(max(voteGet) , voteGet[max(voteGet)])
```

<a id="section-3"></a>

## 직접 확인할 질문

1. 첫 입력에 정답을 맞혔을 때 강사님과 내 `count`는 각각 몇인가?
2. `max(득표)`가 표 수가 아닌 키를 비교한다는 것은 어떻게 확인할 수 있을까?
3. 내 `quiz/01_quiz.py`에서 입력받은 후보 이름이 표 수와 연결되는가?

<a id="section-4"></a>

## 추가로 알면 좋은 것

동점 처리까지 완성한 별도 투표 프로그램은 두 수업 원본에 없다. 새로 구현할 때는 **후보 이름과 표 수의 대응**을 먼저 분명히 하고, 집계와 최댓값 비교를 따로 검증해야 한다.

