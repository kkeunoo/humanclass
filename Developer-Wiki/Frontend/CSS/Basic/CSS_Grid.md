---
title: CSS Grid
version: v1.0
last_updated: 2026-07-22
status: Completed
---

# CSS Grid

## 문서 정보

| 항목 | 내용 |
|------|------|
| 문서명 | CSS Grid |
| 분류 | Frontend / CSS / Basic |
| 난이도 | Intermediate |
| 선수 지식 | CSS Display, Position, Flexbox |
| 핵심 주제 | Grid Container, Grid Item, 2차원 레이아웃 |
| 버전 | v1.0 |
| 최종 수정일 | 2026-07-22 |

---

# 개요

CSS Grid Layout(Grid)은 **2차원(Two-Dimensional) 레이아웃**을 만들기 위한 CSS 레이아웃 시스템이다.

Flexbox가 **한 방향(Row 또는 Column)** 의 배치에 최적화되어 있다면, Grid는 **행(Row)과 열(Column)을 동시에 제어**할 수 있도록 설계되었다.

복잡한 화면을 구성해야 하는 관리자 페이지(Admin Dashboard), 갤러리, 카드 목록, 메인 레이아웃 등에서는 Grid가 매우 강력한 기능을 제공한다.

대표적인 활용 사례는 다음과 같다.

- Dashboard
- 관리자(Admin) 페이지
- 갤러리
- 메인 페이지 레이아웃
- 뉴스 사이트
- 쇼핑몰 상품 목록
- 카드 UI
- 포트폴리오 목록

---

# Grid가 필요한 이유

Flexbox만으로도 대부분의 UI를 만들 수 있지만, 행과 열을 동시에 제어해야 하는 경우에는 코드가 복잡해진다.

예를 들어 다음과 같은 레이아웃을 생각해 보자.

```text
┌──────────────────────────────┐
│ Header                       │
├────────────┬─────────────────┤
│ Sidebar    │ Main            │
│            │                 │
├────────────┴─────────────────┤
│ Footer                       │
└──────────────────────────────┘
```

Flexbox로도 구현은 가능하지만 여러 개의 부모 요소를 중첩해야 한다.

Grid는 이러한 구조를 훨씬 직관적으로 표현할 수 있다.

---

# Flexbox와 Grid 차이

| Flexbox | Grid |
|---------|------|
| 1차원 레이아웃 | 2차원 레이아웃 |
| 한 방향 배치 | 행과 열 동시 제어 |
| 콘텐츠 중심 | 레이아웃 중심 |
| Navigation | Dashboard |
| Toolbar | Admin UI |
| Header | 전체 페이지 |

---

# 핵심 개념

Grid도 Flexbox처럼 부모와 자식의 역할이 구분된다.

```text
Grid Container
│
├── Grid Item
├── Grid Item
├── Grid Item
└── Grid Item
```

| 구성 | 설명 |
|------|------|
| Grid Container | 부모 요소 |
| Grid Item | 직계 자식 요소 |

Grid 관련 속성은 대부분 Container에 작성한다.

---

# display: grid

부모 요소를 Grid Container로 만든다.

```css
.container{

    display:grid;

}
```

```html
<div class="container">

    <div>A</div>

    <div>B</div>

    <div>C</div>

</div>
```

이 순간부터 직계 자식들은 모두 Grid Item이 된다.

---

# Grid의 구성 요소

Grid는 다음 네 가지 요소를 이해해야 한다.

```text
Grid Container
    │
    ├── Grid Line
    ├── Grid Track
    ├── Grid Cell
    └── Grid Area
```

---

## Grid Line

행과 열을 구분하는 기준선이다.

```text
1   2   3   4

│ A │ B │ C │
```

Grid의 위치는 Line 번호를 기준으로 계산된다.

---

## Grid Track

Line과 Line 사이의 공간이다.

```text
│ A │

^^^^^

Track
```

행 Track과 열 Track이 존재한다.

