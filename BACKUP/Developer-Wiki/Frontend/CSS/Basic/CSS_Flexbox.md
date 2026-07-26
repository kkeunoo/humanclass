---
title: CSS Flexbox
version: v1.0
last_updated: 2026-07-22
status: Completed
---

# CSS Flexbox

## 문서 정보

| 항목 | 내용 |
|------|------|
| 문서명 | CSS Flexbox |
| 분류 | Frontend / CSS / Basic |
| 난이도 | Basic → Intermediate |
| 선수 지식 | CSS Display, CSS Position |
| 핵심 주제 | Flex Container, Flex Item, Main Axis, Cross Axis, Flex Layout |
| 버전 | v1.0 |
| 최종 수정일 | 2026-07-22 |

---

# 개요

Flexbox(Flexible Box Layout)는 **1차원(One-Dimensional) 레이아웃**을 만들기 위한 CSS 레이아웃 시스템이다.

과거에는 `float`, `inline-block`, `table`, `position` 등을 조합하여 레이아웃을 구성했지만 코드가 복잡하고 유지보수가 어려웠다.

Flexbox는 이러한 문제를 해결하기 위해 등장했으며, 현재 대부분의 웹 프로젝트에서 기본 레이아웃 방식으로 사용된다.

Flexbox는 다음과 같은 상황에서 특히 강력하다.

- Header Navigation
- Card Layout
- Toolbar
- 버튼 그룹
- 로그인 폼
- 검색창
- Dashboard Header
- Footer
- Sidebar
- Pagination
- 가운데 정렬
- 반응형 UI

Flexbox는 행(Row) 또는 열(Column) 한 방향의 레이아웃을 제어하는 데 최적화되어 있다.

---

# 핵심 개념

Flexbox는 부모 요소와 자식 요소의 역할이 명확하게 구분된다.

```text
Flex Container
│
├── Flex Item
├── Flex Item
├── Flex Item
└── Flex Item
```

| 구성 | 설명 |
|------|------|
| Flex Container | 부모 요소 |
| Flex Item | 자식 요소 |

부모가 Flex Container가 되면 **직계 자식만 Flex Item**이 된다.

```html
<div class="container">

    <div>HTML</div>

    <div>CSS</div>

    <div>JavaScript</div>

</div>
```

```css
.container{
    display:flex;
}
```

위 예제에서 `.container`는 Flex Container이고,

```html
<div>HTML</div>
<div>CSS</div>
<div>JavaScript</div>
```

세 개가 Flex Item이다.

손자는 Flex Item이 아니다.

---

# display: flex

Flexbox는 부모에 적용한다.

```css
.container{
    display:flex;
}
```

브라우저는 이 순간부터 자식을 Flex Item으로 처리한다.

기본 배치는 다음과 같다.

```text
HTML     CSS     JavaScript
```

기본 특징

- 가로(Row) 방향 배치
- 줄바꿈하지 않음
- Item 크기에 맞게 배치
- Main Axis 생성
- Cross Axis 생성

---

# Flex Container와 Flex Item

부모

```css
.container{

    display:flex;

}
```

자식

```css
.item{

}
```

Flexbox의 대부분 속성은 부모(Container)에 적용된다.

예를 들어

```css
.container{

    justify-content:center;

}
```

처럼 부모가 자식들의 정렬을 제어한다.

반면 Item 전용 속성도 존재한다.

예를 들어

```css
.item{

    flex-grow:1;

}
```

은 특정 Item 하나의 크기만 변경한다.

정리하면 다음과 같다.

### Container 속성

- display
- flex-direction
- flex-wrap
- flex-flow
- justify-content
- align-items
- align-content
- gap

### Item 속성

- order
- flex-grow
- flex-shrink
- flex-basis
- flex
- align-self

---

# Main Axis

Flexbox에서 가장 중요한 개념이다.

Main Axis는 **모든 Flex 계산의 기준 축**이다.

기본값은 가로 방향이다.

```css
.container{

    display:flex;

}
```

```text
Main Axis

────────────────────────▶
```

