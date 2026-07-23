---
title: HTML 목록 태그
version: v1.0
last_updated: 2026-07-21
status: Completed
---

# HTML 목록 태그

## 개요

웹 페이지에서는 여러 항목을 일정한 기준에 따라 나열해야 하는 경우가 많다.

대표적인 예는 다음과 같다.

- 메뉴
- 상품 목록
- 공지사항
- 학습 과정
- 순위
- 작업 순서
- 용어 설명
- 자주 묻는 질문

HTML에서는 목록의 성격에 따라 서로 다른 태그를 사용한다.

| 태그 | 역할 |
|---|---|
| `<ul>` | 순서가 중요하지 않은 목록 |
| `<ol>` | 순서가 중요한 목록 |
| `<li>` | 목록의 각 항목 |
| `<dl>` | 설명 목록 |
| `<dt>` | 설명할 용어나 이름 |
| `<dd>` | 용어에 대한 설명 |

목록 태그는 단순히 글머리 기호나 번호를 표시하기 위한 태그가 아니다.

목록의 구조와 항목 사이의 관계를 브라우저, 검색 엔진, 화면 낭독기 등에 전달하는 의미를 가진다.

---

# 핵심 개념

## 목록의 종류

HTML 목록은 크게 세 가지로 구분할 수 있다.

### 순서가 없는 목록

항목의 순서가 중요하지 않을 때 `<ul>`을 사용한다.

```html
<ul>
    <li>HTML</li>
    <li>CSS</li>
    <li>JavaScript</li>
</ul>
```

### 순서가 있는 목록

작업 순서나 순위처럼 항목의 순서가 중요할 때 `<ol>`을 사용한다.

```html
<ol>
    <li>회원 가입</li>
    <li>로그인</li>
    <li>강의 신청</li>
</ol>
```

### 설명 목록

용어와 설명, 이름과 값처럼 서로 연결된 정보를 표현할 때 `<dl>`을 사용한다.

```html
<dl>
    <dt>HTML</dt>
    <dd>웹 페이지의 구조를 정의하는 마크업 언어</dd>

    <dt>CSS</dt>
    <dd>웹 페이지의 디자인과 레이아웃을 정의하는 언어</dd>
</dl>
```

---

# 순서가 없는 목록

## `<ul>`

`<ul>`은 Unordered List의 약자로, 항목의 순서가 중요하지 않은 목록을 나타낸다.

```html
<ul>
    <li>HTML</li>
    <li>CSS</li>
    <li>JavaScript</li>
</ul>
```

브라우저에서는 기본적으로 각 항목 앞에 글머리 기호를 표시한다.

```text
• HTML
• CSS
• JavaScript
```

글머리 기호의 모양은 브라우저의 기본 스타일이나 CSS에 따라 달라질 수 있다.

---

## `<li>`

`<li>`는 List Item의 약자로, 목록의 각 항목을 나타낸다.

```html
<ul>
    <li>프론트엔드</li>
    <li>백엔드</li>
    <li>데이터베이스</li>
</ul>
```

`<li>`는 일반적으로 `<ul>`, `<ol>`, `<menu>`와 같은 목록 요소 내부에 작성한다.

잘못된 예는 다음과 같다.

```html
<li>HTML</li>
<li>CSS</li>
```

목록 항목은 목록을 감싸는 부모 요소 안에 작성해야 한다.

```html
<ul>
    <li>HTML</li>
    <li>CSS</li>
</ul>
```

---

## 순서가 중요하지 않은 목록의 예

다음과 같은 내용에는 `<ul>`이 적절하다.

- 지원 기술
- 상품 특징
- 메뉴 항목
- 준비물
- 관련 문서
- 카테고리

```html
<h2>학습 기술</h2>

<ul>
    <li>HTML</li>
    <li>CSS</li>
    <li>JavaScript</li>
    <li>React</li>
</ul>
```

항목의 위치를 서로 바꾸더라도 전체 의미가 크게 달라지지 않는다면 `<ul>`을 사용할 수 있다.

---

# 순서가 있는 목록

## `<ol>`

`<ol>`은 Ordered List의 약자로, 항목의 순서가 중요한 목록을 나타낸다.

```html
<ol>
    <li>프로젝트 폴더를 생성한다.</li>
    <li>HTML 파일을 생성한다.</li>
    <li>CSS 파일을 연결한다.</li>
    <li>JavaScript 파일을 연결한다.</li>
</ol>
```

브라우저에서는 기본적으로 각 항목 앞에 번호를 표시한다.

