# 03. 링크와 경로 — 지금 위치에서 목적지 찾기

[HTML 읽기 안내](README.md) · [이전: 기본 태그](02_HTML_기본태그.md) · [다음: 목록](04_HTML_목록태그.md)

링크가 열리지 않을 때는 파일명만 확인하지 말고 **현재 문서의 위치 → 기준 위치 → 목적지** 순서로 계산한다. 수업 근거는 양쪽 `workspace_html/03_상대주소/03_a.html`과 `workspace_html/asset/detail.html`이다.

## 목차

1. [링크와 새 탭](03_HTML_링크와_경로.md#anchor)
2. [상대 경로 비교](03_HTML_링크와_경로.md#relative)
3. [루트 기준 경로](03_HTML_링크와_경로.md#root)
4. [같은 문서 안의 이동](03_HTML_링크와_경로.md#fragment)
5. [전화·메일·이미지 링크](03_HTML_링크와_경로.md#scheme)
6. [복습](03_HTML_링크와_경로.md#practice)

<a id="anchor"></a>

## 1. `a`·`href`·`target`

설명용 재구성:

```html
<a href="https://example.com">사이트 열기</a>
<a href="https://example.com" target="_blank">새 탭에서 열기</a>
```

`a`는 링크를 만들고, `href`는 목적지를 지정한다. 요소 안의 글자는 클릭할 때 보이는 안내다. `target="_blank"`는 새 탐색 문맥을 요청하며, 보통 새 탭으로 열린다. 브라우저 설정에 따라 새 창일 수도 있다.

양쪽 원본에 외부 주소와 `_blank`가 있다. 구글 주소는 강사님이 `http://`, 나는 `https://`로 적었다. 주소의 스킴이 다르다는 점과 실제로 어느 페이지로 이동하는지는 구분한다. 외부 사이트의 리다이렉트 동작을 이 문서의 고정 결과로 삼지 않는다.

<a id="relative"></a>

## 2. `../`를 실제 폴더 구조로 계산하기

```text
workspace_html/
├── 01_hello.html
├── 03_상대주소/
│   └── 03_a.html       ← 현재 문서
└── asset/
    └── detail.html    ← 목적지
```

### 강사님 코드 — 원본 발췌

강사님 `workspace_html/03_상대주소/03_a.html` 37~37행

```html
    <a href="../asset/detail.html" target="_blank">디테일페이지 이동</a>
```

현재 문서의 폴더에서 `..`로 한 단계 위 `workspace_html`로 올라간 뒤 `asset/detail.html`을 찾는다.

### 내 코드 — 원본 발췌

내 코드 `workspace_html/03_상대주소/03_a.html` 46~46행

```html
        <a href="../asset/detail.html" target="_blank">디테일페이지 이동</a><br>
```

줄바꿈용 `br` 차이를 제외하면 목적지와 새 탐색 문맥 설정은 같다. 두 원본 모두 이 상대 경로는 제시된 폴더 구조와 맞는다.

| `href` | 현재 `03_a.html`에서 찾는 위치 |
| --- | --- |
| `detail.html` | `03_상대주소/detail.html` |
| `./detail.html` | 위와 같은 위치 |
| `../asset/detail.html` | `workspace_html/asset/detail.html` |
| `../01_hello.html` | `workspace_html/01_hello.html` |

`.`은 현재 폴더, `..`은 부모 폴더다. 여기서는 `base` 요소가 없는 수업 문서를 기준으로 설명한다.

### 양쪽 원본에서 함께 고칠 부분

양쪽 모두 `href="01_hello.html"` 링크를 사용한다. 현재 수업 파일의 위치에서는 `03_상대주소/01_hello.html`을 찾으므로, 실제 상위 폴더의 파일과 맞지 않는다.

설명용 수정:

```html
<a href="../01_hello.html" target="_blank">첫 실습 열기</a>
```

강사님 코드라는 이유만으로 올바른 경로라고 가정하지 않는다. 실제 폴더 구조와 비교하는 것이 기준이다.

<a id="root"></a>

## 3. `/`로 시작하면 서버의 루트를 기준으로 한다

### 강사님 코드 — 원본 발췌

강사님 `workspace_html/03_상대주소/03_a.html` 48~48행

```html
    <a href="/asset/detail.html">절대주소 디테일페이지</a>
```

### 내 코드 — 원본 발췌

내 코드 `workspace_html/03_상대주소/03_a.html` 55~55행

```html
        <a href="/asset/detail.html" target="_blank">절대주소 디테일페이지</a><br>
```

내 코드는 `_blank`가 있어 보통 새 탭으로 연다. 같은 서버의 같은 페이지에서 클릭한다면 **계산되는 목적지 경로**는 같고 **여는 문맥**이 다르다.

예를 들어 현재 주소가 `http://localhost:8000/03_상대주소/03_a.html`이고 서버가 `workspace_html`을 루트로 제공한다면:

| 주소 종류 | 예 | 목적지 |
| --- | --- | --- |
| 전체 URL | `https://example.com/help` | 지정한 스킴·서버·경로 |
| 문서 상대 경로 | `../asset/detail.html` | `http://localhost:8000/asset/detail.html` |
| 루트 기준 경로 | `/asset/detail.html` | 위 서버의 `/asset/detail.html` |

원본은 `/...`도 “절대 주소”로 묶어 설명하지만, 이 문서에서는 전체 URL과 혼동하지 않도록 **루트 기준 경로**라고 부른다. `/`는 항상 내 프로젝트 폴더를 뜻하는 것이 아니다. 서버가 어떤 폴더를 루트로 제공하는지에 따라 결과가 달라진다.

파일을 더블클릭한 `file:` 환경과 HTTP 서버 환경도 구분한다. 루트 기준 경로·폼 전송은 서버 주소에서 확인하는 편이 수업의 URL 설명과 맞는다. 이번 장에서는 서버 구현을 새 진도로 추가하지 않는다.

<a id="fragment"></a>

## 4. 같은 문서에서 위아래로 이동하기

### 강사님 코드 — 원본 발췌

강사님 `workspace_html/03_상대주소/03_a.html` 9~10행

```html
    <h1 id="top">맨 위</h1>
    <a>맨 아래로</a>
```

강사님 원본의 `맨 아래로`에는 `href`가 없다. 원본 아래쪽의 `strong`에도 `id="bottom"`이 없으므로 아래로 이동하는 연결이 완성되지 않았다.

### 내 코드 — 원본 발췌

내 코드 `workspace_html/03_상대주소/03_a.html` 14~15행

```html
        <h1 id="top">여기는 맨 위</h1>
        <a href="#bottom">맨 아래로</a><br>
```

내 원본 아래쪽에는 `<strong id="bottom">여기는 맨 아래</strong>`도 있다. **클릭할 링크와 도착 지점을 모두 지정한 내 코드가 이 실습 목적에 더 맞는다.**

| 구성 | 역할 |
| --- | --- |
| `id="bottom"` | 문서 안에서 찾을 요소의 식별자 |
| `href="#bottom"` | 그 식별자를 가진 요소로 이동 |
| `id="top"`과 `href="#top"` | 위로 돌아가는 연결 |

`#`는 `href`에 붙이고, `id` 값 자체에는 붙이지 않는다. 한 문서에서 같은 `id`를 중복 작성하지 않는다. 목적지가 처음부터 화면 안에 있으면 이동해도 큰 스크롤 변화가 없을 수 있다.

<a id="scheme"></a>

## 5. 전화·메일·이미지 링크도 실제 수업 범위다

`tel:`과 `mailto:`는 강사님 코드와 내 코드에 모두 있다. 따라서 별도의 추가 지식으로 밀어내지 않는다. 다음은 연락처를 예시 값으로 바꾼 **설명용 재구성**이며 원본 그대로의 발췌가 아니다.

```html
<a href="tel:01000000000">전화걸기</a>
<a href="mailto:learner@example.com">메일보내기</a>
```

연결된 전화·메일 앱이 있는 환경에서 해당 동작을 요청한다. HTML만으로 전화가 반드시 연결되거나 메일이 자동 발송되는 것은 아니다. 이 검토에서는 실제 전화·메일 동작을 실행하지 않는다.

이미지를 클릭하게 하려면 양쪽 수업 코드처럼 `a` 안에 `img`를 넣는다. 내 원본에는 `_blank` 뒤에 따옴표가 하나 더 있다. 강사님 원본처럼 속성의 따옴표를 짝에 맞게 쓰는 편이 올바르다.

설명용 수정 — 이미지 파일은 같은 폴더에 있어야 한다.

```html
<a href="https://example.com" target="_blank">
    <img src="thumbnail.png" alt="사이트로 이동">
</a>
```

`alt`의 역할과 파일을 찾는 방법은 이미지 장에서 설명한다. 원본의 외부 이미지는 주소 변경·네트워크 상태에 따라 표시되지 않을 수 있다.

<a id="practice"></a>

## 6. 복습

1. 현재 파일이 `pages/list.html`, 목적지가 `images/photo.png`이고 두 폴더가 같은 부모 아래 있다. 상대 경로는?
2. `/asset/detail.html`에서 `/`는 무조건 지금 코드의 프로젝트 폴더인가?
3. `<a href="#end">끝</a>`가 이동할 요소의 속성은 어떻게 적을까?

<details>
<summary>정답과 이유</summary>

1. `../images/photo.png`. `pages`의 부모로 올라간 후 `images`로 들어간다.
2. 아니다. HTTP 문서에서는 해당 서버 주소의 루트 경로를 기준으로 한다.
3. 예를 들어 `<h2 id="end">마무리</h2>`. 식별자 값에는 `#`를 붙이지 않는다.

</details>

## 💡 추가로 알면 좋은 것

> [!TIP]
> 수업 원본에 없는 `base` 설정과 링크 보안 속성의 상세 설계는 기본 경로 문제의 필수 조건이 아니다. `//example.com/help`처럼 `//`로 시작하는 **스킴 상대 URL**은 현재 문서의 스킴을 따라 다른 서버를 가리킨다. 위에서 배운 `../`와 `/`의 차이를 이해한 다음 필요할 때 읽는다.

정확성 참고: [HTML 표준 — 링크](https://html.spec.whatwg.org/dev/links.html).

<!-- legacy-migration -->

<a id="index-section-57"></a>
<a id="index-section-59"></a>
<a id="html-3"></a>
<a id="html-16"></a>
<a id="html-6"></a>
<a id="index-section-56"></a>
<a id="index-section-11"></a>
<a id="index-section-15"></a>
<a id="index-section-12"></a>
<a id="html-14"></a>
<a id="html-4"></a>
<a id="index-section-36"></a>

### 이전 색인 링크 안내

이전 절 주소를 보존한 안내 위치다. 개편 전 절 번호와 현재 절 번호는 서로 다르다. [HTML 새 목차](README.md)에서 현재 수업 본문과 **추가로 알면 좋은 것**을 구분해 찾을 수 있다.

---

[장별 연습문제 풀기](실습/연습문제/03_HTML_링크와_경로_연습문제.md) · [다음: 목록](04_HTML_목록태그.md)