Item은 Main Axis를 따라 배치된다.

```text
HTML

↓

CSS

↓

JavaScript

❌

아니다.

```

실제는

```text
HTML   CSS   JavaScript
```

이다.

즉

기본 Main Axis는 가로이다.

---

# Cross Axis

Main Axis와 수직인 방향을 Cross Axis라고 한다.

```text
          ↑

          │

          │

          │

          ↓
```

즉

```text
Cross Axis

      ↑
      │
      │
      │

HTML CSS JS

────────────▶

Main Axis
```

모든 정렬은

- Main Axis
- Cross Axis

두 축을 기준으로 이루어진다.

---

# Main Axis와 Cross Axis를 이해해야 하는 이유

많은 사람들이

> justify-content = 가로

> align-items = 세로

라고 외운다.

하지만 이것은 절반만 맞는 설명이다.

Flexbox는

"가로/세로"

가 아니라

"Main Axis / Cross Axis"

기준으로 동작한다.

따라서

```css
flex-direction:column;
```

으로 바꾸는 순간

축이 뒤집힌다.

이 원리를 이해하지 못하면 Flexbox를 사용할 때 계속 헷갈리게 된다.

---

# flex-direction

Main Axis의 방향을 변경한다.

```css
.container{

    flex-direction:row;

}
```

기본값이다.

---

## row

기본값

```text
A   B   C   D
```

Main Axis

```text
────────────▶
```

---

## row-reverse

반대로 배치한다.

```text
D   C   B   A
```

Main Axis 방향도 반대로 계산된다.

---

## column

세로 방향으로 변경한다.

```css
.container{

    flex-direction:column;

}
```

배치

```text
A

B

C

D
```

이 순간

Main Axis는

```text
↓

↓

↓

```

가 된다.

---

## column-reverse

역순 배치

```text
D

C

B

A
```

---

# flex-direction에 따른 축 변화

기본값

```css
flex-direction:row;
```

```text
Main Axis

────────────▶

Cross Axis

↑
│
│
↓
```

---

Column

```css
flex-direction:column;
```

```text
Main Axis

↓

↓

↓

Cross Axis

◀──────────▶
```

즉

축이 회전한다.

이것이 Flexbox에서 가장 중요한 원리이다.

---

# justify-content

Main Axis 방향의 정렬을 담당한다.

```css
.container{

    justify-content:center;

}
```

---

## flex-start

기본값

```text
A B C
```

---

## center

```text
        A B C
```

---

## flex-end

```text
                A B C
```

---

## space-between

```text
A          B          C
```

양쪽 끝은 붙고

사이만 동일하게 벌어진다.

---

## space-around

```text
   A      B      C
```

양쪽 여백은

중간 여백의 절반이다.

---

## space-evenly

```text
 A     B     C
```

모든 간격이 동일하다.

실무에서는 가장 많이 사용되는 옵션 중 하나이다.

---

# justify-content 시각적 비교

```text
flex-start

A B C
```

```text
center

      A B C
```

```text
flex-end

            A B C
```

```text
space-between

A       B       C
```

```text
space-around

  A    B    C
```

```text
space-evenly

 A   B   C
```

---

# align-items

Cross Axis 방향의 정렬을 담당한다.

```css
.container{

    display:flex;

    align-items:center;

}
```

예제

```css
.container{

    display:flex;

    height:300px;

    align-items:center;

}
```

결과

```text
────────────────────────

        A B C

────────────────────────
```

Item들이 세로 중앙으로 이동한다.

---

# align-items의 주요 값

## stretch

기본값

```css
align-items:stretch;
```

Cross Axis 방향으로 가능한 공간을 채운다.

---

## flex-start

```text
A

B

C
```

위쪽 정렬

---

## center

세로 중앙 정렬

---

## flex-end

아래쪽 정렬

---

## baseline

텍스트의 Baseline을 기준으로 정렬한다.

```text
HTML

CSS

JavaScript
```

글자 크기가 다른 경우 유용하다.

---

# justify-content와 align-items 차이

