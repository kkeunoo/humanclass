---
title: HTML 폼 태그
version: v1.0
last_updated: 2026-07-21
status: Completed
---

# HTML 폼 태그

## 개요

폼(Form)은 사용자가 입력하거나 선택한 데이터를 서버에 전달하기 위한 HTML 구조이다.

웹사이트의 로그인, 회원가입, 검색, 게시글 작성, 상품 주문, 설문조사, 문의 접수 등 대부분의 사용자 입력 기능은 폼을 기반으로 구현된다.

HTML에서는 `<form>` 요소를 중심으로 다양한 입력 요소를 구성한다.

```html
<form action="/login" method="post">
    <label for="user-id">아이디</label>

    <input
        type="text"
        id="user-id"
        name="userId"
    >

    <label for="user-password">비밀번호</label>

    <input
        type="password"
        id="user-password"
        name="password"
    >

    <button type="submit">
        로그인
    </button>
</form>
```

폼을 이해할 때는 화면에 보이는 입력창뿐 아니라 다음 개념을 함께 이해해야 한다.

- 입력 요소의 의미
- 사용자에게 표시되는 이름
- 서버로 전달되는 데이터 이름
- 제출 방식
- 기본 유효성 검사
- 키보드 사용
- 웹 접근성
- 클라이언트와 서버의 역할

---

# 핵심 개념

폼의 기본 구성은 다음과 같다.

| 요소 또는 속성 | 역할 |
|---|---|
| `<form>` | 사용자 입력 영역 전체 |
| `<label>` | 입력 요소의 이름과 설명 |
| `<input>` | 다양한 형태의 입력 필드 |
| `<textarea>` | 여러 줄 텍스트 입력 |
| `<select>` | 선택 목록 |
| `<option>` | 선택 가능한 항목 |
| `<button>` | 제출, 초기화, 일반 동작 실행 |
| `<fieldset>` | 관련 입력 요소 그룹 |
| `<legend>` | 입력 그룹의 제목 |
| `action` | 데이터를 전송할 주소 |
| `method` | 데이터 전송 방식 |
| `name` | 서버로 전달되는 데이터 이름 |
| `value` | 서버로 전달되는 데이터 값 |

---

# `<form>` 태그

`<form>`은 사용자 입력 요소를 하나의 제출 단위로 묶는다.

```html
<form>
    입력 요소
</form>
```

일반적으로 `action`과 `method` 속성을 함께 사용한다.

```html
<form
    action="/members"
    method="post"
>
    <!-- 입력 요소 -->
</form>
```

---

# `action` 속성

`action`은 폼 데이터를 전송할 서버 주소를 지정한다.

```html
<form action="/login">
```

예를 들어 다음 폼을 제출하면 `/login` 주소로 데이터가 전송된다.

```html
<form
    action="/login"
    method="post"
>
    <input
        type="text"
        name="userId"
    >

    <button type="submit">
        로그인
    </button>
</form>
```

`action`을 생략하면 일반적으로 현재 문서의 주소로 제출될 수 있다.

실무에서는 서버 라우팅 구조에 맞는 명확한 주소를 지정한다.

---

# `method` 속성

`method`는 폼 데이터를 어떤 HTTP 방식으로 전송할지 지정한다.

대표적인 값은 다음과 같다.

| 값 | 특징 |
|---|---|
| `get` | 데이터를 URL 쿼리 문자열에 포함 |
| `post` | 데이터를 요청 본문에 포함 |

---

## GET 방식

```html
<form
    action="/search"
    method="get"
>
    <label for="keyword">검색어</label>

    <input
        type="search"
        id="keyword"
        name="keyword"
    >

    <button type="submit">
        검색
    </button>
</form>
```

사용자가 `HTML`을 입력하면 다음과 같은 주소가 만들어질 수 있다.

```text
/search?keyword=HTML
```

GET 방식은 주로 다음에 적합하다.

- 검색
- 필터
- 정렬
- 조회
- 페이지 번호
- 공유 가능한 조건

URL에 조건이 표시되므로 주소를 저장하거나 공유하기 쉽다.

비밀번호나 민감한 정보를 GET 방식으로 전송하면 안 된다.

---

## POST 방식

```html
<form
    action="/members"
    method="post"
>
    <label for="member-name">이름</label>

    <input
        type="text"
        id="member-name"
        name="name"
    >

    <button type="submit">
        회원가입
    </button>
</form>
```

POST 방식은 주로 다음에 사용한다.

- 회원가입
- 로그인
- 게시글 작성
- 주문 생성
- 파일 업로드
- 데이터 변경

POST라고 해서 데이터가 자동으로 암호화되는 것은 아니다.

민감한 데이터를 안전하게 전송하려면 HTTPS를 사용해야 하며 서버에서도 적절한 보안 처리를 해야 한다.

---

# GET과 POST의 차이

| 구분 | GET | POST |
|---|---|---|
| 데이터 위치 | URL 쿼리 문자열 | 요청 본문 |
| 주요 목적 | 조회 | 생성 및 변경 |
| 주소 공유 | 쉬움 | 일반적으로 어려움 |
| 브라우저 기록 | 남을 수 있음 | 폼 데이터 자체는 URL에 표시되지 않음 |
| 민감 정보 | 부적합 | HTTPS와 함께 사용 |
| 대표 예 | 검색, 필터 | 로그인, 회원가입 |

GET과 POST는 단순히 보안 수준으로 구분하는 것이 아니라 요청의 목적과 의미를 기준으로 선택해야 한다.

---

# `name` 속성

`name`은 폼을 제출할 때 서버로 전달되는 데이터의 이름이다.

```html
<input
    type="text"
    name="userId"
>
```

사용자가 `developer`를 입력했다면 다음과 같은 형태로 전달될 수 있다.

```text
userId=developer
```

`name`이 없는 입력 요소는 일반적인 폼 제출에서 데이터가 전송되지 않는다.

## 잘못된 예

```html
<input
    type="text"
    id="user-id"
>
```

`id`는 있지만 `name`이 없다.

## 올바른 예

```html
<input
    type="text"
    id="user-id"
    name="userId"
>
```

`id`와 `name`은 역할이 다르다.

| 속성 | 역할 |
|---|---|
| `id` | 문서 안에서 요소 식별, `<label>` 연결 |
| `name` | 서버에 전달할 데이터 이름 |

---

# `value` 속성

`value`는 입력 요소의 초기값 또는 서버에 전달되는 값을 지정한다.

```html
<input
    type="text"
    name="nickname"
    value="developer"
>
```

라디오 버튼과 체크박스에서는 선택했을 때 전달할 값을 지정한다.

```html
<input
    type="radio"
    name="level"
    value="beginner"
>
```

```html
<input
    type="checkbox"
    name="skills"
    value="html"
>
```

---

# `<label>` 태그

`<label>`은 입력 요소의 이름이나 목적을 설명한다.

```html
<label for="user-id">
    아이디
</label>

<input
    type="text"
    id="user-id"
    name="userId"
>
```

`for` 값과 입력 요소의 `id` 값이 같아야 한다.

```text
label for="user-id"
input id="user-id"
```

레이블을 클릭하면 연결된 입력 요소에 포커스가 이동한다.

체크박스와 라디오 버튼에서는 레이블 영역까지 클릭할 수 있어 사용성이 좋아진다.

---

# 명시적 레이블 연결

