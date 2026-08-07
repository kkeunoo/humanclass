---
title: HTML 테이블
version: v2.0-final
last_updated: 2026-08-07
status: Completed
---

# HTML 테이블

## 문서 정보

| 항목 | 내용 |
| --- | --- |
| 문서 | `05_HTML_테이블.md` |
| 분류 | `01_HTML` |
| 원본 기준 | `workspace_html/05_table.html`, `workspace_teacher/workspace_html/05_table.html` |
| 핵심 범위 | `table`, `caption`, `thead`, `tbody`, `tfoot`, `tr`, `th`, `td`, `scope`, `colspan`, `rowspan`, `colgroup` |
| 학습 범위 | 표 구조, 제목 셀과 데이터 셀, 셀 병합, 접근성, 반응형 Table |
| 프로젝트 연결 | 게시판, 관리자 화면, 통계표, 가격표, 일정표, 데이터 비교 |
| 문서 형식 | HTML Developer-Wiki V2 확정 형식 |

> 이 문서는 내 코드와 강사님 코드의 `05_table.html`을 비교해 `table`, `tr`, `th`, `td`, `caption`, `thead`, `tbody`, `colspan`, `rowspan`의 역할을 정리한다. 원본의 잘못된 `summary`, 닫는 Tag 오류, Presentational Attribute, 숨겨진 `caption`, 행별 셀 개수 설명을 수정하고 접근성과 반응형 Table 처리까지 연결한다.

# 학습 목표

- 표가 필요한 데이터와 일반 레이아웃을 구분한다.
- `table`, `tr`, `th`, `td`의 역할을 설명한다.
- `caption`, `thead`, `tbody`, `tfoot`으로 표의 구조를 구분한다.
- `colspan`, `rowspan`으로 셀을 병합한다.
- 병합 후 각 행의 논리적인 열 개수를 맞춘다.
- `scope` 속성으로 제목 셀과 데이터 셀의 관계를 명확히 한다.
- `border`, `width`, `height` 같은 표현 속성을 CSS로 대체한다.
- 원본 실습 코드의 잘못된 마크업과 오래된 작성 방식을 찾아 개선한다.
- 게시판 목록과 비교표를 의미 있는 테이블로 작성한다.

# 1. 테이블이란

테이블은 서로 관련된 데이터를 **행(row)**과 **열(column)**로 정리하는 HTML 구조입니다.

```html
<table>
  <tr>
    <th>이름</th>
    <th>직무</th>
  </tr>
  <tr>
    <td>홍길동</td>
    <td>프론트엔드 개발자</td>
  </tr>
</table>
```

위 표는 다음 관계를 표현합니다.

| 행 | 의미 |
| --- | --- |
| 첫 번째 행 | 각 열의 제목 |
| 두 번째 행 | 한 사람에 대한 데이터 |

테이블의 핵심은 선이나 칸 모양이 아니라 **데이터 사이의 관계**입니다.

# 2. 테이블을 사용해야 하는 경우

다음과 같이 행과 열의 교차 관계가 중요한 데이터에 사용합니다.

- 게시판 목록
- 성적표
- 시간표
- 상품 가격 비교
- 재고 현황
- 통계 데이터
- 관리자 페이지의 회원 목록
- 일정표

```html
<table>
  <caption>과정별 수강 현황</caption>
  <thead>
    <tr>
      <th scope="col">과정</th>
      <th scope="col">신청 인원</th>
      <th scope="col">정원</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>HTML/CSS</td>
      <td>24명</td>
      <td>30명</td>
    </tr>
  </tbody>
</table>
```

# 3. 테이블을 사용하면 안 되는 경우

과거에는 웹페이지 전체 배치를 만들기 위해 테이블을 사용하기도 했지만, 현재는 올바른 방식이 아닙니다.

```html
<!-- 레이아웃 목적으로 사용하지 않는다. -->
<table>
  <tr>
    <td>헤더</td>
  </tr>
  <tr>
    <td>본문</td>
  </tr>
  <tr>
    <td>푸터</td>
  </tr>
</table>
```

페이지 구조는 의미에 맞는 요소와 CSS 레이아웃을 사용합니다.

```html
<header>헤더</header>
<main>본문</main>
<footer>푸터</footer>
```

| 목적 | 권장 기술 |
| --- | --- |
| 행과 열로 구성된 데이터 | HTML 테이블 |
| 페이지 전체 배치 | Flexbox, Grid |
| 카드 목록 | `ul`, `li`, CSS Grid |
| 입력 화면 정렬 | `form`, `label`, CSS |

# 4. 테이블의 기본 구성

가장 기본적인 테이블은 `table`, `tr`, `th`, `td`로 구성합니다.

```html
<table>
  <tr>
    <th>지역</th>
    <th>이름</th>
  </tr>
  <tr>
    <td>천안</td>
    <td>홍길동</td>
  </tr>
</table>
```

| 요소 | 의미 | 역할 |
| --- | --- | --- |
| `table` | Table | 표 전체 |
| `tr` | Table Row | 한 행 |
| `th` | Table Header | 행이나 열의 제목 셀 |
| `td` | Table Data | 일반 데이터 셀 |

# 5. `table`: 표 전체 영역

`table`은 표의 시작과 끝을 나타냅니다.

```html
<table>
  <!-- 표의 행과 셀 -->
</table>
```

`table` 자체만 작성하면 화면에 데이터가 나타나지 않습니다. 내부에 행과 셀을 구성해야 합니다.

```html
<table>
  <tr>
    <td>데이터</td>
  </tr>
</table>
```

# 6. `tr`: 한 행

`tr`은 Table Row의 약자로, 표의 가로 한 줄을 나타냅니다.

```html
<tr>
  <td>내용 1</td>
  <td>내용 2</td>
  <td>내용 3</td>
</tr>
```

하나의 `tr` 안에 여러 개의 `th` 또는 `td`를 작성하면 가로 방향으로 셀이 배치됩니다.

```html
<table>
  <tr>
    <td>1행 1열</td>
    <td>1행 2열</td>
  </tr>
  <tr>
    <td>2행 1열</td>
    <td>2행 2열</td>
  </tr>
</table>
```

