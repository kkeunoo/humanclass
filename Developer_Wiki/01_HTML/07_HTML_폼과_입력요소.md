# HTML 폼과 입력 요소

## 문서 정보

| 항목 | 내용 |
| --- | --- |
| 문서 | `07_HTML_폼과_입력요소.md` |
| 권장 선수 학습 | `06_HTML_이미지와_미디어.md` |
| 다음 학습 | `08_HTML_시맨틱태그와_페이지구조.md` |
| 학습 범위 | `form`, `input`, `button`, `label`, `select`, `option`, `textarea`, `name`, `value`, `placeholder`, `readonly`, `disabled`, `checked`, `selected`, `GET`, `POST` |
| 프로젝트 연결 | 로그인, 회원가입, 검색, 설문, 주문, 문의, 관리자 입력 화면 |

> 폼은 사용자가 입력한 데이터를 서버로 전달하는 구조입니다. 화면에 입력 칸을 보이게 만드는 것만으로는 충분하지 않으며, 각 값에 이름을 붙이고 올바른 전송 방식과 접근성까지 함께 설계해야 합니다.

# 학습 목표

- `form` 요소의 역할을 설명한다.
- 입력 요소가 서버로 전송되기 위한 조건을 이해한다.
- `name`과 `value`가 요청 데이터에서 어떤 역할을 하는지 설명한다.
- `input`의 주요 `type`을 목적에 맞게 선택한다.
- `placeholder`, `readonly`, `disabled`의 차이를 구분한다.
- `checkbox`와 `radio`의 선택 방식과 데이터 구조를 이해한다.
- `label`을 입력 요소와 올바르게 연결한다.
- `select`, `option`, `textarea`를 사용할 수 있다.
- `button`의 기본 타입과 제출 동작을 설명한다.
- `GET`과 `POST`의 차이를 기초 수준에서 구분한다.
- 검색 사이트로 값을 전달하는 폼을 작성한다.
- 내 코드와 강사님 코드를 비교해 오류와 개선점을 찾는다.
- 접근성과 실무 유지보수를 고려한 폼을 구성한다.

# 1. 폼이란?

폼(form)은 사용자가 입력하거나 선택한 값을 하나의 묶음으로 구성해 서버에 전달하는 영역입니다.

대표적인 폼은 다음과 같습니다.

- 로그인
- 회원가입
- 검색
- 게시글 작성
- 문의 등록
- 상품 주문
- 설문 조사
- 관리자 데이터 입력

기본 구조는 다음과 같습니다.

```html
<form action="/login" method="post">
  <label for="user-id">아이디</label>
  <input type="text" id="user-id" name="userId">

  <label for="user-password">비밀번호</label>
  <input
    type="password"
    id="user-password"
    name="password"
  >

  <button type="submit">로그인</button>
</form>
```

폼 내부에는 보통 다음 요소들이 사용됩니다.

| 요소 | 역할 |
| --- | --- |
| `input` | 한 줄 입력, 선택, 날짜, 숫자 등 |
| `textarea` | 여러 줄 텍스트 입력 |
| `select` | 선택 목록 |
| `button` | 제출, 초기화, 일반 동작 |
| `label` | 입력 요소의 이름과 목적 제공 |

# 2. `form` 요소

`form`은 서버로 전송할 입력 요소들을 감싸는 컨테이너입니다.

```html
<form>
  <input type="text" name="keyword">
  <button type="submit">검색</button>
</form>
```

한 페이지에 여러 개의 `form`을 둘 수 있습니다.

```html
<form action="/search">
  <!-- 검색 폼 -->
</form>

<form action="/login" method="post">
  <!-- 로그인 폼 -->
</form>
```

하지만 `form` 안에 또 다른 `form`을 중첩하면 안 됩니다.

```html
<!-- 잘못된 구조 -->
<form>
  <form>
    <input type="text">
  </form>
</form>
```

브라우저가 마크업을 예상과 다르게 보정할 수 있고, 제출 범위도 불명확해집니다.

# 3. 폼 데이터의 기본 구조

서버로 전달되는 폼 데이터는 기본적으로 다음 구조를 가집니다.

```text
name=value
```

예를 들어 다음 입력에 사용자가 `HTML`을 입력했다고 가정합니다.

```html
<input type="text" name="keyword">
```

전송 데이터는 다음과 같은 형태가 됩니다.

```text
keyword=HTML
```

입력 요소가 여러 개라면 `&`로 연결됩니다.

```text
song=HypeBoy&singer=NewJeans
```

핵심은 다음과 같습니다.

| 속성 | 역할 |
| --- | --- |
| `name` | 서버가 값을 구분하는 키 |
| `value` | 서버로 전달되는 값 |

`name`이 없는 입력 요소는 화면에는 보이지만 일반적인 폼 전송 데이터에 포함되지 않습니다.

```html
<form method="get">
  <input type="text" name="song">
  <input type="text">
  <input type="text" name="singer">
  <button type="submit">전송</button>
</form>
```

두 번째 입력 칸은 `name`이 없으므로 사용자가 값을 입력해도 서버가 받을 키가 없습니다.

# 4. `input` 기본 사용법

`input`은 다양한 입력 방식을 제공하는 빈 요소입니다.

```html
<input type="text">
```

`input`에는 닫는 태그를 작성하지 않습니다.

```html
<!-- 잘못된 예 -->
<input type="text"></input>
```

`type`을 생략하면 기본값은 `text`입니다.

```html
<input>
```

그러나 코드의 목적을 명확하게 하기 위해 보통 `type`을 직접 작성합니다.

```html
<input type="text">
```

# 5. `type="text"`

한 줄 텍스트를 입력받습니다.

```html
<label for="nickname">닉네임</label>
<input type="text" id="nickname" name="nickname">
```

주요 용도는 다음과 같습니다.

- 이름
- 닉네임
- 제목
- 검색어
- 주소 일부
- 일반 문자열

긴 문장을 여러 줄로 입력받아야 한다면 `textarea`가 더 적절합니다.

# 6. `value`: 초기값과 전송값

텍스트 입력 요소의 `value`는 처음 표시할 값을 지정합니다.

```html
<input
  type="text"
  name="category"
  value="HTML"
>
```

사용자는 초기값을 수정할 수 있습니다.

`value`는 입력 타입에 따라 역할이 조금 다릅니다.

| 입력 타입 | `value`의 의미 |
| --- | --- |
| `text` | 입력 칸의 현재 값 또는 초기값 |
| `submit` | 버튼에 표시되는 문구 |
| `checkbox` | 체크했을 때 서버로 전달할 값 |
| `radio` | 선택했을 때 서버로 전달할 값 |
| `button` | 버튼에 표시되는 문구 |

예시:

```html
<input type="submit" value="전송">
```

```html
<input
  type="checkbox"
  name="option"
  value="shot"
>
```

# 7. `placeholder`

`placeholder`는 입력 전에 보여주는 안내 문구입니다.

```html
<input
  type="text"
  name="keyword"
  placeholder="검색어를 입력하세요"
>
```