---

## Grid Cell

Grid의 가장 작은 단위이다.

```text
┌───┐
│ A │
└───┘
```

HTML의 `<td>`와 비슷한 개념으로 이해하면 된다.

---

## Grid Area

여러 개의 Cell을 합친 영역이다.

```text
┌──────────┐
│          │
│  Area    │
│          │
└──────────┘
```

Grid Area를 이용하면 큰 영역을 쉽게 구성할 수 있다.

---

# grid-template-columns

열(Column)의 개수와 크기를 지정한다.

```css
.container{

    display:grid;

    grid-template-columns:200px 200px 200px;

}
```

결과

```text
┌────┬────┬────┐
│ A  │ B  │ C  │
└────┴────┴────┘
```

열이 3개 생성된다.

---

# 다양한 Column 지정 방법

## 고정 크기

```css
grid-template-columns:100px 200px 300px;
```

---

## 백분율

```css
grid-template-columns:30% 70%;
```

---

## 혼합 사용

```css
grid-template-columns:250px 1fr;
```

Sidebar와 Main 레이아웃에서 자주 사용하는 방식이다.

---

# grid-template-rows

행(Row)의 크기를 지정한다.

```css
.container{

    grid-template-rows:100px 300px 100px;

}
```

결과

```text
Header

Content

Footer
```

행도 열과 동일한 방식으로 크기를 지정할 수 있다.

---

# fr 단위

Grid에서 가장 많이 사용하는 단위이다.

`fr`은 **남은 공간(Fraction)** 을 비율로 나누는 단위이다.

```css
grid-template-columns:1fr 1fr 1fr;
```

세 개의 열이 동일한 크기로 배치된다.

---

## 비율 지정

```css
grid-template-columns:1fr 2fr 1fr;
```

비율은

```text
1 : 2 : 1
```

이 된다.

즉 가운데 열이 양쪽보다 두 배 넓어진다.

---

# px와 fr 혼합

실무에서 가장 많이 사용하는 패턴이다.

```css
grid-template-columns:250px 1fr;
```

결과

```text
Sidebar │──────────── Main ────────────
```

Sidebar는 250px로 고정되고, Main은 남은 공간을 모두 차지한다.

---

---

# repeat()

같은 크기의 행이나 열을 여러 번 작성해야 할 경우 `repeat()` 함수를 사용하면 코드를 간결하게 작성할 수 있다.

기본 문법

```css
grid-template-columns:repeat(횟수, 크기);
```

예제

```css
.container{

    display:grid;

    grid-template-columns:repeat(3, 1fr);

}
```

위 코드는 다음과 동일하다.

```css
grid-template-columns:1fr 1fr 1fr;
```

---

## 다양한 repeat() 활용

### 고정 크기

```css
grid-template-columns:repeat(4, 200px);
```

↓

```text
200px

200px

200px

200px
```

---

### 비율

```css
grid-template-columns:repeat(4, 1fr);
```

↓

```text
1fr

1fr

1fr

1fr
```

---

### 혼합

```css
grid-template-columns:200px repeat(3,1fr);
```

실무에서 Sidebar + Main Layout을 구성할 때 자주 사용한다.

---

# gap

Grid Item 사이의 간격을 지정한다.

```css
.container{

    display:grid;

    gap:20px;

}
```

결과

```text
□   □   □

□   □   □
```

Flexbox와 동일하게 `margin`보다 `gap` 사용을 권장한다.

---

## row-gap

행 사이 간격

```css
row-gap:20px;
```

---

## column-gap

열 사이 간격

```css
column-gap:30px;
```

---

## 두 값을 동시에 지정

```css
gap:20px 40px;
```

```text
row-gap

20px

column-gap

40px
```

---

# Grid Line 번호

Grid는 Line 번호를 기준으로 위치를 계산한다.

예제

```css
grid-template-columns:1fr 1fr 1fr;
```

```text
1     2     3     4

│ A │ B │ C │
```