`for`와 `id`를 사용하여 연결하는 방식이다.

```html
<label for="email">
    이메일
</label>

<input
    type="email"
    id="email"
    name="email"
>
```

실무에서 가장 명확하고 자주 사용하는 방식이다.

---

# 암시적 레이블 연결

입력 요소를 `<label>` 내부에 포함할 수도 있다.

```html
<label>
    이메일

    <input
        type="email"
        name="email"
    >
</label>
```

이 방식도 사용할 수 있지만 구조와 스타일링을 고려하여 프로젝트 전체에서 일관된 방식을 사용하는 것이 좋다.

---

# `placeholder`와 `label`의 차이

`placeholder`는 입력 예시나 형식을 안내하는 짧은 도움말이다.

```html
<input
    type="email"
    id="email"
    name="email"
    placeholder="example@email.com"
>
```

`placeholder`는 레이블을 대신할 수 없다.

## 좋지 않은 예

```html
<input
    type="email"
    name="email"
    placeholder="이메일"
>
```

사용자가 입력하면 placeholder가 사라져 필드의 목적을 확인하기 어려워진다.

## 권장 방식

```html
<label for="email">
    이메일
</label>

<input
    type="email"
    id="email"
    name="email"
    placeholder="example@email.com"
>
```

레이블은 입력 요소의 목적을 설명하고 placeholder는 입력 예시를 제공한다.

---

# `<input>` 태그

`<input>`은 다양한 형태의 사용자 입력을 받는 빈 요소이다.

```html
<input type="text">
```

`type` 속성에 따라 입력 방식과 브라우저 동작이 달라진다.

---

# 주요 `input` 타입

| 타입 | 역할 |
|---|---|
| `text` | 한 줄 텍스트 |
| `password` | 비밀번호 |
| `email` | 이메일 주소 |
| `search` | 검색어 |
| `tel` | 전화번호 |
| `url` | 웹 주소 |
| `number` | 숫자 |
| `date` | 날짜 |
| `time` | 시간 |
| `datetime-local` | 날짜와 시간 |
| `month` | 연도와 월 |
| `week` | 연도와 주 |
| `radio` | 하나만 선택 |
| `checkbox` | 여러 개 선택 |
| `file` | 파일 선택 |
| `range` | 범위 선택 |
| `color` | 색상 선택 |
| `hidden` | 화면에 보이지 않는 값 |
| `submit` | 폼 제출 |
| `reset` | 입력값 초기화 |
| `button` | 일반 버튼 |

---

# `type="text"`

한 줄 텍스트를 입력받는다.

```html
<label for="name">
    이름
</label>

<input
    type="text"
    id="name"
    name="name"
>
```

대표적인 사용 예는 다음과 같다.

- 이름
- 아이디
- 닉네임
- 제목
- 회사명
- 주소 일부

---

# `type="password"`

비밀번호를 입력받는다.

```html
<label for="password">
    비밀번호
</label>

<input
    type="password"
    id="password"
    name="password"
>
```

입력값이 화면에서 마스킹되어 표시된다.

화면에서 숨겨진다고 해서 데이터가 암호화되는 것은 아니다.

비밀번호는 HTTPS로 전송하고 서버에서 안전하게 해시 처리해야 한다.

---

# `type="email"`

이메일 주소를 입력받는다.

```html
<label for="email">
    이메일
</label>

<input
    type="email"
    id="email"
    name="email"
>
```

브라우저는 제출 시 이메일 형식을 기본적으로 검사할 수 있다.

모바일 환경에서는 이메일 입력에 적합한 키보드가 표시될 수 있다.

---

# `type="search"`

검색어를 입력받는다.

```html
<label for="site-search">
    사이트 검색
</label>

<input
    type="search"
    id="site-search"
    name="keyword"
>
```

일반 텍스트 입력과 비슷하지만 검색 목적의 필드라는 의미를 가진다.

---

# `type="tel"`

전화번호를 입력받는다.

```html
<label for="phone">
    전화번호
</label>

<input
    type="tel"
    id="phone"
    name="phone"
    placeholder="010-1234-5678"
>
```

`tel`은 전화번호 형식을 자동으로 완전히 검증하지 않는다.

국가와 서비스에 따라 전화번호 형식이 다양하기 때문이다.

필요한 경우 `pattern` 또는 JavaScript와 서버 검증을 함께 사용한다.

---

# `type="url"`

웹 주소를 입력받는다.

```html
<label for="portfolio-url">
    포트폴리오 주소
</label>

<input
    type="url"
    id="portfolio-url"
    name="portfolioUrl"
    placeholder="https://example.com"
>
```

브라우저는 URL 형식을 기본적으로 검사할 수 있다.

---

# `type="number"`

숫자를 입력받는다.

```html
<label for="age">
    나이
</label>

<input
    type="number"
    id="age"
    name="age"
    min="1"
    max="120"
>
```

숫자의 최소값, 최대값, 증감 단위를 지정할 수 있다.

```html
<input
    type="number"
    name="quantity"
    min="1"
    max="10"
    step="1"
>
```

전화번호, 우편번호, 주민번호처럼 계산하지 않는 숫자 문자열에는 `number`가 적합하지 않을 수 있다.

이러한 값은 `text` 또는 `tel`을 검토한다.

---

# `type="date"`

날짜를 입력받는다.

```html
<label for="birth-date">
    생년월일
</label>

<input
    type="date"
    id="birth-date"
    name="birthDate"
>
```

브라우저와 운영체제에 따라 날짜 선택 UI가 달라질 수 있다.

---

# `type="time"`

시간을 입력받는다.

```html
<label for="reservation-time">
    예약 시간
</label>

<input
    type="time"
    id="reservation-time"
    name="reservationTime"
>
```

---

# `type="datetime-local"`

사용자의 현지 날짜와 시간을 입력받는다.

```html
<label for="meeting-date">
    상담 일시
</label>

<input
    type="datetime-local"
    id="meeting-date"
    name="meetingDate"
>
```

시간대 정보는 포함하지 않으므로 서버에서 시간대 처리를 별도로 고려해야 한다.

---

# `type="radio"`

여러 항목 중 하나만 선택할 때 사용한다.

```html
<fieldset>
    <legend>교육 과정</legend>

    <label>
        <input
            type="radio"
            name="course"
            value="frontend"
        >

        프론트엔드
    </label>

    <label>
        <input
            type="radio"
            name="course"
            value="backend"
        >

        백엔드
    </label>
</fieldset>
```

같은 그룹의 라디오 버튼은 동일한 `name`을 사용해야 한다.

```text
name="course"
```

각 항목의 `value`는 서로 다르게 지정한다.

```text
value="frontend"
value="backend"
```

---

# 기본 선택된 라디오 버튼

`checked` 속성을 사용한다.

```html
<input
    type="radio"
    name="level"
    value="beginner"
    checked
>
```

같은 라디오 그룹에서는 하나만 기본 선택해야 한다.

---

# `type="checkbox"`

여러 항목을 동시에 선택할 때 사용한다.

```html
<fieldset>
    <legend>관심 기술</legend>

    <label>
        <input
            type="checkbox"
            name="skills"
            value="html"
        >

        HTML
    </label>

    <label>
        <input
            type="checkbox"
            name="skills"
            value="css"
        >

        CSS
    </label>

    <label>
        <input
            type="checkbox"
            name="skills"
            value="javascript"
        >

        JavaScript
    </label>
</fieldset>
```

