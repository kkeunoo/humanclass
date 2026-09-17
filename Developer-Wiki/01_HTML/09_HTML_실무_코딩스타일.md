---
title: HTML 실무 코딩 스타일
version: v4.1-detailed-learning
last_updated: 2026-09-17
status: Completed
---

# HTML 실무 코딩 스타일

## 문서 내 목차

- [개요](#html-1)
- [학습 목표](#html-2)
- [개념에서 실제 동작까지](#html-3)
- [1. 기본 Document 구조는 항상 명확하게 작성한다](#html-4)
- [2. `lang`은 실제 Content 언어에 맞춘다](#html-5)
- [3. `<title>`은 `Document`로 남기지 않는다](#html-6)
- [4. Semantic Element는 역할이 있을 때 사용한다](#html-7)
- [5. 단순 Wrapper에는 `div`가 적합하다](#html-8)
- [6. `section`에는 주제가 있어야 한다](#html-9)
- [7. `article`은 독립 Content Unit에 사용한다](#html-10)
- [8. `main`은 Page의 핵심 Content를 나타낸다](#html-11)
- [9. Navigation에는 Accessible Name을 제공한다](#html-12)
- [10. Navigation Item은 List로 구성할 수 있다](#html-13)
- [11. Heading은 글자 크기가 아니라 구조다](#html-14)
- [12. CSS 때문에 Heading Tag를 바꾸지 않는다](#html-15)
- [13. 일반 Text는 의미 있는 Element로 감싼다](#html-16)
- [14. `<br>`은 Layout 간격이 아니다](#html-17)
- [15. `&nbsp;`로 Layout을 맞추지 않는다](#html-18)
- [16. Link Text는 목적을 드러낸다](#html-19)
- [17. Link와 Button을 구분한다](#html-20)
- [18. `target="_blank"`를 자동으로 사용하지 않는다](#html-21)
- [19. Relative Path는 현재 File 위치 기준으로 계산한다](#html-22)
- [20. 외부 Resource Hotlink를 남용하지 않는다](#html-23)
- [21. Image `alt`는 목적을 기준으로 작성한다](#html-24)
- [22. Link 안 Image는 이동 목적을 설명한다](#html-25)
- [23. Image 크기 Attribute와 CSS 역할을 구분한다](#html-26)
- [24. 모든 Image에 `figure`를 사용하지 않는다](#html-27)
- [25. Video에는 사용자가 제어할 방법을 제공한다](#html-28)
- [26. `iframe`에는 `title`을 제공한다](#html-29)
- [27. List는 항목 관계를 표현한다](#html-30)
- [28. `ol`을 “거의 안 쓰는 Tag”로 생각하지 않는다](#html-31)
- [29. 중첩 List는 부모 `li` 안에 넣는다](#html-32)
- [30. Table은 Data에 사용한다](#html-33)
- [31. Table에 `caption`을 검토한다](#html-34)
- [32. Header Cell에 관계를 명시한다](#html-35)
- [33. Presentational Attribute보다 CSS를 사용한다](#html-36)
- [34. Form Control에는 Label이 필요하다](#html-37)
- [35. `id`, `name`, `class` 역할을 구분한다](#html-38)
- [36. `data-*`는 Custom Data에 사용한다](#html-39)
- [37. ARIA는 Native HTML을 대체하는 도구가 아니다](#html-40)
- [38. `aria-label`을 보이는 Label 대신 남용하지 않는다](#html-41)
- [39. Boolean Attribute는 간결하게 작성한다](#html-42)
- [40. Unknown Attribute 오타를 방치하지 않는다](#html-43)
- [41. `button`의 `type`을 명시한다](#html-44)
- [42. Radio Group은 `name`으로 묶는다](#html-45)
- [43. Checkbox에는 의미 있는 `value`를 작성한다](#html-46)
- [44. `fieldset`과 `legend`로 Form Group을 묶는다](#html-47)
- [45. GET과 POST를 보안 Level처럼 구분하지 않는다](#html-48)
- [46. Form은 Server Validation을 전제로 한다](#html-49)
- [47. HTML 안에 비밀 정보를 Comment로 남기지 않는다](#html-50)
- [48. Comment는 “무엇”보다 “왜”를 설명한다](#html-51)
- [49. 개인 복원 메모는 Code와 분리한다](#html-52)
- [50. Inline Style을 기본 방식으로 사용하지 않는다](#html-53)
- [51. JavaScript Hook과 Style Class를 구분할 수 있다](#html-54)
- [52. Class 이름은 의미와 역할을 표현한다](#html-55)
- [53. ID 이름도 목적을 드러낸다](#html-56)
- [54. 한 Element에 같은 ID를 반복하지 않는다](#html-57)
- [55. 잘못된 중첩은 Browser가 자동 보정할 수 있다](#html-58)
- [56. Void Element에는 종료 Tag가 없다](#html-59)
- [57. Tag 이름과 Attribute는 소문자로 통일한다](#html-60)
- [58. Attribute 값에는 일관된 따옴표를 사용한다](#html-61)
- [59. Attribute가 많으면 여러 줄로 작성한다](#html-62)
- [60. HTML 구조와 Visual Order를 다르게 만들지 않는다](#html-63)
- [61. Mobile Menu도 DOM 순서를 유지한다](#html-64)
- [62. Hidden 상태를 Markup 목적과 함께 관리한다](#html-65)
- [63. `aria-expanded`와 실제 상태를 일치시킨다](#html-66)
- [64. Form Error는 연결해서 제공한다](#html-67)
- [65. 날짜·시간 Data에는 `time`을 사용할 수 있다](#html-68)
- [66. 약어에는 필요한 경우 `abbr`을 사용한다](#html-69)
- [67. Download는 실제 Download Resource에 사용한다](#html-70)
- [68. HTML File 이름은 의미 있게 작성한다](#html-71)
- [69. Asset File 이름도 일관되게 작성한다](#html-72)
- [70. 실제 개선 사례 1: 일반 Text](#html-73)
- [71. 실제 개선 사례 2: 존재하지 않는 Heading](#html-74)
- [72. 실제 개선 사례 3: 사용자 정의 Tag](#html-75)
- [73. 실제 개선 사례 4: 내부 Link 경로](#html-76)
- [74. 실제 개선 사례 5: Root Relative와 Absolute URL](#html-77)
- [75. 실제 개선 사례 6: List](#html-78)
- [76. 실제 개선 사례 7: Table `summary`](#html-79)
- [77. 실제 개선 사례 8: 잘못 닫힌 Table Cell](#html-80)
- [78. 실제 개선 사례 9: Image 비율](#html-81)
- [79. 실제 개선 사례 10: Form Submit Attribute](#html-82)
- [80. 실제 개선 사례 11: Radio 중복 선택](#html-83)
- [81. 실제 개선 사례 12: Textarea 내부 Tag](#html-84)
- [82. 실제 개선 사례 13: POST 오해](#html-85)
- [83. 실제 개선 사례 14: Semantic Page 구조](#html-86)
- [84. 실무형 Page 골격 예제](#html-87)
- [85. 실무 검수 순서](#html-88)
- [86. 자주 하는 실수](#html-89)
- [87. HTML Validator 활용](#html-90)
- [88. DevTools에서 확인할 항목](#html-91)
- [89. 접근성 검수 기준](#html-92)
- [90. 코드 리뷰 기준](#html-93)
- [91. 최종 체크리스트](#html-94)
- [92. 핵심 요약](#html-95)
- [마무리](#html-96)
- [브라우저 해석 복습 카드 — 유효하고 읽히며 접근 가능한 마크업](#html-97)



### 문서 정보

| 항목 | 내용 |
| --- | --- |
| 문서 | `09_HTML_실무_코딩스타일.md` |
| 분류 | `01_HTML` |
| 문서 성격 | HTML 실무 작성·리팩토링 기준 문서 |
| 핵심 범위 | Semantic 구조, Heading, Link·Button, List, Table, Media, Form, 접근성, 네이밍, 주석, 검수 |
| 예제 형식 | Before → After → 개선 이유 → 실무 선택 기준 |
| 종합실습 | 별도 문서 `10_HTML_종합실습.md`에서 관리 |
| 문서 형식 | HTML Developer-Wiki 상세 동작 학습판 |

> 이 문서는 새로운 HTML Tag를 추가로 외우는 문서가 아니다.  
> HTML 01~08에서 학습한 Document Structure, Text, Link, List, Table, Media, Form, Semantic Element를 **실제 Project에서는 어떤 기준으로 선택하고 조합하는지** 설명한다.

---

<a id="html-1"></a>

## 개요

HTML이 Browser에 표시된다고 해서 좋은 Markup은 아니다.

다음 두 코드는 화면상 비슷하게 보일 수 있다.

```html
<div class="title">
    공지사항
</div>
```

```html
<h2>
    공지사항
</h2>
```

하지만 의미는 다르다.

```text
div.title
→ 모양과 Class만 존재

h2
→ 문서 구조상 제목이라는 의미 전달
```

실무 HTML은 다음 질문을 반복해서 확인한다.

```text
이 Element가 Content의 역할을 정확히 표현하는가?
    ↓
Heading 구조가 Page의 정보 계층을 반영하는가?
    ↓
Link와 Button의 역할이 구분되는가?
    ↓
Image·Form·Table에 필요한 접근성 정보가 있는가?
    ↓
CSS와 JavaScript가 없어도 읽는 순서가 자연스러운가?
    ↓
Browser·Screen Reader·검색 엔진이 구조를 이해할 수 있는가?
```

> [!IMPORTANT]
> HTML 실무 코딩 스타일의 목적은 Semantic Tag를 많이 사용하는 것이 아니다.
>
> **Content의 의미를 정확히 표현하고, 접근 가능하며, CSS와 JavaScript가 안정적으로 연결될 수 있는 문서 구조**를 만드는 것이 목적이다.

---

<a id="html-2"></a>

## 학습 목표

- 주요 요소와 속성의 의미·차이를 설명한다.
- 입력부터 브라우저 처리와 결과까지 추적한다.
- 원본 코드를 비교하고 오류를 재현·수정한다.

<a id="learning-flow"></a>

### 개발자 도구에서 값을 읽고 확인하기

03_상대주소/03_a.html을 실제 브라우저에서 연 상태에서 개발자 도구의 Console에 다음을 입력합니다. 아래 코드는 HTML에 삽입할 태그가 아니라 브라우저의 JavaScript 확인 명령입니다. 💡 DOM·폼 API를 이용한 확인법으로, JavaScript 과정에서 더 자세히 배웁니다.

```javascript
new URL('01_hello.html', location.href).pathname
```

**예상 결과:** /03_%EC%83%81%EB%8C%80%EC%A3%BC%EC%86%8C/01_hello.html

decodeURIComponent로 감싸면 /03_상대주소/01_hello.html로 읽을 수 있습니다. 소스가 깔끔해 보여도 목적지는 잘못될 수 있습니다. 이 결과는 서버 루트에 03_상대주소 폴더가 있을 때를 가정합니다. HTML은 Python의 print가 없으므로 화면 결과와 Console에서 읽은 값을 분리해 확인합니다. 오류가 나면 명령을 입력한 페이지가 맞는지, 해당 요소가 실제로 있는지, 입력을 먼저 했는지 확인합니다.


<a id="html-3"></a>

## 개념에서 실제 동작까지

### 먼저 이해하기: 코딩 스타일은 오류를 찾기 위한 규칙이다

들여쓰기·이름·따옴표를 통일하는 이유는 예쁘게 보이기 위해서만이 아닙니다. 태그의 부모·자식 관계와 연결 대상을 빨리 읽고 실수를 줄이기 위해서입니다. 정렬했다고 잘못된 태그나 전송 설정이 자동 수정되지는 않습니다.

내 03_a.html의 수업 발췌:

```html
<a href="01_hello.html" target="_blank">01_hello.html</a>
```

이 한 줄은 들여쓰기가 정상이어도 하위 폴더의 현재 문서를 기준으로 잘못된 목적지를 계산할 수 있습니다. 두 원본에 같은 링크가 있으므로 내 코드만의 오류라고 분류하지 않습니다. 개선 코드는 ../01_hello.html이며, 개선 근거는 디스크에서의 상대 위치와 실제 URL입니다.

검수 순서는 문법→구조→연결→동작→접근성→표현입니다. 문법 검사 통과가 사용 가능한 페이지를 보장하지 않고, 브라우저에서 “보인다”가 올바른 문법을 보장하지도 않습니다.

| 검수 | 질문 | 확인 방법 |
| --- | --- | --- |
| 문법 | 종료 태그·따옴표가 맞는가? | 소스와 Validator |
| 구조 | 제목·목록·표가 올바르게 묶였는가? | Elements와 목차 |
| 연결 | href/src/for 대상이 있는가? | 계산된 URL·id |
| 동작 | 클릭·입력·전송 결과가 의도와 같은가? | 실제 조작·Network |
| 접근성 | 이름·키보드 조작·대체 정보가 있는가? | label·alt·Tab 검사 |

수업의 value123="전송"은 value가 아닙니다. 형식이 속성처럼 보이고 화면에서 큰 오류가 나지 않아도 버튼 표시값 기능을 하지 않습니다. 속성 오타를 브라우저가 내가 원하는 것으로 알아서 해석한다고 기대하지 않습니다.

💡 알아두면 좋은 점: 자동 포맷터는 일관된 배치를 돕고 Validator는 규격 문제를 찾습니다. 링크 목적의 적절성, 개인정보의 불필요한 노출, 학습자의 이해 여부는 사람이 추가 검토해야 합니다.

**확인 문제:** 모든 태그 이름을 소문자로 바꾸면 name 없는 입력의 전송 문제가 해결되는가? 아니요. 작성 스타일과 폼의 의미·동작 조건은 다른 검토 항목입니다.


<a id="html-4"></a>

## 1. 기본 Document 구조는 항상 명확하게 작성한다

### 1.1 Before

```html
<html>
<body>
내용
</body>
</html>
```

### 1.2 After

```html
<!doctype html>
<html lang="ko">
    <head>
        <meta charset="UTF-8">

        <meta
            name="viewport"
            content="width=device-width, initial-scale=1.0"
        >

        <title>
            Developer Academy
        </title>
    </head>

    <body>
        ...
    </body>
</html>
```

### 1.3 실무 기준

```text
doctype
→ Standards Mode

lang
→ 문서 주 언어

charset
→ 문자 인코딩

viewport
→ Mobile Viewport

title
→ Browser Tab·Bookmark·검색 결과에 사용되는 문서 제목
```

---

<a id="html-5"></a>

## 2. `lang`은 실제 Content 언어에 맞춘다

### 2.1 Before

```html
<html lang="en">
```

한국어 Page라면 Language 정보가 맞지 않는다.

### 2.2 After

```html
<html lang="ko">
```

일부 구간만 다른 언어라면 해당 Element에 별도로 지정할 수 있다.

```html
<p>
    CSS의
    <span lang="en">
        Cascade
    </span>
    개념을 학습합니다.
</p>
```

---

<a id="html-6"></a>

## 3. `<title>`은 `Document`로 남기지 않는다

### 3.1 Before

```html
<title>Document</title>
```

### 3.2 After

```html
<title>
    HTML 강의 목록 | Developer Academy
</title>
```

Page마다 목적이 구분되는 제목을 작성한다.

---

<a id="html-7"></a>

## 4. Semantic Element는 역할이 있을 때 사용한다

```text
header
→ 머리말

nav
→ 주요 Navigation

main
→ Page 핵심 Content

section
→ 하나의 주제 영역

article
→ 독립적인 Content Unit

aside
→ 보조 Content

footer
→ 바닥글·마무리 정보
```

Semantic Element를 많이 사용하는 것 자체가 목표는 아니다.

---

<a id="html-8"></a>

## 5. 단순 Wrapper에는 `div`가 적합하다

### 5.1 Before

```html
<section class="card-grid">
    ...
</section>
```

단순 Grid Wrapper인데 독립 주제도 Heading도 없다.

### 5.2 After

```html
<div class="card-grid">
    ...
</div>
```

의미가 없는 Layout Group에는 `div`를 사용한다.

---

<a id="html-9"></a>

## 6. `section`에는 주제가 있어야 한다

```html
<section aria-labelledby="course-title">
    <h2 id="course-title">
        추천 과정
    </h2>

    ...
</section>
```

`section`을 단순 Style Box처럼 사용하지 않는다.

---

<a id="html-10"></a>

## 7. `article`은 독립 Content Unit에 사용한다

```html
<article class="news-card">
    <h2>
        HTML 접근성 개선 가이드
    </h2>

    <p>
        Semantic Markup과 Form Label을
        점검하는 방법을 정리합니다.
    </p>
</article>
```

Blog Post, News, Review, Comment, Product Card처럼 독립적으로 배포·재사용 가능한 Content에 적합하다.

---

<a id="html-11"></a>

## 8. `main`은 Page의 핵심 Content를 나타낸다

```html
<body>
    <header>
        ...
    </header>

    <main>
        ...
    </main>

    <footer>
        ...
    </footer>
</body>
```

`main` 안에 다른 `main`을 중첩하지 않는다.

---

<a id="html-12"></a>

## 9. Navigation에는 Accessible Name을 제공한다

Navigation이 하나뿐이고 목적이 명확하면 단순 `nav`도 사용할 수 있다.

여러 Navigation이 있다면 구분한다.

```html
<nav aria-label="주요 메뉴">
    ...
</nav>

<nav aria-label="Footer 메뉴">
    ...
</nav>
```

보이는 Heading이 있다면 `aria-labelledby`를 사용할 수 있다.

---

<a id="html-13"></a>

## 10. Navigation Item은 List로 구성할 수 있다

```html
<nav aria-label="주요 메뉴">
    <ul>
        <li>
            <a href="./html.html">
                HTML
            </a>
        </li>

        <li>
            <a href="./css.html">
                CSS
            </a>
        </li>
    </ul>
</nav>
```

Menu가 항목 집합이라는 의미를 함께 전달할 수 있다.

---

<a id="html-14"></a>

## 11. Heading은 글자 크기가 아니라 구조다

### 11.1 Before

```html
<h1>Page 제목</h1>
<h4>첫 번째 Section</h4>
<h2>세부 제목</h2>
```

### 11.2 After

```html
<h1>Page 제목</h1>

<section>
    <h2>첫 번째 Section</h2>

    <h3>세부 제목</h3>
</section>
```

Heading Level은 Content 계층을 반영한다.

---

<a id="html-15"></a>

## 12. CSS 때문에 Heading Tag를 바꾸지 않는다

### 12.1 Before

```html
<h4>
    큰 제목
</h4>
```

“기본 글씨 크기가 마음에 든다”는 이유로 Level을 선택하지 않는다.

### 12.2 After

```html
<h2 class="section-title">
    큰 제목
</h2>
```

```css
.section-title {
    font-size: 2rem;
}
```

Meaning은 HTML, Appearance는 CSS가 담당한다.

---

<a id="html-16"></a>

## 13. 일반 Text는 의미 있는 Element로 감싼다

### 13.1 Before

```html
안녕하세요.
HTML 강의입니다.
```

### 13.2 After

```html
<p>
    안녕하세요.
    HTML 강의입니다.
</p>
```

문단, Heading, List Item 등 Content 역할에 맞는 Element를 사용한다.

---

<a id="html-17"></a>

## 14. `<br>`은 Layout 간격이 아니다

### 14.1 Before

```html
<p>첫 번째 Content</p>
<br><br><br>
<p>두 번째 Content</p>
```

### 14.2 After

```html
<div class="content-list">
    <p>첫 번째 Content</p>
    <p>두 번째 Content</p>
</div>
```

CSS:

```css
.content-list {
    display: grid;
    gap: 2rem;
}
```

`br`은 Address·Poem처럼 줄바꿈 자체에 의미가 있을 때 사용한다.

---

<a id="html-18"></a>

## 15. `&nbsp;`로 Layout을 맞추지 않는다

### 15.1 Before

```html
이름&nbsp;&nbsp;&nbsp;&nbsp;홍길동
```

### 15.2 After

```html
<dl class="profile-info">
    <dt>이름</dt>
    <dd>홍길동</dd>
</dl>
```

간격은 CSS로 처리한다.

---

<a id="html-19"></a>

## 16. Link Text는 목적을 드러낸다

### 16.1 Before

```html
<a href="./detail.html">
    클릭
</a>
```

### 16.2 After

```html
<a href="./detail.html">
    HTML 과정 자세히 보기
</a>
```

Link만 읽어도 이동 목적을 이해할 수 있어야 한다.

---

<a id="html-20"></a>

## 17. Link와 Button을 구분한다

```text
다른 URL·Page·Fragment 이동
→ a

현재 Page의 상태 변경·기능 실행
→ button
```

### 17.1 Before

```html
<a href="#">
    Modal 열기
</a>
```

### 17.2 After

```html
<button type="button">
    Modal 열기
</button>
```

---

<a id="html-21"></a>

## 18. `target="_blank"`를 자동으로 사용하지 않는다

새 Tab이 실제 UX 요구사항인지 확인한다.

```html
<a
    href="https://example.com/"
    target="_blank"
    rel="noopener"
>
    외부 문서 보기
</a>
```

새 Tab이 열리는 사실을 사용자에게 알려야 하는 상황도 검토한다.

---

<a id="html-22"></a>

## 19. Relative Path는 현재 File 위치 기준으로 계산한다

```text
project/
├── index.html
├── pages/
│   └── detail.html
└── images/
    └── logo.png
```

`pages/detail.html` 기준:

```html
<img
    src="../images/logo.png"
    alt="Developer Academy"
>
```

현재 File 위치를 기준으로 한 단계씩 계산한다.

---

<a id="html-23"></a>

## 20. 외부 Resource Hotlink를 남용하지 않는다

### 20.1 Before

```html
<img
    src="https://other-site.example/image.jpg"
    alt="상품"
>
```

### 20.2 실무 기준

다음을 검토한다.

```text
사용 권한
외부 Site 변경·삭제
Hotlink 차단
Network Latency
Cache 제어
CSP
```

가능하면 Project가 관리하는 Storage·CDN을 사용한다.

---

<a id="html-24"></a>

## 21. Image `alt`는 목적을 기준으로 작성한다

### 21.1 정보성 Image

```html
<img
    src="./images/dashboard.webp"
    alt="교육 과정별 진행률을 보여 주는 대시보드"
>
```

### 21.2 장식용 Image

```html
<img
    src="./images/decorative-line.svg"
    alt=""
>
```

### 21.3 좋지 않은 예

```html
<img
    src="./images/photo.jpg"
    alt="이미지"
>
```

---

<a id="html-25"></a>

## 22. Link 안 Image는 이동 목적을 설명한다

```html
<a href="./course/html.html">
    <img
        src="./images/html-course.webp"
        alt="HTML 과정 자세히 보기"
    >
</a>
```

Image 외에 Link Text가 이미 있다면 중복을 피할 수 있다.

```html
<a href="./course/html.html">
    <img
        src="./images/html-icon.svg"
        alt=""
    >

    <span>
        HTML 과정 자세히 보기
    </span>
</a>
```

---

<a id="html-26"></a>

## 23. Image 크기 Attribute와 CSS 역할을 구분한다

```html
<img
    src="./images/course.webp"
    alt="HTML 과정 미리보기"
    width="800"
    height="450"
    class="course-image"
>
```

```css
.course-image {
    max-width: 100%;
    height: auto;
}
```

HTML Attribute는 Image 비율과 Layout 공간 확보에 도움을 주고, 표시 크기는 CSS에서 유연하게 조절한다.

---

<a id="html-27"></a>

## 24. 모든 Image에 `figure`를 사용하지 않는다

Caption 관계가 실제로 있을 때 사용한다.

```html
<figure>
    <img
        src="./images/result.webp"
        alt="최종 프로젝트 화면"
    >

    <figcaption>
        반응형 교육 과정 Dashboard
    </figcaption>
</figure>
```

---

<a id="html-28"></a>

## 25. Video에는 사용자가 제어할 방법을 제공한다

```html
<video controls>
    <source
        src="./media/lesson.webm"
        type="video/webm"
    >

    <source
        src="./media/lesson.mp4"
        type="video/mp4"
    >

    Browser가 Video를 지원하지 않습니다.
</video>
```

자동 재생을 기본으로 가정하지 않는다.

---

<a id="html-29"></a>

## 26. `iframe`에는 `title`을 제공한다

```html
<iframe
    src="https://www.youtube.com/embed/..."
    title="HTML Semantic 구조 강의 영상"
    loading="lazy"
    allowfullscreen
></iframe>
```

Embed 대상 Site가 `X-Frame-Options` 또는 CSP로 삽입을 제한할 수 있다.

---

<a id="html-30"></a>

## 27. List는 항목 관계를 표현한다

```text
순서 중요하지 않음
→ ul

순서 중요
→ ol

이름·설명 관계
→ dl
```

화면 Marker 모양 때문에 Element를 선택하지 않는다.

---

<a id="html-31"></a>

## 28. `ol`을 “거의 안 쓰는 Tag”로 생각하지 않는다

절차·순위·레시피·설치 단계에는 자연스럽다.

```html
<ol>
    <li>프로젝트 Clone</li>
    <li>Dependency 설치</li>
    <li>Development Server 실행</li>
</ol>
```

---

<a id="html-32"></a>

## 29. 중첩 List는 부모 `li` 안에 넣는다

```html
<ul>
    <li>
        Frontend

        <ul>
            <li>HTML</li>
            <li>CSS</li>
        </ul>
    </li>
</ul>
```

List 계층이 명확해진다.

---

<a id="html-33"></a>

## 30. Table은 Data에 사용한다

### 30.1 Before

```html
<table>
    <tr>
        <td>Logo</td>
        <td>Menu</td>
    </tr>
</table>
```

Page Layout 용도로 사용하지 않는다.

### 30.2 After

```html
<header class="site-header">
    ...
</header>
```

Layout은 CSS Flexbox·Grid가 담당한다.

---

<a id="html-34"></a>

## 31. Table에 `caption`을 검토한다

```html
<table>
    <caption>
        2026년 월별 수강 인원
    </caption>

    ...
</table>
```

Table만 보아도 어떤 Data인지 이해할 수 있게 한다.

---

<a id="html-35"></a>

## 32. Header Cell에 관계를 명시한다

```html
<table>
    <thead>
        <tr>
            <th scope="col">
                과정
            </th>
            <th scope="col">
                수강생
            </th>
        </tr>
    </thead>

    <tbody>
        <tr>
            <th scope="row">
                HTML
            </th>
            <td>32명</td>
        </tr>
    </tbody>
</table>
```

---

<a id="html-36"></a>

## 33. Presentational Attribute보다 CSS를 사용한다

### 33.1 Before

```html
<table
    border="1"
    width="800"
>
```

### 33.2 After

```html
<table class="data-table">
```

```css
.data-table {
    width: 100%;
    border-collapse: collapse;
}
```

HTML은 Data 구조, CSS는 시각 표현을 담당한다.

---

<a id="html-37"></a>

## 34. Form Control에는 Label이 필요하다

### 34.1 Before

```html
<input
    type="email"
    placeholder="Email"
>
```

### 34.2 After

```html
<label for="email">
    Email
</label>

<input
    type="email"
    id="email"
    name="email"
    autocomplete="email"
>
```

Placeholder는 Label이 아니다.

---

<a id="html-38"></a>

## 35. `id`, `name`, `class` 역할을 구분한다

```text
id
→ Document 내 식별
→ label·Fragment·ARIA 연결

name
→ Form 제출 Key

class
→ CSS·JavaScript에서 재사용 가능한 Group
```

```html
<label for="user-email">
    Email
</label>

<input
    type="email"
    id="user-email"
    name="email"
    class="form-control"
>
```

---

<a id="html-39"></a>

## 36. `data-*`는 Custom Data에 사용한다

```html
<button
    type="button"
    data-course-id="html-01"
>
    과정 선택
</button>
```

Style 상태를 모두 `data-*`로 만들 필요는 없다. 실제 Application 상태와 팀 규칙을 기준으로 사용한다.

---

<a id="html-40"></a>

## 37. ARIA는 Native HTML을 대체하는 도구가 아니다

### 37.1 Before

```html
<div
    role="button"
    tabindex="0"
>
    저장
</div>
```

### 37.2 After

```html
<button type="button">
    저장
</button>
```

Native Element가 제공하는 Keyboard·Focus·Accessibility 동작을 먼저 사용한다.

---

<a id="html-41"></a>

## 38. `aria-label`을 보이는 Label 대신 남용하지 않는다

### 38.1 적절한 예

```html
<button
    type="button"
    aria-label="메뉴 닫기"
>
    ×
</button>
```

Icon-only Button처럼 화면 Text가 없을 때 유용하다.

Form Label을 숨기기 위해 무조건 `aria-label`만 사용하는 방식은 신중하게 선택한다.

---

<a id="html-42"></a>

## 39. Boolean Attribute는 간결하게 작성한다

다음은 모두 Boolean Attribute다.

```html
<input required>
<input disabled>
<input checked>

<select multiple>
```

다음처럼 반복 값을 쓸 필요는 없다.

```html
<input required="required">
```

둘 다 동작하지만 간결한 형식을 일관되게 사용한다.

---

<a id="html-43"></a>

## 40. Unknown Attribute 오타를 방치하지 않는다

### 40.1 Before

```html
<input
    type="submit"
    value123="전송"
>
```

Browser가 Attribute를 DOM에 유지해도 Submit Label 기능이 생기는 것은 아니다.

### 40.2 After

```html
<input
    type="submit"
    value="전송"
>
```

HTML Validator와 DevTools로 오타를 확인한다.

---

<a id="html-44"></a>

## 41. `button`의 `type`을 명시한다

Form 내부의 Button은 기본적으로 Submit 동작을 할 수 있다.

```html
<button type="button">
    주소 검색
</button>

<button type="submit">
    회원가입
</button>
```

의도를 명확히 한다.

---

<a id="html-45"></a>

## 42. Radio Group은 `name`으로 묶는다

```html
<label>
    <input
        type="radio"
        name="gender"
        value="female"
    >
    여자
</label>

<label>
    <input
        type="radio"
        name="gender"
        value="male"
    >
    남자
</label>
```

같은 Group에 기본 `checked`를 여러 개 작성하지 않는다.

---

<a id="html-46"></a>

## 43. Checkbox에는 의미 있는 `value`를 작성한다

```html
<label>
    <input
        type="checkbox"
        name="option"
        value="shot"
    >
    Shot 추가
</label>
```

`value`를 생략하면 기본 `"on"` 값이 제출될 수 있다.

---

<a id="html-47"></a>

## 44. `fieldset`과 `legend`로 Form Group을 묶는다

```html
<fieldset>
    <legend>
        연락 방법
    </legend>

    <label>
        <input
            type="radio"
            name="contact"
            value="email"
        >
        Email
    </label>

    <label>
        <input
            type="radio"
            name="contact"
            value="phone"
        >
        전화
    </label>
</fieldset>
```

관련 Control Group의 의미를 전달한다.

---

<a id="html-48"></a>

## 45. GET과 POST를 보안 Level처럼 구분하지 않는다

```text
GET
→ Query String

POST
→ Request Body

HTTPS
→ 전송 구간 암호화
```

POST라고 해서 자동으로 안전한 것은 아니다.

Password·개인정보 전송에는 HTTPS와 Server Validation이 필요하다.

---

<a id="html-49"></a>

## 46. Form은 Server Validation을 전제로 한다

HTML Constraint Validation은 사용자 경험에 유용하지만 보안 검증의 최종 단계가 아니다.

```html
<input
    type="email"
    name="email"
    required
>
```

Server에서도 Type·Length·Allowed Value를 다시 검증한다.

---

<a id="html-50"></a>

## 47. HTML 안에 비밀 정보를 Comment로 남기지 않는다

### 47.1 Before

```html
<!-- 관리자 비밀번호: admin1234 -->
```

HTML Comment는 Browser Source에서 확인할 수 있다.

Password, API Key, Token, 개인 정보, 내부 URL 같은 민감 정보는 작성하지 않는다.

---

<a id="html-51"></a>

## 48. Comment는 “무엇”보다 “왜”를 설명한다

### 48.1 좋지 않은 Comment

```html
<!-- 메뉴 -->
<nav>
```

### 48.2 더 나은 Comment

```html
<!-- Mobile에서도 같은 DOM 순서를 유지해
     Keyboard Focus 순서가 바뀌지 않도록 한다. -->
<nav>
```

Code만 보아도 알 수 있는 내용을 반복하지 않는다.

---

<a id="html-52"></a>

## 49. 개인 복원 메모는 Code와 분리한다

### 49.1 Before

```html
<!-- 0723_HTML_form/label_restore -->
```

작업 이력은 Git Commit, Issue, Changelog 등으로 관리하는 편이 Project Code 집중도를 높인다.

---

<a id="html-53"></a>

## 50. Inline Style을 기본 방식으로 사용하지 않는다

### 50.1 Before

```html
<div
    style="margin-top: 20px; color: blue;"
>
    내용
</div>
```

### 50.2 After

```html
<div class="notice">
    내용
</div>
```

CSS:

```css
.notice {
    margin-top: 1.25rem;
    color: blue;
}
```

동적으로 계산되는 값 등 명확한 이유가 있을 때만 Inline Style을 검토한다.

---

<a id="html-54"></a>

## 51. JavaScript Hook과 Style Class를 구분할 수 있다

Project 규칙에 따라 JavaScript Hook을 별도 Attribute로 분리할 수 있다.

```html
<button
    type="button"
    class="button button--primary"
    data-action="open-modal"
>
    Modal 열기
</button>
```

```text
class
→ Style

data-action
→ JavaScript Behavior
```

팀 규칙이 있다면 일관되게 따른다.

---

<a id="html-55"></a>

## 52. Class 이름은 의미와 역할을 표현한다

### 52.1 Before

```html
<div class="red-box">
```

### 52.2 After

```html
<div class="alert alert--danger">
```

색상보다 Component 역할과 상태를 표현한다.

---

<a id="html-56"></a>

## 53. ID 이름도 목적을 드러낸다

### 53.1 Before

```html
<section id="box1">
```

### 53.2 After

```html
<section
    id="course-overview"
    aria-labelledby="course-overview-title"
>
    <h2 id="course-overview-title">
        과정 소개
    </h2>
</section>
```

Fragment와 ARIA 연결을 읽기 쉬워진다.

---

<a id="html-57"></a>

## 54. 한 Element에 같은 ID를 반복하지 않는다

```html
<!-- 잘못된 예 -->
<input id="email">
<input id="email">
```

ID는 Document 내에서 고유해야 한다.

Label·ARIA·Fragment 연결 오류를 줄이기 위해 Validator로 확인한다.

---

<a id="html-58"></a>

## 55. 잘못된 중첩은 Browser가 자동 보정할 수 있다

### 55.1 Before

```html
<p>
    문단
    <div>
        Box
    </div>
</p>
```

Browser는 DOM을 작성한 코드와 다르게 보정할 수 있다.

### 55.2 After

```html
<div>
    <p>
        문단
    </p>
</div>
```

CSS 문제가 이상해 보이면 실제 DOM Structure도 확인한다.

---

<a id="html-59"></a>

## 56. Void Element에는 종료 Tag가 없다

대표 예:

```html
<img
    src="./image.png"
    alt=""
>

<input type="text">

<br>

<hr>

<meta charset="UTF-8">

<link
    rel="stylesheet"
    href="./style.css"
>
```

HTML에서는 별도 Closing Tag를 작성하지 않는다.

---

<a id="html-60"></a>

## 57. Tag 이름과 Attribute는 소문자로 통일한다

### 57.1 Before

```html
<Pre>
    Content
</Pre>
```

### 57.2 After

```html
<pre>
    Content
</pre>
```

HTML이 대소문자를 엄격히 구분하지 않는 경우에도 Project Style을 일관되게 유지한다.

---

<a id="html-61"></a>

## 58. Attribute 값에는 일관된 따옴표를 사용한다

```html
<a
    href="./detail.html"
    class="detail-link"
>
    자세히 보기
</a>
```

큰따옴표를 Project 기본 규칙으로 정했다면 전체 문서에서 일관되게 사용한다.

---

<a id="html-62"></a>

## 59. Attribute가 많으면 여러 줄로 작성한다

### 59.1 Before

```html
<input type="email" id="email" name="email" autocomplete="email" required class="form-control">
```

### 59.2 After

```html
<input
    type="email"
    id="email"
    name="email"
    autocomplete="email"
    required
    class="form-control"
>
```

Diff와 Review가 쉬워진다.

---

<a id="html-63"></a>

## 60. HTML 구조와 Visual Order를 다르게 만들지 않는다

CSS `order`, Grid Placement, Absolute Position으로 화면 순서를 크게 바꾸면 DOM Reading Order와 차이가 생길 수 있다.

```text
DOM
→ 제목
→ 설명
→ Button
```

화면도 가능한 한 같은 순서를 유지한다.

---

<a id="html-64"></a>

## 61. Mobile Menu도 DOM 순서를 유지한다

Desktop과 Mobile용 Menu를 중복 Markup으로 두 개 만들기보다 같은 Navigation을 CSS와 JavaScript로 상태만 변경하는 방식을 우선 검토한다.

중복 DOM은 다음 문제를 만들 수 있다.

```text
중복 Link
중복 ID
Screen Reader 중복 노출
Focus 관리 복잡
유지보수 증가
```

---

<a id="html-65"></a>

## 62. Hidden 상태를 Markup 목적과 함께 관리한다

```html
<div
    id="mobile-menu"
    hidden
>
    ...
</div>
```

JavaScript:

```javascript
menu.hidden = !isOpen
```

Animation이 필요하면 CSS 상태 Class·ARIA와 함께 설계한다.

---

<a id="html-66"></a>

## 63. `aria-expanded`와 실제 상태를 일치시킨다

```html
<button
    type="button"
    aria-expanded="false"
    aria-controls="mobile-menu"
>
    메뉴
</button>
```

Open 상태:

```html
<button
    type="button"
    aria-expanded="true"
    aria-controls="mobile-menu"
>
    메뉴
</button>
```

ARIA 값만 바꾸고 실제 UI 상태가 그대로이면 안 된다.

---

<a id="html-67"></a>

## 64. Form Error는 연결해서 제공한다

```html
<label for="password">
    Password
</label>

<input
    type="password"
    id="password"
    name="password"
    aria-describedby="password-help password-error"
>

<p id="password-help">
    8자 이상 입력하세요.
</p>

<p
    id="password-error"
    role="alert"
>
    Password가 너무 짧습니다.
</p>
```

실제 Error 발생 시 상태에 맞게 노출한다.

---

<a id="html-68"></a>

## 65. 날짜·시간 Data에는 `time`을 사용할 수 있다

```html
<time datetime="2026-08-07">
    2026년 8월 7일
</time>
```

Machine-readable 값을 함께 제공한다.

---

<a id="html-69"></a>

## 66. 약어에는 필요한 경우 `abbr`을 사용한다

```html
<abbr title="HyperText Markup Language">
    HTML
</abbr>
```

모든 약어에 무조건 사용할 필요는 없지만 문맥상 설명이 필요한 경우 유용하다.

---

<a id="html-70"></a>

## 67. Download는 실제 Download Resource에 사용한다

```html
<a
    href="./files/html-guide.pdf"
    download
>
    HTML Guide PDF 받기
</a>
```

Server Header나 Cross-origin Resource에 따라 Browser 동작이 달라질 수 있다.

---

<a id="html-71"></a>

## 68. HTML File 이름은 의미 있게 작성한다

### 68.1 Before

```text
page1.html
new2.html
test-final-final.html
```

### 68.2 After

```text
index.html
course-detail.html
login.html
dashboard.html
```

URL과 File 역할을 이해하기 쉬워진다.

---

<a id="html-72"></a>

## 69. Asset File 이름도 일관되게 작성한다

### 69.1 Before

```text
Spongebob-Christmas-PNG-Picture.png
최종최종이미지.png
```

### 69.2 After

```text
spongebob-christmas.png
course-dashboard.webp
```

Case-sensitive Server 환경과 URL 관리도 고려한다.

---

<a id="html-73"></a>

## 70. 실제 개선 사례 1: 일반 Text

### 70.1 Before

```html
안녕하세요
```

### 70.2 After

```html
<p>
    안녕하세요.
</p>
```

---

<a id="html-74"></a>

## 71. 실제 개선 사례 2: 존재하지 않는 Heading

### 71.1 Before

```html
<h7>
    세부 제목
</h7>
```

### 71.2 After

```html
<h3>
    세부 제목
</h3>
```

HTML Heading은 `h1`~`h6`이다.

---

<a id="html-75"></a>

## 72. 실제 개선 사례 3: 사용자 정의 Tag

### 72.1 Before

```html
<jeong>
    Content
</jeong>
```

### 72.2 After

일반 구조라면 표준 Element:

```html
<div class="profile">
    Content
</div>
```

실제 Web Component라면 Hyphen을 포함한 Custom Element 이름을 사용한다.

```html
<user-profile></user-profile>
```

---

<a id="html-76"></a>

## 73. 실제 개선 사례 4: 내부 Link 경로

### 73.1 Before

현재 File이 하위 Folder에 있는데:

```html
<a href="01_hello.html">
    HTML 기초
</a>
```

### 73.2 After

```html
<a href="../01_hello.html">
    HTML 기초
</a>
```

File System 위치를 기준으로 계산한다.

---

<a id="html-77"></a>

## 74. 실제 개선 사례 5: Root Relative와 Absolute URL

```text
../asset/detail.html
→ Relative Path

/asset/detail.html
→ Root Relative Path

https://example.com/asset/detail.html
→ Absolute URL
```

서로 같은 개념으로 부르지 않는다.

---

<a id="html-78"></a>

## 75. 실제 개선 사례 6: List

### 75.1 Before

```html
<ol>
    ...
</ol>
```

“숫자가 보이니까 사용”이 아니라 순서 의미를 기준으로 선택한다.

### 75.2 After

```html
<ol>
    <li>회원가입</li>
    <li>Email 인증</li>
    <li>Profile 설정</li>
</ol>
```

---

<a id="html-79"></a>

## 76. 실제 개선 사례 7: Table `summary`

### 76.1 Before

```html
<table>
    <summary>
        제목, 작성자
    </summary>
</table>
```

`summary`는 `details`와 함께 사용하는 Element다.

### 76.2 After

```html
<table>
    <caption>
        게시글 목록
    </caption>

    ...
</table>
```

---

<a id="html-80"></a>

## 77. 실제 개선 사례 8: 잘못 닫힌 Table Cell

### 77.1 Before

```html
<th>
    번호
</td>
```

### 77.2 After

```html
<th scope="col">
    번호
</th>
```

---

<a id="html-81"></a>

## 78. 실제 개선 사례 9: Image 비율

### 78.1 Before

```html
<img
    src="./image.png"
    alt="설명"
    width="200"
    height="300"
>
```

원본 비율과 다르면 왜곡될 수 있다.

### 78.2 After

```html
<img
    src="./image.png"
    alt="설명"
    width="800"
    height="600"
    class="responsive-image"
>
```

CSS:

```css
.responsive-image {
    max-width: 100%;
    height: auto;
}
```

---

<a id="html-82"></a>

## 79. 실제 개선 사례 10: Form Submit Attribute

### 79.1 Before

```html
<input
    type="submit"
    value123="전송"
>
```

### 79.2 After

```html
<input
    type="submit"
    value="전송"
>
```

---

<a id="html-83"></a>

## 80. 실제 개선 사례 11: Radio 중복 선택

### 80.1 Before

```html
<input
    type="radio"
    name="gender"
    checked
>

<input
    type="radio"
    name="gender"
    checked
>
```

### 80.2 After

```html
<input
    type="radio"
    name="gender"
    value="female"
    checked
>

<input
    type="radio"
    name="gender"
    value="male"
>
```

---

<a id="html-84"></a>

## 81. 실제 개선 사례 12: Textarea 내부 Tag

### 81.1 Before

```html
<textarea>
    내용<br>
    <!-- Comment -->
</textarea>
```

### 81.2 After

```html
<textarea
    name="message"
    placeholder="내용을 입력하세요"
></textarea>
```

Textarea 내부는 Text Value로 다룬다.

---

<a id="html-85"></a>

## 82. 실제 개선 사례 13: POST 오해

잘못된 설명:

```text
POST
→ 주소가 절대 바뀌지 않음
→ 안전함
```

정확한 기준:

```text
POST
→ Request Body 사용

Redirect
→ URL이 변경될 수 있음

HTTPS
→ 전송 암호화

Server Validation
→ 데이터 신뢰성·보안 검증
```

---

<a id="html-86"></a>

## 83. 실제 개선 사례 14: Semantic Page 구조

### 83.1 Before

```html
<div class="header"></div>
<div class="menu"></div>
<div class="content"></div>
<div class="footer"></div>
```

### 83.2 After

```html
<header class="site-header">
    ...
</header>

<nav aria-label="주요 메뉴">
    ...
</nav>

<main>
    ...
</main>

<footer class="site-footer">
    ...
</footer>
```

역할이 있는 영역만 Semantic Element로 변경한다.

---

<a id="html-87"></a>

## 84. 실무형 Page 골격 예제

```html
<!doctype html>
<html lang="ko">
    <head>
        <meta charset="UTF-8">

        <meta
            name="viewport"
            content="width=device-width, initial-scale=1.0"
        >

        <meta
            name="description"
            content="Frontend 개발 과정을 소개하는 교육 페이지"
        >

        <title>
            Frontend 과정 | Developer Academy
        </title>

        <link
            rel="stylesheet"
            href="./assets/css/style.css"
        >
    </head>

    <body>
        <header class="site-header">
            <a
                href="./index.html"
                class="site-logo"
            >
                Developer Academy
            </a>

            <nav aria-label="주요 메뉴">
                <ul class="site-nav">
                    <li>
                        <a
                            href="./courses.html"
                            aria-current="page"
                        >
                            과정
                        </a>
                    </li>

                    <li>
                        <a href="./projects.html">
                            프로젝트
                        </a>
                    </li>

                    <li>
                        <a href="./contact.html">
                            문의
                        </a>
                    </li>
                </ul>
            </nav>
        </header>

        <main>
            <section
                class="hero"
                aria-labelledby="hero-title"
            >
                <h1 id="hero-title">
                    Frontend 개발 과정
                </h1>

                <p>
                    HTML, CSS, JavaScript를
                    실무 흐름으로 학습합니다.
                </p>

                <a href="#course-list">
                    과정 살펴보기
                </a>
            </section>

            <section
                id="course-list"
                aria-labelledby="course-list-title"
            >
                <h2 id="course-list-title">
                    추천 과정
                </h2>

                <div class="course-grid">
                    <article class="course-card">
                        <img
                            src="./assets/images/html.webp"
                            alt=""
                            width="640"
                            height="360"
                        >

                        <h3>
                            HTML
                        </h3>

                        <p>
                            Semantic Markup과
                            접근성을 학습합니다.
                        </p>

                        <a href="./courses/html.html">
                            HTML 과정 자세히 보기
                        </a>
                    </article>

                    <article class="course-card">
                        <img
                            src="./assets/images/css.webp"
                            alt=""
                            width="640"
                            height="360"
                        >

                        <h3>
                            CSS
                        </h3>

                        <p>
                            Responsive Layout과
                            UI Styling을 학습합니다.
                        </p>

                        <a href="./courses/css.html">
                            CSS 과정 자세히 보기
                        </a>
                    </article>
                </div>
            </section>

            <section
                aria-labelledby="contact-title"
            >
                <h2 id="contact-title">
                    상담 신청
                </h2>

                <form
                    action="/api/contact"
                    method="post"
                >
                    <div class="form-field">
                        <label for="name">
                            이름
                        </label>

                        <input
                            type="text"
                            id="name"
                            name="name"
                            autocomplete="name"
                            required
                        >
                    </div>

                    <div class="form-field">
                        <label for="email">
                            Email
                        </label>

                        <input
                            type="email"
                            id="email"
                            name="email"
                            autocomplete="email"
                            required
                        >
                    </div>

                    <button type="submit">
                        상담 신청
                    </button>
                </form>
            </section>
        </main>

        <footer class="site-footer">
            <p>
                &copy; 2026 Developer Academy
            </p>
        </footer>

        <script
            src="./assets/js/main.js"
            defer
        ></script>
    </body>
</html>
```

---

<a id="html-88"></a>

## 85. 실무 검수 순서

```text
1. HTML만 보고 Page 구조 확인
    ↓
2. Heading Level 확인
    ↓
3. Landmark 확인
    ↓
4. Link·Button 역할 확인
    ↓
5. List·Table 관계 확인
    ↓
6. Image alt 확인
    ↓
7. Form Label·name 확인
    ↓
8. ID 중복 확인
    ↓
9. Validator 실행
    ↓
10. Keyboard·Screen Reader·DevTools 확인
```

---

<a id="html-89"></a>

## 86. 자주 하는 실수

### 86.1 모든 영역을 `div`로 작성

의미가 있는 영역은 Semantic Element를 검토한다.

### 86.2 모든 영역을 `section`으로 작성

주제와 Heading이 없는 Wrapper는 `div`가 더 적합할 수 있다.

### 86.3 Heading을 Font Size로 선택

문서 계층 기준으로 선택하고 크기는 CSS에서 변경한다.

### 86.4 `href="#"`를 Button처럼 사용

상태 변경은 `button`을 우선한다.

<a id="index-section-181"></a>

### 86.5 Image `alt` 생략

Image 목적에 따라 의미 있는 `alt` 또는 `alt=""`를 제공한다.

### 86.6 Placeholder를 Label로 사용

보이는 Label 또는 Accessible Name을 제공한다.

### 86.7 `name` 없는 Form Control

제출 Key가 없으면 Form Data에 포함되지 않을 수 있다.

### 86.8 Duplicate ID

Label·ARIA·Fragment 연결이 깨질 수 있다.

<a id="index-section-185"></a>

### 86.9 `br` 반복

Layout 간격은 CSS로 처리한다.

### 86.10 Comment에 비밀 정보 작성

HTML Source에서 노출될 수 있다.

---

<a id="html-90"></a>

## 87. HTML Validator 활용

대표적으로 다음을 확인한다.

```text
잘못된 중첩
Duplicate ID
필수 Attribute 누락
Unknown Element·Attribute
닫는 Tag 오류
Table 구조 오류
```

Validator 오류가 없다고 접근성까지 완벽한 것은 아니다.

---

<a id="html-91"></a>

## 88. DevTools에서 확인할 항목

- 실제 DOM이 작성한 Markup과 같은지 확인
- Browser가 자동 보정한 Element 위치 확인
- Accessible Name 확인
- Form Control State 확인
- Network에서 Resource 404 확인
- Console Warning 확인

---

<a id="html-92"></a>

## 89. 접근성 검수 기준

- Keyboard만으로 모든 기능을 사용할 수 있는가?
- Focus 순서가 DOM 순서와 자연스러운가?
- Heading 구조가 Page 내용을 설명하는가?
- Landmark가 과도하게 중복되지 않는가?
- Link Text가 목적을 설명하는가?
- Icon-only Button에 Accessible Name이 있는가?
- Image `alt`가 목적에 맞는가?
- Form Label이 연결되어 있는가?
- Error Message가 Control과 연결되어 있는가?
- Table Header 관계가 명확한가?

---

<a id="html-93"></a>

## 90. 코드 리뷰 기준

HTML Review에서는 다음을 확인한다.

```text
이 Element가 정말 가장 적절한가?
    ↓
Semantic 구조가 과하거나 부족하지 않은가?
    ↓
CSS가 없어도 읽는 순서가 자연스러운가?
    ↓
JavaScript 없이도 기본 기능이 가능한가?
    ↓
접근성 Attribute가 실제 상태와 일치하는가?
    ↓
다른 개발자가 Element 역할을 바로 이해할 수 있는가?
```

---

<a id="html-94"></a>

## 91. 최종 체크리스트

- [ ] `<!doctype html>`을 작성했는가?
- [ ] Document Language가 실제 Content와 일치하는가?
- [ ] `charset`과 `viewport`가 있는가?
- [ ] Page마다 의미 있는 `<title>`을 제공하는가?
- [ ] Semantic Element를 역할에 맞게 사용하는가?
- [ ] 의미 없는 Wrapper에는 `div`를 사용하는가?
- [ ] `main`을 중첩하지 않는가?
- [ ] 여러 Navigation이 있다면 구분 가능한 Name을 제공하는가?
- [ ] Heading Level이 정보 계층을 반영하는가?
- [ ] 일반 Text를 적절한 Element로 감싸는가?
- [ ] Layout을 `<br>`과 `&nbsp;`로 만들지 않는가?
- [ ] Link Text가 이동 목적을 설명하는가?
- [ ] Link와 Button의 역할을 구분하는가?
- [ ] 새 Tab이 실제 요구사항인지 확인했는가?
- [ ] 상대 경로를 현재 File 위치 기준으로 계산했는가?
- [ ] 외부 Resource의 안정성·권한을 확인했는가?
- [ ] 정보성 Image에 목적에 맞는 `alt`를 제공하는가?
- [ ] 장식용 Image에 `alt=""`를 사용하는가?
- [ ] Link Image의 Accessible Name이 목적을 전달하는가?
- [ ] Image Width·Height와 반응형 CSS를 함께 고려하는가?
- [ ] Video에 사용자가 제어할 방법을 제공하는가?
- [ ] `iframe`에 의미 있는 `title`을 제공하는가?
- [ ] List Element를 항목 관계 기준으로 선택하는가?
- [ ] Table을 Layout 용도로 사용하지 않는가?
- [ ] Table에 필요한 `caption`, `th`, `scope`를 제공하는가?
- [ ] Presentational Attribute 대신 CSS를 사용하는가?
- [ ] Form Control에 연결된 Label이 있는가?
- [ ] `id`, `name`, `class` 역할을 구분하는가?
- [ ] Duplicate ID가 없는가?
- [ ] Checkbox·Radio에 의미 있는 `value`를 제공하는가?
- [ ] Radio Group 기본 `checked`가 하나뿐인가?
- [ ] Form Button의 `type`을 명시하는가?
- [ ] GET·POST와 HTTPS 역할을 구분하는가?
- [ ] Server Validation을 수행하는가?
- [ ] Comment에 민감 정보를 작성하지 않는가?
- [ ] Class·ID 이름이 역할을 설명하는가?
- [ ] Tag와 Attribute Style을 일관되게 작성하는가?
- [ ] Browser가 자동 보정한 DOM을 DevTools에서 확인했는가?
- [ ] Validator로 Markup 오류를 확인했는가?
- [ ] Keyboard와 Screen Reader 기준으로 검수했는가?

---

<a id="html-95"></a>

## 92. 핵심 요약

```text
Document
→ doctype
→ lang
→ charset
→ viewport
→ title
```

```text
Structure
→ header
→ nav
→ main
→ section
→ article
→ aside
→ footer
```

```text
Meaning
→ Heading
→ Link vs Button
→ List 관계
→ Table Data
→ Form Label
→ Image alt
```

```text
Project Rule
→ 역할 기반 Class
→ 고유 ID
→ 상대 경로
→ Comment 최소화
→ Inline Style 분리
```

```text
Quality
→ Validator
→ DevTools
→ Keyboard
→ Screen Reader
→ Server Validation
```

---

<a id="html-96"></a>

## 마무리

HTML 실무 코딩 스타일의 핵심은 Tag를 많이 사용하는 것이 아니다.

```text
Content 역할을 먼저 판단하고
    ↓
가장 적절한 Native Element를 선택하고
    ↓
Heading·Landmark·Reading Order를 정리하고
    ↓
Image·Table·Form에 접근성 정보를 제공하고
    ↓
CSS와 JavaScript가 안정적으로 연결되도록 구조화하고
    ↓
Validator와 실제 Browser에서 검수하는 것
```

좋은 HTML은 단순히 Browser에 렌더링되는 Markup이 아니다.

**사람과 Browser, Search Engine, Screen Reader, CSS, JavaScript가 같은 구조를 이해할 수 있도록 Content의 의미를 명확하게 표현하는 문서**다.
<a id="html-97"></a>

## 브라우저 해석 복습 카드 — 유효하고 읽히며 접근 가능한 마크업

실무 HTML은 올바른 중첩, 예측 가능한 들여쓰기, 의미에 맞는 요소, 고유한 id, 설명적인 링크 텍스트를 사용한다. CSS나 JavaScript 편의를 위해 의미를 훼손하지 않는다.

마우스 없이 Tab·Enter·Space로 기능을 시험하고 label, alt, heading, landmark를 확인한다. Validator 오류와 브라우저 자동 보정 DOM을 함께 보고 원인을 수정한다.

**원본 연결:** 내 코드와 강사님 코드의 `workspace_html/01~07 내 코드와 강사님 코드 전체를 재검토하는 Wiki 확장 기준`에서 실제 DOM·요청·접근성 차이를 확인한다.


[HTML 파트 목차로 돌아가기](./README.md)