가장 많이 나오는 면접 질문이다.

Row 기준

```css
display:flex;
```

```text
justify-content

←──────────→

가로
```

```text
align-items

↑

│

↓

세로
```

하지만

```css
flex-direction:column;
```

이 되면

```text
justify-content

↑

│

↓

세로
```

```text
align-items

←──────────→

가로
```

즉

둘은

가로/세로가 아니라

Main Axis / Cross Axis를 기준으로 동작한다.

---

# gap

Flex Item 사이의 간격을 지정한다.

```css
.container{

    display:flex;

    gap:20px;

}
```

결과

```text
A      B      C
```

과거에는

```css
.item{

    margin-right:20px;

}
```

를 많이 사용했지만

마지막 요소의 여백 처리나 방향 변경 시 관리가 어려웠다.

`gap`은 이러한 문제를 해결하며, Flexbox와 Grid 모두에서 사용할 수 있는 권장 방식이다.

---

# gap의 종류

```css
gap:20px;
```

행과 열 간격 모두 20px

---

```css
gap:20px 40px;
```

```text
row-gap : 20px

column-gap : 40px
```

---

또는 개별 속성을 사용할 수도 있다.

```css
row-gap:20px;

column-gap:40px;
```

---

# flex-wrap

기본적으로 Flexbox는 줄바꿈을 하지 않는다.

```css
.container{

    display:flex;

    flex-wrap:nowrap;

}
```

공간이 부족하면 Item은 가능한 한 한 줄에 배치되며, 필요에 따라 줄어들 수 있다.

---

## wrap

```css
.container{

    flex-wrap:wrap;

}
```

공간이 부족하면 다음 줄로 이동한다.

```text
A B C

D E F
```

실무에서는 카드 목록이나 반응형 레이아웃에서 자주 사용한다.

---

## wrap-reverse

줄바꿈 방향을 반대로 한다.

```text
D E F

A B C
```

일반적인 웹 UI에서는 자주 사용되지는 않지만 동작 원리를 알아두면 좋다.

---

# flex-flow

`flex-direction`과 `flex-wrap`을 함께 작성하는 축약 속성이다.

```css
.container{

    flex-flow:row wrap;

}
```

위 코드는 다음과 같다.

```css
.container{

    flex-direction:row;

    flex-wrap:wrap;

}
```

축약 속성을 사용하면 레이아웃 설정을 더 간결하게 표현할 수 있다.

---

# align-content

`align-content`는 여러 줄(Wrap)이 생성되었을 때 **줄(Row) 자체의 정렬**을 담당한다.

많은 초보자가 `align-items`와 혼동하지만 적용 대상이 다르다.

```css
.container{
    display:flex;
    flex-wrap:wrap;
    align-content:center;
}
```

`align-content`는 **줄이 하나뿐이라면 동작하지 않는다.**

---

# align-content

`align-content`는 여러 줄로 배치된 Flex Line 자체를 Cross Axis 방향으로 정렬하는 속성이다.

많은 사람들이 `align-items`와 혼동하지만 두 속성은 완전히 다르다.

| 속성 | 정렬 대상 |
|------|-----------|
| align-items | Item |
| align-content | Flex Line(줄) |

즉,

```text
align-items

줄 안의 Item 정렬
```

```text
align-content

줄 자체 정렬
```

이다.

---

## align-content가 동작하는 조건

다음 두 조건을 만족해야 한다.

### 1. 여러 줄이어야 한다.

```css
.container{

    display:flex;

    flex-wrap:wrap;

}
```

---

### 2. Cross Axis 방향의 여유 공간이 있어야 한다.

예제

```css
.container{

    display:flex;

    flex-wrap:wrap;

    height:500px;

}
```

줄이 하나뿐이면

```css
align-content:center;
```

를 작성해도 아무 변화가 없다.

---

## align-content 값

### stretch (기본값)

줄 전체를 가능한 공간까지 늘린다.

```css
align-content:stretch;
```

---

### flex-start

줄을 위쪽에 배치한다.

