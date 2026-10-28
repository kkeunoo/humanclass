# 09-02 JavaScript TV상태관리 — 연습문제

[해당 본문](../../09-02_JavaScript_TV상태관리.md) · [장별 문제 목차](README.md)

**새로 구성한 연습문제**다. 먼저 해당 본문에서 강사님·내 코드와 실제 동작을 읽는다.

## 문제

수업 원본처럼 `power`와 `lastCh`를 **별도 변수**로 두고, 전원을 켠 뒤 채널을 2로 변경하는 함수 호출 순서를 적자. 전원이 꺼져 있을 때는 채널을 바꾸지 않도록 한다.

**확인 기준:** 호출 전후 `power`, `lastCh`의 값을 표로 적는다. 화면 문구만 바뀌고 실제 채널 변수가 그대로인 경우를 구별한다.

<details>
<summary>해설 — 직접 해 본 뒤 펼치기</summary>

```javascript
let power = false;
let lastCh = 1;
function powerOn() { power = true; }
function channel(ch) {
  if (!power) return;
  if (ch < 0 || ch > 10) return;
  lastCh = ch;
}

channel(2); // 전원이 꺼져 있으므로 lastCh는 1
powerOn();
channel(2); // 이제 lastCh는 2
```

양쪽 원본처럼 **출력 문구와 실제 저장된 값**을 나누어 본다. 원본은 범위 밖 채널과 꺼진 전원에 대해 안내 문구도 출력한다. 위 코드는 변수 변화를 보기 위한 새 축약 예제다.

</details>

`{power: false, channel: 1}` 같은 객체로 상태를 묶는 방법은 [19장 객체](../../19_JavaScript_객체와_JSON.md) 이후에 응용할 수 있다. 이 장의 원본 TV 실습은 별도 변수로 상태를 다루므로 객체 문법을 필수 조건으로 앞당기지 않는다.