여러 체크박스가 같은 `name`을 사용하면 선택된 값들이 같은 데이터 그룹으로 전달될 수 있다.

---

# 동의 체크박스

```html
<label>
    <input
        type="checkbox"
        name="termsAgreement"
        value="agreed"
        required
    >

    이용약관에 동의합니다.
</label>
```

필수 동의 항목에는 `required`를 사용할 수 있다.

선택 동의와 필수 동의를 명확하게 구분해야 한다.

---

# `type="file"`

사용자가 파일을 선택할 수 있다.

```html
<label for="profile-image">
    프로필 이미지
</label>

<input
    type="file"
    id="profile-image"
    name="profileImage"
>
```

허용할 파일 형식을 `accept`로 안내할 수 있다.

```html
<input
    type="file"
    name="profileImage"
    accept="image/png, image/jpeg, image/webp"
>
```

여러 파일을 선택하려면 `multiple`을 사용한다.

```html
<input
    type="file"
    name="attachments"
    multiple
>
```

파일 업로드 폼에서는 일반적으로 다음 인코딩 방식을 사용한다.

```html
<form
    action="/upload"
    method="post"
    enctype="multipart/form-data"
>
```

---

# `type="range"`

범위 안에서 값을 선택한다.

```html
<label for="satisfaction">
    만족도
</label>

<input
    type="range"
    id="satisfaction"
    name="satisfaction"
    min="1"
    max="10"
    value="5"
>
```

현재 선택값을 사용자에게 별도로 표시하면 이해하기 쉽다.

---

# `type="color"`

색상을 선택한다.

```html
<label for="theme-color">
    테마 색상
</label>

<input
    type="color"
    id="theme-color"
    name="themeColor"
    value="#000000"
>
```

---

# `type="hidden"`

화면에는 표시하지 않지만 서버에 함께 전달할 값을 지정한다.

```html
<input
    type="hidden"
    name="courseId"
    value="frontend-basic"
>
```

hidden 값은 사용자 화면에 보이지 않을 뿐 개발자 도구에서 확인하거나 수정할 수 있다.

보안이 필요한 값을 hidden 필드만으로 보호하면 안 된다.

서버는 전달된 값을 다시 검증해야 한다.

---

# 입력 관련 주요 속성

| 속성 | 역할 |
|---|---|
| `required` | 필수 입력 |
| `readonly` | 읽기 전용 |
| `disabled` | 비활성화 |
| `placeholder` | 입력 예시 |
| `minlength` | 최소 문자 수 |
| `maxlength` | 최대 문자 수 |
| `min` | 최소값 |
| `max` | 최대값 |
| `step` | 값의 증가 단위 |
| `pattern` | 정규 표현식 패턴 |
| `autocomplete` | 자동 완성 힌트 |
| `autofocus` | 페이지 로딩 시 자동 포커스 |
| `multiple` | 여러 값 선택 |
| `checked` | 기본 선택 |
| `accept` | 허용 파일 형식 |
| `inputmode` | 모바일 키보드 형태 힌트 |

---

# `required`

필수 입력 필드를 지정한다.

```html
<input
    type="email"
    name="email"
    required
>
```

값을 입력하지 않고 제출하면 브라우저가 기본 오류 메시지를 표시할 수 있다.

클라이언트의 `required`만으로는 충분하지 않다.

개발자 도구를 이용하면 제거하거나 우회할 수 있으므로 서버에서도 반드시 검증해야 한다.

---

# `readonly`

사용자가 값을 수정할 수 없도록 한다.

```html
<input
    type="text"
    name="memberId"
    value="developer01"
    readonly
>
```

`readonly` 값은 일반적으로 폼 제출에 포함된다.

---

# `disabled`

입력 요소를 비활성화한다.

```html
<input
    type="text"
    name="coupon"
    disabled
>
```

사용자가 입력하거나 포커스할 수 없으며 일반적인 폼 제출 데이터에도 포함되지 않는다.

---

# `readonly`와 `disabled`의 차이

| 구분 | `readonly` | `disabled` |
|---|---|---|
| 수정 | 불가능 | 불가능 |
| 포커스 | 가능할 수 있음 | 일반적으로 불가능 |
| 폼 제출 | 포함됨 | 포함되지 않음 |
| 대표 용도 | 수정 불가 정보 | 현재 사용할 수 없는 기능 |

---

# `minlength`와 `maxlength`

문자 입력 길이를 제한한다.

```html
<input
    type="text"
    name="nickname"
    minlength="2"
    maxlength="20"
>
```

```html
<textarea
    name="introduction"
    minlength="10"
    maxlength="500"
></textarea>
```

브라우저 검증과 별도로 서버에서도 길이를 검사해야 한다.

---

# `min`, `max`, `step`

숫자 또는 날짜 입력 범위를 지정할 수 있다.

```html
<input
    type="number"
    name="quantity"
    min="1"
    max="100"
    step="1"
>
```

```html
<input
    type="date"
    name="reservationDate"
    min="2026-07-21"
>
```

---

# `pattern`

정규 표현식을 이용해 입력 형식을 제한할 수 있다.

```html
<label for="member-code">
    회원 코드
</label>

<input
    type="text"
    id="member-code"
    name="memberCode"
    pattern="[A-Z]{3}-[0-9]{4}"
    placeholder="ABC-1234"
>
```

`pattern`만 제공하면 사용자가 요구 형식을 이해하기 어려울 수 있다.

레이블, 안내 문구, 오류 메시지를 함께 제공해야 한다.

---

# `autocomplete`

브라우저에 자동 완성 정보의 의미를 전달한다.

```html
<input
    type="email"
    name="email"
    autocomplete="email"
>
```

대표적인 값은 다음과 같다.

| 값 | 의미 |
|---|---|
| `name` | 전체 이름 |
| `given-name` | 이름 |
| `family-name` | 성 |
| `username` | 사용자 아이디 |
| `current-password` | 현재 비밀번호 |
| `new-password` | 새 비밀번호 |
| `email` | 이메일 |
| `tel` | 전화번호 |
| `street-address` | 주소 |
| `postal-code` | 우편번호 |
| `one-time-code` | 일회용 인증 코드 |

로그인 폼 예시는 다음과 같다.

```html
<input
    type="text"
    name="username"
    autocomplete="username"
>

<input
    type="password"
    name="password"
    autocomplete="current-password"
>
```

회원가입 비밀번호는 다음과 같이 작성할 수 있다.

```html
<input
    type="password"
    name="password"
    autocomplete="new-password"
>
```

---

# `inputmode`

모바일에서 표시할 가상 키보드의 형태를 힌트로 제공한다.

```html
<input
    type="text"
    name="verificationCode"
    inputmode="numeric"
>
```

대표적인 값은 다음과 같다.

| 값 | 용도 |
|---|---|
| `text` | 일반 텍스트 |
| `numeric` | 숫자 |
| `decimal` | 소수점 숫자 |
| `tel` | 전화번호 |
| `email` | 이메일 |
| `url` | URL |
| `search` | 검색 |

`inputmode`는 입력값 검증 기능이 아니다.

사용자에게 적절한 키보드를 제공하는 힌트이다.

---

# `autofocus`

페이지가 열릴 때 입력 요소에 자동으로 포커스를 이동한다.

