# 17-03. 주문·로그인·피자 — 입력 상태에서 결과를 만드는 세 단계

[JavaScript 목차](README.md) · [읽기 안내](00_JavaScript_V3_동작_백과_읽기법.md)

서로 다른 화면처럼 보여도 세 문제는 현재 값을 읽기 → 조건이나 계산 적용 → 결과 표시라는 흐름을 공유한다. 복사한 값이 계속 연결되는지, 경고가 왜 남는지, 문자열 가격이 왜 숫자로 바뀌어야 하는지를 한 단계씩 확인한다.

<a id="chapter-toc"></a>

**이 장의 목차:** [목표](#learn) · [개념](#concepts) · [예제](#example) · [내 코드](#my-code) · [연결](#connections) · [평가](#review) · [비교](#teacher) · [결과·실험](#results) · [TIP·출처](#tips) · [복습](#practice)

<a id="learn"></a>

## 1. 이 장에서 배울 것

주문 정보 복사와 자동 동기화를 구별하고 로그인 입력 검사의 분기 순서를 읽는다. value 분해와 data 속성의 차이, 숫자 변환·합산·토핑 목록 표시를 설명한다.

입력·현재 상태·실행 순서·결과를 분리해 설명한다. 실제 수업 원본은 아래에 표시하고, 원본에 없는 선택 학습은 9절 TIP에 둔다.

<a id="concepts"></a>

## 2. 무엇이며, 왜 필요한가

주문 정보 복사는 값을 읽어 다른 입력 칸에 대입하는 작업이다. 체크한 순간의 문자열을 복사할 뿐, 두 입력 칸 사이에 영구적인 연결이 생기는 것은 아니다. 체크 뒤 원본 주문 주소를 바꾸면 다시 복사하기 전까지 배송 주소는 예전 값이다.

로그인 실습은 입력 여부를 검사한다. if → else if → else는 먼저 맞은 한 갈래만 실행한다. 아이디와 비밀번호가 모두 비어 있으면 첫 경고가 우선이다. 둘 다 있으면 이전 경고를 비운다. 이 결과만으로 사용자가 서버에서 인증되었다고 할 수는 없다.

| 읽은 값 | 실제 자료형 | 계산 전 작업 |
| --- | --- | --- |
| input.value | 문자열 | 필요하면 trim |
| checkbox.checked | boolean | 조건에서 검사 |
| value='small 18000' | 문자열 한 개 | split 뒤 가격 부분을 Number로 변환 |
| data-price='18000' | 속성의 문자열 | dataset.price 또는 getAttribute 뒤 Number |

dataset은 실제 배운 내용이므로 본문에 둔다. data-name은 dataset.name으로 읽고 data-price는 dataset.price로 읽는다. 속성에 숫자처럼 보이는 글자가 있어도 읽은 값은 문자열이다. 18000과 '2000'을 +로 연결하면 20000이라는 숫자 합계가 되지 않으므로 가격을 숫자로 변환한 뒤 더한다.

> 📚 **출처 · 본문 설명 확인:** [MDN dataset](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/dataset). 배운 기능의 뜻을 확인한 근거다. 예제·표·풀이 흐름은 수업 코드를 바탕으로 새로 작성했으며 외부 문장을 직접 인용하지 않았다. 확인일: 2026-10-28.

<a id="example"></a>

## 3. 작은 예제로 먼저 이해하기

**새 설명 예제 · 전체 스크립트.** [HTML 실행 파일](실습/책형_복습/17-03_JavaScript_주문_로그인_피자실습.html)과 같은 폴더의 [JS 파일](실습/책형_복습/17-03_JavaScript_주문_로그인_피자실습.js)을 함께 내려받는다. HTML을 브라우저로 열고 Console에서 결과를 확인한다. script는 필요한 HTML 뒤에 연결한다. 콘솔 출력은 페이지 본문에 자동으로 쓰이지 않는다.

**먼저 준비할 HTML · body 안:**

```html
    <h2>주문 정보</h2>
    <label>이름 <input id="orderName" value="민지"></label>
    <label>주소 <input id="orderAddress" value="서울"></label>
    <label><input id="same" type="checkbox">주문 정보와 같음</label>
    <label>배송 이름 <input id="deliveryName"></label>
    <label>배송 주소 <input id="deliveryAddress"></label>
    <h2>입력 확인</h2>
    <label>아이디 <input id="user"></label><label>비밀번호 <input id="pw" type="password"></label>
    <button id="login" type="button">입력 검사</button><p id="warning"></p>
    <h2>피자 계산</h2>
    <select id="pizza" aria-label="종류"><option data-name="불고기">불고기</option><option data-name="치즈">치즈</option></select>
    <label><input type="radio" name="size" data-price="18000" value="small" checked>small</label>
    <label><input type="radio" name="size" data-price="22000" value="large">large</label>
    <label><input class="topping" type="checkbox" data-price="2000" value="감자">감자</label>
    <label><input class="topping" type="checkbox" data-price="2000" value="고구마">고구마</label>
    <button id="pay" type="button">계산</button><p id="bill"></p>
```

```javascript
document.getElementById('same').addEventListener('click', function () {
    document.getElementById('deliveryName').value = this.checked
        ? document.getElementById('orderName').value : '';
    document.getElementById('deliveryAddress').value = this.checked
        ? document.getElementById('orderAddress').value : '';
});
document.getElementById('login').addEventListener('click', function () {
    const user = document.getElementById('user');
    const pw = document.getElementById('pw');
    const warning = document.getElementById('warning');
    if (user.value.trim() === '') warning.textContent = '아이디 필수';
    else if (pw.value.trim() === '') warning.textContent = '비밀번호 필수';
    else warning.textContent = '';
});
document.getElementById('pay').addEventListener('click', function () {
    const pizza = document.getElementById('pizza');
    const option = pizza.options[pizza.selectedIndex];
    const size = document.querySelector('[name="size"]:checked');
    const toppings = document.querySelectorAll('.topping:checked');
    const names = [];
    let total = Number(size.dataset.price);
    for (const topping of toppings) {
        names.push(topping.value);
        total += Number(topping.dataset.price);
    }
    const result = option.dataset.name + ' / ' + size.value +
        ' / ' + names.join(', ') + ' / ' + total + '원';
    document.getElementById('bill').textContent = result;
    console.log(result);
});
```

주문 정보와 같음을 체크하면 배송 주소는 서울이다. 주문 주소만 부산으로 고쳐도 배송 주소는 서울로 남는다. 입력 검사 버튼을 빈 상태·아이디만 있는 상태·둘 다 있는 상태에서 눌러 경고가 차례로 바뀌고 지워지는지 본다. 피자는 small과 토핑 두 개를 선택해 계산한다. 18000+2000+2000=22000이며 토핑 이름 사이에 쉼표와 공백이 들어간다. 새 예제는 배운 dataset·배열·join을 사용한 개선 예제다. 원본에 있는 도우 선택은 가격이 없어 이 최소 계산 예제에서는 생략했으며, 원본 전체 기능을 재현했다고 하지 않는다.

**예상 출력 또는 관찰:**

```text
불고기 / small / 감자, 고구마 / 22000원
```

<a id="my-code"></a>

## 4. 내가 작성한 코드를 따라 읽기

아래는 원본의 일부다. 원본에 의존하는 앞 선언·HTML·함수는 다음 절의 연결까지 읽는다. 주석의 잘못된 표현도 원문대로 보존하고 설명에서 교정한다.

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_html/javascript/asset/js/17_event_form.js` 159–182행

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

**발췌 바로 풀이:** 두 코드의 결과는 같다. 강사님은 `event.target.checked`로 이번에 클릭한 체크박스를 읽고, 나는 미리 선택한 `valueChk.checked`를 읽었다. 이 문제에서는 같은 요소다. 복사해야 하는 값은 입력 요소의 글자가 아니라 **`.value`**다.

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_html/javascript/asset/js/17_event_form.js` 184–209행

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

**발췌 바로 풀이:** 내 코드는 경고 글씨 색도 빨강으로 지정한다. 강사님 HTML에는 이미 `#warning`에 빨강 스타일이 있다. 둘 다 **로그인 성공이나 서버 인증을 구현한 것은 아니고** 입력 여부만 검사한다. `trim()`은 검사용 문자열을 반환하며 입력 칸의 원래 값을 바꾸지 않는다.

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_html/javascript/asset/js/17_event_form.js` 228–253행

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

**발췌 바로 풀이:** 내 HTML의 크기 `value="small 18000"` 같은 값을 공백으로 나눠 이름과 가격을 읽는다. 선택된 토핑도 같은 방식으로 합산한다. 예를 들어 기본 선택인 small 18,000원과 감자 2,000원은 20,000원이다. 다만 `topResult += 이름`은 토핑을 여러 개 고르면 구분자 없이 붙는다. 강사님 `토핑.join()`처럼 배열에 모아 출력하면 읽기 쉽다.

내 복사는 체크박스의 checked를 직접 읽고 강사님은 event.target.checked를 읽는다. 현재 리스너에서는 같은 요소이므로 결과가 같다. 로그인 문제는 이전 15장의 기본 예제와 달리 성공 갈래에 경고 지우기가 있다. 내 주석의 id1.trim()은 요소에 문자열 메서드를 바로 호출하는 잘못된 예시다. 실제 활성 코드처럼 id1.value.trim()이어야 한다. 내 피자는 small 18000처럼 묶인 value를 공백으로 나눠 이름·가격을 읽고, 체크된 토핑의 가격을 Number로 더한다.

<a id="connections"></a>

## 5. 선언·호출·파일이 연결되는 흐름

HTML의 선택 요소와 value 형식 → pay 클릭 → 현재 size·dough·topping 조회 → 체크 여부 검사 → split 또는 data 속성으로 가격 읽기 → Number 변환 → 합계·결과 표시 순서다. 새 예제에서 options[selectedIndex]는 현재 선택된 option이다. querySelectorAll은 토핑 목록이며 각 요소를 반복해야 한다. 클릭할 때 total과 names를 새로 준비하여 이전 계산값을 다시 더하지 않는다. 원본도 topPrice·priceResult를 콜백 안에서 초기화한다.

<a id="review"></a>

## 6. 잘한 점·아쉬운 점·개선 방향

**잘한 점:** 내 피자는 합계 변수를 클릭마다 초기화하고, 선택된 토핑만 계산하며 입력 확인에서 과거 경고를 지운다. **아쉬운 점:** 토핑 이름을 문자열에 바로 더해 여러 이름이 구분 없이 붙는다. 배열에 push한 뒤 join하면 읽기 좋다. **구조 개선:** split의 두 번째 부분에 가격을 기대하는 방식은 이름의 공백이나 형식 변경에 약하다. 가격을 data-price로 나누면 의미가 분명하다. **범위:** 화면 계산은 주문 확정이나 서버 가격 검증이 아니다.

개선안은 원본을 수정한 결과가 아니다. 실제 오류, 수업용 단순화, 목적에 따른 선택을 구별해 판단한다.

<a id="teacher"></a>

## 7. 강사님 코드가 도움이 되는 비교

출처: `D:/workspace_teacher/workspace_html/javascript/퀴즈/이벤트.html` 120–143행

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

강사님 발췌는 option의 data-name을 dataset으로 읽고 크기 가격을 별도 속성으로 구분하는 부분만 인용한다. 원본 토핑의 price·topping은 data 속성이 아니라 getAttribute로 읽는 사용자 정의 속성이다. 새 개선 예제는 data-price로 통일한 별도 작성이다. 강사님 버튼 ID login.do는 #login.do로 선택하면 ID와 클래스 조합으로 해석되므로 [id="login.do"]처럼 실제 ID를 정확히 선택한다. 내 ID는 login이라 #login으로 맞다.

<a id="results"></a>

## 8. 결과를 추적하고 한 가지 바꾸기

| 계산·판단 | 입력 예 | 결과 |
| --- | --- | --- |
| 복사 | 체크 당시 주소 서울 | 배송 서울 |
| 이후 원본만 수정 | 주문 부산 | 배송 서울 유지 |
| 로그인 검사 | 아이디·비밀번호 모두 빈 값 | 아이디 경고 우선 |
| 크기·토핑 | small + 감자 | 20000원 |
| 크기·토핑 | small + 감자 + 고구마 | 22000원 |

원본의 도우는 이름을 표시하지만 두 HTML에 도우 가격이 없으므로 임의 추가 요금을 원본 결과에 끼우지 않는다. 선택 radio는 원본 HTML의 기본 checked가 있어 찾을 수 있다. 기본 선택을 없앤 구조로 바꾸면 null 가능성을 따로 처리해야 한다.

| 한 가지만 변경 | 예상 | 이유 |
| --- | --- | --- |
| 체크 해제 | 배송 두 칸이 비워짐 | else의 대입 |
| large 선택 | 토핑 두 개면 26000원 | 기본 크기 가격 22000 |
| join 구분자를 ' / '로 | 이름 사이 표시만 변경 | 계산값은 그대로 |
| Number 제거 | 문자열 연결 가능 | DOM 가격은 문자열 |

합계가 긴 숫자 문자열이면 Number 변환 위치를 본다. 토핑 이름이 붙으면 합산 오류가 아니라 표시용 구분자 문제인지 확인한다. 배송이 안 따라오면 체크 클릭 때만 복사하도록 등록한 현재 동작을 읽는다. trim 오류가 나면 요소 자체와 value 문자열을 혼동했는지 본다.

<a id="tips"></a>

## 9. 추가로 알면 좋은 것과 출처

> 💡 **TIP · 수업 범위 밖:** 서버 인증·주문 저장·서버에서 가격 재검산·복잡한 주문 데이터 모델은 추가 학습이다. 이 장은 실제로 작성한 입력 검사와 브라우저 계산을 중심으로 한다.



이 절의 확장은 기본 문제의 필수 조건이 아니다. 📚 출처가 있다는 것과 수업 밖 기능이라는 것은 다른 구분이다.

<a id="practice"></a>

## 10. 복습과 빠른 정리

1. 체크 뒤 주문 주소를 바꾸면 배송도 자동 갱신되는가?
2. 속성의 가격을 더하기 전에 변환하는 이유는?
3. 도우 이름이 있다고 도우 요금도 더하는가?

<details>
<summary>짧은 풀이 — 먼저 답한 뒤 확인</summary>

현재는 체크 클릭 때만 복사하여 자동 갱신되지 않는다. 가격 속성은 문자열이므로 숫자 덧셈을 위해 변환한다. 두 원본에는 도우 가격이 없으므로 임의로 더하지 않는다.

</details>

| 단계 | 관찰 |
| --- | --- |
| 읽기 | 현재 value·checked |
| 변환 | 문자열에서 숫자로 |
| 계산 | 클릭마다 초기화 |
| 표시 | 이름 목록과 금액 구분 |

[장별 연습문제](실습/연습문제/17-03_JavaScript_주문_로그인_피자실습_연습문제.md)에서 예상·설명·수정을 이어 간다. 다음은 [메뉴·Todo](17-04_JavaScript_메뉴와_Todo실습.md)다.

<!-- 이전 색인 이동 주소 보존 -->
<a id="section-1"></a>
<a id="section-2"></a>
<a id="section-3"></a>
<a id="section-4"></a>
<a id="section-5"></a>

[이 장의 목차](#chapter-toc)에서 현재 설명을 찾는다.
