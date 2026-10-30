# 12. DOM 콘텐츠 — 글자·HTML·숫자·현재 시각

[JavaScript 목차](README.md) · [읽기 안내](00_JavaScript_V3_동작_백과_읽기법.md)

요소 안의 내용을 바꿀 때 문자열을 글자로 보여 줄지 HTML로 해석할지 정해야 한다. 같은 요소에 연속으로 대입하면 마지막 내용이 남는다. 숫자 갱신과 시계도 읽기·처리·쓰기의 같은 흐름으로 볼 수 있다.

<a id="chapter-toc"></a>

**이 장의 목차:** [목표](#learn) · [개념](#concepts) · [예제](#example) · [내 코드](#my-code) · [연결](#connections) · [평가](#review) · [비교](#teacher) · [결과·실험](#results) · [TIP·출처](#tips) · [복습](#practice)

<a id="learn"></a>

## 1. 이 장에서 배울 것

textContent·innerText·innerHTML을 구분한다. 화면 문자열의 숫자 변환과 반복마다 Date를 새로 만드는 이유를 설명한다.

입력·현재 상태·실행 순서·결과를 분리해 설명한다. 실제 수업 원본은 아래에 표시하고, 원본에 없는 선택 학습은 9절 TIP에 둔다.

<a id="concepts"></a>

## 2. 무엇이며, 왜 필요한가

textContent는 하위 텍스트를 읽고 문자열을 대입하면 태그 모양도 글자로 넣는다. innerText는 렌더링되는 글자·줄바꿈과 관련되어 스타일·표시 상태의 영향을 받는다. innerHTML은 내부 마크업을 문자열로 읽고 대입 문자열을 HTML로 해석해 내부 내용을 교체한다.

| 입력 | textContent | innerHTML |
| --- | --- | --- |
| '<b>안녕</b>' |꺾쇠 포함 글자 |b 요소와 안녕 |
| '0' 읽기 |문자열 |마크업 문자열 |
| 다시 대입 |기존 내용 교체 |기존 내부 구조 교체 |

글자 표시가 목적이면 textContent 같은 텍스트 속성을 고른다. 사용자가 적은 내용을 그대로 innerHTML로 해석하면 원치 않는 태그나 동작이 들어갈 수 있다. 원본은 이 차이를 실험하는 코드이며 새 보안 도구 전체를 필수로 추가한 것은 아니다.

화면의 '0'을 읽은 뒤 +1은 '01' 연결이 될 수 있어 Number로 바꾼다. 시계는 저장한 now를 계속 읽는 대신 예약 콜백 안마다 new Date로 현재 순간을 다시 읽는다. 더 짧은 타이머 간격이 정확한 실행 시각을 보장하지는 않는다.

> 📚 **출처 · 본문 설명 확인:** [MDN textContent](https://developer.mozilla.org/en-US/docs/Web/API/Node/textContent), [innerText](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/innerText), [innerHTML](https://developer.mozilla.org/en-US/docs/Web/API/Element/innerHTML). 배운 기능의 뜻을 확인한 근거다. 예제·표·풀이 흐름은 수업 코드를 바탕으로 새로 작성했으며 외부 문장을 직접 인용하지 않았다. 확인일: 2026-10-28.

<a id="example"></a>

## 3. 작은 예제로 먼저 이해하기

**새 설명 예제 · 전체 스크립트.** [HTML 실행 파일](실습/책형_복습/12_JavaScript_DOM_콘텐츠생성과_스타일조작.html)과 같은 폴더의 [JS 파일](실습/책형_복습/12_JavaScript_DOM_콘텐츠생성과_스타일조작.js)을 함께 내려받는다. HTML을 브라우저로 열고 Console에서 결과를 확인한다. script는 필요한 HTML 뒤에 연결한다. 콘솔 출력은 페이지 본문에 자동으로 쓰이지 않는다.

**먼저 준비할 HTML · body 안:**

```html
    <div id="plain"></div>
    <div id="markup"></div>
    <p id="count">0</p>
```

```javascript
const plain = document.getElementById('plain');
const markup = document.getElementById('markup');
plain.textContent = '<b>안녕</b>';
markup.innerHTML = '<b>안녕</b>';
console.log(plain.textContent);
console.log(markup.textContent);
console.log(markup.querySelector('b') !== null);
const count = document.getElementById('count');
console.log(count.textContent + 1);
count.textContent = Number(count.textContent) + 1;
console.log(count.textContent);
```

두 영역에 같은 문자열을 넣었지만 plain은 태그 모양의 글자, markup은 실제 b 요소가 된다. markup 안의 b를 선택해 null이 아님을 확인했다. count를 읽으면 문자열0이므로 첫 덧셈은01이다. Number 뒤 대입은 숫자1을 화면 글자로 써 최종1이 된다.

**예상 출력 또는 관찰:**

```text
<b>안녕</b>
안녕
true
01
1
```

<a id="my-code"></a>

## 4. 내가 작성한 코드를 따라 읽기

아래는 원본의 일부다. 원본에 의존하는 앞 선언·HTML·함수는 다음 절의 연결까지 읽는다. 주석의 잘못된 표현도 원문대로 보존하고 설명에서 교정한다.

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_html/javascript/12_dom_content.html` 86–98행

```javascript
            // space는 1개로 보이고 태그는 반영되지 않는 글씨로 들어감
            // innerText == textContent 바꿀 땐 두개 다 동일함, 가져올때만 다름
            msg.textContent = '<h1>h1제목</h1>   a   b      c'
            msg.innerText = '<h1>h1제목</h1>   a   b      c'

            // innerHTML은 안쪽에 그대로 HTML로 인식하도록 넣는것이기 때문에, 태그도 먹힘
            // 변수이기 때문에 +로 추가할 수 있음
            msg.innerHTML = '<h1>h1제목</h1>   a   b      c'
            msg.innerHTML += 'd'

            // 이런 것 처럼 innerHTML로 글쓰기를 눌렀을 때 게시글 추가되게 할 수도 있음
            // script, javascript, css도 : 추가하면 넣을 수 있음, 다음줄은 ;로 구분
            msg.innerHTML = '<a href="javascript:alert(1);alert(2);">눌러봐</a>'
```

**발췌 바로 풀이:** 처음 두 대입은 h1이라는 글자와 꺾쇠를 텍스트로 넣는다. innerHTML 대입에서는 h1 요소가 만들어진다. 이후 += 'd'는 기존 HTML 문자열 뒤에 d를 붙여 다시 넣는다. 마지막 대입은 앞 내용을 전부 덮으므로 **최종 화면에 남는 것은 ‘눌러봐’ 링크**다. 모든 중간 결과가 함께 남는 예제가 아니다.

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_html/javascript/12_dom_content.html` 102–111행

```javascript
            setInterval( function() {
                const count = document.querySelector('#count')
                // #count라는 id를 가진친구들 가져와서, cnt에 넣고 
                // 아래 'string' 타입이기 때문에 증가시키기 위해 Number로 치환
                let cnt = count.textContent
                // console.log(cnt, typeof cnt)

                cnt = Number(cnt) + 1
                count.innerText = cnt
            }, 1000 )
```

**발췌 바로 풀이:** 양쪽은 같은 흐름이다. 처음 #count의 글자는 '0'이다. 읽으면 문자열이므로 Number로 숫자로 바꾼 뒤 1을 더하고 다시 화면에 쓴다.

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_html/javascript/12_dom_content.html` 117–135행

```javascript
            setInterval( function() {
                const clock = document.querySelector('#clock')
                
                // 시간은 반복적으로 체크해야 하기 때문에, setInterval 안에 넣음
                // 밖에 있다고 치면 한 번만 확인해서 반복하지 않기 때문
                const now = new Date()
                const hour = now.getHours()
                const min = now.getMinutes()
                const sec = now.getSeconds()
                // 보통 ms까지 체크해서 보여주면 좋음
                const ms = now.getMilliseconds()

                // console.log(`${min}분 ${sec}초`)
                const clockNew = `${hour}시 ${min}분 ${sec}초.${ms}(ms)`
                clock.textContent = clockNew

                // 1000으로 1초를 설정해놓아도 1초마다 동작하지 않을 수 있기에,
                // 1000ms를 3으로 나누어서 delay가 있을 때 해결할 수 있음
            },250)
```

**발췌 바로 풀이:** Date를 콜백 안에서 새로 만들어 실제 실행 시점의 시·분·초·밀리초를 읽는다. 내250ms는 강사님3000ms보다 잦은 갱신 요청이지만 지연이 사라진다는 보장은 아니다. 밀리초도 필수정보가 아닌 관찰용 표현이다.

내 msg는 textContent → innerText → innerHTML → HTML 추가 → 마지막 링크 대입을 같은 요소에 한다. 최종 내용은 눌러봐 링크이고 앞의 h1이 모두 남지 않는다. count 타이머는 글자 읽기 → Number → +1 → 쓰기를 반복한다. 시계는 Date를 콜백 안에 두어 그때의 시각을 읽는다.

<a id="connections"></a>

## 5. 선언·호출·파일이 연결되는 흐름

선택 → 현재 내용 읽기 → 원하는 자료형으로 처리 → 텍스트 또는 HTML 쓰기 순서다. 원본 msg·count·clock은 앞 HTML의 각 ID 요소다. 타이머 본문의 선택 시점에 그 요소가 있어야 한다. 내 시계는 시·분·초·밀리초를250ms 간격, 강사님은 분·초·밀리초를3000ms 간격으로 표시한다. 둘 다 콜백 안의 new Date이며 변수 이름 자체가 자동 갱신시키지 않는다.

<a id="review"></a>

## 6. 잘한 점·아쉬운 점·개선 방향

**잘한 점:** 내 시계는 현재값을 반복해서 읽는 이유를 적었고 시도 포함했다. **교정:** innerText와 textContent가 쓸 때 모든 상황에서 같다고 외우지 않는다. 줄바꿈 처리 등의 차이가 있다. 간격을 잘게 나누면 지연이 해결된다는 메모도 보장이 아니다. **개선 방향:** 텍스트와 HTML의 목적을 분리하고 성공 표시·실제 현재값·타이머 주기를 따로 확인한다.

개선안은 원본을 수정한 결과가 아니다. 실제 오류, 수업용 단순화, 목적에 따른 선택을 구별해 판단한다.

<a id="teacher"></a>

## 7. 강사님 코드가 도움이 되는 비교



핵심 콘텐츠·카운터는 같아 중복 인용하지 않는다. 시계 차이는 표시 항목·갱신 요청 간격이며 밀리초가 필수 화면 정보라는 뜻은 아니다. 더 자주 갱신하는 내 코드가 모든 면에서 정확한 시계라고 단정하지 않는다.

<a id="results"></a>

## 8. 결과를 추적하고 한 가지 바꾸기

| 원본 단계 | 그때 내용 | 다음 대입 뒤 유지? |
| --- | --- | --- |
| textContent |h1 모양 글자 |교체됨 |
| innerText |h1 모양 글자 |교체됨 |
| innerHTML |h1 요소 |뒤 링크 대입으로 교체 |
| 마지막 HTML |눌러봐 링크 |최종 남음 |

원본 javascript: 링크는 클릭 시 alert를 실행하는 주소다. 글을 넣는 방법을 무조건 게시글 저장 기능과 같다고 생각하지 않는다. 단순 카운터는 '0'→0→1→화면 '1'의 변환으로 설명한다.

| 한 가지 변경 | 예상 | 이유 |
| --- | --- | --- |
| plain속성만innerHTML로 |두영역모두b요소 |해석방식변경 |
| 원래markup속성만textContent로 |b선택false |텍스트로넣음 |
| 원래count대입의Number만제거 |마지막01 |문자열연결 |

태그가 글자로 보이면 텍스트 대입을 확인한다. 반대로 사용자 글이 태그가 되면 HTML 해석 경로를 본다. 숫자 카운터가011처럼 이어지면 Number 변환이 있는지 확인한다. 시계가 멈추면 Date 생성 위치를 본다.

<a id="tips"></a>

## 9. 추가로 알면 좋은 것과 출처

> 💡 **TIP · 수업 범위 밖:** 외부 HTML 정화 도구·정밀 타이머 보정·padStart 시간 자릿수 등은 추가 학습이다. 현재 원본 콘텐츠와 시간 읽기 흐름을 먼저 설명한다.



이 절의 확장은 기본 문제의 필수 조건이 아니다. 📚 출처가 있다는 것과 수업 밖 기능이라는 것은 다른 구분이다.

<a id="practice"></a>

## 10. 복습과 빠른 정리

1. 태그 모양을 글자 그대로 넣으려면?
2. 카운터에서 읽은 값은 숫자인가?
3. Date를 반복 밖에서 한 번만 만들면 현재 시각이 자동 갱신되는가?

<details>
<summary>짧은 풀이 — 먼저 답한 뒤 확인</summary>

textContent 등 텍스트 속성을 쓴다. 읽은 값은 문자열이라 숫자 계산 전 변환한다. 새 순간을 얻으려면 반복 안마다 다시 Date를 만든다.

</details>

| 목적 | 확인 |
| --- | --- |
| 글자 |textContent·innerText |
| 구조해석 |innerHTML |
| 카운터 |문자열→Number→쓰기 |
| 시계 |매회Date생성 |

[장별 연습문제](실습/연습문제/12_JavaScript_DOM_콘텐츠생성과_스타일조작_연습문제.md)에서 예상·설명·수정을 이어 간다. 다음은 [요소 생성과 삽입](12-02_JavaScript_DOM_요소생성과_삽입.md)이다.

<!-- 이전 색인 이동 주소 보존 -->
<a id="section-1"></a>
<a id="section-2"></a>
<a id="section-3"></a>
<a id="section-4"></a>
<a id="section-5"></a>

[이 장의 목차](#chapter-toc)에서 현재 설명을 찾는다.