```text
1. 프로젝트 폴더를 생성한다.
2. HTML 파일을 생성한다.
3. CSS 파일을 연결한다.
4. JavaScript 파일을 연결한다.
```

---

## 순서가 중요한 목록의 예

다음과 같은 내용에는 `<ol>`이 적절하다.

- 작업 절차
- 설치 순서
- 요리 과정
- 순위
- 학습 단계
- 신청 방법

```html
<h2>수강 신청 방법</h2>

<ol>
    <li>회원 가입을 진행한다.</li>
    <li>로그인한다.</li>
    <li>원하는 교육 과정을 선택한다.</li>
    <li>수강 신청 버튼을 누른다.</li>
</ol>
```

항목의 순서를 변경했을 때 내용의 의미나 진행 과정이 달라진다면 `<ol>`을 사용하는 것이 적절하다.

---

# `<ul>`과 `<ol>`의 차이

| 구분 | `<ul>` | `<ol>` |
|---|---|---|
| 이름 | Unordered List | Ordered List |
| 의미 | 순서가 중요하지 않은 목록 | 순서가 중요한 목록 |
| 기본 표시 | 글머리 기호 | 숫자 |
| 사용 예 | 메뉴, 기술 목록, 특징 | 작업 절차, 순위, 학습 단계 |

## `<ul>` 사용 예

```html
<ul>
    <li>노트북</li>
    <li>필기도구</li>
    <li>교재</li>
</ul>
```

준비물의 순서는 특별히 중요하지 않다.

## `<ol>` 사용 예

```html
<ol>
    <li>파일을 다운로드한다.</li>
    <li>압축을 해제한다.</li>
    <li>프로그램을 실행한다.</li>
</ol>
```

설치 과정은 순서가 중요하다.

목록의 화면 모양이 아니라 **항목 사이에 순서가 필요한지**를 기준으로 태그를 선택해야 한다.

---

# 목록 내부의 콘텐츠

`<li>` 내부에는 단순한 텍스트뿐 아니라 다양한 HTML 요소를 작성할 수 있다.

```html
<ul>
    <li>
        <h3>HTML</h3>
        <p>웹 페이지의 구조를 정의합니다.</p>
    </li>

    <li>
        <h3>CSS</h3>
        <p>웹 페이지의 디자인을 정의합니다.</p>
    </li>
</ul>
```

링크를 포함할 수도 있다.

```html
<ul>
    <li>
        <a href="./html.html">HTML 학습하기</a>
    </li>

    <li>
        <a href="./css.html">CSS 학습하기</a>
    </li>
</ul>
```

이미지, 문단, 제목, 버튼 등을 목록 항목 안에 포함하여 카드 목록과 같은 구조를 만들 수도 있다.

```html
<ul>
    <li>
        <article>
            <h3>프론트엔드 과정</h3>
            <p>HTML, CSS, JavaScript를 학습합니다.</p>
            <a href="./frontend.html">과정 보기</a>
        </article>
    </li>
</ul>
```

---

# 중첩 목록

목록 항목 내부에 또 다른 목록을 작성할 수 있다.

이를 **중첩 목록**이라고 한다.

```html
<ul>
    <li>
        Frontend

        <ul>
            <li>HTML</li>
            <li>CSS</li>
            <li>JavaScript</li>
        </ul>
    </li>

    <li>
        Backend

        <ul>
            <li>Java</li>
            <li>Spring</li>
        </ul>
    </li>
</ul>
```

구조는 다음과 같다.

```text
Frontend
├── HTML
├── CSS
└── JavaScript

Backend
├── Java
└── Spring
```

하위 목록은 반드시 관련된 상위 `<li>` 내부에 작성해야 한다.

---

## 잘못된 중첩

```html
<ul>
    <li>Frontend</li>

    <ul>
        <li>HTML</li>
        <li>CSS</li>
    </ul>
</ul>
```

하위 `<ul>`이 관련 항목인 `<li>` 바깥에 작성되어 있다.

---

## 올바른 중첩

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

하위 목록은 상위 목록의 항목 내부에 포함한다.

---

# 서로 다른 목록 중첩하기

`<ul>` 안에 `<ol>`을 넣거나, `<ol>` 안에 `<ul>`을 넣을 수도 있다.

```html
<ul>
    <li>
        프로젝트 준비

        <ol>
            <li>요구사항을 분석한다.</li>
            <li>화면 구조를 설계한다.</li>
            <li>개발 일정을 작성한다.</li>
        </ol>
    </li>

    <li>
        프로젝트 개발

        <ol>
            <li>HTML 구조를 작성한다.</li>
            <li>CSS를 적용한다.</li>
            <li>JavaScript 기능을 구현한다.</li>
        </ol>
    </li>
</ul>
```

