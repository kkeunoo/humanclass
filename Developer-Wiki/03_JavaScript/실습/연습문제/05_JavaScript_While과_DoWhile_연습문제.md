# 05 JavaScript While과 DoWhile — 연습문제

[해당 본문](../../05_JavaScript_While과_DoWhile.md) · [장별 문제 목차](README.md)

**새로 구성한 연습문제**다. 먼저 해당 본문에서 강사님·내 코드와 실제 동작을 읽는다.

## 문제

`while`로 3, 2, 1을 출력하고, 조건이 처음부터 거짓일 때 `do...while` 본문이 몇 번 실행되는지 확인하자.

**확인 기준:** 조건을 **본문 앞에서 검사하는지 뒤에서 검사하는지** 먼저 적는다. 반복 변수가 언제 감소하는지도 확인한다.

<details>
<summary>해설 — 직접 해 본 뒤 펼치기</summary>

```javascript
let number = 3;
while (number > 0) {
  console.log(number);
  number -= 1;
}

let ready = false;
do {
  console.log('한 번 실행');
} while (ready);
```

첫 반복은 3, 2, 1을 출력하고 0에서 멈춘다. 둘째는 `ready`가 처음부터 거짓이어도 본문 뒤에 검사하므로 한 번 출력한다. 감소나 종료 조건을 빠뜨리면 반복이 끝나지 않을 수 있다.

</details>

강사님·내 메뉴 실습에는 **다시 입력받는 위치**가 결과를 좌우한다. 위의 숫자 예제에서 배운 검사 순서를 그 원본 메뉴에 적용해 보자.