열이 3개이면

Line은

4개가 생성된다.

행도 동일한 방식이다.

---

# grid-column

Item이 차지할 열의 범위를 지정한다.

```css
.item{

    grid-column:1 / 3;

}
```

의미

```text
Line 1

↓

A A

↓

Line 3
```

즉

두 개의 열을 차지한다.

---

## grid-column-start

```css
grid-column-start:2;
```

2번 Line부터 시작한다.

---

## grid-column-end

```css
grid-column-end:4;
```

4번 Line까지 사용한다.

---

## 축약형

```css
grid-column:2 / 4;
```

실무에서는 축약형을 많이 사용한다.

---

# grid-row

행도 동일한 방식이다.

```css
.item{

    grid-row:1 / 3;

}
```

두 개의 행을 차지한다.

---

# span

몇 칸을 차지할 것인지 지정한다.

```css
grid-column:span 2;
```

↓

현재 위치에서

2칸 사용

---

예제

```css
.item{

    grid-column:span 3;

}
```

결과

```text
□ □ □
```

3칸을 차지한다.

---

행도 동일하다.

```css
grid-row:span 2;
```

---

# grid-area

`grid-row`와 `grid-column`을 하나로 작성하는 축약 속성이다.

문법

```css
grid-area:

row-start

/

column-start

/

row-end

/

column-end;
```

예제

```css
.item{

    grid-area:1 / 1 / 3 / 3;

}
```

의미

```text
2행

2열

차지
```

---

# grid-template-areas

이름을 이용하여 레이아웃을 만드는 기능이다.

가독성이 매우 뛰어나 실무에서도 많이 사용된다.

예제

```css
.container{

    display:grid;

    grid-template-areas:

        "header header"

        "sidebar main"

        "footer footer";

}
```

---

각 Item

```css
.header{

    grid-area:header;

}
```

```css
.sidebar{

    grid-area:sidebar;

}
```

```css
.main{

    grid-area:main;

}
```

```css
.footer{

    grid-area:footer;

}
```

---

결과

```text
┌──────────────────┐

Header

├──────┬───────────┤

Side   Main

├──────┴───────────┤

Footer

└──────────────────┘
```

---

# grid-template-areas 장점

HTML 구조를 변경하지 않아도

레이아웃을 쉽게 수정할 수 있다.

가독성이 매우 뛰어나다.

관리자(Admin) 페이지에서 많이 사용된다.

---

# 빈 공간 만들기

`.`을 이용하면 빈 Cell을 만들 수 있다.

```css
grid-template-areas:

"header header"

".      main"

"footer footer";
```

↓

```text
□ Main
```

왼쪽이 비어 있는 영역이 된다.

---

# Grid Item 자동 배치

별도의 위치를 지정하지 않으면

브라우저는

왼쪽

↓

오른쪽

↓

다음 줄

순서로 자동 배치한다.

```text
A B C

D E F
```

이 방식을

Auto Placement라고 한다.

---

# Implicit Grid

명시적으로 작성하지 않았지만

필요에 의해 자동 생성되는 Grid를 의미한다.

예를 들어

```css
grid-template-columns:repeat(3,1fr);
```

인데

Item이

10개라면

브라우저는

자동으로 새로운 행을 생성한다.

---

# grid-auto-rows

자동 생성되는 행의 크기를 지정한다.

```css
grid-auto-rows:150px;
```

자동으로 만들어지는 모든 Row가

150px가 된다.

---

# grid-auto-columns

자동 생성되는 Column의 크기를 지정한다.

```css
grid-auto-columns:250px;
```

---

---

# minmax()

Grid에서 가장 많이 사용하는 함수 중 하나이다.

최소 크기와 최대 크기를 동시에 지정할 수 있다.

기본 문법

```css
minmax(최소값, 최대값)
```

예제

```css
grid-template-columns:repeat(3, minmax(200px, 1fr));
```

의미