사용자가 값을 입력하면 안내 문구는 사라지고, 입력 내용을 지우면 다시 나타납니다.

`placeholder`는 실제 값이 아닙니다.

```html
<input
  type="text"
  name="name"
  placeholder="홍길동"
>
```

사용자가 아무것도 입력하지 않으면 `홍길동`이 전송되는 것이 아닙니다.

## 7.1 `value`와 `placeholder` 비교

```html
<input
  type="text"
  value="초기값"
  placeholder="안내 문구"
>
```

`value`가 존재하면 입력 칸에 실제 값이 표시되므로 `placeholder`는 보이지 않습니다.

| 구분 | `value` | `placeholder` |
| --- | --- | --- |
| 실제 입력값인가? | 예 | 아니요 |
| 서버 전송 대상인가? | 예 | 아니요 |
| 사용자가 수정할 수 있는가? | 일반적으로 가능 | 해당 없음 |
| 목적 | 기본 데이터 제공 | 입력 방법 안내 |

## 7.2 `placeholder`를 `label` 대신 쓰지 않는다

```html
<!-- 권장하지 않음 -->
<input type="email" placeholder="이메일">
```

사용자가 입력을 시작하면 입력 항목의 목적이 사라집니다.

```html
<label for="email">이메일</label>
<input
  type="email"
  id="email"
  name="email"
  placeholder="example@example.com"
>
```

`label`은 항목 이름을 제공하고, `placeholder`는 예시나 형식을 보조합니다.

# 8. `readonly`와 `disabled`

## 8.1 `readonly`

사용자가 값을 수정할 수 없지만 일반적인 폼 전송에는 포함됩니다.

```html
<input
  type="text"
  name="memberId"
  value="user01"
  readonly
>
```

## 8.2 `disabled`

입력 요소를 비활성화하며, 일반적인 폼 전송 데이터에 포함되지 않습니다.

```html
<input
  type="text"
  name="memberGrade"
  value="일반 회원"
  disabled
>
```

## 8.3 비교

| 구분 | `readonly` | `disabled` |
| --- | --- | --- |
| 값 수정 | 불가 | 불가 |
| 포커스 | 일반적으로 가능 | 불가 |
| 폼 전송 | 포함 | 제외 |
| 대표 용도 | 수정하면 안 되지만 전달해야 하는 값 | 현재 사용할 수 없는 기능 |

`disabled`된 값을 서버로 반드시 보내야 한다면 별도의 숨김 입력을 함께 사용하는 방법이 있습니다.

```html
<input type="text" value="일반 회원" disabled>
<input type="hidden" name="memberGrade" value="일반 회원">
```

단, 브라우저에서 전송되는 값은 사용자가 개발자 도구로 변경할 수 있으므로 서버는 반드시 값을 다시 검증해야 합니다.

# 9. `type="password"`

비밀번호 입력 내용을 화면에서 가려 표시합니다.

```html
<label for="password">비밀번호</label>
<input
  type="password"
  id="password"
  name="password"
>
```

화면에서 글자가 가려진다고 해서 데이터가 자동으로 암호화되는 것은 아닙니다.

실제 서비스에서는 다음이 필요합니다.

- HTTPS 사용
- 서버에서 안전한 비밀번호 해시 처리
- 로그나 화면에 비밀번호 노출 금지
- 클라이언트 값만 신뢰하지 않기

# 10. 버튼의 종류

HTML에서는 `input`과 `button` 모두 버튼을 만들 수 있습니다.

## 10.1 `input type="button"`

```html
<input type="button" value="일반 버튼">
```

표시 문구는 `value`에 작성합니다.

## 10.2 `input type="submit"`

폼 데이터를 제출합니다.

```html
<input type="submit" value="전송">
```

## 10.3 `button`

```html
<button type="button">일반 버튼</button>
```

`button`은 시작 태그와 종료 태그 사이에 텍스트나 이미지를 넣을 수 있습니다.

```html
<button type="button">
  <img src="asset/search.png" alt="">
  검색
</button>
```

장식용 아이콘이라면 빈 `alt`를 사용할 수 있습니다. 버튼의 텍스트가 이미 목적을 설명하기 때문입니다.

## 10.4 `button`의 기본 타입

`form` 내부에서 `button`의 기본 `type`은 `submit`입니다.

```html
<form>
  <button>저장</button>
</form>
```

위 버튼은 폼을 제출합니다.

제출 목적이 아니라면 반드시 `type="button"`을 지정합니다.

```html
<button type="button">주소 검색</button>
```

| 타입 | 역할 |
| --- | --- |
| `submit` | 폼 제출 |
| `button` | JavaScript 등 일반 동작 |
| `reset` | 폼 초기화 |

# 11. 잘못 작성한 속성은 원하는 기능을 하지 않는다

다음 코드에서 `value123`은 HTML 표준 속성이 아닙니다.

```html
<input type="submit" value123="전송">
```

브라우저는 알 수 없는 사용자 정의 형태의 속성처럼 보관할 수 있지만, 제출 버튼 문구를 지정하는 기능은 하지 않습니다.

올바른 코드는 다음과 같습니다.

```html
<input type="submit" value="전송">
```

HTML은 일부 오류를 자동으로 복구하기 때문에 화면이 보인다고 해서 코드가 올바른 것은 아닙니다.

개발자 도구와 HTML 검사기를 활용해 확인해야 합니다.

# 12. 체크박스

체크박스는 여러 항목을 동시에 선택하거나, 아무것도 선택하지 않을 수 있을 때 사용합니다.

```html
<label>
  <input
    type="checkbox"
    name="coffee"
    value="shot"
  >
  샷 추가
</label>

<label>
  <input
    type="checkbox"
    name="coffee"
    value="pearl"
  >
  펄 추가
</label>
```

두 항목을 모두 선택하면 같은 `name`으로 여러 값이 전달될 수 있습니다.

```text
coffee=shot&coffee=pearl
```

서버에서는 이를 배열이나 목록으로 처리하는 경우가 많습니다.

## 12.1 `checked`

처음부터 선택된 상태로 표시합니다.

```html
<input
  type="checkbox"
  name="agree"
  value="yes"
  checked
>
```

## 12.2 체크하지 않은 값

체크되지 않은 체크박스는 일반적인 폼 전송에 포함되지 않습니다.

```html
<input
  type="checkbox"
  name="marketing"
  value="yes"
>
```

사용자가 체크하지 않으면 `marketing` 키 자체가 전달되지 않을 수 있습니다.

## 12.3 `value`를 생략한 경우

```html
<input type="checkbox" name="agree">
```

선택하면 브라우저 기본값인 `on`이 전달될 수 있습니다.

```text
agree=on
```

서버가 의미를 명확히 알 수 있도록 실무에서는 `value`를 직접 작성하는 것이 좋습니다.

```html
<input
  type="checkbox"
  name="agree"
  value="terms"
>
```

# 13. 라디오 버튼

라디오 버튼은 여러 항목 중 하나만 선택할 때 사용합니다.

