# 13. 폼 요소 — 현재 값과 선택 상태를 읽기

[JavaScript 목차](README.md) · [읽기 안내](00_JavaScript_V3_동작_백과_읽기법.md)

HTML의 입력 요소는 사용자가 글자를 바꾸거나 항목을 고르는 동안 상태가 달라진다. JavaScript는 처음 HTML에 적힌 글자만 읽는 것이 아니라 실행하는 순간의 값을 읽는다. 무엇을 읽고 언제 바꾸었는지 순서까지 알아야 결과를 설명할 수 있다.

<a id="chapter-toc"></a>

**이 장의 목차:** [목표](#learn) · [개념](#concepts) · [예제](#example) · [내 코드](#my-code) · [연결](#connections) · [평가](#review) · [비교](#teacher) · [결과·실험](#results) · [TIP·출처](#tips) · [복습](#practice)

<a id="learn"></a>

## 1. 이 장에서 배울 것

value와 checked를 구별하고 input·radio·checkbox·select·textarea의 현재 상태를 읽는다. 목록과 요소의 차이, 날짜 문자열, 한 번 실행과 이벤트 갱신의 차이까지 연결한다.

입력·현재 상태·실행 순서·결과를 분리해 설명한다. 실제 수업 원본은 아래에 표시하고, 원본에 없는 선택 학습은 9절 TIP에 둔다.

<a id="concepts"></a>

## 2. 무엇이며, 왜 필요한가

폼 요소는 글자를 입력하거나 항목을 고르는 HTML 요소다. 텍스트 입력의 value는 현재 문자열, 체크박스·라디오의 checked는 현재 선택을 나타내는 boolean이다. value가 'a'라고 checked도 'a'인 것은 아니다. 선택하지 않은 체크박스에도 그 항목의 value는 있다.

| 요소 | 읽을 정보 | 중요한 차이 |
| --- | --- | --- |
| input text·password |value |현재 입력 문자열 |
| input date |value |유효한 날짜의 yyyy-mm-dd 문자열 |
| radio |checked·value |같은 name 그룹에서 하나 선택 |
| checkbox |checked·value |여러 개 선택 가능 |
| select |value |현재 선택 option의 값 |
| textarea |value |사용자가 입력한 줄바꿈 포함 글자 |

querySelectorAll은 여러 요소의 목록을 준다. checks2.checked가 아니라 checks2[i].checked처럼 목록 안의 요소를 읽어야 한다. 선택자가 :checked이면 선택된 항목만, :not(:checked)이면 선택되지 않은 항목만 모은다. 라디오를 querySelector로 찾을 때는 아무것도 선택되지 않았다면 null일 가능성도 생각한다.

속성에 적은 초기값·현재 DOM 속성·그 값을 읽은 변수는 같은 말이 아니다. let saved=input.value 뒤 입력이 바뀌어도 saved가 자동 갱신되지는 않는다. 다시 읽거나 이후 이벤트 장처럼 변경 시점에 읽는 함수를 연결해야 한다.

> 📚 **출처 · 본문 설명 확인:** [MDN input.value](https://developer.mozilla.org/en-US/docs/Web/API/HTMLInputElement/value), [input.checked](https://developer.mozilla.org/en-US/docs/Web/API/HTMLInputElement/checked), [select.value](https://developer.mozilla.org/en-US/docs/Web/API/HTMLSelectElement/value), [textarea.value](https://developer.mozilla.org/en-US/docs/Web/API/HTMLTextAreaElement/value). 배운 기능의 뜻을 확인한 근거다. 예제·표·풀이 흐름은 수업 코드를 바탕으로 새로 작성했으며 외부 문장을 직접 인용하지 않았다. 확인일: 2026-10-28.

<a id="example"></a>

## 3. 작은 예제로 먼저 이해하기

**새 설명 예제 · 전체 스크립트.** [HTML 실행 파일](실습/책형_복습/13_JavaScript_DOM_폼요소와_입력값처리.html)과 같은 폴더의 [JS 파일](실습/책형_복습/13_JavaScript_DOM_폼요소와_입력값처리.js)을 함께 내려받는다. HTML을 브라우저로 열고 Console에서 결과를 확인한다. script는 필요한 HTML 뒤에 연결한다. 콘솔 출력은 페이지 본문에 자동으로 쓰이지 않는다.

**먼저 준비할 HTML · body 안:**

```html
    <label for="learner">이름</label><input id="learner" value="민지">
    <label><input class="topic" type="checkbox" value="html" checked>HTML</label>
    <label><input class="topic" type="checkbox" value="css">CSS</label>
    <label><input name="group" type="radio" value="A" checked>A</label>
    <label><input name="group" type="radio" value="B">B</label>
    <label for="lang">언어</label>
    <select id="lang"><option value="python">Python</option><option value="java">Java</option></select>
    <label for="memo">메모</label><textarea id="memo">첫 줄
둘째 줄</textarea>
    <div id="view"></div>
```

```javascript
const learner = document.getElementById('learner');
console.log(learner.value);
const topics = document.querySelectorAll('.topic');
console.log(topics[0].checked);
console.log(document.querySelectorAll('.topic:checked').length);
console.log(document.querySelector('[name=group]:checked').value);
const radios = document.querySelectorAll('[name=group]');
radios[1].checked = true;
console.log(document.querySelector('[name=group]:checked').value);
const lang = document.getElementById('lang');
console.log(lang.value);
lang.value = 'java';
console.log(lang.value);
const memo = document.getElementById('memo');
console.log(memo.value.indexOf('\n'));
document.getElementById('view').innerText = memo.value;
```

초기 HTML에서 HTML 체크박스와 A 라디오를 선택했다. 따라서 처음 선택 개수는1, 라디오 값은A다. B의 checked를 true로 바꾸면 같은 그룹 A가 해제되고 현재 선택을 다시 찾을 때 B가 나온다. select는 Python을 먼저 읽고 java를 대입한 뒤 Java 선택을 읽는다. 메모의 줄바꿈은 인덱스3이며 innerText로 일반 글자와 줄바꿈을 보여 준다. 여기에는 입력 때마다 다시 실행하는 이벤트가 없다.

**예상 출력 또는 관찰:**

```text
민지
true
1
A
B
python
java
3
```

<a id="my-code"></a>

## 4. 내가 작성한 코드를 따라 읽기

아래는 원본의 일부다. 원본에 의존하는 앞 선언·HTML·함수는 다음 절의 연결까지 읽는다. 주석의 잘못된 표현도 원문대로 보존하고 설명에서 교정한다.

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_html/javascript/13_dom_form.html` 47–54행

```javascript
            // input type에 value값이 있지만, 가져오는건 입력 된 최신 데이터
            // text.value로 input text의 값을 바꿔줄 수 있음
            const text = document.querySelector('#id')
            text.value = '12345'
            console.log('text', text.value)
            
            const password = document.querySelector('#pw')
            console.log('password', password.value)
```

**발췌 바로 풀이:** 사용자가 아무것도 입력하지 않고 기다린 경우를 비교한다.

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_html/javascript/13_dom_form.html` 62–79행

```javascript
            const today = new Date()
            const y = today.getFullYear()
            // getMonth는 0~11까지 나오기 때문에 +1 처리
            let m = today.getMonth() + 1 // 7로 나오기 때문에 07로 만들어야 함
            if(m < 10) {
                m = '0' + m
            }
            // m = ('0'+m).slice(-2)

            let d = today.getDate()
            d = ('0'+d).slice(-2)

            // const result = y + '-' + m + '-' + d
            const result = `${y}-${m}-${d}`
            date.value = result

            // 아래 방법을 사용하거나, 위에 new Date로 받아서 각기 값을 넣어줘도 됨
            console.log(today.toISOString().split('T')[0])
```

**발췌 바로 풀이:** getMonth()는 0–11이므로 1을 더한다. 월이 한 자리이면 앞에 '0'을 붙인다. 일은 `('0'+d).slice(-2)`로 마지막 두 글자를 취한다. 예를 들어 7은 '07', 16은 '16'이 된다. 이 문자열을 date.value에 넣는다.

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_html/javascript/13_dom_form.html` 81–96행

```javascript
            // radio 박스의 경우 checked 된 것의 'value'를 가져옴
            const radio = document.querySelector('[name=ai]:checked')
            console.log(radio.value)

            // 아래와 같이 checked = true로 주면 기본 체크값을 바꿀 수 있음
            const radios = document.querySelectorAll('[name=ai]')
            radios[1].checked = true

            // checkbox는 radio와 다르게 중복체크가 가능하기 때문에, all로 가져옴
            // 배열이기 때문에 value값을 출력하기 위해서는 for문으로 작성
            // 아래와 같이 반대의 경우 not()으로 사용할 수 있음
            const checks = document.querySelectorAll('.game:not(:checked)')
            // const checks = document.querySelectorAll('.game:checked')
            for(let i=0; i<checks.length; i++) {
                console.log(checks[i].value)
            }
```

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_html/javascript/13_dom_form.html` 100–108행

```javascript
            const checks2 = document.querySelectorAll('.game')
            for(let i=0; i<checks2.length; i++) {
                console.log(checks2[i].value, checks2[i].checked)
                if(checks2.checked == true) {
                    console.log(checks2[i].value)
                }
            }

            checks2[0].checked = true
```

**발췌 바로 풀이:** 내 if문은 checks2.checked를 읽는다. checks2는 NodeList이므로 해당 속성은 undefined이고 true와 같지 않다. 체크된 항목이 있어도 if 안의 추가 출력이 나오지 않는다. 바로 위 console.log는 checks2[i]를 쓰기 때문에 체크 상태를 정상 출력한다. **전체 코드가 모두 실패하는 오류와 조건 한 부분이 잘못된 오류를 구분한다.**

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_html/javascript/13_dom_form.html` 110–116행

```javascript
            console.log('---------------------------')
            // select의 경우 checkbox와 다르게 체크되어있지 않아도 value가 나옴
            // select도 checked = true로 하되, option에 주어야 함
            const lang = document.getElementById('lang')
            console.log(lang.value)

            lang.value = '4'
```

**발췌 바로 풀이:** 초기 선택은 python(value '2')이므로 lang.value는 '2'다. '4'를 대입하면 java가 선택된다. option 선택 상태의 이름은 selected이며 checked가 아니다. 내 주석의 ‘option에 checked = true’는 잘못된 설명이다. 이 원본처럼 select.value를 설정하면 된다. selected 속성은 용어 교정으로만 확인하고 새로운 필수 구현으로 늘리지 않는다.

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_html/javascript/13_dom_form.html` 119–128행

```javascript
            const textarea = document.querySelector('#textarea')
            console.log(textarea.value)
            console.log(textarea.value.indexOf('\n'))

            const view = document.querySelector('#view')
            view.innerHTML = textarea.value

            // 정규표현식으로 textarea에 있는 \n을 br로 전환해 줄 수 있음
            let str = textarea.value.replace(/\n/g, '<br>')
            view.innerHTML = str
```

**발췌 바로 풀이:** textarea의 현재 입력은 value로 읽는다. 초기값 '초기값'에는 줄바꿈이 없어서 indexOf('\n')은 -1이다. 원본 `/\n/g`는 모든 줄바꿈을 찾아 `<br>`로 바꾸는 간단한 정규표현식 사용이다. 정규표현식 전체 문법을 이 장의 전제로 확대하지 않는다.

원본 전체 작업은 3초 뒤 setTimeout 콜백 한 번 안에서 실행된다. 강사님은 text.value를 먼저 출력하고 12345를 넣지만 내 코드는 먼저 넣고 출력한다. 사용자가 아무것도 바꾸지 않았으면 강사님 출력은 abcd, 나는 12345이며 최종 입력값은 같다. password에는 강사님만 abcd를 대입한다. 무엇을 먼저 관찰하려는지에 따른 차이다.

날짜는 getMonth()+1과 앞의 0 붙이기, ('0'+d).slice(-2)로 월·일을 두 자리로 만든다. 처음 넣은 수업 날짜도 곧 실행 시점의 현지 날짜로 덮는다. UTC의 ISO 날짜를 잘라 쓰는 방법은 같은 대안이 아닐 수 있다. 초기값·최종값·시간대 조건을 구별한다.

내 checks2 반복은 바로 위 출력에서는 checks2[i]를 쓰지만 if에서는 [i]를 빠뜨렸다. 목록의 checked는 undefined여서 추가 출력이 나오지 않는다. 마지막 첫 체크박스 선택은 반복 뒤의 작업이며 이미 끝난 검사를 바꾸지 않는다.

<a id="connections"></a>

## 5. 선언·호출·파일이 연결되는 흐름

HTML의 name·class·id → 3초 뒤 콜백 → 요소 또는 목록 선택 → 현재 value·checked 읽기 → 값 대입 → 다음 선택·출력 순서다. 원본 라디오는 처음 value가 1이고 두 번째를 선택한 뒤에는 gemini가 된다. game의 초기 checked 목록은 0개, :not(:checked)은 6개다. select는 Python의 value 2를 읽고 value 4인 Java로 바꾼다. textarea와 view는 HTML에 있는 각 ID 요소다. innerHTML에 넣으면 사용자 글자의 태그도 해석될 수 있다는 점을 콘텐츠 장과 연결한다.

<a id="review"></a>

## 6. 잘한 점·아쉬운 점·개선 방향

**잘한 점:** 현재 입력을 읽는다는 주석과 체크박스 목록의 반복이 학습 의도에 맞다. **실제 오류:** checks2.checked의 [i] 누락과 option에 checked를 준다는 주석을 교정한다. option의 선택 용어는 selected이고 이 원본은 select.value를 사용한다. **개선 방향:** 글자 표시가 목적이면 innerText를 선택하고, 원본처럼 줄바꿈을 br로 바꾸어 HTML로 해석하는 방식과 구별한다. 모든 입력 검증 도구를 새로 넣을 필요는 없다.

개선안은 원본을 수정한 결과가 아니다. 실제 오류, 수업용 단순화, 목적에 따른 선택을 구별해 판단한다.

<a id="teacher"></a>

## 7. 강사님 코드가 도움이 되는 비교

출처: `D:/workspace_teacher/workspace_html/javascript/13_dom_form.html` 91–98행

```javascript
        const checks2 = document.querySelectorAll('.game')
        for(let i=0; i<checks2.length; i++){
            console.log(checks2[i].value, checks2[i].checked)
            if(checks2[i].checked == true){
                console.log(checks2[i].value)
            }
        }
        checks2[0].checked = true
```

위 강사님 체크박스 조건은 checks2[i].checked로 각 요소를 검사하므로 내 누락을 고칠 때 직접 도움이 되어 인용했다. 단, 초기에는 모두 미선택이라 양쪽 if 안 출력이 없다. 차이를 확인하려면 3초 전에 하나를 체크해야 한다. 현재값 대입·출력 순서는 목적에 따른 선택이며 무조건 강사님 방식으로 바꿀 사안은 아니다.

<a id="results"></a>

## 8. 결과를 추적하고 한 가지 바꾸기

| 실행 시점·조건 | 읽거나 바뀌는 것 | 판단 |
| --- | --- | --- |
| 조작 없이 3초 대기 | 내 text 출력 12345 | 대입 후 읽음 |
| 하나 체크 후 3초 | 위 상태 출력은 true | checks2[i]로 요소를 읽음 |
| 같은 조건의 내 if | 추가 항목 출력 없음 | 목록.checked는 undefined |
| 반복 끝난 뒤 첫 항목 선택 | 현재 첫 항목 true | 과거 반복에는 영향 없음 |
| 콜백 종료 뒤 메모 수정 | view는 이전 글자 | 한 번 실행이며 자동 연결 아님 |

원본 textarea 초기 글자에는 줄바꿈이 없어 indexOf('\n')은 -1이다. 두 줄을 입력하면 위치가 달라진다. 위 새 예제는 처음부터 두 줄이므로 원본 초기 결과와 다르다. 원본의 /\n/g는 줄바꿈을 모두 br로 바꾸는 간단한 사용이며 정규표현식 전체를 배웠다는 근거로 넓히지 않는다.

| 한 가지만 변경 | 예상 | 이유 |
| --- | --- | --- |
| 첫 체크박스의 checked만 제거 | 선택 개수 0 | value가 html이어도 미선택 |
| Java option의 value만 js로 | java 대입 후 일치 option 없음 | 표시 글자와 값은 다름 |
| view의 innerText만 innerHTML로 | 입력 태그가 해석될 수 있음 | 콘텐츠 해석 방식 변경 |

체크했는데 추가 출력이 없으면 목록과 요소를 구별하고 실행 시점도 확인한다. 입력의 textContent가 아니라 value를 읽는다. 화면을 수정했는데 view가 따라오지 않는다면 이벤트가 등록된 코드인지부터 본다. 직접 넣은 태그의 해석과 원문 표시도 별도 확인한다.

<a id="tips"></a>

## 9. 추가로 알면 좋은 것과 출처

> 💡 **TIP · 수업 범위 밖:** FormData·validity API·새 입력 검증 도구·Array.from을 이용한 목록 변환은 추가 학습이다. 기본은 value·checked·선택자·for와 배운 문자열 메서드로 풀 수 있다.



이 절의 확장은 기본 문제의 필수 조건이 아니다. 📚 출처가 있다는 것과 수업 밖 기능이라는 것은 다른 구분이다.

<a id="practice"></a>

## 10. 복습과 빠른 정리

1. 체크박스 value가 a이면 checked도 a인가?
2. 목록의 각 상태를 읽으려면 어디에 [i]가 필요한가?
3. 원본 콜백이 끝난 뒤 입력한 글자가 자동으로 view에 들어가는가?

<details>
<summary>짧은 풀이 — 먼저 답한 뒤 확인</summary>

checked는 true 또는 false다. checks2[i].checked로 요소를 먼저 고른다. 원본은 한 번만 실행하므로 이후 변경을 자동 반영하지 않는다.

</details>

| 질문 | 확인 |
| --- | --- |
| 현재 글자 | value |
| 현재 선택 | checked |
| 목록의 항목 | [i]로 요소 선택 |
| 자동 갱신 | 이벤트·재실행 여부 |

[장별 연습문제](실습/연습문제/13_JavaScript_DOM_폼요소와_입력값처리_연습문제.md)에서 예상·설명·수정을 이어 간다. 다음은 [동기·비동기](14_JavaScript_동기비동기와_이벤트루프.md)다.

<!-- 이전 색인 이동 주소 보존 -->
<a id="section-1"></a>
<a id="section-2"></a>
<a id="section-3"></a>
<a id="section-4"></a>
<a id="section-5"></a>
<a id="section-6"></a>
<a id="section-7"></a>
<a id="section-8"></a>

[이 장의 목차](#chapter-toc)에서 현재 설명을 찾는다.