상위 항목의 순서는 중요하지 않지만, 각 항목 내부의 작업 과정은 순서가 중요하기 때문에 `<ul>`과 `<ol>`을 함께 사용했다.

---

# `<ol>`의 `start` 속성

`start` 속성을 사용하면 목록 번호의 시작 값을 지정할 수 있다.

```html
<ol start="4">
    <li>React</li>
    <li>Spring Boot</li>
    <li>Portfolio</li>
</ol>
```

브라우저에서는 다음과 같이 표시된다.

```text
4. React
5. Spring Boot
6. Portfolio
```

긴 목록을 여러 영역으로 나누면서 번호를 이어서 표시해야 할 때 사용할 수 있다.

```html
<h2>기초 과정</h2>

<ol>
    <li>HTML</li>
    <li>CSS</li>
    <li>JavaScript</li>
</ol>

<h2>심화 과정</h2>

<ol start="4">
    <li>React</li>
    <li>Spring Boot</li>
    <li>Portfolio</li>
</ol>
```

`start` 속성에는 정수를 작성한다.

```html
<ol start="10">
```

---

# `<ol>`의 `reversed` 속성

`reversed` 속성을 사용하면 목록 번호를 내림차순으로 표시할 수 있다.

```html
<ol reversed>
    <li>금메달</li>
    <li>은메달</li>
    <li>동메달</li>
</ol>
```

목록의 항목 수를 기준으로 번호가 감소한다.

```text
3. 금메달
2. 은메달
1. 동메달
```

시작 번호를 함께 지정할 수도 있다.

```html
<ol start="10" reversed>
    <li>열 번째 항목</li>
    <li>아홉 번째 항목</li>
    <li>여덟 번째 항목</li>
</ol>
```

---

# `<ol>`의 `type` 속성

`type` 속성을 사용하면 번호의 표시 방식을 지정할 수 있다.

```html
<ol type="A">
    <li>HTML</li>
    <li>CSS</li>
    <li>JavaScript</li>
</ol>
```

대표적인 값은 다음과 같다.

| 값 | 표시 방식 |
|---|---|
| `1` | 숫자 |
| `A` | 영문 대문자 |
| `a` | 영문 소문자 |
| `I` | 로마 숫자 대문자 |
| `i` | 로마 숫자 소문자 |

```html
<ol type="I">
    <li>Introduction</li>
    <li>HTML</li>
    <li>CSS</li>
</ol>
```

목록의 시각적인 번호 모양만 변경하려면 CSS의 `list-style-type`을 사용할 수도 있다.

```css
.step-list {
    list-style-type: upper-roman;
}
```

HTML 속성은 목록 자체의 번호 체계가 내용의 의미와 관련될 때 사용할 수 있고, 단순한 디자인 변경은 CSS로 처리하는 것이 좋다.

---

# `<li>`의 `value` 속성

순서가 있는 목록에서 특정 항목의 번호를 변경할 수 있다.

```html
<ol>
    <li>첫 번째 항목</li>
    <li value="5">다섯 번째 항목</li>
    <li>여섯 번째 항목</li>
</ol>
```

브라우저에서는 다음과 같이 표시된다.

```text
1. 첫 번째 항목
5. 다섯 번째 항목
6. 여섯 번째 항목
```

`value` 속성은 `<ol>` 내부의 `<li>`에 사용할 수 있다.

일반적인 목록에서는 자동 번호를 사용하는 것이 좋으며, 번호 체계를 의도적으로 변경해야 할 때만 사용한다.

---

# 목록 기호와 CSS

목록의 기본 글머리 기호나 번호 모양은 CSS로 변경할 수 있다.

```html
<ul class="skill-list">
    <li>HTML</li>
    <li>CSS</li>
    <li>JavaScript</li>
</ul>
```

```css
.skill-list {
    list-style-type: square;
}
```

대표적인 값은 다음과 같다.

| 값 | 설명 |
|---|---|
| `disc` | 채워진 원 |
| `circle` | 빈 원 |
| `square` | 사각형 |
| `decimal` | 숫자 |
| `upper-alpha` | 영문 대문자 |
| `lower-alpha` | 영문 소문자 |
| `upper-roman` | 로마 숫자 대문자 |
| `lower-roman` | 로마 숫자 소문자 |
| `none` | 목록 기호 제거 |

```css
.navigation-list {
    list-style: none;
    margin: 0;
    padding: 0;
}
```