```html
<label>
  <input
    type="radio"
    name="delivery"
    value="standard"
    checked
  >
  일반 배송
</label>

<label>
  <input
    type="radio"
    name="delivery"
    value="express"
  >
  빠른 배송
</label>
```

라디오 버튼은 같은 `name`을 가진 항목끼리 하나의 그룹을 형성합니다.

```html
<input type="radio" name="gender" value="female">
<input type="radio" name="gender" value="male">
```

`name`이 다르면 서로 다른 그룹이 되어 동시에 선택할 수 있습니다.

```html
<!-- 서로 다른 그룹 -->
<input type="radio" name="group-a" value="1">
<input type="radio" name="group-b" value="2">
```

## 13.1 여러 항목에 `checked`를 작성한 경우

같은 그룹에서 여러 항목에 `checked`를 작성하면 브라우저는 일반적으로 뒤쪽 항목을 선택된 상태로 처리합니다.

```html
<input
  type="radio"
  name="gender"
  value="female"
  checked
>
<input
  type="radio"
  name="gender"
  value="male"
  checked
>
```

초기 선택값은 한 곳에만 작성해야 합니다.

## 13.2 체크박스와 라디오 비교

| 구분 | 체크박스 | 라디오 |
| --- | --- | --- |
| 선택 개수 | 0개 이상 | 그룹당 1개 |
| 같은 `name` | 복수 값 전달 가능 | 하나의 값 전달 |
| 대표 용도 | 추가 옵션, 약관 동의 | 배송 방식, 결제 방식 |

# 14. `label`

`label`은 입력 요소의 이름과 목적을 사용자에게 알려 줍니다.

## 14.1 감싸는 방식

```html
<label>
  <input type="checkbox" name="option" value="pearl">
  펄 추가
</label>
```

텍스트를 클릭해도 체크박스를 선택할 수 있습니다.

## 14.2 `for`와 `id` 연결 방식

```html
<input
  type="checkbox"
  id="pearl"
  name="option"
  value="pearl"
>
<label for="pearl">펄 추가</label>
```

`label`의 `for` 값과 입력 요소의 `id` 값이 같아야 합니다.

```text
label for="pearl"
input id="pearl"
```

이 방식은 입력 요소와 텍스트가 떨어져 있어도 명시적으로 연결할 수 있습니다.

## 14.3 `id`는 문서에서 고유해야 한다

```html
<!-- 잘못된 예 -->
<input type="checkbox" id="option">
<input type="checkbox" id="option">
```

같은 `id`가 중복되면 `label`, CSS, JavaScript가 어떤 요소를 가리키는지 불명확해집니다.

## 14.4 `label`이 중요한 이유

- 텍스트를 눌러도 입력 요소를 선택할 수 있다.
- 작은 체크박스와 라디오 버튼의 클릭 영역이 넓어진다.
- 스크린 리더가 항목 이름을 이해할 수 있다.
- 폼의 목적이 더 명확해진다.

# 15. `select`와 `option`

`select`는 펼쳐지는 선택 목록을 만듭니다.

```html
<label for="food">음식 종류</label>
<select id="food" name="food">
  <option value="korean">한식</option>
  <option value="chinese">중식</option>
  <option value="western">양식</option>
  <option value="snack">분식</option>
  <option value="japanese">일식</option>
</select>
```

사용자에게 보이는 텍스트와 서버로 전달되는 값은 다르게 지정할 수 있습니다.

```html
<option value="korean">한식</option>
```

화면에는 `한식`이 보이고, 전송 값은 `korean`입니다.

## 15.1 `selected`

처음 선택된 옵션을 지정합니다.

```html
<option value="snack" selected>분식</option>
```

`selected`가 없으면 일반적으로 첫 번째 옵션이 기본 선택됩니다.

## 15.2 안내용 첫 옵션

사용자가 직접 선택하도록 유도할 수 있습니다.

```html
<select name="category" required>
  <option value="" selected disabled>
    카테고리를 선택하세요
  </option>
  <option value="html">HTML</option>
  <option value="css">CSS</option>
  <option value="javascript">JavaScript</option>
</select>
```

빈 값을 가진 안내 옵션과 `required`를 함께 사용하면 선택 검증에 도움이 됩니다.

# 16. 다중 선택 `select`

`multiple`을 사용하면 여러 옵션을 선택할 수 있습니다.

```html
<label for="skills">보유 기술</label>
<select
  id="skills"
  name="skills"
  multiple
  size="3"
>
  <option value="html">HTML</option>
  <option value="css">CSS</option>
  <option value="javascript">JavaScript</option>
  <option value="react">React</option>
</select>
```

| 속성 | 역할 |
| --- | --- |
| `multiple` | 여러 옵션 선택 허용 |
| `size` | 화면에 동시에 표시할 옵션 수 |

데스크톱에서는 `Ctrl` 또는 `Shift` 키를 사용해 여러 항목을 선택할 수 있지만, 모바일이나 사용자 환경에 따라 조작 방식이 다릅니다.

선택지가 많거나 조작이 복잡하다면 체크박스 목록이 더 이해하기 쉬운지 검토해야 합니다.

# 17. `textarea`

`textarea`는 여러 줄 텍스트를 입력받습니다.

```html
<label for="message">문의 내용</label>
<textarea
  id="message"
  name="message"
  rows="8"
  cols="50"
  placeholder="문의 내용을 입력하세요"
></textarea>
```

`textarea`는 `input`과 달리 시작 태그와 종료 태그가 있습니다.

```html
<textarea></textarea>
```

초기값은 태그 사이에 작성합니다.

```html
<textarea name="message">미리 표시할 내용</textarea>
```

## 17.1 공백과 줄바꿈 주의

다음 코드의 들여쓰기와 줄바꿈도 초기값에 포함될 수 있습니다.

```html
<textarea name="message">
  미리 표시할 내용
</textarea>
```

불필요한 공백을 피하려면 시작 태그와 텍스트를 붙여 작성합니다.

```html
<textarea name="message">미리 표시할 내용</textarea>
```

## 17.2 HTML 태그는 렌더링되지 않는다

```html
<textarea>
  첫 번째 줄<br>
  두 번째 줄
</textarea>
```

`<br>`은 줄바꿈 태그로 실행되지 않고 문자 그대로 입력값에 포함됩니다.

`textarea` 내부는 일반 HTML 콘텐츠 영역이 아니라 원시 텍스트 입력값으로 취급됩니다.

## 17.3 주석도 초기값이 될 수 있다

```html
<textarea>
  <!-- 안내 문구 -->
</textarea>
```

주석처럼 작성했더라도 `textarea`에서는 텍스트로 보일 수 있습니다.

초기 안내는 `placeholder`를 사용합니다.

```html
<textarea placeholder="문의 내용을 입력하세요"></textarea>
```

# 18. 폼 초기화

`type="reset"`은 폼 요소를 페이지가 처음 로드되었을 때의 초기 상태로 되돌립니다.

```html
<input type="reset" value="초기화">
```