# 7. `td`: 데이터 셀

`td`는 Table Data의 약자로, 일반 데이터를 담는 셀입니다.

```html
<table>
  <tr>
    <td>HTML</td>
    <td>기초</td>
    <td>20시간</td>
  </tr>
</table>
```

`td` 안에는 텍스트뿐 아니라 링크, 이미지, 버튼 등 다양한 요소를 넣을 수 있습니다.

```html
<td>
  <a href="post-detail.html">게시글 보기</a>
</td>
```

다만 셀 안의 콘텐츠가 복잡해질수록 표가 실제로 적절한 구조인지 다시 검토해야 합니다.

# 8. `th`: 제목 셀

`th`는 Table Header의 약자로, 행 또는 열의 제목을 나타냅니다.

```html
<table>
  <tr>
    <th>이름</th>
    <th>지역</th>
  </tr>
  <tr>
    <td>홍길동</td>
    <td>천안</td>
  </tr>
</table>
```

브라우저는 기본적으로 `th`를 굵고 가운데 정렬된 형태로 표시할 수 있지만, 핵심은 모양이 아니라 **제목 셀이라는 의미**입니다.

## 8.1 열 제목

```html
<thead>
  <tr>
    <th scope="col">번호</th>
    <th scope="col">제목</th>
    <th scope="col">작성자</th>
  </tr>
</thead>
```

## 8.2 행 제목

```html
<tbody>
  <tr>
    <th scope="row">HTML</th>
    <td>20시간</td>
    <td>기초</td>
  </tr>
</tbody>
```

| `scope` 값 | 의미 |
| --- | --- |
| `col` | 해당 `th`가 열 제목 |
| `row` | 해당 `th`가 행 제목 |
| `colgroup` | 여러 열의 그룹 제목 |
| `rowgroup` | 여러 행의 그룹 제목 |

# 9. `th`와 `td`의 차이

| 구분 | `th` | `td` |
| --- | --- | --- |
| 의미 | 제목 셀 | 데이터 셀 |
| 기본 표현 | 굵게, 가운데 정렬될 수 있음 | 일반 글자, 왼쪽 정렬될 수 있음 |
| 접근성 | 다른 셀의 기준 정보 제공 | 실제 데이터 제공 |
| 대표 위치 | 첫 행 또는 첫 열 | 표의 본문 |

다음 코드는 화면상 비슷하게 보이도록 CSS를 적용할 수 있지만 의미는 다릅니다.

```html
<!-- 의미 있는 제목 셀 -->
<th scope="col">작성자</th>
```

```html
<!-- 단순히 굵게 보이게 만든 데이터 셀 -->
<td class="bold">작성자</td>
```

제목 역할이라면 `td`에 굵은 글씨를 적용하는 대신 `th`를 사용합니다.

# 10. 행마다 셀 개수를 맞추기

병합하지 않은 기본 표에서는 각 행의 셀 개수를 동일하게 맞추는 것이 중요합니다.

```html
<!-- 올바른 예 -->
<table>
  <tr>
    <td>1-1</td>
    <td>1-2</td>
    <td>1-3</td>
  </tr>
  <tr>
    <td>2-1</td>
    <td>2-2</td>
    <td>2-3</td>
  </tr>
</table>
```

```html
<!-- 논리적인 열 개수가 맞지 않는 예 -->
<table>
  <tr>
    <td>1-1</td>
    <td>1-2</td>
    <td>1-3</td>
  </tr>
  <tr>
    <td>2-1</td>
    <td>2-2</td>
    <td>2-3</td>
    <td>2-4</td>
  </tr>
</table>
```

브라우저가 표를 어느 정도 보정해 표시할 수는 있지만, 데이터 구조가 불규칙해지고 열의 관계가 명확하지 않게 됩니다.

> 셀 병합을 사용한 경우에는 단순한 태그 개수가 아니라 `colspan`과 `rowspan`이 차지하는 범위까지 포함하여 논리적인 열 수를 계산해야 합니다.

# 11. 표 제목 `caption`

`caption`은 표 전체의 제목이나 설명을 제공합니다.

```html
<table>
  <caption>2026년 교육 과정 신청 현황</caption>
  <tr>
    <th scope="col">과정</th>
    <th scope="col">신청 인원</th>
  </tr>
  <tr>
    <td>웹 개발</td>
    <td>24명</td>
  </tr>
</table>
```

`caption`은 일반적으로 `table`의 첫 번째 자식으로 작성합니다.

```html
<table>
  <caption>게시판 목록</caption>
  <thead>...</thead>
  <tbody>...</tbody>
</table>
```

## 11.1 `caption`을 숨겨야 하는 경우

화면 디자인상 제목을 별도의 `h2`로 이미 제공했더라도, 표의 접근 가능한 이름을 보완하기 위해 `caption`을 시각적으로만 숨길 수 있습니다.

```html
<h2>공지사항</h2>
<table>
  <caption class="sr-only">공지사항 게시글 목록</caption>
  <!-- 표 내용 -->
</table>
```

```css
.sr-only {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  white-space: nowrap;
  border: 0;
}
```

`hidden` 속성은 보조 기술에서도 제외될 수 있으므로, 접근성 정보를 제공할 목적이라면 시각적 숨김 클래스를 사용하는 편이 적절합니다.

# 12. 표의 구조 구분

표는 `thead`, `tbody`, `tfoot`으로 영역을 구분할 수 있습니다.

```html
<table>
  <caption>상품 주문 내역</caption>
  <thead>
    <tr>
      <th scope="col">상품</th>
      <th scope="col">수량</th>
      <th scope="col">금액</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>키보드</td>
      <td>1개</td>
      <td>80,000원</td>
    </tr>
  </tbody>
  <tfoot>
    <tr>
      <th scope="row" colspan="2">합계</th>
      <td>80,000원</td>
    </tr>
  </tfoot>
</table>
```

| 요소 | 역할 |
| --- | --- |
| `thead` | 제목 행 그룹 |
| `tbody` | 주요 데이터 행 그룹 |
| `tfoot` | 합계, 요약 등 마지막 행 그룹 |