---

### center

줄 전체를 가운데 배치한다.

---

### flex-end

줄을 아래쪽에 배치한다.

---

### space-between

줄 사이의 간격만 동일하게 만든다.

---

### space-around

줄의 양쪽 여백이 절반씩 생긴다.

---

### space-evenly

모든 줄 간격이 동일하다.

---

# align-items와 align-content 비교

예제

```css
.container{

    display:flex;

    flex-wrap:wrap;

    height:400px;

}
```

```text
align-items

↓

각 줄 안에서

Item을 정렬
```

반면

```text
align-content

↓

줄 전체를

위·가운데·아래

정렬
```

둘을 혼동하지 않는 것이 중요하다.

---

# Item 속성

지금까지는 Container 속성을 살펴보았다.

이제부터는

**Flex Item**

전용 속성을 학습한다.

대표적인 속성은 다음과 같다.

- order
- flex-grow
- flex-shrink
- flex-basis
- flex
- align-self

---

# order

Item의 화면 표시 순서를 변경한다.

```css
.item{

    order:2;

}
```

기본값은

```css
order:0;
```

이다.

숫자가 작을수록 먼저 배치된다.

---

## order 예제

HTML

```html
<div class="container">

    <div>A</div>

    <div>B</div>

    <div>C</div>

</div>
```

CSS

```css
.container{

    display:flex;

}

.container div:nth-child(2){

    order:-1;

}
```

결과

```text
B A C
```

---

## order 주의사항

`order`는

화면의 순서만 변경한다.

DOM 순서는 변경되지 않는다.

즉

```html
A

B

C
```

가

```text
B A C
```

로 보여도

키보드 Tab 이동

화면 낭독기

검색 엔진

모두

원래 DOM 순서를 사용한다.

따라서 접근성을 위해

`order`를 이용하여

콘텐츠 순서를 크게 변경하는 것은 권장되지 않는다.

---

# flex-grow

Flexbox에서

남는 공간을

얼마나 가져갈지를 결정한다.

기본값

```css
flex-grow:0;
```

---

## grow 예제

```css
.item{

    flex-grow:1;

}
```

```text
A BBBBBBBBBBBBBBB
```

남는 공간을

Item이 가져간다.

---

## grow 비율

```css
.item1{

    flex-grow:1;

}

.item2{

    flex-grow:2;

}
```

남는 공간을

```text
1 : 2
```

비율로 나누어 가진다.

---

예를 들어

남는 공간이

300px라면

```text
Item1

100px

Item2

200px
```

가 된다.

---

# grow 계산 원리

다음 예제를 보자.

```css
.item1{

    flex-grow:1;

}

.item2{

    flex-grow:1;

}

.item3{

    flex-grow:2;

}
```

남는 공간

400px

↓

비율

```text
1

1

2
```

↓

총합

```text
4
```

↓

계산

```text
400 / 4

=

100
```

따라서

```text
item1

100px

item2

100px

item3

200px
```

를 가져간다.

---

# flex-shrink

공간이 부족할 때

얼마나 줄어들 것인지를 결정한다.

기본값

```css
flex-shrink:1;
```

즉

기본적으로

모든 Item은 줄어든다.

---

## shrink 예제

```css
.item{

    flex-shrink:0;
}
```

줄어들지 않는다.

---

```css
.item{

    flex-shrink:2;
}
```

다른 Item보다

두 배 빠르게 줄어든다.

---

# shrink 계산

예를 들어

Container

```text
600px
```

Item 총합

```text
700px
```

부족한 공간

```text
100px
```

↓

shrink 비율에 따라

100px를

나누어 줄인다.

---

# flex-basis

Item의

초기 크기이다.

```css
.item{

    flex-basis:200px;

}
```

---

예제

```css
.item{

    flex-basis:300px;

}
```

Item은

300px부터 시작한다.

---

# width와 flex-basis 차이

많이 헷갈리는 부분이다.

```css
width:200px;
```

와

```css
flex-basis:200px;
```

는

비슷하지만 다르다.