```html
<input
    type="search"
    name="keyword"
    autofocus
>
```

과도하게 사용하면 화면 낭독기 사용자나 모바일 사용자에게 혼란을 줄 수 있다.

한 페이지에서 신중하게 사용해야 한다.

---

# `<textarea>`

여러 줄 텍스트를 입력받는다.

```html
<label for="message">
    문의 내용
</label>

<textarea
    id="message"
    name="message"
    rows="6"
    cols="40"
></textarea>
```

대표적인 사용 예는 다음과 같다.

- 게시글 본문
- 자기소개
- 문의 내용
- 후기
- 댓글

초기값은 `value` 속성이 아니라 시작 태그와 종료 태그 사이에 작성한다.

```html
<textarea name="message">초기 내용</textarea>
```

들여쓰기나 줄바꿈도 값에 포함될 수 있으므로 초기값이 필요하지 않다면 태그 사이를 비워 두는 것이 좋다.

---

# `<select>`

여러 선택지 중 하나 또는 여러 개를 선택할 수 있는 목록을 만든다.

```html
<label for="course">
    교육 과정
</label>

<select
    id="course"
    name="course"
>
    <option value="frontend">
        프론트엔드
    </option>

    <option value="backend">
        백엔드
    </option>
</select>
```

---

# `<option>`

`<select>` 내부의 각 선택 항목을 나타낸다.

```html
<option value="frontend">
    프론트엔드
</option>
```

사용자에게 표시되는 내용과 서버에 전달되는 값을 다르게 지정할 수 있다.

```text
표시: 프론트엔드
전달: frontend
```

---

# 안내용 기본 옵션

```html
<select
    id="course"
    name="course"
    required
>
    <option value="" selected disabled>
        교육 과정을 선택하세요
    </option>

    <option value="frontend">
        프론트엔드
    </option>

    <option value="backend">
        백엔드
    </option>
</select>
```

빈 값을 가진 안내 옵션을 제공하고 필수 선택에는 `required`를 사용할 수 있다.

---

# `selected`

기본 선택할 옵션을 지정한다.

```html
<option
    value="frontend"
    selected
>
    프론트엔드
</option>
```

---

# 여러 옵션 선택

`multiple`을 사용한다.

```html
<label for="skills">
    관심 기술
</label>

<select
    id="skills"
    name="skills"
    multiple
>
    <option value="html">HTML</option>
    <option value="css">CSS</option>
    <option value="javascript">JavaScript</option>
</select>
```

데스크톱에서는 보조 키를 사용해야 할 수 있어 사용 방법이 직관적이지 않을 수 있다.

선택지가 많지 않다면 체크박스가 더 적절할 수 있다.

---

# `<optgroup>`

관련 옵션을 그룹으로 묶는다.

```html
<select name="course">
    <optgroup label="Frontend">
        <option value="html">HTML</option>
        <option value="css">CSS</option>
        <option value="javascript">JavaScript</option>
    </optgroup>

    <optgroup label="Backend">
        <option value="java">Java</option>
        <option value="spring">Spring</option>
    </optgroup>
</select>
```

---

# `<button>`

버튼은 폼 제출, 초기화 또는 일반 동작 실행에 사용한다.

```html
<button type="submit">
    제출
</button>
```

대표적인 타입은 다음과 같다.

| 값 | 역할 |
|---|---|
| `submit` | 폼 제출 |
| `reset` | 입력값 초기화 |
| `button` | 기본 동작 없는 일반 버튼 |

---

# `type="submit"`

폼 데이터를 제출한다.

```html
<button type="submit">
    회원가입
</button>
```

폼 내부의 `<button>`은 브라우저에 따라 기본값이 `submit`으로 동작할 수 있으므로 `type`을 명시하는 것이 좋다.

---

# `type="button"`

JavaScript로 별도의 동작을 구현할 때 사용한다.

```html
<button
    type="button"
    id="password-toggle"
>
    비밀번호 표시
</button>
```

폼을 제출하지 않는 버튼에는 `type="button"`을 명시한다.

---

# `type="reset"`

폼 입력값을 초기 상태로 되돌린다.

```html
<button type="reset">
    초기화
</button>
```

사용자가 작성한 내용을 실수로 모두 지울 수 있으므로 실무에서는 신중하게 사용한다.

---

# `<input type="submit">`과 `<button>`

다음 방식으로도 제출 버튼을 만들 수 있다.

```html
<input
    type="submit"
    value="회원가입"
>
```

일반적으로 `<button>`은 내부에 텍스트와 아이콘 등 다양한 콘텐츠를 넣을 수 있어 더 유연하다.

```html
<button type="submit">
    <span aria-hidden="true">✓</span>
    회원가입
</button>
```

---

# `<fieldset>`

관련된 폼 요소를 하나의 그룹으로 묶는다.

```html
<fieldset>
    <legend>회원 정보</legend>

    <label for="name">
        이름
    </label>

    <input
        type="text"
        id="name"
        name="name"
    >
</fieldset>
```

라디오 버튼과 체크박스 그룹에서 특히 유용하다.

---

# `<legend>`

`<fieldset>` 그룹의 제목을 제공한다.

```html
<fieldset>
    <legend>수강 희망 과정</legend>

    <label>
        <input
            type="radio"
            name="course"
            value="frontend"
        >

        프론트엔드
    </label>

    <label>
        <input
            type="radio"
            name="course"
            value="backend"
        >

        백엔드
    </label>
</fieldset>
```

각 항목의 레이블만으로는 그룹 전체의 질문을 알기 어려우므로 `legend`를 사용한다.

---

# `<datalist>`

사용자에게 추천 입력값을 제공한다.

```html
<label for="technology">
    관심 기술
</label>

<input
    type="text"
    id="technology"
    name="technology"
    list="technology-list"
>

<datalist id="technology-list">
    <option value="HTML">
    <option value="CSS">
    <option value="JavaScript">
    <option value="React">
</datalist>
```

`select`와 달리 사용자가 목록에 없는 값을 직접 입력할 수 있다.

---

# `<output>`

계산이나 사용자 동작의 결과를 나타낼 수 있다.

```html
<form
    oninput="result.value = Number(first.value) + Number(second.value)"
>
    <input
        type="number"
        id="first"
        name="first"
        value="0"
    >

    <span>+</span>

    <input
        type="number"
        id="second"
        name="second"
        value="0"
    >

    <span>=</span>

    <output
        name="result"
        for="first second"
    >
        0
    </output>
</form>
```

실무에서는 인라인 JavaScript보다 별도의 JavaScript 파일에서 이벤트를 처리하는 방식이 일반적이다.

---

# 폼 유효성 검사

유효성 검사는 사용자가 입력한 값이 요구 조건에 맞는지 확인하는 과정이다.

HTML은 다음 속성을 이용한 기본 검증 기능을 제공한다.

- `required`
- `type="email"`
- `type="url"`
- `minlength`
- `maxlength`
- `min`
- `max`
- `step`
- `pattern`

```html
<input
    type="email"
    name="email"
    required
>
```

```html
<input
    type="password"
    name="password"
    minlength="8"
    required
>
```

---

# 클라이언트 검증과 서버 검증

HTML과 JavaScript에서 수행하는 검증은 사용자 경험을 개선한다.

하지만 클라이언트 검증은 사용자가 우회하거나 조작할 수 있다.

따라서 서버에서도 모든 값을 다시 검증해야 한다.

