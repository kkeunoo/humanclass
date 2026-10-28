# 08-02 JavaScript 함수참조와 콜백 — 연습문제

[해당 본문](../../08-02_JavaScript_함수참조와_콜백.md) · [장별 문제 목차](README.md)

**새로 구성한 연습문제**다. 먼저 해당 본문에서 강사님·내 코드와 실제 동작을 읽는다.

## 문제

`run(callback)`이 전달받은 함수를 한 번 부르게 작성하자. `done`이라는 함수를 만든 다음 `run(done)`과 `run(done())`가 왜 다른지 예상하자.

**확인 기준:** 함수를 **전달**한 때와 먼저 **호출**한 때를 나누어 실행 순서를 설명한다.

<details>
<summary>해설 — 직접 해 본 뒤 펼치기</summary>

```javascript
function done() { console.log('완료'); }
function run(callback) { callback(); }

run(done); // run 안에서 '완료' 한 번
```

`run(done())`은 인자를 넘기기 전에 `done()`을 실행한다. `done`은 명시적 반환값이 없으므로 그 결과 `undefined`가 `run`에 전달된다. 위처럼 `run`이 무조건 `callback()`을 호출하면 그때는 오류가 난다. **원본의 `test(fn)`에는 함수인지 검사하는 조건이 있었다**는 차이도 확인하자.

</details>

화살표 함수 표기는 [09장](../../09_JavaScript_화살표함수와_TV상태관리.md)에서 배운 다음 적용해도 된다. 이 장의 핵심은 괄호를 붙인 호출과 함수 참조의 차이다.