실무의 내비게이션 메뉴에서는 기본 목록 기호를 제거하는 경우가 많다.

하지만 CSS로 기호를 제거해도 HTML 구조는 여전히 목록으로 유지된다.

---

# 목록과 내비게이션 메뉴

웹 사이트의 메뉴는 관련 링크의 목록이므로 `<ul>`과 `<li>`를 자주 사용한다.

```html
<nav aria-label="주요 메뉴">
    <ul>
        <li>
            <a href="./index.html">홈</a>
        </li>

        <li>
            <a href="./courses.html">교육 과정</a>
        </li>

        <li>
            <a href="./portfolio.html">포트폴리오</a>
        </li>

        <li>
            <a href="./contact.html">문의하기</a>
        </li>
    </ul>
</nav>
```

`<nav>`는 주요 탐색 링크 영역이라는 의미를 나타내고, `<ul>`은 여러 메뉴 항목이 하나의 목록이라는 구조를 나타낸다.

```text
nav
└── ul
    ├── li
    │   └── a
    ├── li
    │   └── a
    ├── li
    │   └── a
    └── li
        └── a
```

단순히 링크를 나열하는 것보다 목록 구조를 사용하면 메뉴 항목 사이의 관계를 더 명확하게 표현할 수 있다.

---

# 설명 목록

## `<dl>`

`<dl>`은 Description List의 약자로, 이름과 설명으로 구성된 목록을 나타낸다.

```html
<dl>
    <dt>HTML</dt>
    <dd>웹 페이지의 구조를 만드는 마크업 언어</dd>

    <dt>CSS</dt>
    <dd>웹 페이지의 디자인과 레이아웃을 정의하는 언어</dd>
</dl>
```

`<dl>` 내부에서는 주로 `<dt>`와 `<dd>`를 사용한다.

| 태그 | 역할 |
|---|---|
| `<dl>` | 설명 목록 전체 |
| `<dt>` | 설명할 용어, 이름 또는 키 |
| `<dd>` | 해당 용어에 대한 설명 또는 값 |

---

## `<dt>`

`<dt>`는 Description Term을 의미하며, 설명할 용어나 이름을 나타낸다.

```html
<dt>HTML</dt>
```

단순한 사전 용어뿐 아니라 상품 속성명, 질문, 이름 등의 역할로도 사용할 수 있다.

---

## `<dd>`

`<dd>`는 Description Details를 의미하며, `<dt>`에서 제시한 용어에 대한 설명이나 값을 나타낸다.

```html
<dd>웹 페이지의 구조를 정의하는 마크업 언어</dd>
```

---

# 설명 목록 활용

## 용어 사전

```html
<dl>
    <dt>Element</dt>
    <dd>시작 태그부터 종료 태그까지 포함한 전체 요소</dd>

    <dt>Attribute</dt>
    <dd>HTML 태그에 추가 정보를 제공하는 값</dd>
</dl>
```

## 상품 정보

```html
<dl>
    <dt>상품명</dt>
    <dd>Developer Keyboard</dd>

    <dt>가격</dt>
    <dd>129,000원</dd>

    <dt>배송비</dt>
    <dd>무료</dd>
</dl>
```

## 과정 정보

```html
<dl>
    <dt>교육 기간</dt>
    <dd>6개월</dd>

    <dt>교육 시간</dt>
    <dd>평일 09:00~18:00</dd>

    <dt>교육 장소</dt>
    <dd>서울특별시 강남구</dd>
</dl>
```

설명 목록은 이름과 값이 서로 연결된 정보를 표현하는 데 유용하다.

---

# 하나의 용어에 여러 설명 작성하기

하나의 `<dt>`에 여러 개의 `<dd>`를 연결할 수 있다.

```html
<dl>
    <dt>HTML</dt>
    <dd>HyperText Markup Language의 약자</dd>
    <dd>웹 페이지의 구조를 정의하는 마크업 언어</dd>
</dl>
```

---

# 여러 용어에 하나의 설명 작성하기

여러 `<dt>`가 하나의 `<dd>` 설명을 공유할 수도 있다.

```html
<dl>
    <dt>Frontend</dt>
    <dt>프론트엔드</dt>
    <dd>사용자가 직접 보는 웹 화면을 개발하는 영역</dd>
</dl>
```

---

# `<dl>`과 `<ul>`의 차이

| 구분 | `<ul>` | `<dl>` |
|---|---|---|
| 구조 | 동일한 성격의 항목 목록 | 이름과 설명의 관계 |
| 내부 요소 | `<li>` | `<dt>`, `<dd>` |
| 사용 예 | 기술 목록, 메뉴, 특징 | 용어 사전, 상품 정보, 질문과 답변 |

