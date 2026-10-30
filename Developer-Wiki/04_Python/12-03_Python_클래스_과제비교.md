# 12-03. 클래스 과제 — 요구한 데이터와 동작에 맞춰 설계하기

[Python 목차](README.md) · [읽기 안내](00-00_Python_V3_동작_백과_읽기법.md)

실행 오류가 없다는 것과 문제의 요구를 충족했다는 것은 다르다. 노래 목록·주소 변경·가게 생성 문제를 어떤 값·객체·메서드가 필요한지로 나누고, 내 코드의 살릴 점과 보완할 점을 비교한다.

**이 장의 목차:** [목표](#learn) · [개념](#concepts) · [예제](#example) · [내 코드](#my-code) · [연결](#connections) · [평가](#review) · [비교](#teacher) · [결과·실험](#results) · [TIP·출처](#tips) · [복습](#practice)

<a id="learn"></a>

## 1. 이 장에서 배울 것

노래와 목록 관리 객체의 역할을 나누고 공통 리스트·인스턴스별 리스트를 구별한다. 주소만 바꾸는 요구와 계정 전체 변경을 비교하며, 생성 필수 인자와 실제 객체 수를 확인한다.

실제 원본·새 예제·개선안·선택 학습을 구분하고 입력·실행 순서·반환값·출력을 연결한다.

<a id="concepts"></a>

## 2. 무엇이며, 왜 필요한가

문제의 명사와 동사를 코드의 책임으로 연결한다. 노래는 제목·가수·앨범·가사를 보관하고, 목록은 여러 노래를 모아 순회한다. 둘을 한 클래스가 모두 맡으면 모든 목록이 공유되어야 하는지 개별로 관리되어야 하는지 흐려질 수 있다.

| 과제 요구 | 저장할 것 | 호출할 동작 | 확인할 결과 |
| --- | --- | --- | --- |
| 노래 두 곡 이상 | 곡별 네 속성 | 목록에 넣고 순회 | 각 제목·가수 |
| 주소 변경·조회 | 계정의 주소 | 주소 setter·getter | 주소만 바뀌고 반환 |
| 가게 두 곳 | 각 이름·자본금 | 필수 인자로 생성 | 서로 다른 두 값 |

클래스 속성에 둔 리스트는 인스턴스들이 함께 본다. self.songList=[]를 초기화에서 만들면 목록 인스턴스마다 바깥 리스트가 따로 생긴다. 어느 쪽이 무조건 틀린 것은 아니며 독립된 차트 두 개를 원하는지 같은 공통 저장소를 원하는지 요구부터 정해야 한다.

메서드는 필요한 범위만 다루면 사용 의도가 분명해진다. 주소만 바꾸는 호출에 매번 ID·비밀번호까지 넣게 하면 다른 값도 함께 바꿀 여지가 생긴다. 한 번에 계정 전체를 바꾸는 기능이 별도로 필요할 수는 있지만 이번 과제의 주소 변경과 같은 기능은 아니다.

> 📚 **출처 · 본문 설명 확인:** [Python 클래스·인스턴스 변수](https://docs.python.org/ko/3/tutorial/classes.html#class-and-instance-variables). 실제 배운 문법의 의미를 확인한 근거다. 예제·표·풀이 자체는 수업 자료를 바탕으로 새로 구성했다. 외부 문장을 직접 인용하지 않았다. 이번 문법 확인 기간: 2026-10-28~29.

<a id="example"></a>

## 3. 작은 예제로 먼저 이해하기

**새 설명 예제 · 전체 코드.** [실행 파일](실습/책형_복습/12-03_Python_클래스_과제비교.py)을 제공한다. Python이 설치된 환경에서 새 .py 파일로 저장해 실행한다. 터미널은 그 파일이 있는 폴더에서 열고 `python 파일이름.py`를 실행한다. VS Code의 Python 실행 기능을 사용해도 된다. 결과는 터미널에 표시된다.



```python
class Song:
    def __init__(self, title, singer, album, lyrics):
        self.title = title
        self.singer = singer
        self.album = album
        self.lyrics = lyrics
class Chart:
    def __init__(self):
        self.songs = []
    def add_song(self, song):
        self.songs.append(song)
    def show_songs(self):
        for song in self.songs:
            print(f'{song.title}-{song.singer}')
chart = Chart()
chart.add_song(Song('첫 곡', '가수 A', '앨범 A', '연습 가사 A'))
chart.add_song(Song('둘째 곡', '가수 B', '앨범 B', '연습 가사 B'))
chart.show_songs()
other_chart = Chart()
print('다른 목록', len(other_chart.songs))
class Account:
    def __init__(self):
        self.__address = ''
    def set_address(self, address):
        if address.strip() == '':
            print('주소 확인')
            return
        self.__address = address
    def get_address(self):
        return self.__address
account = Account()
account.set_address('천안')
account.set_address('   ')
print(account.get_address())
class Shop:
    def __init__(self, name, money):
        self.name = name
        self.money = money
shop1 = Shop('천안점', 20000)
shop2 = Shop('아산점', 50000)
print(shop1.name, shop1.money)
print(shop2.name, shop2.money)
```

Chart는 자기 songs 목록을 만들어 두 곡을 저장하고 show_songs에서 순회한다. 새 Chart의 목록은 비어 있어 앞 목록과 독립됨을 확인한다. 주소는 천안을 넣은 뒤 공백 입력을 거부하여 기존 천안이 남는다. strip 검사는 배운 문자열 문법을 조합한 새 개선이며 강사님 원본의 if addr보다 조건을 보완했다. 가게는 두 필수 값으로 각각 두 객체를 만든다. 새 클래스명과 가상 곡은 설명용 재구성이지 원래 제출본이 아니다.

**예상 출력 또는 관찰:**

```text
첫 곡-가수 A
둘째 곡-가수 B
다른 목록 0
주소 확인
천안
천안점 20000
아산점 50000
```

<a id="my-code"></a>

## 4. 내가 작성한 코드를 따라 읽기

아래는 원본 발췌다. 주석의 잘못된 설명도 원문을 보존하고 풀이에서 교정한다. 필요한 선언·호출·다른 파일의 정의는 다음 절까지 연결해 읽는다.

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_python/12_class.py` 163–192행

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

**발췌 바로 풀이:** 강사님은 **노래 한 곡을 나타내는 `Song`**을 만들고, 두 객체를 `melon` 리스트에 넣어 `제목-가수`를 출력한다. 내 `Melon1`은 객체를 만들 때마다 곡 정보를 딕셔너리로 만들어 `Melon1.allSong`이라는 **클래스 공통 리스트**에 추가한다. 나는 세 곡을 만들어 각각 `print_sing()`으로 출력했고, 공통 리스트도 채워진다. 다만 실제 출력에서는 `allSong`을 순회하지 않으므로, 강사님의 **곡 객체를 모은 뒤 리스트를 순회하는 구조**가 문제의 “모든 곡을 리스트로 관리하고 출력”에 더 직접적으로 맞는다.

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_python/12_class.py` 201–219행

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

**발췌 바로 풀이:** 문제는 `id`·`pw`·`addr`을 속성으로 두고 **주소를 바꾸거나 반환하는 메서드**를 만드는 것이다. 강사님은 `setAddr(addr)`와 `getAddr()`를 따로 만들어 주소만 다룬다. 내 코드는 `setAccount(id,pw,addr)`로 세 값을 한 번에 바꾸고 `getAccount()`로 세 값을 함께 반환한다. 내 함수도 실행되지만, **주소만 변경하거나 주소만 돌려주는 요구에는 강사님 방식이 더 정확하다.** 강사님은 빈 주소를 거부하는 조건도 추가했다.

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_python/12_class.py` 227–237행

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

**발췌 바로 풀이:** 두 코드 모두 생성자의 필수 매개변수 두 개를 통해 가게 이름과 자본금을 받는다. 강사님은 `Knotted2('천안점', 10000)` 한 객체만 실제로 만들었고, 나는 `mKnotted`로 **천안점과 아산점 두 객체**를 만들었다. 문제의 “두 군데에 창업” 조건에서는 내 실제 생성 수가 더 맞지만, 이름·자본금을 반드시 넣어야 생성된다는 규칙은 양쪽에 같다.

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_python/12_class.py` 240–249행

```python
class Melon :
    def __init__(self) :
        self.songList = []

    def appendSong(self, song) :
        self.songList.append(song)

m = Melon()
m.appendSong(sing1)

```

**발췌 바로 풀이:** 두 `Melon` 구현 모두 `self.songList=[]`를 **객체별로** 만들고, `appendSong`으로 한 곡을 넣는다. 강사님은 `s1`, 나는 `sing1`을 넣었다. 이 목록의 값을 꺼내 출력하는 메서드까지는 아직 작성하지 않았다.

내 Melon1은 곡 정보를 딕셔너리로 만들어 공통 allSong에 넣고 세 객체의 print_sing을 각각 호출한다. allSong은 채웠지만 실제 출력에는 그 목록 순회를 사용하지 않는다. allSong은 정적 메서드가 아니라 클래스 속성이다. albem 키의 오타는 현재 제목·가수 출력에는 영향을 주지 않지만 album 조회와 다르다. 내 Human은 setAccount에서 세 값을 모두 바꾸고 getAccount에서 튜플을 반환한다. mKnotted는 두 지점을 실제 생성했다.

<a id="connections"></a>

## 5. 선언·호출·파일이 연결되는 흐름

Song 초기화 → 곡 객체 → Chart.add_song의 매개변수 song → self.songs.append → show_songs가 각 곡 속성 읽기다. 원본 끝의 Melon 정의도 함께 실었다. self.songList를 만들고 appendSong으로 한 곡을 넣는 것까지이며 출력 메서드는 없다. 내 sing1은 Melon1 인스턴스라 원본 Melon 목록에도 그 객체가 들어간다. 목록에 곡 이름 문자열만 넣은 것으로 설명하지 않는다.

<a id="review"></a>

## 6. 잘한 점·아쉬운 점·개선 방향

**잘한 점:** 내 노래는 요구보다 많은 세 곡을 저장했고 가게는 두 곳을 실제 만들었다. **요구와 차이:** 노래 출력은 공통 목록 순회가 아니고 주소 요구는 계정 전체 메서드로 넓어졌다. **개선:** 곡 상태·목록 책임·주소 변경 범위를 나눠 이름과 메서드를 맞춘다. **공정한 평가:** 클래스 공통 리스트 자체를 무조건 금지하지 않는다. 독립 차트 요구에서 공유가 부적절해지는 이유를 설명한다.

개선안은 D 드라이브 원본을 수정한 결과가 아니다. 실제 오류·수업용 단순화·목적에 따른 선택을 구별한다.

<a id="teacher"></a>

## 7. 강사님 코드가 도움이 되는 비교

출처: `D:/workspace_teacher/workspace_python/_12_class.py` 172–185행

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

출처: `D:/workspace_teacher/workspace_python/_12_class.py` 187–205행

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

강사님의 Song 객체 목록 순회와 주소 전용 메서드는 요구를 더 직접 표현하여 필요한 부분만 인용한다. 반면 가게는 강사님이 한 곳, 내가 두 곳을 실제 생성하므로 두 군데 조건에는 내 생성 수가 더 맞다. 강사님 빈 주소 검사는 공백만 있는 문자열까지 막지 않으며 새 예제의 strip 보완과 구별한다.

<a id="results"></a>

## 8. 결과를 추적하고 한 가지 바꾸기

| 요구 | 강사님 활성 코드 | 내 활성 코드 |
| --- | --- | --- |
| 노래 관리·출력 | 곡 객체 두 개를 리스트로 순회 | 공통 dict 목록과 개별 출력 세 번 |
| 주소 변경 | setAddr·getAddr | 계정 전체 세 값 설정·튜플 반환 |
| 가게 두 곳 | 한 객체 | 두 객체 |
| 별도 Melon | 인스턴스 목록에 s1 추가 | 인스턴스 목록에 sing1 추가 |

문제 주석의 기능을 전부 구현한 것으로 세지 않는다. 정의만 있으면 정의, 생성만 했으면 생성, 실제 호출까지 있으면 그 결과로 구분한다. 반환 튜플을 화면에 출력한 것과 주소만 반환하는 API를 같은 요구 충족으로 판정하지 않는다.

| 한 가지만 변경 | 예상 | 이유 |
| --- | --- | --- |
| Chart.songs를 클래스 공통 리스트로 | 두 차트에서 같은 목록을 볼 수 있음 | 저장 위치 변경 |
| show_songs 호출 제거 | 목록은 있어도 곡 출력 없음 | 저장과 표시 분리 |
| 주소 검사 제거 | 공백 주소로 바뀜 | 허용 입력 규칙 변경 |
| Shop의 money 인자 생략 | TypeError | 필수 인자 누락 |

항목이 예상보다 많으면 공통 목록 공유인지 본다. 주소만 바꾸고 싶은데 ID까지 필요하면 메서드 책임을 확인한다. 곡이 저장됐는데 출력이 없으면 실제 순회 호출을 본다. 잘못된 키 오타는 해당 키를 읽는 시점에 드러날 수 있다.

<a id="tips"></a>

## 9. 추가로 알면 좋은 것과 출처

> 💡 **TIP · 수업 범위 밖:** 여러 사용자의 계정 보안·비밀번호 저장·데이터베이스·여러 차트의 전체 설계·자동 검증 모델은 추가 학습이다. 이 과제는 브라우저 서비스나 인증이 아니라 Python 객체와 메서드 책임을 연습한 것이다.

TIP은 기본 문제의 필수 조건이 아니다. 배운 문법을 확인한 📚 출처와 선택 확장을 구별한다.

<a id="practice"></a>

## 10. 복습과 빠른 정리

1. allSong이라는 이름은 정적 메서드인가?
2. 내 getAccount는 주소 하나만 돌려주는가?
3. 가게 두 곳 요구에서 어느 코드가 실제 두 객체인가?
4. 새 Chart마다 목록을 따로 두려면 어디서 만드는가?

<details>
<summary>풀이 — 먼저 자신의 답을 적은 뒤 펼치기</summary>

클래스 속성 리스트다. 세 값을 튜플로 반환한다. 내 mKnotted 코드다. __init__에서 self.songs=[]로 인스턴스마다 만든다.

</details>

| 기준 | 질문 |
| --- | --- |
| 요구 | 어떤 값을 바꾸고 반환하나? |
| 저장 | 공통인가 개별인가? |
| 실행 | 실제 몇 객체·몇 호출인가? |
| 평가 | 동작함과 요구 충족은 같은가? |

[장별 연습문제](실습/연습문제/12-03_Python_클래스_과제비교_연습문제.md) · 다음은 [상속·super](13-01_Python_상속과_super.md)다.

<!-- 이전 명시 앵커 보존 -->
<a id="section-1"></a>
<a id="section-2"></a>
<a id="section-3"></a>
<a id="section-4"></a>
<a id="section-5"></a>
