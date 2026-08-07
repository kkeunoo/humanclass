---
title: HTML 링크와 경로
version: v2.0-final
last_updated: 2026-08-07
status: Completed
---

# HTML 링크와 경로

## 문서 정보

| 항목 | 내용 |
| --- | --- |
| 문서 | `03_HTML_링크와_경로.md` |
| 분류 | `01_HTML` |
| 원본 기준 | `workspace_html/03_상대주소/03_a.html`, `workspace_teacher/workspace_html/03_상대주소/03_a.html` |
| 핵심 범위 | `a`, `href`, `target`, `rel`, URL Scheme, 상대 경로, Root Relative Path, Absolute URL, Fragment Link, Download |
| 학습 범위 | Link, 새 Tab, 전화·Email, Image Link, 파일 경로, 문서 내부 이동, 접근성 |
| 프로젝트 연결 | Navigation, 상세 페이지 이동, 외부 Site 연결, 전화·Email Link, Page 내부 목차, Download |
| 문서 형식 | HTML Developer-Wiki V2 확정 형식 |

> 이 문서는 내 코드와 강사님 코드의 `03_a.html`을 비교해 `a`, `href`, `target`, URL Scheme과 파일 경로의 동작을 정리한다. 원본의 빠진 `href`·`id`·`alt`, 잘못된 따옴표, `http` Link, Root Relative Path를 절대 주소라고 부른 설명은 수정하고, Link 목적·새 Tab·보안·접근성·Debugging까지 실무 기준으로 보완한다.

# 학습 목표

- `a` 요소와 `href` 속성의 역할을 설명한다.
- 현재 탭과 새 탭에서 링크를 여는 방식을 구분한다.
- `target="_blank"`를 사용할 때 보안 속성을 함께 작성한다.
- `tel:`, `mailto:` 같은 URL 스킴을 활용한다.
- 상대 경로, 루트 상대 경로, 절대 URL의 차이를 구분한다.
- `./`, `../`, `/`가 각각 어떤 위치를 가리키는지 설명한다.
- 이미지 전체를 클릭 가능한 링크로 만든다.
- `id`와 해시 링크를 이용해 문서 내부를 이동한다.
- 파일 다운로드 링크와 일반 페이지 이동 링크를 구분한다.
- 잘못된 따옴표, 경로, 빈 링크를 찾아 수정한다.

# 1. 링크를 만드는 `a` 요소

`a`는 Anchor의 약자로, 현재 문서에서 다른 문서나 위치로 이동할 수 있는 링크를 만듭니다.

```html
<a href="https://www.example.com">Example 사이트</a>
```

| 구성 | 역할 |
| --- | --- |
| `a` | 링크 요소 |
| `href` | 이동할 대상 주소 |
| 링크 텍스트 | 사용자가 클릭하는 내용 |

`href`는 Hypertext Reference의 약자입니다. 브라우저는 `href`의 값을 확인하여 링크를 클릭했을 때 어디로 이동할지 결정합니다.

## 1.1 링크 텍스트는 목적을 드러내야 한다

```html
<a href="guide.html">HTML 학습 가이드 보기</a>
```

다음처럼 목적이 불분명한 표현만 반복하는 방식은 피하는 것이 좋습니다.

```html
<a href="guide.html">여기</a>
<a href="notice.html">클릭</a>
```

링크 텍스트는 링크만 읽어도 이동 목적을 예상할 수 있게 작성합니다.

```html
<a href="guide.html">HTML 학습 가이드 보기</a>
<a href="notice.html">수업 공지사항 확인하기</a>
```

# 2. `href`가 없는 `a` 요소

다음 코드는 화면에 텍스트는 표시되지만 실제 이동 기능은 없습니다.

```html
<a>맨 아래로</a>
```

이동 가능한 링크라면 `href`를 작성해야 합니다.

```html
<a href="#bottom">맨 아래로</a>
```

단순 텍스트를 표시하려는 목적이라면 `a` 대신 의미에 맞는 요소를 사용합니다.

```html
<span>맨 아래 안내</span>
```

클릭 동작을 JavaScript로 처리하는 버튼이라면 `a`보다 `button`이 적절할 수 있습니다.

```html
<button type="button">메뉴 열기</button>
```

| 목적 | 권장 요소 |
| --- | --- |
| 다른 문서나 위치로 이동 | `a` |
| 기능 실행 | `button` |
| 일반 텍스트 | `span`, `p` 등 |

# 3. 현재 탭과 새 탭

기본적으로 링크는 현재 탭에서 열립니다.

```html
<a href="https://www.naver.com">네이버</a>
```

새 탭에서 열려면 `target="_blank"`를 사용합니다.

```html
<a href="https://www.google.com" target="_blank">구글</a>
```

## 3.1 주요 `target` 값

| 값 | 동작 |
| --- | --- |
| `_self` | 현재 탐색 영역에서 열기, 기본값 |
| `_blank` | 새 탭 또는 새 창에서 열기 |
| `_parent` | 부모 탐색 영역에서 열기 |
| `_top` | 최상위 탐색 영역에서 열기 |

일반적인 페이지에서는 `_self`와 `_blank`를 가장 자주 사용합니다.

## 3.2 `_blank`와 `rel`

외부 링크를 새 탭에서 열 때는 다음처럼 `rel`을 함께 작성하는 습관이 좋습니다.

