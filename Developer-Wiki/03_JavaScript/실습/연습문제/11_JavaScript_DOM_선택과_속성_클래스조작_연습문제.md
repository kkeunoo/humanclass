# 11 JavaScript DOM 선택과 속성 클래스조작 — 연습문제

[해당 본문](../../11_JavaScript_DOM_선택과_속성_클래스조작.md) · [장별 문제 목차](README.md)

**새로 구성한 연습문제**다. 먼저 해당 본문에서 강사님·내 코드와 실제 동작을 읽는다.

## 문제

아래 HTML에서 `querySelector('#title')`과 `querySelectorAll('.item')`의 반환 결과를 각각 예상하자. 존재하지 않는 `#missing`을 찾을 때도 확인하자.

```html
<h2 id="title">목록</h2>
<p class="item">A</p>
<p class="item">B</p>
```

**확인 기준:** 요소 하나, 요소 목록, 찾지 못한 결과를 구별한다. 목록에 결과가 0개인 경우와 `null`도 같은 값인지 생각한다.

<details>
<summary>해설 — 직접 해 본 뒤 펼치기</summary>

`querySelector('#title')`은 `h2` 요소 하나, `querySelectorAll('.item')`은 두 문단을 담은 목록이다. `querySelector('#missing')`은 `null`이다. 반면 `querySelectorAll('#missing')`은 **빈 목록**이므로 `null`과 같지 않다.

</details>

클래스 추가·제거는 [다음 11-02장](../../11-02_JavaScript_DOM_속성과_클래스.md)에서 배운다. 이 장의 문제는 **무엇을 선택해 돌려받았는가**에 집중한다.
