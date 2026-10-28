# 10. 종합복습 — 배운 태그로 학습 신청 문서 만들기

[HTML 목차](README.md) · [폼 전송 복습](07-02_HTML_폼_전송과_GET_POST.md)

**종합실습**은 앞에서 따로 배운 문서 구조·목록·표·폼을 하나의 문서에 연결해 보는 연습이다. 이번에는 수업에서 실제 사용한 태그만으로 학습 신청 화면을 만들고, 제출 전 주소에 붙을 값을 예상한다. 화면이 보이는 것과 신청이 서버에 저장되는 것은 다른 일이다.

아래 코드는 원본에 그대로 존재하는 시험 코드가 아니라 **수업 범위 안에서 만든 설명용 재구성**이다. CSS·JavaScript·FastAPI를 먼저 구현하지 않아도 문서와 GET 제출을 확인할 수 있다.

## 1. 만들 문서

| 필요한 기능 | 사용할 수업 내용 | 출처 |
| --- | --- | --- |
| 문서 제목·본문 제목 | title·h1·h2·p | `02_tag.html`, `03_a.html` |
| 준비물·진행 순서 | ul·ol·li | `04_ul.html` |
| 수업 일정 | table·caption·thead·tbody·tr·th·td | `05_table.html` |
| 신청 위치로 이동 | a·href·id | `03_상대주소/03_a.html` |
| 입력과 선택 | form·label·input·select·textarea·button | `07_form.html` |
| 제출 값 확인 | method=get·name·value·checked·selected | `07_form.html` |

원본의 잘못된 `summary`와 닫기 태그는 반복하지 않는다. 기본 장에서 교정한 구조로 작성한다.

## 2. 먼저 직접 작성하기

1. 탭 제목을 `학습 신청 연습`, 본문 제목을 `HTML 복습 모임`으로 작성한다.
2. 신청 폼으로 이동하는 문서 내부 링크를 만든다.
3. 준비물은 순서 없는 목록, 진행 순서는 번호 목록으로 만든다.
4. 표에는 과목과 시간 열, 데이터 행 두 개를 넣는다.
5. 이름 입력과 두 체크박스, 선택 목록, 메모, 제출·초기화 버튼을 만든다.
6. 각 입력의 제출 이름과 초기값을 적고, 처음 제출될 쿼리를 예상한다.

**성공 기준은 예쁜 화면이 아니라 구조와 제출 결과를 설명하는 것**이다.

<details>
<summary>예시 정답 — 먼저 작성한 뒤 비교하기</summary>

```html
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>학습 신청 연습</title>
</head>
<body>
    <h1>HTML 복습 모임</h1>
    <p>오늘 배운 목록·표·폼을 연결해 봅니다.</p>
    <a href="#application">신청 입력으로 이동</a>

    <h2>준비물</h2>
    <ul>
        <li>수업 코드</li>
        <li>브라우저</li>
    </ul>
    <h2>진행 순서</h2>
    <ol>
        <li>원본 코드 읽기</li>
        <li>결과 예상하기</li>
        <li>브라우저에서 확인하기</li>
    </ol>

    <table border="1">
        <caption>복습 일정</caption>
        <thead>
            <tr><th>과목</th><th>시간</th></tr>
        </thead>
        <tbody>
            <tr><td>목록과 표</td><td>30분</td></tr>
            <tr><td>폼 전송</td><td>30분</td></tr>
        </tbody>
    </table>

    <h2 id="application">신청 입력</h2>
    <form method="get">
        <p>
            <label for="learner">이름</label>
            <input id="learner" name="learner" type="text" value="student">
        </p>
        <p>
            <label><input type="checkbox" name="topic" value="table" checked>표</label>
            <label><input type="checkbox" name="topic" value="form">폼</label>
        </p>
        <p>
            <label for="session">참여 시간</label>
            <select id="session" name="session">
                <option value="am" selected>오전</option>
                <option value="pm">오후</option>
            </select>
        </p>
        <p>
            <label for="memo">메모</label>
            <textarea id="memo" name="memo" rows="3" cols="30">review</textarea>
        </p>
        <button type="submit">신청 연습</button>
        <input type="reset" value="처음 상태로">
    </form>
</body>
</html>
```

</details>

같은 코드의 [실행용 HTML 파일](실습/목록_표_폼_GET제출_복습.html)도 제공한다. GitHub에서는 HTML 소스로 보일 수 있으므로 내려받아 브라우저에서 연다. GET 요청은 현재 문서를 제공하는 로컬 HTTP 서버에서 확인한다. 이 예제에는 신청을 저장하는 서버가 없다. `border`는 기본편과 같은 격자 관찰용 표현이며 이후 CSS로 바꿀 대상이다.