```html
<a
  href="https://www.google.com"
  target="_blank"
  rel="noopener noreferrer"
>
  구글
</a>
```

| 값 | 역할 |
| --- | --- |
| `noopener` | 새 페이지가 원래 페이지를 제어하는 것을 방지 |
| `noreferrer` | 이동 대상에 이전 페이지 주소가 전달되는 것을 제한 |

현대 Browser는 `_blank` Link에 `noopener`에 준하는 보호를 적용하는 경우가 많지만, 지원 범위와 의도를 명확히 하기 위해 외부 Link에는 `rel="noopener"`를 명시할 수 있습니다. `noreferrer`는 Referrer 전달도 막으므로 분석 요구사항을 고려해 추가합니다.

## 3.3 모든 링크를 새 탭으로 열지 않는다

새 탭은 사용자의 탐색 흐름을 바꾸므로 목적에 맞게 사용합니다.

| 상황 | 일반적인 선택 |
| --- | --- |
| 같은 사이트의 목록 → 상세 페이지 | 현재 탭 |
| 같은 사이트의 이전·다음 페이지 | 현재 탭 |
| 참고용 외부 문서 | 새 탭을 고려 |
| 사용자가 입력 중인 페이지에서 외부 도움말 열기 | 새 탭을 고려 |

새 탭 여부는 절대 규칙이라기보다 서비스 흐름과 사용자 경험을 기준으로 결정합니다.

# 4. URL 스킴

URL 앞부분의 스킴은 어떤 방식으로 자원을 처리할지 나타냅니다.

```text
https://www.example.com
mailto:study@example.com
tel:01012345678
```

## 4.1 웹 주소 `http:`와 `https:`

```html
<a href="https://www.example.com">웹사이트 방문</a>
```

가능하면 암호화된 통신을 사용하는 `https://` 주소를 사용합니다.

## 4.2 전화 연결 `tel:`

```html
<a href="tel:01012345678">전화 걸기</a>
```

모바일 기기에서는 전화 앱을 실행할 수 있습니다. 데스크톱에서는 연결된 통화 프로그램에 따라 동작이 달라질 수 있습니다.

화면에 표시되는 번호는 읽기 좋게 작성하되 `href`에는 공백 없이 작성할 수 있습니다.

```html
<a href="tel:01012345678">010-1234-5678</a>
```

국제 전화번호는 국가 코드를 포함할 수 있습니다.

```html
<a href="tel:+821012345678">+82 10-1234-5678</a>
```

## 4.3 이메일 작성 `mailto:`

```html
<a href="mailto:study@example.com">메일 보내기</a>
```

제목과 본문을 미리 지정할 수도 있습니다.

```html
<a href="mailto:study@example.com?subject=수업 문의&body=안녕하세요.">
  수업 문의 메일 보내기
</a>
```

실제 URL에서는 한글과 공백이 인코딩될 수 있습니다. 복잡한 제목이나 본문을 직접 조합할 때는 URL 인코딩을 고려해야 합니다.

## 4.4 그 밖의 스킴

```html
<a href="sms:01012345678">문자 보내기</a>
```

환경에 따라 동작 여부가 다를 수 있으므로 실제 대상 기기에서 테스트합니다.

# 5. 이미지 링크

`a` 요소 안에 `img`를 넣으면 이미지를 클릭했을 때 링크로 이동합니다.

```html
<a href="https://www.example.com">
  <img src="banner.jpg" alt="Example 사이트 바로가기">
</a>
```

외부 사이트를 새 탭에서 여는 예시입니다.

```html
<a
  href="https://www.example.com"
  target="_blank"
  rel="noopener noreferrer"
>
  <img src="banner.jpg" alt="Example 사이트 새 탭에서 열기">
</a>
```

이미지 링크에서도 `alt`는 중요합니다. 이미지가 보이지 않거나 화면 낭독기를 사용하는 경우에도 링크의 목적을 이해할 수 있어야 합니다.

## 5.1 잘못된 따옴표 수정

다음 코드에는 `target` 뒤에 큰따옴표가 하나 더 있습니다.

```html
<a href="https://www.example.com" target="_blank"">
```

수정합니다.

```html
<a href="https://www.example.com" target="_blank">
```

HTML 속성은 시작 따옴표와 종료 따옴표의 짝을 정확히 맞춰야 합니다.

# 6. 경로를 이해하기 위한 폴더 구조

경로를 이해하려면 현재 문서의 위치를 먼저 확인해야 합니다.

다음과 같은 폴더 구조를 가정합니다.

```text
workspace_html/
├─ 01_hello.html
├─ asset/
│  ├─ detail.html
│  └─ images/
│     └─ logo.png
└─ pages/
   └─ 03_a.html        ← 현재 문서
```

현재 문서가 `pages/03_a.html`이라면:

- 같은 폴더의 파일은 현재 폴더를 기준으로 찾습니다.
- `asset` 폴더로 이동하려면 먼저 부모 폴더로 올라가야 합니다.
- 부모 폴더는 `..`로 표현합니다.

# 7. 상대 경로

상대 경로는 현재 문서의 위치를 기준으로 대상 파일을 찾는 경로입니다.

## 7.1 같은 폴더의 파일

```text
pages/
├─ 03_a.html
└─ detail.html
```

```html
<a href="detail.html">상세 페이지</a>
```

현재 폴더를 나타내는 `./`를 명시해도 같습니다.