- 최소 크기 : 200px
- 최대 크기 : 남는 공간을 비율대로 사용

브라우저 크기가 커지면

```text
200px

↓

350px

↓

500px
```

처럼 자연스럽게 늘어난다.

반대로 화면이 작아져도 200px 이하로는 줄어들지 않는다.

---

# auto-fit

반응형 Grid에서 가장 많이 사용하는 기능이다.

```css
grid-template-columns:

repeat(auto-fit, minmax(250px,1fr));
```

브라우저 폭에 따라

열(Column)의 개수가 자동으로 변경된다.

예를 들어

넓은 화면

```text
□ □ □ □
```

좁은 화면

```text
□ □

□ □
```

더 좁은 화면

```text
□

□

□
```

처럼 자동으로 재배치된다.

---

# auto-fill

사용 가능한 공간만큼 Column을 생성한다.

```css
grid-template-columns:

repeat(auto-fill, minmax(250px,1fr));
```

겉보기에는 auto-fit과 비슷하지만

빈 Column을 유지한다는 차이가 있다.

---

# auto-fit vs auto-fill

가장 많이 나오는 면접 질문이다.

### auto-fit

- 빈 Column 제거
- Item이 공간을 확장
- 대부분의 반응형 UI에서 사용

### auto-fill

- 빈 Column 유지
- Grid 구조 유지
- 특별한 레이아웃에서 사용

실무에서는 대부분

```css
auto-fit
```

을 사용한다.

---

# justify-items

각 Grid Item 내부의 가로 정렬을 담당한다.

```css
.container{

    justify-items:center;

}
```

결과

```text
┌────────┐

    A

└────────┘
```

---

# align-items

각 Grid Item 내부의 세로 정렬이다.

```css
.container{

    align-items:center;

}
```

---

# place-items

축약형이다.

```css
place-items:center;
```

↓

```css
justify-items:center;

align-items:center;
```

---

# justify-content

Grid 전체를 Container 안에서 가로 정렬한다.

```css
justify-content:center;
```

Grid의 전체 너비가 Container보다 작을 때 동작한다.

---

# align-content

Grid 전체를 세로 방향으로 정렬한다.

```css
align-content:center;
```

---

# place-content

축약형이다.

```css
place-content:center;
```

↓

```css
justify-content:center;

align-content:center;
```

---

# Grid와 Flexbox 함께 사용하기

실무에서는 둘 중 하나만 사용하는 경우보다

함께 사용하는 경우가 훨씬 많다.

예제

```text
Grid

↓

카드 배치

↓

Card 내부

↓

Flexbox
```

즉

페이지 레이아웃은 Grid

컴포넌트 내부는 Flexbox

라는 조합이 가장 일반적이다.

---

# 실무 패턴 1

## Dashboard

```css
.wrapper{

    display:grid;

    grid-template-columns:250px 1fr;

}
```

```text
Sidebar │ Main
```

Main 내부

```css
.cards{

    display:grid;

    grid-template-columns:

    repeat(auto-fit,minmax(250px,1fr));

    gap:24px;

}
```

---

# 실무 패턴 2

## 상품 목록

```css
.products{

    display:grid;

    grid-template-columns:

    repeat(auto-fit,minmax(280px,1fr));

    gap:20px;

}
```

브라우저 크기에 따라

상품 수가 자동으로 변경된다.

---

# 실무 패턴 3

## Portfolio

```css
.portfolio{

    display:grid;

    grid-template-columns:

    repeat(auto-fit,minmax(320px,1fr));

}
```

반응형 포트폴리오에서

가장 많이 사용하는 코드이다.

---

# 실무 패턴 4

## Gallery

```css
.gallery{

    display:grid;

    grid-template-columns:

    repeat(auto-fit,minmax(180px,1fr));

    gap:12px;

}
```

이미지 갤러리 제작 시 자주 사용된다.

---

# 반응형 Grid

Grid는 Media Query 없이도

