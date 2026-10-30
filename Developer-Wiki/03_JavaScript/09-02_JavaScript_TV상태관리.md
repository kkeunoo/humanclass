# 09-02. TV 상태 관리 — 함수 호출 뒤 남는 값

[JavaScript 목차](README.md) · [읽기 안내](00_JavaScript_V3_동작_백과_읽기법.md)

전원·채널·볼륨·음소거는 함수를 호출한 뒤에도 기억해야 한다. 상태 관리란 현재 값이 다음 호출의 결과에 영향을 주는 흐름이다. 실제 기기를 제어하는 코드가 아니라 변수와 Console로 동작을 모의한다.

<a id="chapter-toc"></a>

**이 장의 목차:** [목표](#learn) · [개념](#concepts) · [예제](#example) · [내 코드](#my-code) · [연결](#connections) · [평가](#review) · [비교](#teacher) · [결과·실험](#results) · [TIP·출처](#tips) · [복습](#practice)

<a id="learn"></a>

## 1. 이 장에서 배울 것

저장 상태와 출력 문구를 구분한다. 전원 검사·경계 제한·음소거 해제를 어떤 순서로 처리하는지 비교하고 내 전원 토글의 장점을 설명한다.

입력·현재 상태·실행 순서·결과를 분리해 설명한다. 실제 수업 원본은 아래에 표시하고, 원본에 없는 선택 학습은 9절 TIP에 둔다.

<a id="concepts"></a>

## 2. 무엇이며, 왜 필요한가

함수 안에서 power를 바꾸고 끝나도 바깥 변수에 저장한 값은 다음 호출에 남는다. 매번 지역변수로 false를 새로 만들면 같은 전원 상태를 유지할 수 없다. 반면 함수 안에서만 필요한 중간 계산은 지역변수로 두는 편이 읽기 쉽다.

| 원본 상태 | 초기·범위 | 확인 |
| --- | --- | --- |
| power |false |꺼져 있으면 조작 제한 |
| lastCh |0,0~10 |끝을 넘으면 순환 |
| lastVol |0,0~5 |끝에서 제한,순환 아님 |
| 음소거 |강사님status_mute·내VOL_MUTE=false |저장볼륨과 별도 |

CH_MAX·VOL_MAX는const로 정한 경계다. 내 VOL_MUTE는 대문자여도let이라 바뀐다. 대문자가 언어 기능으로 상수를 만들지는 않는다. 두 원본 모두 전원을 꺼도 채널·볼륨을 초기화하지 않아 다시 켜면 이전 값을 기억한다.

음소거는 lastVol을0으로 지우는 것과 다르다. 별도 참거짓으로 소리 없는 상태를 표현해야 해제 뒤 이전 볼륨을 기억할 수 있다. 화면 문구만 ‘해제’라고 출력해도 실제 변수가 바뀌지 않으면 다음 호출 상태는 그대로다.

> 📚 **출처 · 본문 설명 확인:** [MDN 함수의 범위](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Functions)와 [블록 범위 let](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/let). TV의 상태 정책은 수업 원본을 분석한 것. 배운 기능의 뜻을 확인한 근거다. 예제·표·풀이 흐름은 수업 코드를 바탕으로 새로 작성했으며 외부 문장을 직접 인용하지 않았다. 확인일: 2026-10-28.

<a id="example"></a>

## 3. 작은 예제로 먼저 이해하기

**새 설명 예제 · 전체 스크립트.** [HTML 실행 파일](실습/책형_복습/09-02_JavaScript_TV상태관리.html)과 같은 폴더의 [JS 파일](실습/책형_복습/09-02_JavaScript_TV상태관리.js)을 함께 내려받는다. HTML을 브라우저로 열고 Console에서 결과를 확인한다. script는 필요한 HTML 뒤에 연결한다. 콘솔 출력은 페이지 본문에 자동으로 쓰이지 않는다.

```javascript
let power = false;
let lastVol = 5;
let muted = true;
const VOL_MAX = 5;
function powerOne() {
    power = !power;
    console.log(power ? '켜짐' : '꺼짐');
}
function volumeUp() {
    if (!power) {
        console.log('전원 꺼짐');
        return;
    }
    muted = false;
    lastVol++;
    if (lastVol > VOL_MAX) {
        lastVol = VOL_MAX;
    }
    console.log(lastVol, muted);
}
volumeUp();
powerOne();
volumeUp();
powerOne();
```

이 새 예제는 경계 사례를 바로 보려고 볼륨5·음소거true에서 시작했다. 원본의 초기값0·false와 구별한다. 꺼졌을 때는 값을 바꾸지 않고 돌아간다. 켠 뒤에는 최대 볼륨이어도 먼저 음소거를 해제하고5로 제한해 상태를 출력한다. 두 번의 powerOne은 처음 전원 상태로 돌아온다. 사용한 함수 정의가 모두 위에 있다.

**예상 출력 또는 관찰:**

```text
전원 꺼짐
켜짐
5 false
꺼짐
```

<a id="my-code"></a>

## 4. 내가 작성한 코드를 따라 읽기

아래는 원본의 일부다. 원본에 의존하는 앞 선언·HTML·함수는 다음 절의 연결까지 읽는다. 주석의 잘못된 표현도 원문대로 보존하고 설명에서 교정한다.

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_html/javascript/09_1_tv.html` 57–73행

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

**발췌 바로 풀이:** 같은 흐름이다. 전원을 먼저 확인하고 채널 범위를 벗어나면 return하여 lastCh를 바꾸지 않는다. 강사님 테스트의 `channel(-50) // 0` 주석은 결과와 다르다. 채널 없음 안내 후 이전 채널을 유지한다.

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_html/javascript/09_1_tv.html` 105–121행

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

**발췌 바로 풀이:** 강사님은 전원이 켜졌으면 먼저 음소거를 해제하고 볼륨을 올린 뒤 최대값으로 제한한다. 내 코드는 최대값을 넘은 경우 첫 if에서 끝나 음소거 해제와 출력이 실행되지 않는다. **볼륨 5·음소거 중 올림**에서 강사님은 음소거 해제·5 출력, 내 코드는 음소거 유지·추가 출력 없음이다. 최솟값 0에서 내림도 같은 구조의 문제다.

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_html/javascript/09_1_tv.html` 46–55행

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

**발췌 바로 풀이:** 현재 power를 보고 반대 값으로 바꾸는 기능이 명확하다. 기존 함수들을 억지로 지우거나 새 객체 컨트롤러로 재설계할 필요는 없다. 단, 원본의 자동 테스트 부분에서는 powerOne이 호출되지 않으므로 별도로 호출하여 확인해야 한다.

내 channel은 전원을 확인하고 범위 밖이면 return해 lastCh를 유지한다. powerOne은 현재 전원을 보고 반대로 바꾸는 기능을 추가했다. volUp은 증가 뒤 최대값 검사와 음소거 해제를 else if로 연결했다. 이 구조에서는 최대값을 넘는 첫 갈래에 걸리면 해제·출력 갈래를 건너뛴다.

<a id="connections"></a>

## 5. 선언·호출·파일이 연결되는 흐름

전원 상태 → 조작 허용 여부 → 값 변경 → 범위 보정 → 다른 상태 변경 → 출력 순서로 추적한다. 원본 채널 올림은10다음0, 내림은0다음10이다. 볼륨은0·5에서 멈춘다. 내 muteOne은 상태를 토글하지만 muteOn·muteOff는 문구만 있고 VOL_MUTE 대입이 없어 이름과 상태가 어긋난다. 이 함수들의 역할을 판단할 때 메시지뿐 아니라 대입문을 찾는다.

<a id="review"></a>

## 6. 잘한 점·아쉬운 점·개선 방향

**잘한 점:** 내 원버튼 전원은 한 동작으로 번갈아 바꾸는 목적이 명확하다. 자동 테스트에서 호출되지는 않아 별도 확인이 필요하다. **실제 경계 오류:** 볼륨5·음소거에서올림,0·음소거에서내림이면 내 코드는 해제를 건너뛸 수 있다. **개선 방향:** 강사님처럼 해제를 먼저 하고 경계 제한 뒤 출력하도록 나눈다. 작은 조건문을 이해하지 못한 채 새 객체 컨트롤러로 전면 교체할 필요는 없다.

개선안은 원본을 수정한 결과가 아니다. 실제 오류, 수업용 단순화, 목적에 따른 선택을 구별해 판단한다.

<a id="teacher"></a>

## 7. 강사님 코드가 도움이 되는 비교

출처: `D:/workspace_teacher/workspace_html/javascript/09_1_tv.html` 91–104행

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

위 강사님 volumeUp은 전원이 켜졌을 때 먼저 음소거를 해제한 다음 볼륨 제한과 출력을 처리한다. 내 volUp의 최대값 경계에서 도움이 되는 차이여서 인용했다. 다만 직접 채널 입력은 양쪽 모두 자료형·정수 검증이 충분하지 않다. NaN은 범위 비교에 걸리지 않고 문자열5는 그대로 저장될 수 있으므로 정상 숫자 전제를 표시한다.

<a id="results"></a>

## 8. 결과를 추적하고 한 가지 바꾸기

| 시작 상태·호출 | 원본 또는 개선 판단 |
| --- | --- |
| 꺼짐에서 조작 |값 유지·안내 |
| channel(10) 뒤올림 |0으로순환 |
| channel(0) 뒤내림 |10으로순환 |
| 정상채널 뒤-50 |이전채널유지,주석의0아님 |
|5·음소거에서올림 |강사님은해제·5출력,내원본은해제건너뜀 |
| powerOne 두번 |처음전원으로복귀 |

이 표는 호출 전 상태를 맞춰 비교하는 기준이다. 이미 다른 테스트로 값이 바뀐 상태에서 연속 실행하면 결과도 달라질 수 있다.

| 한 가지 변경 | 예상 | 이유 |
| --- | --- | --- |
| 새 예제 초기power만true |첫조작5false·다음토글꺼짐 |시작상태변경 |
| 원래 muted=false 줄만제거 |켜도음소거true유지 |문구아닌대입필요 |
| 원래 초기lastVol만3 |켜고올리면4 |경계전상태 |

메시지는 맞는데 다음 동작이 이상하면 상태 대입을 확인한다. 최대·최소에서 출력이 사라지면 else if로 서로 다른 책임을 묶었는지 본다. 테스트마다 power·lastVol·음소거 초기값을 적는다.

<a id="tips"></a>

## 9. 추가로 알면 좋은 것과 출처

> 💡 **TIP · 수업 범위 밖:** 객체·클래스 기반 컨트롤러, 화면 리모컨UI·상태 저장소는 추가 학습이다. 기본 목표는 원본 변수·함수와 상태 변화의 정확성이다.



이 절의 확장은 기본 문제의 필수 조건이 아니다. 📚 출처가 있다는 것과 수업 밖 기능이라는 것은 다른 구분이다.

<a id="practice"></a>

## 10. 복습과 빠른 정리

1. 음소거할때 저장볼륨을 반드시0으로 지워야 하는가?
2. 대문자let은 상수인가?
3. 최대볼륨에서 음소거해제가 안되면 어떤 순서를 바꾸는가?

<details>
<summary>짧은 풀이 — 먼저 답한 뒤 확인</summary>

별도 상태를 두어 기존 볼륨을 기억할 수 있다. 대문자는 이름 약속이고let값은 바뀐다. 해제를 먼저 하고 범위 보정과 출력을 별도로 처리한다.

</details>

| 검토 | 질문 |
| --- | --- |
| 상태 |호출뒤무엇이남나 |
| 출력 |상태와일치하나 |
| 경계 |최소·최대에서도되나 |
| 순서 |서로다른작업을else if로묶었나 |

[장별 연습문제](실습/연습문제/09-02_JavaScript_TV상태관리_연습문제.md)에서 예상·설명·수정을 이어 간다. 다음은 [문자열](10_JavaScript_문자열과_문자열메서드.md)이다.

<!-- 이전 색인 이동 주소 보존 -->
<a id="section-1"></a>
<a id="section-2"></a>
<a id="section-3"></a>
<a id="section-4"></a>
<a id="section-5"></a>
<a id="section-6"></a>

[이 장의 목차](#chapter-toc)에서 현재 설명을 찾는다.
