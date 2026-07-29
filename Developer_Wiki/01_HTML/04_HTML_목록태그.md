# HTML 목록 태그

## 문서 정보

| 항목 | 내용 |
| --- | --- |
| 문서 | `04_HTML_목록태그.md` |
| 권장 선수 학습 | `03_HTML_링크와_경로.md` |
| 다음 학습 | `05_HTML_테이블.md` |
| 학습 범위 | `ul`, `ol`, `li`, `dl`, `dt`, `dd`, 중첩 목록, 목록과 내비게이션 |
| 프로젝트 연결 | 내비게이션, 메뉴, 카테고리, 순위, 작업 절차, FAQ 용어 설명 |

> HTML 목록은 단순히 앞에 점이나 숫자를 붙이는 기능이 아닙니다. 서로 관련된 항목의 관계와 순서를 문서 구조로 표현하며, 내비게이션과 메뉴처럼 실제 웹사이트에서 매우 자주 사용됩니다.

# 학습 목표

- 순서 없는 목록과 순서 있는 목록의 차이를 설명한다.
- `ul`, `ol`의 직접적인 자식으로 `li`를 작성한다.
- 목록 항목 안에 링크, 이미지, 문단 등 다양한 콘텐츠를 배치한다.
- 하위 목록을 올바르게 중첩한다.
- `ol`의 `start`, `reversed`, `value`, `type` 속성을 활용한다.
- `dl`, `dt`, `dd`로 용어와 설명의 관계를 표현한다.
- 목록의 시각적 모양과 문서 의미를 구분한다.
- 메뉴를 단순한 `div` 묶음이 아닌 의미 있는 목록으로 구성한다.
- 내 코드와 강사님 코드의 차이를 분석하고 개선한다.

# 1. 목록이 필요한 이유

서로 관련된 여러 항목을 나열할 때 목록 요소를 사용합니다.

```html
<ul>
  <li>HTML</li>
  <li>CSS</li>
  <li>JavaScript</li>
</ul>
```

브라우저는 기본 스타일로 들여쓰기와 불릿을 표시하지만, 목록 요소를 사용하는 핵심 이유는 모양이 아니라 **항목 사이의 관계를 구조로 표현하기 위해서**입니다.

| 표현하려는 내용 | 권장 요소 |
| --- | --- |
| 순서가 중요하지 않은 항목 | `ul` |
| 단계, 순위처럼 순서가 중요한 항목 | `ol` |
| 용어와 설명의 조합 | `dl`, `dt`, `dd` |

# 2. 순서 없는 목록 `ul`

`ul`은 Unordered List의 약자로, 순서 자체가 의미에 영향을 주지 않는 항목에 사용합니다.

```html
<ul>
  <li>공지사항</li>
  <li>자주 묻는 질문</li>
  <li>문의하기</li>
</ul>
```

항목의 위치를 서로 바꾸어도 내용의 의미가 크게 달라지지 않는다면 `ul`이 적합합니다.

## 2.1 대표 사용 사례

- 웹사이트 주 메뉴
- 상품 카테고리
- 기능 목록
- 준비물 목록
- 관련 문서 모음
- 태그나 키워드 모음

```html
<nav aria-label="주요 메뉴">
  <ul>
    <li><a href="index.html">홈</a></li>
    <li><a href="courses.html">교육 과정</a></li>
    <li><a href="projects.html">프로젝트</a></li>
  </ul>
</nav>
```

`nav`는 탐색 영역의 의미를 나타내고, `ul`은 여러 링크가 하나의 메뉴 집합이라는 관계를 표현합니다.

# 3. 목록 항목 `li`

`li`는 List Item의 약자로, `ul` 또는 `ol` 안의 각 항목을 나타냅니다.

```html
<ul>
  <li>아이템 1</li>
  <li>아이템 2</li>
  <li>아이템 3</li>
</ul>
```

## 3.1 `ul`과 `ol`의 직접 자식

`ul`과 `ol`의 직접 자식은 일반적으로 `li`여야 합니다.

```html
<!-- 올바른 구조 -->
<ul>
  <li>HTML</li>
  <li>CSS</li>
</ul>
```

```html
<!-- 피해야 할 구조 -->
<ul>
  <p>HTML</p>
  <a href="css.html">CSS</a>
</ul>
```

필요한 콘텐츠는 `li` 안에 배치합니다.

```html
<ul>
  <li><p>HTML 기초 과정</p></li>
  <li><a href="css.html">CSS 과정 보기</a></li>
</ul>
```

