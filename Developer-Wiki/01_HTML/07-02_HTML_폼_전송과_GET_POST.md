# 폼 전송 — 이름과 값을 고르고 GET·POST 요청으로 보내기

[HTML 목차](README.md) · [이전: 입력요소](07_HTML_폼과_입력요소.md) · [다음: 종합실습](10_HTML_종합실습.md)

앞 장에서는 입력창의 초기 상태와 선택을 읽었다. 이제 그중 무엇을 요청에 담고 어느 주소로 보낼지 결정한다. **입력 화면 → 제출 항목 → 요청 → 서버 응답**을 각각 확인해야 ‘화면에 있던 값이 왜 빠졌는가’와 ‘왜 전송 후 오류가 났는가’를 설명할 수 있다.

<a id="chapter-toc"></a>

**목차:** [1 준비](#learn) · [2 개념과 항목 구성](#concepts) · [3 전체 예제](#example) · [4 내 코드](#my-code) · [5 받는 쪽과 연결](#connections) · [6 코드 검토](#review) · [7 강사님 비교](#teacher) · [8 결과·확인 순서](#results) · [9 TIP](#tips) · [10 복습](#practice)

<a id="learn"></a>

## 1. 이번 장에서 배울 것

| 조건 | 내용 |
| --- | --- |
| 실제 수업 파일 | 양쪽 `workspace_html/07_form.html`의 GET·검색·POST 폼 |
| 앞선 학습 | name·value·선택·readonly·disabled |
| 새 파일 | [실습/07-02_전송_복습.html](실습/07-02_전송_복습.html) |
| 입력 UI 확인 | 로컬 파일로도 가능 |
| 요청 방식·대상 확인 | 수업의 Live Server 등 HTTP 미리보기에서 열고 Network로 관찰 |
| 서버 역할 | 새 파일에는 값을 저장하거나 POST를 처리하는 서버 코드가 없음 |
| 결과 구분 | 코드·규칙 기준 예상과 현재 실제 실행 기록 구별 |

새 예제는 외부 검색 서비스를 대상으로 제출하지 않고 자기 문서를 대상으로 한다. 정적 서버에서 GET으로 같은 HTML이 다시 보이면 **요청을 받아 문서를 제공한 것**이지, 입력한 값을 DB에 저장한 증거가 아니다. POST 처리 지원은 별도로 확인한다.

<a id="concepts"></a>
<a id="action"></a>

## 2. 개념부터 이해하기

### 2.1 폼이 정하는 세 가지

| 설정 | 정하는 것 | 질문 |
| --- | --- | --- |
| `action` | 요청을 받을 주소 | 어디로 보낼까? |
| `method` | 전송 방식 | GET인가 POST인가? |
| 각 입력의 `name`·현재값·상태 | 제출할 항목 | 무엇을 보낼까? |

target은 응답을 어느 문맥에 열지 정하며, 값의 이름이나 요청 대상을 대신하지 않는다. 이 수업처럼 action을 생략하면 현재 문서 주소를 대상으로 하고 method를 생략하면 기본 GET으로 제출한다.

예를 들어 `name="song"` 입력에 hello가 있으면 제출 항목은 `song=hello`로 읽는다. 같은 화면에 입력이 세 개 있어도 이름이 없는 입력은 일반 폼 전송의 이름 있는 항목으로 포함되지 않는다.

<a id="entries"></a>

### 2.2 제출할 항목을 먼저 고르기

| 현재 상태 | 이 수업의 일반 제출에서 |
| --- | --- |
| name이 없음 | 제외 |
| 이름 있는 텍스트 값이 빈 문자열 | 이름과 빈 값의 항목이 될 수 있음 |
| 이름 있는 readonly 텍스트 | 제출 가능 |
| disabled | 제외 |
| 체크박스·라디오 미선택 | 제외 |
| 선택된 체크박스·라디오에 value 없음 | 기본값 on |
| 선택한 option에 value 있음 | 표시 글자보다 value 사용 |
| 일반 type=button | 자동으로 제출 버튼 항목이 되지 않음 |
| 실제 제출에 사용한 이름 있는 제출 버튼 | 그 이름·값도 포함될 수 있음 |

화면에 빈칸으로 보이는 것과 항목이 아예 없는 것은 다르다. 이름 있는 텍스트 입력의 빈 값은 `song=`으로 표현될 수 있고, 이름 없는 입력은 그 이름조차 만들지 않는다.

같은 name의 체크박스 두 개가 선택되면 **이름이 같은 두 항목**이 된다. `coffee=1&coffee=2`를 HTML 단계에서 ‘뒤의 값만 남는다’고 단정하지 않는다. 받는 쪽이 여러 값을 어떻게 읽는지는 서버 코드에서 확인할 문제다.

> 📚 **출처 · 본문 설명 확인:** 제출할 항목을 구성하는 조건과 폼 제출은 [HTML 표준 — Form control infrastructure](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html)로 확인했다. 여기의 표는 파일 업로드 등 추가 기능 없이 수업의 기본 입력에 적용한 설명이다.

<a id="get"></a>

### 2.3 GET과 POST에서 값이 있는 자리

| 비교 | 이 수업의 GET 폼 | 이 수업의 POST 폼 |
| --- | --- | --- |
| 값의 위치 | 보통 URL의 쿼리 문자열 | 요청 본문 |
| 주소창에서 볼 것 | `?` 뒤 이름과 값 | 본문 값은 쿼리로 붙지 않음 |
| 받는 쪽 | 해당 GET 요청 처리 | 해당 POST 요청 처리 |

GET에서 이름과 값은 `=`로, 여러 항목은 `&`로 구분하고 보통 주소의 `?` 뒤에 둔다. 공백·한글·특수문자는 전송 형식에 맞게 인코딩되므로 주소 표시가 사용자가 입력한 글자와 완전히 같지 않을 수 있다.

POST는 ‘주소가 절대로 바뀌지 않는다’는 뜻이 아니다. action이 다른 주소이거나 서버가 다른 곳으로 이동시키면 주소도 달라질 수 있다. **폼 값을 URL 쿼리로 붙이는 대신 본문에 넣는다는 차이**로 먼저 이해한다. POST라는 방식 자체가 암호화를 제공하지도 않는다.

<a id="example"></a>

## 3. 작은 예제와 결과

**설명용 새 예제 · 전체 문서.** [07-02_전송_복습.html](실습/07-02_전송_복습.html)과 같은 내용이다. 이 파일만으로 GET 화면 재표시는 가능해도 POST를 저장·처리할 서버가 생기지는 않는다.

```html
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <title>GET과 POST 복습</title>
</head>
<body>
    <h1>제출 항목 확인</h1>
    <form action="07-02_전송_복습.html" method="get">
        <p><label>노래 <input type="text" name="song" value="hello"></label></p>
        <p><label>이름 없는 입력 <input type="text" value="ignored"></label></p>
        <p><label>읽기 전용 <input type="text" name="fixed" value="A" readonly></label></p>
        <p><label>비활성 <input type="text" name="off" value="B" disabled></label></p>
        <p><label><input type="checkbox" name="coffee" value="1" checked>샷추가</label>
            <label><input type="checkbox" name="coffee" value="2" checked>펄추가</label>
            <label><input type="checkbox" name="coffee" value="5">얼음추가</label></p>
        <p><label>종류 <select name="course">
            <option value="1">한식</option>
            <option value="4" selected>분식</option>
        </select></label></p>
        <p><label>메모 <textarea name="memo">note</textarea></label></p>
        <button type="submit">GET 전송</button>
    </form>
    <h2>POST는 받는 서버의 지원도 필요</h2>
    <form action="07-02_전송_복습.html" method="post">
        <label>검색어 <input type="text" name="query" value="hello"></label>
        <button type="submit">POST 전송</button>
    </form>
</body>
</html>
```

**초기 상태의 항목 구성 기준 예상:** 첫 폼의 이름과 값은 다음과 같다. 브라우저로 새로 전송해 받은 기록이 아니라 코드의 상태와 제출 규칙에서 도출한 값이다.

```text
song=hello&fixed=A&coffee=1&coffee=2&course=4&memo=note
```

| 코드에 있는 것 | 포함 여부 | 이유 |
| --- | --- | --- |
| song=hello | 포함 | 이름 있는 현재값 |
| ignored | 제외 | name 없음 |
| fixed=A | 포함 | readonly는 비활성과 다름 |
| off=B | 제외 | disabled |
| coffee=1·2 | 둘 다 포함 | 두 항목 선택 |
| coffee=5 | 제외 | 미선택 |
| course=4 | 포함 | 선택한 option의 value |
| memo=note | 포함 | 이름 있는 textarea 현재 내용 |

**하나만 바꾸는 실험:** coffee 값 1인 체크박스의 선택만 해제한다. 다른 상태는 그대로라면 `coffee=1`만 빠진다. 다음 실험은 선택을 복원한 뒤 시작한다. 한 번에 여러 항목을 바꾸면 제외된 원인을 설명하기 어렵다.

<a id="my-code"></a>

## 4. 내 코드 따라 읽기

### 4.1 이름 없는 입력을 둔 GET 실험

**내 코드 · 원본 발췌** — `workspace_html/07_form.html` 129–134행.

```html
        <form method="get">
            <input type="text" name="song"><br>
            <input type="text"><br>
            <input type="text" name="singer"><br>
            <input type="submit" value="get 연습"><br>
        </form>
```

첫 입력과 셋째 입력에만 name이 있다. song에 hello, 가운데 입력에 ignored, singer에 student를 적었다면 제출 항목은 `song=hello&singer=student`다. 가운데 입력이 보이거나 글자를 입력할 수 있다는 사실이 제출 항목임을 보장하지 않는다.

action이 없으므로 현재 문서 주소를 대상으로 한다. 같은 문서가 다시 열린다고 위 입력 내용이 서버에 저장된 것은 아니다.

<a id="post"></a>

### 4.2 본문으로 값을 보내는 POST 실험

**내 코드 · 원본 발췌** — 같은 파일 147–150행.

```html
        <form method="post">
            <input type="text" name="query"><br>
            <input type="submit" value="post 연습"><br>
        </form>
```

query의 값을 현재 주소로 POST한다. 이 HTML에는 그 요청을 처리하는 서버 함수가 없다. 원본의 Live Server 관련 메모는 **특정 정적 서버가 POST를 처리하지 못한 관찰**로 읽어야 한다. 모든 서버가 같은 상태 코드나 같은 화면으로 실패한다는 일반 법칙은 아니다.

<a id="connections"></a>

## 5. 받는 쪽과 연결하기

원본에는 네이버 검색 폼의 name query, 구글 검색 폼의 name q가 있다. 같은 검색어를 담아도 받는 쪽이 기대하는 데이터 이름에 맞춰야 한다. 링크 주소만 맞으면 이름은 아무렇게나 정해도 된다는 뜻이 아니다.

```text
input의 name과 현재값
   → 폼이 제출 항목 구성
   → action 주소에 GET 또는 POST 요청
   → 서버가 기대하는 이름으로 읽음
   → 처리 결과를 응답
```

이 단계에는 아직 import한 Python 함수가 없다. ‘서버가 값을 받는다’는 말만으로 구현까지 있다고 가정하지 않는다. 이후 FastAPI 단원의 실제 라우터 함수에서 그 이름을 어디서 읽고 무엇을 반환하는지 연결한다.

| 경계 | 이 HTML이 하는 것 | 다른 구현이 필요한 것 |
| --- | --- | --- |
| 입력 화면 | 사용자 값 편집·선택 | 자료 저장 규칙 |
| 폼 제출 | 대상·방식·항목 구성 | 서버의 처리 함수 |
| 응답 화면 | 서버가 보낸 결과 열기 | 저장 성공 여부의 판단 |

외부 검색 서비스의 현재 결과는 이 문서의 고정 출력으로 쓰지 않는다. 새 예제는 로컬 자기 문서를 대상으로 해 요청 구조에 집중한다.

<a id="review"></a>

## 6. 내 코드 돌아보기

name이 있는 입력과 없는 입력을 나란히 둔 점이 좋다. 주소에 보이는 값과 보이지 않는 입력을 비교할 수 있다. 또한 원본은 POST 오류 화면이 떠도 개발자도구에서 요청 값을 확인할 수 있다고 기록했다. **전송과 처리 성공을 분리해 본 관찰**이다.

| 원본의 메모·선택 | 평가 종류 | 정확하게 읽기 |
| --- | --- | --- |
| 이름 없는 입력 | 수업용 비교 | 실제 필요한 항목에는 name을 명시 |
| POST는 주소 변경 없음 | 설명 보완 | 값이 쿼리에 붙지 않는다는 차이로 읽기 |
| 정적 서버의 POST 오류 | 환경에 따른 관찰 | 서버·응답 상태를 따로 확인 |
| 검색 서비스별 이름 다름 | 필요한 계약 | 받는 쪽이 기대하는 query·q를 맞춤 |

**개선 예시 · 원본에 미적용:** 3절은 action을 파일명으로 명시하고 초기값·상태도 적어 예상 항목을 비교하기 쉽게 했다. 서버 저장 기능을 추가한 개선이 아니라 **요청을 설명하기 쉬운 학습용 구성**이다.

<a id="teacher"></a>

## 7. 강사님 코드에서 배울 점

GET·POST 원본의 입력 이름과 전송 방식은 강사님과 내가 같다. 마지막 br 등 표시 차이는 제출 원리를 바꾸지 않아 긴 원본을 두 번 인용하지 않는다.

이 장에서는 어느 쪽이 더 좋다고 평가할 차이보다 **같은 요청 규칙이 두 코드에 적용된다**는 점을 확인한다. 양쪽 모두의 name 없는 입력은 비교 실험으로 읽고, 실제 데이터로 필요하면 이름을 추가한다.

<a id="results"></a>

## 8. 결과와 확인 방법

### 8.1 전송을 볼 때 확인할 순서

수업에서 사용한 HTTP 미리보기로 새 예제를 연다. 실제 URL은 프로젝트의 서버 루트와 폴더 위치에 따라 다르다. 입력을 초기 상태로 둔 뒤 제출하고 브라우저 개발자도구의 Network에서 해당 요청을 선택한다.

| 순서 | 확인할 것 | 비교 기준 |
| --- | --- | --- |
| 1 | Request URL | action을 현재 문서에서 계산한 대상 |
| 2 | 요청 방식 | GET인지 POST인지 |
| 3 | 보낸 값 | GET 쿼리 또는 POST 본문 |
| 4 | 서버 응답 상태 | 요청을 어떻게 처리했는지 |
| 5 | 응답 내용 | 문서 재표시·오류·저장 결과 등을 구별 |

상태 코드가 오류여도 요청 값이 보내졌을 수 있다. 반대로 문서가 정상 표시돼도 그 서버가 값을 저장했다고 결론 내릴 수 없다. 원본의 관찰 순서처럼 **보낸 데이터와 응답을 각각 확인**한다.

### 8.2 경계·오류 사례

| 바뀐 조건 | 예상되는 차이 |
| --- | --- |
| 이름 있는 song을 빈칸으로 지움 | song= 같은 빈 값의 항목 가능 |
| song의 name 제거 | 항목 자체 제외 |
| 체크박스의 value 제거 후 선택 | 기본값 on 사용 |
| 같은 이름 두 개 선택 | 두 항목으로 구성; 서버 해석은 별도 |
| POST를 지원하지 않는 정적 서버 | 방식 미지원 등의 오류 응답 가능 |
| file 주소로 POST 시험 | HTTP 서버 처리와 같은 전제로 판단하면 안 됨 |

예제의 초기 항목·action 상대 경로·방식은 정적으로 검사한다. 브라우저에서 새로 제출한 네트워크 기록이나 실제 POST 저장을 확인한 것처럼 표시하지 않는다. 이전 편집 기록에 있는 별도 로컬 수신 테스트와 이번 개편의 검증 범위를 구별한다.

<a id="tips"></a>

## 9. 추가로 알면 좋은 것

> 💡 **TIP · 수업 범위 밖:** 파일 첨부와 enctype, JavaScript의 FormData·fetch로 요청을 구성하는 방법은 별도 주제다. 기본 GET·POST 폼을 이해하기 전에 그 코드를 먼저 요구하지 않는다. 요청을 만드는 방법이 늘어나도 대상·방식·이름과 값·응답이라는 확인 순서는 유지된다.

> 🔗 **다음 학습:** FastAPI에서 경로·쿼리·폼·모델 입력을 배우면 이 HTML의 name과 실제 서버 함수의 입력을 맞춰 볼 수 있다. 지금 단계의 HTML만으로 서버의 입력 검증과 저장이 완성된 것은 아니다.

<a id="practice"></a>

## 10. 복습과 다음 학습

1. id만 있고 name이 없는 입력이 자동으로 그 id 이름으로 전송될까?
2. 같은 coffee 체크박스 두 개가 선택되면 왜 한 값만 남는다고 단정할 수 없을까?
3. 3절에서 name 없는 ignored 입력도 보내려면 어디를 고칠까?

<details>
<summary>풀이</summary>

id는 제출 이름을 대신하지 않는다. 같은 name의 선택 항목들은 여러 항목으로 전송될 수 있고, 서버가 읽는 방식을 봐야 한다. ignored 입력을 보내려면 예를 들어 name="extra"를 추가한다. 초기값은 그대로라면 extra=ignored라는 항목이 생긴다. 원래 기본 예측에는 그 이름이 없었다.

</details>

| 빠른 확인 | 질문 |
| --- | --- |
| action | 어디로 보낼까? |
| method | GET·POST 중 무엇인가? |
| name | 제출 이름이 있는가? |
| 상태 | 활성·선택 조건을 갖췄는가? |
| 현재값 | 초기값을 사용자가 바꿨는가? |
| 응답 | 전송과 처리 성공을 구분했는가? |

원본 비교와 첨부 학습 메모를 바탕으로 작성하고, 외부 설명은 [HTML 폼 제출 표준](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html)에서 2026-10-28 확인했다. 외부 문장을 그대로 가져온 직접 인용은 없다.

[장별 문제](실습/연습문제/07-02_HTML_폼_전송과_GET_POST_연습문제.md) → [종합실습](10_HTML_종합실습.md) → [실무 코딩스타일](09_HTML_실무_코딩스타일.md)