```text
사용자 입력
    ↓
HTML 기본 검증
    ↓
JavaScript 추가 검증
    ↓
서버 최종 검증
    ↓
데이터 저장
```

서버 검증은 선택이 아니라 필수이다.

---

# `novalidate`

브라우저의 기본 유효성 검사를 비활성화한다.

```html
<form
    action="/members"
    method="post"
    novalidate
>
```

커스텀 검증 UI를 구현할 때 사용할 수 있다.

하지만 `novalidate`를 사용했다면 JavaScript와 서버에서 검증을 정확하게 구현해야 한다.

---

# `formnovalidate`

특정 제출 버튼에서만 기본 검증을 생략한다.

```html
<button
    type="submit"
    formnovalidate
>
    임시 저장
</button>
```

완성되지 않은 내용을 임시 저장하는 기능 등에 사용할 수 있다.

---

# 폼 인코딩 방식

`enctype`은 폼 데이터를 인코딩하는 방식을 지정한다.

대표적인 값은 다음과 같다.

| 값 | 용도 |
|---|---|
| `application/x-www-form-urlencoded` | 기본 폼 데이터 |
| `multipart/form-data` | 파일 업로드 |
| `text/plain` | 일반적으로 실무 전송에는 거의 사용하지 않음 |

파일 업로드 예시는 다음과 같다.

```html
<form
    action="/profile"
    method="post"
    enctype="multipart/form-data"
>
    <input
        type="file"
        name="profileImage"
    >

    <button type="submit">
        업로드
    </button>
</form>
```

---

# 폼과 접근성

## 모든 입력 요소에 이름 제공하기

가능하면 시각적으로 확인할 수 있는 `<label>`을 제공한다.

```html
<label for="email">
    이메일
</label>

<input
    type="email"
    id="email"
    name="email"
>
```

---

## 관련 선택지를 그룹으로 묶기

```html
<fieldset>
    <legend>연락 방법</legend>

    <label>
        <input
            type="radio"
            name="contactMethod"
            value="email"
        >

        이메일
    </label>

    <label>
        <input
            type="radio"
            name="contactMethod"
            value="phone"
        >

        전화
    </label>
</fieldset>
```

---

## 필수 입력 안내하기

`required`만 사용하는 것보다 화면에서도 필수 여부를 명확하게 표시한다.

```html
<label for="name">
    이름
    <span aria-hidden="true">*</span>
</label>

<input
    type="text"
    id="name"
    name="name"
    required
    aria-describedby="name-required"
>

<p id="name-required">
    필수 입력 항목입니다.
</p>
```

별표만으로 필수 여부를 표현하면 의미를 이해하기 어려울 수 있으므로 설명을 함께 제공한다.

---

## 도움말 연결하기

`aria-describedby`를 사용해 입력 요소와 안내 문구를 연결할 수 있다.

```html
<label for="password">
    비밀번호
</label>

<input
    type="password"
    id="password"
    name="password"
    minlength="8"
    aria-describedby="password-help"
>

<p id="password-help">
    영문, 숫자를 포함하여 8자 이상 입력하세요.
</p>
```

---

## 오류 메시지 연결하기

```html
<label for="email">
    이메일
</label>

<input
    type="email"
    id="email"
    name="email"
    aria-invalid="true"
    aria-describedby="email-error"
>

<p id="email-error">
    올바른 이메일 주소를 입력하세요.
</p>
```

오류가 없는 상태에서 무조건 `aria-invalid="true"`를 작성하면 안 된다.

검증 결과에 따라 동적으로 변경해야 한다.

---

## 색상만으로 오류를 표시하지 않기

테두리 색상만 빨간색으로 변경하는 것으로는 충분하지 않다.

오류 아이콘과 명확한 텍스트 메시지를 함께 제공한다.

```html
<p class="error-message">
    이메일 주소 형식을 확인해 주세요.
</p>
```

---

## 키보드로 사용할 수 있어야 한다

입력 요소와 버튼은 기본 HTML 요소를 사용하면 키보드 접근성을 자연스럽게 제공한다.

클릭 가능한 기능을 `<div>`로 구현하는 방식은 피한다.

```html
<button type="button">
    주소 검색
</button>
```

---

# 로그인 폼 예제

```html
<form
    action="/login"
    method="post"
>
    <div>
        <label for="login-id">
            아이디
        </label>

        <input
            type="text"
            id="login-id"
            name="username"
            autocomplete="username"
            required
        >
    </div>

    <div>
        <label for="login-password">
            비밀번호
        </label>

        <input
            type="password"
            id="login-password"
            name="password"
            autocomplete="current-password"
            required
        >
    </div>

    <label>
        <input
            type="checkbox"
            name="rememberLogin"
            value="true"
        >

        로그인 상태 유지
    </label>

    <button type="submit">
        로그인
    </button>
</form>
```

---

# 검색 폼 예제

```html
<form
    action="/search"
    method="get"
    role="search"
>
    <label for="search-keyword">
        검색어
    </label>

    <input
        type="search"
        id="search-keyword"
        name="keyword"
        placeholder="검색어를 입력하세요"
    >

    <button type="submit">
        검색
    </button>
</form>
```

검색 조건은 URL로 공유할 수 있어야 하므로 GET 방식이 적절한 경우가 많다.

---

# 문의 폼 예제

```html
<form
    action="/inquiries"
    method="post"
>
    <div>
        <label for="inquiry-name">
            이름
        </label>

        <input
            type="text"
            id="inquiry-name"
            name="name"
            autocomplete="name"
            required
        >
    </div>

    <div>
        <label for="inquiry-email">
            이메일
        </label>

        <input
            type="email"
            id="inquiry-email"
            name="email"
            autocomplete="email"
            required
        >
    </div>

    <div>
        <label for="inquiry-type">
            문의 유형
        </label>

        <select
            id="inquiry-type"
            name="inquiryType"
            required
        >
            <option value="" selected disabled>
                문의 유형을 선택하세요
            </option>

            <option value="course">
                교육 과정
            </option>

            <option value="payment">
                결제
            </option>

            <option value="employment">
                취업 지원
            </option>
        </select>
    </div>

    <div>
        <label for="inquiry-message">
            문의 내용
        </label>

        <textarea
            id="inquiry-message"
            name="message"
            rows="8"
            minlength="10"
            maxlength="1000"
            required
        ></textarea>
    </div>

    <button type="submit">
        문의 등록
    </button>
</form>
```

---

# 실무 예제 프로젝트

다음은 Developer Academy의 수강 신청 폼 예제이다.