또는 다음처럼 작성합니다.

```html
<button type="reset">초기화</button>
```

사용자가 입력한 모든 내용을 실수로 지울 수 있으므로 실제 서비스에서는 초기화 버튼이 꼭 필요한지 검토해야 합니다.

긴 신청서나 작성 화면에서 초기화 버튼을 제출 버튼 가까이에 두면 오조작 위험이 커집니다.

# 19. 다양한 입력 타입

HTML은 입력 목적에 맞는 여러 `type`을 제공합니다.

## 19.1 색상

```html
<label for="theme-color">테마 색상</label>
<input
  type="color"
  id="theme-color"
  name="themeColor"
>
```

## 19.2 날짜

```html
<label for="start-date">시작일</label>
<input
  type="date"
  id="start-date"
  name="startDate"
  value="2026-06-24"
>
```

날짜 값은 일반적으로 `YYYY-MM-DD` 형식을 사용합니다.

## 19.3 시간

```html
<label for="start-time">시작 시간</label>
<input
  type="time"
  id="start-time"
  name="startTime"
>
```

## 19.4 숫자

```html
<label for="quantity">수량</label>
<input
  type="number"
  id="quantity"
  name="quantity"
  min="1"
  max="10"
  step="1"
>
```

숫자 입력에는 일부 브라우저에서 지수 표기용 `e` 등이 입력될 수 있습니다.

따라서 화면 입력 제한만 믿지 말고 서버에서도 숫자 범위와 형식을 검증해야 합니다.

## 19.5 범위

```html
<label for="volume">볼륨</label>
<input
  type="range"
  id="volume"
  name="volume"
  min="10"
  max="100"
  step="10"
  value="50"
>
```

| 속성 | 역할 |
| --- | --- |
| `min` | 최소값 |
| `max` | 최대값 |
| `step` | 증가·감소 단위 |
| `value` | 초기값 |

범위 입력은 현재 값을 화면에서 바로 알기 어려울 수 있으므로 필요하면 JavaScript로 값을 함께 표시합니다.

# 20. 실무에서 자주 사용하는 추가 입력 타입

## 20.1 이메일

```html
<label for="email">이메일</label>
<input
  type="email"
  id="email"
  name="email"
  autocomplete="email"
>
```

브라우저가 기본적인 이메일 형식을 검사하고 모바일에서 이메일 입력에 적합한 키보드를 제공할 수 있습니다.

## 20.2 전화번호

```html
<label for="phone">전화번호</label>
<input
  type="tel"
  id="phone"
  name="phone"
  autocomplete="tel"
>
```

`tel`은 전화번호 형식을 자동으로 완벽하게 검증하지 않습니다. 국가와 서비스 정책에 맞는 추가 검증이 필요합니다.

## 20.3 URL

```html
<label for="portfolio">포트폴리오 URL</label>
<input
  type="url"
  id="portfolio"
  name="portfolio"
>
```

## 20.4 검색

```html
<label for="site-search">사이트 검색</label>
<input
  type="search"
  id="site-search"
  name="keyword"
>
```

## 20.5 숨김 값

```html
<input
  type="hidden"
  name="articleId"
  value="123"
>
```

화면에 보이지 않지만 폼 데이터에 포함됩니다.

숨김 입력은 보안 장치가 아닙니다. 사용자가 개발자 도구로 값을 변경할 수 있으므로 서버 검증이 필요합니다.

# 21. `required`와 기본 검증

`required`는 필수 입력을 지정합니다.

```html
<label for="username">이름</label>
<input
  type="text"
  id="username"
  name="username"
  required
>
```

필수 항목이 비어 있으면 브라우저가 폼 제출을 막고 안내 메시지를 표시할 수 있습니다.

다른 기본 검증 속성도 있습니다.

| 속성 | 용도 |
| --- | --- |
| `required` | 필수 입력 |
| `minlength` | 최소 글자 수 |
| `maxlength` | 최대 글자 수 |
| `min` | 최소 숫자·날짜 |
| `max` | 최대 숫자·날짜 |
| `step` | 입력 단위 |
| `pattern` | 정규식 패턴 |

예시:

```html
<label for="user-id">아이디</label>
<input
  type="text"
  id="user-id"
  name="userId"
  minlength="4"
  maxlength="20"
  required
>
```

클라이언트 검증은 사용자 편의를 위한 1차 검증입니다.

서버는 모든 입력값을 다시 검증해야 합니다.

# 22. `action`

`action`은 폼 데이터를 전송할 서버 주소를 지정합니다.

```html
<form action="/members" method="post">
```

`action`을 생략하면 현재 문서 주소로 전송됩니다.

```html
<form method="get">
```

외부 검색 서비스로 값을 전달할 수도 있습니다.

```html
<form
  action="https://www.google.com/search"
  method="get"
  target="_blank"
>
  <label for="google-query">구글 검색</label>
  <input
    type="search"
    id="google-query"
    name="q"
  >
  <button type="submit">검색</button>
</form>
```

구글 검색은 검색어 키로 `q`를 사용하므로 입력 요소의 `name`도 `q`로 맞춥니다.

# 23. `method`

`method`는 폼 데이터를 어떤 HTTP 방식으로 전달할지 지정합니다.

기초 단계에서는 `GET`과 `POST`를 우선 이해합니다.

```html
<form method="get">
```

```html
<form method="post">
```

`method`를 생략하면 기본값은 `get`입니다.

# 24. GET 방식

GET은 데이터를 URL의 쿼리 문자열로 전달합니다.

```html
<form method="get" action="/search">
  <input type="text" name="keyword">
  <button type="submit">검색</button>
</form>
```

사용자가 `HTML`을 입력하면 주소는 다음과 비슷해집니다.

```text
/search?keyword=HTML
```

여러 값은 `&`로 연결됩니다.

```text
/search?keyword=HTML&page=2
```

GET의 대표적인 특징은 다음과 같습니다.

- 주소에 데이터가 표시된다.
- 검색 결과를 북마크하거나 공유하기 쉽다.
- 조회와 검색 요청에 적합하다.
- 브라우저 기록에 남을 수 있다.
- 민감한 정보를 보내는 용도로 적합하지 않다.

# 25. POST 방식

POST는 요청 본문(body)에 폼 데이터를 담아 전달합니다.

```html
<form method="post" action="/login">
  <input type="text" name="userId">
  <input type="password" name="password">
  <button type="submit">로그인</button>
</form>
```

주소창에 값이 직접 나타나지 않는다는 점은 GET과 다릅니다.

하지만 POST가 자동으로 데이터를 암호화하는 것은 아닙니다.

HTTPS가 없는 환경에서는 전송 내용을 안전하게 보호할 수 없습니다.

POST는 다음과 같은 작업에 주로 사용합니다.

- 로그인
- 회원가입
- 게시글 등록
- 주문 생성
- 데이터 수정
- 파일 업로드

# 26. GET과 POST 비교