이 요소들은 반드시 화면에 별도의 선이나 배경을 자동으로 만드는 것은 아닙니다. 주로 구조와 의미를 구분하며, 스타일은 CSS로 적용합니다.

# 13. `thead`: 제목 영역

`thead`는 표의 열 제목처럼 머리말 역할을 하는 행을 묶습니다.

```html
<thead>
  <tr>
    <th scope="col">번호</th>
    <th scope="col">제목</th>
    <th scope="col">작성자</th>
    <th scope="col">작성일</th>
  </tr>
</thead>
```

`thead` 안에는 하나 이상의 `tr`을 작성할 수 있습니다.

```html
<thead>
  <tr>
    <th rowspan="2" scope="col">과정</th>
    <th colspan="2" scope="colgroup">수강 인원</th>
  </tr>
  <tr>
    <th scope="col">온라인</th>
    <th scope="col">오프라인</th>
  </tr>
</thead>
```

# 14. `tbody`: 데이터 영역

`tbody`는 표의 주요 데이터를 묶습니다.

```html
<tbody>
  <tr>
    <td>1</td>
    <td>HTML 테이블 정리</td>
    <td>홍길동</td>
    <td>2026-07-28</td>
  </tr>
  <tr>
    <td>2</td>
    <td>CSS 선택자 복습</td>
    <td>김개발</td>
    <td>2026-07-29</td>
  </tr>
</tbody>
```

브라우저는 작성자가 `tbody`를 생략해도 내부적으로 삽입할 수 있습니다. JavaScript로 `table`의 자식 요소를 탐색할 때 예상과 다른 구조가 보일 수 있으므로 명시적으로 작성하는 습관이 좋습니다.

# 15. `tfoot`: 요약 영역

`tfoot`은 합계나 요약 정보를 담는 행 그룹입니다.

```html
<tfoot>
  <tr>
    <th scope="row">합계</th>
    <td>3개 과정</td>
    <td>72명</td>
  </tr>
</tfoot>
```

모든 표에 필요한 것은 아닙니다. 합계나 정리 행이 있는 경우에 사용합니다.

# 16. 셀 병합 `colspan`

`colspan`은 하나의 셀이 여러 열을 차지하도록 합니다.

```html
<table>
  <tr>
    <th colspan="2">연락처</th>
  </tr>
  <tr>
    <td>전화번호</td>
    <td>이메일</td>
  </tr>
</table>
```

`colspan="2"`는 해당 셀이 가로 방향으로 두 칸을 차지한다는 의미입니다.

## 16.1 병합 전후

병합 전:

```html
<tr>
  <td>1-1</td>
  <td>1-2</td>
  <td>1-3</td>
</tr>
```

두 번째와 세 번째 열을 병합한 후:

```html
<tr>
  <td>1-1</td>
  <td colspan="2">1-2와 1-3 병합</td>
</tr>
```

병합된 범위에 해당하는 기존 셀은 제거해야 합니다.

# 17. 셀 병합 `rowspan`

`rowspan`은 하나의 셀이 여러 행을 차지하도록 합니다.

```html
<table>
  <tr>
    <th rowspan="2">연락처</th>
    <td>010-1234-5678</td>
  </tr>
  <tr>
    <td>user@example.com</td>
  </tr>
</table>
```

`rowspan="2"`가 첫 번째 행과 두 번째 행의 같은 열을 차지하므로, 두 번째 행에는 해당 위치의 셀을 다시 작성하지 않습니다.

# 18. `colspan`과 `rowspan` 함께 사용하기

```html
<table>
  <tr>
    <td rowspan="2">1-1</td>
    <td colspan="2">1-2</td>
  </tr>
  <tr>
    <td>2-2</td>
    <td>2-3</td>
  </tr>
</table>
```

논리적인 열 개수는 모든 행에서 3개입니다.

| 행 | 작성된 셀 | 실제 차지하는 열 |
| --- | --- | --- |
| 1행 | `rowspan` 셀 1개 + `colspan="2"` 셀 1개 | 3열 |
| 2행 | 일반 셀 2개 | 앞 행의 `rowspan` 1열 + 현재 2열 = 3열 |

## 18.1 안전하게 병합하는 순서

1. 먼저 병합 없이 전체 셀을 작성한다.
2. 병합할 시작 셀에 `colspan` 또는 `rowspan`을 추가한다.
3. 병합 범위에 포함된 나머지 셀을 제거한다.
4. 각 행의 논리적인 열 개수를 확인한다.
5. 제목 셀의 `scope` 관계를 검토한다.

원본 실습의 “먼저 전체 칸을 만든 뒤 영향을 받는 셀을 지운다”는 방법은 병합 구조를 이해하기 좋은 방식입니다.

# 19. 셀 안에 작성할 수 있는 콘텐츠

`th`와 `td` 안에는 일반적인 플로 콘텐츠를 작성할 수 있습니다.

```html
<td>
  <img src="profile.jpg" alt="홍길동 프로필">
  <strong>홍길동</strong>
</td>
```

```html
<td>
  <a href="post.html">HTML 테이블 작성법</a>
</td>
```

```html
<td>
  <button type="button">수정</button>
</td>
```

그러나 `tr` 바로 아래에는 일반 텍스트나 링크를 직접 작성하지 않고 `th` 또는 `td` 안에 넣어야 합니다.

```html
<!-- 잘못된 구조 -->
<tr>
  게시글 제목
  <a href="post.html">보기</a>
</tr>
```

```html
<!-- 올바른 구조 -->
<tr>
  <td>게시글 제목</td>
  <td><a href="post.html">보기</a></td>
</tr>
```

# 20. 원본 코드에서 확인한 오류와 개선점

원본 실습은 테이블의 핵심 구조와 병합 원리를 단계적으로 확인하기에 유용합니다. 다만 일부 코드는 현재 HTML 기준에 맞게 보완할 필요가 있습니다.

## 20.1 `summary` 요소는 `table`의 설명 요소가 아니다

원본 강사님 코드에는 다음 구조가 있습니다.

```html
<table>
  <caption>테이블 내용에 대한 설명</caption>
  <summary>제목, 작성자</summary>
  <!-- ... -->
</table>
```

