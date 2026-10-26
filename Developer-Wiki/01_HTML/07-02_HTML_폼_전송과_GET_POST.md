# 07-02. 폼 전송 — 어떤 이름과 값이 어디로 가는가?

[HTML 읽기 안내](README.md) · [입력요소로 돌아가기](07_HTML_폼과_입력요소.md)

폼은 입력을 보여 주는 데서 끝나지 않는다. 전송할 주소·방식·항목을 정한다. 양쪽 `workspace_html/07_form.html`의 GET·POST 예제를 기준으로 **입력 → 이름과 값 → 요청 → 서버 응답** 순서로 읽는다.

## 목차

1. [GET 원본 비교](#get)
2. [제출될 항목 고르기](#entries)
3. [`action`과 검색 폼](#action)
4. [POST와 서버 지원](#post)
5. [복습](#practice)

<a id="get"></a>

## 1. GET: 이름 있는 입력을 주소의 쿼리로 보낸다

### 강사님 코드 — 원본 발췌

강사님 `workspace_html/07_form.html` 93~98행

```html
    <form method="get">
        <input type="text" name="song"><br>
        <input type="text"><br>
        <input type="text" name="singer"><br>
        <input type="submit" value="get 연습">
    </form>
```

세 입력 중 첫 번째와 세 번째에만 `name`이 있다. 가운데 입력은 화면에는 있지만 이 폼 전송에서 이름 있는 항목으로 포함되지 않는다.

### 내 코드 — 원본 발췌

내 코드 `workspace_html/07_form.html` 129~134행

```html
        <form method="get">
            <input type="text" name="song"><br>
            <input type="text"><br>
            <input type="text" name="singer"><br>
            <input type="submit" value="get 연습"><br>
        </form>
```

마지막 `br` 등 표시 차이를 제외하면 전송 동작은 같다. 원본에 `action`이 없으므로 현재 문서 주소를 대상으로 제출한다.

예를 들어 `song`에 `hello`, 가운데 입력에 `ignored`, `singer`에 `student`를 적으면 쿼리는 다음과 같다.

```text
song=hello&singer=student
```

이름과 값은 `=`로 연결하고 여러 항목은 `&`로 구분한다. 보통 요청 주소에서 `?` 뒤에 붙는다. 한글·공백·특수문자는 전송 형식에 맞게 인코딩되므로 주소창의 표기가 입력 글자와 완전히 같지 않을 수 있다.

<a id="entries"></a>

## 2. 화면에 보이는 모든 값이 제출되지는 않는다

| 입력 상태 | 이 수업의 일반 폼 제출에서 확인할 점 |
| --- | --- |
| `name` 없음 | 제출할 이름이 없어 제외 |
| `disabled` | 제외 |
| 이름 있는 텍스트 입력이 `readonly` | 읽기 전용이어도 제출 가능 |
| 체크박스·라디오가 미선택 | 제외 |
| 선택된 체크박스·라디오에 `value` 없음 | 기본값 `on` |
| 선택된 `option`에 `value` 있음 | 표시 글자 대신 해당 값 사용 |
| 일반 `type="button"` | 이름·값이 있어도 제출 버튼 항목으로 자동 포함되지 않음 |
| 제출 버튼 | 실제 제출에 사용한 버튼에 이름이 있으면 그 값도 포함될 수 있음 |

같은 이름의 체크박스를 두 개 선택하면 `coffee=1&coffee=2`처럼 이름이 반복될 수 있다. 이를 “마지막 값만 남는다”라고 HTML 단계에서 단정하지 않는다. 서버에서 여러 값을 받는 방법은 FastAPI에서 연결한다.

### 전송 확인용 예제 — 설명용 재구성

이 예제는 외부 사이트 대신 현재 문서에 GET으로 보낸다. 테스트용 값만 사용한다.

```html
<form method="get">
    <label>노래 <input type="text" name="song" value="hello"></label>
    <label>이름 없는 입력 <input type="text" value="ignored"></label>
    <input type="text" name="fixed" value="A" readonly>
    <input type="text" name="off" value="B" disabled>
    <label><input type="checkbox" name="coffee" value="1" checked>샷추가</label>
    <label><input type="checkbox" name="coffee" value="2" checked>펄추가</label>
    <button type="submit">전송 확인</button>
</form>
```

초기 상태로 제출하면 쿼리는 다음과 같다.

```text
song=hello&fixed=A&coffee=1&coffee=2
```

`ignored`와 `off=B`는 포함되지 않는다. 실제 검증에서는 요청을 화면에 돌려주는 로컬 수신 주소로 `action`만 바꾸어 제출했고, 이 쿼리와 일치했다. 같은 구성의 POST도 같은 항목을 본문으로 전송했다. 이 결과는 값을 저장했다는 증거가 아니라 브라우저가 **어떤 항목을 요청에 넣었는지** 보여 주는 것이다.

<a id="action"></a>

## 3. `action`: 요청을 받을 주소

양쪽 원본은 네이버 검색 주소에 `name="query"`, 구글 검색 주소에 `name="q"`를 사용한다. 같은 검색어 입력이라도 받는 쪽이 기대하는 이름과 맞춰야 한다. 내가 마음대로 `name="search"`로 바꿔도 상대 서비스가 알아서 해석한다고 가정하지 않는다.

| 폼 속성 | 역할 | 원본 예 |
| --- | --- | --- |
| `action` | 요청을 보낼 대상 | 검색 주소 또는 생략한 현재 주소 |
| `method` | 전송 방식 | `get`, `post` |
| `target` | 응답을 열 문맥 | 구글 검색의 `_blank` |

이 검토에서는 원본의 외부 검색 폼을 실제로 제출하지 않고 로컬 테스트 폼으로 전송 규칙을 확인한다. 검색 서비스의 현재 처리 동작은 수업 코드의 고정 출력으로 제시하지 않는다.

<a id="post"></a>

## 4. POST: 본문에 담아 보내며 서버의 처리가 필요하다

### 강사님 코드 — 원본 발췌

강사님 `workspace_html/07_form.html` 108~111행

```html
    <form method="post">
        <input type="text" name="query"><br>
        <input type="submit" value="post 연습">
    </form>
```

### 내 코드 — 원본 발췌

내 코드 `workspace_html/07_form.html` 147~150행

```html
        <form method="post">
            <input type="text" name="query"><br>
            <input type="submit" value="post 연습"><br>
        </form>
```

두 코드는 `name="query"`의 값을 현재 주소로 POST 전송한다. 역시 줄바꿈 표시 외에 전송 목적은 같다.

| 비교 | GET | POST |
| --- | --- | --- |
| 이 수업의 폼 값 위치 | URL 쿼리 | 요청 본문 |
| 주소창에서 값 확인 | 보통 쿼리로 확인 | 본문 값은 주소창에 붙지 않음 |
| 받는 서버의 지원 | 해당 GET 요청 처리 필요 | 해당 POST 요청 처리 필요 |

내 주석의 “POST는 주소 변경이 없다”는 표현은 보완해야 한다. **폼 값을 쿼리로 붙이지 않는다는 뜻**으로 읽는다. `action`이 다른 주소이거나 서버가 리다이렉트하면 페이지 주소는 바뀔 수 있다. POST 자체가 암호화를 제공하는 것도 아니다.

정적 파일 서버가 POST를 처리하지 않으면 405 또는 501 같은 응답을 받을 수 있다. 정확한 상태 코드는 서버에 따라 다르다. 버튼 클릭 후 오류 페이지가 보인다는 사실만으로 HTML에서 전송 자체가 없었다고 판단하지 않는다.

브라우저 개발자도구의 네트워크 요청에서 방식·대상·보낸 값을 확인하고, 서버 응답은 따로 확인한다. 요청 내용을 읽는 상세 도구 사용법과 서버 구현은 별도 학습으로 연결한다. 이 장을 읽기 위해 `fetch`·`FormData`·FastAPI 코드를 먼저 배울 필요는 없다.

<a id="practice"></a>

## 5. 복습

1. 입력에 `id="song"`만 있고 `name`이 없다. `song=...`으로 자동 제출될까?
2. 선택된 두 체크박스가 같은 `name`을 갖는다. 한 개만 제출될까?
3. POST 응답이 오류여도 요청 본문이 서버로 전달되었을 수 있을까?
4. `action`을 생략한 GET 폼은 기본적으로 어디로 보낼까?

<details>
<summary>정답과 이유</summary>

1. 아니다. 이 폼의 제출 이름은 `name`이다.
2. 둘 다 제출 조건을 갖추면 같은 이름의 항목 두 개가 될 수 있다.
3. 그렇다. 전송과 서버의 성공적인 처리는 구분한다.
4. 현재 문서 주소를 대상으로 한다.

</details>

**다시 볼 핵심:** `action` → `method` → `name` → 선택·활성 상태 → 값 → 응답 순서로 확인한다.

정확성 참고: [HTML 표준 — 폼 제출과 데이터 구성](https://html.spec.whatwg.org/dev/form-control-infrastructure.html).

[다음: 기본 종합복습](10_HTML_종합실습.md) · [HTML 목차](README.md)