| 항목 | GET | POST |
| --- | --- | --- |
| 데이터 위치 | URL 쿼리 문자열 | 요청 본문 |
| 주소 표시 | 보임 | 직접 보이지 않음 |
| 대표 용도 | 조회, 검색 | 생성, 변경, 로그인 |
| 북마크·공유 | 쉬움 | 일반적으로 어려움 |
| 민감 정보 | 부적합 | HTTPS와 함께 사용 |
| 기본값 | `form`의 기본 방식 | 직접 지정 필요 |

`GET은 안전하지 않고 POST는 안전하다`처럼 단순하게 외우면 안 됩니다.

- GET도 HTTPS를 사용하면 전송 구간은 암호화됩니다.
- POST도 HTTPS가 없으면 안전하지 않습니다.
- 서버는 요청 방식과 관계없이 인증, 권한, 검증을 수행해야 합니다.

# 27. Live Server에서 POST 오류가 발생하는 이유

정적 파일 서버인 Live Server는 HTML, CSS, JavaScript 파일을 제공하는 용도입니다.

```html
<form method="post">
  <input type="text" name="query">
  <button type="submit">POST 연습</button>
</form>
```

POST 요청을 처리할 백엔드 경로가 없으면 다음과 같은 응답이 나올 수 있습니다.

```text
405 Method Not Allowed
```

이는 HTML 문법 오류라기보다 서버가 해당 방식의 요청 처리를 지원하지 않기 때문입니다.

POST를 실제로 처리하려면 다음과 같은 서버가 필요합니다.

- Spring Boot
- Node.js
- Django
- Flask
- PHP
- 기타 백엔드 애플리케이션

개발자 도구의 Network 탭에서는 요청 방식과 전송 데이터가 어떻게 구성되는지 확인할 수 있습니다.

# 28. 검색 폼 실습

## 28.1 네이버 검색

```html
<form
  method="get"
  action="https://search.naver.com/search.naver"
  target="_blank"
>
  <label for="naver-query">네이버 검색어</label>
  <input
    type="search"
    id="naver-query"
    name="query"
  >
  <button type="submit">네이버 검색</button>
</form>
```

네이버 검색은 검색어 키로 `query`를 사용합니다.

## 28.2 구글 검색

```html
<form
  method="get"
  action="https://www.google.com/search"
  target="_blank"
>
  <label for="google-q">구글 검색어</label>
  <input
    type="search"
    id="google-q"
    name="q"
  >
  <button type="submit">구글 검색</button>
</form>
```

구글 검색은 검색어 키로 `q`를 사용합니다.

이 예제에서 중요한 점은 외부 사이트마다 요구하는 매개변수 이름이 다를 수 있다는 것입니다.

# 29. 내 코드 분석

원본 내 코드에는 폼 요소별 동작을 이해하기 위한 주석과 실습이 자세하게 포함되어 있습니다.

대표적인 장점은 다음과 같습니다.

- `form` 안에 `form`을 중첩하지 않아야 한다는 점을 기록했다.
- `name`이 없으면 전송되지 않는다는 점을 이해했다.
- `readonly`와 `disabled`의 전송 차이를 기록했다.
- 체크박스와 라디오 버튼의 선택 방식 차이를 정리했다.
- `label`의 감싸기 방식과 `for` 연결 방식을 모두 실습했다.
- `GET` 쿼리 문자열 구조를 확인했다.
- Live Server가 POST 처리를 하지 못하는 이유를 관찰했다.

학습 기록으로서 개념을 놓치지 않고 주석으로 남겼다는 점이 좋습니다.

# 30. 내 코드에서 확인된 개선점

## 30.1 잘못된 `value123`

원본에는 다음 코드가 있습니다.

```html
<input type="submit" value123="전송">
```

`value123`은 제출 버튼 문구를 지정하는 속성이 아닙니다.

```html
<input type="submit" value="전송">
```

오타가 있어도 브라우저가 페이지를 중단하지 않을 수 있으므로 화면만 보고 판단하면 안 됩니다.

## 30.2 `value`와 `placeholder`를 함께 사용한 예

```html
<input
  type="text"
  value="초기값"
  placeholder="플레이스홀더"
>
```

이 코드는 문법적으로 가능하지만 `value`가 존재하므로 `placeholder`가 보이지 않습니다.

두 속성의 차이를 확인하기 위한 실습으로는 의미가 있지만, 실제 폼에서는 목적에 맞게 하나씩 사용하는 것이 명확합니다.

## 30.3 입력 요소와 텍스트를 `label`로 연결

원본의 일부 체크박스와 라디오 버튼은 입력 요소 뒤에 텍스트만 작성되어 있습니다.

```html
<input
  type="checkbox"
  name="coffee"
  value="1"
>
샷 추가
```

다음처럼 `label`을 사용하면 클릭 영역과 접근성이 좋아집니다.

```html
<label>
  <input
    type="checkbox"
    name="coffee"
    value="shot"
  >
  샷 추가
</label>
```

## 30.4 의미 있는 `value` 사용

숫자 값도 사용할 수 있지만 서버 코드에서 의미를 바로 이해하기 어렵습니다.

```html
<input
  type="checkbox"
  name="coffee"
  value="1"
>
```

다음처럼 의미가 드러나는 값을 사용할 수 있습니다.

```html
<input
  type="checkbox"
  name="coffee"
  value="shot"
>
```

프로젝트 정책에 따라 데이터베이스 식별자를 사용할 수도 있으므로 정답이 하나로 고정되는 것은 아닙니다.

## 30.5 여러 개의 `<br>` 대신 구조와 CSS 사용

폼 요소 사이를 `<br>`로 반복해서 띄우면 레이아웃 관리가 어렵습니다.

```html
<label for="name">이름</label>
<input type="text" id="name" name="name">
<br>
```

구조를 그룹화한 뒤 CSS로 간격을 지정합니다.

```html
<div class="form-field">
  <label for="name">이름</label>
  <input type="text" id="name" name="name">
</div>
```

```css
.form-field {
  display: grid;
  gap: 0.5rem;
  margin-bottom: 1rem;
}
```

# 31. 강사님 코드 분석

강사님 코드는 다음 학습 내용을 하나의 파일에서 빠르게 실습하도록 구성되어 있습니다.

- 주요 `input` 타입
- `value`, `placeholder`
- `readonly`, `disabled`
- `button`, `submit`
- 체크박스와 라디오
- `select`, `multiple`
- `label`
- `textarea`
- `reset`
- 날짜, 시간, 숫자, 범위 입력
- GET과 POST
- 외부 검색 폼

코드를 직접 실행하면서 각 요소가 화면에서 어떻게 동작하는지 확인하기에 적합합니다.

# 32. 내 코드 vs 강사님 코드

