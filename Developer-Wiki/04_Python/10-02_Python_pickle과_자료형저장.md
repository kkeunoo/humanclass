# 10-02. `pickle`로 자료형을 저장하고 다시 읽기

[Python 목차](README.md) · [이전: 텍스트 파일](10-01_Python_텍스트파일_읽고쓰기.md) · [다음: 단어 찾기](10-03_Python_파일에서_단어찾기.md)

앞 장의 `str(a)` 방식으로는 리스트가 문자열로 바뀌었다. 양쪽 원본은 이번에는 `pickle.dump`와 `pickle.load`로 **문자열·숫자·리스트·딕셔너리**를 같은 자료형으로 다시 가져오는 연습을 한다.

<!-- chapter-toc -->

- [1. 여러 값을 쓰고 읽는 순서](10-02_Python_pickle과_자료형저장.md#section-1)
- [직접 확인할 질문](10-02_Python_pickle과_자료형저장.md#section-2)
- [추가로 알면 좋은 것](10-02_Python_pickle과_자료형저장.md#section-3)

<a id="section-1"></a>

## 1. 여러 값을 쓰고 읽는 순서

### 강사님 코드

출처: `teacher/workspace_python/_10_file.py` 78–113행 · **원본 발췌**

```python
import pickle

name = 'eng'
age = 20
address = '한글'
arr = [1,2,3,4]
score = {
    'k': 1,
    'k2': 'val'
}

with open('pickle.p', 'wb') as f :
    pickle.dump(name, f)
    pickle.dump(age, f)
    pickle.dump(address, f)
    pickle.dump(arr, f)
    pickle.dump(score, f)

with open('pickle.p', 'rb') as f :
    # dump 순서대로 꺼낸다
    p1 = pickle.load(f)
    print(p1)
    p2 = pickle.load(f)
    print(p2, type(p2))
    p2 = pickle.load(f)
    print(p2, type(p2))
    p2 = pickle.load(f)
    print(p2, type(p2))
    p2 = pickle.load(f)
    print(p2, type(p2))
    print(p2['k'])

    # dump한 만큼만 꺼낼 수 있다
    # p2 = pickle.load(f)
    # print(p2, type(p2))

```

### 내 코드

출처: `me/workspace_python/10_file.py` 86–119행 · **원본 발췌**

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

`'wb'`는 바이너리 쓰기, `'rb'`는 바이너리 읽기다. 두 코드 모두 `name` → `age` → `address` → `arr` → `score` 또는 `scores` 순서로 **다섯 번** `dump`하고, 같은 순서로 **다섯 번** `load`한다. `age=20`은 다시 읽어도 정수이고, `arr`는 리스트, 마지막 값은 딕셔너리다. 강사님은 마지막 딕셔너리에서 `p2['k']`, 나는 `p2['k']`와 `type(p2)`를 출력한다.

내 주석에 있는 “실무에서는 `dump` 1개만 사용”은 이 수업 코드에서 **하나의 값을 묶어서 저장하는 대안**을 떠올리게 하지만, 보편적 필수 규칙은 아니다. 여기서는 다섯 번 저장한 만큼 다섯 번 읽는 실제 흐름을 먼저 이해한다. 그보다 더 읽으면 파일 끝에 도달해 `EOFError`가 날 수 있다는 주석도 양쪽 코드에 있다.

<a id="section-2"></a>

## 직접 확인할 질문

1. `str([1,2,3,4])`를 텍스트 파일에 쓴 것과 `pickle.dump([1,2,3,4], f)`로 쓴 것은 읽은 뒤 자료형이 어떻게 다를까?
2. 다섯 번째 `load`의 결과는 어떤 자료형일까?

<a id="section-3"></a>

**이 장을 읽은 뒤:** [장별 연습문제 풀기](실습/연습문제/10-02_Python_pickle과_자료형저장_연습문제.md)

## 추가로 알면 좋은 것

`pickle` 파일은 **믿을 수 없는 출처의 파일을 읽는 용도에 적합하지 않다**. 이 원본은 직접 쓴 파일을 직접 다시 읽는 수업 예제다. `joblib`은 주석에서만 언급되고 실제 사용 코드는 없으므로 이 장의 필수 학습으로 다루지 않는다.