`summary`는 `details` 요소의 요약 제목으로 사용하는 요소이며, `table`의 자식으로 사용하는 요소가 아닙니다.

```html
<details>
  <summary>상세 정보 보기</summary>
  <p>추가 설명</p>
</details>
```

표의 제목은 `caption`으로 제공하고, 추가 설명이 필요하면 표 주변의 문단이나 `aria-describedby`를 활용할 수 있습니다.

```html
<p id="board-description">최근 등록된 게시글을 최신순으로 제공합니다.</p>
<table aria-describedby="board-description">
  <caption>게시판 목록</caption>
  <!-- ... -->
</table>
```

## 20.2 닫는 태그가 잘못된 `th`

내 코드에는 다음 오타가 있습니다.

```html
<th width="30"></td>
```

시작 태그가 `th`이면 닫는 태그도 `</th>`여야 합니다.

```html
<th width="30"></th>
```

내용이 없는 제목 셀이라면 접근성 측면에서 무엇을 나타내는 열인지 확인해야 합니다.

```html
<th scope="col">번호</th>
```

## 20.3 `border` 속성 대신 CSS 사용

실습에서 구조를 확인하기 위해 다음처럼 작성했습니다.

```html
<table border="1">
```

학습 과정에서 칸을 빠르게 확인하기에는 편리하지만, 실무에서는 표현을 CSS로 분리합니다.

```html
<table class="board-table">
```

```css
.board-table,
.board-table th,
.board-table td {
  border: 1px solid #ccc;
}

.board-table {
  border-collapse: collapse;
}
```

## 20.4 `width`, `height` 속성 대신 CSS 사용

원본 코드:

```html
<th width="200" height="100">첫 번째</th>
```

권장 방식:

```html
<th class="course-name">첫 번째</th>
```

```css
.course-name {
  width: 200px;
  height: 100px;
}
```

테이블의 열 너비는 같은 열의 모든 셀과 표 전체 너비의 영향을 받습니다. 한 셀에 값을 지정했다고 해서 반드시 그 셀만 독립적으로 해당 크기가 되는 것은 아닙니다.

## 20.5 `hidden`을 적용한 `caption`

내 코드에는 다음 내용이 있습니다.

```html
<caption hidden>테이블 내용에 대한 설명을 함</caption>
```

`hidden`은 요소를 렌더링과 접근성 트리에서 제외할 수 있습니다. 표 설명을 보조 기술에 전달하려는 목적이라면 `hidden` 대신 시각적 숨김 클래스를 검토합니다.

```html
<caption class="sr-only">게시판 제목과 작성자 목록</caption>
```

## 20.6 `td` 밖의 콘텐츠에 대한 설명 보완

원본 주석에는 “`td`가 아닌 곳에 넣으면 테이블 밖으로 빠져나간다”는 설명이 있습니다. 브라우저의 HTML 파싱 과정에서 잘못된 콘텐츠가 표 밖으로 이동하거나 예상하지 못한 위치에 재배치될 수 있으므로, 결과에 의존해서는 안 됩니다.

핵심 규칙은 다음과 같습니다.

```text
tr의 직접 자식은 th 또는 td로 구성한다.
```

브라우저별 보정 결과를 외우기보다 유효한 구조를 작성하는 것이 중요합니다.

# 21. 내 코드와 강사님 코드 비교

두 원본은 기본 Table, Header Cell, 행·열 병합, `caption`, `thead`, `tbody`, 크기 속성을 같은 순서로 실습한다. 내 코드는 설명과 게시판 Table 예제가 더 많고, 강사님 코드는 짧은 기본 예제 중심이다.

## 21.1 기본 문서 구조

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

본문이 한국어이므로 다음처럼 맞추는 편이 적절하다.

```html
<html lang="ko">
```

Page 제목도 목적을 드러내게 작성한다.

```html
<title>HTML 테이블 실습</title>
```

## 21.2 복원 메모

내 코드에는 다음 개인 작업 기록이 있다.

```html
<!-- 0723_HTML_table(tr/th/td)_restore -->
```

학습 개념과 직접 관련이 없다면 Git Commit이나 별도 작업 기록으로 분리하는 편이 문서 집중도를 높인다.

## 21.3 `td`와 `th` 설명

내 코드는 `td`를 “한 칸”, `th`를 “컬럼 또는 열의 제목”이라고 설명한다.

```text
td
→ 일반 데이터 셀

th
→ 행 또는 열의 제목 셀
```

`th`는 열 제목뿐 아니라 행 제목에도 사용할 수 있다.

```html
<tr>
    <th scope="row">
        이름
    </th>
    <td>홍길동</td>
</tr>
```

기본 굵기와 가운데 정렬은 Browser 기본 Style일 뿐 핵심 의미가 아니다.

## 21.4 행별 셀 개수 차이

두 코드 모두 두 번째 Table의 두 번째 행에 Cell을 하나 더 추가한다.

```html
<tr>
    <td>내용2-1</td>
    <td>내용2-2</td>
    <td>내용2-3</td>
    <td>내용2-4</td>
</tr>
```

첫 번째 행에는 세 Cell만 있다.

```html
<tr>
    <th>내용1</th>
    <th>내용2</th>
    <th>내용3</th>
</tr>
```

Browser가 Table을 완전히 깨뜨리는 것은 아니지만, 행별 Column 관계가 달라져 Data 의미와 정렬이 모호해진다.

```text
중요한 기준
→ 각 행의 Cell 수가 무조건 같아야 한다

정확한 기준
→ colspan·rowspan까지 고려했을 때
  논리적인 Column Grid가 일관되어야 한다
```

## 21.5 지역·이름 예제 Content 차이

### 내 코드

```html
<tr>
    <th>지역</th>
    <td>천안</td>
    <td>평택</td>
</tr>

<tr>
    <th>이름</th>
    <td>홍길동</td>
    <td>김길동</td>
</tr>
```

### 강사님 코드

```html
<tr>
    <th>지역</th>
    <td>천안</td>
    <td>통영</td>
</tr>

<tr>
    <th>이름</th>
    <td>민수</td>
    <td>개똥</td>
</tr>
```

