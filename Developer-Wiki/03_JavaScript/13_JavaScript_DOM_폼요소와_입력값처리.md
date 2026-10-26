# 13. 폼 요소 — 입력값과 선택 상태 읽기

[JavaScript 목차](README.md) · [이전: 스타일·퀴즈](12-03_JavaScript_DOM_스타일과_퀴즈.md) · [다음: 동기·비동기](14_JavaScript_동기비동기와_이벤트루프.md)

기준은 양쪽 `13_dom_form.html`이다. input·select·textarea에서 **현재 값은 value, 라디오·체크박스의 체크 상태는 checked**로 다룬다. 모든 작업이 3초 지연 setTimeout 콜백 안에서 한 번 실행된다. 입력할 때마다 자동 갱신하는 이벤트 실습과 구분한다.

<!-- chapter-toc -->

- [1. 입력값을 읽는 순서도 결과에 영향을 준다](13_JavaScript_DOM_폼요소와_입력값처리.md#section-1)
- [2. 날짜 입력은 yyyy-mm-dd 문자열](13_JavaScript_DOM_폼요소와_입력값처리.md#section-2)
- [3. value와 checked는 다른 정보다](13_JavaScript_DOM_폼요소와_입력값처리.md#section-3)
- [4. 내 체크박스 조건의 [i] 누락](13_JavaScript_DOM_폼요소와_입력값처리.md#section-4)
- [5. select는 선택된 option의 value를 읽는다](13_JavaScript_DOM_폼요소와_입력값처리.md#section-5)
- [6. textarea의 줄바꿈을 화면에 출력하기](13_JavaScript_DOM_폼요소와_입력값처리.md#section-6)
- [7. 복습](13_JavaScript_DOM_폼요소와_입력값처리.md#section-7)
- [추가로 알면 좋은 것](13_JavaScript_DOM_폼요소와_입력값처리.md#section-8)

<a id="section-1"></a>

## 1. 입력값을 읽는 순서도 결과에 영향을 준다

### 강사님 코드

출처: `teacher/workspace_html/javascript/13_dom_form.html` 45–51행 · **원본 발췌**

```javascript
        const text = document.querySelector('#id')
        console.log('text', text.value)
        text.value = '12345'
        
        const password = document.querySelector('#pw')
        console.log('password', password.value)
        password.value = 'abcd'
```

### 내 코드

출처: `me/workspace_html/javascript/13_dom_form.html` 47–54행 · **원본 발췌**

```javascript
            // input type에 value값이 있지만, 가져오는건 입력 된 최신 데이터
            // text.value로 input text의 값을 바꿔줄 수 있음
            const text = document.querySelector('#id')
            text.value = '12345'
            console.log('text', text.value)
            
            const password = document.querySelector('#pw')
            console.log('password', password.value)
```

사용자가 아무것도 입력하지 않고 기다린 경우를 비교한다.

| 항목 | 강사님 | 내 코드 |
| --- | --- | --- |
| text 출력 | 바꾸기 전 'abcd' | 바꾼 후 '12345' |
| 최종 text.value | '12345' | '12345' |
| password 출력 | 빈 문자열 | 빈 문자열 |
| 최종 password.value | 'abcd' | 빈 문자열 |

value는 HTML 속성에 적힌 초기 글자만 읽는 것이 아니라 현재 입력값을 읽는다. 3초가 되기 전에 입력했다면 강사님이 먼저 출력하는 값도 달라진다. 나는 대입 후 출력하므로 text 출력이 '12345'다. 어느 쪽이 무조건 좋다기보다 **바꾸기 전 값을 볼지, 바꾼 결과를 볼지**에 따른 차이다.

<a id="section-2"></a>

## 2. 날짜 입력은 yyyy-mm-dd 문자열

### 강사님 코드

출처: `teacher/workspace_html/javascript/13_dom_form.html` 61–75행 · **원본 발췌**

```javascript
        const today = new Date()
        const y = today.getFullYear()
        let m = today.getMonth() + 1 // 7
        if (m < 10){
            m = '0' + m
        }

        let d = today.getDate()
        d = ('0'+d).slice(-2)

        // const result = y +'-'+ m +'-'+ d
        const result = `${y}-${m}-${d}`
        date.value = result

        console.log(today.toISOString().split('T')[0])
```

### 내 코드

출처: `me/workspace_html/javascript/13_dom_form.html` 62–79행 · **원본 발췌**

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

getMonth()는 0–11이므로 1을 더한다. 월이 한 자리이면 앞에 '0'을 붙인다. 일은 `('0'+d).slice(-2)`로 마지막 두 글자를 취한다. 예를 들어 7은 '07', 16은 '16'이 된다. 이 문자열을 date.value에 넣는다.

두 원본 모두 앞에서 수업 날짜를 한 번 넣지만 곧 result로 덮는다. 최종 값은 실행한 컴퓨터의 현지 날짜다. 실행 날짜가 달라져도 당시 수업 날짜가 계속 남는 코드가 아니다.

원본의 toISOString().split('T')[0]은 **UTC 날짜**다. 현지 날짜와 항상 같지 않으므로 내 주석처럼 완전히 같은 대안으로 취급하지 않는다. 날짜 기준은 [07 Date](07_JavaScript_Date와_날짜처리.md)에서 이어 읽는다. padStart를 새로 요구하지 않아도 원본 문법으로 두 자리를 만들 수 있다.

<a id="section-3"></a>

## 3. value와 checked는 다른 정보다

### 강사님 코드

출처: `teacher/workspace_html/javascript/13_dom_form.html` 77–88행 · **원본 발췌**

```javascript
        const radio = document.querySelector('[name=ai]:checked')
        console.log(radio.value)

        const radios = document.querySelectorAll('[name=ai]')
        radios[1].checked = true


        // const checks = document.querySelectorAll('.game:checked')
        const checks = document.querySelectorAll('.game:not(:checked)')
        for(let i=0; i<checks.length; i++){
            console.log(checks[i].value)
        }
```

### 내 코드

출처: `me/workspace_html/javascript/13_dom_form.html` 81–96행 · **원본 발췌**

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

| 표현 | 의미 | 조작하지 않은 원본 기준 |
| --- | --- | --- |
| '[name=ai]:checked' | 현재 선택된 ai 라디오 | 첫 라디오, value '1' |
| radios[1].checked = true | 두 번째 라디오 선택 | gemini 선택, 첫 라디오 해제 |
| '.game:checked' | 체크된 게임 목록 | 처음에는 0개 |
| '.game:not(:checked)' | 체크 안 된 게임 목록 | 처음에는 6개 |

같은 그룹의 라디오는 하나를 선택하고, 체크박스는 여러 개를 선택할 수 있다. value는 각 항목의 값 문자열이고 checked는 true/false다. 체크박스가 여러 개면 querySelectorAll로 목록을 얻어 **각 요소**에 접근한다. 목록 자체에 value·checked를 묻지 않는다.

<a id="section-4"></a>

## 4. 내 체크박스 조건의 [i] 누락

### 강사님 코드

출처: `teacher/workspace_html/javascript/13_dom_form.html` 91–98행 · **원본 발췌**

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

### 내 코드

출처: `me/workspace_html/javascript/13_dom_form.html` 100–108행 · **원본 발췌**

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

내 if문은 checks2.checked를 읽는다. checks2는 NodeList이므로 해당 속성은 undefined이고 true와 같지 않다. 체크된 항목이 있어도 if 안의 추가 출력이 나오지 않는다. 바로 위 console.log는 checks2[i]를 쓰기 때문에 체크 상태를 정상 출력한다. **전체 코드가 모두 실패하는 오류와 조건 한 부분이 잘못된 오류를 구분한다.**

강사님처럼 아래와 같이 요소 하나의 상태를 검사하면 된다.

**내 코드 교정 — 조건 한 줄 변경**

```javascript
if (checks2[i].checked == true) {
    console.log(checks2[i].value)
}
```

원본 HTML은 체크박스가 모두 해제되어 있어 처음에는 양쪽 if 안 출력이 모두 없다. 차이를 보려면 3초 전에 하나를 체크해야 한다. 마지막 checks2[0].checked = true는 **반복문 이후**에 실행되므로 이번 반복의 검사 결과를 거꾸로 바꾸지 않는다.

<a id="section-5"></a>

## 5. select는 선택된 option의 value를 읽는다

### 강사님 코드

출처: `teacher/workspace_html/javascript/13_dom_form.html` 100–103행 · **원본 발췌**

```javascript
        const lang = document.getElementById('lang')
        console.log(lang.value)

        lang.value = '4'
```

### 내 코드

출처: `me/workspace_html/javascript/13_dom_form.html` 110–116행 · **원본 발췌**

```javascript
            console.log('---------------------------')
            // select의 경우 checkbox와 다르게 체크되어있지 않아도 value가 나옴
            // select도 checked = true로 하되, option에 주어야 함
            const lang = document.getElementById('lang')
            console.log(lang.value)

            lang.value = '4'
```

초기 선택은 python(value '2')이므로 lang.value는 '2'다. '4'를 대입하면 java가 선택된다. option 선택 상태의 이름은 selected이며 checked가 아니다. 내 주석의 ‘option에 checked = true’는 잘못된 설명이다. 이 원본처럼 select.value를 설정하면 된다. selected 속성은 용어 교정으로만 확인하고 새로운 필수 구현으로 늘리지 않는다.

<a id="section-6"></a>

## 6. textarea의 줄바꿈을 화면에 출력하기

### 강사님 코드

출처: `teacher/workspace_html/javascript/13_dom_form.html` 106–114행 · **원본 발췌**

```javascript
        const textarea = document.querySelector('#textarea')
        console.log(textarea.value)
        console.log(textarea.value.indexOf('\n'))

        const view = document.querySelector('#view')
        view.innerHTML = textarea.value

        let str = textarea.value.replace(/\n/g, '<br>')
        view.innerHTML = str
```

### 내 코드

출처: `me/workspace_html/javascript/13_dom_form.html` 119–128행 · **원본 발췌**

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

textarea의 현재 입력은 value로 읽는다. 초기값 '초기값'에는 줄바꿈이 없어서 indexOf('\n')은 -1이다. 원본 `/\n/g`는 모든 줄바꿈을 찾아 `<br>`로 바꾸는 간단한 정규표현식 사용이다. 정규표현식 전체 문법을 이 장의 전제로 확대하지 않는다.

두 코드 모두 HTML을 해석하는 innerHTML에 입력을 넣는다. 사용자가 `<b>안녕</b>`을 입력하면 글자 그대로가 아니라 b 요소가 생긴다. 줄바꿈과 일반 글자 표시가 목적이라면 다음처럼 이미 배운 innerText를 쓰는 쪽이 의도에 맞는다.

**설명용 교정 — 입력을 HTML로 해석하지 않기**

```javascript
view.innerText = textarea.value
```

이 대입은 태그 문법을 글자로 표시하고 줄바꿈도 반영한다. textContent와 innerHTML의 차이는 [12 콘텐츠](12_JavaScript_DOM_콘텐츠생성과_스타일조작.md)에서 자세히 다룬다.

<a id="section-7"></a>

## 7. 복습

1. 체크박스 value가 'a'이면 checked도 'a'인가?
2. checks2.checked 대신 무엇을 검사해야 하는가?
3. 아무 조작 없이 기다리면 마지막에 선택되는 언어는?
4. 3초 뒤 textarea를 바꾸면 #view도 자동으로 바뀌는가?

<details>
<summary>정답</summary>

1. 아니다. checked는 체크 상태를 나타내는 boolean이다.
2. 반복문에서 checks2[i].checked를 검사한다.
3. value '4'인 java다.
4. 아니다. 원본은 콜백을 한 번만 실행한다. 입력 이벤트 연결은 이후 이벤트 장에서 배운다.

</details>

<a id="section-8"></a>

**이 장을 읽은 뒤:** [장별 연습문제 풀기](실습/연습문제/13_JavaScript_DOM_폼요소와_입력값처리_연습문제.md)

## 추가로 알면 좋은 것

FormData, validity API, 새 입력 검증 도구, Array.from으로 입력 목록 변환하기는 추가 학습이다. 기본 복습은 value·checked·선택자·for문·배운 문자열 메서드로 해결한다.

