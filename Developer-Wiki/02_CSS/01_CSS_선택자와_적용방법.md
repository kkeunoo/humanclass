# 01. 선택자와 적용 방법 — 무엇을 바꿀 것인가

[CSS 목차](README.md) · [충돌과 상속](01-02_CSS_우선순위와_상속.md)

HTML이 내용의 구조라면 CSS는 그 구조를 화면에 어떻게 표시할지 정한다. 먼저 **어떤 요소를 고르는지**, 다음으로 **어떤 속성을 어떤 값으로 바꾸는지** 읽는다.

<!-- chapter-toc -->

- [1. CSS를 읽고 연결하기](01_CSS_선택자와_적용방법.md#section-1)
- [2. 원본에 있는 선택자 찾기](01_CSS_선택자와_적용방법.md#section-2)
- [3. 상태에 따라 달라지는 선택](01_CSS_선택자와_적용방법.md#section-3)
- [복습](01_CSS_선택자와_적용방법.md#section-4)

<a id="section-1"></a>

## 1. CSS를 읽고 연결하기

```css
/* 설명용 재구성: 모든 h2의 글자 크기를 지정 */
h2 {
    font-size: 30px;
}
```

`h2`는 선택자, `font-size`는 속성, `30px`는 값이다. 선언은 `속성: 값;`으로 적는다. 마지막 선언의 세미콜론은 생략할 수 있지만, 선언을 추가할 때 실수하지 않도록 붙인다. CSS 주석은 `/* ... */`이고 HTML 주석과 다르다.

| 수업에서 쓴 방법 | 원본 위치 | 읽을 때 확인할 것 |
| --- | --- | --- |
| 내부 CSS | 양쪽 `01_selector.html`의 style | head 안의 style에 규칙을 적음 |
| 외부 CSS | 양쪽 `03_box.html`의 link | href가 실제 CSS 파일까지 연결되는지 |
| 인라인 CSS | 양쪽 `01_selector.html`의 div2 | 해당 요소의 style 속성에 선언을 적음 |

외부 파일 연결 예시는 `03_box.html`의 `<link rel="stylesheet" href="asset/css/03_box.css">`다. 외부 CSS 파일에는 `<style>` 태그를 넣지 않는다. 파일의 적용 방식만으로 언제나 우선순위가 결정되는 것은 아니다. 충돌은 다음 문서에서 살펴본다.

<a id="section-2"></a>

## 2. 원본에 있는 선택자 찾기

| 원본 선택자 | 고르는 대상 |
| --- | --- |
| `*` | 모든 요소 |
| `h1, h2` | h1 또는 h2 |
| `#li1` | id가 li1인 요소 |
| `.c1` | c1 클래스를 가진 요소 |
| `[readonly]` | readonly 속성이 있는 요소 |
| `[type=password]` | type 값이 password인 요소 |
| `[href^=https]` / `[href$=com]` | href 값이 해당 문자열로 시작 / 끝나는 요소 |
| `[class~=bigText]` | 공백으로 구분한 class 항목 중 bigText가 있는 요소 |
| `h2.c1` / `li.c1.c2` | 한 요소가 적힌 조건을 모두 만족 |
| `div strong` | div 안의 모든 깊이에 있는 strong |
| `div > strong` | div의 바로 아래 자식 strong |

`.c1`의 점을 지우면 클래스 선택자가 태그 선택자로 바뀐다. 같은 클래스를 고르는 다른 표기라는 뜻이 아니다. `~=`는 class 전용 문법이 아니라 속성의 공백 구분 항목을 비교하는 문법이다. `#li3`과 `[id=li3]`는 이 원본에서 같은 요소를 고르지만 **명시도는 다르다**. [선택자 표준](https://www.w3.org/TR/selectors-4/)

### 강사님 코드

`01_selector.html` 87~95행 — **원본 발췌**

```css
        /* 자손 선택자 */
        div strong {
            color: blue;
        }

        /* 자식 선택자 */
        div > strong {
            font-size: 40px;
        }
```

div 바로 아래 strong은 파란색·40px가 모두 적용된다. div 안의 a 아래 strong은 자손 조건만 맞으므로 파란색이 된다. 어떤 규칙이 맞는지 HTML의 부모·자식 관계를 따라 읽는다.

### 내 코드

`01_selector.html` 89~99행 — **원본 발췌**

```css
            /* 자손 선택자, 띄어쓰기는 div 핏줄에 strong이 언젠가 나온다면 적용 
            div 안에 몇단계 아래여도 strong이 있다면 적용되는 양식 */
            div strong {
                color: blue;
            }

            /* 자식 선택자, 꺽새를 이용하면 바로 밑에 있는 자식만 선택할 때 적용 
            div아래 strong이 있을 경우에만 적용되는 양식 */
            div > strong {
                font-size: 40px;
            }
```

동작은 같다. 내 주석의 “몇 단계 아래여도”는 자손과 자식을 구분하는 데 도움이 된다. 다만 CSS의 관계는 코드 들여쓰기가 아니라 실제 요소의 중첩으로 정해진다.

<a id="section-3"></a>

## 3. 상태에 따라 달라지는 선택

### 강사님 코드

`01_selector.html` 111~123행 — **원본 발췌**

```css
        /* checkbox, radio가 선택된 상태일 때 */
        input[type=checkbox]:checked{
            width: 20px;
            height: 20px;
        }

        /* + : 바로 다음 형제 요소 */
        /* input[type=checkbox] + span {
            text-decoration: line-through;
        } */
        input[type=checkbox]:checked + span {
            text-decoration: line-through;
        }
```

체크된 체크박스는 20×20 크기가 되고, 바로 다음 요소 형제가 span이면 취소선을 긋는다. 중간의 줄바꿈·공백 텍스트가 `+` 관계를 끊지는 않는다. 주석 안의 규칙은 실행되지 않는다.

### 내 코드

`01_selector.html` 117~129행 — **원본 발췌**

```css
            /* 체크박스 또는 라디오가 선택 된 상태일 때 상태 변경 */
            input[type=checkbox]:checked {
                width: 20px;
                height: 20px;
            }

            /* input[type=checkbox]: + span {
                text-decoration: line-through;
            } */
            /* 체크박스 또는 라디오가 선택 된 상태일 때 다음 형제요소를 변경 */
            input[type=checkbox]:checked + span {
                text-decoration: line-through;
            }
```

실행되는 규칙은 같다. 주석의 `input[type=checkbox]: + span`은 콜론 뒤 상태 이름이 없어 잘못된 선택자다. 지금은 주석이므로 영향이 없지만 그대로 활성화하면 안 된다. 라디오도 `:checked` 상태를 가질 수 있으나, **이 규칙은 type=checkbox로 제한되어 라디오에는 적용되지 않는다.**

| 나머지 수업 선택자 | 의미·주의 |
| --- | --- |
| `#div1:hover` | 포인터를 올린 상태 |
| `#div1:active` | 활성화하는 동안. 클릭 후 영구 유지하는 선택이 아님 |
| `.text1:focus` | 해당 입력이 포커스를 가진 상태 |
| `#ul1 > li:nth-child(4)` | 부모의 요소 자식 중 4번째이면서 li인 요소 |
| `#ul1 > li:nth-child(2n+1)` | 1·3·5번째 요소 자식 중 li |
| `#ul1 li:not(.c3)` | ul1 안의 li 중 c3 클래스가 없는 요소 |
| `h3::before` / `h3::after` | h3 내용의 앞·뒤에 원본의 content 문자열 표시 |
| `::selection` | 선택한 텍스트 영역의 표현 |

`nth-child`는 li만 따로 세는 문법이 아니다. 원본은 형제가 모두 li라서 차이가 안 보인다. 가상 요소의 글은 HTML에 실제 자식 태그를 추가한 것과 구분한다. 원본 주석의 “자바는 document만 건드릴 수 있음”은 JavaScript 전체의 기능 제한으로 외우지 않는다.

<a id="section-4"></a>

## 복습

체크박스와 span 사이에 `<em>안내</em>`를 넣으면 원본의 취소선이 span에 적용될까?

<details>
<summary>해설</summary>

아니다. 바로 다음 요소 형제가 em으로 바뀌므로 `+ span`이 맞지 않는다. 새 선택자를 추가하기 전에 현재 HTML 구조와 선택 조건을 먼저 확인한다.

</details>

**추가로 알면 좋은 것:** `:focus-visible`, `:is()`, `:where()`, `:has()`와 BEM 설계는 원본 선택자 실습과 분리한다. 기본 문제에 요구하지 않는다.

<!-- inlined-extra-2026 -->


## 추가로 알면 좋은 것

이하의 내용은 **수업 원본에서 확인된 필수 진도가 아닌 추가 학습**이다. 위의 기본 설명을 이해한 뒤 필요할 때 읽는다.

<a id="extra-02-1"></a>

### 1. 선택 조건과 상호작용

| 기능 | 기본 선택자 이후에 생기는 질문 |
| --- | --- |
| :is() | 여러 선택 조건을 한 곳에서 묶고 싶을 때 |
| :where() | 묶은 조건의 명시도를 0으로 다루고 싶을 때 |
| :has() | 관계를 만족하는 요소의 존재에 따라 대상을 고를 때 |
| :focus-visible | 브라우저가 포커스 표시가 필요하다고 판단한 상태를 표현할 때 |
| pointer-events | 포인터 대상 처리와 키보드 포커스를 구분할 때 |
| inert·aria-hidden | CSS 표시 외에 조작·접근성 의미를 다룰 때. HTML·접근성의 별도 학습 필요 |

```css
/* 추가 예제: 실제 button 요소의 키보드 포커스 표현 */
.action:focus-visible {
    outline: 3px solid #185abc;
    outline-offset: 3px;
}
```

focus-visible을 “Tab을 눌렀을 때만”이라는 단일 조건으로 외우지 않는다. 기본 :focus와 목적을 비교한다. 포커스 표시를 제거하고 대체 표시도 주지 않는 방향으로 사용하지 않는다. [선택자 표준](https://www.w3.org/TR/selectors-4/#the-focus-visible-pseudo)

<!-- legacy-migration -->

<a id="css-12"></a>
<a id="css-48"></a>
<a id="css-51"></a>
<a id="index-section-94"></a>
<a id="index-section-86"></a>
<a id="index-section-87"></a>
<a id="index-section-80"></a>

### 이전 색인 링크 안내

이전 절 주소를 보존한 이동 안내다. 옛 절 번호와 현재 절은 같지 않다. 적용·선택자는 이 문서, 우선순위·상속은 [분리한 문서](01-02_CSS_우선순위와_상속.md), 새 선택자는 [추가편](01_CSS_선택자와_적용방법.md#extra-02-1)에서 읽는다.

---

[장별 연습문제 풀기](실습/연습문제/01_CSS_선택자와_적용방법_연습문제.md)