## 3. 예상 결과와 실제 확인

처음 상태에서 제출할 쿼리:

```text
learner=student&topic=table&session=am&memo=review
```

폼 체크박스도 선택하고 시간을 오후로 바꾸면:

```text
learner=student&topic=table&topic=form&session=pm&memo=review
```

같은 이름 `topic`이 반복되어도 두 선택을 표현할 수 있다. 화면에서 `오후`를 선택했지만 값은 `pm`이다. 초기화 버튼은 이 변경을 지우고 처음의 `student`, 표 선택, 오전, `review`로 돌아간다.

## 4. 원본으로 다시 설명해 보기

예시 정답을 읽기 전에, 원본에서 어떤 차이를 배웠는지 다시 확인한다.

| 수업 원본 비교 | 강사님 코드 | 내 코드 | 이 실습에 적용한 판단 |
| --- | --- | --- | --- |
| 표의 설명 | `caption` 아래 잘못 놓인 `summary` | 두 요소를 `hidden`으로 작성 | `caption`을 보이게 두고 잘못된 `summary`를 넣지 않음. [표 원본 비교](05_HTML_테이블.md#groups) |
| 체크박스의 마지막 값 | `name="coffee"`만 있고 `value` 없음 | `value="5"`까지 지정 | 선택지를 구별하려는 이 실습에서는 `topic`마다 값을 지정. [폼 원본 비교](07_HTML_폼과_입력요소.md#choice) |
| GET 전송 | `song`·`singer`에 이름 있음 | 같은 전송 항목, 마지막 `br`만 차이 | 화면 배치보다 `name`·선택 상태를 보고 쿼리 예상. [전송 원본 비교](07-02_HTML_폼_전송과_GET_POST.md#get) |

표의 코드는 원본을 그대로 다시 붙인 것이 아니라 앞 장의 비교를 요약한 것이다. 아래 질문은 **새로 만든 종합실습**의 값으로 답한다.

- 왜 이름에 `id`와 `name`을 둘 다 썼는가?
- 표 체크박스의 `value`를 지우면 어떤 값이 제출되는가?
- 신청 버튼을 `type="button"`으로 바꾸면 기본 제출이 일어나는가?
- GET 제출 후 문서가 다시 보여도 실제 신청 저장까지 끝났는가?

<details>
<summary>해설</summary>

- id는 label 연결, name은 제출 이름에 사용한다.
- 선택되어 제출되면 기본값 `on`이 된다. 강사님 coffee 마지막 항목과 같은 원리다.
- 일반 버튼은 기본 제출을 하지 않는다.
- 아니다. HTML의 요청 구성과 서버 저장은 별개다.

</details>

## 5. 이미지·경로까지 따로 복습하기

원본 `06_img.html`에서 이미지의 너비만 200으로 지정한 경우와 200×300을 모두 지정한 경우를 비교한다. 이 실습의 실제 이미지 경로와 내 문서 위치를 먼저 적는다. 깨진 경로를 고치는 것과 이미지 비율을 고치는 것을 구별한다.

추가편의 `nav`·`article`·`fieldset`·`required`·ARIA를 몰라도 여기까지 설명할 수 있으면 이번 기본 복습을 마친 것이다.

<!-- inlined-extra-2026 -->

## 추가로 알면 좋은 것

이하의 내용은 **수업 원본에서 확인된 필수 진도가 아닌 추가 학습**이다. 위의 기본 설명을 이해한 뒤 필요할 때 읽는다.

<a id="extra-04-1"></a>

### 1. 기본 복습과 달라지는 것

| 기본편에서 배운 것 | 이 프로젝트의 추가 내용 |
| --- | --- |
| 제목·문단·목록 | header·nav·main·section·article·aside·footer로 역할 분리 |
| label·입력·폼 전송 | fieldset·legend·email·required로 입력 구조·검증 확장 |
| id·문서 내부 링크 | 탐색 영역 이름인 aria-label, 날짜의 time |

CSS·JavaScript·이미지 파일·서버 API가 없이도 구조와 브라우저의 입력 검증을 확인하도록 범위를 줄였다. 신청 저장, 발송, 로그인, 상담 처리는 구현하지 않았다.

<a id="extra-04-2"></a>

### 2. 전체 예제

```html
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>학습 과정 안내 — 추가 실습</title>
</head>
<body>
    <header>
        <h1>학습 과정 안내</h1>
        <nav aria-label="주요 메뉴">
            <a href="#courses">과정</a>
            <a href="#consultation">상담 연습</a>
        </nav>
    </header>
    <main>
        <section id="courses">
            <h2>학습 과정</h2>
            <article>
                <h3>HTML 기초</h3>
                <p>문서의 구조와 폼 전송을 공부합니다.</p>
            </article>
            <article>
                <h3>CSS 기초</h3>
                <p>색상·크기·배치를 공부합니다.</p>
            </article>
        </section>
        <section id="consultation">
            <h2>상담 연습</h2>
            <p>실제 상담이 접수되지 않는 예제입니다. 연습용 값만 입력하세요.</p>
            <form method="get">
                <fieldset>
                    <legend>연락 정보</legend>
                    <p>
                        <label for="name">이름</label>
                        <input id="name" name="name" type="text" required>
                    </p>
                    <p>
                        <label for="email">이메일</label>
                        <input id="email" name="email" type="email" required>
                    </p>
                </fieldset>
                <button type="submit">입력 형식 확인</button>
            </form>
        </section>
    </main>
    <aside>
        <h2>먼저 확인할 내용</h2>
        <p>기본편의 name과 value를 이해한 뒤 확장합니다.</p>
    </aside>
    <footer>
        <p>작성일 <time datetime="2026-09-18">2026년 9월 18일</time></p>
    </footer>
</body>
</html>
```

[실행용 HTML 파일](실습/교육과정_추가실습.html)을 저장해 확인할 수 있다. 실제 개인정보 대신 `student`, `student@example.com` 같은 연습용 값을 사용한다.

<a id="extra-04-3"></a>

### 3. 단계별 확인

1. 메뉴를 눌러 같은 문서의 해당 구역으로 이동하는지 확인한다.
2. 빈 폼으로 제출을 시도해 필수 입력 검증을 확인한다.
3. 이메일 칸에 `not-an-email`을 넣고 형식 검증을 확인한다.
4. 예시 값을 넣고 제출하면 현재 문서의 URL에 이름과 값이 구성되는지 확인한다.
5. 이 결과와 실제 상담 저장·이메일 발송이 어떻게 다른지 설명한다.

오류 안내의 문구와 모양은 브라우저·언어 설정마다 다를 수 있다. 이 예제는 브라우저의 기본 입력 검증을 확인하는 것이며, 서버 검증과 접근성 전체 검수를 대체하지 않는다.

<a id="extra-04-4"></a>

### 4. 기존 큰 프로젝트의 나머지 기능은 어디로 갔나?

| 이전 코드의 구성 | 이번 개편에서의 처리 |
| --- | --- |
| 페이지 골격·독립 카드·메뉴 | 이 예제와 시맨틱 구조편으로 통합 |
| 이미지·figure·자막·lazy | [확장 요소](06_HTML_이미지와_미디어.md#extra-02-2)에 역할·파일 전제 정리 |
| 복잡한 표·scope | [표 확장](05_HTML_테이블.md#extra-02-4)으로 분리 |
| 여러 입력 타입·검증 속성 | [폼 확장](07_HTML_폼과_입력요소.md#extra-02-3)으로 분리 |
| time·abbr·address·다운로드 | 확장 요소편으로 분리 |
| CSS·JS·실제 서버·여러 페이지의 경로 | 해당 과목과 프로젝트 구현 단계의 후속 과제로 남김 |
| 메뉴 토글·다크 모드·aria-live·구조화 데이터 | [설계와 검수](09_HTML_실무_코딩스타일.md#extra-03-4)에 후속 학습으로 명시 |

예전 예제의 `assets/css/style.css`, `classroom.webp`, 상세 페이지, `/newsletter` 같은 경로는 파일·서버를 따로 준비해야 했다. 그 큰 코드를 바로 실행 가능한 수업 완성본으로 제시하지 않는다. 원래 파일은 제공된 ZIP에 보존되어 있으며, 이번에는 중복을 줄이고 실행 전제가 분명한 작은 예제로 다시 구성했다.

<!-- legacy-migration -->

<a id="index-section-68"></a>
<a id="index-section-14"></a>
<a id="html-29"></a>
<a id="html-58"></a>
<a id="html-7"></a>
<a id="html-44"></a>
<a id="html-39"></a>
<a id="html-12"></a>
<a id="html-24"></a>
<a id="index-section-65"></a>
<a id="index-section-66"></a>
<a id="html-43"></a>

### 이전 색인 링크 안내

이전 절 주소를 보존한 안내 위치다. 개편 전 절 번호와 현재 절 번호는 서로 다르다. 이전 확장 프로젝트는 [추가로 알면 좋은 것 — 교육과정 페이지](10_HTML_종합실습.md#extra-04-1)로 옮겼다. 이 문서 위쪽은 배운 태그만으로 구성한 새 기본 복습이다.

---

[HTML 목차로 돌아가기](README.md)