## 3.2 `li` 안에는 다양한 콘텐츠를 넣을 수 있다

```html
<ul>
  <li>
    <h2>HTML 과정</h2>
    <p>문서 구조와 시맨틱 태그를 학습합니다.</p>
    <a href="html-course.html">과정 자세히 보기</a>
  </li>
  <li>
    <h2>CSS 과정</h2>
    <p>레이아웃과 반응형 디자인을 학습합니다.</p>
    <a href="css-course.html">과정 자세히 보기</a>
  </li>
</ul>
```

목록의 각 항목이 카드처럼 여러 내용을 포함해야 할 때도 `li`를 유지할 수 있습니다.

# 4. 순서 있는 목록 `ol`

`ol`은 Ordered List의 약자로, 항목의 순서가 의미를 가질 때 사용합니다.

```html
<ol>
  <li>프로젝트 요구사항 확인</li>
  <li>화면 구조 설계</li>
  <li>HTML 마크업 작성</li>
  <li>CSS 스타일 적용</li>
</ol>
```

## 4.1 대표 사용 사례

- 작업 절차
- 설치 순서
- 레시피 단계
- 순위
- 목차
- 시간 순서가 있는 기록

`ol`이 화면에 숫자를 표시한다는 이유만으로 사용하는 것이 아니라, **순서를 바꾸었을 때 의미가 달라지는가**를 기준으로 선택합니다.

| 질문 | 선택 |
| --- | --- |
| 항목 순서를 바꾸어도 의미가 같은가? | `ul` |
| 순서를 바꾸면 절차나 결과가 달라지는가? | `ol` |

# 5. `ol`의 주요 속성

## 5.1 시작 번호 `start`

```html
<ol start="4">
  <li>CSS 선택자</li>
  <li>박스 모델</li>
  <li>레이아웃</li>
</ol>
```

목록은 4부터 시작합니다. 페이지가 나뉜 연속 순위나 이어지는 절차에서 사용할 수 있습니다.

## 5.2 역순 `reversed`

```html
<ol reversed>
  <li>금메달</li>
  <li>은메달</li>
  <li>동메달</li>
</ol>
```

`reversed`는 불리언 속성이므로 속성명만 작성할 수 있습니다.

## 5.3 특정 항목 번호 `value`

```html
<ol>
  <li>첫 번째 단계</li>
  <li value="5">다섯 번째 단계부터 다시 시작</li>
  <li>여섯 번째 단계</li>
</ol>
```

`value`는 `ol` 안의 특정 `li` 번호를 변경합니다. 이후 항목의 번호도 이어서 계산됩니다.

## 5.4 번호 형태 `type`

```html
<ol type="A">
  <li>HTML</li>
  <li>CSS</li>
</ol>
```

| 값 | 표시 예시 |
| --- | --- |
| `1` | 1, 2, 3 |
| `A` | A, B, C |
| `a` | a, b, c |
| `I` | I, II, III |
| `i` | i, ii, iii |

시각적 표현만 바꾸는 목적이라면 CSS의 `list-style-type`을 고려할 수 있습니다. `type` 속성은 번호 형식 자체가 콘텐츠 의미와 연결될 때 사용할 수 있습니다.

# 6. 중첩 목록

상위 항목 아래에 하위 항목이 있을 때 목록을 중첩합니다.

```html
<ul>
  <li>프론트엔드
    <ul>
      <li>HTML</li>
      <li>CSS</li>
      <li>JavaScript</li>
    </ul>
  </li>
  <li>백엔드
    <ul>
      <li>Java</li>
      <li>Spring Boot</li>
    </ul>
  </li>
</ul>
```

## 6.1 하위 목록은 해당 `li` 안에 넣는다

```html
<!-- 권장 구조 -->
<ul>
  <li>리스트 1</li>
  <li>리스트 2
    <ul>
      <li>리스트 2-1</li>
      <li>리스트 2-2</li>
    </ul>
  </li>
</ul>
```

다음처럼 상위 `li`를 닫은 뒤 하위 `ul`을 형제처럼 배치하면 목록 간의 관계가 올바르게 표현되지 않습니다.

```html
<!-- 잘못된 구조 -->
<ul>
  <li>리스트 2</li>
  <ul>
    <li>리스트 2-1</li>
  </ul>
</ul>
```

## 6.2 텍스트도 함께 작성한다

강사님 원본 예제에는 하위 목록을 포함한 `li`에 상위 항목 텍스트가 없는 형태가 있습니다.

