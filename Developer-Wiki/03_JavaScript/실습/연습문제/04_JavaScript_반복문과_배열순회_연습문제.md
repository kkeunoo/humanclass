# 04 JavaScript 반복문과 배열순회 — 연습문제

[해당 본문](../../04_JavaScript_반복문과_배열순회.md) · [장별 문제 목차](README.md)

**새로 구성한 연습문제**다. 먼저 해당 본문에서 강사님·내 코드와 실제 동작을 읽는다.

## 문제

`[3, 8, 1, 6]`을 순회하여 짝수의 개수와 합을 별도로 구하자.

**확인 기준:** 배열 원소마다 짝수 조건의 결과, 누적 개수, 누적 합을 표로 적는다.

<details>
<summary>해설 — 직접 해 본 뒤 펼치기</summary>

```javascript
const values = [3, 8, 1, 6];
let count = 0;
let sum = 0;
for (const value of values) {
  if (value % 2 === 0) {
    count += 1;
    sum += value;
  }
}
console.log(count, sum); // 2 14
```

3과 1에서는 누적값이 그대로다. 8에서 개수 1·합 8, 6에서 개수 2·합 14가 된다. 반복 한 번마다 **검사 → 필요하면 갱신** 순서다.

</details>

강사님·내 원본의 `for`와 배열 순회 예제를 읽을 때도 초기값·종료 조건·매회 변경값을 따로 표시해 보자. `map`·`filter`는 같은 장의 원본 비교 뒤에 읽는다.
