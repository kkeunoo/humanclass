# 12-03. 클래스 과제 — 요구한 데이터와 동작에 맞춰 설계하기 — 연습문제

[본문](../../12-03_Python_클래스_과제비교.md) · [문제 목차](README.md)

실제 수업 내용을 바탕으로 **새로 구성한 연습문제**다. 원래 수업 퀴즈·당시 내 풀이와 구별한다. 실행 전 예상 → 이유 설명 → 한 가지 수정 순서로 풀어 본다.

## 목표와 실행 조건

노래와 목록 관리 객체의 역할을 나누고 공통 리스트·인스턴스별 리스트를 구별한다. 주소만 바꾸는 요구와 계정 전체 변경을 비교하며, 생성 필수 인자와 실제 객체 수를 확인한다.

[전체 Python 파일](../책형_복습/12-03_Python_클래스_과제비교.py)을 새 파일로 실행한다. 입력·준비 파일·import 조건은 [본문 3절](../../12-03_Python_클래스_과제비교.md#example)을 먼저 확인한다. 의도적으로 예외를 관찰하는 예제는 오류 종류와 그 전에 나온 출력도 답에 적는다.

## 문제 1. 결과와 실행 순서 예상



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

<details>
<summary>힌트와 풀이</summary>

입력·현재 값·실행 순서·반환값·출력 위치를 따로 표시한다.

```text
첫 곡-가수 A
둘째 곡-가수 B
다른 목록 0
주소 확인
천안
천안점 20000
아산점 50000
```

Chart는 자기 songs 목록을 만들어 두 곡을 저장하고 show_songs에서 순회한다. 새 Chart의 목록은 비어 있어 앞 목록과 독립됨을 확인한다. 주소는 천안을 넣은 뒤 공백 입력을 거부하여 기존 천안이 남는다. strip 검사는 배운 문자열 문법을 조합한 새 개선이며 강사님 원본의 if addr보다 조건을 보완했다. 가게는 두 필수 값으로 각각 두 객체를 만든다. 새 클래스명과 가상 곡은 설명용 재구성이지 원래 제출본이 아니다.

</details>

## 문제 2. 이유를 자신의 말로 설명

1. allSong이라는 이름은 정적 메서드인가?
2. 내 getAccount는 주소 하나만 돌려주는가?
3. 가게 두 곳 요구에서 어느 코드가 실제 두 객체인가?
4. 새 Chart마다 목록을 따로 두려면 어디서 만드는가?

<details>
<summary>풀이</summary>

클래스 속성 리스트다. 세 값을 튜플로 반환한다. 내 mKnotted 코드다. __init__에서 self.songs=[]로 인스턴스마다 만든다.

| 요구 | 강사님 활성 코드 | 내 활성 코드 |
| --- | --- | --- |
| 노래 관리·출력 | 곡 객체 두 개를 리스트로 순회 | 공통 dict 목록과 개별 출력 세 번 |
| 주소 변경 | setAddr·getAddr | 계정 전체 세 값 설정·튜플 반환 |
| 가게 두 곳 | 한 객체 | 두 객체 |
| 별도 Melon | 인스턴스 목록에 s1 추가 | 인스턴스 목록에 sing1 추가 |

문제 주석의 기능을 전부 구현한 것으로 세지 않는다. 정의만 있으면 정의, 생성만 했으면 생성, 실제 호출까지 있으면 그 결과로 구분한다. 반환 튜플을 화면에 출력한 것과 주소만 반환하는 API를 같은 요구 충족으로 판정하지 않는다.

</details>

## 문제 3. 한 가지만 바꾸기

본문의 다음 실험에서 한 행만 골라 결과를 먼저 예상한다. 실행 후 원래 예제로 돌아가 다음 변경을 확인한다.

| 한 가지만 변경 | 예상 | 이유 |
| --- | --- | --- |
| Chart.songs를 클래스 공통 리스트로 | 두 차트에서 같은 목록을 볼 수 있음 | 저장 위치 변경 |
| show_songs 호출 제거 | 목록은 있어도 곡 출력 없음 | 저장과 표시 분리 |
| 주소 검사 제거 | 공백 주소로 바뀜 | 허용 입력 규칙 변경 |
| Shop의 money 인자 생략 | TypeError | 필수 인자 누락 |

<details>
<summary>막힐 때 확인할 것</summary>

항목이 예상보다 많으면 공통 목록 공유인지 본다. 주소만 바꾸고 싶은데 ID까지 필요하면 메서드 책임을 확인한다. 곡이 저장됐는데 출력이 없으면 실제 순회 호출을 본다. 잘못된 키 오타는 해당 키를 읽는 시점에 드러날 수 있다.

</details>

## 채점과 복습

값만 맞혔는지보다 어떤 입력·분기·호출로 그 결과가 나왔는지 설명한다. 예외·주석·의도한 동작을 혼동하지 않는다. 모르면 연결된 본문의 개념·작은 예제·내 원본 풀이로 돌아간다. TIP의 선택 학습은 필수 정답이 아니다.