```html
<ul>
  <li>리스트1</li>
  <li>
    <ul>
      <li>리스트2-1</li>
      <li>리스트2-2</li>
    </ul>
  </li>
</ul>
```

문법상 중첩 위치는 맞지만, 실제 콘텐츠에서는 상위 그룹 이름을 작성하는 편이 구조를 이해하기 쉽습니다.

```html
<ul>
  <li>리스트1</li>
  <li>리스트2
    <ul>
      <li>리스트2-1</li>
      <li>리스트2-2</li>
    </ul>
  </li>
</ul>
```

# 7. 설명 목록 `dl`, `dt`, `dd`

`dl`은 Description List, `dt`는 Description Term, `dd`는 Description Details를 의미합니다.

```html
<dl>
  <dt>HTML</dt>
  <dd>웹 문서의 구조와 의미를 작성하는 마크업 언어</dd>

  <dt>CSS</dt>
  <dd>웹 문서의 시각적 표현을 담당하는 스타일 언어</dd>
</dl>
```

| 요소 | 역할 |
| --- | --- |
| `dl` | 용어와 설명의 전체 그룹 |
| `dt` | 설명할 용어 또는 이름 |
| `dd` | 해당 용어의 설명이나 값 |

## 7.1 하나의 용어에 여러 설명

```html
<dl>
  <dt>HTML</dt>
  <dd>HyperText Markup Language의 약자</dd>
  <dd>웹페이지 구조를 작성하는 언어</dd>
</dl>
```

## 7.2 여러 용어에 하나의 설명

```html
<dl>
  <dt>Chrome</dt>
  <dt>Firefox</dt>
  <dt>Edge</dt>
  <dd>웹 문서를 해석하고 표시하는 브라우저</dd>
</dl>
```

## 7.3 대표 사용 사례

- 용어 사전
- 상품 사양의 이름과 값
- FAQ의 질문과 답변
- 인물 정보의 항목과 값
- 메타데이터 표현

```html
<dl>
  <div>
    <dt>교육 기간</dt>
    <dd>6개월</dd>
  </div>
  <div>
    <dt>교육 방식</dt>
    <dd>이론과 프로젝트 병행</dd>
  </div>
</dl>
```

`dl` 내부의 여러 용어·설명 그룹을 스타일링하기 위해 `div`로 묶을 수 있습니다.

# 8. `ul`, `ol`, `dl` 비교

| 구분 | `ul` | `ol` | `dl` |
| --- | --- | --- | --- |
| 의미 | 순서 없는 목록 | 순서 있는 목록 | 용어와 설명 목록 |
| 주요 자식 | `li` | `li` | `dt`, `dd`, 필요 시 그룹용 `div` |
| 대표 사례 | 메뉴, 카테고리 | 절차, 순위 | 용어 사전, 사양 정보 |
| 순서 중요성 | 낮음 | 높음 | 용어-설명 관계가 중요 |
| 기본 표시 | 불릿 | 번호 | 브라우저별 들여쓰기 |

# 9. 목록과 링크

목록 항목 안에 링크를 넣는 구조는 내비게이션에서 매우 자주 사용됩니다.

```html
<ul>
  <li><a href="index.html">홈</a></li>
  <li><a href="about.html">소개</a></li>
  <li><a href="contact.html">문의</a></li>
</ul>
```

`a`만 여러 개 나열해도 화면은 만들 수 있지만, 목록을 사용하면 링크들이 하나의 관련된 메뉴 집합이라는 의미가 명확해집니다.

```html
<!-- 의미가 약한 구조 -->
<nav>
  <a href="index.html">홈</a>
  <a href="about.html">소개</a>
  <a href="contact.html">문의</a>
</nav>
```

```html
<!-- 메뉴 항목 관계를 명시한 구조 -->
<nav aria-label="주요 메뉴">
  <ul>
    <li><a href="index.html">홈</a></li>
    <li><a href="about.html">소개</a></li>
    <li><a href="contact.html">문의</a></li>
  </ul>
</nav>
```

두 방식 모두 사용할 수 있지만, 계층이나 항목 집합을 강조해야 하는 메뉴에서는 목록 구조가 유용합니다.

# 10. 목록의 기본 스타일과 CSS

브라우저는 목록에 기본 여백과 마커를 적용합니다.

```css
ul {
  margin: 1em 0;
  padding-left: 40px;
}
```

브라우저별 기본값은 다를 수 있으므로 실제 프로젝트에서는 필요한 스타일을 명시합니다.