## 단순한 기술 목록

```html
<ul>
    <li>HTML</li>
    <li>CSS</li>
    <li>JavaScript</li>
</ul>
```

## 기술과 설명

```html
<dl>
    <dt>HTML</dt>
    <dd>웹 페이지의 구조를 정의한다.</dd>

    <dt>CSS</dt>
    <dd>웹 페이지의 스타일을 정의한다.</dd>
</dl>
```

각 항목이 동일한 수준으로 나열되는 경우에는 `<ul>`을 사용하고, 이름과 설명의 관계가 있는 경우에는 `<dl>`을 사용한다.

---

# 목록과 접근성

올바른 목록 태그를 사용하면 화면 낭독기는 목록의 항목 수와 구조를 사용자에게 전달할 수 있다.

예를 들어 다음 구조가 있다고 가정한다.

```html
<ul>
    <li>HTML</li>
    <li>CSS</li>
    <li>JavaScript</li>
</ul>
```

보조 기술은 이 콘텐츠가 세 개의 항목으로 구성된 목록이라는 사실을 파악할 수 있다.

반면 단순히 문단과 특수문자로 목록처럼 표현하면 구조를 정확하게 전달하기 어렵다.

```html
<p>• HTML</p>
<p>• CSS</p>
<p>• JavaScript</p>
```

화면에서는 비슷하게 보일 수 있지만, HTML 구조상으로는 목록이 아니다.

목록은 모양이 아니라 의미에 맞는 태그를 사용해야 한다.

---

# 실무 활용

목록 태그는 다양한 화면에서 사용된다.

## 기술 스택

```html
<ul>
    <li>HTML5</li>
    <li>CSS3</li>
    <li>JavaScript</li>
    <li>React</li>
</ul>
```

## 작업 단계

```html
<ol>
    <li>요구사항 분석</li>
    <li>화면 설계</li>
    <li>마크업 작성</li>
    <li>스타일 적용</li>
    <li>기능 구현</li>
</ol>
```

## 내비게이션

```html
<nav aria-label="문서 메뉴">
    <ul>
        <li><a href="./html.html">HTML</a></li>
        <li><a href="./css.html">CSS</a></li>
        <li><a href="./javascript.html">JavaScript</a></li>
    </ul>
</nav>
```

## 상품 특징

```html
<ul>
    <li>무료 배송</li>
    <li>1년 무상 보증</li>
    <li>30일 이내 교환 가능</li>
</ul>
```

## 상품 상세 정보

```html
<dl>
    <dt>제품명</dt>
    <dd>Developer Keyboard</dd>

    <dt>연결 방식</dt>
    <dd>유선 및 블루투스</dd>

    <dt>보증 기간</dt>
    <dd>구매일로부터 1년</dd>
</dl>
```

---

# 실무 예제 프로젝트

다음은 Developer Academy의 교육 과정 소개 페이지 일부이다.

```html
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta
        name="viewport"
        content="width=device-width, initial-scale=1.0"
    >

    <title>교육 과정 | Developer Academy</title>
</head>
<body>
    <header>
        <h1>Developer Academy</h1>

        <nav aria-label="주요 메뉴">
            <ul>
                <li>
                    <a href="./index.html">홈</a>
                </li>

                <li>
                    <a href="./courses.html">교육 과정</a>
                </li>

                <li>
                    <a href="./projects.html">프로젝트</a>
                </li>

                <li>
                    <a href="./contact.html">문의하기</a>
                </li>
            </ul>
        </nav>
    </header>

    <main>
        <section>
            <h2>웹 개발자 취업 과정</h2>

            <p>
                웹 개발에 필요한 프론트엔드와 백엔드 기술을
                단계적으로 학습합니다.
            </p>

            <h3>주요 학습 기술</h3>

            <ul>
                <li>
                    Frontend

                    <ul>
                        <li>HTML</li>
                        <li>CSS</li>
                        <li>JavaScript</li>
                        <li>React</li>
                    </ul>
                </li>

                <li>
                    Backend

                    <ul>
                        <li>Java</li>
                        <li>Spring Boot</li>
                    </ul>
                </li>

                <li>
                    Database

                    <ul>
                        <li>Oracle</li>
                        <li>SQL</li>
                    </ul>
                </li>
            </ul>
        </section>

        <section>
            <h2>학습 진행 순서</h2>

            <ol>
                <li>HTML로 웹 페이지의 구조를 작성한다.</li>
                <li>CSS로 디자인과 레이아웃을 구현한다.</li>
                <li>JavaScript로 동적인 기능을 추가한다.</li>
                <li>React로 사용자 인터페이스를 개발한다.</li>
                <li>Spring Boot로 서버를 구현한다.</li>
                <li>프로젝트를 완성하고 포트폴리오를 제작한다.</li>
            </ol>
        </section>

        <section>
            <h2>과정 정보</h2>

            <dl>
                <dt>교육 기간</dt>
                <dd>6개월</dd>

                <dt>교육 시간</dt>
                <dd>평일 오전 9시부터 오후 6시까지</dd>

                <dt>교육 방식</dt>
                <dd>이론 학습과 실무 프로젝트 병행</dd>

                <dt>지원 내용</dt>
                <dd>수강료 전액 지원</dd>
                <dd>포트폴리오 및 취업 컨설팅 지원</dd>
            </dl>
        </section>

        <section>
            <h2>수강 신청 방법</h2>

            <ol>
                <li>교육 과정 상담을 신청한다.</li>
                <li>상담 일정에 맞춰 담당자와 상담한다.</li>
                <li>지원 자격을 확인한다.</li>
                <li>수강 신청서를 제출한다.</li>
                <li>최종 등록을 완료한다.</li>
            </ol>
        </section>
    </main>
</body>
</html>
```

