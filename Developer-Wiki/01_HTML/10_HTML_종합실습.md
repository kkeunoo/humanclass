# 10. 종합복습 — 배운 태그로 학습 신청 문서 만들기

[HTML 목차](README.md) · [폼 전송 복습](07-02_HTML_폼_전송과_GET_POST.md)

기존 10번의 교육 사이트 프로젝트에는 시맨틱 영역·ARIA·새 입력 속성 등이 섞여 있었다. 그 내용은 [추가 프로젝트](추가로_알면_좋은_것/04_교육과정_페이지_확장.md)로 분리했다. 이 장은 **양쪽 수업 코드에서 사용한 HTML을 조합하는 기본 복습**이다.

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

같은 코드의 [실행용 HTML 파일](실습/학습신청.html)도 제공한다. GitHub에서는 HTML 소스로 보일 수 있으므로 내려받아 브라우저에서 연다. GET 요청은 현재 문서를 제공하는 로컬 HTTP 서버에서 확인한다. 이 예제에는 신청을 저장하는 서버가 없다. `border`는 기본편과 같은 격자 관찰용 표현이며 이후 CSS로 바꿀 대상이다.

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

[HTML 목차로 돌아가기](README.md)

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

이전 절 주소를 보존한 안내 위치다. 개편 전 절 번호와 현재 절 번호는 서로 다르다. 이전 확장 프로젝트는 [추가로 알면 좋은 것 — 교육과정 페이지](추가로_알면_좋은_것/04_교육과정_페이지_확장.md)로 옮겼다. 이 문서 위쪽은 배운 태그만으로 구성한 새 기본 복습이다.
