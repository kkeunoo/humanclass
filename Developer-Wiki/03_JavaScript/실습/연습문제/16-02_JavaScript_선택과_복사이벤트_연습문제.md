# 16-02 JavaScript 선택과 복사이벤트 — 연습문제

[해당 본문](../../16-02_JavaScript_선택과_복사이벤트.md) · [장별 문제 목차](README.md)

**새로 구성한 연습문제**다. 먼저 해당 본문에서 강사님·내 코드와 실제 동작을 읽는다.

## 문제

문장 선택과 복사 이벤트에서 발생한 이벤트 이름을 콘솔에 기록하자.

**확인 기준:** 선택 영역을 만드는 행위와 실제 복사 행위를 구분한다. 기록을 위해 기본 복사 기능을 막을 필요가 있는지 생각한다.

<details>
<summary>해설 — 직접 해 본 뒤 펼치기</summary>

수업 원본에서는 `selectstart`와 `copy`를 따로 다룬다. 시작할 때 `selectstart`, 사용자가 복사를 실행할 때 `copy`가 일어난다. 아래처럼 **발생한 이벤트 이름만 읽으면 된다**.

```html
<p id="sentence">선택하고 복사할 문장</p>
<script>
  const sentence = document.querySelector('#sentence');
  sentence.addEventListener('selectstart', function(event) { console.log(event.type); });
  sentence.addEventListener('copy', function(event) { console.log(event.type); });
</script>
```

`preventDefault()`를 넣으면 원래의 선택·복사 동작 자체가 막힐 수 있으므로 기록 문제에는 넣지 않는다.

</details>

강사님·내 원본의 선택 글자 뒤에 출처 문구를 붙이는 예제는 **복사 결과를 바꾸는 동작**이다. 이 문제는 먼저 선택과 복사가 서로 다른 시점임을 확인하는 단계다.
