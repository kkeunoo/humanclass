# 14. 미디어쿼리 — 화면 조건에 따라 규칙 바꾸기

[CSS 목차](README.md)

미디어쿼리는 조건을 만족할 때 안쪽 CSS도 적용하도록 한다. 기존 CSS 파일 전체를 지우고 새 파일로 바꾸는 동작은 아니다.

<!-- chapter-toc -->

- [1. 600px 경계](14_CSS_미디어쿼리와_반응형.md#section-1)
- [2. 원본 메뉴가 완성된 메뉴는 아닌 이유](14_CSS_미디어쿼리와_반응형.md#section-2)
- [복습](14_CSS_미디어쿼리와_반응형.md#section-3)

<a id="section-1"></a>

## 1. 600px 경계

### 강사님 코드

`14_media.html` 25~37행 — **원본 발췌**

```css
        @media screen 
        and (max-width: 600px)
        /* and (min-width: 500px) */
        {
            /* 또 다른 CSS 영역 */
            li {
                display: block;
                width: 100%;
            }

            span {
                display: inline;
            }
```

화면 너비가 600px 이하이면 li는 inline-block에서 block으로, 너비는 100px에서 100%로 바뀐다. 메뉴 안내 span도 표시한다. 600px 자체가 포함된다.

### 내 코드

`14_media.html` 25~37행 — **원본 발췌**

```css
        @media screen 
        and (max-width: 600px)
        /* and (min-width: 500px) */
        {
            /* 또 다른 CSS 영역 */
            li {
                display: block;
                width: 100%;
            }

            span {
                display: inline;
            }
```

이 파일은 양쪽 내용이 같다. min-width:500px는 주석이므로 현재 500px보다 작은 화면도 조건에 맞는다. 주석을 해제해 and로 연결하면 500~600px 사이만 만족한다.

| 뷰포트 너비 | 현재 쿼리 | 메뉴 li | 안내 span |
| --- | --- | --- | --- |
| 601px | 불일치 | inline-block, 100px | none |
| 600px | 일치 | block, 100% | inline |
| 500px | 일치 | block, 100% | inline |

원본 head의 viewport 메타는 모바일에서 레이아웃 뷰포트를 기기 너비에 맞추어 보려는 설정이다. 화면 너비 조건은 CSS 픽셀로 읽는다. [미디어쿼리 표준](https://www.w3.org/TR/mediaqueries-4/)

<a id="section-2"></a>

## 2. 원본 메뉴가 완성된 메뉴는 아닌 이유

양쪽은 좁은 화면에서 ul을 opacity:0, top:-20px로 두고 `span:hover + ul`일 때 opacity:1, top:0으로 바꾼다. display:none은 주석이다.

- 투명한 ul의 자리는 남는다. [숨김 차이](05_CSS_투명도와_요소숨김.md)를 적용해 읽는다.
- 포인터가 span에서 메뉴로 이동하면 span:hover가 풀릴 수 있다.
- span은 일반적으로 키보드 버튼처럼 동작하지 않는다. 터치에서 hover 기반 동작도 동일하게 보장되지 않는다.
- transition이 hover에만 있어 돌아갈 때의 움직임은 들어갈 때와 다르다.
- li의 width:100%에 content-box 테두리가 더해져 부모 너비보다 2px 커질 수 있다.

수업 범위에서 너비 넘침만 교정하려면 해당 li에 `box-sizing:border-box`를 적용해 비교한다. 새로운 JavaScript 토글 메뉴 전체를 기본 예제의 정답으로 요구하지 않는다.

<a id="section-3"></a>

## 복습

600px에서 메뉴가 보이지 않는다면 미디어쿼리가 실패했다고 단정할 수 있을까?

<details>
<summary>해설</summary>

없다. 조건이 맞아도 원본은 ul을 투명하게 만든다. li의 display·span의 표시·ul의 opacity를 각각 확인한다.

</details>

**추가로 알면 좋은 것:** Container Query·새 장치 조건·키보드와 터치를 지원하는 토글 메뉴 구현은 추가편이다.

<!-- legacy-migration -->

<a id="css-48"></a>
<a id="css-24"></a>
<a id="css-23"></a>
<a id="css-4"></a>
<a id="css-26"></a>
<a id="css-18"></a>
<a id="css-21"></a>
<a id="css-46"></a>
<a id="css-37"></a>
<a id="css-12"></a>
<a id="css-6"></a>
<a id="css-16"></a>
<a id="css-11"></a>

### 이전 색인 링크 안내

이전 절 주소를 보존한 이동 안내다. 옛 절 번호와 현재 절은 같지 않다. [현재 CSS 목차](README.md)에서 수업 본문과 **추가로 알면 좋은 것**을 구분해 찾는다.

<!-- inlined-extra-2026 -->

**이 장을 읽은 뒤:** [장별 연습문제 풀기](실습/연습문제/14_CSS_미디어쿼리와_반응형_연습문제.md)

## 추가로 알면 좋은 것

이하의 내용은 **수업 원본에서 확인된 필수 진도가 아닌 추가 학습**이다. 위의 기본 설명을 이해한 뒤 필요할 때 읽는다.

<a id="extra-01-4"></a>

### 4. 미디어쿼리와 Container Query

```css
/* 추가 예제: 부모의 가로 크기를 기준으로 자식 표현 변경 */
.panel { container-type: inline-size; }
@container (min-width: 500px) {
    .panel-content { display: flex; }
}
```

수업의 미디어쿼리는 뷰포트 조건을 보지만, 이 예제는 크기 질의 컨테이너가 된 부모의 너비를 본다. 같은 화면에서도 좁은 사이드바와 넓은 본문에 들어간 컴포넌트가 달리 반응하게 만들 때 학습할 수 있다. [컨테이너 질의 표준](https://www.w3.org/TR/css-contain-3/)
