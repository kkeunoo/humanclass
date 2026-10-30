# 15. 모듈과 import — 정의가 있는 파일에서 호출한 곳까지 — 연습문제

[본문](../../15_Python_모듈과_import.md) · [문제 목차](README.md)

실제 수업 내용을 바탕으로 **새로 구성한 연습문제**다. 원래 수업 퀴즈·당시 내 풀이와 구별한다. 실행 전 예상 → 이유 설명 → 한 가지 수정 순서로 풀어 본다.

## 목표와 실행 조건

모듈 전체·일부 이름·별칭을 구분한다. 함수·클래스 정의를 가져와 호출하는 두 파일 흐름을 설명하고 표준 모듈·설치 패키지·직접 작성한 파일을 나눈다.

[전체 Python 파일](../책형_복습/15_Python_모듈과_import.py)을 새 파일로 실행한다. 입력·준비 파일·import 조건은 [본문 3절](../../15_Python_모듈과_import.md#example)을 먼저 확인한다. 의도적으로 예외를 관찰하는 예제는 오류 종류와 그 전에 나온 출력도 답에 적는다.

## 문제 1. 결과와 실행 순서 예상

**같은 폴더의 보조 파일 book_tools.py**

```python
def add(x, y):
    return x + y

def sub(x, y):
    return x - y

class Hero:
    def attack(self):
        print('공격한다')
```

```python
import book_tools as tools
from book_tools import sub as subtract, Hero
print(tools.add(2, 3))
print(subtract(5, 2))
hero = Hero()
hero.attack()
```

<details>
<summary>힌트와 풀이</summary>

입력·현재 값·실행 순서·반환값·출력 위치를 따로 표시한다.

```text
5
3
공격한다
```

tools.add가 보조 파일의 add(2,3)을 호출해 5를 반환하고 바깥 print가 출력한다. subtract는 sub 함수에 붙인 현재 파일의 별칭이라 5-2의 3을 반환한다. Hero를 가져와 객체를 만들고 attack을 호출할 때 공격한다가 출력된다. 보조 파일의 모든 정의를 위에 실었으므로 어디서 계산하거나 출력하는지 한 줄씩 연결할 수 있다.

</details>

## 문제 2. 이유를 자신의 말로 설명

1. tools.add와 subtract의 앞부분이 다른 이유는?
2. helper의 정의만 읽으면 attack 문구가 나오는가?
3. 원본 addd·subb는 실제 호출되는가?
4. requests는 Python 표준 모듈인가?

<details>
<summary>풀이</summary>

모듈 별칭 접근과 직접 가져온 함수 별칭이기 때문이다. 메서드를 호출해야 나온다. 원본에서는 가져오기만 했다. requests는 별도 설치 패키지다.

| 원본 호출 | 정의 위치 | 효과 |
| --- | --- | --- |
| fn1.add(1,2) | fn/fn_15_1.py | 3 반환 |
| sub(3,2) | 같은 보조 파일 | 1 반환 |
| Hero().attack() | 보조 파일 클래스 | 공격한다 출력 |
| random.random()·rand() | 표준 모듈 | 각각 난수 반환 |
| urlopen(...).read().decode(...) | 표준 urllib | 바이트 응답을 문자열로 해석 |
| requests.get(...).text | 설치 패키지 | 응답의 텍스트 관찰 |

난수 값·웹페이지 본문은 고정 정답이 아니다. urlopen 결과를 read하면 바이트를 받고 decode에서 문자열로 해석한다. 이 원본은 utf-8을 지정했지만 모든 웹페이지가 그 인코딩이라고 확대하지 않는다. 로컬 helper 검증과 외부 요청 성공은 구분했다.

</details>

## 문제 3. 한 가지만 바꾸기

본문의 다음 실험에서 한 행만 골라 결과를 먼저 예상한다. 실행 후 원래 예제로 돌아가 다음 변경을 확인한다.

| 한 가지만 변경 | 예상 | 이유 |
| --- | --- | --- |
| tools.add 인자 변경 | 반환 합 변경 | 보조 파일 함수 실행 |
| 별칭만 바꾸고 호출은 그대로 | 이름 오류 가능 | 현재 파일 이름 연결 |
| helper를 다른 폴더로 이동 | 찾는 경로가 맞지 않으면 실패 | 모듈 탐색 조건 |
| attack 호출 제거 | 공격 문구 없음 | 정의·생성과 실제 호출은 별개 |

<details>
<summary>막힐 때 확인할 것</summary>

ModuleNotFoundError면 파일명·폴더·실행 환경을 먼저 본다. 가져온 함수가 안 보이면 import 방식에 맞는 이름으로 호출했는지 확인한다. helper만 실행해 출력이 없다고 실패로 판단하지 않는다. random.py 같은 이름을 내 파일에 쓰면 표준 모듈 이름과 충돌할 수 있으므로 목적 이름을 고른다.

</details>

## 채점과 복습

값만 맞혔는지보다 어떤 입력·분기·호출로 그 결과가 나왔는지 설명한다. 예외·주석·의도한 동작을 혼동하지 않는다. 모르면 연결된 본문의 개념·작은 예제·내 원본 풀이로 돌아간다. TIP의 선택 학습은 필수 정답이 아니다.