## 예제 구조

```text
body
├── header
│   ├── h1
│   └── nav
│       └── ul
│           ├── li
│           │   └── a
│           ├── li
│           │   └── a
│           ├── li
│           │   └── a
│           └── li
│               └── a
└── main
    ├── section
    │   ├── h2
    │   ├── p
    │   ├── h3
    │   └── ul
    │       ├── li
    │       │   └── ul
    │       ├── li
    │       │   └── ul
    │       └── li
    │           └── ul
    ├── section
    │   ├── h2
    │   └── ol
    │       └── li
    ├── section
    │   ├── h2
    │   └── dl
    │       ├── dt
    │       └── dd
    └── section
        ├── h2
        └── ol
            └── li
```

## 예제에서 확인할 내용

- 주요 메뉴를 링크 목록으로 표현했다.
- 순서가 중요하지 않은 학습 기술은 `<ul>`로 작성했다.
- 기술의 하위 항목은 중첩 목록으로 구성했다.
- 학습 과정과 신청 절차는 순서가 중요하므로 `<ol>`을 사용했다.
- 교육 기간과 교육 방식처럼 이름과 값의 관계가 있는 정보는 `<dl>`로 작성했다.
- 하나의 교육 정보에 여러 설명이 필요한 경우 여러 `<dd>`를 사용했다.

---

# 이번 문서에서 새롭게 배운 내용

| 개념 또는 태그 | 설명 |
|---|---|
| 목록 | 관련된 여러 항목을 하나의 구조로 표현한 것 |
| `<ul>` | 순서가 중요하지 않은 목록 |
| `<ol>` | 순서가 중요한 목록 |
| `<li>` | 목록의 각 항목 |
| 중첩 목록 | 목록 항목 내부에 또 다른 목록을 작성한 구조 |
| `start` | `<ol>`의 시작 번호 지정 |
| `reversed` | `<ol>`의 번호를 내림차순으로 표시 |
| `type` | `<ol>`의 번호 표시 형식 지정 |
| `value` | 특정 `<li>`의 번호 지정 |
| `<dl>` | 이름과 설명으로 구성된 설명 목록 |
| `<dt>` | 설명할 용어나 이름 |
| `<dd>` | 용어에 대한 설명이나 값 |
| `list-style` | 목록 기호나 번호 모양을 설정하는 CSS 속성 |

---

# 자주 하는 실수

## 1. 화면 모양만 보고 `<ul>`과 `<ol>`을 선택한다

번호가 필요하다는 이유만으로 `<ol>`을 사용하는 것이 아니라, 항목의 순서가 실제로 중요한지 판단해야 한다.

```html
<ul>
    <li>HTML</li>
    <li>CSS</li>
    <li>JavaScript</li>
</ul>
```

기술 목록은 순서를 바꾸더라도 의미가 크게 달라지지 않으므로 `<ul>`이 적절하다.

```html
<ol>
    <li>HTML을 작성한다.</li>
    <li>CSS를 적용한다.</li>
    <li>JavaScript를 연결한다.</li>
</ol>
```

작업 과정은 순서가 중요하므로 `<ol>`이 적절하다.

---

## 2. `<li>`를 목록 요소 밖에 작성한다

### 잘못된 예

