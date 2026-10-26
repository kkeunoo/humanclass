# 04. display — 줄을 차지하는 방식 바꾸기

[CSS 목차](README.md)

display는 요소의 박스를 어떻게 배치할지 정한다. HTML 태그의 의미·허용 중첩과 CSS의 배치 방식은 서로 구분한다.

| 원본 실험 | 동작 |
| --- | --- |
| block | 일반 흐름에서 새 줄을 차지. width로 너비를 줄여도 다음 block이 자동으로 옆에 붙지는 않음 |
| inline | 글자 흐름 안에 놓임. 일반 span의 width·height는 적용되지 않음 |
| inline-block | 한 줄에 놓이면서 width·height·padding 등을 가짐 |
| table / table-cell | 표 형태 배치의 박스. HTML table의 의미를 자동 부여하지 않음 |
| none | 박스 배치에서 제외. [숨김 비교](05_CSS_투명도와_요소숨김.md) 참고 |

`img` 같은 대체 요소는 일반 글자 span과 크기 규칙이 다르다. “inline이면 이미지도 width가 안 된다”로 외우지 않는다.

<!-- chapter-toc -->

- [1. inline-block과 공백](04_CSS_Display와_요소배치.md#section-1)
- [2. inline의 padding은 가짜가 아니다](04_CSS_Display와_요소배치.md#section-2)
- [3. 양쪽 원본에서 교정할 부분](04_CSS_Display와_요소배치.md#section-3)
- [복습](04_CSS_Display와_요소배치.md#section-4)

<a id="section-1"></a>

## 1. inline-block과 공백

### 강사님 코드

`asset/css/04_display.css` 65~84행 — **원본 발췌**

```css
.parent3 {
    border: 1px dotted rgb(255,0,255);

    font-size: 0;
}
.parent3 > div {
    border: 1px solid red;
    display: inline-block;

    width: 100px;
    height: 50px;

    padding: 50px;

    /* inline, inline-block 만 적용 됨 */
    /* 세로방향 정렬 */
    vertical-align: top;

    font-size: 16px;
}
```

부모 글자 크기를 0으로 만들어 HTML 줄바꿈·들여쓰기에서 생긴 공백 폭을 줄이고, 자식 글자 크기를 16px로 복원했다. 자식은 width 100px에 좌우 padding 100px·border 2px가 붙어 202px다. `vertical-align:top`으로 서로 윗부분을 맞춘다.

### 내 코드

`asset/css/04_display.css` 77~98행 — **원본 발췌**

```css
.parent3 {
    border: 1px dotted rgb(255, 0, 255);
    font-size: 0px;
}

/* 아래처럼 2줄을 적었을 때 맨 아래 줄 내용(baseline)을 기준으로 줄이 맞춰지기 때문에 약간 올라간 모습 */
/* 아래와 같은 경우 vertical-align으로 정렬을 해줄 수 있다 */
.parent3 > div {
    border: 1px solid red;
    display:inline-block;
    
    width: 100px;
    height: 50px;

    padding: 50px;

    /* vertical은 세로정렬이며 inline에서만 적용 됨(inline, inline-block) */
    vertical-align: top;
    
    /* 4px 공백을 해소하기 위해 부모에 font-size 0을 주고, 하위 자식들에게 별도 font-size를 줌 */
    font-size: 16px;
}
```

선언과 결과가 같다. 내 주석의 “4px 공백”은 이때의 관찰값에 가깝다. 공백 폭은 글꼴·글자 크기 등에 따라 달라지므로 항상 4px라고 가정해 음수 margin을 넣지 않는다.

`vertical-align`은 원본의 inline-block뿐 아니라 뒤의 table-cell에도 적용된다. 모든 block 상자를 부모의 세로 가운데에 놓아 주는 속성은 아니다.

<a id="section-2"></a>

## 2. inline의 padding은 가짜가 아니다

양쪽 `.inline`의 `padding:30px 50px`에서 위아래 padding·border는 실제로 그려진다. 다만 일반 비대체 inline의 **줄 높이 계산을 그만큼 늘려 주지 않아** 다른 줄과 겹칠 수 있다. 위아래 margin이 줄 간격을 만들지 않는다는 것과 구별한다.

강사님은 “border는 밀림”, 나는 “가짜 border”라고 주석을 달았다. 복습할 때는 **그려지는 영역과 줄 배치에 반영되는 영역의 차이**로 고쳐 이해한다. [인라인 배치 표준](https://www.w3.org/TR/CSS2/visuren.html#inline-formatting)

<a id="section-3"></a>

## 3. 양쪽 원본에서 교정할 부분

- 강사님 파일명은 `04_dispaly.html`, 내 파일명은 `04_display.html`이다. 철자가 다른 실제 경로를 확인한다.
- 본문의 `div.block*2`는 편집기 약어를 펼치지 않고 남긴 텍스트라 화면에도 나온다. 필요 없다면 지운다.
- 양쪽의 `<span><div>...</div></span>`는 span의 허용 콘텐츠에 맞지 않는다. display를 바꿔도 HTML 중첩 규칙이 바뀌지는 않는다. 바깥을 div로 바꾸거나 안쪽을 span으로 바꾼 뒤 필요한 display를 지정한다.
- `-webkit-`는 숨겨진 옵션이라는 뜻이 아니라 특정 브라우저 계열에서 시작된 접두 표기다. 해당 속성의 지원과 표준 여부는 개별적으로 확인한다.

`.parent2`의 `text-align:center`는 안쪽 inline-block들을 가운데로 놓는다. 각 자식의 글자 정렬과 부모가 자식 박스를 정렬하는 관계를 나누어 읽는다.

<a id="section-4"></a>

## 복습

width 100px, padding 50px, border 1px인 두 inline-block은 200px짜리 부모 한 줄에 들어갈까?

<details>
<summary>해설</summary>

아니다. 원본의 content-box에서는 하나가 202px다. 공백을 제거해도 박스 자체의 너비 부족은 해결되지 않는다.

</details>

**추가로 알면 좋은 것:** display:contents와 Grid로 배치를 다시 설계하는 예제는 별도 확장이다.

<!-- legacy-migration -->

<a id="css-4"></a>
<a id="css-57"></a>
<a id="css-42"></a>
<a id="css-12"></a>
<a id="css-39"></a>
<a id="css-10"></a>

### 이전 색인 링크 안내

이전 절 주소를 보존한 이동 안내다. 옛 절 번호와 현재 절은 같지 않다. [현재 CSS 목차](README.md)에서 수업 본문과 **추가로 알면 좋은 것**을 구분해 찾는다.

**이 장을 읽은 뒤:** [장별 연습문제 풀기](실습/연습문제/04_CSS_Display와_요소배치_연습문제.md)