Content만 다르고 구조는 같다. 첫 번째 Cell이 행 제목이라면 `scope="row"`를 추가하는 편이 관계를 더 명확히 전달한다.

```html
<th scope="row">지역</th>
```

## 21.6 셀 병합 설명

내 코드는 병합을 다음처럼 설명한다.

```html
<!-- col(컬럼)span(간격) 컬럼의 간격
     row(행)span(간격) 열의 간격 -->
```

`span`은 간격이 아니라 **몇 개의 Cell 영역을 차지하는지**를 나타낸다.

```text
colspan="2"
→ 가로 방향 두 Column 차지

rowspan="2"
→ 세로 방향 두 Row 차지
```

원본처럼 모든 Cell을 먼저 작성한 뒤 병합되는 Cell을 제거하는 방식은 Grid를 확인하기 쉬운 학습 방법이다.

## 21.7 `caption`

### 내 코드

```html
<caption hidden>
    테이블 내용에 대한 설명을 함
</caption>
```

### 강사님 코드

```html
<caption>
    테이블 내용에 대한 설명
</caption>
```

`caption`은 Table의 제목 또는 설명을 제공한다. 내 코드처럼 `hidden`을 사용하면 시각적으로도 숨겨지고 일반적으로 접근성 Tree에서도 제외될 수 있어 제목 제공 목적이 사라질 수 있다.

보이게 제공하는 기본 예:

```html
<caption>
    게시글 목록
</caption>
```

시각적으로만 숨기고 Screen Reader에는 제공하려면 `hidden`이 아니라 Visually Hidden CSS Pattern을 사용한다.

## 21.8 잘못된 `<summary>`

두 코드 모두 `table` 안에 `summary`를 작성한다.

```html
<summary>
    제목, 작성자
</summary>
```

`summary`는 `details`의 Summary를 나타내는 Element이며 `table`의 직접 자식으로 사용하는 설명 요소가 아니다.

올바른 사용:

```html
<details>
    <summary>
        자세히 보기
    </summary>

    <p>추가 내용</p>
</details>
```

Table 설명은 `caption`, 주변 Heading, 본문 Text, 필요 시 ARIA 연결을 사용한다.

## 21.9 `thead`와 `tbody`

두 코드 모두 다음 구조를 사용한다.

```html
<table>
    <thead>
        <tr>
            <th>제목</th>
            <th>작성자</th>
        </tr>
    </thead>

    <tbody>
        <tr>
            <td>제목1</td>
            <td>작성자1</td>
        </tr>
    </tbody>
</table>
```

`thead`와 `tbody`는 화면에 별도의 선을 자동으로 만드는 요소가 아니라 Table Row Group의 의미 구조를 제공한다.

내 코드 주석의 “세로일 경우는 묶지 못함”보다는 다음처럼 설명하는 편이 정확하다.

```text
thead
→ Column Header 중심의 Row Group

tbody
→ 주요 Data Row Group

tfoot
→ 합계·요약 Row Group
```

행 제목은 `tbody` 안에서도 `th scope="row"`로 작성할 수 있다.

## 21.10 `border` Attribute

두 코드 모두 다음 방식을 사용한다.

```html
<table border="1">
```

학습 중 Cell 경계를 빠르게 보는 데는 편하지만 실제 Style은 CSS로 분리한다.

```html
<table class="data-table">
```

```css
.data-table {
    border-collapse: collapse;
}

.data-table th,
.data-table td {
    border: 1px solid #cccccc;
}
```

## 21.11 `width`와 `height` Attribute

두 코드 모두 Cell에 크기 속성을 작성한다.

```html
<th
    width="200"
    height="100"
>
    첫번째
</th>
```

```html
<td
    width="250"
    height="50"
>
    두번째
</td>
```

`width`, `height` 같은 Presentational Attribute보다 CSS를 사용한다.

```css
.data-table__label {
    width: 12.5rem;
    min-height: 6.25rem;
}
```

Table의 실제 Column Width는 Cell Content, Table Layout Algorithm, 병합, CSS Width의 영향을 함께 받으므로 한 Cell의 값만으로 독립적으로 결정되지 않을 수 있다.

## 21.12 내 코드의 게시판 Table

내 코드에는 강사님 코드에 없는 게시판 목록 예제가 추가되어 있다.

```html
<table border="1">
    <thead>
        <tr>
            <th width="30"></td>
            <th width="250">제목</th>
            <th width="50">작성자</th>
            <th width="150">작성일</th>
            <th width="50">조회</th>
        </tr>
    </thead>
</table>
```

첫 번째 Header Cell은 다음처럼 잘못 닫혀 있다.

```html
<th width="30"></td>
```

올바른 구조:

```html
<th scope="col">
    번호
</th>
```

빈 Header를 남기기보다 Column 목적을 명확한 Text로 제공한다.

## 21.13 게시판 Data의 반복값

내 코드 게시판 예제는 번호 `23`과 같은 제목을 여러 행에 반복한다.

학습 구조에는 문제가 없지만 실제 Data 관계를 확인하려면 각 행이 구분되는 값이 더 적절하다.

```html
<tr>
    <td>23</td>
    <td>UI 구현 사전평가</td>
    <td>이름1</td>
    <td>2026-06-23</td>
    <td>1</td>
</tr>
```

날짜는 의미를 명확히 하기 위해 `time` Element도 사용할 수 있다.

```html
<time datetime="2026-06-23">
    2026.06.23.
</time>
```

## 21.14 원본 비교 요약

| 항목 | 내 코드 | 강사님 코드 | 개선 기준 |
| --- | --- | --- | --- |
| 복원 메모 | 있음 | 없음 | 작업 기록과 학습 내용 분리 |
| `td` 설명 | 상세 | 간단 | 일반 Data Cell로 설명 |
| `th` 설명 | 열 제목 중심 | 열 제목 중심 | 행·열 제목 모두 가능 |
| 행별 Cell | 3개와 4개 혼합 | 3개와 4개 혼합 | 논리적 Column Grid 유지 |
| 지역·이름 Data | 천안·평택·홍길동·김길동 | 천안·통영·민수·개똥 | 구조 차이 없음 |
| `caption` | `hidden` | 표시 | Table 제목은 접근 가능하게 제공 |
| `summary` | `hidden` 사용 | 표시 | `table` 직접 자식으로 사용 불가 |
| `border` | 사용 | 사용 | CSS로 분리 |
| `width`·`height` | 사용 | 사용 | CSS로 분리 |
| 게시판 예제 | 있음 | 없음 | `th` 닫는 Tag 오류 수정 |
| `lang` | `en` | `en` | 한국어 문서는 `ko` |

