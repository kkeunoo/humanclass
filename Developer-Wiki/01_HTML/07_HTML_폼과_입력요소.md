# 폼과 입력요소 — 화면의 이름표·입력값·제출 이름을 구분하기

[HTML 목차](README.md) · [이전: 이미지](06_HTML_이미지와_미디어.md) · [다음: 폼 전송](07-02_HTML_폼_전송과_GET_POST.md)

입력창에 글자가 보인다고 그 글자가 모두 전송되는 것은 아니다. 체크박스 옆의 글자가 자동으로 값이 되는 것도 아니다. 이 장은 **사용자에게 보이는 안내, 현재 입력 상태, 전송할 이름과 값**을 나눠 읽고 다음 장의 요청 구성으로 연결한다.

<a id="chapter-toc"></a>

**목차:** [1 준비](#learn) · [2 개념·상태](#concepts) · [3 전체 예제](#example) · [4 내 코드](#my-code) · [5 전송과 연결](#connections) · [6 검토·개선](#review) · [7 강사님 비교](#teacher) · [8 확인](#results) · [9 TIP](#tips) · [10 복습](#practice)

<a id="learn"></a>

## 1. 이번 장에서 배울 것

| 조건 | 내용 |
| --- | --- |
| 실제 수업 파일 | 양쪽 `workspace_html/07_form.html` |
| 배운 요소 | form, input, button, select·option, label, textarea |
| 새 실행 자료 | [실습/07_입력_복습.html](실습/07_입력_복습.html) |
| 이 장의 실행 | 로컬 파일로 입력·선택·초기화 상태 관찰 가능 |
| 다음 장의 확인 | HTTP에서 요청 방식·대상·이름과 값 확인 |
| 시작 상태 | 파일을 새로 열고 입력을 바꾸기 전의 value·checked·selected |

브라우저가 이전 입력을 복원하거나 자동 완성하면 시작 상태가 코드와 다르게 보일 수 있다. 초기화 버튼으로 초기 상태를 비교하고, 결과를 적을 때는 **코드의 초기 상태인지 사용자가 바꾼 상태인지** 표시한다. form을 여러 개 작성할 수 있지만 form 안에 form을 중첩하지 않는다.

<a id="concepts"></a>
<a id="text"></a>

## 2. 개념부터 이해하기

### 2.1 입력창을 읽는 네 가지 이름

```html
<!-- 설명용 새 예제 · form 안의 조각 -->
<label for="student-name">이름</label>
<input id="student-name" type="text" name="student" value="학습자" placeholder="이름 입력">
```

| 부분 | 무엇을 정하는가? | 이 예제 |
| --- | --- | --- |
| label의 글자 | 사용자에게 보여 줄 이름표 | 이름 |
| id | 문서 안에서 요소를 구별하는 식별자 | student-name |
| label의 for | 어느 id의 입력과 연결할지 | student-name |
| name | 제출할 데이터의 이름 | student |
| value | 입력의 초기 내용 | 학습자 |
| placeholder | 값이 비었을 때 보일 안내 | 이름 입력 |

id가 있다고 제출 이름 name이 자동으로 생기지 않는다. label의 for는 **id에 맞추는 것**이고 name에 맞추는 것이 아니다. 이 구별을 알면 ‘화면의 이름을 바꿨는데 서버에서 읽는 이름은 왜 그대로인가’를 설명할 수 있다.

### 2.2 초기값과 안내, 현재값

처음에는 `학습자`가 실제 값으로 보이고 placeholder는 보이지 않는다. 사용자가 값을 지우면 `이름 입력`이라는 안내가 보이지만 그 글자가 값으로 들어간 것은 아니다. 사용자가 `새이름`을 입력하면 현재 값은 그 글자다.

| 시점 | 보이는 것 | 실제 현재 입력값 |
| --- | --- | --- |
| 처음 | 학습자 | 학습자 |
| 내용 전부 삭제 | 이름 입력이라는 안내 | 빈 값 |
| 새 글자 입력 | 새이름 | 새이름 |

`type="password"`도 수업에 있다. 입력 글자를 가려 표시하는 타입이며, 전송·저장의 암호화까지 구현하는 기능이 아니다. 화면 표시와 데이터 처리의 역할을 구별한다.

<a id="state"></a>

### 2.3 읽기 전용과 비활성은 다르다

readonly와 disabled는 둘 다 값을 일반적으로 고칠 수 없게 보일 수 있지만, 기능과 제출 조건이 다르다. 아래는 비교하기 위해 **name을 추가한 새 예제**다.

```html
<input type="text" name="fixed" value="A" readonly>
<input type="text" name="off" value="B" disabled>
```

| 상태 | 화면에서의 조작 | 일반 폼 제출에서 |
| --- | --- | --- |
| readonly인 텍스트 | 값 편집 불가 | 이름 등 조건이 맞으면 fixed=A 포함 |
| disabled | 일반 상호작용 불가 | off=B 제외 |

원본의 두 입력에는 name이 없다. 따라서 원본 그대로에서 ‘readonly라 제출된다’고 결론 내릴 수 없다. **읽기 전용이어도 제출 이름과 다른 조건이 있어야 한다.** 또한 readonly를 모든 입력 타입에 적용할 수 있는 것은 아니므로 체크박스를 잠그는 일반 규칙으로 쓰지 않는다.

> 📚 **출처 · 본문 설명 확인:** [MDN — readonly](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/readonly), [disabled](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/disabled)로 적용 범위와 제출 차이를 확인했다. 수업 코드의 name 누락도 함께 대조한다.

<a id="choice"></a>

### 2.4 체크박스와 라디오에서 그룹과 값 읽기

체크박스는 여러 개를 고를 수 있고, 이 수업처럼 같은 폼·같은 name을 가진 라디오는 한 그룹에서 하나를 선택한다. **보이는 글자와 제출 값은 따로 지정**한다.

| 표기 | 뜻 |
| --- | --- |
| `name="coffee"` | 선택값을 담을 이름 |
| `value="2"` | 이 항목을 골랐을 때 보낼 값 |
| `checked` | 초기 선택 상태 |
| 선택 안 됨 | 해당 체크박스·라디오는 제출 목록에서 제외 |
| value가 없는 선택 항목 | 기본 제출 값 on |

checked가 초기 상태라는 말은 이후 사용자의 선택을 무시하고 언제나 제출한다는 뜻이 아니다. 현재 선택 상태를 기준으로 본다. value가 없으면 옆의 ‘얼음추가’ 글자가 자동으로 전송되는 것도 아니다.

<a id="other"></a>

### 2.5 select·label·textarea

select 안의 option은 **보여 줄 글자**와 **보낼 값**을 나눌 수 있다. `<option value="4" selected>분식</option>`이면 초기 선택의 제출 값은 분식이라는 글자 대신 4다. multiple은 여러 선택, size는 보이는 행 수다. name이 없으면 선택 목록 자체의 제출 이름이 없다.

label은 input을 감싸거나 for·id를 맞춰 연결할 수 있다. 글자를 클릭해도 연결된 체크박스에 작용하므로 작은 네모만 겨냥할 필요가 줄어든다. 실제 파일에서 for와 id가 같은지 확인한다.

textarea의 초기 내용은 input의 value 속성과 다르게 **시작·종료 태그 사이**에 적는다.

```html
<textarea name="memo" rows="3" cols="30" placeholder="메모 입력">오늘 배운 내용</textarea>
```

rows·cols는 보이는 크기를 정하는 정보이며 최대 글자 수 제한이 아니다. 그 사이에 적은 불필요한 들여쓰기·줄바꿈도 초기 텍스트에 영향을 줄 수 있다. textarea 안의 `<br>`는 일반 본문처럼 줄바꿈 태그로 작동하지 않고 글자로 보이는 문맥이라는 점도 원본의 실험과 연결한다.

> 📚 **출처 · 본문 설명 확인:** label 연결은 [HTML 표준 — Forms](https://html.spec.whatwg.org/multipage/forms.html), select·option·textarea는 [Form elements](https://html.spec.whatwg.org/multipage/form-elements.html)로 확인했다.

<a id="button"></a>

### 2.6 버튼과 다른 수업 입력 타입

| 종류 | 하는 일 | 글자를 적는 곳 |
| --- | --- | --- |
| input type=button | 기본 제출 기능 없는 버튼 | value |
| button type=button | 기본 제출 기능 없는 버튼 | 요소 안의 내용 |
| submit | 폼 제출 | input은 value, button은 안의 내용 |
| reset | 초기 value·checked·selected 상태 복원 | input이면 value |

이 수업의 일반 form 안에서 type을 생략한 button은 제출 버튼으로 동작하므로 의도를 명시하면 읽기 쉽다. 일반 button에 별도 기능을 연결하지 않으면 눌러도 화면 변화가 없을 수 있다. input은 안쪽 콘텐츠를 갖지 않지만 button은 이미지 등 내용을 담을 수 있다.

| 수업에 있는 타입 | 확인할 것 |
| --- | --- |
| color | 색 선택값과 표시 UI |
| date·time | 날짜·시간 값; 보이는 UI는 환경별 차이 |
| number | 숫자 입력; 편집 중 허용 문자와 최종 유효한 값 구별 |
| range | min·max·step에 따른 범위와 간격 |

원본의 range는 min 10, max 100, step 10이다. 새 예제에는 value 50도 명시해 시작 상태를 분명히 했다. number 입력에 환경에 따라 `e`가 들어갈 수 있다는 관찰을 ‘숫자 타입인데 글자는 무조건 입력 불가’라는 규칙과 구별한다.

> 📚 **출처 · 본문 설명 확인:** 입력 타입·초기 선택·불리언 속성은 [HTML 표준 — Input](https://html.spec.whatwg.org/multipage/input.html), 버튼의 역할은 [Form elements](https://html.spec.whatwg.org/multipage/form-elements.html)로 확인했다.

<a id="example"></a>

## 3. 작은 예제와 결과

**설명용 새 예제 · 전체 문서.** [07_입력_복습.html](실습/07_입력_복습.html)은 배운 요소의 상태를 비교하는 파일이다. 전송 뒤 내용을 자동 저장하거나 응답에 값 목록을 출력하는 서버 구현은 없다.

```html
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <title>입력 상태 복습</title>
</head>
<body>
    <h1>입력과 선택</h1>
    <form action="07_입력_복습.html" method="get">
        <p><label for="student-name">이름</label>
            <input id="student-name" type="text" name="student" value="학습자" placeholder="이름 입력"></p>
        <p><label>읽기 전용 <input type="text" name="fixed" value="A" readonly></label></p>
        <p><label>비활성 <input type="text" name="off" value="B" disabled></label></p>
        <h2>여러 개 고르는 옵션</h2>
        <p><label><input type="checkbox" name="coffee" value="1">샷추가</label>
            <label><input type="checkbox" name="coffee" value="2" checked>펄추가</label>
            <label><input type="checkbox" name="coffee" value="3" disabled>휘핑크림</label>
            <label><input type="checkbox" name="coffee" value="5">얼음추가</label></p>
        <h2>하나 고르는 방식</h2>
        <p><label><input type="radio" name="mode" value="online" checked>온라인</label>
            <label><input type="radio" name="mode" value="offline">오프라인</label></p>
        <p><label>과목
            <select name="course">
                <option value="html" selected>HTML</option>
                <option value="css">CSS</option>
            </select></label></p>
        <p><label>메모 <textarea name="memo" rows="3" cols="30">복습</textarea></label></p>
        <p><label>날짜 <input type="date" name="day" value="2026-06-24"></label></p>
        <p><label>시간 <input type="time" name="start" value="09:00"></label></p>
        <p><label>숫자 <input type="number" name="count" value="2"></label></p>
        <p><label>범위 <input type="range" name="hours" min="10" max="100" step="10" value="50"></label></p>
        <p><label>색 <input type="color" name="theme" value="#336699"></label></p>
        <button type="button">일반 버튼</button>
        <button type="submit">전송</button>
        <input type="reset" value="초기 상태로">
    </form>
</body>
</html>
```

**초기 상태 기준 예상:** 이름은 학습자, 펄추가만 체크, 온라인·HTML 선택, 메모 복습, 날짜와 다른 입력은 적힌 초기값을 사용한다. 읽기 전용 A는 편집하지 못하고 비활성 B는 일반 조작 대상에서 빠진다. 전송 항목의 정확한 구성은 다음 장에서 읽는다.

**하나만 바꾸는 실험:** 이름을 모두 지워 placeholder를 본 뒤 초기화 버튼을 누른다. 빈 상태로만 돌아가는 것이 아니라 value에 적힌 학습자로 돌아간다. 체크박스를 바꾼 뒤 초기화하면 checked로 적은 펄추가가 다시 초기 선택이 된다. 다른 문법을 추가하지 않고 **현재값과 초기값의 차이**를 관찰한다.

<a id="my-code"></a>

## 4. 내 코드 따라 읽기

### 4.1 실제 초기값 입력

**내 코드 · 원본 발췌** — `workspace_html/07_form.html` 18행.

```html
            text(value) : <input type="text" name="val" value="초기값"><br>
```

전송 이름은 val, 초기값은 초기값이다. 앞의 `text(value)`라는 화면 글자가 제출 이름이 되는 것이 아니다. 같은 파일의 placeholder 입력과 비교하면서 주석의 ‘회색 초기값’은 **빈 입력 안내**라고 더 정확히 읽는다.

### 4.2 내가 값을 명시한 체크박스

**내 코드 · 원본 발췌** — 같은 파일 52–56행.

```html
            <input type="checkbox" name="coffee" value="1">샷추가
            <input type="checkbox" name="coffee" value="2" checked>펄추가
            <input type="checkbox" name="coffee" value="3" disabled>휘핑크림추가
            <input type="checkbox" name="coffee" value="4" >시럽추가
            <input type="checkbox" name="coffee" value="5" >얼음추가
```

같은 name의 체크박스를 여러 개 고를 수 있다. 초기에는 value 2인 항목만 checked다. value 3은 disabled이므로 일반 제출에서 제외된다. 마지막도 value 5를 명시해 얼음 선택을 구별할 수 있다.

### 4.3 초기 선택 하나를 둔 라디오

**내 코드 · 원본 발췌** — 같은 파일 66–67행.

```html
            <input type="radio" name="gender" value="여자" checked>여자
            <input type="radio" name="gender" value="남자">남자
```

두 요소가 같은 gender 그룹이고 여자 항목 하나에 초기 선택을 지정했다. 같은 폼의 china 그룹은 name이 달라 별도 그룹이다. 원본 china 항목들은 value가 없어 선택한 음식 이름이 자동으로 값이 되지 않는다는 점도 함께 확인한다.

<a id="connections"></a>

## 5. 다른 파일과 연결하기

입력 요소는 값을 편집·선택하는 화면을 만든다. 그 값이 다른 코드로 넘어가려면 form의 대상·방식·제출 조건이 맞아야 한다. 다음 장의 연결은 다음 순서다.

```text
HTML 초기값
  → 사용자 입력·선택
  → 제출 가능한 name과 현재값 고르기
  → action 주소로 method 방식의 요청
  → 받는 쪽의 처리와 응답
```

새 예제는 자기 HTML 파일을 GET 대상으로 삼는다. 다시 문서가 열린다고 서버가 입력값을 저장했다는 뜻은 아니다. 폼 데이터를 처리하는 Python 함수나 DB는 현재 파일에 없다. 그런 구현이 나오는 FastAPI 단원에서 name이 함수 입력과 어떻게 연결되는지 추적한다.

<a id="review"></a>

## 6. 내 코드 돌아보기

초기값·placeholder를 함께 시험하고, 체크박스 값과 라디오 초기 선택을 명시한 점은 좋다. 화면을 보면서도 어떤 값을 주고받을지 생각한 기록이다.

| 원본의 선택·표현 | 평가 종류 | 보완 |
| --- | --- | --- |
| 얼음추가에 value 5 명시 | 구별에 도움이 되는 선택 | 실제 제출 값이 어느 항목인지 명확 |
| 라디오 초기 checked 하나 | 의도가 명확한 선택 | 한 그룹에서 초기 선택 하나를 표시 |
| placeholder를 회색 초기값으로 설명 | 용어 보완 | 현재 값이 아닌 빈 상태 안내 |
| readonly는 서버로 간다는 주석 | 조건 누락 | 원본은 name이 없으므로 제출 조건 확인 |
| value123 속성 | 속성 오타 | 버튼 글자를 설정하려면 value 사용 |
| textarea는 모두 그대로 보임 | 설명 보완 | 해당 텍스트 문맥과 초기 공백을 확인 |

reset은 빈칸 만들기가 아니라 초기 상태 복원이다. 잘못 기억하면 편집한 뒤 버튼을 눌렀을 때 ‘왜 값이 남았지?’라고 오해한다. 실행 순서와 초기 속성을 나란히 기록하면 된다.

<a id="teacher"></a>

## 7. 강사님 코드에서 배울 점

체크박스 마지막 항목은 실제로 차이가 있으므로 그 한 줄만 본다.

**강사님 코드 · 비교에 필요한 발췌** — 대응 `07_form.html` 32행.

```html
        <input type="checkbox" name="coffee" >간얼음
```

value가 없어 그 항목을 선택해 제출하면 기본값 on이다. 내 원본은 마지막 항목을 value 5로 구별했다. 어떤 옵션인지 받는 쪽에서 분명히 알아야 한다면 **내 값 명시 방식이 이 목적에 더 맞는다.**

강사님 라디오 초기 선택에도 차이가 있다.

**강사님 코드 · 비교에 필요한 발췌** — 같은 파일 39–40행.

```html
        <input type="radio" name="gender" value="여자" checked>여자
        <input type="radio" name="gender" value="남자" checked>남자
```

같은 그룹에 checked가 둘 있어도 두 항목을 동시에 고르는 라디오가 되지 않는다. 이 원본처럼 뒤에 오는 checked 항목이 초기 선택이 되는 경우보다, 내 코드처럼 의도한 항목 하나만 명시하는 편이 읽기 명확하다. 출처에 따라 우열을 정하지 않고 실제 상태와 목적을 비교한다.

<a id="results"></a>

## 8. 결과와 확인 방법

| 현상 | 먼저 확인할 것 |
| --- | --- |
| 힌트는 보이는데 제출 값은 빈칸 | placeholder와 현재값을 혼동했는가? |
| 읽기 전용인데 값이 안 넘어감 | name·form 소속 등 다른 조건이 있는가? |
| disabled="false"인데 비활성 | 불리언 속성의 존재 여부 |
| 선택 음식 이름 대신 on | value를 명시했는가? |
| label 글자를 눌러도 연결 안 됨 | for와 id 일치, 중복 ID 여부 |
| textarea에 들여쓰기까지 보임 | 시작·종료 태그 사이의 초기 텍스트 |
| 초기화 뒤 값이 남음 | value·checked·selected의 초기 상태 |

정적 검사로 새 예제의 label 연결·이름·초기 속성·범위를 확인하고, 동작 결과는 코드와 HTML 규칙 기준으로 예상한다. 모든 브라우저의 날짜·색·숫자 입력 UI를 같은 모양으로 실행 확인한 것은 아니다. 현재 상태를 바꾼 뒤에는 초기 쿼리 예측과 결과가 달라질 수 있다.

<a id="tips"></a>

## 9. 추가로 알면 좋은 것

<a id="extra-02-3"></a>

> 💡 **TIP · 수업 범위 밖:** required·pattern 등 검증 속성, fieldset·legend로 입력을 묶는 방법은 더 공부할 수 있다. 하지만 새 속성의 상세 사용을 이 수업 원본의 기본 문제에 요구하지 않는다. 브라우저 검증과 서버 검증도 각각 별도로 이해해야 한다. [출처: HTML 표준 — Forms](https://html.spec.whatwg.org/multipage/forms.html).

> 🔗 **다음 학습:** name·현재값·선택 상태를 이해했으면 다음 장에서 어떤 항목이 요청에 포함되는지 확인한다. 입력창이 보이는 것, 요청을 보내는 것, 서버가 저장하는 것은 각각 확인할 단계다.

<a id="practice"></a>

## 10. 복습과 다음 학습

1. placeholder만 보이는 입력의 현재값은 그 안내 글자인가?
2. label의 for는 name과 id 중 무엇에 맞출까?
3. 한 가지 속성만 고쳐, readonly·disabled 비교 예제에서 이름 있는 비활성 입력을 활성화해 본다.

<details>
<summary>풀이</summary>

placeholder는 빈 입력의 안내라 현재값 자체가 아니다. for는 입력의 id에 맞춘다. 비활성을 해제하려면 disabled 속성을 제거한다. disabled="false"로 바꾸는 것은 끄는 표기가 아니다.

</details>

| 빠른 확인 | 의미 |
| --- | --- |
| id / name | 문서 식별자 / 제출 이름 |
| value / placeholder | 초기 실제 값 / 빈 상태 힌트 |
| checked / selected | 체크·라디오 초기 선택 / option 초기 선택 |
| readonly / disabled | 읽기 전용 / 일반 제출에서 제외되는 비활성 |
| textarea 초기값 | 시작·종료 태그 사이 |
| reset | 초기 상태 복원 |

외부 문서는 관련 문단에 출처를 표시했고 확인일은 2026-10-28이다. BACKUP 폼 문서의 사용 상황·속성별 상세 풀이를 참고하되 배운 범위는 양쪽 원본으로 대조했다.

[장별 문제](실습/연습문제/07_HTML_폼과_입력요소_연습문제.md) → [다음: GET·POST 전송](07-02_HTML_폼_전송과_GET_POST.md)

<!-- 이전 색인에서 사용하는 이동 주소 보존 -->
<a id="html-10"></a>
<a id="html-17"></a>
<a id="html-18"></a>
<a id="html-19"></a>
<a id="html-23"></a>
<a id="html-24"></a>
<a id="html-25"></a>
<a id="html-37"></a>
<a id="html-4"></a>
<a id="html-6"></a>
<a id="html-7"></a>
<a id="html-8"></a>
<a id="html-9"></a>
<a id="index-section-102"></a>
<a id="index-section-116"></a>
<a id="index-section-15"></a>
<a id="index-section-17"></a>
<a id="index-section-24"></a>
<a id="index-section-28"></a>
<a id="index-section-36"></a>
<a id="index-section-40"></a>
<a id="index-section-45"></a>
<a id="index-section-5"></a>
<a id="index-section-72"></a>
<a id="index-section-88"></a>
<a id="index-section-93"></a>

이전 절 주소로 왔다면 [이 장의 목차](#chapter-toc)에서 현재 설명을 찾을 수 있다.
