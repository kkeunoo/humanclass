# 10-03. 파일에서 조건에 맞는 단어 찾기

[Python 목차](README.md) · [이전: `pickle`](10-02_Python_pickle과_자료형저장.md)

두 원본은 `word.txt`를 읽고 **`c` 또는 `C`가 들어간 단어**를 찾은 다음 쉼표와 마침표를 지워 출력하는 문제를 푼다. 문자열의 `split`, `lower`, `in`, `replace`가 **파일에서 읽은 값**에 이어지는 것을 보는 장이다.

<!-- chapter-toc -->

- [1. 강사님 첫 풀이와 수정 풀이](10-03_Python_파일에서_단어찾기.md#section-1)
- [2. 내가 작성한 실행 코드](10-03_Python_파일에서_단어찾기.md#section-2)
- [3. 이 문제에서 조심해 읽을 부분](10-03_Python_파일에서_단어찾기.md#section-3)
- [직접 확인할 질문](10-03_Python_파일에서_단어찾기.md#section-4)
- [추가로 알면 좋은 것](10-03_Python_파일에서_단어찾기.md#section-5)

<a id="section-1"></a>

## 1. 강사님 첫 풀이와 수정 풀이

### 강사님 코드 — 첫 풀이

출처: `teacher/workspace_python/_10_file.py` 133–152행 · **원본 발췌**

```python
with open('word.txt', 'r') as file :
    txt = file.read()
    print(txt)
    
    # txt = 'Fortunately, however, for the reputation of Asteroid B-612, a Turkish dictator made a law that his subjects, under pain of death, should change to European costume. So in 1920 the astronomer gave his demonstration all over again, dressed with impressive style and elegance. And this time everybody accepted his report.'
    txt_list = txt.split(' ')
    print(txt_list)
    # for i in range(len(txt_list)) :
    #     print(txt_list[i])

    for word in txt_list :
        # print(word)
        tmp = word.split('c')
        if len(tmp) > 1 :
            a = word.split('.')
            b = ''.join(a)
            c = b.split(',')
            d = ''.join(c)
            print(d)

```

### 강사님 코드 — 다시 쓴 풀이

출처: `teacher/workspace_python/_10_file.py` 154–177행 · **원본 발췌**

```python
with open('word.txt', 'r') as file :
    txt = file.read()
    print(txt)
    
    # txt = 'Fortunately, however, for the reputation of Asteroid B-612, a Turkish dictator made a law that his subjects, under pain of death, should change to European costume. So in 1920 the astronomer gave his demonstration all over again, dressed with impressive style and elegance. And this time everybody accepted his report.'
    txt_list = txt.split(' ')
    print(txt_list)
    # for i in range(len(txt_list)) :
    #     print(txt_list[i])

    for word in txt_list :
        # if word.find('c') != -1 :
        # if word.count('c') > 0 :
        # if 'c' in word or 'C' in word :
        if 'c'.lower() in word.lower() :
            a = word.replace(',', '')
            b = a.replace('.', '')
            # b = word.replace(',', '').replace('.', '')
            print(b)

# print([1,2,3].find())
```

첫 풀이는 `word.split('c')`의 결과가 둘 이상이면 소문자 `c`가 있다고 판단한다. 따라서 대문자 `C`만 있는 단어는 놓친다. 둘째 풀이는 `word.lower()`에서 `c`를 검사하므로 대소문자 구분을 없애고, `replace(',', '').replace('.', '')`와 같은 흐름으로 기호를 지운다. 양쪽 풀이가 **모두 실행되는 코드**라는 점도 중요하다. 첫 결과 뒤에 구분선을 출력하고 다시 `word.txt`를 읽는다.

<a id="section-2"></a>

## 2. 내가 작성한 실행 코드

### 내 코드

출처: `me/workspace_python/10_file.py` 138–146행 · **원본 발췌**

```python
print('-'*30)
# 단어 중 대소문자 구분없이 c를 포함하는 단어를 출력하시오. 단 , . 은 출력하지 마시오
with open('word.txt', 'r') as file :
    # vf_파일 read하며 반복문에 넣어 바로 대소문자 검사 및 strip으로 ',' '.' 제거 후 출력
    for word in file.read().split(' ') :
        if 'c' in word.lower() :
            print(word.replace(',','').replace('.',''), end=' ')
print()

```

나는 `for word in file.read().split(' ')`로 단어를 하나씩 꺼내고, `'c' in word.lower()`로 검사한다. 맞는 단어만 `replace`로 쉼표와 마침표를 없애어 출력한다. 내 파일의 아래쪽 `find`를 사용하는 여러 시도와 `r+`, `w+`는 모두 **주석 처리된 비교 메모**다. 실행 경로에 포함되지 않으므로 완성된 파일 읽기 기능으로 설명하지 않는다.

<a id="section-3"></a>

## 3. 이 문제에서 조심해 읽을 부분

두 원본 모두 `split(' ')`으로 **일반 공백 한 칸**을 기준으로 나눈다. 줄바꿈이나 여러 공백까지 자연스럽게 “단어”로 나누는 완성된 분석기는 아니다. 또 요구사항은 쉼표와 마침표 제거이므로 다른 문장부호까지 지운다고 생각하지 말자. 이 장에서는 입력 파일의 실제 문장을 검사하고, 어떤 단어가 출력되는지 한 단계씩 따라가면 된다.

<a id="section-4"></a>

## 직접 확인할 질문

1. 대문자 `C`만 포함된 단어는 강사님 첫 풀이와 둘째 풀이에서 각각 어떻게 될까?
2. 내 코드는 `replace`를 검사 전과 검사 후 중 언제 적용할까?

<a id="section-5"></a>

**이 장을 읽은 뒤:** [장별 연습문제 풀기](실습/연습문제/10-03_Python_파일에서_단어찾기_연습문제.md)

## 추가로 알면 좋은 것

여러 공백·줄바꿈·다양한 문장부호를 모두 다루는 토큰화는 이 원본에 구현되지 않았다. 이 문제의 학습 목표는 **파일 읽기와 이미 배운 문자열 메서드를 연결하는 것**이다.