| 비교 항목 | 내 코드 | 강사님 코드 |
| --- | --- | --- |
| 주석 | 개념과 관찰 내용이 상세함 | 핵심 설명 중심 |
| `form` 중첩 주의 | 직접 기록함 | 코드에서는 중첩하지 않음 |
| `readonly` / `disabled` | 전송 차이를 설명함 | 각 요소를 실습함 |
| 잘못된 속성 실습 | `value123`을 작성해 결과 확인 | 올바른 `value` 사용 |
| 라디오 `checked` | 성별 그룹은 하나만 선택되도록 수정 | 성별 두 항목 모두 `checked` |
| `textarea` | 태그 사이 공백 문제를 일부 개선 | `<br>`과 주석이 그대로 들어가는 예 포함 |
| POST | Live Server의 405 가능성을 설명 | POST 폼 자체를 실습 |
| 학습 성격 | 복습 주석이 풍부함 | 수업 진행용 예제 중심 |

# 33. 강사님 코드에서 주의해서 볼 부분

## 33.1 같은 라디오 그룹에 두 개의 `checked`

강사님 코드에는 다음 형태가 있습니다.

```html
<input
  type="radio"
  name="gender"
  value="여자"
  checked
>
여자

<input
  type="radio"
  name="gender"
  value="남자"
  checked
>
남자
```

같은 `name` 그룹에서는 하나만 선택할 수 있으므로 일반적으로 뒤쪽 항목이 선택된 상태로 나타납니다.

이는 브라우저 동작을 확인하기 위한 실습으로 볼 수 있지만, 실제 코드에서는 하나에만 `checked`를 작성합니다.

## 33.2 `textarea` 내부의 `<br>`과 주석

```html
<textarea>
  미리 보여줄 글<br>
  <!-- 주석 -->
</textarea>
```

`textarea` 내부에서는 `<br>`과 주석이 HTML로 처리되지 않고 입력값의 일부가 될 수 있습니다.

실제 초기값은 텍스트만 작성합니다.

```html
<textarea name="message">미리 보여줄 글</textarea>
```

## 33.3 `action` 오타가 있는 주석

강사님 코드 주석에는 `acrion`이라고 적힌 부분이 있습니다.

정확한 속성명은 `action`입니다.

```html
<form action="/submit">
```

문서화할 때는 원본의 오타를 그대로 정답처럼 옮기지 않고, 어떤 부분이 오타인지 명시해 수정해야 합니다.

# 34. 권장 통합 예제: 회원가입 폼

```html
<form action="/members" method="post">
  <div class="form-field">
    <label for="member-id">아이디</label>
    <input
      type="text"
      id="member-id"
      name="userId"
      minlength="4"
      maxlength="20"
      autocomplete="username"
      required
    >
  </div>

  <div class="form-field">
    <label for="member-password">비밀번호</label>
    <input
      type="password"
      id="member-password"
      name="password"
      minlength="8"
      autocomplete="new-password"
      required
    >
  </div>

  <fieldset>
    <legend>관심 분야</legend>

    <label>
      <input
        type="checkbox"
        name="interests"
        value="frontend"
      >
      프론트엔드
    </label>

    <label>
      <input
        type="checkbox"
        name="interests"
        value="backend"
      >
      백엔드
    </label>

    <label>
      <input
        type="checkbox"
        name="interests"
        value="ai"
      >
      AI
    </label>
  </fieldset>

  <fieldset>
    <legend>수신 동의</legend>

    <label>
      <input
        type="radio"
        name="receiveEmail"
        value="yes"
        checked
      >
      동의
    </label>

    <label>
      <input
        type="radio"
        name="receiveEmail"
        value="no"
      >
      거부
    </label>
  </fieldset>

  <div class="form-field">
    <label for="introduction">자기소개</label>
    <textarea
      id="introduction"
      name="introduction"
      rows="6"
      maxlength="500"
      placeholder="500자 이내로 입력하세요"
    ></textarea>
  </div>

  <button type="submit">가입하기</button>
  <button type="button">취소</button>
</form>
```

# 35. `fieldset`과 `legend`

관련 입력 항목을 하나의 그룹으로 묶을 때 사용합니다.

```html
<fieldset>
  <legend>배송 방법</legend>

  <label>
    <input
      type="radio"
      name="delivery"
      value="standard"
    >
    일반 배송
  </label>

  <label>
    <input
      type="radio"
      name="delivery"
      value="express"
    >
    빠른 배송
  </label>
</fieldset>
```

| 요소 | 역할 |
| --- | --- |
| `fieldset` | 관련 폼 요소 그룹 |
| `legend` | 그룹의 제목 |

라디오 버튼이나 체크박스처럼 여러 항목이 하나의 질문에 속할 때 특히 유용합니다.

# 36. 폼 접근성 체크리스트

폼을 작성할 때 다음 항목을 확인합니다.

1. 모든 중요한 입력 요소에 항목 이름이 있는가?
2. `label`과 입력 요소가 연결되어 있는가?
3. `id`가 중복되지 않는가?
4. 체크박스와 라디오 버튼의 그룹 의미가 명확한가?
5. 오류 메시지가 어떤 입력에서 발생했는지 알 수 있는가?
6. 색상만으로 필수·오류 상태를 구분하지 않는가?
7. 키보드만으로 모든 입력과 버튼을 사용할 수 있는가?
8. 버튼 문구가 동작을 구체적으로 설명하는가?
9. `placeholder`를 `label` 대신 사용하지 않았는가?
10. 필수 입력을 시각적 표시와 HTML 속성으로 함께 안내하는가?

# 37. 폼 보안과 서버 검증

HTML 속성은 사용자의 입력을 돕지만 보안을 완성하지 않습니다.

다음 값은 모두 조작될 수 있습니다.

- `readonly`
- `disabled`
- `hidden`
- `min`
- `max`
- `required`
- `pattern`
- `value`

사용자는 개발자 도구나 직접 요청을 만들어 서버에 임의의 값을 보낼 수 있습니다.

서버에서는 반드시 다음을 수행해야 합니다.

- 필수값 확인
- 데이터 타입 확인
- 길이와 범위 확인
- 허용된 값인지 확인
- 인증 사용자 확인
- 권한 확인
- SQL 인젝션 등 공격 방어
- 출력 시 안전한 이스케이프 처리

# 38. 자주 하는 실수

## 38.1 `name` 누락

```html
<input type="text" id="nickname">
```

화면에는 입력되지만 폼 전송 키가 없습니다.

```html
<input
  type="text"
  id="nickname"
  name="nickname"
>
```

## 38.2 `id`와 `name`을 같은 개념으로 생각함

`id`는 문서 안에서 요소를 식별하고 `label`, CSS, JavaScript 연결에 사용합니다.

`name`은 폼 전송에서 서버가 값을 구분하는 키입니다.

```html
<label for="user-id">아이디</label>
<input
  type="text"
  id="user-id"
  name="userId"
>
```

두 값은 같아도 되고 달라도 되지만 역할은 다릅니다.

## 38.3 일반 버튼의 `type` 누락

```html
<form>
  <button>주소 검색</button>
</form>
```

의도하지 않게 폼이 제출될 수 있습니다.

```html
<button type="button">주소 검색</button>
```

## 38.4 라디오 버튼의 `name`이 서로 다름