# 22. 대표 실무 예제: 게시판 목록

```html
<section aria-labelledby="notice-title">
  <h2 id="notice-title">공지사항</h2>

  <div class="table-scroll">
    <table class="board-table">
      <caption class="sr-only">공지사항 게시글 번호, 제목, 작성자, 작성일, 조회 수</caption>
      <thead>
        <tr>
          <th scope="col">번호</th>
          <th scope="col">제목</th>
          <th scope="col">작성자</th>
          <th scope="col">작성일</th>
          <th scope="col">조회</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>3</td>
          <td><a href="notice-3.html">교육 일정 변경 안내</a></td>
          <td>관리자</td>
          <td><time datetime="2026-07-28">2026.07.28.</time></td>
          <td>42</td>
        </tr>
        <tr>
          <td>2</td>
          <td><a href="notice-2.html">프로젝트 제출 방법</a></td>
          <td>관리자</td>
          <td><time datetime="2026-07-25">2026.07.25.</time></td>
          <td>31</td>
        </tr>
      </tbody>
    </table>
  </div>
</section>
```

```css
.table-scroll {
  overflow-x: auto;
}

.board-table {
  width: 100%;
  min-width: 720px;
  border-collapse: collapse;
}

.board-table th,
.board-table td {
  padding: 12px 16px;
  border: 1px solid #ddd;
  text-align: center;
}

.board-table th {
  background: #f5f5f5;
}

.board-table td:nth-child(2) {
  text-align: left;
}
```

# 23. 반응형 테이블

테이블은 열이 많으면 모바일 화면보다 넓어질 수 있습니다. 구조를 무리하게 변경하기보다 가로 스크롤 영역을 제공하는 방법이 자주 사용됩니다.

```html
<div class="table-scroll" tabindex="0" aria-label="표를 가로로 스크롤할 수 있습니다.">
  <table>
    <!-- 표 내용 -->
  </table>
</div>
```

```css
.table-scroll {
  max-width: 100%;
  overflow-x: auto;
}
```

## 23.1 무조건 셀을 블록으로 바꾸지 않는다

다음과 같이 모든 테이블 요소를 `display: block`으로 변경하면 행과 열의 의미가 약해지고 표 구조가 깨질 수 있습니다.

```css
/* 신중하게 사용해야 하는 방식 */
table,
thead,
tbody,
tr,
th,
td {
  display: block;
}
```

모바일 카드 형태가 더 적합한 데이터라면 HTML 구조 자체를 목록이나 카드로 별도 제공하는 방법도 검토합니다.

# 24. 테이블 CSS 기초

## 24.1 테두리 합치기

```css
table {
  border-collapse: collapse;
}
```

`border-collapse: collapse`는 인접한 셀의 테두리를 하나처럼 합칩니다.

## 24.2 셀 여백

```css
th,
td {
  padding: 12px;
}
```

## 24.3 텍스트 정렬

```css
th {
  text-align: center;
}

td {
  text-align: left;
  vertical-align: middle;
}
```

`vertical-align`은 테이블 셀 내부의 세로 정렬에 사용할 수 있습니다.

## 24.4 줄무늬 행

```css
tbody tr:nth-child(even) {
  background: #f8f8f8;
}
```

## 24.5 마우스 오버

```css
tbody tr:hover {
  background: #f0f4ff;
}
```

마우스 오버만으로 중요한 정보를 전달하지 않아야 하며, 키보드 사용자가 조작해야 하는 요소에는 별도의 포커스 스타일을 제공합니다.

# 25. `colgroup`과 `col`

여러 열에 공통 스타일이나 의미를 적용할 때 `colgroup`과 `col`을 사용할 수 있습니다.

```html
<table>
  <caption>과정별 학습 시간</caption>
  <colgroup>
    <col class="course-column">
    <col span="2" class="time-column">
  </colgroup>
  <thead>
    <tr>
      <th scope="col">과정</th>
      <th scope="col">이론</th>
      <th scope="col">실습</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>HTML</td>
      <td>4시간</td>
      <td>8시간</td>
    </tr>
  </tbody>
</table>
```

```css
.course-column {
  width: 40%;
}

.time-column {
  width: 30%;
}
```

`col`은 셀 내부 콘텐츠를 직접 감싸는 요소가 아니며, 적용 가능한 CSS 속성에도 제한이 있습니다.

# 26. 접근성 체크

## 26.1 표 제목 제공

```html
<caption>2026년 월별 수강 신청 인원</caption>
```

## 26.2 제목 셀 구분

```html
<th scope="col">1월</th>
<th scope="row">웹 개발</th>
```

## 26.3 빈 셀의 의미 확인

단순히 디자인을 맞추기 위해 빈 `th`를 만들면 보조 기술 사용자가 열의 의미를 알기 어렵습니다.

```html
<!-- 의미가 불명확한 예 -->
<th></th>
```

```html
<!-- 의미를 제공한 예 -->
<th scope="col">선택</th>
```

화면에서만 숨기려면 시각적 숨김 텍스트를 사용할 수 있습니다.

```html
<th scope="col"><span class="sr-only">게시글 선택</span></th>
```

## 26.4 색상만으로 상태를 구분하지 않는다

```html
<td><span class="status status--complete">완료</span></td>
```

배경색뿐 아니라 “완료” 같은 텍스트도 함께 제공합니다.

## 26.5 복잡한 표는 단순화한다

`rowspan`, `colspan`이 지나치게 많은 표는 시각적으로도 해석하기 어렵고 접근성 관계도 복잡해집니다. 가능하면 표를 여러 개로 나누거나 데이터 구조를 단순화합니다.

# 27. 자주 하는 실수

## 27.1 레이아웃을 테이블로 만든다