```html
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">

    <meta
        name="viewport"
        content="width=device-width, initial-scale=1.0"
    >

    <title>수강 신청 | Developer Academy</title>
</head>
<body>
    <header>
        <a href="./index.html">
            Developer Academy
        </a>

        <nav aria-label="주요 메뉴">
            <ul>
                <li>
                    <a href="./courses.html">
                        교육 과정
                    </a>
                </li>

                <li>
                    <a href="./projects.html">
                        실무 프로젝트
                    </a>
                </li>

                <li>
                    <a
                        href="./apply.html"
                        aria-current="page"
                    >
                        수강 신청
                    </a>
                </li>
            </ul>
        </nav>
    </header>

    <main>
        <section aria-labelledby="apply-title">
            <h1 id="apply-title">
                웹 개발자 과정 수강 신청
            </h1>

            <p>
                신청 정보를 작성하면 담당자가 확인 후
                상담 일정을 안내합니다.
            </p>

            <p>
                별표(*)가 표시된 항목은 필수입니다.
            </p>

            <form
                action="/applications"
                method="post"
                enctype="multipart/form-data"
            >
                <fieldset>
                    <legend>
                        기본 정보
                    </legend>

                    <div>
                        <label for="applicant-name">
                            이름
                            <span aria-hidden="true">*</span>
                        </label>

                        <input
                            type="text"
                            id="applicant-name"
                            name="name"
                            autocomplete="name"
                            required
                        >
                    </div>

                    <div>
                        <label for="applicant-email">
                            이메일
                            <span aria-hidden="true">*</span>
                        </label>

                        <input
                            type="email"
                            id="applicant-email"
                            name="email"
                            autocomplete="email"
                            placeholder="example@email.com"
                            required
                        >
                    </div>

                    <div>
                        <label for="applicant-phone">
                            전화번호
                            <span aria-hidden="true">*</span>
                        </label>

                        <input
                            type="tel"
                            id="applicant-phone"
                            name="phone"
                            autocomplete="tel"
                            inputmode="tel"
                            placeholder="010-1234-5678"
                            required
                        >
                    </div>

                    <div>
                        <label for="birth-date">
                            생년월일
                        </label>

                        <input
                            type="date"
                            id="birth-date"
                            name="birthDate"
                        >
                    </div>
                </fieldset>

                <fieldset>
                    <legend>
                        희망 교육 과정
                    </legend>

                    <label>
                        <input
                            type="radio"
                            name="course"
                            value="frontend"
                            required
                        >

                        프론트엔드 개발
                    </label>

                    <label>
                        <input
                            type="radio"
                            name="course"
                            value="backend"
                        >

                        백엔드 개발
                    </label>

                    <label>
                        <input
                            type="radio"
                            name="course"
                            value="fullstack"
                        >

                        풀스택 개발
                    </label>
                </fieldset>

                <fieldset>
                    <legend>
                        학습 경험
                    </legend>

                    <p>
                        경험한 기술을 모두 선택하세요.
                    </p>

                    <label>
                        <input
                            type="checkbox"
                            name="experiencedSkills"
                            value="html"
                        >

                        HTML
                    </label>

                    <label>
                        <input
                            type="checkbox"
                            name="experiencedSkills"
                            value="css"
                        >

                        CSS
                    </label>

                    <label>
                        <input
                            type="checkbox"
                            name="experiencedSkills"
                            value="javascript"
                        >

                        JavaScript
                    </label>

                    <label>
                        <input
                            type="checkbox"
                            name="experiencedSkills"
                            value="java"
                        >

                        Java
                    </label>
                </fieldset>

                <fieldset>
                    <legend>
                        상담 정보
                    </legend>

                    <div>
                        <label for="consultation-date">
                            희망 상담 일시
                        </label>

                        <input
                            type="datetime-local"
                            id="consultation-date"
                            name="consultationDate"
                        >
                    </div>

                    <div>
                        <label for="contact-method">
                            선호 연락 방법
                        </label>

                        <select
                            id="contact-method"
                            name="contactMethod"
                        >
                            <option value="phone">
                                전화
                            </option>

                            <option value="email">
                                이메일
                            </option>

                            <option value="message">
                                문자 메시지
                            </option>
                        </select>
                    </div>

                    <div>
                        <label for="application-message">
                            지원 동기
                            <span aria-hidden="true">*</span>
                        </label>

                        <textarea
                            id="application-message"
                            name="message"
                            rows="8"
                            minlength="20"
                            maxlength="1000"
                            aria-describedby="message-help"
                            required
                        ></textarea>

                        <p id="message-help">
                            학습 목표와 지원 동기를
                            20자 이상 작성하세요.
                        </p>
                    </div>

                    <div>
                        <label for="portfolio-file">
                            포트폴리오 파일
                        </label>

                        <input
                            type="file"
                            id="portfolio-file"
                            name="portfolioFile"
                            accept=".pdf,.zip"
                        >
                    </div>
                </fieldset>

                <fieldset>
                    <legend>
                        약관 동의
                    </legend>

                    <label>
                        <input
                            type="checkbox"
                            name="privacyAgreement"
                            value="agreed"
                            required
                        >

                        개인정보 수집 및 이용에 동의합니다.
                    </label>

                    <label>
                        <input
                            type="checkbox"
                            name="marketingAgreement"
                            value="agreed"
                        >

                        교육 및 취업 정보 수신에 동의합니다.
                        선택 사항입니다.
                    </label>
                </fieldset>

                <input
                    type="hidden"
                    name="applicationSource"
                    value="website"
                >

                <button type="submit">
                    수강 신청 제출
                </button>

                <button type="button">
                    작성 내용 임시 저장
                </button>
            </form>
        </section>
    </main>
</body>
</html>
```

---

# 예제 구조 분석

```text
main
└── section
    ├── h1
    ├── p
    └── form
        ├── fieldset
        │   ├── legend
        │   ├── label
        │   └── input
        ├── fieldset
        │   ├── legend
        │   └── input[type="radio"]
        ├── fieldset
        │   ├── legend
        │   └── input[type="checkbox"]
        ├── fieldset
        │   ├── legend
        │   ├── input[type="datetime-local"]
        │   ├── select
        │   ├── textarea
        │   └── input[type="file"]
        ├── fieldset
        │   ├── legend
        │   └── input[type="checkbox"]
        ├── input[type="hidden"]
        ├── button[type="submit"]
        └── button[type="button"]
```

---

# 예제에서 확인할 내용

- 폼 전체를 `<form>`으로 묶었다.
- 회원 정보와 선택 항목을 `<fieldset>`으로 구분했다.
- 각 입력 요소에 `<label>`을 연결했다.
- 서버로 전송할 모든 입력 요소에 `name`을 지정했다.
- 회원가입 성격의 요청이므로 POST 방식을 사용했다.
- 파일 업로드를 위해 `multipart/form-data`를 사용했다.
- 라디오 버튼은 같은 `name`으로 하나의 그룹을 만들었다.
- 체크박스는 여러 값을 선택할 수 있게 구성했다.
- 필수 항목에는 `required`를 사용했다.
- 도움말은 `aria-describedby`로 입력 요소와 연결했다.
- 제출 버튼과 일반 기능 버튼의 타입을 구분했다.
- hidden 값은 서버에서 다시 검증해야 한다.

---

# 이번 문서에서 새롭게 배운 내용