어느 정도 반응형을 구현할 수 있다.

대표적인 코드

```css
grid-template-columns:

repeat(auto-fit,minmax(250px,1fr));
```

이 한 줄만으로도

대부분의 카드 레이아웃이 자연스럽게 반응형으로 동작한다.

---

# Grid 설계 순서

실무에서는 다음 순서로 Grid를 설계하는 경우가 많다.

1. Container 생성
2. Column 개수 결정
3. Row 결정
4. Gap 설정
5. Item 배치
6. 반응형 적용
7. 세부 정렬

이 순서를 익혀두면 복잡한 레이아웃도 쉽게 구성할 수 있다.

---

---

# 실무 예제 프로젝트

다음은 Grid를 이용한 관리자(Admin) 대시보드 레이아웃 예제이다.

## HTML

```html
<div class="dashboard">

    <aside class="sidebar">
        Sidebar
    </aside>

    <header class="header">
        Header
    </header>

    <main class="content">

        <div class="cards">

            <article class="card">Card 1</article>
            <article class="card">Card 2</article>
            <article class="card">Card 3</article>
            <article class="card">Card 4</article>

        </div>

    </main>

</div>
```

---

## CSS

```css
*{
    margin:0;
    padding:0;
    box-sizing:border-box;
}

.dashboard{

    display:grid;

    grid-template-columns:250px 1fr;

    grid-template-rows:70px 1fr;

    min-height:100vh;

}

.sidebar{

    grid-row:1 / 3;

    background:#333;

    color:white;

    padding:20px;

}

.header{

    background:#f5f5f5;

    display:flex;

    align-items:center;

    padding:0 24px;

}

.content{

    padding:24px;

}

.cards{

    display:grid;

    grid-template-columns:

    repeat(auto-fit,minmax(250px,1fr));

    gap:24px;

}

.card{

    padding:20px;

    border:1px solid #ddd;

    border-radius:8px;

}
```

---

## 레이아웃 구조

```text
┌──────────────────────────────────────────┐
│ Sidebar │            Header              │
├─────────┼────────────────────────────────┤
│         │ Card │ Card │ Card            │
│         ├──────┼──────┼───────          │
│         │ Card │ Card │ Card            │
│         │                            │
└─────────┴───────────────────────────────┘
```

이 예제에는 다음 개념들이 모두 포함되어 있다.

- Grid Container
- Grid Item
- grid-template-columns
- grid-template-rows
- fr
- gap
- repeat()
- auto-fit
- minmax()
- Grid + Flexbox 조합

---

# Grid와 Flexbox 선택 기준

실무에서는 "Grid와 Flexbox 중 무엇을 사용할까?"라는 고민을 자주 하게 된다.

다음 기준을 기억하면 대부분의 상황에서 적절한 선택을 할 수 있다.

| 상황 | 추천 |
|------|------|
| Header | Flexbox |
| Navigation | Flexbox |
| Toolbar | Flexbox |
| 버튼 정렬 | Flexbox |
| 검색창 | Flexbox |
| Card 내부 레이아웃 | Flexbox |
| 카드 목록 | Grid |
| 이미지 갤러리 | Grid |
| Dashboard | Grid |
| 관리자(Admin) 페이지 | Grid |
| 메인 페이지 레이아웃 | Grid |

---

# Flexbox와 Grid를 함께 사용하는 이유

실무에서는 둘을 경쟁 관계가 아니라 **상호 보완적인 기술**로 사용한다.

예를 들어 쇼핑몰 메인 페이지를 만든다면

```text
전체 상품 목록
        │
      Grid
        │
상품 카드 하나
        │
     Flexbox
```

처럼 구성하는 것이 일반적이다.

즉,

- **Grid** → 큰 레이아웃 구성
- **Flexbox** → 개별 컴포넌트 내부 정렬

이라는 역할 분담을 기억하면 된다.

---

# 이번 문서에서 새롭게 배운 내용

