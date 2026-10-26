# 07. 폼 입력요소 — 보이는 값과 제출되는 값 구분하기

[HTML 읽기 안내](README.md) · [이전: 이미지와 미디어](06_HTML_이미지와_미디어.md) · [다음: 폼 전송](07-02_HTML_폼_전송과_GET_POST.md)

양쪽 `workspace_html/07_form.html`은 같은 화면에서 입력·선택·버튼을 실험한다. 이번 장에서는 각 요소의 상태를 읽고, 다음 장에서 실제 전송 내용을 연결한다. `form`은 제출할 입력들을 묶으며, `form` 안에 또 `form`을 중첩하지 않는다.

## 목차

1. [텍스트 입력과 초기값](#text)
2. [`readonly`와 `disabled`](#state)
3. [버튼의 종류](#button)
4. [체크박스·라디오 원본 비교](#choice)
5. [`select`·`label`·`textarea`](#other)
6. [나머지 수업 입력 타입과 복습](#practice)

<a id="text"></a>

## 1. `value`와 `placeholder`는 다르다

### 강사님 코드 — 원본 발췌

강사님 `workspace_html/07_form.html` 12~12행

```html
        text(value) : <input type="text" name="val" value="초기값"><br>
```

`name="val"`은 제출할 이름, `value="초기값"`은 이 입력의 초기 내용이다.

### 내 코드 — 원본 발췌

내 코드 `workspace_html/07_form.html` 18~18행

```html
            text(value) : <input type="text" name="val" value="초기값"><br>
```

이 줄의 동작은 같다. 나는 추가로 `value`와 `placeholder`를 함께 쓴 입력도 작성했다. 비교 실험을 통해 실제 값과 힌트를 구분할 수 있다.

설명용 재구성:

```html
<input type="text" name="nickname" value="학습자" placeholder="별명 입력">
```

처음에는 `학습자`가 값으로 보인다. 값을 모두 지우면 빈 상태의 안내인 `별명 입력`이 나타난다. 안내 글자가 입력값으로 자동 저장되는 것은 아니다.

| 설정 | 역할 | 흔한 오해 |
| --- | --- | --- |
| `type="text"` | 한 줄 텍스트 입력 | 생략해도 기본 텍스트 입력이지만 명시하면 읽기 쉬움 |
| `value` | 초기값 | placeholder와 같은 회색 안내가 아님 |
| `placeholder` | 빈 입력의 힌트 | 제출되는 값이나 영구적인 이름표가 아님 |
| `name` | 폼에 담아 보낼 이름 | `id`가 자동으로 대신하지 않음 |

원본의 `type="password"`는 입력 글자를 가려 보이게 한다. 화면에서 가려진다는 사실과 안전한 전송·저장은 별개의 문제다. HTML 입력 타입만으로 암호화가 구현되는 것은 아니다.

<a id="state"></a>

## 2. `readonly`와 `disabled`: 둘 다 못 고쳐도 제출은 다르다

원본 양쪽의 읽기 전용·비활성 입력에는 **`name`이 없다.** 따라서 원본 상태 그대로는 읽기 전용 값이 제출되는지 비교하기에 부족하다. 내 주석의 “readonly는 서버로 간다”에는 **제출 가능한 이름 등 조건을 갖춘 경우**라는 전제가 필요하다.

설명용 수정 — 비교를 위해 `name`을 추가했다.

```html
<form method="get">
    <input type="text" name="readonly_value" value="A" readonly>
    <input type="text" name="disabled_value" value="B" disabled>
    <button type="submit">상태 비교</button>
</form>
```

| 상태 | 화면에서 편집 | 위 예제의 제출 결과 |
| --- | --- | --- |
| `readonly` | 값 편집 불가 | `readonly_value=A` 포함 |
| `disabled` | 일반 상호작용 불가 | `disabled_value` 제외 |

적용 가능한 요소·타입이 서로 같지는 않다. 체크박스에 `readonly`를 붙여 잠그는 방식으로 확장하지 않는다. `readonly`·`disabled`도 불리언 속성이므로 `disabled="false"`를 “활성화”라고 읽지 않는다.

<a id="button"></a>

## 3. 버튼의 역할을 명시하기

| 수업 코드 | 클릭했을 때의 역할 | 버튼 글자를 적는 곳 |
| --- | --- | --- |
| `input type="button"` | 기본 제출 동작 없음 | `value` |
| `button type="button"` | 기본 제출 동작 없음 | 시작·종료 태그 사이 |
| `input type="submit"` | 폼 제출 | `value` |
| `button type="submit"` | 폼 제출 | 시작·종료 태그 사이 |
| `input type="reset"` | 폼 입력 상태를 초기값으로 되돌림 | `value` |

수업의 일반적인 `form` 안에서 `type`을 생략한 `<button>`은 제출 버튼으로 동작한다. 일반 버튼 의도라면 `type="button"`을 명시한다. 기능을 별도로 연결하지 않은 일반 버튼은 클릭해도 특별한 작업을 하지 않는다.

내 원본에는 `value123="전송"`이라는 오타 실험이 있다. 버튼 글자를 설정하는 속성은 `value`이므로 `value123`는 같은 역할을 하지 않는다. 브라우저 기본 제출 문구가 보이는 현상을 HTML이 오타를 의도대로 고쳤다고 해석하지 않는다.

양쪽 원본처럼 `button` 안에는 이미지를 넣을 수 있다. `input`은 종료 태그와 내부 콘텐츠를 가지지 않으므로 같은 방식으로 이미지 태그를 감싸지 않는다.

<a id="choice"></a>

## 4. 체크박스와 라디오: 선택 상태와 값 따로 읽기

### 체크박스 — 강사님 원본 발췌

강사님 `workspace_html/07_form.html` 28~32행

```html
        <input type="checkbox" name="coffee" value="1">샷추가
        <input type="checkbox" name="coffee" value="2" checked>펄추가
        <input type="checkbox" name="coffee" value="3" disabled>휘핑크림
        <input type="checkbox" name="coffee" value="4" >시럽
        <input type="checkbox" name="coffee" >간얼음
```

여러 체크박스가 같은 `name="coffee"`를 사용한다. 마지막 항목에는 `value`가 없어 선택 후 제출되면 기본값 `on`이 쓰인다.

### 체크박스 — 내 원본 발췌

내 코드 `workspace_html/07_form.html` 52~56행

```html
            <input type="checkbox" name="coffee" value="1">샷추가
            <input type="checkbox" name="coffee" value="2" checked>펄추가
            <input type="checkbox" name="coffee" value="3" disabled>휘핑크림추가
            <input type="checkbox" name="coffee" value="4" >시럽추가
            <input type="checkbox" name="coffee" value="5" >얼음추가
```

나는 마지막 항목에도 `value="5"`를 지정했다. **어떤 옵션을 골랐는지 서버에서 구별하려는 목적에는 내 코드가 더 명확하다.** 이름이 같아도 여러 체크박스를 동시에 선택할 수 있다.

| 원본 초기 상태 | 제출 대상으로 선택되는 것 |
| --- | --- |
| `checked`인 펄추가 | `coffee=2` |
| 체크하지 않은 항목 | 포함되지 않음 |
| `disabled`인 항목 | 제출에서 제외 |

나중에 사용자가 선택을 바꾸면 제출 결과도 바뀐다. `checked`는 HTML에 적힌 초기 선택 상태이며, 그 뒤의 사용자 선택을 무시하고 항상 제출하라는 뜻이 아니다.

### 라디오 — 강사님 원본 발췌

강사님 `workspace_html/07_form.html` 39~40행

```html
        <input type="radio" name="gender" value="여자" checked>여자
        <input type="radio" name="gender" value="남자" checked>남자
```

같은 그룹의 두 항목 모두 `checked`다. 이 원본을 처음 읽은 브라우저에서는 뒤에 있는 남자 항목이 선택 상태가 된다. 두 항목을 동시에 선택하는 그룹이 되지는 않는다.

### 라디오 — 내 원본 발췌

내 코드 `workspace_html/07_form.html` 66~67행

```html
            <input type="radio" name="gender" value="여자" checked>여자
            <input type="radio" name="gender" value="남자">남자
```

나는 초기 선택을 여자 항목 하나에만 두었다. **초기 선택 의도가 명확하다.** 이 수업처럼 같은 폼 안에서 같은 `name`을 가진 라디오를 한 그룹으로 읽고, 서로 다른 `name`은 별도 그룹으로 읽는다.

양쪽 `china` 그룹은 각 라디오에 `value`가 없다. 선택한 음식 이름의 화면 글자가 자동으로 값이 되는 것은 아니므로, 구별하려면 각 음식에 값을 명시해야 한다.

<a id="other"></a>

## 5. `select`·`label`·`textarea`

### 선택 목록

양쪽 원본의 `select name="sel1"`에는 값 `1`~`5`인 `option`이 있고, 분식에 `selected`가 있다. 처음 제출 값은 **화면 글자 `분식`이 아닌 `sel1=4`**다. 강사님의 `양식11111111`과 내 `양식`처럼 표시 글자가 달라도 `value="3"`이면 제출 값은 같다.

`multiple`이 있으면 여러 항목을 선택할 수 있고, `size="3"`은 보이는 행 수를 지정한다. 양쪽 원본의 이 다중 선택 목록에는 `name`이 없으므로 선택하더라도 이름 있는 항목으로 제출되지 않는다. 단일 선택 예제와 구분한다.

### 이름표 연결

양쪽 원본은 감싸는 방법과 `for`·`id`를 맞추는 방법을 모두 사용한다. 다음은 설명용 재구성이다.

```html
<input type="checkbox" id="pearl" name="coffee" value="2">
<label for="pearl">펄추가</label>
```

글자 `펄추가`를 클릭해도 연결된 체크박스를 선택할 수 있다. 연결 기준은 `for="pearl"` ↔ `id="pearl"`이고, 제출 이름은 `name="coffee"`다. `for`를 `name`에 맞추는 것이 아니다.

### 여러 줄 입력

강사님은 `textarea` 안에 `미리`, 줄바꿈, `<br>`, `<!-- 주석 -->`을 넣었고, 나는 미리 보여줄 글과 들여쓰기를 넣었다. 이 위치에서는 `<br>`나 주석 모양도 텍스트로 보일 수 있다. 일반 본문과 다른 해석을 확인하는 실험이다.

설명용 수정:

```html
<textarea name="memo" rows="3" cols="30" placeholder="메모 입력">오늘 배운 내용</textarea>
```

초기값은 `value` 속성이 아니라 **시작 태그와 종료 태그 사이**에 적는다. 들여쓰기·줄바꿈을 불필요하게 넣으면 초기 내용에 포함될 수 있다. `rows`·`cols`는 표시 크기이며 최대 입력 글자 수를 제한하는 설정은 아니다.

<a id="practice"></a>

## 6. 원본에 있는 다른 입력 타입

아래 타입도 양쪽 코드에 실제로 있다. “추가 입력 타입”이라는 이유만으로 빼지 않는다.

| 타입 | 수업에서 확인할 내용 |
| --- | --- |
| `color` | 색 선택 UI |
| `date` | 날짜, 원본 초기값 `2026-06-24` |
| `time` | 시간 입력 |
| `number` | 숫자 입력. 환경에 따라 지수 표현의 `e` 등이 입력될 수 있음 |
| `range` | 원본의 `min="10"`, `max="100"`, `step="10"` |

모양과 입력 방식은 브라우저·운영체제에 따라 달라질 수 있다. 원본의 `reset`은 모든 입력을 무조건 빈 문자열로 만드는 버튼이 아니다. `value`·`checked`·`selected` 등의 초기 상태로 되돌리는 동작을 확인한다.

### 복습

1. `placeholder="이름"`만 있고 값이 비어 있으면 `이름`이라는 글자가 제출될까?
2. 원본 `readonly` 입력을 그대로 두고 값이 제출되지 않았다. 먼저 확인할 속성은?
3. 같은 `name`의 라디오 두 개에 모두 `checked`를 쓰는 대신 어떻게 작성할까?
4. `rows="3"`이면 세 글자만 입력할 수 있을까?

<details>
<summary>정답과 이유</summary>

1. 아니다. 힌트는 입력값이 아니다.
2. 제출 이름인 `name`이 있는지 확인한다.
3. 의도한 초기 선택 하나에만 `checked`를 둔다.
4. 아니다. 표시할 행 수다.

</details>

**추가로 알면 좋은 것:** 원본에 없는 입력 타입·`fieldset`/`legend`·상세 검증 속성·접근성 설계 전체를 기본 예제의 필수 조건으로 추가하지 않는다.

정확성 참고: [HTML 표준 — input](https://html.spec.whatwg.org/dev/input.html), [폼 컨트롤과 제출](https://html.spec.whatwg.org/dev/form-control-infrastructure.html).

[다음: 폼 전송](07-02_HTML_폼_전송과_GET_POST.md)

<!-- legacy-migration -->

<a id="index-section-102"></a>
<a id="index-section-45"></a>
<a id="html-4"></a>
<a id="index-section-17"></a>
<a id="html-18"></a>
<a id="index-section-5"></a>
<a id="html-23"></a>
<a id="html-7"></a>
<a id="index-section-93"></a>
<a id="html-24"></a>
<a id="index-section-24"></a>
<a id="index-section-28"></a>
<a id="html-10"></a>
<a id="html-37"></a>
<a id="index-section-36"></a>
<a id="html-6"></a>
<a id="index-section-15"></a>
<a id="html-25"></a>
<a id="index-section-88"></a>
<a id="html-17"></a>
<a id="html-9"></a>
<a id="index-section-40"></a>
<a id="html-19"></a>
<a id="index-section-116"></a>
<a id="html-8"></a>
<a id="index-section-72"></a>

### 이전 색인 링크 안내

이전 절 주소를 보존한 안내 위치다. 개편 전 절 번호와 현재 절 번호는 서로 다르다. 입력 상태는 이 문서, 제출되는 이름·값과 GET·POST는 [폼 전송](07-02_HTML_폼_전송과_GET_POST.md), 수업 밖 입력 기능은 [추가 입력 속성](추가로_알면_좋은_것/02_확장_요소와_속성.md#forms)에서 읽는다.
