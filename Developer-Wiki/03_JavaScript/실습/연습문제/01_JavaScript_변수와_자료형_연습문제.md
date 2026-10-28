# 01 JavaScript 변수와 자료형 — 연습문제

[해당 본문](../../01_JavaScript_변수와_자료형.md) · [장별 문제 목차](README.md)

**새로 구성한 연습문제**다. 먼저 해당 본문에서 강사님·내 코드와 실제 동작을 읽는다.

## 문제

문자열 `"7"`과 숫자 `7`을 각각 변수에 넣고 `typeof`, `+`, `===` 결과를 출력하자.

**확인 기준:** 각 변수의 값과 자료형을 먼저 적고, `+`와 `===`가 무엇을 비교·계산하는지 예상한다.

<details>
<summary>해설 — 직접 해 본 뒤 펼치기</summary>

```javascript
const text = '7';
const number = 7;
console.log(typeof text);    // 'string'
console.log(typeof number);  // 'number'
console.log(text + number);  // '77'
console.log(text === number); // false
```

문자열이 섞인 `+`는 이어 붙인 결과를 만든다. 숫자 14를 원하면 수업의 `Number(text) + number`처럼 변환한 뒤 더한다. 화면에 같은 7로 보이는 것과 자료형이 같은 것은 다르다.

</details>

강사님·내 원본의 `typeof`와 숫자 변환 예제를 찾아 위의 `'7'`을 다른 입력으로 바꾸어 보자. 비교식의 결과와 변수 자체의 값은 별도로 기록한다.
