# 10. float와 clear — 글이 이미지를 감싸는 배치

[CSS 목차](README.md)

float는 요소를 한쪽으로 보내고 주변 인라인 내용이 돌아 흐르게 한다. absolute처럼 모든 주변 내용과 무관하게 떠 있는 상자로 외우면 원본의 글 감싸기를 설명하기 어렵다.

<!-- chapter-toc -->

- [1. 원본의 왼쪽·오른쪽 상자](10_CSS_Float와_Clear.md#section-1)
- [2. 부모 높이와 clearfix](10_CSS_Float와_Clear.md#section-2)
- [3. 원본 헤더의 한계](10_CSS_Float와_Clear.md#section-3)
- [복습](10_CSS_Float와_Clear.md#section-4)

<a id="section-1"></a>

## 1. 원본의 왼쪽·오른쪽 상자

양쪽 `article img`는 width:100px·float:right다. 이미지가 로드되면 오른쪽에 있고 본문 글줄이 그 옆으로 흐른다. 이어지는 `.box.left` 두 개와 `.box.right` 두 개는 각각 왼쪽·오른쪽부터 배치된다. 오른쪽의 3·4는 소스 순서와 왼쪽에서 읽는 시각 순서가 다를 수 있다.

내 “float도 inline-block으로 변경”이라는 주석은 교정한다. float는 별도 배치 규칙이며 display:inline-block과 같은 속성 변경이 아니다. clear는 float를 취소하거나 DOM 순서를 바꾸지 않고, 해당 요소가 앞선 float 아래로 내려가게 하는 조건이다.

<a id="section-2"></a>

## 2. 부모 높이와 clearfix

### 강사님 코드

`asset/css/10_float.css` 25~29행 — **원본 발췌**

```css
.clearFix:after {
    content: "";
    display: block;
    clear: both;
}
```

부모 안의 마지막에 빈 가상 요소를 만들고 clear:both를 적용한다. 부모 안에 float 자식만 있어 높이를 원하는 대로 감싸지 못하는 상황을 이 후행 박스로 해결한다.

### 내 코드

`asset/css/10_float.css` 29~38행 — **원본 발췌**

```css
/* float을 clear:both로 내린다고 해도 그 층에 남아있음 */
.clearFix:after {
    content: "";
    display: block;
    clear: both;
}

/* .test {
    clear: both;
} */
```

실행되는 clearfix는 같다. `.test`의 clear는 주석 상태다. 부모의 class가 정확히 clearFix인지도 확인한다. 내 HTML의 “float을 초기화”는 **자식의 float 선언을 지우는 것**이 아니라 이후 흐름과 부모 높이를 정리한다는 뜻으로 읽는다.

### HTML에 적용한 강사님 코드

`10_float.html` 27~31행 — **원본 발췌**

```html
    <div class="clearFix">
        <div class="box left">왼쪽</div>
        <div class="box right">오른쪽</div>
    </div>
    <div style="border: 1px solid red;">다른 내용의 시작</div>
```

### 같은 위치의 내 코드

`10_float.html` 26~30행 — **원본 발췌**

```html
        <div class="clearFix">
            <div class="box left">왼쪽</div>
            <div class="box right">오른쪽</div>
        </div>
        <div class="test" style="border: 1px solid red;">다른 내용의 시작</div>
```

부모가 float 자식 두 개와 가상 요소를 감싸고 다음 내용이 아래에 이어진다. 원본 앞부분의 `<div style="clear:both"></div>`는 실제 빈 요소를 쓰는 방식이고, clearfix는 가상 요소로 같은 종류의 후행 정리 역할을 한다. [float·clear 표준](https://www.w3.org/TR/CSS2/visuren.html#floats)

<a id="section-3"></a>

## 3. 원본 헤더의 한계

헤더는 왼쪽·오른쪽 float와 가운데 inline-block 로고를 섞는다. 남은 공간 가운데 정렬과 화면 전체 정중앙은 양쪽 메뉴 너비가 다르면 달라질 수 있다. 내 `.coup div` 규칙은 이 HTML에 coup 요소가 없어 매칭되지 않는다. 선언이 존재하는 것과 실제 적용되는 것을 구분한다.

<a id="section-4"></a>

## 복습

clearfix를 부모에 적용하면 자식의 float:left가 none으로 바뀔까?

<details>
<summary>해설</summary>

아니다. 자식의 float는 유지된다. 부모 안의 후행 clear 박스가 배치 결과에 영향을 주는 것이다.

</details>

**추가로 알면 좋은 것:** flow-root·shape-outside·Grid 헤더 대체는 별도 학습이다. 배운 float 실험을 새 기술 예제로 통째로 바꾸지 않는다.

<!-- legacy-migration -->

<a id="css-4"></a>
<a id="css-18"></a>

### 이전 색인 링크 안내

이전 절 주소를 보존한 이동 안내다. 옛 절 번호와 현재 절은 같지 않다. [현재 CSS 목차](README.md)에서 수업 본문과 **추가로 알면 좋은 것**을 구분해 찾는다.

<!-- inlined-extra-2026 -->

**이 장을 읽은 뒤:** [장별 연습문제 풀기](실습/연습문제/10_CSS_Float와_Clear_연습문제.md)

## 추가로 알면 좋은 것

이하의 내용은 **수업 원본에서 확인된 필수 진도가 아닌 추가 학습**이다. 위의 기본 설명을 이해한 뒤 필요할 때 읽는다.

<a id="extra-01-3"></a>

### 3. float 이후의 flow-root

```css
/* 추가 예제: float 자식을 감싸는 부모 */
.float-parent { display: flow-root; }
```

새 블록 서식 맥락을 만들어 float 자식을 감싸는 높이 계산에 사용할 수 있다. 기존 clearfix의 역할을 비교할 때 유용하지만, 수업에서 배운 가상 요소·clear를 설명하지 못한 채 이것만 정답으로 외우지는 않는다. [CSS display 표준](https://www.w3.org/TR/css-display-3/#valdef-display-flow-root)

display:contents는 요소의 박스와 의미·접근성 영향을 따로 검토해야 한다. shape-outside·복잡한 겹침 맥락·isolation도 별도 심화다.