Flexbox에서는

보통

`flex-basis`

가

우선 적용된다.

---

예제

```css
.item{

    width:100px;

    flex-basis:300px;

}
```

실제로는

300px 기준으로

계산된다.

---

# flex-grow + basis

예제

```css
.item{

    flex-grow:1;

    flex-basis:200px;

}
```

순서

```text
1.

200px 확보

↓

2.

남는 공간 계산

↓

3.

grow 적용
```

---

# flex-shrink + basis

예제

```css
.item{

    flex-basis:300px;

    flex-shrink:1;

}
```

순서

```text
300px 시작

↓

공간 부족

↓

shrink 적용
```

---

# flex 속기

다음 세 개를 한 번에 작성한다.

```text
flex-grow

flex-shrink

flex-basis
```

---

## flex:1

가장 많이 사용하는 코드이다.

```css
.item{

    flex:1;

}
```

=

```css
.item{

    flex:1 1 0;
}
```

이다.

---

## flex:auto

```css
flex:auto;
```

=

```css
flex:1 1 auto;
```

---

## flex:none

```css
flex:none;
```

=

```css
flex:0 0 auto;
```

줄어들지도

늘어나지도 않는다.

---

## flex 초기값

```css
flex:0 1 auto;
```

브라우저 기본값이다.

---

# flex 속기 정리

| 속성 | 의미 |
|------|------|
| flex:1 | 공간을 균등하게 나눔 |
| flex:auto | 콘텐츠 크기를 유지하면서 공간 분배 |
| flex:none | 크기 고정 |
| flex:0 1 auto | 기본값 |

---

# align-self

특정 Item 하나만

Cross Axis 정렬을 변경한다.

```css
.item{

    align-self:flex-end;

}
```

부모의

```css
align-items:center;
```

보다

우선한다.

---

## 예제

```css
.container{

    display:flex;

    align-items:center;

}
```

```css
.item{

    align-self:flex-start;

}
```

Item 하나만

위쪽으로 이동한다.

---

# auto margin

실무에서 매우 많이 사용하는 패턴이다.

예제

```css
.menu{

    margin-left:auto;

}
```

결과

```text
Logo                     Menu
```

남는 공간을

margin이 가져간다.

---

## Header 패턴

```css
header{

    display:flex;

}

.logo{

}

.menu{

    margin-left:auto;

}
```

HTML을 복잡하게 만들지 않고

Header를 구성할 수 있다.

---

## 버튼 그룹

```css
.buttons{

    display:flex;

}
```

```css
.submit{

    margin-left:auto;

}
```

결과

```text
취소            저장
```

버튼을

오른쪽 끝으로 밀어낼 수 있다.

---

# min-width:0

실무에서 가장 많이 놓치는 속성 중 하나이다.

Flex Item의 기본값은

```css
min-width:auto;
```

이다.

그래서

긴 문자열이 있으면

Item이 줄어들지 않을 수 있다.

---

예제

```css
.item{

    min-width:0;
}
```

이렇게 작성하면

필요할 때

정상적으로 줄어든다.

---

## 왜 필요한가?

예제

```text
Container

500px
```

Item

```text
매우매우매우매우매우매우긴문자열...
```

↓

기본값

```css
min-width:auto;
```

↓

줄어들지 않음

↓

레이아웃 깨짐

---

```css
min-width:0;
```

↓

줄어듦

↓

overflow 처리 가능

---

실무에서는 다음 속성과 함께 사용하는 경우가 많다.

```css
overflow:hidden;

text-overflow:ellipsis;

white-space:nowrap;
```

---

---

# 실무에서 자주 사용하는 Flexbox 패턴

Flexbox는 대부분의 웹 프로젝트에서 기본 레이아웃으로 사용된다.

다음은 실무에서 가장 많이 사용하는 패턴들이다.

---

## Header Layout

가장 많이 사용하는 형태이다.

```html
<header class="header">

    <h1 class="logo">MySite</h1>

    <nav class="menu">

        <a href="#">Home</a>
        <a href="#">About</a>
        <a href="#">Contact</a>

    </nav>

</header>
```

