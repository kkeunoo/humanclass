# 06 JavaScript 배열과 배열메서드 — 연습문제

[해당 본문](../../06_JavaScript_배열과_배열메서드.md) · [장별 문제 목차](README.md)

**새로 구성한 연습문제**다. 먼저 해당 본문에서 강사님·내 코드와 실제 동작을 읽는다.

## 문제

`[10, 20, 30]`에서 20 이상만 남겨 각각 2배로 만든 새 배열을 구하자. 원본도 출력하자.

**확인 기준:** 조건에 남는 원소, 두 배로 바뀐 원소, 원본 배열의 최종 상태를 각각 적는다.

<details>
<summary>해설 — 직접 해 본 뒤 펼치기</summary>

```javascript
const values = [10, 20, 30];
const selected = values.filter(function(value) { return value >= 20; });
const doubled = selected.map(function(value) { return value * 2; });
console.log(selected); // [20, 30]
console.log(doubled); // [40, 60]
console.log(values);  // [10, 20, 30]
```

`filter`와 `map`은 [04장 원본](../../04_JavaScript_반복문과_배열순회.md)에서 먼저 사용했다. 두 메서드는 여기서 새 배열을 만들므로 원본은 그대로다. 반대로 이 장의 `push`는 원본을 바꾼다.

</details>

강사님·내 06장 코드의 `push`·`slice`·`sort`를 같은 기준으로 **반환값 / 원본 변경 여부** 표에 넣어 보자.