## 10.1 마커 제거

```css
.menu {
  margin: 0;
  padding: 0;
  list-style: none;
}
```

```html
<ul class="menu">
  <li><a href="index.html">홈</a></li>
  <li><a href="about.html">소개</a></li>
</ul>
```

마커를 없애도 HTML 구조상 목록이라는 의미는 유지됩니다.

## 10.2 가로 메뉴

내 코드에서는 다음 CSS를 사용했습니다.

```css
#list li {
  display: inline-block;
}
```

학습 단계에서는 가로 배치 원리를 확인할 수 있지만, 실제 메뉴에서는 Flexbox를 사용하면 간격과 정렬을 더 명확하게 관리할 수 있습니다.

```css
.menu {
  display: flex;
  gap: 16px;
  margin: 0;
  padding: 0;
  list-style: none;
}
```

```html
<ul class="menu">
  <li><a href="index.html">홈</a></li>
  <li><a href="courses.html">과정</a></li>
  <li><a href="contact.html">문의</a></li>
</ul>
```

| 방식 | 특징 |
| --- | --- |
| `inline-block` | 간단한 가로 배치 학습에 적합 |
| `flex` | 간격, 정렬, 반응형 배치를 관리하기 쉬움 |

# 11. 목록 마커 꾸미기

## 11.1 `list-style-type`

```css
.skills {
  list-style-type: square;
}
```

```css
.steps {
  list-style-type: upper-roman;
}
```

## 11.2 `list-style-position`

```css
.notice-list {
  list-style-position: inside;
}
```

| 값 | 동작 |
| --- | --- |
| `outside` | 마커를 콘텐츠 영역 바깥쪽에 표시, 기본값 |
| `inside` | 마커를 콘텐츠 흐름 안쪽에 표시 |

## 11.3 `::marker`

```css
.check-list li::marker {
  content: "✓ ";
  font-weight: 700;
}
```

`::marker`를 사용하면 목록 구조는 유지하면서 마커를 꾸밀 수 있습니다. 지원 범위와 적용 가능한 CSS 속성에는 제한이 있을 수 있으므로 실제 환경에서 확인합니다.

# 12. Emmet으로 목록 빠르게 작성하기

원본 코드의 주석처럼 Emmet을 사용하면 반복 구조를 빠르게 생성할 수 있습니다.

```text
ul>li*5
```

확장 결과:

```html
<ul>
  <li></li>
  <li></li>
  <li></li>
  <li></li>
  <li></li>
</ul>
```

텍스트까지 포함할 수 있습니다.

```text
ul>li{메뉴 $}*3
```

```html
<ul>
  <li>메뉴 1</li>
  <li>메뉴 2</li>
  <li>메뉴 3</li>
</ul>
```

Emmet은 HTML 문법이 아니라 편집기의 코드 작성 보조 기능입니다. 확장된 최종 HTML 구조가 올바른지 반드시 확인합니다.

# 13. 접근성과 의미 구조

## 13.1 모양만 보고 목록을 선택하지 않는다

`ul`은 점을 표시하기 위한 요소가 아니고, `ol`은 숫자를 표시하기 위한 요소만도 아닙니다.

```html
<!-- 순서가 중요한 가입 절차 -->
<ol>
  <li>약관 동의</li>
  <li>정보 입력</li>
  <li>이메일 인증</li>
</ol>
```

```html
<!-- 순서가 중요하지 않은 서비스 기능 -->
<ul>
  <li>실시간 알림</li>
  <li>파일 공유</li>
  <li>검색 기능</li>
</ul>
```

CSS로 번호나 불릿을 제거해도 문서의 의미는 변하지 않습니다.

## 13.2 메뉴의 현재 페이지 표시

```html
<nav aria-label="주요 메뉴">
  <ul>
    <li><a href="index.html">홈</a></li>
    <li><a href="courses.html" aria-current="page">교육 과정</a></li>
    <li><a href="contact.html">문의</a></li>
  </ul>
</nav>
```

`aria-current="page"`는 현재 페이지에 해당하는 링크를 보조 기술에 알리는 데 사용할 수 있습니다.

## 13.3 목록을 불필요하게 숨기지 않는다

CSS의 `list-style: none`은 마커만 제거하며 목록 구조는 유지합니다. 다만 특정 브라우저와 보조 기술 조합에서는 스타일 변경에 따른 해석 차이가 있을 수 있으므로, 실제 서비스의 핵심 내비게이션은 의미 있는 `nav`와 명확한 링크 텍스트를 함께 사용합니다.