```css
.header{

    display:flex;

    align-items:center;

    padding:20px;

}

.menu{

    margin-left:auto;

    display:flex;

    gap:20px;

}
```

결과

```text
Logo                          Home About Contact
```

실무에서는 `margin-left:auto`를 매우 자주 사용한다.

---

# Navigation

```css
nav{

    display:flex;

    gap:24px;

    align-items:center;

}
```

메뉴 간 간격은 `margin`보다 `gap`을 사용하는 것이 유지보수에 유리하다.

---

# 카드 목록(Card Layout)

```css
.cards{

    display:flex;

    flex-wrap:wrap;

    gap:24px;

}
```

```css
.card{

    flex:1 1 300px;

}
```

브라우저 크기가 줄어들면 자동으로 줄바꿈된다.

```text
□ □ □

□ □ □
```

반응형 UI에서 가장 많이 사용하는 패턴이다.

---

# Sidebar Layout

```css
.layout{

    display:flex;

}
```

```css
.sidebar{

    width:260px;

}
```

```css
.content{

    flex:1;

}
```

결과

```text
┌────────┬────────────────────┐
│Sidebar │                    │
│        │      Content       │
│        │                    │
└────────┴────────────────────┘
```

---

# Toolbar

```css
.toolbar{

    display:flex;

    align-items:center;

    gap:12px;

}
```

검색창

버튼

필터

정렬 버튼

등을 배치할 때 많이 사용한다.

---

# 버튼 그룹

```css
.buttons{

    display:flex;

    justify-content:flex-end;

    gap:12px;

}
```

결과

```text
             취소   저장
```

---

# 가운데 정렬

Flexbox의 대표적인 활용 예제이다.

```css
.container{

    display:flex;

    justify-content:center;

    align-items:center;

}
```

결과

```text
┌────────────────────┐

        Item

└────────────────────┘
```

가로와 세로를 동시에 가운데 정렬할 수 있다.

---

# 로그인 화면

```css
body{

    display:flex;

    justify-content:center;

    align-items:center;

    min-height:100vh;

}
```

로그인 페이지나 로딩 화면에서 자주 사용되는 패턴이다.

---

# Holy Grail Layout

대표적인 웹 레이아웃 구조이다.

```text
Header

Sidebar   Main

Footer
```

Flexbox를 이용하면 비교적 간단하게 구현할 수 있다.

---

# Flexbox와 Grid 비교

| Flexbox | Grid |
|---------|------|
| 1차원 레이아웃 | 2차원 레이아웃 |
| 행 또는 열 중심 | 행과 열을 동시에 제어 |
| 콘텐츠 흐름 중심 | 레이아웃 중심 |
| Header | Dashboard |
| Navigation | 관리자 페이지 |
| Toolbar | 전체 페이지 |
| Card 목록 | 복잡한 UI |

---

# 언제 Flexbox를 사용할까?

다음과 같은 경우에는 Flexbox가 적합하다.

- Header
- Navigation
- 버튼 정렬
- Toolbar
- 검색창
- Card 목록
- Footer
- Sidebar
- Pagination
- 한 줄 레이아웃

---

# 언제 Grid를 사용할까?

다음과 같은 경우에는 Grid가 적합하다.

- Dashboard
- 관리자 페이지
- 복잡한 화면
- 행과 열을 동시에 제어해야 하는 경우
- 전체 페이지 레이아웃

---

# 실무 예제 프로젝트

다음은 Flexbox를 이용한 간단한 Header 레이아웃이다.

```html
<header class="header">

    <h1>Developer Wiki</h1>

    <nav>

        <a href="#">HTML</a>
        <a href="#">CSS</a>
        <a href="#">JavaScript</a>
        <a href="#">React</a>

    </nav>

</header>
```

```css
*{
    margin:0;
    padding:0;
    box-sizing:border-box;
}

.header{

    display:flex;

    align-items:center;

    padding:20px;

    background:#222;

    color:white;

}

nav{

    margin-left:auto;

    display:flex;

    gap:24px;

}

nav a{

    color:white;

    text-decoration:none;

}
```

