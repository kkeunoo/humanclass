# 17-03. 주문·로그인·피자 — 입력값을 읽고 결과 만들기

[JavaScript 목차](README.md) · [이전: 이벤트 전파·위임](17-02_JavaScript_이벤트전파와_위임.md) · [다음: 메뉴·Todo](17-04_JavaScript_메뉴와_Todo실습.md)

강사님의 `퀴즈/이벤트.html`과 내 `17_event_form.html`, `asset/js/17_event_form.js`에서 실제로 작성한 실습을 비교한다. 세 문제 모두 **클릭할 때 현재 입력 상태를 읽는다**. 아래 코드는 수업 원본을 그대로 옮겼다.

<!-- chapter-toc -->

- [1. 주문 정보와 배송 정보 복사](17-03_JavaScript_주문_로그인_피자실습.md#section-1)
- [2. 로그인 입력 확인](17-03_JavaScript_주문_로그인_피자실습.md#section-2)
- [3. 피자 선택과 총액](17-03_JavaScript_주문_로그인_피자실습.md#section-3)
- [직접 확인할 질문](17-03_JavaScript_주문_로그인_피자실습.md#section-4)
- [추가로 알면 좋은 것](17-03_JavaScript_주문_로그인_피자실습.md#section-5)

<a id="section-1"></a>

## 1. 주문 정보와 배송 정보 복사

체크박스를 켜면 주문 이름·주소의 `.value`를 배송 입력 칸에 넣고, 끄면 배송 칸을 비운다. 체크한 뒤 주문 정보를 다시 고쳐도 배송 칸은 자동 갱신되지 않는다. 복사는 체크박스를 누른 순간에만 일어난다.

### 강사님 코드

출처: `teacher/workspace_html/javascript/퀴즈/이벤트.html` 67~88행 · **원본 발췌**

```javascript
function q1(){
    
    document.querySelector('#q1 .chk').addEventListener('click', function(event){
        const order_name = document.querySelector('#q1 .order .name')
        const order_addr = document.querySelector('#q1 .order .addr')

        const delivery_name = document.querySelector('#q1 .delivery .name')
        const delivery_addr = document.querySelector('#q1 .delivery .addr')

        /*
            event.target : 실제로 이벤트가 발생한 것
            event.currentTarget : 이벤트가 적용되어 있는 것 (this)
        */
        if(event.target.checked){
            delivery_name.value = order_name.value
            delivery_addr.value = order_addr.value
        } else {
            delivery_name.value = ''
            delivery_addr.value = ''
        }
    })
}
```

### 내 코드

출처: `me/workspace_html/javascript/asset/js/17_event_form.js` 159~182행 · **원본 발췌**

```javascript
window.addEventListener('load', function() {
    /*
        문제1_주문과 배송
        주문 정보 : input으로 이름, 주소를 적을 수 있음
        ㅁ(checkbox) 주문 정보와 배송 정보가 같습니다 
        배송 정보 : input으로 이름, 주소를 적을 수 있음
        * 체크하면 주문 정보 > 배송 정보로 데이터가 복사되도록
        * 체크를 풀면 배송 정보 글씨를 지우기
    */
    const valueChk = document.querySelector('.valueChk')
    valueChk.addEventListener('click', function(event){
        const name1 = document.querySelector('.name1')
        const name2 = document.querySelector('.name2')
        const address1 = document.querySelector('.address1')
        const address2 = document.querySelector('.address2')

        if(valueChk.checked == true) {
            name2.value = name1.value
            address2.value = address1.value
        } else {
            name2.value = ''
            address2.value = ''
        }
    })
```

두 코드의 결과는 같다. 강사님은 `event.target.checked`로 이번에 클릭한 체크박스를 읽고, 나는 미리 선택한 `valueChk.checked`를 읽었다. 이 문제에서는 같은 요소다. 복사해야 하는 값은 입력 요소의 글자가 아니라 **`.value`**다.

<a id="section-2"></a>

## 2. 로그인 입력 확인

아이디가 비었으면 아이디 경고, 아이디는 있고 비밀번호가 비었으면 비밀번호 경고, 둘 다 있으면 이전 경고를 지운다. 양쪽 모두 `trim()`으로 앞뒤 공백만 있는 입력도 비어 있다고 판단한다.

### 강사님 코드

출처: `teacher/workspace_html/javascript/퀴즈/이벤트.html` 90~109행 · **원본 발췌**

```javascript
function q2(){
    
    // const login = document.querySelector('#q2 #login.do')
    const login = document.querySelector('#q2 [id="login.do"]')
    login.addEventListener('click', function(){
        const id = document.querySelector('#q2 #id')
        const pw = document.querySelector('#q2 #pw')
        const warning = document.querySelector('#q2 #warning')

        // if(id.value == ''){
        console.log(id.value.trim().length, id.value.trim().length == 0)
        if(id.value.trim().length == 0){
            warning.innerText = '아이디는 필수입니다'
        } else if(pw.value.trim().length == 0){
            warning.textContent = '비밀번호는 필수입니다'
        } else {
            warning.textContent = ''
        }
    })
}
```

### 내 코드

출처: `me/workspace_html/javascript/asset/js/17_event_form.js` 184~209행 · **원본 발췌**

```javascript
    /*
        문제2_로그인창
        로그인 버튼을 눌렀을 때 아이디 / 비밀번호가 없으면,
        빨간 글씨가 나오게 (단, 아이디/비밀번호를 쓰고 로그인을 누르면 빨간 글씨 지우기)
    */
    const login = document.querySelector('#login')
    login.addEventListener('click', function(){
        const id1 = document.querySelector('.id1')
        const pw1 = document.querySelector('.pw1')
        const errChk = document.querySelector('.errChk')
        // console.log(errChk)
        
        // if(id1.trim().length == 0) { 으로도 사용할 수 있다.
        if(id1.value.trim() == '') {
            errChk.innerText = '아이디를 입력하세요'
            // style은 css에 주고나서, Attribute를 줘서 적용시키는게 좋음
            errChk.style.color = 'red'
        } else if(pw1.value.trim() == '') {
            errChk.innerText = '패스워드를 입력하세요'
            errChk.style.color = 'red'
        } else {
            errChk.innerText = ''
        }
        // console.log(id1.value)
        // console.log(pw1.value)
    })
```

내 코드는 경고 글씨 색도 빨강으로 지정한다. 강사님 HTML에는 이미 `#warning`에 빨강 스타일이 있다. 둘 다 **로그인 성공이나 서버 인증을 구현한 것은 아니고** 입력 여부만 검사한다. `trim()`은 검사용 문자열을 반환하며 입력 칸의 원래 값을 바꾸지 않는다.

강사님 버튼 ID는 `login.do`라서 CSS 선택자 `#login.do`로 읽으면 `id=login`이면서 `class=do`인 요소를 찾게 된다. 수업 코드의 `[id="login.do"]`는 실제 ID를 정확히 찾는다. 내 버튼은 `id="login"`이므로 `#login`으로 선택한다.

<a id="section-3"></a>

## 3. 피자 선택과 총액

피자 종류는 `select`, 크기·도우는 선택된 `radio`, 토핑은 체크된 `checkbox`로 읽는다. **크기 가격과 선택 토핑 가격을 합산한다.** 도우 가격은 두 HTML에 없다.

### 강사님 코드: 속성으로 가격 분리

출처: `teacher/workspace_html/javascript/퀴즈/이벤트.html` 120~143행 · **원본 발췌**

```javascript
        const pizza = document.querySelector('#q3 .pizza')
        console.log(pizza.value)
        console.log(pizza.options)
        console.log(pizza.selectedIndex)
        const option = pizza.options[pizza.selectedIndex]
        console.log(option.innerText)
        console.log(option.getAttribute('data-name'))
        console.log(option.dataset.name)
        option.dataset.minsu = '강사'
        종류 = option.getAttribute('data-name')

        const size = document.querySelector('[name="size"]:checked')
        크기 = size.getAttribute('data-size')
        총액 += Number(size.getAttribute('data-price'))
        console.log(총액)

        const dough = document.querySelector('[name="dough"]:checked')
        도우 = dough.getAttribute('data-dough')
        
        const aTopping = document.querySelectorAll('[type="checkbox"]:checked')
        for( topping of aTopping ){
            토핑.push(topping.getAttribute('topping'))
            총액 += Number(topping.getAttribute('price'))
        }
```

출처: `teacher/workspace_html/javascript/퀴즈/이벤트.html` 153~160행 · **원본 발췌**

```javascript
        document.querySelector('#q3 #bill').innerHTML = `
            종류 : ${종류}<br>
            크기 : ${크기}<br>
            도우 : ${도우}<br>
            토핑 : ${토핑.join()}<br>
            <hr>
            총액 : ${총액}<br>
        `
```

HTML의 가격 예시:

출처: `teacher/workspace_html/javascript/퀴즈/이벤트.html` 293~318행 · **원본 발췌**

```javascript
    <div id="q3">
        <h2>quiz 3</h2>
        종류 : 
        <select class="pizza">
            <option value="10" data-name="불고기">불고기</option>
            <option value="20" data-name="페퍼로니">페퍼로니</option>
            <option value="30" data-name="포테이토">포테이토</option>
            <option value="40" data-name="치즈">치즈</option>
            <option value="50" data-name="파인애플">파인애플</option>
            <option value="60" data-name="고르곤졸라">고르곤졸라</option>
        </select>
        <br>
        사이즈 : 
        <input type="radio" name="size" value="10" data-size="small" data-price="18000" checked>small(18000)
        <input type="radio" name="size" value="20" data-size="medium" data-price="20000">medium(20000)
        <input type="radio" name="size" value="30" data-size="large" data-price="22000">large(22000)
        <br>
        도우 :
        <input type="radio" name="dough" value="10" data-dough="씬" checked>씬
        <input type="radio" name="dough" value="20" data-dough="고구마">고구마
        <input type="radio" name="dough" value="30" data-dough="치즈">치즈
        <input type="radio" name="dough" value="40" data-dough="소보로">소보로
        <br>
        토핑 :
        <input type="checkbox" value="10" topping="감자" price="2000">감자(2000)
        <input type="checkbox" value="20" topping="고구마" price="2000">고구마(2000)
```

강사님은 `data-name`, `data-size`, `data-price`로 이름과 가격을 구분한다. `option.dataset.name`을 읽는 법도 실제 배운 내용이므로 본문에 둔다. 다만 토핑의 `topping`, `price`는 `data-` 속성이 아닌 일반 사용자 정의 속성이라 `getAttribute()`로 읽고 있다. 새 코드를 작성한다면 `data-topping`, `data-price`로 통일하는 편이 의미가 분명하다.

### 내 코드: value를 나누어 가격 계산

출처: `me/workspace_html/javascript/asset/js/17_event_form.js` 228~253행 · **원본 발췌**

```javascript
   // 최종정리본
   const pay = document.querySelector('#pay')
   pay.addEventListener('click', function(){
       const order = document.querySelector('#order')
       const size = document.querySelector('[name=size]:checked')
       const dough = document.querySelector('[name=dough]:checked')
       const topping = document.querySelectorAll('.topping')
       const orderChk = document.querySelector('#orderChk')
       const orderPrice = document.querySelector('#orderPrice')
       let topResult = ''
       let topPrice = 0
       let priceResult = 0

       for(let i=0; i<topping.length; i++) {
           if(topping[i].checked == true) {
               // console.log('토핑', topping[i].value.split(' ')[0])
               topResult += topping[i].value.split(' ')[0]
               topPrice += Number(topping[i].value.split(' ')[1])
           }
       }
       priceResult += topPrice + Number(size.value.split(' ')[1])

       orderChk.innerText = 
       `종류: ${order.value}, 사이즈: ${size.value.split(' ')[0]}, 도우: ${dough.value}, 토핑:${topResult}`
       orderPrice.innerText = `총액: ${priceResult}원`
    }) 
```

내 HTML의 크기 `value="small 18000"` 같은 값을 공백으로 나눠 이름과 가격을 읽는다. 선택된 토핑도 같은 방식으로 합산한다. 예를 들어 기본 선택인 small 18,000원과 감자 2,000원은 20,000원이다. 다만 `topResult += 이름`은 토핑을 여러 개 고르면 구분자 없이 붙는다. 강사님 `토핑.join()`처럼 배열에 모아 출력하면 읽기 쉽다.

강사님 코드는 피자 종류에서 `option.dataset.name`을 보여 주고 가격을 별도 속성으로 분리한 점이 읽기 쉽다. 내 코드는 HTML의 `value`만 사용해 계산 흐름을 추적하기 쉽지만, 값에 공백이 더 들어가면 `split(' ')[1]`에 의존하는 구조가 깨질 수 있다. **두 방식 모두 이번 수업 실습**이며 `dataset`은 추가편으로 밀지 않는다.

<a id="section-4"></a>

## 직접 확인할 질문

1. 주문 정보 체크 후 주문 주소를 바꾸면 배송 주소도 바뀔까? 어떤 이벤트가 등록됐는지 확인하자.
2. 로그인 입력이 공백뿐일 때 `trim()` 뒤 길이는 얼마일까?
3. 피자에서 size와 topping 중 무엇이 총액에 더해지는지 HTML 속성과 코드를 연결해 보자.

<a id="section-5"></a>

**이 장을 읽은 뒤:** [장별 연습문제 풀기](실습/연습문제/17-03_JavaScript_주문_로그인_피자실습_연습문제.md)

## 추가로 알면 좋은 것

실제 서비스에서 사용자 입력을 HTML 문자열에 넣거나 서버로 보낼 때에는 별도의 출력 안전 처리와 서버 검사가 필요하다. 이 수업의 피자 실습은 브라우저 안에서 선택값을 읽고 계산하는 단계까지다.

