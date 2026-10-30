# 12-03. DOM 스타일과 퀴즈 — 단위 문자열과 클래스 조건

[JavaScript 목차](README.md) · [읽기 안내](00_JavaScript_V3_동작_백과_읽기법.md)

요소의 글자색·높이를 바꾸려면 CSS값과 JavaScript값을 연결한다. 값이 66px라는 문자열인지 숫자66인지 구별하고, CSS규칙의 결과와 인라인 style도 나누어 읽는다.

<a id="chapter-toc"></a>

**이 장의 목차:** [목표](#learn) · [개념](#concepts) · [예제](#example) · [내 코드](#my-code) · [연결](#connections) · [평가](#review) · [비교](#teacher) · [결과·실험](#results) · [TIP·출처](#tips) · [복습](#practice)

<a id="learn"></a>

## 1. 이 장에서 배울 것

style과 계산된 스타일을 비교한다. px분리·숫자 계산·단위 재결합을 설명하고 클래스 개수·글자·빈값 퀴즈를 검토한다.

입력·현재 상태·실행 순서·결과를 분리해 설명한다. 실제 수업 원본은 아래에 표시하고, 원본에 없는 선택 학습은 9절 TIP에 둔다.

<a id="concepts"></a>

## 2. 무엇이며, 왜 필요한가

element.style은 인라인 스타일을 다룬다. JavaScript로 쓴 값뿐 아니라 HTML의 style 속성도 반영하지만 별도 CSS 규칙의 모든 값이 여기에 들어 있지는 않다. style.height가 빈 문자열이어도 실제 높이가0이라는 뜻은 아니다. 계산된 값은 getComputedStyle로 확인한다.

| 읽기·쓰기 | 의미 |
| --- | --- |
| style.fontSize |CSS font-size의 JavaScript 속성 |
| style.backgroundColor |CSS background-color의 JavaScript 속성 |
| style.height |인라인 높이 문자열 |
| getComputedStyle(e).getPropertyValue('height') |규칙 적용 후 값 |

66px에5px를 더하려면 px 부분과 숫자를 구분한다. parseInt('66px')는66이며 +5 뒤 'px'를 붙이면71px다. Number('66px')는 NaN, '66px'+5는 '66px5'다. 내 split 후 Number도 정수 px 조건에서는 같은71px를 만든다. 소수·다른 단위를 일괄 처리하는 범용 도구라고 소개하지 않는다.

classList.contains('q2')는 q2라는 항목 전체를 검사한다. q2-1·q2-2는 다른 이름이다. 공백만 있는 글을 빈값으로 보려면 textContent.trim()==='' 같은 조건을 쓸 수 있다. 보이는 글자 기준 innerText와 저장 텍스트 기준 검사를 같게 외우지 않는다.

> 📚 **출처 · 본문 설명 확인:** [MDN HTMLElement.style](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/style), [getComputedStyle](https://developer.mozilla.org/en-US/docs/Web/API/Window/getComputedStyle), [classList](https://developer.mozilla.org/en-US/docs/Web/API/Element/classList). 배운 기능의 뜻을 확인한 근거다. 예제·표·풀이 흐름은 수업 코드를 바탕으로 새로 작성했으며 외부 문장을 직접 인용하지 않았다. 확인일: 2026-10-28.

<a id="example"></a>

## 3. 작은 예제로 먼저 이해하기

**새 설명 예제 · 전체 스크립트.** [HTML 실행 파일](실습/책형_복습/12-03_JavaScript_DOM_스타일과_퀴즈.html)과 같은 폴더의 [JS 파일](실습/책형_복습/12-03_JavaScript_DOM_스타일과_퀴즈.js)을 함께 내려받는다. HTML을 브라우저로 열고 Console에서 결과를 확인한다. script는 필요한 HTML 뒤에 연결한다. 콘솔 출력은 페이지 본문에 자동으로 쓰이지 않는다.

**먼저 준비할 HTML · body 안:**

```html
    <div id="box">크기 관찰</div>
    <div class="quiz q2">퀴즈2</div>
    <div class="quiz q2">   </div>
    <div class="quiz q2-1">다른 클래스</div>
```

**위 파일 head의 style:**

```css
        #box { height: 66px; }
```

```javascript
const box = document.getElementById('box');
console.log(`인라인=[${box.style.height}]`);
const height = getComputedStyle(box).getPropertyValue('height');
console.log(height);
box.style.height = parseInt(height) + 5 + 'px';
console.log(box.style.height);
const quizzes = document.querySelectorAll('.quiz');
let count = 0;
for (let i = 0; i < quizzes.length; i++) {
    if (quizzes[i].classList.contains('q2')) {
        count++;
    }
    if (quizzes[i].textContent.trim() === '') {
        quizzes[i].textContent = '비어있음';
    }
}
console.log(count);
console.log(quizzes[1].textContent);
```

높이를 CSS 규칙으로만 주어 인라인값은 빈 문자열이지만 계산된 높이는66px다. 숫자로 읽어5 더하고 px를 붙여 인라인71px로 쓴다. q2는 두 개이고 q2-1은 세지 않는다. 두 번째 quiz의 공백은 trim 뒤 비어 있어 글자를 채운다. 원본 여섯 요소를 세 개로 줄인 새 예제임을 구분한다.

**예상 출력 또는 관찰:**

```text
인라인=[]
66px
71px
2
비어있음
```

<a id="my-code"></a>

## 4. 내가 작성한 코드를 따라 읽기

아래는 원본의 일부다. 원본에 의존하는 앞 선언·HTML·함수는 다음 절의 연결까지 읽는다. 주석의 잘못된 표현도 원문대로 보존하고 설명에서 교정한다.

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_html/javascript/12_dom_content.html` 326–342행

```javascript
            const clock = document.getElementById('clock')
            clock.style.color = 'red'
            // 아래처럼 style에 CSS에 직접적으로 주는 경우 -로 연결되는 프로퍼티는
            // 카멜케이스로 font-size > fontSize 변경해서 사용함
            clock.style.fontSize = '1.5em'

            console.log(clock.style)
            console.log(clock.style.color)
            // 기존 CSS에 있는 값이 아래 출력물에 들어가있지는 않아서 공백으로 나옴("")
            // 변수에 넣어서 적용한 값만 출력물로 볼 수 있음
            // javascript 값이 비어있을 때 css를 적용시킴(우선순위)
            console.log(clock.style.height)
            clock.style.height = '50px'
            console.log(clock.style.height)

            let w = window.getComputedStyle(clock, null).getPropertyValue('width')
            console.log('w', w)
```

**발췌 바로 풀이:** style.color에 'red', style.fontSize에 '1.5em'을 넣는다. CSS의 font-size를 JavaScript 속성으로 쓸 때는 fontSize처럼 쓴다.

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_html/javascript/12_dom_content.html` 348–356행

```javascript
            // let m = clock.style.height = parseInt(Math.random() * 100) + 'px'
            clock.style.height = parseInt(Math.random() * 100) + 'px'
            console.log(clock.style.height)
            // let n = Number(m.split('px')[0])
            let n = Number(clock.style.height.split('px')[0])
            console.log(n+5, typeof n)
            let t = n+5
            clock.style.height = t + 'px'
            console.log(clock.style.height)
```

**발췌 바로 풀이:** 양쪽은 0–99 정수 높이를 px 문자열로 만든 뒤 5를 더한다. 최종 높이는 5–104px 범위다. 매번 무작위이므로 특정 숫자가 고정 정답은 아니다.

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_html/javascript/12_dom_content.html` 300–306행

```javascript
            const style = document.createElement('style')
            style.innerText = `
                #board {
                    border: 1px solid red;
                }
            `
            body.append(style)
```

**발췌 바로 풀이:** 강사님 발췌의 style과 body는 앞에서 각각 createElement('style'), querySelector('body')로 준비한 변수다. 양쪽 모두 style 요소에 CSS 글자를 넣고 body에 연결하여 #board 테두리를 바꾼다. 원본의 script 요소 생성·alert 부분은 **주석 처리된 코드**라 자동 실행 결과에 포함하지 않는다.

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_html/javascript/12_dom_content.html` 377–380행

```javascript
            let Q1_query = document.querySelector('.quiz.q1')
            // console.log(quiz1)
            Q1_query.innerText += ' 쮸인님~♥'
            console.log(Q1_query.innerText)
```

**발췌 바로 풀이:** 내 문서에는 .quiz.q1 요소가 스크립트 앞에 있다. 기존 글자 '힌트만 달라' 뒤에 ' 쮸인님~♥'가 붙는다. 강사님 파일에는 이 q1 요소가 문제 주석 안에만 있으므로, 내 풀이를 강사님 HTML에 그대로 넣으면 선택 결과가 null일 수 있다.

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_html/javascript/12_dom_content.html` 394–413행

```javascript
            let Q2_query = document.querySelectorAll('div.quiz')
            // console.log(quiz2, typeof quiz2)
            // 전체 가져온 div 개수와, q2가 들어온 div의 개수 파악 변수 선언
            let Q2_divCnt = 0
            let Q2_isCnt = 0

            for(let i=0; i<Q2_query.length; i++) {
                // isQ2로 배열로 가져온 값에서 'q2 class'가 있을 경우 true 반환
                let isQ2 = Q2_query[i].classList.contains('q2')
                Q2_divCnt++ // 총 div개수 확인용
                
                // 'q2'라는 class가 있어 true가 반환이 되었을 경우,
                // 개수를 카운팅하고 알아보기 쉽도록 bg, fontWeight 변경
                if(isQ2 == true) {
                    Q2_isCnt++
                    Q2_query[i].style.background = 'yellow'
                    Q2_query[i].style.fontWeight = 'bold'
                }
            }
            console.log(`${Q2_divCnt}개 div중, q2포함은 ${Q2_isCnt}개`)
```

**발췌 바로 풀이:** 전체 div.quiz 6개 중 q2는 2개다. q2-1·q2-2는 q2와 **서로 다른 클래스 이름**이다. classList.contains('q2')는 이름 일부가 아닌 클래스 하나가 있는지 판단한다. 노란 배경과 굵은 글자는 찾은 요소를 확인하기 위한 내 표시다.

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_html/javascript/12_dom_content.html` 423–432행

```javascript
            let Q3_query = document.querySelectorAll('div.quiz.q2')
            // q2가 가지는 태그의 글씨를 저장하기 위한 Q3_str 빈 변수 선언
            let Q3_str = ''
            // console.log(Q3_query)
            for(let i=0; i<Q3_query.length; i++) {
                // for문으로 q2를 가진 길이만큼 반복을 돌게 하며,
                // 출력 결과값을 쉽게 알아볼 수 있도록 벡틱으로 각 배열의 값 출력
                Q3_str += `${i+1}번째 값 : ${Q3_query[i].textContent}\n`
            }
            console.log(Q3_str)
```

**발췌 바로 풀이:** 첫 요소의 글자는 '퀴즈2'이고 두 번째는 공백 세 칸이다. textContent는 그 공백도 읽는다. 강사님 문제 주석 중 예상 글자를 '퀴즈2-1'로 적은 부분은 실제 q2 요소의 내용과 다르다. 내 결과를 그 주석에 맞추어 바꾸지 않는다.

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_html/javascript/12_dom_content.html` 440–462행

```javascript
            let Q4_query = document.querySelectorAll('div.quiz')
            // console.log(quiz4)

            // 전체 div를 검사하기 위해 for문으로 가져온 배열의 길이만큼 돌게함
            for(let i=0; i<Q4_query.length; i++) {
                // 각 배열 중에서 innerText로 글씨가 없는 곳을 확인하고,
                // 다시 innerText로 '비어있음' 으로 글씨를 채워줌
                // textContent로 했을 땐 공백까지 모두 포함하기 때문에,
                // 이럴 경우에는 trim()을 이용해서 공백을 제거 후 비교도 가능
                // if(Q4_query[i].textContent == '') {
                if(Q4_query[i].innerText == '') {
                    Q4_query[i].innerText = '비어있음'
                    Q4_query[i].style.background = 'red'
                }
                // 각 div별로 어떤 text가 들어가 있는지 확인하기 위한 출력물
                console.log(`${i+1}번 div내용 : ${Q4_query[i].innerText}`)

                // 만약 '비어있음'이 들어갔을 때 구분하기 쉽도록 bg 설정
                // if(Q4_query[i].innerText == '비어있음') {
                //     // console.log('비어비어')
                //     Q4_query[i].style.background = 'red'
                // }
            }
```

**발췌 바로 풀이:** 원본의 일반 표시 상태에서 공백만 있는 두 번째 q2의 innerText는 빈 문자열이므로 '비어있음'과 빨간 배경을 넣는다. 보이는 글자 기준이라는 점을 의도한 풀이로 읽는다. 저장된 텍스트의 양 끝 공백을 제외해 검사하려면 이미 배운 trim을 연결할 수 있다.

내 clock은 color:red·fontSize:1.5em을 쓰고 style.height를 읽은 뒤50px를 대입한다. 너비 w는 계산된 스타일로 읽는다. 원본의 무작위 높이는 매번 달라66px는 고정 원본 출력이 아닌 설명 조건이다. style 요소를 만들어 CSS 문자열을 넣고 body에 append하는 부분도 있다. script 생성·alert는 주석이어서 실행 결과에 포함하지 않는다.

<a id="connections"></a>

## 5. 선언·호출·파일이 연결되는 흐름

요소 선택 → 인라인 또는 계산값 읽기 → 문자열 해석 → 숫자 계산 → 단위 문자열 → style 대입 순서다. 원본의 style 변수는 createElement("style"), body는 querySelector("body")로 준비한 것이다. 내 퀴즈는 스크립트 앞에 실제 대상 HTML이 있지만 강사님 q1은 문제 주석 안에 있어 내 풀이만 붙이면 null일 수 있다.

<a id="review"></a>

## 6. 잘한 점·아쉬운 점·개선 방향

**잘한 점:** 내 퀴즈는 일치 개수와 전체 개수를 함께 출력하고 찾은 요소에 색·굵기를 주어 확인하기 좋다. **교정:** JS값이 비어 있을 때만 CSS가 적용된다는 단순 서열은 정확하지 않다. style은 인라인 읽기이고 별도 규칙·우선순위가 따로 있다. **개선 방향:** 고정 px 수업 계산의 전제와 다른 단위의 한계를 함께 적는다.

개선안은 원본을 수정한 결과가 아니다. 실제 오류, 수업용 단순화, 목적에 따른 선택을 구별해 판단한다.

<a id="teacher"></a>

## 7. 강사님 코드가 도움이 되는 비교



강사님의 parseInt는 정수 px를 짧게 읽고 내 split 후 Number는 단위 분리를 눈으로 볼 수 있다. 현재 조건에서는 둘 다 맞고 어느 쪽도 모든 단위 해석의 정답은 아니다. 강사님 후반은 문제 위주라 내 완성 풀이를 그쪽 원문으로 바꾸어 소개하지 않는다.

<a id="results"></a>

## 8. 결과를 추적하고 한 가지 바꾸기

| 내 원본 퀴즈 | 결과·판단 |
| --- | --- |
| q1 문장 추가 |기존 문장 뒤 새 글자 |
| div.quiz 중 q2 |6개 중2개 |
| q2 글자 읽기 |퀴즈2와 공백3칸 |
| 빈 글자 채우기 |일반 표시 상태의 공백 요소에 비어있음 |

강사님 문제 주석의 예상 문구 퀴즈2-1과 실제 q2 요소 글자는 다르다. 내 결과를 틀린 주석에 맞추지 않는다. 공백 검사는 실제 표시 기준인지, 양끝을 제거한 텍스트 기준인지 요구사항으로 정한다.

| 한 가지 변경 | 예상 | 이유 |
| --- | --- | --- |
| CSS높이만80px |계산80·새인라인85px |입력크기변경 |
| 두번째class를q2-2로 |q2개수1 |정확한항목비교 |
| 원래빈값검사trim만제거 |공백요소를안채움 |공백은빈문자열아님 |

style에 값이 없다고 선택 실패와 혼동하지 않는다. 높이 계산이 NaN이면 단위가 붙은 문자열을 Number로 바로 읽었는지 본다. 클래스 일부가 같아도 contains는 다른 항목이면 false다.

<a id="tips"></a>

## 9. 추가로 알면 좋은 것과 출처

> 💡 **TIP · 수업 범위 밖:** 다양한 단위를 처리하는 범용 크기 조절기·스타일 관리 도구는 추가 학습이다. 현재 원본의 정수 px와 실제 퀴즈 풀이까지 먼저 이해한다.



이 절의 확장은 기본 문제의 필수 조건이 아니다. 📚 출처가 있다는 것과 수업 밖 기능이라는 것은 다른 구분이다.

<a id="practice"></a>

## 10. 복습과 빠른 정리

1. style.height가 비었으면 실제 높이도0인가?
2. q2-1에 contains(q2)는 참인가?
3. 공백만 있는 textContent를 비었다고 검사하려면?

<details>
<summary>짧은 풀이 — 먼저 답한 뒤 확인</summary>

반드시0은 아니며 인라인값이 없을 수 있다. 정확한 항목이 다르면 false다. trim 후 빈 문자열과 비교할 수 있다.

</details>

| 구분 | 확인 |
| --- | --- |
| 인라인/계산 |style/getComputedStyle |
| 높이 |숫자·단위분리 |
| 클래스 |항목전체비교 |
| 빈값 |표시·trim정책 |

[장별 연습문제](실습/연습문제/12-03_JavaScript_DOM_스타일과_퀴즈_연습문제.md)에서 예상·설명·수정을 이어 간다. 다음은 [폼 입력](13_JavaScript_DOM_폼요소와_입력값처리.md)이다.

<!-- 이전 색인 이동 주소 보존 -->
<a id="section-1"></a>
<a id="section-2"></a>
<a id="section-3"></a>
<a id="section-4"></a>
<a id="section-5"></a>
<a id="section-6"></a>

[이 장의 목차](#chapter-toc)에서 현재 설명을 찾는다.