# 14. 내 코드와 강사님 코드 비교

## 14.1 공통 학습 내용

두 코드 모두 다음 내용을 포함합니다.

- `ul`과 `li`를 이용한 순서 없는 목록
- `ol`과 `li`를 이용한 순서 있는 목록
- 목록 항목 안의 링크
- 중첩 목록
- `dl`, `dt`, `dd`를 이용한 설명 목록
- Emmet의 `ul>li*5` 작성 방식

## 14.2 주요 차이 비교

| 항목 | 내 코드 | 강사님 코드 | 판단 |
| --- | --- | --- | --- |
| 외부 링크 새 탭 | `target="_blank"` 사용 | 현재 탭으로 연결 | 사용 흐름에 따라 선택 |
| 중첩 목록 상위 텍스트 | `리스트2` 작성 | 상위 `li` 텍스트 없음 | 내 코드가 관계를 이해하기 쉬움 |
| 가로 목록 예제 | `inline-block` CSS 추가 | 없음 | CSS 연결 학습에 유용 |
| 목록 설명 주석 | 사용 목적과 접근성 설명 추가 | 핵심 문법 중심 | 내 코드가 복습 정보가 많음 |
| Emmet 결과 | 주석으로 작성 방법만 기록 | 실제 확장 결과 포함 | 강사님 코드가 결과 확인에 유리 |
| 문서 언어 | `lang="en"` | `lang="en"` | 한국어 문서라면 `ko`로 수정 권장 |

## 14.3 내 코드의 장점

내 코드에는 다음과 같은 학습 기록이 추가되어 있습니다.

```html
<!-- ul안에 ul을 추가로 넣고싶다면 li에 넣어야 접근성 위반이 안 됨 -->
```

표현을 조금 다듬으면 다음 원칙을 기억하는 데 도움이 됩니다.

> 하위 목록은 그 하위 항목이 속한 상위 `li` 내부에 작성해야 목록의 계층 관계가 올바르게 표현된다.

또한 상위 항목 텍스트를 작성해 중첩 구조의 의미가 더 명확합니다.

```html
<li>리스트2
  <ul>
    <li>리스트2-1</li>
    <li>리스트2-2</li>
  </ul>
</li>
```

## 14.4 내 코드에서 수정할 부분

### `lang` 속성

문서 본문이 한국어이므로 다음처럼 수정하는 편이 적절합니다.

```html
<html lang="ko">
```

### 외부 링크 프로토콜

원본의 `http://naver.com`보다 `https://`를 사용하는 편이 좋습니다.

```html
<a href="https://www.naver.com" target="_blank" rel="noopener noreferrer">
  네이버
</a>
```

### `id`보다 재사용 가능한 클래스

원본은 가로 목록에 `id="list"`를 사용했습니다.

```html
<ul id="list">
```

같은 스타일의 메뉴를 여러 번 사용할 가능성이 있다면 클래스로 작성하는 편이 재사용하기 쉽습니다.

```html
<ul class="list-inline">
```

```css
.list-inline {
  display: flex;
  gap: 12px;
  list-style: none;
}
```

## 14.5 강사님 코드에서 보완할 부분

강사님 코드의 중첩 예제는 상위 `li`에 제목이 없습니다.

```html
<li>
  <ul>
    <li>리스트2-1</li>
    <li>리스트2-2</li>
  </ul>
</li>
```

문법 구조를 보여 주는 예제로는 가능하지만, 실제 콘텐츠에서는 그룹 이름을 추가하는 편이 명확합니다.

또한 외부 사이트 링크에는 `https://`를 사용하고, 새 탭으로 열어야 한다면 `target`과 `rel`을 함께 검토합니다.

## 14.6 학습 코드와 실무 코드

원본 코드는 각 태그의 기본 동작을 한 파일에서 확인하기 위한 학습 코드입니다. 실제 프로젝트에서는 다음을 함께 고려합니다.

- 목록의 의미에 맞는 `ul`, `ol`, `dl` 선택
- 내비게이션 영역의 `nav`
- 현재 페이지의 `aria-current`
- 재사용 가능한 클래스명
- Flexbox 기반 가로 메뉴
- 명확한 링크 텍스트
- 반응형 메뉴 구조

# 15. 개선된 통합 예제

