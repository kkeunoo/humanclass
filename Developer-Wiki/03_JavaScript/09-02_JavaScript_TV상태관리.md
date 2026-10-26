# 09-02. TV 실습 — 출력 문구와 실제 상태 구분하기

[JavaScript 목차](README.md) · [이전: 화살표 함수](09_JavaScript_화살표함수와_TV상태관리.md) · [다음: 문자열](10_JavaScript_문자열과_문자열메서드.md)

기준은 양쪽 `09_1_tv.html`이다. 여기서 상태란 전원·현재 채널·저장된 볼륨·음소거처럼 다음 호출에도 기억해야 하는 값이다. 실제 TV 기기 제어가 아니라 변수와 콘솔로 동작을 모의하는 수업 실습이다.

<!-- chapter-toc -->

- [1. 어떤 값을 기억하는가](#section-1)
- [2. 채널: 범위를 넘으면 순환](#section-2)
- [3. 볼륨과 음소거 — 경계에서 드러나는 차이](#section-3)
- [4. 내 원버튼 전원의 장점](#section-4)
- [5. 순서대로 확인할 복습](#section-5)
- [추가로 알면 좋은 것](#section-6)

<a id="section-1"></a>

## 1. 어떤 값을 기억하는가

| 역할 | 강사님 이름 | 내 이름 | 초기값·범위 |
| --- | --- | --- | --- |
| 전원 | power | power | false |
| 채널 | lastCh | lastCh | 0, 범위 0–10 |
| 저장 볼륨 | lastVol | lastVol | 0, 범위 0–5 |
| 음소거 | status_mute | VOL_MUTE | false |

CH_MAX·VOL_MAX 같은 const는 경계값을 한곳에서 정한다. 내 VOL_MUTE는 대문자지만 let이고 값이 바뀐다. 대문자가 언어 기능으로 상수를 만드는 것은 아니다. 두 원본 모두 전원을 꺼도 채널·볼륨을 초기화하지 않아 다시 켜면 이전 값이 남는다.

<a id="section-2"></a>

## 2. 채널: 범위를 넘으면 순환

### 강사님 코드

출처: `teacher/workspace_html/javascript/09_1_tv.html` 46–59행 · **원본 발췌**

```javascript
    function channel(ch){
        if(power){

            if(ch < CH_MIN || ch > CH_MAX){
                console.log('채널이 없습니다')
                return
            }

            lastCh = ch
            console.log(ch+'번으로 채널 변경')
        } else {
            console.log('전원 꺼져있음')
        }
    }
```

### 내 코드

출처: `me/workspace_html/javascript/09_1_tv.html` 57–73행 · **원본 발췌**

```javascript
            function channel(ch) {
                if(power) {

                    // return만 쓰면 해당 함수가 종료되기 때문에 else 대신 사용
                    // 지정채널을 받을 때 채널이 0~10의 값이 아니라면, 채널이 없다고 출력하며 종료
                    if(ch < CH_MIN || ch > CH_MAX) {
                        console.log('채널이 없습니다')
                        return
                    }

                    // 0~10번사이 채널일 경우 받은 ch인자로 채널을 변경하며, lastCh에 저장
                    lastCh = ch
                    console.log(ch+'번으로 채널변경')
                } else {
                    console.log('전원 꺼져있음')
                }
            }
```

같은 흐름이다. 전원을 먼저 확인하고 채널 범위를 벗어나면 return하여 lastCh를 바꾸지 않는다. 강사님 테스트의 `channel(-50) // 0` 주석은 결과와 다르다. 채널 없음 안내 후 이전 채널을 유지한다.

채널 올림은 10 다음 0, 내림은 0 다음 10으로 순환한다. 볼륨은 이런 순환이 아니라 최대·최소에서 멈춘다. 직접 채널 입력은 양쪽 모두 정상 숫자 전제를 충분히 검증하지 않는다. NaN은 두 범위 비교를 모두 통과하고, 문자열 '5'는 숫자로 바뀌지 않은 채 저장될 수 있다. UI 입력을 붙일 때는 자료형·정수 여부를 먼저 검토해야 한다.

<a id="section-3"></a>

## 3. 볼륨과 음소거 — 경계에서 드러나는 차이

### 강사님 코드

출처: `teacher/workspace_html/javascript/09_1_tv.html` 91–104행 · **원본 발췌**

```javascript
    function volumeUp(){
        if(power){
            status_mute = false

            // lastCh = lastCh + 1
            lastVol++
            if(lastVol > VOL_MAX){
                lastVol = VOL_MAX
            }
            console.log('볼륨 : '+ lastVol)
        } else {
            console.log('전원 꺼져있음')
        }
    }
```

### 내 코드

출처: `me/workspace_html/javascript/09_1_tv.html` 105–121행 · **원본 발췌**

```javascript
            function volUp() {
                if(power) {
                    lastVol++
                    // VOL_MUTE = false 로 미리 선언해놔도 됨
                    if(lastVol > VOL_MAX) {
                        lastVol = VOL_MAX
                    } else if(VOL_MUTE == true) {
                        console.log('[음소거 해제 및 볼륨UP] 현재볼륨 : ',lastVol)
                        VOL_MUTE = false;
                    } else {
                        console.log('[볼륨UP] 현재볼륨 : ',lastVol)
                    }

                } else {
                    console.log('전원 꺼져있음')
                }
            }
```

강사님은 전원이 켜졌으면 먼저 음소거를 해제하고 볼륨을 올린 뒤 최대값으로 제한한다. 내 코드는 최대값을 넘은 경우 첫 if에서 끝나 음소거 해제와 출력이 실행되지 않는다. **볼륨 5·음소거 중 올림**에서 강사님은 음소거 해제·5 출력, 내 코드는 음소거 유지·추가 출력 없음이다. 최솟값 0에서 내림도 같은 구조의 문제다.

다음은 **내 변수명·함수명을 유지한 교정 예제**다. 강사님의 조건 배치 장점을 반영했다.

```javascript
function volUp() {
    if (!power) {
        console.log('전원 꺼져있음');
        return;
    }
    VOL_MUTE = false;
    lastVol++;
    if (lastVol > VOL_MAX) lastVol = VOL_MAX;
    console.log('[볼륨UP] 현재볼륨 :', lastVol);
}
```

음소거는 lastVol을 0으로 지우는 것이 아니라 별도 불리언 상태를 바꾸고 0으로 들리는 상태를 표현한다. 그래야 해제할 때 기존 볼륨을 기억한다. 강사님 mute와 내 muteOne은 이 구조다. 반면 내 muteOn·muteOff는 문구만 출력하고 VOL_MUTE를 바꾸지 않아 함수 이름과 실제 상태가 어긋난다. 실제 상태를 바꾸려면 각각 true·false 대입을 추가해야 한다.

<a id="section-4"></a>

## 4. 내 원버튼 전원의 장점

강사님은 powerOn·powerOff를 나누었다. 내 파일에는 한 버튼으로 번갈아 바꾸는 powerOne이 추가되어 있다.

출처: `me/workspace_html/javascript/09_1_tv.html` 46–55행 · **원본 발췌**

```javascript
            function powerOne() {
                if(power) {
                    console.log("원버튼 TV 꺼짐")    
                    power = false;
                // } else if (!power) {
                } else {
                    console.log("원버튼 TV 켜짐")   
                    power = true;
                }
            }
```

현재 power를 보고 반대 값으로 바꾸는 기능이 명확하다. 기존 함수들을 억지로 지우거나 새 객체 컨트롤러로 재설계할 필요는 없다. 단, 원본의 자동 테스트 부분에서는 powerOne이 호출되지 않으므로 별도로 호출하여 확인해야 한다.

<a id="section-5"></a>

## 5. 순서대로 확인할 복습

| 시작 조건·호출 | 기대할 상태 |
| --- | --- |
| 전원 꺼짐에서 채널·볼륨 조작 | 값 유지·꺼짐 안내 |
| 켜기 → channel(10) → channelUp() | lastCh=0 |
| channel(0) → channelDown() | lastCh=10 |
| 정상 채널 후 channel(-50) | 이전 채널 유지 |
| 볼륨 5·음소거 후 올림 | 교정본: 볼륨 5·음소거 false |
| 내 powerOne 두 번 | 시작 전원 상태로 복귀 |

출력 문구뿐 아니라 변수 값도 확인해야 muteOn처럼 문구와 상태가 다른 오류를 잡을 수 있다. 테스트를 독립적으로 반복할 때는 시작 상태를 다시 설정한다.

<a id="section-6"></a>

## 추가로 알면 좋은 것

객체·클래스 컨트롤러 재설계, 화면 리모컨 UI, 상태 저장소는 확장이다. 기본은 원본 변수·함수와 상태 전이의 정확성을 이해하는 것이다.