- Grid는 2차원 레이아웃 시스템이다.
- Grid Container와 Grid Item의 역할을 이해했다.
- `grid-template-columns`, `grid-template-rows`로 행과 열을 정의할 수 있다.
- `fr` 단위를 이용해 남은 공간을 비율로 나눌 수 있다.
- `repeat()` 함수로 반복되는 코드를 줄일 수 있다.
- `grid-column`, `grid-row`, `grid-area`를 이용해 Item의 위치를 제어할 수 있다.
- `grid-template-areas`를 이용하면 레이아웃을 직관적으로 설계할 수 있다.
- `minmax()`와 `auto-fit`을 활용하면 Media Query를 최소화하면서 반응형 레이아웃을 구현할 수 있다.
- Grid와 Flexbox는 함께 사용하는 것이 일반적인 실무 방식이다.

---

# 자주 하는 실수

- Grid와 Flexbox를 경쟁 관계라고 생각한다.
- `fr` 대신 `%`만 사용한다.
- `repeat()`를 활용하지 않아 코드가 길어진다.
- `auto-fit`과 `auto-fill`의 차이를 모른다.
- `grid-column`의 Line 번호를 혼동한다.
- `grid-template-areas`를 사용하지 않아 복잡한 레이아웃을 관리하기 어렵게 만든다.
- 모든 레이아웃을 Grid만으로 구현하려고 한다.
- Grid Item 내부 정렬까지 Grid로 해결하려고 한다.

---

# 면접 포인트

### CSS Grid란 무엇인가?

행(Row)과 열(Column)을 동시에 제어할 수 있는 2차원 레이아웃 시스템이다.

---

### Flexbox와 Grid의 차이는?

Flexbox는 1차원, Grid는 2차원 레이아웃에 적합하다.

---

### `fr` 단위란?

남은 공간을 비율(Fraction)로 나누는 Grid 전용 단위이다.

---

### `repeat()`를 사용하는 이유는?

반복되는 Column 또는 Row 정의를 간결하게 작성하기 위해 사용한다.

---

### `grid-area`의 장점은?

행과 열의 시작·끝 위치를 하나의 속성으로 지정할 수 있으며, `grid-template-areas`와 함께 사용하면 가독성이 높아진다.

---

### `auto-fit`과 `auto-fill`의 차이는?

- `auto-fit`은 빈 Column을 제거하고 Item을 확장한다.
- `auto-fill`은 빈 Column을 유지하여 Grid 구조를 보존한다.

실무에서는 대부분 `auto-fit`을 사용한다.

---

### `minmax()`는 언제 사용하는가?

반응형 Grid에서 최소 크기를 보장하면서 남는 공간을 유연하게 분배하기 위해 사용한다.

---

### Grid와 Flexbox를 함께 사용하는 이유는?

Grid는 전체 레이아웃을, Flexbox는 컴포넌트 내부 정렬을 담당하도록 역할을 분리하면 유지보수가 쉬워진다.

---

# 핵심 정리

- Grid는 2차원 레이아웃 시스템이다.
- 부모는 Grid Container, 자식은 Grid Item이다.
- `grid-template-columns`와 `grid-template-rows`로 레이아웃을 정의한다.
- `fr`은 남는 공간을 비율로 분배하는 Grid 전용 단위이다.
- `repeat()`는 반복되는 코드를 줄여준다.
- `grid-column`, `grid-row`, `grid-area`를 이용해 Item 위치를 지정할 수 있다.
- `grid-template-areas`는 복잡한 레이아웃을 직관적으로 표현한다.
- `auto-fit`, `minmax()`를 이용하면 반응형 레이아웃을 쉽게 구현할 수 있다.
- Grid는 전체 구조를, Flexbox는 내부 정렬을 담당하는 것이 일반적인 실무 패턴이다.

---

# 변경 이력

| Version | 날짜 | 변경 내용 |
|---------|------|----------|
| v1.0 | 2026-07-22 | 최초 작성 |
