# 03 JavaScript 조건문과 Switch — 연습문제

[해당 본문](../../03_JavaScript_조건문과_Switch.md) · [장별 문제 목차](README.md)

**새로 구성한 연습문제**다. 먼저 해당 본문에서 강사님·내 코드와 실제 동작을 읽는다.

## 문제

점수 82를 A(90 이상), B(80 이상), C(그 외)로 표시하는 `if / else if / else`를 작성하자. 90점과 79점으로도 바꾸어 실행해 보자.

**확인 기준:** 82점에서 어느 조건이 먼저 참인지 추적한다. 경계값 90점과 79점도 의도한 갈래로 가는지 확인한다.

<details>
<summary>해설 — 직접 해 본 뒤 펼치기</summary>

```javascript
const score = 82;
if (score >= 90) console.log('A');
else if (score >= 80) console.log('B');
else console.log('C');
```

82점은 첫 조건이 거짓, 둘째가 참이어서 `B` 한 번이다. 90점은 `A`, 79점은 `C`다. `score >= 80`을 먼저 놓으면 90점도 B가 될 수 있으므로 **조건 순서**를 확인한다.

</details>

`switch`는 수업 원본처럼 **정해진 값과 case를 비교하는 문제**에서 다시 연습한다. 이 점수 구간 문제를 풀기 위해 배우지 않은 `switch(true)` 패턴을 필수로 넣지 않는다.