```html
<!-- 잘못된 접근 -->
<table>
  <tr>
    <td>사이드바</td>
    <td>본문</td>
  </tr>
</table>
```

레이아웃은 CSS Grid 또는 Flexbox를 사용합니다.

## 27.2 `tr` 밖에 `td`를 작성한다

```html
<!-- 잘못된 구조 -->
<table>
  <td>데이터</td>
</table>
```

```html
<!-- 올바른 구조 -->
<table>
  <tr>
    <td>데이터</td>
  </tr>
</table>
```

## 27.3 제목 셀을 모두 `td`로 작성한다

```html
<tr>
  <td>이름</td>
  <td>지역</td>
</tr>
```

```html
<tr>
  <th scope="col">이름</th>
  <th scope="col">지역</th>
</tr>
```

## 27.4 병합한 셀을 제거하지 않는다

```html
<!-- colspan으로 두 열을 차지하면서 기존 셀도 남아 있음 -->
<tr>
  <td colspan="2">병합</td>
  <td>불필요한 셀</td>
</tr>
```

표 전체 열 수를 계산하여 병합 범위의 셀을 제거합니다.

## 27.5 `colspan="0"`이나 잘못된 값을 사용한다

`colspan`, `rowspan`에는 의도한 범위에 맞는 유효한 양의 정수를 작성합니다.

```html
<td colspan="2">두 열 병합</td>
```

## 27.6 `summary`를 표 설명으로 사용한다

`summary`는 `details`의 자식으로 사용하는 요소입니다. 표 제목은 `caption`을 사용합니다.

## 27.7 HTML 속성만으로 디자인을 완성한다

`border`, `cellpadding`, `cellspacing`, `bgcolor`, `width`, `height` 같은 오래된 표현 방식에 의존하지 않고 CSS로 분리합니다.

# 28. 실무 개선 원칙

## 28.1 먼저 데이터 관계를 설계한다

코드를 작성하기 전에 다음을 정리합니다.

- 한 행이 무엇을 의미하는가?
- 한 열이 무엇을 의미하는가?
- 열 제목과 행 제목은 무엇인가?
- 합계나 요약 행이 필요한가?
- 병합이 꼭 필요한가?

## 28.2 시각적 모양보다 의미를 먼저 작성한다

1. 올바른 `table` 구조 작성
2. `caption`, `th`, `scope` 추가
3. 데이터 검수
4. CSS 적용
5. 반응형 동작 확인

## 28.3 복잡한 병합을 최소화한다

병합이 많을수록 유지보수와 접근성이 어려워집니다. 같은 정보를 더 단순한 표 두 개로 나눌 수 있는지 검토합니다.

## 28.4 동적 데이터에서도 구조를 유지한다

React나 서버 템플릿으로 행을 반복 생성하더라도 다음 구조는 유지합니다.

```html
<tbody>
  <tr>
    <td>...</td>
  </tr>
</tbody>
```

각 행에는 안정적인 식별자를 사용하고, 데이터가 없을 때는 열 전체를 차지하는 안내 행을 제공할 수 있습니다.

```html
<tr>
  <td colspan="5">등록된 게시글이 없습니다.</td>
</tr>
```

## 28.5 정렬 가능한 열은 상태를 전달한다

JavaScript로 정렬 기능을 추가한다면 현재 정렬 상태를 `aria-sort`로 전달할 수 있습니다.

```html
<th scope="col" aria-sort="ascending">
  <button type="button">작성일</button>
</th>
```


# 29. 종합실습

## Level 1

### 문제 1

다음 데이터를 2행 3열 테이블로 작성하세요.

- 첫 번째 행: 이름, 지역, 직무
- 두 번째 행: 홍길동, 천안, 개발자

### 문제 2

다음 코드의 구조적 오류를 수정하세요.

```html
<table>
  <td>HTML</td>
  <td>CSS</td>
</table>
```

### 문제 3

다음 첫 번째 행의 셀을 적절한 제목 셀로 수정하고 `scope`를 추가하세요.

```html
<tr>
  <td>상품명</td>
  <td>가격</td>
</tr>
```

### 문제 4

표의 제목으로 “2026년 과정별 신청 현황”을 추가하세요.

## Level 2

### 문제 5

다음 3열 표에서 첫 번째 행의 두 번째 셀과 세 번째 셀을 병합하세요.

```html
<tr>
  <td>1-1</td>
  <td>1-2</td>
  <td>1-3</td>
</tr>
```

### 문제 6

다음 표에서 첫 번째 열의 두 행을 병합하세요.

```html
<table>
  <tr>
    <td>연락처</td>
    <td>전화번호</td>
  </tr>
  <tr>
    <td>연락처</td>
    <td>이메일</td>
  </tr>
</table>
```

### 문제 7

다음 코드에서 현재 HTML 구조상 부적절한 요소를 찾아 수정하세요.

```html
<table>
  <caption>회원 목록</caption>
  <summary>이름, 이메일</summary>
  <tr>
    <th>이름</th>
    <th>이메일</th>
  </tr>
</table>
```

## Level 3

### 문제 8

`caption`, `thead`, `tbody`, `tfoot`을 모두 사용해 상품명, 수량, 금액과 합계를 표현하는 주문 내역 표를 작성하세요.

### 문제 9

다음 실습 코드를 실무 권장 방식으로 변경하세요.

```html
<table border="1" width="600">
  <tr>
    <th width="300">과정</th>
    <th width="300">시간</th>
  </tr>
</table>
```

조건:

- HTML 표현 속성을 제거한다.
- 클래스를 추가한다.
- CSS로 테두리와 너비를 적용한다.

## Challenge

### 문제 10

다음 조건을 만족하는 게시판 목록을 작성하세요.

- 표 제목 제공
- 번호, 제목, 작성자, 작성일, 조회 수 열
- `thead`, `tbody` 사용
- 각 열 제목에 `scope` 사용
- 제목에 상세 페이지 링크 사용
- 날짜에 `time` 요소 사용
- 데이터가 없을 때 사용할 안내 행도 별도로 작성
- 모바일에서 가로 스크롤 가능하도록 CSS 작성

# 30. 정답과 해설