| 개념 또는 요소 | 설명 |
|---|---|
| `<form>` | 사용자 입력을 제출 단위로 묶는 요소 |
| `action` | 폼 데이터를 전송할 주소 |
| `method` | GET 또는 POST 전송 방식 |
| `name` | 서버로 전달되는 데이터 이름 |
| `value` | 입력값 또는 제출값 |
| `<label>` | 입력 요소의 이름과 설명 |
| `for` | 레이블과 입력 요소 연결 |
| `<input>` | 다양한 한 줄 입력 요소 |
| `type` | 입력 방식 지정 |
| `required` | 필수 입력 |
| `readonly` | 수정 불가, 제출 포함 |
| `disabled` | 비활성화, 제출 제외 |
| `placeholder` | 입력 예시 |
| `autocomplete` | 자동 완성 의미 제공 |
| `inputmode` | 모바일 키보드 힌트 |
| `pattern` | 입력 패턴 지정 |
| `<textarea>` | 여러 줄 텍스트 입력 |
| `<select>` | 선택 목록 |
| `<option>` | 선택 항목 |
| `<optgroup>` | 선택 항목 그룹 |
| `<button>` | 제출 또는 일반 동작 |
| `<fieldset>` | 관련 입력 그룹 |
| `<legend>` | 입력 그룹의 제목 |
| `<datalist>` | 추천 입력값 목록 |
| `<output>` | 계산 또는 동작 결과 |
| `enctype` | 폼 데이터 인코딩 방식 |
| `multipart/form-data` | 파일 업로드용 인코딩 |
| 클라이언트 검증 | 브라우저와 JavaScript 검증 |
| 서버 검증 | 서버에서 수행하는 최종 검증 |

---

# 자주 하는 실수

## 1. `name`을 작성하지 않는다

```html
<input
    type="text"
    id="user-id"
>
```

`id`가 있어도 `name`이 없으면 일반적인 폼 제출에 값이 포함되지 않는다.

```html
<input
    type="text"
    id="user-id"
    name="userId"
>
```

---

## 2. `id`와 `name`을 같은 개념으로 생각한다

`id`는 HTML 문서 안에서 요소를 식별하고 레이블과 연결한다.

`name`은 서버에 전달할 데이터 이름이다.

두 속성은 값이 같을 수도 있지만 역할은 다르다.

---

## 3. `placeholder`를 레이블 대신 사용한다

```html
<input
    type="text"
    placeholder="이름"
>
```

입력 후 placeholder가 사라져 필드의 목적을 확인하기 어렵다.

```html
<label for="name">
    이름
</label>

<input
    type="text"
    id="name"
    name="name"
    placeholder="홍길동"
>
```

---

## 4. 라디오 버튼마다 다른 `name`을 사용한다

### 잘못된 예

```html
<input
    type="radio"
    name="frontend"
    value="frontend"
>

<input
    type="radio"
    name="backend"
    value="backend"
>
```

두 항목을 동시에 선택할 수 있게 된다.

### 올바른 예

```html
<input
    type="radio"
    name="course"
    value="frontend"
>

<input
    type="radio"
    name="course"
    value="backend"
>
```

---

## 5. 체크박스와 라디오 버튼에 `value`를 지정하지 않는다

```html
<input
    type="checkbox"
    name="skills"
>
```

브라우저 기본값이 전달될 수 있어 의미를 알기 어렵다.

```html
<input
    type="checkbox"
    name="skills"
    value="html"
>
```

---

## 6. 버튼의 `type`을 생략한다

```html
<form>
    <button>
        비밀번호 보기
    </button>
</form>
```

폼이 의도치 않게 제출될 수 있다.

```html
<button type="button">
    비밀번호 보기
</button>
```

---

## 7. 폼 제출 버튼을 링크로 구현한다

```html
<a href="#">
    회원가입
</a>
```

폼 제출은 버튼을 사용한다.

```html
<button type="submit">
    회원가입
</button>
```

---

## 8. 페이지 이동을 submit 버튼으로 구현한다

다른 페이지 이동이 목적이라면 `<a>`를 사용해야 한다.

```html
<a href="./login.html">
    로그인 페이지로 이동
</a>
```

---

## 9. 파일 업로드 폼에 `multipart/form-data`를 작성하지 않는다

```html
<form
    action="/upload"
    method="post"
>
```

파일 업로드에는 다음 형식을 사용한다.

```html
<form
    action="/upload"
    method="post"
    enctype="multipart/form-data"
>
```

---

## 10. 비밀번호를 GET 방식으로 전송한다

```html
<form
    action="/login"
    method="get"
>
```

URL에 값이 노출될 수 있다.

로그인과 회원가입은 일반적으로 POST와 HTTPS를 사용한다.

---

## 11. POST를 사용하면 자동으로 안전하다고 생각한다

POST 데이터도 암호화된 것은 아니다.

HTTPS를 사용하고 서버에서 인증, 권한, 검증, 비밀번호 해시 처리를 해야 한다.

---

## 12. HTML 검증만 신뢰한다

`required`나 `pattern`은 개발자 도구로 우회할 수 있다.

서버에서 반드시 다시 검증한다.

---

## 13. 전화번호에 `type="number"`를 사용한다

전화번호는 계산 대상이 아니며 앞자리 0과 특수문자가 필요할 수 있다.

```html
<input
    type="tel"
    name="phone"
>
```

---

## 14. 우편번호에 `type="number"`를 사용한다

우편번호도 숫자 계산 대상이 아니라 식별 문자열이다.

```html
<input
    type="text"
    name="postalCode"
    inputmode="numeric"
>
```

---

## 15. `disabled` 값을 서버로 전달될 것이라 생각한다

`disabled` 요소는 일반적인 폼 제출에서 제외된다.

값을 전송해야 한다면 `readonly` 또는 hidden 입력과 서버 검증을 고려한다.

---

## 16. `readonly`와 `disabled`를 구분하지 않는다

`readonly`는 수정할 수 없지만 값이 제출된다.

`disabled`는 비활성화되고 값이 제출되지 않는다.

---

## 17. 선택 그룹에 제목을 제공하지 않는다

```html
<label>
    <input type="radio" name="course">
    프론트엔드
</label>
```

각 항목은 알 수 있지만 무엇을 선택하는 그룹인지 불명확할 수 있다.

```html
<fieldset>
    <legend>희망 교육 과정</legend>

    <!-- 라디오 버튼 -->
</fieldset>
```

---

## 18. 오류를 색상만으로 표시한다

빨간 테두리만 표시하지 말고 구체적인 오류 메시지를 함께 제공한다.

---

## 19. 모든 입력 필드에 `autofocus`를 사용한다

한 페이지에서 여러 `autofocus`를 사용하거나 자동 포커스를 남용하면 사용자 흐름을 방해할 수 있다.

---

## 20. hidden 필드를 신뢰한다

hidden 필드는 화면에만 보이지 않을 뿐 사용자가 수정할 수 있다.

가격, 권한, 회원 등급과 같은 값은 서버에서 신뢰하지 말고 다시 확인한다.

---

## 21. textarea 초기값에 불필요한 공백을 넣는다

```html
<textarea name="message">
    내용을 입력하세요.
</textarea>
```

줄바꿈과 공백이 실제 값에 포함될 수 있다.

placeholder가 필요하면 다음처럼 작성한다.

```html
<textarea
    name="message"
    placeholder="내용을 입력하세요."
></textarea>
```

---

## 22. reset 버튼을 쉽게 배치한다

사용자가 작성한 내용을 실수로 모두 지울 수 있다.

초기화 기능이 정말 필요한지 검토하고, 필요하다면 확인 절차를 고려한다.

---

# 면접 포인트

## Q1. `<form>` 태그는 어떤 역할을 하나요?

사용자가 입력하거나 선택한 데이터를 하나의 제출 단위로 묶고 서버로 전송하는 역할을 한다.

`action`으로 전송 주소를 지정하고 `method`로 전송 방식을 지정할 수 있다.

---

## Q2. GET과 POST의 차이는 무엇인가요?

GET은 데이터를 URL 쿼리 문자열에 포함하며 주로 조회, 검색, 필터에 사용한다.

