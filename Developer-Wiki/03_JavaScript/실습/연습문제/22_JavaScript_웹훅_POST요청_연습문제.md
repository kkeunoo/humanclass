# 22 JavaScript 웹훅 POST요청 — 연습문제

[해당 본문](../../22_JavaScript_웹훅_POST요청.md) · [장별 문제 목차](README.md)

**새로 구성한 연습문제**다. 먼저 해당 본문에서 강사님·내 코드와 실제 동작을 읽는다.

## 문제

강사님·내 원본의 웹훅 요청에서 사용하는 `username`과 `content`를 넣은 객체를 만들고 `JSON.stringify` 결과를 예상하자. XHR의 `open('post', url)`, `setRequestHeader`, `send`에 각각 어떤 종류의 값을 주는지 연결하자. 실제 전송은 하지 않는다.

**확인 기준:** 객체와 문자열의 자료형 차이, 본문 형식을 알리는 헤더, 전송 본문을 구분한다. 주소나 비밀 값을 문서에 넣지 않는다.

<details>
<summary>해설 — 직접 해 본 뒤 펼치기</summary>

```javascript
const param = { username: '연습', content: '안녕하세요' };
const body = JSON.stringify(param);
console.log(body);
// {"username":"연습","content":"안녕하세요"}
```

원본의 `xhr.open('post', url)`은 방식과 주소를, `xhr.setRequestHeader('Content-Type', 'application/json')`은 본문 형식을, `xhr.send(body)`는 실제 보낼 문자열을 정한다. 위 `body` 확인은 로컬 계산이며 외부 요청이 성공했다는 증거가 아니다.

</details>

이 장의 양쪽 코드는 **XHR**로 요청하므로, 새 `fetch` 옵션 객체의 `method`·`headers`·`body` 표기를 기본 답으로 요구하지 않는다. `fetch` 방식은 [21장](../../21_JavaScript_외부AI_API요청과_대화기록.md)의 실제 예제와 비교할 때 읽는다.