## 문제 1 정답

```html
<table>
  <tr>
    <th scope="col">이름</th>
    <th scope="col">지역</th>
    <th scope="col">직무</th>
  </tr>
  <tr>
    <td>홍길동</td>
    <td>천안</td>
    <td>개발자</td>
  </tr>
</table>
```

## 문제 2 정답

```html
<table>
  <tr>
    <td>HTML</td>
    <td>CSS</td>
  </tr>
</table>
```

`td`는 `tr` 안에 작성합니다.

## 문제 3 정답

```html
<tr>
  <th scope="col">상품명</th>
  <th scope="col">가격</th>
</tr>
```

두 셀은 각 열의 제목이므로 `th`가 적절합니다.

## 문제 4 정답

```html
<table>
  <caption>2026년 과정별 신청 현황</caption>
  <!-- 표 내용 -->
</table>
```

## 문제 5 정답

```html
<tr>
  <td>1-1</td>
  <td colspan="2">1-2와 1-3</td>
</tr>
```

병합되는 세 번째 셀은 제거합니다.

## 문제 6 정답

```html
<table>
  <tr>
    <th rowspan="2" scope="rowgroup">연락처</th>
    <td>전화번호</td>
  </tr>
  <tr>
    <td>이메일</td>
  </tr>
</table>
```

첫 번째 셀이 두 행을 차지하므로 두 번째 행의 중복 셀을 제거합니다.

## 문제 7 정답

```html
<table>
  <caption>회원 목록</caption>
  <thead>
    <tr>
      <th scope="col">이름</th>
      <th scope="col">이메일</th>
    </tr>
  </thead>
</table>
```

`summary`는 `table`의 설명 요소가 아니므로 제거합니다. 추가 설명이 필요하면 주변 문단을 사용할 수 있습니다.

## 문제 8 예시 정답

```html
<table>
  <caption>상품 주문 내역</caption>
  <thead>
    <tr>
      <th scope="col">상품명</th>
      <th scope="col">수량</th>
      <th scope="col">금액</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>키보드</td>
      <td>1개</td>
      <td>80,000원</td>
    </tr>
    <tr>
      <td>마우스</td>
      <td>2개</td>
      <td>60,000원</td>
    </tr>
  </tbody>
  <tfoot>
    <tr>
      <th scope="row" colspan="2">합계</th>
      <td>140,000원</td>
    </tr>
  </tfoot>
</table>
```

## 문제 9 정답

```html
<table class="course-table">
  <tr>
    <th scope="col">과정</th>
    <th scope="col">시간</th>
  </tr>
</table>
```

```css
.course-table {
  width: 600px;
  border-collapse: collapse;
}

.course-table th,
.course-table td {
  width: 50%;
  border: 1px solid #333;
}
```

실제 반응형 화면에서는 고정 너비 대신 `width: 100%`와 `max-width`를 함께 사용하는 방법도 검토합니다.

## 문제 10 예시 정답

```html
<section aria-labelledby="board-title">
  <h2 id="board-title">게시판</h2>

  <div class="table-scroll" tabindex="0" aria-label="게시판 표를 가로로 스크롤할 수 있습니다.">
    <table class="board-table">
      <caption class="sr-only">게시글 번호, 제목, 작성자, 작성일, 조회 수</caption>
      <thead>
        <tr>
          <th scope="col">번호</th>
          <th scope="col">제목</th>
          <th scope="col">작성자</th>
          <th scope="col">작성일</th>
          <th scope="col">조회</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>1</td>
          <td><a href="post-1.html">첫 번째 게시글</a></td>
          <td>관리자</td>
          <td><time datetime="2026-07-28">2026.07.28.</time></td>
          <td>10</td>
        </tr>
      </tbody>
    </table>
  </div>
</section>
```

데이터가 없을 때의 행:

```html
<tr>
  <td colspan="5">등록된 게시글이 없습니다.</td>
</tr>
```

```css
.table-scroll {
  max-width: 100%;
  overflow-x: auto;
}

.board-table {
  width: 100%;
  min-width: 720px;
  border-collapse: collapse;
}

.board-table th,
.board-table td {
  padding: 12px;
  border: 1px solid #ddd;
}
```

# 31. 최종 체크리스트

- [ ] 표 형식 데이터에만 `table`을 사용했는가?
- [ ] 모든 데이터 셀이 `tr` 안에 있는가?
- [ ] 제목 셀에 `th`를 사용했는가?
- [ ] 필요한 `th`에 `scope`를 지정했는가?
- [ ] 표의 제목이나 목적을 `caption`으로 제공했는가?
- [ ] `thead`, `tbody`, `tfoot`을 의미에 맞게 구분했는가?
- [ ] `colspan`, `rowspan` 적용 후 논리적인 열 수가 맞는가?
- [ ] 병합 범위의 중복 셀을 제거했는가?
- [ ] `summary`를 `table` 내부에 잘못 사용하지 않았는가?
- [ ] 시작 태그와 닫는 태그가 일치하는가?
- [ ] `border`, `width`, `height` 같은 표현을 CSS로 분리했는가?
- [ ] 모바일에서 표가 잘리지 않도록 처리했는가?
- [ ] 빈 제목 셀에 의미 있는 설명을 제공했는가?

# 32. 핵심 요약

- `table`은 행과 열의 관계를 가진 데이터를 표현합니다.
- `tr`은 행, `th`는 제목 셀, `td`는 데이터 셀입니다.
- `caption`은 표 전체의 제목을 제공합니다.
- `thead`, `tbody`, `tfoot`은 표의 제목·본문·요약 영역을 구분합니다.
- `colspan`은 열을, `rowspan`은 행을 병합합니다.
- 셀 병합 후에는 모든 행의 논리적인 열 개수를 확인해야 합니다.
- `scope="col"`과 `scope="row"`는 제목과 데이터의 관계를 명확하게 합니다.
- `summary`는 표 요소가 아니라 `details`의 요약 요소입니다.
- 실습용 `border`, `width`, `height` 속성은 실무에서 CSS로 대체합니다.
- 테이블은 페이지 레이아웃이 아니라 데이터 표현에 사용합니다.
