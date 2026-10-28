# 10 JavaScript 문자열과 문자열메서드 — 연습문제

[해당 본문](../../10_JavaScript_문자열과_문자열메서드.md) · [장별 문제 목차](README.md)

**새로 구성한 연습문제**다. 먼저 해당 본문에서 강사님·내 코드와 실제 동작을 읽는다.

## 문제

`"  JavaScript Wiki  "`의 양끝 공백을 지운 뒤 `"Wiki"`가 시작하는 위치를 찾아보자. `"Python"`을 찾으면 무엇이 나오는지도 예상하자.

**확인 기준:** `trim()` 뒤 문자열과 `indexOf()`의 두 결과를 따로 적는다. 값이 없을 때의 결과를 0과 혼동하지 않는다.

<details>
<summary>해설 — 직접 해 본 뒤 펼치기</summary>

```javascript
const text = '  JavaScript Wiki  '.trim();
console.log(text);                  // 'JavaScript Wiki'
console.log(text.indexOf('Wiki'));  // 11
console.log(text.indexOf('Python')); // -1
```

`trim()`은 앞뒤 공백만 제거한다. `indexOf()`는 찾은 시작 위치를 돌려주고, 없으면 `-1`이다. 강사님·내 원본의 이메일에서 `@` 위치를 찾는 방법도 같은 원리다.

</details>

`toLowerCase()`와 `includes()`를 조합하는 방법은 이 장의 양쪽 원본에서 확인되지 않았다. **추가로 알면 좋은 것**으로만 보고, 기본 문제는 실제 배운 `trim()`·`indexOf()`로 푼다.
