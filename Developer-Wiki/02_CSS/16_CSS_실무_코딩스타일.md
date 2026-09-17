---
title: CSS 실무 코딩 스타일
version: v4.1-detailed-learning
last_updated: 2026-09-17
status: Completed
---

# CSS 실무 코딩 스타일

## 문서 내 목차

- [문서 정보](#css-1)
- [개요](#css-2)
- [공통 예제 구조](#css-3)
- [핵심 기준](#css-4)
- [학습 목표](#css-5)
- [개념에서 실제 동작까지](#css-6)
- [1. Class 이름은 역할을 표현한다](#css-7)
- [2. ID보다 Class를 기본으로 사용한다](#css-8)
- [3. Tag Selector에 Component Style을 직접 묶지 않는다](#css-9)
- [4. 긴 후손 Selector를 피한다](#css-10)
- [5. Selector 깊이를 낮게 유지한다](#css-11)
- [6. BEM은 목적에 맞게 사용한다](#css-12)
- [7. Utility Class는 한 가지 책임만 가진다](#css-13)
- [8. 상태는 `is-`, `has-` 형태로 표현할 수 있다](#css-14)
- [9. Attribute 상태도 활용한다](#css-15)
- [10. Cascade를 먼저 이해하고 덮어쓴다](#css-16)
- [11. 명시도를 높여서 문제를 해결하지 않는다](#css-17)
- [12. `!important`는 예외적으로 사용한다](#css-18)
- [13. `:where()`로 명시도를 낮출 수 있다](#css-19)
- [14. `:is()`는 반복 Selector를 줄인다](#css-20)
- [15. Cascade Layer로 역할 순서를 관리한다](#css-21)
- [16. 전역 Reset은 의도적으로 작성한다](#css-22)
- [17. `border-box`를 전역으로 통일한다](#css-23)
- [18. 물리 방향보다 논리 속성을 고려한다](#css-24)
- [19. 간격은 Scale로 관리한다](#css-25)
- [20. 자식 Margin보다 부모 `gap`을 우선 검토한다](#css-26)
- [21. 색상은 역할 기반 Token으로 관리한다](#css-27)
- [22. Component Token으로 의미를 좁힌다](#css-28)
- [23. Fallback 값을 제공한다](#css-29)
- [24. `rem`을 기본 크기 단위로 활용한다](#css-30)
- [25. 유연한 크기는 `clamp()`로 설계한다](#css-31)
- [26. Container 너비는 `min()`과 `max-width`를 활용한다](#css-32)
- [27. `100vw`보다 `100%`가 적합한 경우가 많다](#css-33)
- [28. 높이는 콘텐츠를 우선한다](#css-34)
- [29. Full Viewport에는 동적 단위를 검토한다](#css-35)
- [30. Layout은 Flexbox와 Grid를 우선한다](#css-36)
- [31. Flexbox는 주축과 교차축을 기준으로 작성한다](#css-37)
- [32. Flex Item에는 `min-width: 0`이 필요할 수 있다](#css-38)
- [33. Grid는 반복 Column을 간결하게 만든다](#css-39)
- [34. Position은 기준 요소를 명확히 만든다](#css-40)
- [35. `z-index` 숫자를 무작정 높이지 않는다](#css-41)
- [36. Float는 기사 Text 흐름에 제한적으로 사용한다](#css-42)
- [37. 숨김 방식은 목적에 맞게 선택한다](#css-43)
- [38. `opacity: 0`만으로 숨기지 않는다](#css-44)
- [39. Overflow는 문제를 숨기는 용도로 사용하지 않는다](#css-45)
- [40. 긴 문자열을 안전하게 처리한다](#css-46)
- [41. Typography는 공통 Scale로 관리한다](#css-47)
- [42. 본문 줄높이는 단위 없이 작성한다](#css-48)
- [43. Web Font는 Fallback과 성능을 함께 고려한다](#css-49)
- [44. 링크는 Hover만으로 상태를 표현하지 않는다](#css-50)
- [45. Focus Outline을 제거하지 않는다](#css-51)
- [46. Disabled 상태는 색상만으로 표현하지 않는다](#css-52)
- [47. 상태 표현은 JavaScript Inline Style보다 Class를 사용한다](#css-53)
- [48. Inline Style은 동적 수치에 제한적으로 사용한다](#css-54)
- [49. Background Image는 장식에 사용한다](#css-55)
- [50. Background 위 Text 대비를 확인한다](#css-56)
- [51. Shadow는 깊이와 상태를 제한적으로 표현한다](#css-57)
- [52. Transition은 변경 속성을 명시한다](#css-58)
- [53. Transition은 기본 상태에 작성한다](#css-59)
- [54. 움직임에는 Transform과 Opacity를 우선 검토한다](#css-60)
- [55. `prefers-reduced-motion`을 제공한다](#css-61)
- [56. Mobile First로 기본 Style을 작성한다](#css-62)
- [57. Breakpoint는 Device 이름보다 Layout 기준으로 정한다](#css-63)
- [58. Hover 가능 여부를 조건으로 사용할 수 있다](#css-64)
- [59. Container Query로 Component를 독립시킨다](#css-65)
- [60. Dark Mode는 Token을 교체한다](#css-66)
- [61. CSS 파일은 역할별로 분리한다](#css-67)
- [62. Import 순서를 고정한다](#css-68)
- [63. Component와 Page Layout을 분리한다](#css-69)
- [64. 주석은 이유와 제약을 설명한다](#css-70)
- [65. Browser 기본 Style을 이해하고 덮어쓴다](#css-71)
- [66. CSS Validation과 Lint를 자동화한다](#css-72)
- [67. 실제 개선 사례 1: 구조 의존 Selector](#css-73)
- [68. 실제 개선 사례 2: `rem` 기준 오해](#css-74)
- [69. 실제 개선 사례 3: 부모 배경색 상속 오해](#css-75)
- [70. 실제 개선 사례 4: Margin Collapse 만능 해결](#css-76)
- [71. 실제 개선 사례 5: 잘못된 HTML 중첩](#css-77)
- [72. 실제 개선 사례 6: 숨김 방식 혼동](#css-78)
- [73. 실제 개선 사례 7: Background와 콘텐츠 이미지 혼동](#css-79)
- [74. 실제 개선 사례 8: Absolute Position 중앙 정렬](#css-80)
- [75. 실제 개선 사례 9: Float Layout](#css-81)
- [76. 실제 개선 사례 10: Hover 전용 Transition](#css-82)
- [77. 실제 개선 사례 11: `transition: all`](#css-83)
- [78. 실제 개선 사례 12: Transform 함수 덮어쓰기](#css-84)
- [79. 실제 개선 사례 13: Hover 메뉴 접근성](#css-85)
- [80. 실제 개선 사례 14: Flex 시각 순서](#css-86)
- [81. 실무형 예제: 반응형 Product Card](#css-87)
- [82. 파일 구조 예시](#css-88)
- [83. 자주 하는 실수](#css-89)
- [84. 핵심 요약](#css-90)
- [85. 최종 체크리스트](#css-91)
- [마무리](#css-92)
- [렌더링 복습 카드 — 의도·범위·재사용성이 보이는 규칙](#css-93)


<a id="css-1"></a>

## 문서 정보

| 항목 | 내용 |
| --- | --- |
| 문서 | `16_CSS_실무_코딩스타일.md` |
| 분류 | `02_CSS` |
| 문서 성격 | CSS 실무 예제 및 리팩토링 기준 문서 |
| 핵심 범위 | 네이밍, Cascade, 명시도, 변수, Layout, 반응형, 상태, 접근성, 성능, 파일 구조 |
| 예제 형식 | Before → After → 결과 → 개선 이유 → 실무 선택 기준 |
| 종합실습 | 별도 문서 `17_CSS_종합실습.md`에서 관리 |
| 문서 형식 | CSS Developer-Wiki 상세 동작 학습판 |

> 이 문서는 새로운 CSS 속성을 배우는 문서가 아니다.  
> CSS 01~15번에서 학습한 선택자·박스 모델·Layout·반응형·시각 효과를 **실무에서는 어떤 기준으로 선택하고 조합하는지** 설명하는 기준 문서다.

---

<a id="css-2"></a>

## 개요

화면이 원하는 모습으로 보인다고 해서 반드시 좋은 CSS는 아니다.

```css
#header div ul li a:hover {
    color: red !important;
}
```

```css
.nav-link:hover,
.nav-link:focus-visible {
    color: var(--color-primary);
}
```

두 코드는 비슷한 결과를 만들 수 있지만 유지보수성은 다르다.

```text
첫 번째 코드
→ 구조에 강하게 의존
→ 명시도 높음
→ !important 사용
→ Keyboard 상태 누락

두 번째 코드
→ 역할 기반 Class
→ 낮고 예측 가능한 명시도
→ 디자인 토큰 사용
→ Hover·Focus 상태 함께 제공
```

실무 CSS는 다음 질문을 반복해서 확인한다.

```text
이 Selector는 HTML 구조가 바뀌어도 유지되는가?
    ↓
같은 값을 한곳에서 관리할 수 있는가?
    ↓
Layout과 시각 효과의 책임이 분리되어 있는가?
    ↓
모바일·Keyboard·Reduced Motion 환경에서도 사용할 수 있는가?
    ↓
다른 Component에 영향을 주지 않는가?
    ↓
삭제하거나 수정할 때 영향 범위를 예측할 수 있는가?
```

> [!IMPORTANT]
> CSS 실무 코딩 스타일의 목적은 속성을 적게 쓰는 것이 아니다.
>
> **의도가 보이고, 충돌이 적고, 반응형으로 확장 가능하며, 접근성과 유지보수를 함께 만족하는 Style Sheet**를 만드는 것이 목적이다.

---

<a id="css-3"></a>

## 공통 예제 구조

이 문서에서는 다음 Card Component를 여러 예제에서 사용한다.

```html
<article class="product-card">
    <img
        class="product-card__image"
        src="./images/keyboard.webp"
        alt="기계식 키보드"
    >

    <div class="product-card__body">
        <span class="product-card__badge">
            인기
        </span>

        <h2 class="product-card__title">
            기계식 키보드
        </h2>

        <p class="product-card__description">
            업무와 학습에 적합한 키보드입니다.
        </p>

        <button
            type="button"
            class="button button--primary"
        >
            장바구니 담기
        </button>
    </div>
</article>
```

```css
.product-card {
    display: grid;
    gap: 1rem;
    padding: 1rem;
    border: 1px solid var(--color-border);
    border-radius: var(--radius-medium);
    background: var(--color-surface);
}
```

---

<a id="css-4"></a>

## 핵심 기준

| 기준 | 의미 |
| --- | --- |
| 역할 기반 네이밍 | 모양보다 Component와 상태의 의미를 표현 |
| 낮은 명시도 | Selector 충돌과 덮어쓰기 비용 감소 |
| 디자인 토큰 | 색상·간격·크기·그림자를 한곳에서 관리 |
| Layout 분리 | Flex·Grid·Position의 역할을 구분 |
| 상태 클래스 | JavaScript는 상태만 변경하고 CSS가 표현 담당 |
| Mobile First | 작은 화면 기본값에서 필요한 만큼 확장 |
| 접근성 | Hover뿐 아니라 Focus·Motion·Contrast 고려 |
| 예측 가능한 Cascade | 선언 순서와 Layer를 의도적으로 관리 |
| Component 범위 | 다른 화면과 Component에 영향 최소화 |
| 성능 | Layout·Paint 비용이 큰 효과를 필요한 곳에만 사용 |

---

<a id="css-5"></a>

## 학습 목표

- 주요 속성의 의미와 차이를 설명한다.
- 대상과 계산 기준을 찾고 결과를 예측한다.
- 원본을 비교하고 적용·배치 오류를 수정한다.

<a id="learning-flow"></a>

<a id="css-6"></a>

## 개념에서 실제 동작까지

### 코딩 스타일이란? 표현 의도를 유지하며 변경 범위를 통제하는 규칙

좋은 CSS 스타일은 단순 정렬이 아니라 “어느 요소의 어떤 속성이 왜 이겼는지”를 추적 가능하게 만드는 것입니다. 이름 통일·토큰·낮은 명시도는 수정 영향을 예측하기 위한 수단이지 목적 없는 규칙 암기가 아닙니다.

**수업과 보충의 경계:** 01~15의 원본을 비교하고 그 문제를 개선하는 확장 학습입니다. BEM·레이어·토큰·Grid 등 모든 기준이 번호형 수업에서 그대로 사용됐다고 주장하지 않습니다. 💡 보충 설계로 읽습니다.

내 수업 소스는 [human]에 important border를 적용했습니다. 그 예제는 중요도 실험이므로 당시 코드를 틀렸다고 삭제하지 않습니다. 실제 컴포넌트 설계에서는 선택자가 역할과 상태를 드러내도록 다시 구성합니다.

💡 개선 예제:

```css
.card { border: 1px solid var(--card-border, #ddd); }
.card.is-selected { border-color: #1765d1; }
```

card는 공통 표현, is-selected는 상태입니다. 변하는 border-color만 추가해 다른 폭·스타일을 불필요하게 재정의하지 않습니다. 클래스 이름을 새로 썼다고 HTML에 그 클래스가 자동 생기지는 않습니다. HTML·CSS·상태 변경 코드를 함께 맞춥니다.

| 검수 | 먼저 물을 질문 |
| --- | --- |
| 적용 | 파일이 로드되고 선택자가 맞는가? |
| 값 | 속성 충돌·상속·축약 초기화가 있는가? |
| 크기 | 단위 기준·box-sizing·최소 크기가 맞는가? |
| 배치 | 정상 흐름·기준 박스·축이 맞는가? |
| 사용성 | hover 외에 focus·터치·숨김 상태도 확인했는가? |

“전체에 overflow:hidden 추가”나 “z-index:99999 추가”로 문제를 숨기면 다른 오류를 만들 수 있습니다. 원인→수정→영향 범위→회귀 확인을 기록합니다.

**확인:** 기존 클래스의 사용 곳을 찾고 하나의 컴포넌트부터 바꿉니다. 계산값이 바뀌었는지와 화면·키보드 동작을 같이 검토합니다. 포맷터 성공을 기능 검증 성공으로 기록하지 않습니다.

### 내 추가 실습에서 발견한 선언 오타

내 `workspace_html/css/실습_개인/asset/css/연습_01.css`의 발췌입니다. 강사님 동일 파일과의 비교라고 꾸미지 않습니다.

```css
div.msg {
    background-color: #ffffff;
    font-size: 15px;
    border: 1px sold #ffffff;
    padding: 5px;
    border-radius: 10px;
}
```

`sold`는 유효한 border-style 값이 아니므로 이 border 선언이 무시됩니다. 규칙 전체가 사라져 배경·크기·padding까지 전부 무효가 되는 것은 아닙니다. `solid`로 고치면 1px 테두리 선언이 유효해집니다. 같은 흰 배경과 흰 테두리이면 눈으로 구분하기 어려울 수도 있으므로 Styles·Computed에서 선언 유효성도 확인합니다. 다른 규칙에 유효한 border가 있으면 그 값이 남을 수 있습니다. 오타 확인을 위해 원본 소스 파일 자체를 수정하지는 않았습니다.


### 개발자 도구에서 실제 값을 읽기

이 문서에서 제안한 개선 카드 예제을 브라우저에서 열고 Console에 다음을 입력합니다. 💡 JavaScript를 이용한 CSS 진단 명령이며 CSS 파일에 쓰는 코드가 아닙니다.

```javascript
getComputedStyle(document.querySelector('.card')).borderTopColor
```

**예상 결과:** 기본 fallback 적용 시 rgb(221, 221, 221)

HTML에 class card를 넣고 제시한 CSS를 연결한 경우입니다. 선택자가 null이면 먼저 요소 존재를 확인합니다. 요소가 없다는 오류가 나오면 페이지와 선택 대상을 먼저 확인합니다. getComputedStyle은 API에서 계산·해석된 스타일을 읽고 getBoundingClientRect는 변환이 반영된 표시 경계 상자를 읽습니다. margin까지 포함한 전체 점유를 자동 반환하는 값은 아닙니다. CSS에는 Python의 print가 없으므로 화면 결과와 Console 값 확인을 구분합니다.

### 짧은 점검 문제와 해설

**문제:** 포맷터 통과가 CSS 동작 검증인가?

**해설:** 아닙니다. 선택자·계산값·배치·상호작용 검토가 별도로 필요합니다.

먼저 답을 가리고 이유를 말한 뒤 본문의 단계별 예제와 종합실습으로 확인합니다.

<a id="css-7"></a>

## 1. Class 이름은 역할을 표현한다

### 1-1. Before

```css
.red-box {
    padding: 20px;
    background: red;
}
```

색상이 바뀌면 이름과 실제 모습이 달라진다.

### 1-2. After

```css
.alert {
    padding: 1.25rem;
}

.alert--danger {
    background: var(--color-danger-surface);
}
```

### 1-3. 개선 이유

```text
.red-box
→ 현재 모양 표현

.alert
→ Component 역할 표현

.alert--danger
→ 상태·변형 표현
```

---

<a id="css-8"></a>

## 2. ID보다 Class를 기본으로 사용한다

### 2-1. Before

```css
#login-button {
    background: blue;
}
```

### 2-2. After

```css
.login-form__submit {
    background: var(--color-primary);
}
```

ID는 Page Anchor·JavaScript 연결 등 명확한 목적이 있을 때 사용하고, Style은 재사용 가능한 Class를 기본으로 한다.

---

<a id="css-9"></a>

## 3. Tag Selector에 Component Style을 직접 묶지 않는다

### 3-1. Before

```css
button {
    width: 100%;
    border-radius: 20px;
}
```

Page의 모든 Button에 영향을 준다.

### 3-2. After

```css
.button {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    border-radius: var(--radius-medium);
}

.login-form__submit {
    width: 100%;
}
```

Base Component와 특정 Layout 요구사항을 분리한다.

---

<a id="css-10"></a>

## 4. 긴 후손 Selector를 피한다

### 4-1. Before

```css
main section div ul li a {
    color: black;
}
```

HTML 구조가 한 단계만 바뀌어도 적용되지 않을 수 있다.

### 4-2. After

```css
.category-link {
    color: var(--color-text);
}
```

---

<a id="css-11"></a>

## 5. Selector 깊이를 낮게 유지한다

권장 예:

```css
.product-card {}
.product-card__title {}
.product-card--featured {}
```

주의할 예:

```css
.page .content .product-list .product-card .title span {}
```

실무에서는 대체로 1~2단계 Class Selector로 충분한지 먼저 검토한다.

---

<a id="css-12"></a>

## 6. BEM은 목적에 맞게 사용한다

```text
Block
→ product-card

Element
→ product-card__title

Modifier
→ product-card--featured
```

```css
.product-card {}
.product-card__image {}
.product-card__title {}
.product-card--featured {}
```

BEM 이름을 무조건 길게 만드는 것이 목적은 아니다. Component 경계와 상태가 명확해야 한다.

---

<a id="css-13"></a>

## 7. Utility Class는 한 가지 책임만 가진다

```css
.u-hidden {
    display: none !important;
}

.u-text-center {
    text-align: center;
}

.u-visually-hidden {
    position: absolute;
    inline-size: 1px;
    block-size: 1px;
    overflow: hidden;
    clip-path: inset(50%);
    white-space: nowrap;
}
```

Utility는 작은 예외 처리에 유용하지만 모든 Style을 Utility 조합으로만 구성할지는 팀 규칙에 따라 결정한다.

---

<a id="css-14"></a>

## 8. 상태는 `is-`, `has-` 형태로 표현할 수 있다

```css
.menu.is-open {
    display: block;
}

.form-field.has-error {
    border-color: var(--color-danger);
}

.button.is-loading {
    cursor: wait;
}
```

JavaScript는 상태 Class를 변경한다.

```javascript
menu.classList.toggle(
    "is-open",
    isOpen,
)
```

---

<a id="css-15"></a>

## 9. Attribute 상태도 활용한다

```css
.accordion-button[
    aria-expanded="true"
] {
    background: var(--color-primary-soft);
}
```

접근성 상태와 시각 상태를 같은 Attribute로 연결할 수 있다.

---

<a id="css-16"></a>

## 10. Cascade를 먼저 이해하고 덮어쓴다

Cascade 판단 요소:

```text
Origin과 Importance
→ Layer
→ 명시도
→ 선언 순서
```

같은 명시도라면 뒤에 작성된 선언이 적용된다.

```css
.button {
    color: black;
}

.button {
    color: blue;
}
```

최종 색상:

```text
blue
```

---

<a id="css-17"></a>

## 11. 명시도를 높여서 문제를 해결하지 않는다

### 11-1. Before

```css
.page .header .nav .nav-link {
    color: black;
}

.page .header .nav .nav-link.active {
    color: blue !important;
}
```

### 11-2. After

```css
.nav-link {
    color: var(--color-text);
}

.nav-link.is-active {
    color: var(--color-primary);
}
```

---

<a id="css-18"></a>

## 12. `!important`는 예외적으로 사용한다

적절할 수 있는 사례:

```text
접근성 Utility
외부 Library를 제어할 수 없는 경우
사용자 Theme Override
명확한 Utility 규칙
```

일반 Component 충돌을 해결하기 위해 반복 사용하지 않는다.

---

<a id="css-19"></a>

## 13. `:where()`로 명시도를 낮출 수 있다

```css
:where(
    .card,
    .panel,
    .dialog
) {
    box-sizing: border-box;
}
```

`:where()` 내부 Selector의 명시도는 0이다.

---

<a id="css-20"></a>

## 14. `:is()`는 반복 Selector를 줄인다

```css
:is(
    .card,
    .panel
) :is(
    h2,
    h3
) {
    margin-block-start: 0;
}
```

`:is()`는 내부에서 가장 높은 명시도의 영향을 받는다.

---

<a id="css-21"></a>

## 15. Cascade Layer로 역할 순서를 관리한다

```css
@layer reset, base, components, utilities;
```

```css
@layer reset {
    *,
    *::before,
    *::after {
        box-sizing: border-box;
    }
}

@layer components {
    .button {
        border-radius: 0.5rem;
    }
}

@layer utilities {
    .u-hidden {
        display: none !important;
    }
}
```

파일 순서만으로 모든 우선순위를 관리하는 부담을 줄일 수 있다.

---

<a id="css-22"></a>

## 16. 전역 Reset은 의도적으로 작성한다

```css
*,
*::before,
*::after {
    box-sizing: border-box;
}

html {
    color-scheme: light dark;
}

body {
    margin: 0;
    min-block-size: 100dvh;
}

img,
picture,
video,
canvas,
svg {
    display: block;
    max-inline-size: 100%;
}
```

모든 기본 Style을 무조건 제거하지 않는다. Form Control과 Focus Outline을 지울 때는 대체 Style이 필요하다.

---

<a id="css-23"></a>

## 17. `border-box`를 전역으로 통일한다

```css
*,
*::before,
*::after {
    box-sizing: border-box;
}
```

```text
width
→ Content + Padding + Border 포함
```

Component 크기 계산을 예측하기 쉬워진다.

---

<a id="css-24"></a>

## 18. 물리 방향보다 논리 속성을 고려한다

### 18-1. Before

```css
.card {
    margin-left: auto;
    padding-right: 1rem;
}
```

### 18-2. After

```css
.card {
    margin-inline-start: auto;
    padding-inline-end: 1rem;
}
```

글쓰기 방향과 국제화 대응에 유리하다.

---

<a id="css-25"></a>

## 19. 간격은 Scale로 관리한다

```css
:root {
    --space-1: 0.25rem;
    --space-2: 0.5rem;
    --space-3: 0.75rem;
    --space-4: 1rem;
    --space-6: 1.5rem;
    --space-8: 2rem;
}
```

### 19-1. Before

```css
.card {
    padding: 17px;
    margin-bottom: 23px;
}
```

### 19-2. After

```css
.card {
    padding: var(--space-4);
    margin-block-end: var(--space-6);
}
```

---

<a id="css-26"></a>

## 20. 자식 Margin보다 부모 `gap`을 우선 검토한다

### 20-1. Before

```css
.menu-item {
    margin-right: 16px;
}

.menu-item:last-child {
    margin-right: 0;
}
```

### 20-2. After

```css
.menu {
    display: flex;
    gap: var(--space-4);
}
```

간격 책임이 부모 Layout에 모인다.

---

<a id="css-27"></a>

## 21. 색상은 역할 기반 Token으로 관리한다

```css
:root {
    --color-text: #1f2937;
    --color-text-muted: #6b7280;
    --color-surface: #ffffff;
    --color-border: #d1d5db;
    --color-primary: #2563eb;
    --color-danger: #dc2626;
}
```

좋지 않은 이름:

```css
--blue: #2563eb;
--gray1: #f3f4f6;
```

권장 이름:

```css
--color-primary: #2563eb;
--color-surface-muted: #f3f4f6;
```

---

<a id="css-28"></a>

## 22. Component Token으로 의미를 좁힌다

```css
.product-card {
    --card-padding: var(--space-4);
    --card-radius: var(--radius-large);
    --card-background: var(--color-surface);

    padding: var(--card-padding);
    border-radius: var(--card-radius);
    background: var(--card-background);
}
```

Modifier에서 Token만 변경할 수 있다.

```css
.product-card--featured {
    --card-background:
        var(--color-primary-soft);
}
```

---

<a id="css-29"></a>

## 23. Fallback 값을 제공한다

```css
.button {
    color: var(
        --button-color,
        var(--color-text)
    );
}
```

Custom Property가 없을 때 사용할 값을 지정한다.

---

<a id="css-30"></a>

## 24. `rem`을 기본 크기 단위로 활용한다

```css
.card {
    padding: 1rem;
    border-radius: 0.75rem;
}

.card__title {
    font-size: 1.25rem;
}
```

사용자 글꼴 크기 설정과 함께 확장된다.

고정 Border와 정밀한 Hairline에는 `px`가 적합할 수 있다.

---

<a id="css-31"></a>

## 25. 유연한 크기는 `clamp()`로 설계한다

```css
.hero-title {
    font-size: clamp(
        2rem,
        5vw,
        4.5rem
    );
}
```

```text
최소 크기
→ 2rem

유동 범위
→ 5vw

최대 크기
→ 4.5rem
```

---

<a id="css-32"></a>

## 26. Container 너비는 `min()`과 `max-width`를 활용한다

```css
.container {
    width: min(
        100% - 2rem,
        75rem
    );

    margin-inline: auto;
}
```

고정 Width보다 작은 화면에서 안전하다.

---

<a id="css-33"></a>

## 27. `100vw`보다 `100%`가 적합한 경우가 많다

### 27-1. Before

```css
.section {
    width: 100vw;
}
```

Scrollbar 너비까지 포함해 가로 Overflow가 생길 수 있다.

### 27-2. After

```css
.section {
    width: 100%;
}
```

Viewport 전체를 의도한 특수한 상황에서만 `vw`를 사용한다.

---

<a id="css-34"></a>

## 28. 높이는 콘텐츠를 우선한다

### 28-1. Before

```css
.card {
    height: 300px;
}
```

Text가 늘면 Overflow가 발생할 수 있다.

### 28-2. After

```css
.card {
    min-height: 18.75rem;
}
```

정확한 고정 높이가 요구사항인지 확인한다.

---

<a id="css-35"></a>

## 29. Full Viewport에는 동적 단위를 검토한다

```css
.hero {
    min-height: 100dvh;
}
```

모바일 Browser UI 변화까지 고려할 수 있다.

Fallback이 필요하면 다음 순서로 작성할 수 있다.

```css
.hero {
    min-height: 100vh;
    min-height: 100dvh;
}
```

---

<a id="css-36"></a>

## 30. Layout은 Flexbox와 Grid를 우선한다

```text
한 축 중심
→ Flexbox

행·열 두 축
→ Grid

겹침·배지·모달
→ Position

기사 이미지 주변 Text
→ Float
```

Position과 Float를 일반 Page Layout에 남용하지 않는다.

---

<a id="css-37"></a>

## 31. Flexbox는 주축과 교차축을 기준으로 작성한다

```css
.toolbar {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: var(--space-3);
}
```

`justify-content`를 무조건 가로 정렬, `align-items`를 무조건 세로 정렬이라고 외우지 않는다.

---

<a id="css-38"></a>

## 32. Flex Item에는 `min-width: 0`이 필요할 수 있다

```css
.media__content {
    min-width: 0;
}
```

긴 Text가 Flex Container를 밀어내는 문제를 줄인다.

---

<a id="css-39"></a>

## 33. Grid는 반복 Column을 간결하게 만든다

```css
.product-grid {
    display: grid;
    grid-template-columns:
        repeat(
            auto-fit,
            minmax(
                min(100%, 16rem),
                1fr
            )
        );

    gap: var(--space-6);
}
```

Media Query를 과도하게 늘리지 않고 Card 수를 조정할 수 있다.

---

<a id="css-40"></a>

## 34. Position은 기준 요소를 명확히 만든다

```css
.product-card {
    position: relative;
}

.product-card__badge {
    position: absolute;
    inset-block-start: var(--space-3);
    inset-inline-end: var(--space-3);
}
```

Absolute 요소의 기준 부모에 `position: relative`를 명확히 작성한다.

---

<a id="css-41"></a>

## 35. `z-index` 숫자를 무작정 높이지 않는다

```css
:root {
    --z-base: 0;
    --z-dropdown: 100;
    --z-sticky: 200;
    --z-overlay: 900;
    --z-modal: 1000;
}
```

Stacking Context 내부에서 비교된다는 점을 함께 이해한다.

---

<a id="css-42"></a>

## 36. Float는 기사 Text 흐름에 제한적으로 사용한다

```css
.article-image {
    float: inline-start;
    inline-size: 12rem;
    margin-inline-end: var(--space-4);
    margin-block-end: var(--space-2);
}
```

Header와 Card Layout에는 Flexbox·Grid를 우선한다.

---

<a id="css-43"></a>

## 37. 숨김 방식은 목적에 맞게 선택한다

| 목적 | 방식 |
| --- | --- |
| Layout에서도 제거 | `display: none` 또는 `hidden` |
| 공간 유지 | `visibility: hidden` |
| Fade 전환 | `opacity` + `visibility` + Pointer 제어 |
| Screen Reader만 제공 | Visually Hidden |
| 단순 Crop | `overflow: hidden` 또는 `clip` |

---

<a id="css-44"></a>

## 38. `opacity: 0`만으로 숨기지 않는다

### 38-1. Before

```css
.menu {
    opacity: 0;
}
```

보이지 않아도 Pointer·Focus 대상이 될 수 있다.

### 38-2. After

```css
.menu {
    visibility: hidden;
    opacity: 0;
    pointer-events: none;
}

.menu.is-open {
    visibility: visible;
    opacity: 1;
    pointer-events: auto;
}
```

---

<a id="css-45"></a>

## 39. Overflow는 문제를 숨기는 용도로 사용하지 않는다

### 39-1. Before

```css
body {
    overflow-x: hidden;
}
```

가로 Overflow 원인을 가릴 수 있다.

### 39-2. After

다음 원인을 먼저 찾는다.

```text
100vw
고정 Width
긴 URL
음수 Margin
Absolute 요소
Transform
Grid 최소 크기
```

필요한 Component에만 Overflow를 적용한다.

---

<a id="css-46"></a>

## 40. 긴 문자열을 안전하게 처리한다

```css
.code,
.url,
.message {
    overflow-wrap: anywhere;
}
```

한 줄 말줄임표:

```css
.title {
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
}
```

---

<a id="css-47"></a>

## 41. Typography는 공통 Scale로 관리한다

```css
:root {
    --font-size-small: 0.875rem;
    --font-size-base: 1rem;
    --font-size-large: 1.25rem;
    --font-size-heading: clamp(
        1.75rem,
        3vw,
        3rem
    );
}
```

---

<a id="css-48"></a>

## 42. 본문 줄높이는 단위 없이 작성한다

```css
body {
    line-height: 1.6;
}
```

자식 글꼴 크기에 비례해 상속된다.

---

<a id="css-49"></a>

## 43. Web Font는 Fallback과 성능을 함께 고려한다

```css
@font-face {
    font-family: "Project Sans";
    src:
        url("./fonts/project-sans.woff2")
        format("woff2");
    font-display: swap;
}
```

```css
body {
    font-family:
        "Project Sans",
        system-ui,
        sans-serif;
}
```

---

<a id="css-50"></a>

## 44. 링크는 Hover만으로 상태를 표현하지 않는다

```css
.link:hover,
.link:focus-visible {
    color: var(--color-primary);
    text-decoration-thickness: 0.125em;
}
```

Keyboard 사용자에게도 같은 상태를 제공한다.

---

<a id="css-51"></a>

## 45. Focus Outline을 제거하지 않는다

### 45-1. Before

```css
button:focus {
    outline: none;
}
```

### 45-2. After

```css
.button:focus-visible {
    outline: 0.1875rem solid
        var(--color-focus);
    outline-offset: 0.1875rem;
}
```

---

<a id="css-52"></a>

## 46. Disabled 상태는 색상만으로 표현하지 않는다

```css
.button:disabled {
    cursor: not-allowed;
    opacity: 0.55;
}
```

HTML `disabled` Attribute와 함께 사용한다.

---

<a id="css-53"></a>

## 47. 상태 표현은 JavaScript Inline Style보다 Class를 사용한다

### 47-1. Before

```javascript
button.style.backgroundColor = "red"
button.style.display = "none"
```

### 47-2. After

```javascript
button.classList.add(
    "is-error",
)

button.hidden = true
```

CSS:

```css
.button.is-error {
    background:
        var(--color-danger);
}
```

---

<a id="css-54"></a>

## 48. Inline Style은 동적 수치에 제한적으로 사용한다

Progress처럼 값이 계속 달라지는 경우:

```javascript
progress.style.setProperty(
    "--progress",
    `${percent}%`,
)
```

```css
.progress__bar {
    inline-size: var(--progress);
}
```

시각 규칙은 CSS에 유지한다.

---

<a id="css-55"></a>

## 49. Background Image는 장식에 사용한다

```css
.hero {
    background:
        linear-gradient(
            rgb(0 0 0 / 0.45),
            rgb(0 0 0 / 0.45)
        ),
        url("./images/hero.webp")
        center / cover
        no-repeat;
}
```

콘텐츠 의미가 있는 이미지는 `<img>`와 적절한 `alt`를 사용한다.

---

<a id="css-56"></a>

## 50. Background 위 Text 대비를 확인한다

```css
.hero {
    color: white;
}
```

이미지에 따라 대비가 달라질 수 있으므로 Overlay·Text Shadow·배경색 Fallback을 함께 검토한다.

---

<a id="css-57"></a>

## 51. Shadow는 깊이와 상태를 제한적으로 표현한다

```css
:root {
    --shadow-small:
        0 0.125rem 0.375rem
        rgb(0 0 0 / 0.12);

    --shadow-medium:
        0 0.75rem 1.5rem
        rgb(0 0 0 / 0.16);
}
```

```css
.card {
    box-shadow: var(--shadow-small);
}
```

과도한 Blur·다중 Shadow는 시각적 복잡도와 Paint 비용을 높인다.

---

<a id="css-58"></a>

## 52. Transition은 변경 속성을 명시한다

### 52-1. Before

```css
.card {
    transition: all 0.3s;
}
```

### 52-2. After

```css
.card {
    transition:
        transform 0.3s ease,
        box-shadow 0.3s ease;
}
```

---

<a id="css-59"></a>

## 53. Transition은 기본 상태에 작성한다

```css
.button {
    transition:
        background-color 0.2s,
        transform 0.2s;
}

.button:hover {
    transform: translateY(-0.125rem);
}
```

Hover 상태에만 작성하면 해제 시 전환이 다르게 동작할 수 있다.

---

<a id="css-60"></a>

## 54. 움직임에는 Transform과 Opacity를 우선 검토한다

### 54-1. Before

```css
.card:hover {
    top: -4px;
}
```

### 54-2. After

```css
.card:hover {
    transform:
        translateY(-0.25rem);
}
```

Layout 재계산을 줄이고 원래 공간을 유지한다.

---

<a id="css-61"></a>

## 55. `prefers-reduced-motion`을 제공한다

```css
@media (
    prefers-reduced-motion:
    reduce
) {
    *,
    *::before,
    *::after {
        scroll-behavior: auto;
        animation-duration:
            0.01ms !important;
        animation-iteration-count:
            1 !important;
        transition-duration:
            0.01ms !important;
    }
}
```

팀 정책에 맞게 범위를 조정한다.

---

<a id="css-62"></a>

## 56. Mobile First로 기본 Style을 작성한다

```css
.product-grid {
    display: grid;
    grid-template-columns: 1fr;
    gap: var(--space-4);
}

@media (
    min-width: 48rem
) {
    .product-grid {
        grid-template-columns:
            repeat(2, 1fr);
    }
}
```

작은 화면 기본값에서 필요한 기능을 확장한다.

---

<a id="css-63"></a>

## 57. Breakpoint는 Device 이름보다 Layout 기준으로 정한다

좋지 않은 기준:

```text
iPhone
Tablet
Desktop
```

권장 기준:

```text
Navigation이 겹치는 지점
Card 최소 너비가 깨지는 지점
Text 줄 길이가 과도해지는 지점
```

---

<a id="css-64"></a>

## 58. Hover 가능 여부를 조건으로 사용할 수 있다

```css
@media (
    hover: hover
) and (
    pointer: fine
) {
    .card:hover {
        transform:
            translateY(-0.25rem);
    }
}
```

Touch 장치에 Hover 효과를 전제로 하지 않는다.

---

<a id="css-65"></a>

## 59. Container Query로 Component를 독립시킨다

```css
.card-list {
    container-type: inline-size;
}
```

```css
@container (
    min-width: 40rem
) {
    .product-card {
        grid-template-columns:
            10rem 1fr;
    }
}
```

Page Viewport가 아니라 Component가 놓인 공간을 기준으로 반응한다.

---

<a id="css-66"></a>

## 60. Dark Mode는 Token을 교체한다

```css
:root {
    --color-text: #1f2937;
    --color-surface: #ffffff;
}

@media (
    prefers-color-scheme:
    dark
) {
    :root {
        --color-text: #f3f4f6;
        --color-surface: #111827;
    }
}
```

Component마다 색상을 다시 작성하지 않는다.

---

<a id="css-67"></a>

## 61. CSS 파일은 역할별로 분리한다

```text
styles/
├── reset.css
├── tokens.css
├── base.css
├── layout.css
├── components/
│   ├── button.css
│   ├── card.css
│   └── modal.css
├── utilities.css
└── main.css
```

작은 프로젝트에서는 과도한 분리를 피한다.

---

<a id="css-68"></a>

## 62. Import 순서를 고정한다

```css
@import url("./reset.css");
@import url("./tokens.css");
@import url("./base.css");
@import url("./layout.css");
@import url("./components/button.css");
@import url("./utilities.css");
```

실제 운영 환경에서는 Bundler와 Build 전략에 따라 파일 결합 방식을 선택한다.

---

<a id="css-69"></a>

## 63. Component와 Page Layout을 분리한다

```css
.card {
    border-radius: var(--radius-medium);
}
```

```css
.dashboard__card {
    grid-column: span 2;
}
```

Card 자체 Style과 Dashboard 안에서의 배치 책임을 분리한다.

---

<a id="css-70"></a>

## 64. 주석은 이유와 제약을 설명한다

좋지 않은 주석:

```css
/* 배경을 파란색으로 설정 */
.button {
    background: blue;
}
```

좋은 주석:

```css
/* 이미지 위에서도 Text 대비를 유지하기 위해
   반투명 Overlay를 함께 사용한다. */
.hero {
    background:
        linear-gradient(
            rgb(0 0 0 / 0.45),
            rgb(0 0 0 / 0.45)
        ),
        url("./hero.webp")
        center / cover
        no-repeat;
}
```

---

<a id="css-71"></a>

## 65. Browser 기본 Style을 이해하고 덮어쓴다

```css
button,
input,
select,
textarea {
    font: inherit;
}
```

Form Control의 모든 기본 Style을 제거하면 Focus·Disabled·Platform 동작을 다시 구현해야 한다.

---

<a id="css-72"></a>

## 66. CSS Validation과 Lint를 자동화한다

대표 도구:

```text
Formatter
→ Prettier

Lint
→ Stylelint

Browser 검사
→ DevTools, Lighthouse

접근성
→ axe, WAVE 등
```

팀 규칙을 Repository에 저장한다.

---

<a id="css-73"></a>

## 67. 실제 개선 사례 1: 구조 의존 Selector

### 67-1. Before

```css
div#header ul li a {
    color: blue;
}
```

### 67-2. After

```css
.nav-link {
    color: var(--color-primary);
}
```

---

<a id="css-74"></a>

## 68. 실제 개선 사례 2: `rem` 기준 오해

잘못된 설명:

```text
rem은 body 기준
```

정확한 기준:

```text
rem
→ Root html의 font-size 기준
```

```css
html {
    font-size: 100%;
}
```

---

<a id="css-75"></a>

## 69. 실제 개선 사례 3: 부모 배경색 상속 오해

```text
자식 배경색이 부모로부터 상속됨
```

이 아니라:

```text
자식의 기본 배경이 transparent
→ 뒤의 부모 배경이 보임
```

`background-color`는 기본적으로 상속되지 않는다.

---

<a id="css-76"></a>

## 70. 실제 개선 사례 4: Margin Collapse 만능 해결

### 70-1. Before

```css
.parent {
    overflow: hidden;
}
```

콘텐츠가 잘릴 수 있다.

### 70-2. After

목적에 따라 선택한다.

```css
.parent {
    display: flow-root;
}
```

또는:

```css
.parent {
    padding-block-start:
        0.0625rem;
}
```

Flex·Grid Layout에서는 `gap`을 활용할 수 있다.

---

<a id="css-77"></a>

## 71. 실제 개선 사례 5: 잘못된 HTML 중첩

```html
<span>
    <div>내용</div>
</span>
```

Browser가 DOM을 자동 보정할 수 있다.

개선:

```html
<div>
    <span>내용</span>
</div>
```

CSS 문제처럼 보여도 HTML 구조를 먼저 검수한다.

---

<a id="css-78"></a>

## 72. 실제 개선 사례 6: 숨김 방식 혼동

```css
.item {
    opacity: 0;
}
```

보이지 않아도 상호작용할 수 있다.

개선:

```css
.item {
    visibility: hidden;
    opacity: 0;
    pointer-events: none;
}
```

---

<a id="css-79"></a>

## 73. 실제 개선 사례 7: Background와 콘텐츠 이미지 혼동

상품 사진처럼 의미가 있는 이미지:

```html
<img
    src="./product.webp"
    alt="기계식 키보드"
>
```

장식용 Hero 이미지:

```css
.hero {
    background-image:
        url("./hero.webp");
}
```

---

<a id="css-80"></a>

## 74. 실제 개선 사례 8: Absolute Position 중앙 정렬

### 74-1. Before

```css
.modal {
    top: 200px;
    left: 300px;
}
```

### 74-2. After

```css
.modal {
    position: fixed;
    inset: 50% auto auto 50%;
    transform:
        translate(-50%, -50%);
}
```

또는 Overlay에 Grid를 사용할 수 있다.

```css
.modal-overlay {
    display: grid;
    place-items: center;
}
```

---

<a id="css-81"></a>

## 75. 실제 개선 사례 9: Float Layout

### 75-1. Before

```css
.header-left {
    float: left;
}

.header-right {
    float: right;
}
```

### 75-2. After

```css
.header {
    display: flex;
    align-items: center;
    justify-content:
        space-between;
}
```

Float는 기사 Text 흐름에 남겨 둔다.

---

<a id="css-82"></a>

## 76. 실제 개선 사례 10: Hover 전용 Transition

### 76-1. Before

```css
.button:hover {
    transition:
        background-color 0.3s;
}
```

### 76-2. After

```css
.button {
    transition:
        background-color 0.3s;
}
```

---

<a id="css-83"></a>

## 77. 실제 개선 사례 11: `transition: all`

### 77-1. Before

```css
.card {
    transition: all 0.5s;
}
```

### 77-2. After

```css
.card {
    transition:
        transform 0.5s,
        box-shadow 0.5s;
}
```

---

<a id="css-84"></a>

## 78. 실제 개선 사례 12: Transform 함수 덮어쓰기

### 78-1. Before

```css
.box {
    transform:
        translateX(50px);
    transform:
        rotate(10deg);
}
```

첫 Transform은 덮어써진다.

### 78-2. After

```css
.box {
    transform:
        translateX(50px)
        rotate(10deg);
}
```

---

<a id="css-85"></a>

## 79. 실제 개선 사례 13: Hover 메뉴 접근성

### 79-1. Before

```css
.menu-label:hover + .menu-list {
    display: block;
}
```

Touch·Keyboard 환경에서 동작이 불안정하다.

### 79-2. After

```css
.menu-list {
    display: none;
}

.menu-button[
    aria-expanded="true"
] + .menu-list {
    display: block;
}
```

---

<a id="css-86"></a>

## 80. 실제 개선 사례 14: Flex 시각 순서

```css
.item {
    order: -1;
}
```

DOM 순서와 Keyboard 순서는 바뀌지 않는다.

중요한 콘텐츠 순서는 HTML에서 먼저 수정한다.

---

<a id="css-87"></a>

## 81. 실무형 예제: 반응형 Product Card

```css
:root {
    --color-text: #1f2937;
    --color-text-muted: #6b7280;
    --color-surface: #ffffff;
    --color-border: #d1d5db;
    --color-primary: #2563eb;
    --color-primary-hover: #1d4ed8;
    --color-focus: #93c5fd;

    --space-2: 0.5rem;
    --space-3: 0.75rem;
    --space-4: 1rem;
    --space-6: 1.5rem;

    --radius-small: 0.5rem;
    --radius-medium: 0.75rem;
    --radius-round: 999rem;

    --shadow-card:
        0 0.5rem 1.25rem
        rgb(15 23 42 / 0.12);
}

*,
*::before,
*::after {
    box-sizing: border-box;
}

.product-card {
    position: relative;
    display: grid;
    gap: var(--space-4);
    overflow: hidden;
    border: 1px solid
        var(--color-border);
    border-radius:
        var(--radius-medium);
    background:
        var(--color-surface);
    color: var(--color-text);
    box-shadow:
        var(--shadow-card);
    transition:
        transform 0.25s ease,
        box-shadow 0.25s ease;
}

.product-card__image {
    inline-size: 100%;
    aspect-ratio: 16 / 9;
    object-fit: cover;
}

.product-card__body {
    display: grid;
    gap: var(--space-3);
    padding:
        0 var(--space-4)
        var(--space-4);
}

.product-card__badge {
    position: absolute;
    inset-block-start:
        var(--space-3);
    inset-inline-end:
        var(--space-3);
    padding:
        var(--space-2)
        var(--space-3);
    border-radius:
        var(--radius-round);
    background:
        var(--color-primary);
    color: white;
    font-size: 0.875rem;
}

.product-card__title {
    margin: 0;
    font-size:
        clamp(
            1.25rem,
            3vw,
            1.75rem
        );
}

.product-card__description {
    margin: 0;
    color:
        var(--color-text-muted);
    line-height: 1.6;
    overflow-wrap: anywhere;
}

.button {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    min-block-size: 2.75rem;
    padding-inline:
        var(--space-4);
    border: 0;
    border-radius:
        var(--radius-small);
    font: inherit;
    cursor: pointer;
}

.button--primary {
    background:
        var(--color-primary);
    color: white;
    transition:
        background-color 0.2s,
        transform 0.2s;
}

.button--primary:hover {
    background:
        var(--color-primary-hover);
}

.button--primary:focus-visible {
    outline: 0.1875rem solid
        var(--color-focus);
    outline-offset: 0.1875rem;
}

@media (
    hover: hover
) and (
    pointer: fine
) {
    .product-card:hover {
        transform:
            translateY(-0.25rem);
    }

    .button--primary:hover {
        transform:
            translateY(-0.125rem);
    }
}

@media (
    min-width: 40rem
) {
    .product-card {
        grid-template-columns:
            minmax(10rem, 14rem)
            1fr;
    }

    .product-card__image {
        block-size: 100%;
        aspect-ratio: auto;
    }

    .product-card__body {
        align-content: center;
        padding:
            var(--space-6);
    }
}

@media (
    prefers-reduced-motion:
    reduce
) {
    .product-card,
    .button--primary {
        transition: none;
    }
}
```

### 81-1. 코드에서 무엇을 사용하는 걸까?

| 코드 | 사용하는 이유 |
| --- | --- |
| 역할 기반 Token | 색상·간격 일관성 |
| `border-box` | 크기 계산 단순화 |
| Grid | Card의 두 축 Layout |
| `aspect-ratio` | 이미지 비율 유지 |
| `object-fit` | 이미지 Crop |
| 논리 속성 | 방향 독립적 배치 |
| `clamp()` | 유연한 제목 크기 |
| Hover Media Query | Hover 가능한 장치만 효과 적용 |
| `focus-visible` | Keyboard Focus 표시 |
| Reduced Motion | 움직임 접근성 |
| Mobile First | 작은 화면 기본 구조 |

---

<a id="css-88"></a>

## 82. 파일 구조 예시

```text
styles/
├── reset.css
├── tokens.css
├── base.css
├── layout.css
├── components/
│   ├── button.css
│   ├── product-card.css
│   ├── navigation.css
│   └── modal.css
├── pages/
│   └── home.css
├── utilities.css
└── main.css
```

---

<a id="css-89"></a>

## 83. 자주 하는 실수

### 83-1. 모든 요소를 ID로 Style

명시도가 높고 재사용하기 어렵다.

### 83-2. HTML 구조를 Selector에 그대로 복사

Markup 변경에 취약하다.

### 83-3. 충돌할 때마다 `!important` 추가

Cascade 문제를 더 크게 만든다.

### 83-4. 임의의 간격값을 계속 추가

Spacing Scale이 무너진다.

### 83-5. Layout에 Position·Float 남용

반응형 변경이 어려워진다.

### 83-6. `opacity: 0`만으로 숨김

상호작용과 Focus가 남을 수 있다.

<a id="index-section-151"></a>

### 83-7. 모든 Transition에 `all`

의도하지 않은 속성까지 전환된다.

### 83-8. Hover 상태만 작성

Keyboard와 Touch 사용자를 놓친다.

### 83-9. Focus Outline을 제거

현재 위치를 알기 어렵다.

### 83-10. 가로 Overflow를 Body에서 숨김

실제 Layout 오류를 발견하지 못한다.

---

<a id="css-90"></a>

## 84. 핵심 요약

```text
Selector
→ 역할 기반 Class
→ 낮은 명시도
→ 짧은 깊이
```

```text
Design Token
→ 색상
→ 간격
→ Radius
→ Shadow
→ Typography
```

```text
Layout
→ Flexbox
→ Grid
→ Position
→ Float의 목적 구분
```

```text
상태
→ Class 또는 Attribute
→ Hover + Focus
→ Disabled + Loading
```

```text
반응형
→ Mobile First
→ Layout이 깨지는 지점
→ Container Query 검토
```

```text
효과
→ 필요한 속성만 Transition
→ Transform·Opacity 우선
→ Reduced Motion 제공
```

---

<a id="css-91"></a>

## 85. 최종 체크리스트

- [ ] Class 이름이 역할을 표현하는가?
- [ ] Style에 ID Selector를 불필요하게 사용하지 않는가?
- [ ] 긴 후손 Selector를 피했는가?
- [ ] Selector 깊이가 낮고 예측 가능한가?
- [ ] Modifier와 상태 Class가 구분되는가?
- [ ] `!important` 없이 Cascade를 관리할 수 있는가?
- [ ] Cascade Layer 또는 파일 순서가 명확한가?
- [ ] `border-box`를 일관되게 적용했는가?
- [ ] 논리 속성을 사용할 수 있는 부분을 검토했는가?
- [ ] 색상과 간격을 Token으로 관리하는가?
- [ ] 임의의 Magic Number를 반복하지 않는가?
- [ ] 자식 Margin보다 부모 `gap`을 우선 검토했는가?
- [ ] 크기에 `rem`, `%`, `clamp()`를 적절히 사용하는가?
- [ ] 고정 Height가 실제 요구사항인지 확인했는가?
- [ ] `100vw`로 불필요한 가로 Overflow를 만들지 않는가?
- [ ] Flexbox·Grid·Position·Float의 목적을 구분하는가?
- [ ] Flex Item의 `min-width: 0` 필요성을 확인했는가?
- [ ] `z-index` Scale과 Stacking Context를 이해하는가?
- [ ] 숨김 방식이 목적과 접근성에 맞는가?
- [ ] 긴 문자열과 Overflow를 처리하는가?
- [ ] 본문 줄높이를 충분히 제공하는가?
- [ ] Web Font에 Fallback과 `font-display`를 제공하는가?
- [ ] Hover뿐 아니라 `focus-visible`을 제공하는가?
- [ ] Focus Outline을 제거하지 않는가?
- [ ] Disabled 상태가 HTML Attribute와 연결되는가?
- [ ] JavaScript Inline Style보다 상태 Class를 사용하는가?
- [ ] 콘텐츠 이미지와 장식용 Background를 구분하는가?
- [ ] Background 위 Text 대비를 확인했는가?
- [ ] Shadow와 Transition을 필요한 곳에만 사용하는가?
- [ ] `transition: all`을 피하는가?
- [ ] Transform 함수가 덮어쓰이지 않는가?
- [ ] Reduced Motion 환경을 고려하는가?
- [ ] Mobile First 방식으로 작성했는가?
- [ ] Breakpoint가 Device 이름이 아닌 Layout 기준인가?
- [ ] Hover 가능 여부를 Media Query로 확인하는가?
- [ ] Container Query 적용 가능성을 검토했는가?
- [ ] Dark Mode를 Token 교체 방식으로 관리하는가?
- [ ] Component와 Page Layout 책임이 분리되어 있는가?
- [ ] Stylelint·Formatter·DevTools로 검수하는가?

---

<a id="css-92"></a>

## 마무리

CSS 실무 코딩 스타일의 핵심은 화려한 효과를 많이 사용하는 것에서 끝나지 않는다.

```text
Selector에서 역할과 범위가 보이고
    ↓
색상·간격·크기가 일관된 Token으로 관리되고
    ↓
Layout 도구가 목적에 맞게 선택되고
    ↓
상태·반응형·접근성이 함께 설계되고
    ↓
수정하거나 삭제할 때 영향 범위를 예측할 수 있는 것
```

좋은 CSS는 단순히 화면을 꾸미는 코드가 아니다.

**HTML의 의미를 해치지 않고, 다양한 화면과 입력 환경에서 안정적으로 동작하며, 다른 개발자가 안전하게 확장할 수 있는 UI 규칙**이다.
<a id="css-93"></a>

## 렌더링 복습 카드 — 의도·범위·재사용성이 보이는 규칙

실무 CSS는 선택자 범위를 예측 가능하게 하고, 반복 값을 변수·공통 클래스로 관리하며, 상태와 반응형 규칙을 가까운 책임 단위로 묶는다. 무작정 `!important`를 늘리면 원인 추적이 어려워진다.

01~15번 내 코드와 강사님 코드를 Styles의 승리 선언, Computed 값, Box Model 결과로 비교한다. 이름은 모양보다 역할과 컴포넌트 관계를 드러낸다.

**원본 연결:** 내 코드와 강사님 코드의 `workspace_html/css/01~15 전체 원본`에서 실제 선택자·계산값·화면 차이를 확인한다.


[CSS 파트 목차로 돌아가기](./README.md)
