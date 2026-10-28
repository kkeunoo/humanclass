# 12-03. 클래스 과제 비교 — 노래, 계정, 가게

[Python 목차](README.md) · [이전: 속성과 메서드](12-02_Python_클래스속성과_메서드.md)

강사님 원본의 세 문제에는 실제 구현이 있고, 내 파일에도 대응 풀이가 있다. 문제 문구를 기능으로 취급하지 않고 **실행되는 클래스와 객체 생성**을 비교한다. 어느 쪽 코드가 의도에 더 가까운지도 각 문제 아래에서 짚는다.

## 먼저: 문제의 요구와 코드의 결과를 나누기

클래스 과제는 **무엇을 저장할지 → 객체를 몇 개 만들지 → 어떤 메서드를 호출할지** 순서로 읽는다. 예를 들어 노래 두 곡을 저장한다면 두 객체를 만들고, 두 객체를 리스트에 담아 출력하는 흐름이다. 아래는 그 구조만 보여 주는 **설명용 재구성**이다.

```python
class Song:
    def __init__(self, title):
        self.title = title

songs = [Song('첫 곡'), Song('둘째 곡')]
for song in songs:
    print(song.title)
# 첫 곡
# 둘째 곡
```

이것은 강사님이나 내가 제출한 원본 코드가 아니다. 아래에서는 실제 노래 과제의 네 속성과 저장 위치·출력 방법, 이어지는 계정과 가게 과제의 요구를 각각 비교한다.

<!-- chapter-toc -->