```html
<li>HTML</li>
<li>CSS</li>
```

### 올바른 예

```html
<ul>
    <li>HTML</li>
    <li>CSS</li>
</ul>
```

---

## 3. `<ul>` 또는 `<ol>`의 바로 아래에 일반 텍스트를 작성한다

### 좋지 않은 예

```html
<ul>
    Frontend
    <li>HTML</li>
    <li>CSS</li>
</ul>
```

목록 내부의 콘텐츠는 `<li>`로 구성한다.

```html
<ul>
    <li>Frontend</li>
    <li>HTML</li>
    <li>CSS</li>
</ul>
```

---

## 4. 하위 목록을 상위 `<li>` 밖에 작성한다

### 잘못된 예

```html
<ul>
    <li>Frontend</li>

    <ul>
        <li>HTML</li>
        <li>CSS</li>
    </ul>
</ul>
```

### 올바른 예

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

---

## 5. 목록처럼 보이게 문단과 특수문자를 사용한다

### 좋지 않은 예

```html
<p>• HTML</p>
<p>• CSS</p>
<p>• JavaScript</p>
```

### 권장 방식

```html
<ul>
    <li>HTML</li>
    <li>CSS</li>
    <li>JavaScript</li>
</ul>
```

목록 태그를 사용해야 구조와 항목 수를 보조 기술에 전달할 수 있다.

---

## 6. 목록 기호를 제거하기 위해 HTML 구조까지 없앤다

메뉴의 글머리 기호가 필요하지 않더라도 목록 구조를 유지하고 CSS로 기호만 제거한다.

```html
<nav>
    <ul class="navigation-list">
        <li><a href="./index.html">홈</a></li>
        <li><a href="./about.html">소개</a></li>
    </ul>
</nav>
```

```css
.navigation-list {
    list-style: none;
    margin: 0;
    padding: 0;
}
```

---

## 7. 이름과 값을 모두 `<ul>`로 작성한다

### 의미가 불명확한 예

```html
<ul>
    <li>교육 기간: 6개월</li>
    <li>교육 시간: 평일 09:00~18:00</li>
</ul>
```

이름과 값의 관계를 명확히 표현하려면 `<dl>`을 사용할 수 있다.

```html
<dl>
    <dt>교육 기간</dt>
    <dd>6개월</dd>

    <dt>교육 시간</dt>
    <dd>평일 09:00~18:00</dd>
</dl>
```

---

## 8. 디자인을 위해 `type` 속성만 사용한다

번호 형식이 콘텐츠의 의미와 관련되지 않고 단순히 시각적인 변경이라면 CSS를 사용하는 것이 좋다.

```css
.step-list {
    list-style-type: upper-roman;
}
```

HTML은 구조와 의미를 담당하고 CSS는 표현을 담당한다.

---

## 9. 목록을 지나치게 깊게 중첩한다

```text
목록
└── 목록
    └── 목록
        └── 목록
            └── 목록
```

중첩이 너무 깊어지면 사용자가 구조를 이해하기 어려워지고 모바일 화면에서도 복잡해진다.

필요한 경우 내용을 여러 섹션이나 페이지로 분리한다.

---

# 면접 포인트

## Q1. `<ul>`과 `<ol>`의 차이는 무엇인가요?

`<ul>`은 항목의 순서가 중요하지 않은 목록에 사용하고, `<ol>`은 작업 절차나 순위처럼 항목의 순서가 중요한 목록에 사용한다.

화면에 표시되는 글머리 기호나 숫자보다 목록의 의미를 기준으로 선택해야 한다.

---

## Q2. `<li>` 태그는 어떤 역할을 하나요?

`<li>`는 목록의 각 항목을 나타낸다.

일반적으로 `<ul>`이나 `<ol>` 내부에 작성하며, 텍스트뿐 아니라 링크, 문단, 이미지, 다른 목록 등의 요소를 포함할 수 있다.

---

## Q3. 중첩 목록은 어떻게 작성하나요?

하위 목록을 관련된 상위 `<li>` 내부에 작성한다.

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

하위 목록을 상위 `<li>`의 형제로 작성하지 않도록 주의해야 한다.

---

## Q4. `<ol>`의 `start` 속성은 무엇인가요?

순서가 있는 목록의 시작 번호를 지정한다.

```html
<ol start="4">
    <li>React</li>
    <li>Spring</li>
</ol>
```

위 목록은 4번부터 시작한다.

---

## Q5. `<ol>`의 `reversed` 속성은 무엇인가요?

목록 번호를 내림차순으로 표시한다.