```html
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>HTML 목록 예제</title>
  <style>
    body {
      font-family: sans-serif;
      line-height: 1.6;
    }

    .main-menu {
      display: flex;
      gap: 16px;
      margin: 0;
      padding: 0;
      list-style: none;
    }

    .course-info > div {
      display: grid;
      grid-template-columns: 100px 1fr;
      gap: 12px;
    }

    .course-info dt {
      font-weight: 700;
    }

    .course-info dd {
      margin: 0;
    }
  </style>
</head>
<body>
  <header>
    <nav aria-label="주요 메뉴">
      <ul class="main-menu">
        <li><a href="index.html" aria-current="page">홈</a></li>
        <li><a href="courses.html">교육 과정</a></li>
        <li><a href="projects.html">프로젝트</a></li>
      </ul>
    </nav>
  </header>

  <main>
    <h1>개발자 학습 과정</h1>

    <section>
      <h2>학습 분야</h2>
      <ul>
        <li>프론트엔드
          <ul>
            <li>HTML</li>
            <li>CSS</li>
            <li>JavaScript</li>
          </ul>
        </li>
        <li>백엔드
          <ul>
            <li>Java</li>
            <li>Spring Boot</li>
          </ul>
        </li>
      </ul>
    </section>

    <section>
      <h2>프로젝트 진행 순서</h2>
      <ol>
        <li>요구사항 분석</li>
        <li>화면 구조 설계</li>
        <li>기능 구현</li>
        <li>테스트 및 배포</li>
      </ol>
    </section>

    <section>
      <h2>과정 정보</h2>
      <dl class="course-info">
        <div>
          <dt>교육 기간</dt>
          <dd>6개월</dd>
        </div>
        <div>
          <dt>교육 방식</dt>
          <dd>이론 학습과 프로젝트 실습</dd>
        </div>
      </dl>
    </section>
  </main>
</body>
</html>
```

# 16. 자주 하는 실수

## 16.1 `ul` 바로 아래에 일반 요소 작성

```html
<ul>
  <a href="index.html">홈</a>
</ul>
```

```html
<ul>
  <li><a href="index.html">홈</a></li>
</ul>
```

## 16.2 하위 목록을 `li` 밖에 작성

```html
<ul>
  <li>프론트엔드</li>
  <ul>
    <li>HTML</li>
  </ul>
</ul>
```

```html
<ul>
  <li>프론트엔드
    <ul>
      <li>HTML</li>
    </ul>
  </li>
</ul>
```

## 16.3 숫자가 필요하다는 이유만으로 `ol` 사용

순서가 중요하지 않은 항목은 CSS로 번호처럼 꾸미려는 목적 때문에 `ol`로 바꾸지 않습니다. 콘텐츠의 의미를 먼저 판단합니다.

## 16.4 순서가 중요한 절차를 `ul`로 작성

설치나 가입 절차처럼 순서를 지켜야 하는 내용은 `ol`이 적절합니다.

## 16.5 `dl`을 일반 레이아웃 도구로 사용

`dl`은 단순히 두 열을 만들기 위한 요소가 아닙니다. 이름과 설명 또는 항목과 값의 관계가 있을 때 사용합니다.

## 16.6 마커를 없애려고 목록 구조까지 제거

```html
<div class="menu">
  <div>홈</div>
  <div>소개</div>
</div>
```

메뉴 항목의 관계가 중요하다면 목록 구조를 유지하고 CSS로 마커만 제거합니다.

## 16.7 지나치게 깊은 중첩

목록이 여러 단계로 깊어지면 사용자가 구조를 이해하기 어렵고 모바일 메뉴도 복잡해집니다. 정보 구조를 재검토하거나 별도 페이지로 분리합니다.

# 17. 실무 팁

## 17.1 요소 선택 기준을 먼저 정한다

```text
순서가 중요한가?
├─ 예 → ol
└─ 아니오
   ├─ 용어와 설명 관계인가? → dl
   └─ 관련 항목의 나열인가? → ul
```

## 17.2 CSS 초기화는 클래스 범위에서 시작한다

모든 `ul`의 스타일을 전역에서 제거하면 본문 목록까지 영향을 받을 수 있습니다.

```css
/* 영향 범위가 큼 */
ul {
  list-style: none;
}
```

```css
/* 메뉴에만 적용 */
.main-menu {
  margin: 0;
  padding: 0;
  list-style: none;
}
```

## 17.3 가로 메뉴는 Flexbox를 우선 검토한다

`inline-block`도 가능하지만, `display: flex`와 `gap`을 사용하면 공백 문자 문제 없이 간격과 정렬을 관리하기 쉽습니다.

## 17.4 링크 클릭 영역을 충분히 확보한다

