# 01. CSS 선택자와 적용 — 어떤 요소를 어떻게 바꿀까

[CSS 목차](README.md) · [읽기 안내](00_CSS_V3_동작_백과_읽기법.md)

HTML로 만든 제목·목록·입력을 화면에 어떻게 표시할지 정하는 언어가 CSS다. 먼저 ‘누구에게 적용하는가’를 고른 뒤 ‘무엇을 어떤 값으로 바꾸는가’를 적는다. 규칙을 읽는 이 순서가 모든 CSS 장의 출발점이다.

<a id="chapter-toc"></a>

**이 장의 목차:** [목표](#learn) · [개념](#concepts) · [작은 예제](#example) · [내 코드](#my-code) · [연결](#connections) · [평가](#review) · [비교](#teacher) · [결과·실험](#results) · [TIP·출처](#tips) · [복습](#practice)

<a id="learn"></a>

## 1. 이 장에서 배울 것

선택자·속성·값·선언을 구분한다. 내부·외부·인라인 적용 위치를 찾고, 자손·자식·형제·상태 조건에 맞는 요소를 직접 짚는다.

이번 장의 개념과 원본 기능은 수업 범위다. 원본에 없는 선택 기능은 9절 TIP으로 구분한다. 결과를 읽을 때는 선택된 요소·속성·기준값·실행 상태를 함께 적는다.

<a id="concepts"></a>

## 2. 무엇이며, 왜 필요한가

`h2 { color: blue; }`에서 h2는 대상 선택자, color는 글자색 속성, blue는 값이다. 중괄호 안의 `color: blue;` 한 묶음이 선언이다. 같은 규칙에 여러 선언을 적을 수 있다. HTML의 `<style>` 안에 쓰는 내부 CSS, 별도 파일을 link로 불러오는 외부 CSS, 요소의 style 속성에 쓰는 인라인 선언을 구분한다. 외부 .css에는 style 태그를 넣지 않는다.

선택자는 이름만 보는 것과 관계·상태를 함께 보는 것이 있다. `.notice`는 notice 클래스를 가진 요소, `#result`는 그 ID를 가진 요소다. `div strong`은 div 아래 어느 깊이에 있는 strong도 고르지만 `div > strong`은 바로 아래만 고른다. `+`는 바로 다음 **요소 형제**다. 코드의 공백 들여쓰기 자체가 부모·형제 관계를 만드는 것은 아니다.

| 수업 선택자 | 읽는 말 | 구별할 것 |
| --- | --- | --- |
| `*` / `h1, h2` | 전체 / h1 또는 h2 | 쉼표는 둘 중 해당 요소 |
| `h2.c1` / `li.c1.c2` | 한 요소가 조건 모두 만족 | 공백을 넣은 자손 관계와 다름 |
| `[readonly]` / `[type=password]` | 속성 있음 / 속성값 일치 | HTML 속성 기준 |
| `[href^=https]` / `[href$=com]` | 해당 문자열로 시작 / 끝 | 링크의 실제 안전성을 판정하는 규칙은 아님 |
| `[class~=bigText]` | 공백으로 나눈 항목 중 일치 | 속성 토큰 비교 |
| `:hover` / `:active` / `:focus` | 올림 / 활성화 중 / 포커스 | 클릭 후 영구 상태와 다름 |
| `:nth-child(2n+1)` | 1·3·5번째 요소 자식 중 조건 일치 | 같은 태그만 따로 세는 문법 아님 |
| `:not(.c3)` | c3 아닌 대상 | 나머지 선택 조건도 함께 읽음 |
| `::before` / `::after` / `::selection` | 앞뒤 생성 내용 / 선택한 글 표현 | 실제 HTML 자식 추가와 다름 |

> 📚 **출처 · 본문 설명 확인:** [W3C 선택자 — 관계·상태·명시도](https://www.w3.org/TR/selectors-4/). 설명과 비교 표는 수업 원본을 바탕으로 새로 풀어 썼다. 외부 원문을 직접 인용한 문장은 아니다. 확인일: 2026-10-28.

<a id="example"></a>

## 3. 작은 예제로 먼저 이해하기

**새 설명 예제 · 전체 파일.** [실행 파일](실습/책형_복습/01_CSS_선택자와_적용방법.html)을 브라우저로 연다. 이 예제는 위 style 안에 CSS를 모두 넣어 외부 파일 연결이 필요 없다. 원본 CSS에 붙이면 다른 규칙이 섞일 수 있으므로 먼저 별도 파일로 확인한다.

```html
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>01. CSS 선택자와 적용 — 어떤 요소를 어떻게 바꿀까</title>
    <style>
        div strong { color: blue; }
        div > strong { font-size: 24px; }
        input[type=checkbox]:checked + span { text-decoration: line-through; }
    </style>
</head>
<body>
    <h1>선택 조건 관찰</h1>
    <div>
        <strong>바로 아래</strong>
        <p><strong>한 단계 더 안쪽</strong></p>
    </div>
    <label><input type="checkbox"><span>복습 완료</span></label>
</body>
</html>
```

두 strong은 모두 div의 자손이어서 파랑이다. 첫 strong만 직접 자식이므로 24px가 된다. 체크 전에는 취소선 조건이 맞지 않고, 체크하면 바로 다음 span에 취소선이 생긴다. 글자 사이의 줄바꿈 텍스트는 요소 형제가 아니므로 그 자체로 + 관계를 끊지 않는다.

<a id="my-code"></a>

## 4. 내가 작성한 코드를 따라 읽기

아래는 **내 원본 발췌**다. 주석의 표현도 원문대로 두었다. 설명에서 교정한 내용을 원본에 이미 수정한 것처럼 읽지 않는다.

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_html/css/01_selector.html` 89–99행

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

**발췌 바로 풀이:** 동작은 같다. 내 주석의 “몇 단계 아래여도”는 자손과 자식을 구분하는 데 도움이 된다. 다만 CSS의 관계는 코드 들여쓰기가 아니라 실제 요소의 중첩으로 정해진다.

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_html/css/01_selector.html` 117–129행

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

**발췌 바로 풀이:** 실행되는 규칙은 같다. 주석의 `input[type=checkbox]: + span`은 콜론 뒤 상태 이름이 없어 잘못된 선택자다. 지금은 주석이므로 영향이 없지만 그대로 활성화하면 안 된다. 라디오도 `:checked` 상태를 가질 수 있으나, **이 규칙은 type=checkbox로 제한되어 라디오에는 적용되지 않는다.**

첫 발췌는 자손·자식을 ‘몇 단계 아래’와 ‘바로 밑’으로 설명한다. div 안의 a 아래 strong에는 자손 규칙만 맞는 식으로 HTML 관계를 따라 대입한다. 두 번째 발췌의 실행 규칙은 체크박스에만 제한된다. 주석에 radio도 적었지만 선택자의 type=checkbox가 라디오를 제외한다. 주석 처리한 `input[type=checkbox]: + span`은 상태 이름이 빠진 잘못된 선택자이며, 현재는 실행되지 않는다.

<a id="connections"></a>

## 5. 파일·요소·값이 연결되는 흐름

HTML에 class·id·속성·중첩을 작성 → 선택자가 조건을 검사 → 맞는 요소의 해당 속성이 후보가 됨 → 충돌이 있으면 다음 장의 우선순위로 결정된다. class는 여러 요소에 재사용할 수 있고 한 요소에도 여러 항목을 넣을 수 있다. CSS 파일이 존재해도 link 경로가 틀리면 규칙을 불러오지 못한다.

<a id="review"></a>

## 6. 잘한 점·아쉬운 점·개선 방향

**잘한 점:** 내 주석은 자손과 자식의 차이를 처음 읽을 때 이해하기 쉽게 풀었다. **아쉬운 점:** 체크박스 제한과 radio 설명이 섞였다. 주석도 실제 선택 조건에 맞춰 고치는 편이 좋다. **개선 방향:** 상태 실험을 켜고 끌 때는 먼저 문법을 확인하고, 체크 전·후에 어느 요소가 바뀌는지 적는다. 실제 제어가 아닌 생성 글자로 중요한 설명을 대신하는 설계는 별도로 판단한다.

제안은 원본을 수정한 결과가 아니다. **실제 오류**, **관찰을 위한 수업용 단순화**, **목적에 따라 가능한 선택**을 구별한다. 단지 짧게 쓰거나 최신 기능을 쓴다고 더 좋은 코드는 아니다.

<a id="teacher"></a>

## 7. 강사님 코드가 도움이 되는 비교



강사님과 내 실행 규칙은 같다. 중복 원문을 붙여도 새 동작이 늘지 않아 강사님 코드는 재인용하지 않는다. 강사님 주석의 JavaScript 관련 짧은 표현도 언어 전체의 기능 제한으로 외우지 않는다. 본문은 선택 조건과 현재 HTML 구조를 근거로 판단한다.

<a id="results"></a>

## 8. 결과를 예상하고 한 가지 바꾸기

아래는 **명시한 조건에서의 코드 기준 예상**이다. 이번 편집에서 실제 브라우저 렌더링을 재실행했다는 기록과 구별한다. 매 실험은 원래 예제로 돌아가 한 조건만 바꾼다.

| 한 가지 변경 | 예상 | 이유 |
| --- | --- | --- |
| `div > strong`의 >를 공백으로 | 두 strong이 24px | 자손 조건으로 넓어짐 |
| input과 span 사이에 em 추가 | span 취소선 미적용 | 바로 다음 요소는 em |
| type만 radio로 | 해당 취소선 미적용 | checkbox 조건 불일치 |

아무것도 바뀌지 않으면 저장·CSS 연결·선택자 철자·현재 상태 순서로 확인한다. 대상이 선택되지 않은 문제에 !important부터 추가하면 원인을 가리기 쉽다.

<a id="tips"></a>

## 9. 추가로 알면 좋은 것과 출처

> 💡 **TIP · 수업 범위 밖:** :is()·:where()·:has()·:focus-visible, inert·aria-hidden와 접근성 설계 전체는 추가 학습이다. 기본 선택자의 관계·상태를 이해한 뒤 필요할 때 확장한다.

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

이 절의 확장은 기본 문제의 필수 조건이 아니다. 2절의 📚 출처는 배운 기능의 설명을 확인하는 근거이며, 출처가 있다는 이유로 모두 수업 밖 내용인 것은 아니다.

<a id="practice"></a>

## 10. 복습과 빠른 정리

1. div 아래 p 아래 strong은 `div > strong`에 맞는가?
2. 체크박스 다음에 줄바꿈만 있어도 + 관계가 끊기는가?
3. `li.c1.c2`는 두 요소를 고르는가?

<details>
<summary>짧은 풀이 — 먼저 답한 뒤 확인</summary>

직접 자식이 아니므로 첫 조건에 맞지 않는다. 줄바꿈 텍스트는 다음 요소 형제를 바꾸지 않는다. li.c1.c2는 하나의 li가 두 클래스를 모두 갖는 조건이다.

</details>

| 빠른 정리 | 뜻 |
| --- | --- |
| 공백 / > | 자손 / 직접 자식 |
| + | 바로 다음 요소 형제 |
| :checked | 현재 선택 상태 |
| 속성: 값; | 한 선언 |

[장별 연습문제](실습/연습문제/01_CSS_선택자와_적용방법_연습문제.md)에서 예상·설명·수정을 이어 간다. 다음은 [충돌과 상속](01-02_CSS_우선순위와_상속.md)이다.

<!-- 이전 색인 이동 주소 보존 -->
<a id="css-12"></a>
<a id="css-48"></a>
<a id="css-51"></a>
<a id="index-section-80"></a>
<a id="index-section-86"></a>
<a id="index-section-87"></a>
<a id="index-section-94"></a>
<a id="section-1"></a>
<a id="section-2"></a>
<a id="section-3"></a>
<a id="section-4"></a>

이전 절 주소로 왔다면 [이 장의 목차](#chapter-toc)에서 현재 설명을 찾는다.