```html
<a href="./detail.html">상세 페이지</a>
```

| 표현 | 의미 |
| --- | --- |
| `detail.html` | 현재 폴더의 `detail.html` |
| `./detail.html` | 현재 폴더의 `detail.html` |

## 7.2 현재 폴더 아래의 하위 폴더

```text
pages/
├─ 03_a.html
└─ detail/
   └─ product.html
```

```html
<a href="detail/product.html">상품 상세</a>
```

또는 다음처럼 작성할 수 있습니다.

```html
<a href="./detail/product.html">상품 상세</a>
```

## 7.3 부모 폴더의 파일

```text
workspace_html/
├─ 01_hello.html
└─ pages/
   └─ 03_a.html
```

현재 문서가 `pages/03_a.html`일 때 부모 폴더의 `01_hello.html`로 이동합니다.

```html
<a href="../01_hello.html">Hello 페이지</a>
```

`..`는 현재 폴더의 부모 폴더를 의미합니다.

## 7.4 부모 폴더의 다른 하위 폴더

```text
workspace_html/
├─ asset/
│  └─ detail.html
└─ pages/
   └─ 03_a.html
```

이동 순서는 다음과 같습니다.

```text
pages/03_a.html
→ ../ 로 workspace_html 이동
→ asset/ 폴더 진입
→ detail.html 선택
```

```html
<a href="../asset/detail.html">상세 페이지 이동</a>
```

## 7.5 두 단계 위로 이동

```html
<a href="../../index.html">메인 페이지</a>
```

| 기호 | 의미 |
| --- | --- |
| `.` | 현재 폴더 |
| `..` | 한 단계 위의 부모 폴더 |
| `../..` | 두 단계 위의 폴더 |

상대 경로에서 가장 중요한 질문은 다음과 같습니다.

```text
현재 HTML 파일은 어느 폴더에 있는가?
이동할 파일은 현재 파일을 기준으로 어디에 있는가?
```

# 8. 절대 URL

절대 URL은 프로토콜과 도메인을 포함한 완전한 웹 주소입니다.

```html
<a href="https://developer.mozilla.org/ko/">MDN Web Docs</a>
```

```text
https://developer.mozilla.org/ko/
└─ 프로토콜 + 도메인 + 경로
```

| 장점 | 단점 |
| --- | --- |
| 현재 파일 위치와 관계없이 동일한 주소를 가리킴 | 도메인이나 경로가 바뀌면 수정 필요 |
| 외부 사이트 연결에 적합 | 내부 파일 개발 환경에서는 주소가 길어질 수 있음 |

외부 사이트는 일반적으로 절대 URL을 사용합니다.

# 9. 루트 상대 경로

`/`로 시작하는 경로는 현재 웹사이트의 루트를 기준으로 찾습니다.

```html
<a href="/asset/detail.html">상세 페이지</a>
```

예를 들어 현재 사이트가 다음 주소에서 실행되고 있다고 가정합니다.

```text
http://localhost:5500/pages/03_a.html
```

`/asset/detail.html`은 다음 주소를 가리킵니다.

```text
http://localhost:5500/asset/detail.html
```

## 9.1 루트 상대 경로와 파일 시스템 루트는 다르다

브라우저에서 `/`는 일반적으로 현재 사이트의 도메인과 포트 뒤의 최상위 경로를 의미합니다.

```text
https://example.com/products/list.html
                  ↑ 사이트 루트는 도메인 뒤의 /
```

```html
<a href="/images/logo.png">로고</a>
```

이는 Windows의 `C:\`나 Linux의 파일 시스템 `/`를 직접 의미하지 않습니다.

## 9.2 로컬 파일로 직접 열 때 주의

HTML 파일을 `file:///` 방식으로 직접 열면 루트 상대 경로의 기준이 개발 서버에서 실행할 때와 다르게 해석되거나 정상적으로 동작하지 않을 수 있습니다.

따라서 프로젝트를 테스트할 때는 Live Server 같은 개발 서버를 이용하는 것이 좋습니다.

# 10. 경로 방식 비교

| 경로 유형 | 예시 | 기준 | 대표 용도 |
| --- | --- | --- | --- |
| 같은 폴더 상대 경로 | `detail.html` | 현재 문서 폴더 | 같은 폴더 파일 |
| 현재 폴더 명시 | `./detail.html` | 현재 문서 폴더 | 기준을 명시하고 싶을 때 |
| 부모 폴더 상대 경로 | `../detail.html` | 현재 문서의 부모 폴더 | 상위 폴더 파일 |
| 루트 상대 경로 | `/asset/detail.html` | 현재 사이트 루트 | 사이트 내부 공통 경로 |
| 절대 URL | `https://example.com/detail.html` | 전체 인터넷 주소 | 외부 사이트 또는 고정 주소 |

## 10.1 `//example.com` 형식

다음과 같이 프로토콜을 생략한 프로토콜 상대 URL도 존재합니다.

```html
<a href="//example.com">Example</a>
```

현재 페이지가 `https`라면 `https://example.com`으로 연결됩니다. 그러나 현대 웹에서는 보안과 명확성을 위해 `https://`를 직접 작성하는 방식이 더 이해하기 쉽습니다.

```html
<a href="https://example.com">Example</a>
```

# 11. 문서 내부 이동