```css
.main-menu a {
  display: block;
  padding: 12px 16px;
}
```

텍스트만 작은 영역으로 클릭되게 하지 않고 링크 자체에 패딩을 적용합니다.

## 17.5 목록이 동적으로 생성되어도 구조를 유지한다

JavaScript나 React로 메뉴를 렌더링할 때도 최종 DOM이 `ul > li > a`처럼 의미 있는 구조가 되도록 합니다.

# 18. 면접·복습 포인트

## Q1. `ul`과 `ol`의 차이는 무엇인가요?

`ul`은 순서가 중요하지 않은 관련 항목에 사용하고, `ol`은 절차나 순위처럼 순서가 의미를 가질 때 사용합니다.

## Q2. `ul`과 `ol`의 직접 자식으로 무엇을 작성하나요?

목록의 각 항목을 나타내는 `li`를 작성합니다. 링크나 문단 같은 콘텐츠는 `li` 안에 배치합니다.

## Q3. 중첩 목록은 어디에 작성해야 하나요?

하위 목록이 속한 상위 항목의 `li` 내부에 작성합니다.

## Q4. `dl`, `dt`, `dd`는 언제 사용하나요?

용어와 설명, 항목명과 값처럼 이름과 세부 정보의 관계를 표현할 때 사용합니다.

## Q5. 목록 마커를 제거하면 목록의 의미도 사라지나요?

아닙니다. CSS로 마커를 제거해도 HTML의 목록 구조와 의미는 유지됩니다.

## Q6. 메뉴를 `ul`로 작성하는 이유는 무엇인가요?

여러 링크가 하나의 관련된 메뉴 집합이며 각 링크가 메뉴 항목이라는 관계를 구조적으로 표현할 수 있기 때문입니다.

# 19. Problems

## Level 1

### 문제 1

다음 항목을 순서 없는 목록으로 작성하세요.

```text
HTML
CSS
JavaScript
```

### 문제 2

다음 가입 절차를 순서 있는 목록으로 작성하세요.

```text
약관 동의
정보 입력
이메일 인증
```

### 문제 3

다음 코드의 잘못된 구조를 수정하세요.

```html
<ul>
  <a href="index.html">홈</a>
  <a href="about.html">소개</a>
</ul>
```

### 문제 4

`HTML`이라는 용어와 `웹 문서의 구조를 작성하는 언어`라는 설명을 설명 목록으로 작성하세요.

## Level 2

### 문제 5

`프론트엔드` 아래에 `HTML`, `CSS`, `JavaScript`가 포함되는 중첩 목록을 작성하세요.

### 문제 6

다음 목록이 5부터 시작하도록 수정하세요.

```html
<ol>
  <li>다섯 번째 항목</li>
  <li>여섯 번째 항목</li>
</ol>
```

### 문제 7

홈, 교육 과정, 프로젝트 링크를 포함하는 내비게이션을 `nav`, `ul`, `li`, `a`로 작성하세요.

## Level 3

### 문제 8

다음 코드의 문제점을 찾아 올바르게 수정하세요.

```html
<ul>
  <li>개발</li>
  <ul>
    <li>프론트엔드</li>
    <li>백엔드</li>
  </ul>
</ul>
```

### 문제 9

목록 마커를 제거하고 항목을 가로로 배치하는 CSS를 Flexbox로 작성하세요. 클래스명은 `.category-list`를 사용합니다.

## Challenge

### 문제 10

다음 조건을 만족하는 학습 페이지 영역을 작성하세요.

- `nav` 안에 홈, 커리큘럼, 프로젝트 메뉴 작성
- 현재 페이지는 커리큘럼이며 `aria-current="page"` 사용
- 프론트엔드와 백엔드 분야를 중첩 목록으로 표현
- 프로젝트 진행 4단계를 순서 있는 목록으로 표현
- 교육 기간과 교육 방식을 설명 목록으로 표현

# 20. Answers

## 문제 1 정답

```html
<ul>
  <li>HTML</li>
  <li>CSS</li>
  <li>JavaScript</li>
</ul>
```

## 문제 2 정답

```html
<ol>
  <li>약관 동의</li>
  <li>정보 입력</li>
  <li>이메일 인증</li>
</ol>
```

순서를 바꾸면 가입 흐름이 달라지므로 `ol`을 사용합니다.

## 문제 3 정답

```html
<ul>
  <li><a href="index.html">홈</a></li>
  <li><a href="about.html">소개</a></li>
</ul>
```

