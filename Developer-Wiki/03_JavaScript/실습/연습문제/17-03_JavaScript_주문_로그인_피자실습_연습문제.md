# 17-03 JavaScript 주문 로그인 피자실습 — 연습문제

[해당 본문](../../17-03_JavaScript_주문_로그인_피자실습.md) · [장별 문제 목차](README.md)

**새로 구성한 연습문제**다. 먼저 해당 본문에서 강사님·내 코드와 실제 동작을 읽는다.

## 문제

새 연습 가격표를 **작은 피자 10,000원 / 큰 피자 15,000원**으로 정한다. 큰 피자 2개를 선택했을 때 합계를 구하고, 수량이 0 이하이면 계산 대신 안내문을 표시하자.

**확인 기준:** 선택한 크기의 단가와 수량을 따로 읽고, 숫자 변환·유효성 검사를 한 뒤 계산한다. 원본 가격표와 이 문제의 새 가격표를 혼동하지 않는다.

<details>
<summary>해설 — 직접 해 본 뒤 펼치기</summary>

큰 피자 2개라면 `15000 × 2 = 30000`원이다. `input.value`는 숫자처럼 보여도 문자열이므로 계산 전에 `Number(...)`로 바꾼다. 수량이 0이라면 합계 0원을 “정상 주문”으로 표시하지 말고 안내를 보여 준다. 강사님·내 원본의 피자 선택 코드도 **선택 상태와 계산 결과**를 따로 확인한다.

```html
<select id="size"><option value="10000">작은 피자</option><option value="15000">큰 피자</option></select>
<input id="quantity" type="number" value="2">
<button id="calculate">계산</button><p id="result"></p>
<script>
  document.getElementById('calculate').addEventListener('click', function () {
    const price = Number(document.getElementById('size').value);
    const quantity = Number(document.getElementById('quantity').value);
    const result = document.getElementById('result');
    if (quantity <= 0) {
      result.textContent = '수량을 확인하세요';
    } else {
      result.textContent = (price * quantity) + '원';
    }
  });
</script>
```

큰 피자를 선택한 상태에서 실행하면 `30000원`이 표시된다. 이 코드는 **새 연습의 가격·수량 조건**을 구현한 것이며 원본 피자 주문의 발췌가 아니다.

</details>

이 문제의 가격은 수업 원본에서 발췌한 값이 아니라 계산을 연습하기 위해 새로 정한 조건이다. 원본과 비교할 때는 숫자 자체보다 **선택 → 변환 → 검사 → 계산** 순서를 본다.
