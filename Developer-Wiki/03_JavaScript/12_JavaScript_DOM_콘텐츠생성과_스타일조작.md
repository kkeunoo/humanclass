# 12. DOM 콘텐츠 — 글자로 넣을지 HTML로 해석할지 정하기

[JavaScript 목차](README.md) · [이전: 속성·클래스](11-02_JavaScript_DOM_속성과_클래스.md) · [다음: 요소 생성·삽입](12-02_JavaScript_DOM_요소생성과_삽입.md)

기준은 양쪽 `12_dom_content.html`이다. 원본이 길어 **콘텐츠와 타이머 → 요소 생성·표 만들기 → 스타일과 퀴즈**로 나누었다. 이 장은 같은 요소에 값을 읽고 쓰는 차이부터 확인한다.

<!-- chapter-toc -->

- [1. textContent·innerText·innerHTML](12_JavaScript_DOM_콘텐츠생성과_스타일조작.md#section-1)
- [2. 숫자처럼 보여도 읽은 값은 문자열이다](12_JavaScript_DOM_콘텐츠생성과_스타일조작.md#section-2)
- [3. 현재 시각은 반복할 때마다 다시 읽는다](12_JavaScript_DOM_콘텐츠생성과_스타일조작.md#section-3)
- [4. 복습](12_JavaScript_DOM_콘텐츠생성과_스타일조작.md#section-4)
- [추가로 알면 좋은 것](12_JavaScript_DOM_콘텐츠생성과_스타일조작.md#section-5)

<a id="section-1"></a>

## 1. textContent·innerText·innerHTML

| 속성 | 읽을 때 | 문자열을 대입할 때 |
| --- | --- | --- |
| textContent | 하위 텍스트를 공백·줄바꿈도 포함해 읽음 | 태그 문법을 일반 글자로 넣음 |
| innerText | 렌더링되는 글자를 기준으로 읽음 | 태그 문법은 글자로 넣고 줄바꿈은 표시용 줄바꿈으로 처리 |
| innerHTML | 내부 HTML 마크업을 문자열로 읽음 | 문자열을 HTML로 해석하여 내부 내용을 교체 |

innerText는 스타일과 표시 상태의 영향을 받는다. 두 텍스트 속성이 언제나 같다고 외우지 않는다. 특히 ‘공백을 읽는 결과’와 ‘공백이 화면에 보이는 결과’는 다를 수 있다. [MDN innerText](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/innerText)

### 강사님 코드

출처: `teacher/workspace_html/javascript/12_dom_content.html` 88–96행 · **원본 발췌**

```javascript
        // textContent, innerText는 tag도 글씨로 인식한다
        msg.textContent = '<h1>h1제목</h1>   a  b    c'
        msg.innerText = '<h1>h1제목</h1>   a  b    c'

        // innerHTML은 tag는 tag로 인식한다
        msg.innerHTML = '<h1>h1제목</h1>   a  b    c'
        msg.innerHTML += 'd'

        msg.innerHTML = '<a href="javascript:alert(1);alert(2);">눌러봐</a>'
```

### 내 코드

출처: `me/workspace_html/javascript/12_dom_content.html` 86–98행 · **원본 발췌**

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

처음 두 대입은 h1이라는 글자와 꺾쇠를 텍스트로 넣는다. innerHTML 대입에서는 h1 요소가 만들어진다. 이후 += 'd'는 기존 HTML 문자열 뒤에 d를 붙여 다시 넣는다. 마지막 대입은 앞 내용을 전부 덮으므로 **최종 화면에 남는 것은 ‘눌러봐’ 링크**다. 모든 중간 결과가 함께 남는 예제가 아니다.

마지막 링크는 누르면 alert를 실행하는 javascript: 주소다. 원본은 HTML 해석의 영향을 보여 주는 예제로 읽는다. 직접 입력받은 문자열을 innerHTML에 그대로 넣으면 원치 않는 HTML이나 실행 동작이 들어갈 수 있다. 글자 출력 목적이면 이미 배운 textContent/innerText를 쓴다. 이는 수업 코드의 동작을 바로잡는 설명이며 새 보안 도구를 필수로 추가하는 것이 아니다. [MDN innerHTML](https://developer.mozilla.org/en-US/docs/Web/API/Element/innerHTML)

<a id="section-2"></a>

## 2. 숫자처럼 보여도 읽은 값은 문자열이다

### 강사님 코드

출처: `teacher/workspace_html/javascript/12_dom_content.html` 100–107행 · **원본 발췌**

```javascript
        setInterval( function(){
            const count = document.querySelector('#count')
            let cnt = count.textContent
            // console.log(cnt, typeof cnt)

            cnt = Number(cnt) + 1
            count.innerText = cnt
        }, 1000 )
```

### 내 코드

출처: `me/workspace_html/javascript/12_dom_content.html` 102–111행 · **원본 발췌**

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

양쪽은 같은 흐름이다. 처음 #count의 글자는 '0'이다. 읽으면 문자열이므로 Number로 숫자로 바꾼 뒤 1을 더하고 다시 화면에 쓴다.

```text
화면 '0' → 문자열 '0' → Number로 0 → 0 + 1 → 화면 '1'
```

Number를 생략하면 '0' + 1은 '01'이다. setInterval은 지정 간격으로 실행을 요청하지만 정확한 시각을 보장하지 않는다. 함수 안에서 요소를 선택한다고 ‘무조건 동작’하는 것도 아니다. 실행 시점에 #count가 있어야 한다. 타이머의 등록·취소는 [08-03](08-03_JavaScript_타이머와_취소.md)에서 다룬다.

<a id="section-3"></a>

## 3. 현재 시각은 반복할 때마다 다시 읽는다

### 강사님 코드

출처: `teacher/workspace_html/javascript/12_dom_content.html` 110–120행 · **원본 발췌**

```javascript
        setInterval( function(){
            const now = new Date()
            const m = now.getMinutes()
            const s = now.getSeconds()
            const ms = now.getMilliseconds()

            const clock = document.querySelector('#clock')

            const time = m +'분 '+ s +'초.'+ ms
            clock.textContent = time
        }, 3000 )
```

### 내 코드

출처: `me/workspace_html/javascript/12_dom_content.html` 117–135행 · **원본 발췌**

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

| 비교 | 강사님 | 내 코드 |
| --- | --- | --- |
| 표시 | 분·초·밀리초 | 시·분·초·밀리초 |
| 지정 간격 | 3000ms | 250ms |
| Date 생성 | 콜백 안 | 콜백 안 |

두 코드 모두 실행할 때마다 new Date()로 그때의 시각을 읽는다. Date 객체를 밖에서 한 번만 만들고 계속 같은 객체에서 읽으면 현재 시각으로 자동 갱신되지 않는다.

내 코드는 더 자주 갱신하고 시(hour)도 보여 준다. 다만 주석의 ‘간격을 잘게 나누면 delay 해결’은 보장할 수 없다. 간격을 줄이면 갱신 요청 횟수가 늘 뿐이고, 브라우저가 바쁘면 지연될 수 있다. 밀리초는 필수 표시가 아니라 두 원본에서 시간을 관찰하기 위해 넣은 값이다.

<a id="section-4"></a>

## 4. 복습

1. `<b>안녕</b>`을 태그 없이 글자 그대로 출력하려면?
2. count.textContent + 1과 Number(count.textContent) + 1의 차이는?
3. 이 원본을 실행하면 h1과 ‘눌러봐’ 링크가 모두 남는가?
4. Date를 콜백 안에서 생성하는 이유는?

<details>
<summary>정답</summary>

1. textContent 또는 innerText에 문자열을 대입한다.
2. 전자는 문자열 연결, 후자는 숫자 덧셈이다.
3. 아니다. 마지막 innerHTML 대입이 앞 내용을 교체한다.
4. 반복 실행 시점의 시각을 새로 얻기 위해서다.

</details>

<a id="section-5"></a>

**이 장을 읽은 뒤:** [장별 연습문제 풀기](실습/연습문제/12_JavaScript_DOM_콘텐츠생성과_스타일조작_연습문제.md)

## 추가로 알면 좋은 것

외부 HTML을 허용할 때 쓰는 정화 도구, 정밀한 타이머 보정, padStart로 시간 자릿수를 맞추는 확장은 이 장의 필수 학습에서 제외한다.