`ul`의 각 항목을 `li`로 만들고 링크를 그 안에 작성합니다.

## 문제 4 정답

```html
<dl>
  <dt>HTML</dt>
  <dd>웹 문서의 구조를 작성하는 언어</dd>
</dl>
```

## 문제 5 정답

```html
<ul>
  <li>프론트엔드
    <ul>
      <li>HTML</li>
      <li>CSS</li>
      <li>JavaScript</li>
    </ul>
  </li>
</ul>
```

## 문제 6 정답

```html
<ol start="5">
  <li>다섯 번째 항목</li>
  <li>여섯 번째 항목</li>
</ol>
```

## 문제 7 정답

```html
<nav aria-label="주요 메뉴">
  <ul>
    <li><a href="index.html">홈</a></li>
    <li><a href="courses.html">교육 과정</a></li>
    <li><a href="projects.html">프로젝트</a></li>
  </ul>
</nav>
```

## 문제 8 정답

```html
<ul>
  <li>개발
    <ul>
      <li>프론트엔드</li>
      <li>백엔드</li>
    </ul>
  </li>
</ul>
```

하위 `ul`을 상위 항목인 `개발`의 `li` 안으로 이동합니다.

## 문제 9 정답

```css
.category-list {
  display: flex;
  gap: 16px;
  margin: 0;
  padding: 0;
  list-style: none;
}
```

## 문제 10 예시 정답

```html
<nav aria-label="주요 메뉴">
  <ul>
    <li><a href="index.html">홈</a></li>
    <li><a href="curriculum.html" aria-current="page">커리큘럼</a></li>
    <li><a href="projects.html">프로젝트</a></li>
  </ul>
</nav>

<section>
  <h2>학습 분야</h2>
  <ul>
    <li>프론트엔드
      <ul>
        <li>HTML</li>
        <li>CSS</li>
        <li>JavaScript</li>
      </ul>
    </li>
    <li>백엔드
      <ul>
        <li>Java</li>
        <li>Spring Boot</li>
      </ul>
    </li>
  </ul>
</section>

<section>
  <h2>프로젝트 진행 순서</h2>
  <ol>
    <li>요구사항 분석</li>
    <li>화면 설계</li>
    <li>기능 구현</li>
    <li>테스트 및 배포</li>
  </ol>
</section>

<section>
  <h2>교육 정보</h2>
  <dl>
    <dt>교육 기간</dt>
    <dd>6개월</dd>
    <dt>교육 방식</dt>
    <dd>이론과 프로젝트 병행</dd>
  </dl>
</section>
```

# 21. 최종 체크리스트

- [ ] 순서가 중요하지 않은 항목에 `ul`을 사용했는가?
- [ ] 순서가 중요한 절차와 순위에 `ol`을 사용했는가?
- [ ] `ul`과 `ol`의 각 항목을 `li`로 작성했는가?
- [ ] 링크와 문단 등은 `li` 안에 배치했는가?
- [ ] 하위 목록을 상위 `li` 내부에 작성했는가?
- [ ] 용어와 설명 관계에 `dl`, `dt`, `dd`를 사용했는가?
- [ ] 시각적 모양이 아닌 콘텐츠 의미를 기준으로 목록을 선택했는가?
- [ ] 내비게이션의 링크 텍스트가 명확한가?
- [ ] 현재 페이지에 필요하면 `aria-current="page"`를 사용했는가?
- [ ] 전역 목록 스타일이 다른 본문 목록에 영향을 주지 않는가?

# 22. 핵심 요약

```text
ul                  → 순서가 중요하지 않은 목록
ol                  → 순서가 중요한 목록
li                  → ul·ol의 각 항목
dl                  → 용어와 설명의 전체 목록
dt                  → 설명할 용어 또는 이름
dd                  → 용어의 설명 또는 값
ol start="5"        → 목록을 5부터 시작
ol reversed         → 역순 목록
li value="5"       → 특정 항목 번호 지정
ul > li > ul        → 올바른 중첩 목록 구조
nav > ul > li > a   → 대표적인 내비게이션 구조
list-style: none    → 목록 의미는 유지하고 마커 제거
display: flex       → 가로 메뉴 배치에 자주 사용
```

> 목록 태그를 선택할 때는 화면에 점이나 숫자가 필요한지를 먼저 생각하지 않습니다. 항목 사이에 순서가 있는지, 용어와 설명의 관계인지, 하나의 관련된 집합인지를 판단한 뒤 의미에 맞는 요소를 선택해야 합니다.