POST는 데이터를 요청 본문에 포함하며 회원가입, 로그인, 데이터 생성과 변경에 주로 사용한다.

요청의 목적과 HTTP 의미를 기준으로 선택해야 한다.

---

## Q3. `id`와 `name`의 차이는 무엇인가요?

`id`는 문서 안에서 요소를 식별하고 `<label>`의 `for`와 연결하는 데 사용한다.

`name`은 폼 제출 시 서버로 전달되는 데이터의 이름이다.

---

## Q4. `<label>`이 필요한 이유는 무엇인가요?

입력 요소의 목적을 사용자와 보조 기술에 전달한다.

레이블을 클릭하면 연결된 입력 요소에 포커스가 이동하여 사용성도 좋아진다.

---

## Q5. placeholder가 label을 대체할 수 있나요?

대체할 수 없다.

placeholder는 입력 중 사라지고 대비가 낮을 수 있으며 입력 필드의 지속적인 이름을 제공하지 못한다.

레이블은 유지하고 placeholder는 입력 예시나 형식 안내에 사용한다.

---

## Q6. 라디오 버튼과 체크박스의 차이는 무엇인가요?

라디오 버튼은 같은 그룹에서 하나만 선택할 때 사용한다.

체크박스는 여러 항목을 독립적으로 선택할 때 사용한다.

라디오 그룹은 동일한 `name`을 사용해야 한다.

---

## Q7. `readonly`와 `disabled`의 차이는 무엇인가요?

`readonly`는 사용자가 수정할 수 없지만 일반적으로 값이 제출된다.

`disabled`는 사용할 수 없으며 일반적인 폼 제출에서 값도 제외된다.

---

## Q8. `<fieldset>`과 `<legend>`는 왜 사용하나요?

관련 입력 요소를 하나의 의미 있는 그룹으로 묶고 그룹의 제목을 제공한다.

라디오 버튼, 체크박스, 주소 정보, 회원 정보 등을 구조적으로 설명하는 데 유용하다.

---

## Q9. 폼 내부 버튼의 `type`을 명시해야 하는 이유는 무엇인가요?

폼 내부의 버튼은 기본적으로 제출 버튼처럼 동작할 수 있다.

제출 버튼은 `submit`, 일반 기능 버튼은 `button`으로 명시하면 의도하지 않은 폼 제출을 방지할 수 있다.

---

## Q10. HTML 기본 유효성 검사만 사용하면 충분한가요?

충분하지 않다.

HTML 검증은 사용자 경험 개선에 도움이 되지만 우회할 수 있으므로 서버에서 모든 값을 다시 검증해야 한다.

---

## Q11. 파일 업로드 폼에서 필요한 설정은 무엇인가요?

일반적으로 `method="post"`와 `enctype="multipart/form-data"`를 사용한다.

파일 입력은 `<input type="file">`로 구성한다.

---

## Q12. `autocomplete`은 왜 사용하나요?

브라우저와 비밀번호 관리자에 입력 정보의 의미를 전달한다.

사용자는 저장된 이름, 이메일, 주소, 비밀번호 등을 더 빠르고 정확하게 입력할 수 있다.

---

## Q13. `inputmode`는 무엇인가요?

모바일 환경에서 어떤 형태의 가상 키보드를 표시할지 힌트를 제공한다.

입력값 검증 기능은 아니므로 별도의 검증이 필요하다.

---

## Q14. `select`와 `datalist`의 차이는 무엇인가요?

`select`는 제공된 옵션 중에서 선택한다.

`datalist`는 추천 목록을 제공하지만 사용자가 목록에 없는 값도 직접 입력할 수 있다.

---

## Q15. 클라이언트 검증과 서버 검증의 차이는 무엇인가요?

클라이언트 검증은 브라우저에서 빠른 피드백을 제공하여 사용자 경험을 개선한다.

서버 검증은 조작된 요청과 잘못된 데이터를 차단하는 최종 검증이며 반드시 수행해야 한다.

---

# 핵심 정리

- `<form>`은 사용자 입력 요소를 하나의 제출 단위로 묶는다.
- `action`은 전송 주소, `method`는 전송 방식을 지정한다.
- GET은 조회와 검색, POST는 생성과 변경에 주로 사용한다.
- POST 자체가 데이터를 암호화하지 않으므로 HTTPS가 필요하다.
- `name`은 서버에 전달되는 데이터 이름이다.
- `id`는 요소 식별과 레이블 연결에 사용한다.
- 모든 입력 요소에는 의미 있는 `<label>`을 제공하는 것이 좋다.
- placeholder는 레이블을 대신할 수 없다.
- `<input>`의 `type`에 따라 입력 방식과 기본 검증이 달라진다.
- 라디오 버튼은 하나만 선택하고 체크박스는 여러 개 선택할 수 있다.
- 같은 라디오 그룹은 동일한 `name`을 사용한다.
- `<textarea>`는 여러 줄 텍스트 입력에 사용한다.
- `<select>`와 `<option>`은 선택 목록을 구성한다.
- `<fieldset>`과 `<legend>`는 관련 입력 그룹을 설명한다.
- 제출 버튼은 `type="submit"`을 사용한다.
- 폼 제출이 아닌 일반 버튼에는 `type="button"`을 명시한다.
- `readonly` 값은 제출되지만 `disabled` 값은 일반적으로 제출되지 않는다.
- 파일 업로드에는 `multipart/form-data`가 필요하다.
- `required`, `pattern`, `minlength` 등으로 기본 검증을 제공할 수 있다.
- HTML과 JavaScript 검증은 우회할 수 있으므로 서버 검증이 필수이다.
- 오류 메시지는 입력 요소와 연결하고 색상뿐 아니라 텍스트로도 제공한다.
- 폼은 키보드와 화면 낭독기로 사용할 수 있도록 구성해야 한다.

---

# 변경 이력

| Version | 날짜 | 변경 내용 |
|---|---|---|
| v1.0 | 2026-07-21 | HTML 폼 태그 문서 최초 작성 |
| v1.0 | 2026-07-21 | `form`, `action`, `method` 기본 구조 추가 |
| v1.0 | 2026-07-21 | GET과 POST의 차이 정리 |
| v1.0 | 2026-07-21 | `label`, `id`, `name`, `value` 역할 추가 |
| v1.0 | 2026-07-21 | 주요 `input` 타입과 사용 예제 추가 |
| v1.0 | 2026-07-21 | 라디오 버튼과 체크박스 그룹 설명 추가 |
| v1.0 | 2026-07-21 | `textarea`, `select`, `option`, `optgroup` 추가 |
| v1.0 | 2026-07-21 | `button`, `fieldset`, `legend` 설명 추가 |
| v1.0 | 2026-07-21 | `datalist`, `output` 요소 추가 |
| v1.0 | 2026-07-21 | 입력 속성과 HTML 기본 유효성 검사 추가 |
| v1.0 | 2026-07-21 | 파일 업로드와 `multipart/form-data` 추가 |
| v1.0 | 2026-07-21 | 폼 접근성과 오류 메시지 작성법 추가 |
| v1.0 | 2026-07-21 | 로그인, 검색, 문의 폼 예제 추가 |
| v1.0 | 2026-07-21 | 수강 신청 실무 프로젝트 예제 추가 |
| v1.0 | 2026-07-21 | 자주 하는 실수와 면접 포인트 추가 |