이 예제에는 다음 개념들이 모두 포함되어 있다.

- display:flex
- align-items
- gap
- margin-left:auto
- Main Axis
- Cross Axis

---

# 이번 문서에서 새롭게 배운 내용

- Flexbox는 1차원 레이아웃 시스템이다.
- 부모(Container)와 자식(Item)의 역할이 명확하게 구분된다.
- 모든 정렬은 Main Axis와 Cross Axis를 기준으로 이루어진다.
- `justify-content`와 `align-items`는 축을 기준으로 동작한다.
- `gap`은 Item 간 간격을 관리하는 가장 권장되는 방법이다.
- `flex-grow`, `flex-shrink`, `flex-basis`를 통해 공간을 유연하게 분배할 수 있다.
- `margin-left:auto`는 Header와 Navigation에서 매우 자주 사용된다.
- `min-width:0`은 긴 문자열로 인한 레이아웃 깨짐을 방지하는 중요한 속성이다.

---

# 자주 하는 실수

- `justify-content`를 항상 가로 정렬이라고 외운다.
- `align-items`를 항상 세로 정렬이라고 외운다.
- `flex-direction` 변경 시 축이 바뀌는 것을 잊는다.
- `order`로 화면 순서를 크게 변경한다.
- `gap` 대신 `margin`만 사용한다.
- `flex-basis`와 `width`를 같은 개념으로 생각한다.
- `min-width:0`을 작성하지 않아 레이아웃이 깨진다.
- `align-content`와 `align-items`를 혼동한다.

---

# 면접 포인트

### Flexbox가 필요한 이유는 무엇인가?

기존 `float` 기반 레이아웃의 한계를 해결하기 위해 등장한 1차원 레이아웃 시스템이다.

---

### Main Axis와 Cross Axis란?

Flexbox의 모든 계산 기준이 되는 두 개의 축이다.

---

### justify-content와 align-items의 차이는?

`justify-content`는 Main Axis 방향, `align-items`는 Cross Axis 방향을 정렬한다.

---

### flex-grow란?

남는 공간을 비율에 따라 나누어 갖는 속성이다.

---

### flex-shrink란?

공간이 부족할 때 줄어드는 비율을 지정하는 속성이다.

---

### flex-basis란?

Flex Item의 초기 크기를 지정하는 속성이다.

---

### flex:1은 무엇을 의미하는가?

`flex: 1 1 0`의 축약형으로, 남는 공간을 균등하게 분배한다.

---

### gap을 사용하는 이유는?

Item 간 간격을 일정하게 유지하며 `margin`보다 관리가 쉽기 때문이다.

---

### order 사용 시 주의할 점은?

화면 순서만 변경되고 DOM 순서는 유지되므로 접근성을 고려해야 한다.

---

### Flexbox와 Grid의 차이는?

Flexbox는 1차원 레이아웃, Grid는 2차원 레이아웃에 적합하다.

---

# 핵심 정리

- Flexbox는 1차원 레이아웃 시스템이다.
- 부모는 Flex Container, 자식은 Flex Item이다.
- 모든 정렬은 Main Axis와 Cross Axis 기준으로 동작한다.
- `justify-content`는 Main Axis, `align-items`는 Cross Axis를 담당한다.
- `gap`은 간격을 관리하는 가장 권장되는 방식이다.
- `flex-grow`, `flex-shrink`, `flex-basis`는 공간 분배의 핵심 속성이다.
- `margin-left:auto`와 `min-width:0`은 실무에서 매우 자주 사용되는 패턴이다.
- Header, Navigation, Card Layout 등 대부분의 UI는 Flexbox로 구현할 수 있다.
- 복잡한 2차원 레이아웃에는 Grid를 사용하는 것이 적합하다.

---

# 변경 이력

| Version | 날짜 | 변경 내용 |
|---------|------|----------|
| v1.0 | 2026-07-22 | 최초 작성 |