같은 문서 안의 특정 위치로 이동하려면 대상 요소에 `id`를 지정하고, 링크의 `href`에 `#id값`을 작성합니다.

```html
<h1 id="top">페이지 맨 위</h1>
<a href="#bottom">맨 아래로 이동</a>

<!-- 중간 콘텐츠 -->

<strong id="bottom">페이지 맨 아래</strong>
<a href="#top">맨 위로 이동</a>
```

## 11.1 동작 원리

```text
href="#bottom"
        ↓
id="bottom"인 요소를 찾음
        ↓
해당 요소가 보이는 위치로 이동
```

`href`의 해시 값과 대상의 `id` 값은 정확히 일치해야 합니다.

```html
<a href="#lesson-1">1강으로 이동</a>
<h2 id="lesson-1">1강 HTML 기초</h2>
```

## 11.2 `id` 작성 원칙

- 한 문서에서 같은 `id`를 중복하지 않습니다.
- 의미를 알 수 있는 이름을 사용합니다.
- 공백을 넣지 않습니다.
- 링크의 `href`와 철자를 일치시킵니다.

좋은 예시입니다.

```html
<h2 id="html-path">HTML 경로</h2>
<a href="#html-path">HTML 경로로 이동</a>
```

피해야 할 예시입니다.

```html
<h2 id="section 1">HTML 경로</h2>
```

## 11.3 다른 문서의 특정 위치로 이동

파일 경로 뒤에 해시를 붙일 수 있습니다.

```html
<a href="guide.html#path">경로 설명 바로 보기</a>
```

외부 페이지에도 해당 `id`가 존재한다면 같은 방식으로 이동할 수 있습니다.

```html
<a href="https://example.com/guide.html#path">외부 가이드의 경로 섹션</a>
```

# 12. 반복 `br`로 거리를 만들지 않는다

수업 예제에서는 위아래 이동을 확인하기 위해 `br`을 여러 번 작성할 수 있습니다.

```html
<br><br><br><br><br>
```

이는 문서 내부 이동을 눈으로 확인하기 위한 학습용 코드입니다. 실제 페이지의 여백이나 높이를 만들 때는 CSS를 사용합니다.

```html
<section class="content-space">
  긴 콘텐츠 영역
</section>
```

```css
.content-space {
  min-height: 100vh;
}
```

| 목적 | 권장 방식 |
| --- | --- |
| 문장 안의 의미 있는 줄바꿈 | `br` |
| 요소 사이의 여백 | CSS `margin`, `padding` |
| 최소 화면 높이 | CSS `min-height` |

# 13. 파일 다운로드 링크

`download` 속성을 사용하면 브라우저에 파일 다운로드를 요청할 수 있습니다.

```html
<a href="files/html-guide.pdf" download>HTML 가이드 다운로드</a>
```

다운로드 파일명을 제안할 수도 있습니다.

```html
<a href="files/html-guide.pdf" download="HTML_학습가이드.pdf">
  HTML 가이드 다운로드
</a>
```

브라우저 정책, 파일 출처, 서버 설정에 따라 `download`의 동작이 제한될 수 있으므로 실제 환경에서 테스트해야 합니다.

# 14. 링크 접근성

## 14.1 링크 목적을 명확히 작성한다

```html
<a href="curriculum.html">6개월 교육과정 확인하기</a>
```

```html
<a href="curriculum.html">자세히 보기</a>
```

문맥상 의미가 충분하다면 `자세히 보기`도 사용할 수 있지만, 링크만 따로 읽었을 때 목적이 불분명할 수 있습니다. 가능하면 대상이 드러나는 문구를 사용합니다.

## 14.2 새 탭 열림을 알릴 수 있다

```html
<a
  href="https://example.com"
  target="_blank"
  rel="noopener noreferrer"
>
  외부 개발 문서 열기 <span aria-hidden="true">↗</span>
</a>
```

새 탭으로 열리는 링크가 많다면 아이콘이나 보조 문구로 동작을 예측할 수 있게 설계합니다.

## 14.3 URL 자체를 링크 텍스트로 남용하지 않는다

```html
<a href="https://example.com/docs/html/path">
  HTML 경로 가이드
</a>
```

긴 URL을 그대로 노출하는 것보다 의미 있는 링크 텍스트가 읽기 쉽습니다.

# 15. 내 코드와 강사님 코드 비교

두 원본은 외부 Link, 새 Tab, URL Scheme, Image Link, 상대 경로, Root Relative Path, Page 내부 이동을 같은 순서로 실습한다.

## 15.1 기본 문서 구조

두 코드 모두 HTML5 기본 구조를 사용한다.

```html
<!doctype html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta
            name="viewport"
            content="width=device-width, initial-scale=1.0"
        >
        <title>Document</title>
    </head>
</html>
```

본문이 한국어이므로 다음처럼 문서 언어를 맞추는 편이 적절하다.

```html
<html lang="ko">
```

`<title>Document</title>`도 실제 Page 목적을 드러내는 제목으로 바꾼다.

```html
<title>HTML 링크와 경로 실습</title>
```

## 15.2 복원 메모와 설명 수준

내 코드에는 다음 복원 메모가 있다.

```html
<!-- 0723_HTML_상대주소/절대주소_restore -->
```

또한 Emmet, Viewport, 새 Tab·새 Window 조작, 상대 경로 기호에 관한 설명이 강사님 코드보다 상세하다.

