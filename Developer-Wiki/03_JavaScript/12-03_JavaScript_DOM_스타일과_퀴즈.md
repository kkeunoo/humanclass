# 12-03. DOM 스타일·퀴즈 — 문자열 값을 읽고 고치기

[JavaScript 목차](README.md) · [이전: 요소 생성·삽입](12-02_JavaScript_DOM_요소생성과_삽입.md)

양쪽 `12_dom_content.html`의 후반부다. 앞에서 선택한 요소의 style을 바꾸고, 내 퀴즈 풀이로 선택·텍스트·클래스를 함께 복습한다.

<!-- chapter-toc -->

- [1. 직접 쓴 스타일과 계산된 스타일](#section-1)
- [2. '66px'에 5 더하기](#section-2)
- [3. style 요소도 만들어 붙일 수 있다](#section-3)
- [4. 내 퀴즈 풀이로 다시 확인하기](#section-4)
- [5. 복습](#section-5)
- [추가로 알면 좋은 것](#section-6)

<a id="section-1"></a>

## 1. 직접 쓴 스타일과 계산된 스타일

### 강사님 코드

출처: `teacher/workspace_html/javascript/12_dom_content.html` 330–345행 · **원본 발췌**

```javascript
        const clock = document.getElementById('clock')
        // CSS에서 -로 연결되는 프로퍼티 명은
        // 카멜케이스(단어를 대문자로 연결)로 변경해서 사용하면 된다
        // font-size >>>> fontSize
        // background-color >>>> backgroundColor
        clock.style.color = 'red'
        clock.style.fontSize = '1.5em'
        console.log('-----------------------')
        console.log(clock.style)
        console.log(clock.style.color)
        console.log(clock.style.height)
        clock.style.height = '50px'
        console.log(clock.style.height)

        let w = window.getComputedStyle(clock, null).getPropertyValue('width')
        console.log('w', w)
```

### 내 코드

출처: `me/workspace_html/javascript/12_dom_content.html` 326–342행 · **원본 발췌**

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

style.color에 'red', style.fontSize에 '1.5em'을 넣는다. CSS의 font-size를 JavaScript 속성으로 쓸 때는 fontSize처럼 쓴다.

| 읽는 방법 | 무엇을 읽는가 | 원본에서 주의할 점 |
| --- | --- | --- |
| clock.style.height | 요소의 인라인 스타일 | 아직 지정하지 않으면 ''일 수 있음 |
| getComputedStyle(clock, null).getPropertyValue('width') | 스타일 규칙 등을 적용한 결과 값 | 화면·부모 너비에 따라 달라짐 |

style은 JavaScript로 지정한 값뿐 아니라 HTML의 style 속성도 반영한다. 별도 CSS 규칙의 값까지 전부 들어 있는 것은 아니다. 내 주석의 ‘변수에 넣은 값만 출력’이나 ‘JS 값이 비어 있을 때 CSS 적용’은 이 구분으로 고쳐 읽는다. CSS 우선순위를 그런 두 단계로만 설명할 수는 없다. [MDN getComputedStyle](https://developer.mozilla.org/en-US/docs/Web/API/Window/getComputedStyle)

<a id="section-2"></a>

## 2. '66px'에 5 더하기

### 강사님 코드

출처: `teacher/workspace_html/javascript/12_dom_content.html` 349–355행 · **원본 발췌**

```javascript
        clock.style.height = parseInt(Math.random() * 100) +'px'
        console.log(clock.style.height)
        // 기존 높이보다 5px 크게
        // 66px + 5 : 66px5
        // console.log(Number('66px')) // NaN
        // console.log(parseInt('66px') + 5)
        clock.style.height = parseInt(clock.style.height) + 5 + 'px'
```

### 내 코드

출처: `me/workspace_html/javascript/12_dom_content.html` 348–356행 · **원본 발췌**

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

양쪽은 0–99 정수 높이를 px 문자열로 만든 뒤 5를 더한다. 최종 높이는 5–104px 범위다. 매번 무작위이므로 특정 숫자가 고정 정답은 아니다.

| 예시 입력 '66px' | 중간 값 | +5 후 다시 px 연결 |
| --- | --- | --- |
| 강사님 parseInt('66px') | 66 | '71px' |
| 내 Number('66px'.split('px')[0]) | 66 | '71px' |

둘 다 원본의 정수 px 값에서는 맞다. 강사님 방법은 짧고, 내 방법은 단위를 분리하는 과정을 볼 수 있다. Number('66px')는 NaN이고 '66px' + 5는 '66px5'다. 다른 단위나 소수 높이에까지 이 풀이를 그대로 일반화하지 않는다.

<a id="section-3"></a>

## 3. style 요소도 만들어 붙일 수 있다

### 강사님 코드

출처: `teacher/workspace_html/javascript/12_dom_content.html` 312–318행 · **원본 발췌**

```javascript
        style.innerText = `
                #board {
                    border: 1px solid red;
                }
        `
        // body에 style을 넣는다
        body.append(style)
```

### 내 코드

출처: `me/workspace_html/javascript/12_dom_content.html` 300–306행 · **원본 발췌**

```javascript
            const style = document.createElement('style')
            style.innerText = `
                #board {
                    border: 1px solid red;
                }
            `
            body.append(style)
```

강사님 발췌의 style과 body는 앞에서 각각 createElement('style'), querySelector('body')로 준비한 변수다. 양쪽 모두 style 요소에 CSS 글자를 넣고 body에 연결하여 #board 테두리를 바꾼다. 원본의 script 요소 생성·alert 부분은 **주석 처리된 코드**라 자동 실행 결과에 포함하지 않는다.

<a id="section-4"></a>

## 4. 내 퀴즈 풀이로 다시 확인하기

강사님 파일 후반에는 주로 문제 설명이 있고 완성 풀이가 없다. 내 파일에는 대상 HTML과 실행 풀이가 있다. 강사님 주석을 완성 코드처럼 만들지 않고 내 풀이를 기준으로 복습한다.

### 문제1: 문장 뒤에 글자 붙이기

출처: `me/workspace_html/javascript/12_dom_content.html` 377–380행 · **원본 발췌**

```javascript
            let Q1_query = document.querySelector('.quiz.q1')
            // console.log(quiz1)
            Q1_query.innerText += ' 쮸인님~♥'
            console.log(Q1_query.innerText)
```

내 문서에는 .quiz.q1 요소가 스크립트 앞에 있다. 기존 글자 '힌트만 달라' 뒤에 ' 쮸인님~♥'가 붙는다. 강사님 파일에는 이 q1 요소가 문제 주석 안에만 있으므로, 내 풀이를 강사님 HTML에 그대로 넣으면 선택 결과가 null일 수 있다.

### 문제2: q2 클래스가 있는 요소 수

출처: `me/workspace_html/javascript/12_dom_content.html` 394–413행 · **원본 발췌**

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

전체 div.quiz 6개 중 q2는 2개다. q2-1·q2-2는 q2와 **서로 다른 클래스 이름**이다. classList.contains('q2')는 이름 일부가 아닌 클래스 하나가 있는지 판단한다. 노란 배경과 굵은 글자는 찾은 요소를 확인하기 위한 내 표시다.

### 문제3: q2 요소의 글자 읽기

출처: `me/workspace_html/javascript/12_dom_content.html` 423–432행 · **원본 발췌**

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

첫 요소의 글자는 '퀴즈2'이고 두 번째는 공백 세 칸이다. textContent는 그 공백도 읽는다. 강사님 문제 주석 중 예상 글자를 '퀴즈2-1'로 적은 부분은 실제 q2 요소의 내용과 다르다. 내 결과를 그 주석에 맞추어 바꾸지 않는다.

### 문제4: 빈 글자 채우기

출처: `me/workspace_html/javascript/12_dom_content.html` 440–462행 · **원본 발췌**

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

원본의 일반 표시 상태에서 공백만 있는 두 번째 q2의 innerText는 빈 문자열이므로 '비어있음'과 빨간 배경을 넣는다. 보이는 글자 기준이라는 점을 의도한 풀이로 읽는다. 저장된 텍스트의 양 끝 공백을 제외해 검사하려면 이미 배운 trim을 연결할 수 있다.

**설명용 교정 예제 — 원본 발췌 아님**

```javascript
if (Q4_query[i].textContent.trim() === '') {
    Q4_query[i].textContent = '비어있음'
}
```

이 예제는 for문 안에서 쓰는 조건·대입 부분이다. 전체 문서의 숨겨진 요소까지 판별하는 새 도구로 확대하지 않는다.

<a id="section-5"></a>

## 5. 복습

1. style.height가 ''이면 실제 요소 높이도 반드시 0인가?
2. classList.contains('q2')가 q2-1에도 참인가?
3. 공백만 있는 textContent를 빈 글자로 취급하려면?

<details>
<summary>정답</summary>

1. 아니다. 인라인으로 지정한 height가 없다는 뜻일 수 있다.
2. 아니다. 정확한 클래스 이름을 검사한다.
3. trim()으로 양 끝 공백을 제거한 결과가 ''인지 비교한다.

</details>

<a id="section-6"></a>

## 추가로 알면 좋은 것

다양한 CSS 단위를 처리하는 범용 크기 조절기나 스타일 관리 도구는 별도 확장이다. 기본 학습은 원본의 정수 px 계산과 실제 퀴즈 풀이까지다.

