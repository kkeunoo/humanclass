# 17-03. 주문·로그인·피자 — 입력 상태에서 결과를 만드는 세 단계 — 연습문제

[본문](../../17-03_JavaScript_주문_로그인_피자실습.md) · [문제 목차](README.md)

실제 수업 기능을 바탕으로 **새로 구성한 연습문제**다. 강사님 원본 퀴즈와 구분한다. 예상 → 이유 → 수정 순서로 풀고, 정답은 먼저 답한 뒤 펼친다.

## 목표와 실행 조건

주문 정보 복사와 자동 동기화를 구별하고 로그인 입력 검사의 분기 순서를 읽는다. value 분해와 data 속성의 차이, 숫자 변환·합산·토핑 목록 표시를 설명한다.

[전체 실행 HTML](../책형_복습/17-03_JavaScript_주문_로그인_피자실습.html)과 같은 폴더의 JS를 함께 준비한다. Console을 열고 새로고침하면 처음부터 실행한다. 원본과 별도 파일이므로 기존 변수·타이머·출력 변경 실험의 영향을 섞지 않는다. 실제 입력·현재 시각·난수는 고정 결과와 구별한다.

입력·버튼·키보드·스크롤 예제는 [본문의 3절](../../17-03_JavaScript_주문_로그인_피자실습.md#example)에 적힌 조작 순서대로 결과를 예상한다. 통신 예제는 해당 절의 가상 JSON 파일과 로컬 웹 실행 준비가 필요하며 HTML을 직접 여는 조건과 다르다. Console 출력이 없는 문제는 화면의 값·개수·선택 상태를 답한다.

## 문제 1. 실행 순서와 결과 예상

다음은 **새 설명 예제**다. 출력 전에 어떤 값이 어떤 순서로 만들어지는지 적는다.

**필요한 HTML · 스크립트 앞:**

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

<details>
<summary>힌트와 풀이</summary>

**힌트:** 입력·현재 상태·실행 시점·반환값을 따로 표시한다.

```text
불고기 / small / 감자, 고구마 / 22000원
```

주문 정보와 같음을 체크하면 배송 주소는 서울이다. 주문 주소만 부산으로 고쳐도 배송 주소는 서울로 남는다. 입력 검사 버튼을 빈 상태·아이디만 있는 상태·둘 다 있는 상태에서 눌러 경고가 차례로 바뀌고 지워지는지 본다. 피자는 small과 토핑 두 개를 선택해 계산한다. 18000+2000+2000=22000이며 토핑 이름 사이에 쉼표와 공백이 들어간다. 새 예제는 배운 dataset·배열·join을 사용한 개선 예제다. 원본에 있는 도우 선택은 가격이 없어 이 최소 계산 예제에서는 생략했으며, 원본 전체 기능을 재현했다고 하지 않는다.

</details>

## 문제 2. 개념을 자신의 말로 설명

1. 체크 뒤 주문 주소를 바꾸면 배송도 자동 갱신되는가?
2. 속성의 가격을 더하기 전에 변환하는 이유는?
3. 도우 이름이 있다고 도우 요금도 더하는가?

<details>
<summary>풀이</summary>

현재는 체크 클릭 때만 복사하여 자동 갱신되지 않는다. 가격 속성은 문자열이므로 숫자 덧셈을 위해 변환한다. 두 원본에는 도우 가격이 없으므로 임의로 더하지 않는다.

| 계산·판단 | 입력 예 | 결과 |
| --- | --- | --- |
| 복사 | 체크 당시 주소 서울 | 배송 서울 |
| 이후 원본만 수정 | 주문 부산 | 배송 서울 유지 |
| 로그인 검사 | 아이디·비밀번호 모두 빈 값 | 아이디 경고 우선 |
| 크기·토핑 | small + 감자 | 20000원 |
| 크기·토핑 | small + 감자 + 고구마 | 22000원 |

원본의 도우는 이름을 표시하지만 두 HTML에 도우 가격이 없으므로 임의 추가 요금을 원본 결과에 끼우지 않는다. 선택 radio는 원본 HTML의 기본 checked가 있어 찾을 수 있다. 기본 선택을 없앤 구조로 바꾸면 null 가능성을 따로 처리해야 한다.

</details>

## 문제 3. 한 가지를 바꾸어 확인

먼저 **체크 해제**를 바꾸면 무엇이 달라질지 적는다. 그다음 실행 파일에 해당 변경만 적용해 실제 결과와 비교한다. 나머지 실험도 원래 예제로 돌아가 하나씩 수행한다.

<details>
<summary>변경 결과와 막힐 때 확인</summary>

| 한 가지만 변경 | 예상 | 이유 |
| --- | --- | --- |
| 체크 해제 | 배송 두 칸이 비워짐 | else의 대입 |
| large 선택 | 토핑 두 개면 26000원 | 기본 크기 가격 22000 |
| join 구분자를 ' / '로 | 이름 사이 표시만 변경 | 계산값은 그대로 |
| Number 제거 | 문자열 연결 가능 | DOM 가격은 문자열 |

합계가 긴 숫자 문자열이면 Number 변환 위치를 본다. 토핑 이름이 붙으면 합산 오류가 아니라 표시용 구분자 문제인지 확인한다. 배송이 안 따라오면 체크 클릭 때만 복사하도록 등록한 현재 동작을 읽는다. trim 오류가 나면 요소 자체와 value 문자열을 혼동했는지 본다.

</details>

## 채점과 복습

| 점검 | 확인할 것 |
| --- | --- |
| 예측 | 실행 전에 출력·상태를 적었는가? |
| 근거 | 문법·조건·반환·순서로 설명했는가? |
| 수정 | 한 조건만 바꾸었는가? |
| 확인 | 실제 관찰과 코드 기준 예상을 구분했는가? |

틀린 이유를 설명할 수 없다면 [본문](../../17-03_JavaScript_주문_로그인_피자실습.md)의 작은 예제·내 원본 풀이로 돌아간다. TIP의 미학습 기능은 이 문제의 필수 정답이 아니다.