```html
<input type="radio" name="gender-female">
<input type="radio" name="gender-male">
```

둘 다 선택될 수 있습니다.

```html
<input type="radio" name="gender" value="female">
<input type="radio" name="gender" value="male">
```

## 38.5 `disabled` 값이 전송될 것이라고 생각함

```html
<input
  type="text"
  name="grade"
  value="VIP"
  disabled
>
```

일반적인 폼 전송에서는 제외됩니다.

## 38.6 `textarea`에 `value` 사용

```html
<!-- 잘못된 사용 -->
<textarea value="초기값"></textarea>
```

초기값은 태그 사이에 작성합니다.

```html
<textarea>초기값</textarea>
```

## 38.7 체크박스에 `value` 누락

```html
<input type="checkbox" name="agree">
```

선택 시 의미가 불명확한 `on`이 전달될 수 있습니다.

```html
<input
  type="checkbox"
  name="agree"
  value="terms"
>
```

# 39. 디버깅 방법

## 39.1 주소창 확인

GET 폼을 제출한 뒤 주소의 쿼리 문자열을 확인합니다.

```text
?keyword=HTML&page=1
```

## 39.2 개발자 도구 Network 탭

1. 개발자 도구를 연다.
2. Network 탭으로 이동한다.
3. 폼을 제출한다.
4. 생성된 요청을 선택한다.
5. 요청 방식, URL, Payload를 확인한다.

## 39.3 Elements 탭

- `name`이 누락되지 않았는가?
- `disabled` 상태인가?
- `label for`와 `input id`가 일치하는가?
- `button type`이 올바른가?
- 같은 `id`가 중복되지 않았는가?

## 39.4 HTML 검사

화면이 정상처럼 보여도 다음 오류가 있을 수 있습니다.

- 알 수 없는 속성
- 잘못된 태그 중첩
- 중복 `id`
- 닫는 태그 누락
- 잘못된 폼 구조

# 40. 실무 개선 예제

## 40.1 검색 폼

```html
<form
  class="search-form"
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
    placeholder="강의명을 입력하세요"
    required
  >

  <button type="submit">
    검색
  </button>
</form>
```

## 40.2 문의 폼

```html
<form action="/inquiries" method="post">
  <div>
    <label for="inquiry-title">제목</label>
    <input
      type="text"
      id="inquiry-title"
      name="title"
      maxlength="100"
      required
    >
  </div>

  <div>
    <label for="inquiry-email">답변 받을 이메일</label>
    <input
      type="email"
      id="inquiry-email"
      name="email"
      autocomplete="email"
      required
    >
  </div>

  <div>
    <label for="inquiry-content">문의 내용</label>
    <textarea
      id="inquiry-content"
      name="content"
      rows="10"
      required
    ></textarea>
  </div>

  <button type="submit">문의 등록</button>
</form>
```

# 41. 면접·복습 포인트

## Q1. `id`와 `name`의 차이는 무엇인가요?

`id`는 문서에서 요소를 식별하고 `label`, CSS, JavaScript와 연결할 때 사용합니다. `name`은 폼 전송 시 서버가 값을 구분하는 키입니다.

## Q2. `readonly`와 `disabled`의 가장 중요한 차이는 무엇인가요?

둘 다 사용자가 수정할 수 없지만, `readonly` 값은 일반적으로 전송되고 `disabled` 값은 전송되지 않습니다.

## Q3. 체크박스와 라디오 버튼의 차이는 무엇인가요?

체크박스는 여러 항목을 동시에 선택하거나 아무것도 선택하지 않을 수 있습니다. 라디오 버튼은 같은 `name` 그룹 안에서 하나만 선택합니다.

## Q4. 폼 안의 `button` 기본 타입은 무엇인가요?

`submit`입니다. 제출 목적이 아닌 버튼은 `type="button"`을 명시해야 합니다.

## Q5. POST는 왜 무조건 안전한 방식이 아닌가요?

주소창에 값이 보이지 않을 뿐 자동 암호화되는 것은 아닙니다. HTTPS, 인증, 권한 확인, 서버 검증이 함께 필요합니다.

## Q6. `placeholder`를 `label` 대신 사용하면 안 되는 이유는 무엇인가요?

사용자가 입력을 시작하면 안내 문구가 사라져 항목의 목적을 확인하기 어렵고 접근성도 나빠질 수 있습니다.

## Q7. 왜 서버에서도 입력값을 검증해야 하나요?

HTML 속성과 JavaScript 검증은 사용자가 우회하거나 조작할 수 있기 때문입니다.

# Problems

## 문제 1. 기본 입력 폼

이름을 입력받고 제출하는 폼을 작성하세요.

조건:

- `label`을 사용한다.
- `input type="text"`를 사용한다.
- `name="username"`을 지정한다.
- 제출 버튼을 만든다.

## 문제 2. `readonly`와 `disabled`

다음 요구사항을 만족하는 입력 요소를 작성하세요.

- 회원 아이디는 수정할 수 없지만 서버로 전송한다.
- 회원 등급은 화면에 보이지만 서버로 전송하지 않는다.

## 문제 3. 체크박스

다음 관심 분야 중 여러 개를 선택할 수 있도록 작성하세요.

- HTML
- CSS
- JavaScript

모든 항목의 `name`은 `skills`로 통일하고 의미 있는 `value`를 지정하세요.

## 문제 4. 라디오 버튼

배송 방식을 하나만 선택하도록 작성하세요.

- 일반 배송
- 빠른 배송

`일반 배송`이 기본 선택되도록 작성하세요.

## 문제 5. `label` 연결

다음 코드의 문제를 찾아 수정하세요.

```html
<label for="email">이메일</label>
<input type="email" id="user-email" name="email">
```

## 문제 6. 선택 목록

한식, 중식, 양식 중 하나를 선택하는 `select`를 작성하세요.

조건:

- `name="food"`를 사용한다.
- 화면에는 한국어가 보인다.
- 서버에는 `korean`, `chinese`, `western`이 전달된다.
- 한식이 기본 선택된다.

## 문제 7. 문의 내용

여러 줄 문의 내용을 입력받는 요소를 작성하세요.

조건:

- `label`을 연결한다.
- `name="message"`를 사용한다.
- 8줄 높이를 사용한다.
- `문의 내용을 입력하세요`를 안내 문구로 표시한다.

## 문제 8. 잘못된 버튼 수정

다음 코드는 주소 검색 버튼을 누르면 폼이 제출됩니다.

```html
<form>
  <input type="text" name="address">
  <button>주소 검색</button>
  <button type="submit">가입하기</button>
</form>
```

주소 검색 버튼이 폼을 제출하지 않도록 수정하세요.

## 문제 9. GET 검색 폼

구글 검색 폼을 작성하세요.

조건:

- 전송 방식은 GET이다.
- 전송 주소는 `https://www.google.com/search`이다.
- 검색어의 `name`은 `q`이다.
- 새 탭에서 결과를 연다.

## 문제 10. 전송 결과 예측

