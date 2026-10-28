# 17-04 JavaScript 메뉴와 Todo실습 — 연습문제

[해당 본문](../../17-04_JavaScript_메뉴와_Todo실습.md) · [장별 문제 목차](README.md)

**새로 구성한 연습문제**다. 먼저 해당 본문에서 강사님·내 코드와 실제 동작을 읽는다.

## 문제

Todo 세 개를 추가한 뒤 둘째 항목만 삭제하고 남은 항목 수를 표시하자. 수업 원본처럼 각 항목은 `div`로 만든다.

**확인 기준:** A·B·C 중 **B만 사라졌는지**와 화면의 개수가 실제 항목 `div` 개수와 같은지 확인한다. 목록을 모두 지우는 동작과 구분한다.

<details>
<summary>해설 — 직접 해 본 뒤 펼치기</summary>

항목 A·B·C를 추가한 뒤 B의 삭제 버튼을 누르면 A·C가 남고 전체 개수는 2다. 부모 목록에 리스너 하나를 붙이는 방식이라면 눌린 대상이 삭제 버튼인지 먼저 확인하고, **그 버튼이 속한 B 항목**을 지운다. 그다음 남은 `div`를 다시 세어 화면에 표시한다. 단순히 표시 숫자에서 1만 빼면 다른 삭제 경로와 값이 어긋날 수 있다.

```html
<div id="list">
  <div><span>A</span><button class="del">삭제</button></div>
  <div><span>B</span><button class="del">삭제</button></div>
  <div><span>C</span><button class="del">삭제</button></div>
</div>
<p id="count">3</p>
<script>
  const list = document.getElementById('list');
  list.addEventListener('click', function (event) {
    if (event.target.classList.contains('del')) {
      event.target.parentNode.remove();
      document.getElementById('count').textContent = list.querySelectorAll('div').length;
    }
  });
</script>
```

이 코드는 삭제 부분만 연습하려고 A·B·C를 HTML에 미리 둔 **새 축약 예제**다. 수업 원본처럼 입력값으로 항목을 만드는 방법은 본문 2절에서 확인한다.

</details>

강사님 코드의 메뉴 강조는 이전 선택을 지운 뒤 새 선택을 표시한다. 내 원본의 글자 앞에 `✔`를 붙이는 방식은 같은 메뉴를 다시 누를 때 문구가 누적될 수 있다. 이 Todo 문제는 그 비교를 읽은 뒤 [종합실습](../../24_JavaScript_종합실습.md)으로 이어진다.