```html
<ol reversed>
    <li>세 번째</li>
    <li>두 번째</li>
    <li>첫 번째</li>
</ol>
```

`reversed`는 값 없이 속성 이름만 작성할 수 있는 불리언 속성이다.

---

## Q6. `<dl>`, `<dt>`, `<dd>`는 언제 사용하나요?

이름과 설명 또는 키와 값의 관계를 가진 정보를 표현할 때 사용한다.

`<dl>`은 설명 목록 전체, `<dt>`는 설명할 이름, `<dd>`는 해당 이름에 대한 설명이나 값을 나타낸다.

용어 사전, 상품 정보, 교육 과정 정보 등에 사용할 수 있다.

---

## Q7. 내비게이션 메뉴에 목록 태그를 사용하는 이유는 무엇인가요?

메뉴는 서로 관련된 여러 링크의 집합이기 때문에 목록 구조로 표현할 수 있다.

`<nav>`로 주요 탐색 영역임을 나타내고, 내부 링크들을 `<ul>`과 `<li>`로 구성하면 메뉴 항목 사이의 관계를 명확하게 전달할 수 있다.

---

## Q8. 목록의 글머리 기호를 없애려면 어떻게 하나요?

HTML 구조를 제거하지 않고 CSS의 `list-style`을 사용한다.

```css
.navigation-list {
    list-style: none;
}
```

CSS로 글머리 기호를 제거해도 HTML의 목록 의미는 유지된다.

---

## Q9. `<ul>`의 항목 순서를 CSS로 바꾸면 의미도 바뀌나요?

화면상의 표시 순서를 변경하더라도 HTML 원본의 논리적 순서는 그대로 남을 수 있다.

특히 키보드 탐색이나 화면 낭독기의 읽기 순서와 시각적 순서가 달라질 수 있으므로, 중요한 콘텐츠 순서는 가능하면 HTML 문서 구조에서 올바르게 작성해야 한다.

---

## Q10. 목록과 단순한 문단 나열의 차이는 무엇인가요?

목록 태그를 사용하면 여러 항목이 하나의 관련된 집합이라는 구조를 명확히 표현할 수 있다.

화면 낭독기와 같은 보조 기술은 목록의 시작, 종료, 항목 수 등을 사용자에게 전달할 수 있다.

---

# 핵심 정리

- `<ul>`은 순서가 중요하지 않은 목록을 표현한다.
- `<ol>`은 순서가 중요한 목록을 표현한다.
- `<li>`는 목록의 각 항목을 나타낸다.
- 목록의 화면 모양이 아니라 항목의 의미와 순서를 기준으로 태그를 선택한다.
- `<li>` 내부에는 텍스트뿐 아니라 링크, 문단, 이미지와 다른 목록도 작성할 수 있다.
- 하위 목록은 관련된 상위 `<li>` 내부에 작성한다.
- `<ol>`의 `start`는 시작 번호를 지정한다.
- `<ol>`의 `reversed`는 번호를 내림차순으로 표시한다.
- `<ol>`의 `type`은 번호 형식을 지정한다.
- `<li>`의 `value`는 특정 항목의 번호를 지정할 수 있다.
- `<dl>`은 이름과 설명 또는 키와 값의 관계를 표현한다.
- `<dt>`는 설명할 이름이고 `<dd>`는 해당 이름의 설명이나 값이다.
- 내비게이션 메뉴는 `<nav>`와 목록 태그를 함께 사용하는 경우가 많다.
- 목록 기호와 번호의 디자인은 CSS로 변경한다.
- 올바른 목록 구조는 웹 접근성과 문서의 의미 전달에 도움이 된다.

---

# 변경 이력

| Version | 날짜 | 변경 내용 |
|---|---|---|
| v1.0 | 2026-07-21 | HTML 목록 태그 문서 최초 작성 |
| v1.0 | 2026-07-21 | `ul`, `ol`, `li`의 역할과 차이 정리 |
| v1.0 | 2026-07-21 | 중첩 목록 작성 방법 추가 |
| v1.0 | 2026-07-21 | `start`, `reversed`, `type`, `value` 속성 추가 |
| v1.0 | 2026-07-21 | `dl`, `dt`, `dd` 설명 목록 추가 |
| v1.0 | 2026-07-21 | 내비게이션과 목록의 실무 활용 추가 |
| v1.0 | 2026-07-21 | 목록과 웹 접근성 설명 추가 |
| v1.0 | 2026-07-21 | 실무 예제 프로젝트와 구조 분석 추가 |
| v1.0 | 2026-07-21 | 자주 하는 실수와 면접 포인트 추가 |