다음 폼에서 사용자가 노래에 `Dynamite`, 가수에 `BTS`를 입력하고 제출했습니다.

```html
<form method="get" action="/search">
  <input type="text" name="song">
  <input type="text">
  <input type="text" name="singer">
  <button type="submit">검색</button>
</form>
```

생성될 가능성이 높은 URL을 작성하세요.

## 문제 11. 오류 찾기

다음 코드에서 문제를 모두 찾아 수정하세요.

```html
<form>
  <label for="agree">약관 동의</label>
  <input
    type="checkbox"
    id="agreement"
    name="agree"
  >

  <textarea value="문의 내용"></textarea>

  <button>주소 찾기</button>
</form>
```

## 문제 12. 종합 회원가입 폼

다음 요소를 포함하는 회원가입 폼을 작성하세요.

- 아이디
- 비밀번호
- 이메일
- 관심 분야 체크박스 3개
- 이메일 수신 여부 라디오 버튼
- 자기소개
- 가입 버튼
- 취소 버튼

접근성을 고려해 `label`, `fieldset`, `legend`를 사용하세요.

# Answers & Explanations

## 정답 1

```html
<form>
  <label for="username">이름</label>
  <input
    type="text"
    id="username"
    name="username"
  >
  <button type="submit">제출</button>
</form>
```

`label for`와 `input id`를 일치시켰습니다.

## 정답 2

```html
<input
  type="text"
  name="memberId"
  value="user01"
  readonly
>

<input
  type="text"
  name="memberGrade"
  value="일반 회원"
  disabled
>
```

`readonly`는 전송되고 `disabled`는 일반적으로 전송되지 않습니다.

## 정답 3

```html
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
```

같은 `name`으로 여러 값을 전달할 수 있습니다.

## 정답 4

```html
<label>
  <input
    type="radio"
    name="delivery"
    value="standard"
    checked
  >
  일반 배송
</label>

<label>
  <input
    type="radio"
    name="delivery"
    value="express"
  >
  빠른 배송
</label>
```

같은 `name`이므로 하나만 선택됩니다.

## 정답 5

```html
<label for="user-email">이메일</label>
<input
  type="email"
  id="user-email"
  name="email"
>
```

`for`와 `id` 값이 일치해야 합니다.

## 정답 6

```html
<label for="food">음식 종류</label>
<select id="food" name="food">
  <option value="korean" selected>한식</option>
  <option value="chinese">중식</option>
  <option value="western">양식</option>
</select>
```

사용자에게 보이는 텍스트와 서버 전송 값은 다르게 지정할 수 있습니다.

## 정답 7

```html
<label for="message">문의 내용</label>
<textarea
  id="message"
  name="message"
  rows="8"
  placeholder="문의 내용을 입력하세요"
></textarea>
```

`textarea`의 안내 문구는 `placeholder`를 사용합니다.

## 정답 8

```html
<form>
  <input type="text" name="address">
  <button type="button">주소 검색</button>
  <button type="submit">가입하기</button>
</form>
```

일반 동작 버튼은 `type="button"`을 지정합니다.

## 정답 9

```html
<form
  method="get"
  action="https://www.google.com/search"
  target="_blank"
>
  <label for="q">검색어</label>
  <input
    type="search"
    id="q"
    name="q"
  >
  <button type="submit">구글 검색</button>
</form>
```

구글 검색은 `q`라는 검색어 키를 사용합니다.

## 정답 10

```text
/search?song=Dynamite&singer=BTS
```

두 번째 입력 요소는 `name`이 없으므로 일반적인 폼 전송 데이터에서 제외됩니다.

## 정답 11

```html
<form>
  <label for="agreement">약관 동의</label>
  <input
    type="checkbox"
    id="agreement"
    name="agree"
    value="yes"
  >

  <label for="message">문의 내용</label>
  <textarea
    id="message"
    name="message"
  >문의 내용</textarea>

  <button type="button">주소 찾기</button>
</form>
```

수정한 내용:

1. `label for`를 `id`와 일치시켰다.
2. 체크박스에 의미 있는 `value`를 추가했다.
3. `textarea`의 초기값을 태그 사이에 작성했다.
4. 일반 버튼에 `type="button"`을 지정했다.
5. `textarea`에도 `label`과 `name`을 추가했다.

## 정답 12

```html
<form action="/members" method="post">
  <div>
    <label for="user-id">아이디</label>
    <input
      type="text"
      id="user-id"
      name="userId"
      required
    >
  </div>

  <div>
    <label for="password">비밀번호</label>
    <input
      type="password"
      id="password"
      name="password"
      required
    >
  </div>

  <div>
    <label for="email">이메일</label>
    <input
      type="email"
      id="email"
      name="email"
      required
    >
  </div>

  <fieldset>
    <legend>관심 분야</legend>

    <label>
      <input
        type="checkbox"
        name="interests"
        value="html"
      >
      HTML
    </label>

    <label>
      <input
        type="checkbox"
        name="interests"
        value="css"
      >
      CSS
    </label>

    <label>
      <input
        type="checkbox"
        name="interests"
        value="javascript"
      >
      JavaScript
    </label>
  </fieldset>

  <fieldset>
    <legend>이메일 수신 여부</legend>

    <label>
      <input
        type="radio"
        name="receiveEmail"
        value="yes"
        checked
      >
      동의
    </label>

    <label>
      <input
        type="radio"
        name="receiveEmail"
        value="no"
      >
      거부
    </label>
  </fieldset>

  <div>
    <label for="introduction">자기소개</label>
    <textarea
      id="introduction"
      name="introduction"
      rows="6"
    ></textarea>
  </div>

  <button type="submit">가입하기</button>
  <button type="button">취소</button>
</form>
```

# 핵심 요약

- `form`은 사용자 입력값을 서버로 전달하는 범위를 정의한다.
- 폼 데이터의 기본 구조는 `name=value`이다.
- 입력 요소에 `name`이 없으면 일반적인 폼 전송에 포함되지 않는다.
- `value`는 실제 값이고 `placeholder`는 입력 안내 문구이다.
- `readonly` 값은 전송되지만 `disabled` 값은 일반적으로 전송되지 않는다.
- 체크박스는 여러 개를 선택할 수 있고, 라디오는 같은 `name` 그룹에서 하나만 선택한다.
- `label`은 감싸거나 `for`와 `id`를 맞춰 입력 요소와 연결한다.
- `textarea` 초기값은 태그 사이에 작성하며 내부 HTML은 렌더링되지 않는다.
- `button`은 폼 내부에서 기본 타입이 `submit`이므로 일반 버튼은 `type="button"`을 지정한다.
- GET은 주로 조회와 검색에, POST는 생성과 변경 요청에 사용한다.
- POST도 HTTPS와 서버 검증이 없으면 안전하지 않다.
- HTML 검증은 사용자 편의를 위한 1차 검증이며 서버 검증을 대신하지 못한다.
- 화면이 정상적으로 보이더라도 속성 오타와 잘못된 구조가 없는지 개발자 도구와 검사기로 확인해야 한다.