복원 이력은 학습 개념과 직접 관련이 없다면 Git Commit이나 별도 작업 기록으로 분리하는 편이 문서 집중도를 높인다.

## 15.3 아래로 이동하는 Link

### 내 코드

```html
<h1 id="top">여기는 맨 위</h1>
<a href="#bottom">맨 아래로</a>
```

```html
<strong id="bottom">
    여기는 맨 아래
</strong>

<a href="#top">맨 위로</a>
```

`href`와 `id`가 연결되어 위·아래 이동이 모두 동작한다.

### 강사님 코드

```html
<h1 id="top">맨 위</h1>
<a>맨 아래로</a>
```

```html
<strong>여기 맨 아래임</strong>
<a href="#top">맨 위로</a>
```

아래로 이동하는 `a`에 `href`가 없고 아래쪽 대상에도 `id`가 없다. 따라서 Text는 보이지만 아래로 이동하는 Link는 아니다.

개선:

```html
<a href="#bottom">
    맨 아래로
</a>

<strong id="bottom">
    여기 맨 아래
</strong>
```

## 15.4 Google 주소의 Protocol

### 내 코드

```html
<a
    href="https://google.com"
    target="_blank"
>
    구글
</a>
```

### 강사님 코드

```html
<a
    href="http://google.com"
    target="_blank"
>
    구글
</a>
```

가능하면 암호화된 연결인 `https://`를 명시한다.

```html
<a href="https://www.google.com/">
    Google
</a>
```

## 15.5 새 Tab Link와 `rel`

두 코드 모두 외부 Link에 `target="_blank"`를 사용하지만 `rel`은 없다.

```html
<a
    href="https://www.google.com/"
    target="_blank"
    rel="noopener noreferrer"
>
    Google
</a>
```

`noopener`는 새 Page와 원래 Page의 Window 연결을 끊는 의도를 나타낸다. `noreferrer`는 Referrer 전달도 제한하므로 분석 요구사항을 고려해 선택한다.

모든 외부 Link를 새 Tab으로 열 필요는 없다. 사용자의 탐색 흐름과 Service 정책을 기준으로 결정한다.

## 15.6 전화와 Email Link

두 코드 모두 `tel:`과 `mailto:`를 올바른 방향으로 실습한다.

```html
<a href="tel:+821012345678">
    010-1234-5678
</a>

<a href="mailto:study@example.com">
    Email 보내기
</a>
```

실제 문서에는 개인 전화번호와 Email을 그대로 공개하기 전에 개인정보 노출 범위를 확인한다.

## 15.7 Image Link의 따옴표 오류

내 코드에는 `target` 뒤에 큰따옴표가 하나 더 있다.

```html
<a
    href="https://comic.naver.com/..."
    target="_blank""
>
```

올바른 형식:

```html
<a
    href="https://comic.naver.com/..."
    target="_blank"
    rel="noopener noreferrer"
>
```

잘못된 따옴표는 뒤 Attribute와 Tag 구조를 Browser가 예상과 다르게 해석하게 만들 수 있다.

## 15.8 Image의 `alt` 누락

두 코드 모두 Link 안의 Image에 `alt`가 없다.

```html
<img
    src="https://image-comic.pstatic.net/...jpg"
>
```

Image가 Link의 유일한 Content라면 `alt`가 Link 목적을 전달해야 한다.

```html
<a href="https://comic.naver.com/...">
    <img
        src="./images/webtoon-thumbnail.jpg"
        alt="웹툰 작품 목록 보기"
    >
</a>
```

`alt`에 “이미지”라고만 쓰기보다 클릭했을 때 어디로 이동하는지 드러낸다.

## 15.9 외부 Image URL 의존성

두 코드 모두 다른 Site의 Image URL을 직접 사용한다.

```html
<img
    src="https://image-comic.pstatic.net/...jpg"
    alt="웹툰 작품 목록 보기"
>
```

학습 실험에는 사용할 수 있지만 실제 Project에서는 다음 문제가 있다.

```text
상대 Site의 파일 변경·삭제
외부 요청 제한
성능과 Cache 제어 어려움
저작권·사용 권한
```

사용 권한을 확인한 Image를 Project 내부나 관리 가능한 Storage에서 제공하는 방식을 우선 검토한다.

## 15.10 같은 Project 내부 Link

두 코드 모두 같은 상위 폴더의 `01_hello.html`을 현재 폴더에 있는 것처럼 작성한다.

```html
<a href="01_hello.html">
    01_hello.html
</a>
```

실제 현재 파일 위치는 다음과 같다.

```text
workspace_html/
├── 01_hello.html
└── 03_상대주소/
    └── 03_a.html
```

따라서 `03_a.html` 기준으로는 부모 폴더로 이동해야 한다.

```html
<a href="../01_hello.html">
    HTML 기초 Page
</a>
```

경로는 Link Text나 원래 의도만 보고 판단하지 않고 **현재 파일의 실제 위치**를 기준으로 계산한다.

## 15.11 `../asset/detail.html`

두 코드 모두 다음 상대 경로를 사용한다.

```html
<a href="../asset/detail.html">
    Detail Page 이동
</a>
```

현재 폴더가 `workspace_html/03_상대주소/`이고 `asset`이 `workspace_html/asset/`에 있다면 올바른 흐름이다.

```text
03_상대주소/03_a.html
→ ../
→ workspace_html/
→ asset/
→ detail.html
```

