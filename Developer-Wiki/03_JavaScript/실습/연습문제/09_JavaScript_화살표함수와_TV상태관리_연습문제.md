# 09 JavaScript 화살표함수와 TV상태관리 — 연습문제

[해당 본문](../../09_JavaScript_화살표함수와_TV상태관리.md) · [장별 문제 목차](README.md)

**새로 구성한 연습문제**다. 먼저 해당 본문에서 강사님·내 코드와 실제 동작을 읽는다.

## 문제

숫자 하나를 받아 1을 더해 반환하는 함수를 일반 함수와 화살표 함수로 각각 작성하자. 화살표 함수에서 중괄호를 사용할 때 `return`을 빼면 무엇이 나오는지 확인하자.

**확인 기준:** 두 함수의 호출 결과를 비교하고, **짧은 식 반환**과 **중괄호 안의 명시적 반환**을 구분한다.

<details>
<summary>해설 — 직접 해 본 뒤 펼치기</summary>

```javascript
function addOne(value) { return value + 1; }
const addOneArrow = (value) => value + 1;
console.log(addOne(2));      // 3
console.log(addOneArrow(2)); // 3
```

`(value) => { value + 1; }`은 중괄호가 있는 함수 본문에서 반환하지 않아 `undefined`가 된다. 이 문제는 [본문의 화살표 함수 반환](../../09_JavaScript_화살표함수와_TV상태관리.md)을 연습한다.

</details>

TV 채널 상태를 바꾸는 문제는 [다음 09-02장](../../09-02_JavaScript_TV상태관리.md)의 연습문제에서 다룬다. 아직 배우지 않은 DOM 버튼 이벤트를 이 장의 필수 조건으로 넣지 않는다.