- [1. 노래 두 곡 이상 저장하고 출력하기](12-03_Python_클래스_과제비교.md#section-1)
- [2. 계정의 주소 바꾸고 읽기](12-03_Python_클래스_과제비교.md#section-2)
- [3. 필수 값이 있는 가게 만들기](12-03_Python_클래스_과제비교.md#section-3)
- [직접 확인할 질문](12-03_Python_클래스_과제비교.md#section-4)
- [추가로 알면 좋은 것](12-03_Python_클래스_과제비교.md#section-5)

<a id="section-1"></a>

## 1. 노래 두 곡 이상 저장하고 출력하기

### 강사님 코드

출처: `teacher/workspace_python/_12_class.py` 172–185행 · **원본 발췌**

```python
class Song :
    # - 제목, 가수명, 앨범명, 가사
    def __init__(self, title, singer, album, lyric):
        self.title = title
        self.singer = singer
        self.album = album
        self.lyric = lyric

s1 = Song('LOVE ATTACK', 'RESCENE (리센느)', 'SCENEDROME', '라부 어택')
s2 = Song('갑자기', '아이오아이 (I.O.I)', 'I.O.I 3rd MINI ALBUM', '써든 어택')

melon = [s1, s2]
for song in melon :
    print(f'{song.title}-{song.singer}')
```

### 내 코드

출처: `me/workspace_python/12_class.py` 163–192행 · **원본 발췌**

```python
class Melon1 :
    allSong = [] # 이런 형태로 정적 메소드 선언하는건 좋지 않음

    def __init__(self, title, singer, album, words) :
        self.melonList = {
            "title" : title, 
            "singer" : singer, 
            "albem" : album, 
            "words" : words
        }
        Melon1.allSong.append(self.melonList)

    def print_sing(self) :
        print(self.melonList['title'], self.melonList['singer'], sep='-')
   
sing1 = Melon1('LOVE ATTACK', 'RESCENE (리센느)', 'SCENEDROME', '난나나나1')
sing2 = Melon1('갑자기', '아이오아이 (I.O.I)', 'I.O.I 3rd MINI ALBUM [I.O.I : LOOP]', '난나나나2')
sing3 = Melon1('REDRED', 'CORTIS (코르티스)', 'GREENGREEN', '난나나나3')
# sing4 = Melon('테스트', '테스트', '테스트') # 인자값 덜 넣었을 때 테스트

# print(sing1.melonList)
# print(sing2.melonList)
# print(sing3.melonList)
# print(Melon.allSong)

# list배열로 받아서 반복문으로 출력했으면 더 예쁘게 됨
sing1.print_sing()
sing2.print_sing()
sing3.print_sing()

```

강사님은 **노래 한 곡을 나타내는 `Song`**을 만들고, 두 객체를 `melon` 리스트에 넣어 `제목-가수`를 출력한다. 내 `Melon1`은 객체를 만들 때마다 곡 정보를 딕셔너리로 만들어 `Melon1.allSong`이라는 **클래스 공통 리스트**에 추가한다. 나는 세 곡을 만들어 각각 `print_sing()`으로 출력했고, 공통 리스트도 채워진다. 다만 실제 출력에서는 `allSong`을 순회하지 않으므로, 강사님의 **곡 객체를 모은 뒤 리스트를 순회하는 구조**가 문제의 “모든 곡을 리스트로 관리하고 출력”에 더 직접적으로 맞는다.

내 딕셔너리의 앨범 키는 `'albem'`으로 적혀 있다. 이 코드 안에서는 그 키를 다시 읽지 않아 출력에는 영향을 주지 않지만, 나중에 `'album'`을 찾으면 다른 키이므로 주의해야 한다. 클래스 공통 리스트는 새 `Melon1` 객체마다 공유되므로 개별 차트마다 별도 목록이 필요할 때는 맞지 않는다. 두 파일 끝의 `Melon` 클래스는 별도의 `songList`를 인스턴스에 두고 **한 곡을 추가**하는 짧은 예다.

### 강사님 코드 — `Melon`에 곡 추가

출처: `teacher/workspace_python/_12_class.py` 217–225행 · **원본 발췌**

```python
class Melon :
    def __init__(self):
        self.songList = []

    def appendSong(self, song):
        self.songList.append(song)
m = Melon()
m.appendSong(s1)

```

### 내 코드 — `Melon`에 곡 추가

출처: `me/workspace_python/12_class.py` 240–249행 · **원본 발췌**

```python
class Melon :
    def __init__(self) :
        self.songList = []

    def appendSong(self, song) :
        self.songList.append(song)

m = Melon()
m.appendSong(sing1)

```

두 `Melon` 구현 모두 `self.songList=[]`를 **객체별로** 만들고, `appendSong`으로 한 곡을 넣는다. 강사님은 `s1`, 나는 `sing1`을 넣었다. 이 목록의 값을 꺼내 출력하는 메서드까지는 아직 작성하지 않았다.

<a id="section-2"></a>

## 2. 계정의 주소 바꾸고 읽기

### 강사님 코드

출처: `teacher/workspace_python/_12_class.py` 187–205행 · **원본 발췌**

```python
class HumanJobs :
    def __init__(self):
        self.__id = None
        self.__pw = ''
        self.__addr = ''

    def setAddr(self, addr):
        if addr :
            self.__addr = addr
        else :
            print('주소를 다시 입력하세요')
    def getAddr(self):
        return self.__addr

h1 = HumanJobs()
# print( h1.__id )
h1.setAddr('천안')
h1_addr = h1.getAddr()
print( h1_addr )
```

### 내 코드

출처: `me/workspace_python/12_class.py` 201–219행 · **원본 발췌**

```python
class Human :
    def __init__(self) :
        self.__id = ''
        self.__pw = ''
        self.__addr = ''

    def setAccount(self, id, pw, addr) : # 주소만 변경이 문제였기 때문에, 따로 나누어야 함
        self.__id = id
        self.__pw = pw
        self.__addr = addr

    def getAccount(self) :
        return self.__id, self.__pw, self.__addr

human1 = Human()
human1.setAccount('human', 1234, '동남구 대흥동')
# print(human1.__id) # 접근불가 확인
print(human1.getAccount())

```

문제는 `id`·`pw`·`addr`을 속성으로 두고 **주소를 바꾸거나 반환하는 메서드**를 만드는 것이다. 강사님은 `setAddr(addr)`와 `getAddr()`를 따로 만들어 주소만 다룬다. 내 코드는 `setAccount(id,pw,addr)`로 세 값을 한 번에 바꾸고 `getAccount()`로 세 값을 함께 반환한다. 내 함수도 실행되지만, **주소만 변경하거나 주소만 돌려주는 요구에는 강사님 방식이 더 정확하다.** 강사님은 빈 주소를 거부하는 조건도 추가했다.

<a id="section-3"></a>

## 3. 필수 값이 있는 가게 만들기

### 강사님 코드

출처: `teacher/workspace_python/_12_class.py` 207–215행 · **원본 발췌**

```python
class Knotted2 :
    def __init__(self, 상호, 자본금) :
        self.상호 = 상호
        self.자본금 = 자본금

# k1 = Knotted2()
# k1 = Knotted2('천안점')
k1 = Knotted2('천안점', 10000)

```

### 내 코드

출처: `me/workspace_python/12_class.py` 227–237행 · **원본 발췌**

```python
class mKnotted : 
    def __init__(self, name, money):
        self.name = name
        self.money = money

k1 = mKnotted('천안점', 20000)
k2 = mKnotted('아산점', 50000)
# k3 = mKnotted('동남점')

print(k1.name, k1.money)
print(k2.name, k2.money)
```

두 코드 모두 생성자의 필수 매개변수 두 개를 통해 가게 이름과 자본금을 받는다. 강사님은 `Knotted2('천안점', 10000)` 한 객체만 실제로 만들었고, 나는 `mKnotted`로 **천안점과 아산점 두 객체**를 만들었다. 문제의 “두 군데에 창업” 조건에서는 내 실제 생성 수가 더 맞지만, 이름·자본금을 반드시 넣어야 생성된다는 규칙은 양쪽에 같다.

<a id="section-4"></a>

## 직접 확인할 질문

1. 내 `Melon1.allSong`에는 세 곡 정보가 들어가는데, 화면 출력에는 그 리스트를 직접 사용하는가?
2. 내 `getAccount()`는 주소 하나만 돌려주는가?
3. 두 매개변수 중 하나를 빠뜨린 `mKnotted(...)` 호출은 왜 주석 처리했을까?

<a id="section-5"></a>

## 추가로 알면 좋은 것

클래스 공통 리스트와 인스턴스별 리스트 중 무엇을 쓸지는 **서로 다른 차트를 여러 개 만들 계획인지**에 따라 달라진다. 원본에는 차트를 여러 개 운영하는 요구가 없으므로 여기서는 두 코드의 실제 자료 저장 위치까지만 비교한다.

**이 장을 읽은 뒤:** [장별 연습문제 풀기](실습/연습문제/12-03_Python_클래스_과제비교_연습문제.md) → [13-01. 상속과 super](13-01_Python_상속과_super.md)