실제 대상 파일이 존재하는지도 반드시 확인한다.

## 15.12 `/asset/detail.html`의 정확한 이름

두 코드의 주석은 `/`로 시작하는 주소를 “절대 주소” 범주에 포함한다.

```html
<a href="/asset/detail.html">
    절대주소 Detail Page
</a>
```

더 정확한 구분:

```text
https://example.com/asset/detail.html
→ Absolute URL

/asset/detail.html
→ Root Relative URL

../asset/detail.html
→ Relative URL
```

`/asset/detail.html`은 Protocol과 Host를 포함하지 않으며 현재 Site Root를 기준으로 하는 **Root Relative Path**다.

Local File을 직접 열 때와 Development Server에서 실행할 때 기준이 달라질 수 있으므로 Server 환경에서 확인한다.

## 15.13 Protocol Relative URL

원본 주석에는 `//`로 시작하는 주소도 소개된다.

```html
<a href="//example.com">
    Example
</a>
```

현재 Page의 Protocol을 따라가지만 현대 Project에서는 보안과 의도를 명확히 하기 위해 `https://`를 직접 작성하는 편이 일반적이다.

```html
<a href="https://example.com/">
    Example
</a>
```

## 15.14 반복 `<br>`

두 코드 모두 Page 내부 이동 거리를 만들기 위해 `<br>`을 50개 사용한다.

```html
<br><br><br><br><br>
```

Fragment Link 이동을 눈으로 확인하는 학습 실험으로는 사용할 수 있지만 실제 Layout 높이와 여백은 CSS로 만든다.

```html
<section class="long-content">
    중간 Content
</section>
```

```css
.long-content {
    min-height: 100vh;
}
```

## 15.15 원본 비교 요약

| 항목 | 내 코드 | 강사님 코드 | 개선 기준 |
| --- | --- | --- | --- |
| 아래 이동 | `href="#bottom"`과 `id` 있음 | `href`와 대상 `id` 없음 | Fragment와 대상 ID 연결 |
| Google | `https` | `http` | 가능한 경우 `https` |
| 새 Tab 보안 | `rel` 없음 | `rel` 없음 | 목적에 맞게 `noopener` 검토 |
| Image Link | 따옴표 오류 | 현재 Tab | Attribute 문법 검수 |
| Image `alt` | 없음 | 없음 | Link 목적을 나타내는 `alt` |
| 내부 파일 경로 | `01_hello.html` | `01_hello.html` | 실제 위치상 `../01_hello.html` 검토 |
| `/asset/...` 설명 | 절대 주소 | 절대 주소 | Root Relative Path로 구분 |
| 반복 `<br>` | 50개 | 50개 | Layout은 CSS |
| `lang` | `en` | `en` | 한국어 문서는 `ko` |
| 외부 Image | Hotlink | Hotlink | 권한·안정성·성능 확인 |

# 16. 개선된 통합 예제

```html
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>HTML 링크와 경로</title>
</head>
<body>
  <header id="top">
    <h1>HTML 링크와 경로</h1>

    <nav aria-label="페이지 내 이동">
      <a href="#external">외부 링크</a>
      <a href="#project">프로젝트 링크</a>
      <a href="#contact">연락처</a>
      <a href="#bottom">맨 아래</a>
    </nav>
  </header>

  <main>
    <section id="external">
      <h2>외부 링크</h2>
      <p>
        <a
          href="https://developer.mozilla.org/ko/"
          target="_blank"
          rel="noopener noreferrer"
        >
          MDN Web Docs 새 탭에서 열기
        </a>
      </p>
    </section>

    <section id="project">
      <h2>프로젝트 내부 링크</h2>
      <ul>
        <li><a href="../01_hello.html">Hello 페이지</a></li>
        <li><a href="../asset/detail.html">상세 페이지</a></li>
        <li><a href="/asset/detail.html">사이트 루트 기준 상세 페이지</a></li>
      </ul>
    </section>

    <section id="contact">
      <h2>연락하기</h2>
      <p><a href="tel:01012345678">010-1234-5678</a></p>
      <p><a href="mailto:study@example.com">study@example.com</a></p>
    </section>

    <section>
      <h2>이미지 링크</h2>
      <a
        href="https://www.example.com"
        target="_blank"
        rel="noopener noreferrer"
      >
        <img src="../asset/images/logo.png" alt="Example 사이트 열기">
      </a>
    </section>
  </main>

  <footer id="bottom">
    <a href="#top">맨 위로 이동</a>
  </footer>
</body>
</html>
```

# 17. 자주 하는 실수

## 17.1 현재 파일 위치를 기준으로 생각하지 않음

```html
<a href="asset/detail.html">상세 페이지</a>
```

현재 파일이 `pages` 폴더에 있고 `asset`이 부모 폴더 아래에 있다면 이 경로는 잘못되었습니다.

```html
<a href="../asset/detail.html">상세 페이지</a>
```

## 17.2 Windows 경로를 HTML에 그대로 사용

```html
<a href="C:\workspace\asset\detail.html">상세 페이지</a>
```

웹 프로젝트에서는 프로젝트 구조를 기준으로 URL 경로를 작성합니다.

```html
<a href="../asset/detail.html">상세 페이지</a>
```

## 17.3 역슬래시 사용

```html
<a href="..\asset\detail.html">상세 페이지</a>
```

URL 경로는 `/`를 사용합니다.

```html
<a href="../asset/detail.html">상세 페이지</a>
```

## 17.4 `href`와 `id` 불일치

```html
<a href="#bottom">맨 아래로</a>
<strong id="footer">맨 아래</strong>
```

수정합니다.

```html
<a href="#bottom">맨 아래로</a>
<strong id="bottom">맨 아래</strong>
```

## 17.5 새 탭 링크에 잘못된 따옴표

```html
<a href="https://example.com" target="_blank"">링크</a>
```

```html
<a href="https://example.com" target="_blank">링크</a>
```

## 17.6 이미지 링크에 `alt` 없음

```html
<a href="detail.html">
  <img src="product.jpg">
</a>
```

```html
<a href="detail.html">
  <img src="product.jpg" alt="상품 상세 정보 보기">
</a>
```

## 17.7 빈 `href` 사용

```html
<a href="">링크</a>
```

빈 `href`는 현재 문서를 다시 요청하거나 페이지 위치를 변경할 수 있습니다. 아직 목적지가 없다면 링크를 만들지 않거나 개발 단계임을 명확히 처리합니다.

```html
<span>준비 중</span>
```

## 17.8 `href="#"`를 임시 버튼처럼 사용

```html
<a href="#">메뉴 열기</a>
```

기능 실행이 목적이라면 버튼을 사용합니다.

```html
<button type="button">메뉴 열기</button>
```

# 18. 실무 팁

## 18.1 링크 확인 순서

링크가 동작하지 않을 때 다음 순서로 점검합니다.

```text
1. href가 작성되었는가?
2. 따옴표가 올바르게 닫혔는가?
3. 현재 HTML 파일의 위치는 어디인가?
4. 대상 파일의 실제 위치는 어디인가?
5. ../의 개수가 맞는가?
6. 파일명과 확장자의 대소문자가 정확한가?
7. 개발 서버의 루트가 어디인가?
8. 대상 요소의 id가 존재하는가?
```

## 18.2 파일명은 단순하게 관리한다

```text
좋은 예시
html-path.html
product-detail.html
01_hello.html

주의가 필요한 예시
최종 진짜 최종 수정본.html
상품 상세 페이지(수정).html
```

한글 파일명도 사용할 수 있지만 배포 환경과 협업 도구에서 인코딩 문제가 발생할 수 있으므로 영문 소문자, 숫자, 하이픈을 중심으로 관리하는 방식이 일반적입니다.

## 18.3 외부 링크는 주기적으로 점검한다

외부 URL은 사이트 개편이나 삭제로 변경될 수 있습니다. 프로젝트 배포 전에는 중요한 외부 링크가 실제로 열리는지 확인합니다.

## 18.4 내비게이션에는 링크를 사용한다

```html
<nav aria-label="주요 메뉴">
  <a href="/">홈</a>
  <a href="/courses/">교육과정</a>
  <a href="/projects/">프로젝트</a>
</nav>
```

페이지 이동을 위한 메뉴는 `a`가 적절합니다. JavaScript 동작만 실행하는 메뉴 버튼과 구분해야 합니다.


# 19. 종합실습

## Level 1

### 문제 1

네이버를 현재 탭에서 여는 링크를 작성하세요.

```html
<!-- 작성 영역 -->


```

### 문제 2

구글을 새 탭에서 열고 보안 속성까지 작성하세요.

```html
<!-- 작성 영역 -->


```

### 문제 3

`010-1234-5678`로 전화할 수 있는 링크를 작성하세요.

```html
<!-- 작성 영역 -->


```

### 문제 4

`study@example.com`으로 메일을 작성할 수 있는 링크를 만드세요.

```html
<!-- 작성 영역 -->


```

## Level 2

### 문제 5

다음 폴더 구조에서 `pages/03_a.html`이 `asset/detail.html`로 이동하도록 링크를 작성하세요.

```text
project/
├─ asset/
│  └─ detail.html
└─ pages/
   └─ 03_a.html
```

```html
<!-- 작성 영역 -->


```

### 문제 6

다음 코드의 오류를 모두 수정하세요.

```html
<a href="https://example.com" target="_blank"">
  <img src="banner.jpg">
</a>
```

```html
<!-- 수정 영역 -->



```

### 문제 7

`맨 아래로` 링크를 클릭하면 `footer`로 이동하도록 빈칸을 채우세요.

```html
<a href="________">맨 아래로</a>

<footer id="________">
  페이지 맨 아래
</footer>
```

## Level 3

### 문제 8

다음 잘못된 코드를 의미에 맞게 수정하세요.

```html
<a href="#">메뉴 열기</a>
<a>수업 안내</a>
```

조건:

- `메뉴 열기`는 JavaScript로 기능을 실행할 예정입니다.
- `수업 안내`는 `notice.html`로 이동합니다.

```html
<!-- 수정 영역 -->


```

### 문제 9

현재 문서가 `courses/html/03_link.html`에 있고, 이동할 파일이 프로젝트 루트의 `index.html`에 있습니다. 상대 경로 링크를 작성하세요.

```html
<!-- 작성 영역 -->


```

## Challenge

### 문제 10

다음 요소를 포함한 간단한 링크 모음 페이지를 작성하세요.

- 페이지 제목
- 현재 페이지 내부의 `연락처` 섹션으로 이동하는 링크
- 외부 개발 문서 새 탭 링크
- 전화 링크
- 이메일 링크
- 이미지 링크
- 맨 위로 이동하는 링크

```html
<!-- 작성 영역 -->













```

# 20. 정답과 해설

## 문제 1 정답

```html
<a href="https://www.naver.com">네이버</a>
```

`target`을 작성하지 않으면 기본적으로 현재 탭에서 열립니다.

## 문제 2 정답

```html
<a
  href="https://www.google.com"
  target="_blank"
  rel="noopener noreferrer"
>
  구글
</a>
```

`_blank`는 새 탭이나 새 창을 열며, 외부 링크에는 `rel`을 함께 작성할 수 있습니다.

## 문제 3 정답

```html
<a href="tel:01012345678">010-1234-5678</a>
```

화면에는 읽기 좋은 형식으로 표시하고 `href`에는 전화 스킴을 사용합니다.

## 문제 4 정답

```html
<a href="mailto:study@example.com">study@example.com</a>
```

`mailto:`는 기본 메일 작성 프로그램을 열도록 요청합니다.

## 문제 5 정답

```html
<a href="../asset/detail.html">상세 페이지</a>
```

현재 위치인 `pages`에서 `..`로 부모 폴더에 올라간 뒤 `asset/detail.html`로 이동합니다.

## 문제 6 정답

```html
<a
  href="https://example.com"
  target="_blank"
  rel="noopener noreferrer"
>
  <img src="banner.jpg" alt="Example 사이트 열기">
</a>
```

추가 큰따옴표를 제거하고, 외부 새 탭 링크에 `rel`을 추가했으며, 이미지에 링크 목적을 전달하는 `alt`를 작성했습니다.

## 문제 7 정답

```html
<a href="#footer">맨 아래로</a>

<footer id="footer">
  페이지 맨 아래
</footer>
```

`href`의 해시 값과 `id` 값이 동일해야 합니다.

## 문제 8 정답

```html
<button type="button">메뉴 열기</button>
<a href="notice.html">수업 안내</a>
```

기능 실행은 `button`, 페이지 이동은 `a`가 적절합니다.

## 문제 9 정답

```html
<a href="../../index.html">메인 페이지</a>
```

`html` 폴더에서 한 단계, `courses` 폴더에서 한 단계를 더 올라가면 프로젝트 루트에 도착합니다.

## 문제 10 예시 정답

```html
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>링크 모음</title>
</head>
<body>
  <header id="top">
    <h1>개발 학습 링크 모음</h1>
    <a href="#contact">연락처로 이동</a>
  </header>

  <main>
    <section>
      <h2>외부 문서</h2>
      <a
        href="https://developer.mozilla.org/ko/"
        target="_blank"
        rel="noopener noreferrer"
      >
        MDN Web Docs 열기
      </a>
    </section>

    <section>
      <h2>이미지 링크</h2>
      <a href="detail.html">
        <img src="banner.jpg" alt="상세 페이지 보기">
      </a>
    </section>

    <section id="contact">
      <h2>연락처</h2>
      <p><a href="tel:01012345678">010-1234-5678</a></p>
      <p><a href="mailto:study@example.com">study@example.com</a></p>
    </section>
  </main>

  <footer>
    <a href="#top">맨 위로 이동</a>
  </footer>
</body>
</html>
```

문구와 파일명은 달라질 수 있습니다. 중요한 점은 이동 목적에 맞는 `href`, 고유한 `id`, 이미지의 `alt`, 새 탭 링크의 속성을 올바르게 작성하는 것입니다.

# 21. 최종 체크리스트

- [ ] 링크에 실제 이동 목적이 있다면 `href`를 작성했는가?
- [ ] 링크 텍스트만 읽어도 이동 목적을 이해할 수 있는가?
- [ ] 기능 실행은 `button`, 페이지 이동은 `a`로 구분했는가?
- [ ] 외부 새 탭 링크에 필요한 `rel`을 검토했는가?
- [ ] 이미지 링크에 적절한 `alt`를 작성했는가?
- [ ] 속성 따옴표의 짝이 정확한가?
- [ ] 현재 문서 위치를 기준으로 상대 경로를 계산했는가?
- [ ] URL 경로에 역슬래시가 아닌 `/`를 사용했는가?
- [ ] 루트 상대 경로를 개발 서버 환경에서 확인했는가?
- [ ] 문서 내부 링크의 해시 값과 `id`가 일치하는가?
- [ ] 같은 `id`를 중복해서 사용하지 않았는가?
- [ ] 반복 `br`을 실제 레이아웃용으로 사용하지 않았는가?

# 22. 핵심 요약

```text
a                     → 다른 문서나 위치로 이동하는 링크
href                  → 이동 대상 주소
target="_blank"       → 새 탭 또는 새 창
rel="noopener..."     → 새 탭 외부 링크 보안 보완
tel:                  → 전화 연결
mailto:               → 이메일 작성
./                    → 현재 폴더
../                   → 부모 폴더
/                     → 현재 사이트 루트
https://...           → 절대 URL
#section              → 같은 문서의 id 위치로 이동
download              → 파일 다운로드 요청
```

> 경로 문제를 해결하는 가장 확실한 방법은 주소를 외우는 것이 아니라, 현재 파일과 대상 파일의 위치를 폴더 구조로 그린 뒤 한 단계씩 이동하는 것입니다.
