# 보이는 값과 입력 상태 — 연습문제

[본문으로](../../07_HTML_폼과_입력요소.md) · [문제 목차](README.md)

이 파일은 수업 원본을 바탕으로 **새로 구성한 연습문제**다. 실제 강사님 퀴즈와 구분한다. 풀이 전에 예상과 이유를 직접 적고, 본문의 실행 파일에 적용해 확인한다.

## 목표와 실행 조건

id·name·value·placeholder를 구분하고 선택·읽기 전용·초기화를 설명한다.

HTML 조각은 본문에서 제공한 전체 파일의 적절한 위치에 넣는다. ‘코드로 예상한 결과’와 ‘브라우저에서 실제 확인한 결과’를 따로 적는다. 폼 요청은 로컬 HTTP 환경에서 관찰하고, 서버 저장 기능을 이 문제에 임의로 추가하지 않는다.

## 문제 1. 먼저 결과 예상하기

**새 설명 예제 · form 안의 조각.** 사용자가 아직 수정하지 않았다. 현재 값·힌트·초기 선택과 제출 이름을 적는다.

```html
<label for="nick">별명</label>
<input id="nick" name="nickname" value="student" placeholder="별명을 입력">
<label><input type="checkbox" name="topic" value="html" checked>HTML</label>
<label><input type="checkbox" name="topic" value="css">CSS</label>
```

힌트 글자가 입력값이 될까? 같은 name의 체크박스는 둘 다 선택할 수 있을까?

<details>
<summary>힌트와 풀이</summary>

**힌트:** 속성 이름과 현재 값을 구별하고, 이 코드가 전체 문서인지 조각인지 먼저 확인한다.

별명 현재 값은 student, 이름은 nickname, 힌트는 ‘별명을 입력’이다. placeholder는 값이 아니며 현재 글자가 있으면 보통 힌트가 보이지 않는다. 초기에는 HTML만 선택되지만 체크박스 둘을 모두 선택할 수 있다. 같은 name radio의 단일 선택과 구별한다. label의 for는 name이 아니라 id nick에 연결된다.

</details>

## 문제 2. 이유를 설명하기

readonly와 disabled의 차이를 설명한다. 두 입력 모두 name이 없다면, readonly 속성만 보고 ‘그 입력값은 제출된다’고 할 수 있을까? reset은 언제나 빈칸으로 돌릴까?

<details>
<summary>풀이</summary>

readonly는 해당 텍스트 입력을 사용자가 편집하지 못하게 하되 이름 등 제출 조건을 갖추면 제출에 포함될 수 있다. disabled는 비활성 제어로 제출에서 제외된다. 둘 다 name이 없으면 그 이름 없는 입력은 제출 항목이 되지 않는다. reset은 문서의 초기값·초기 선택으로 돌린다. value="student"가 초기값이면 빈칸이 아닌 student로 돌아간다.

</details>

## 문제 3. 고치고 한 가지 바꾸기

이름을 `nickname=student`, 메모를 `memo=review`로 초기화하려 했다. 다음을 고치고 초기화 버튼을 누를 때의 결과를 적는다.

```html
<form>
    <input id="nickname" placeholder="student">
    <textarea name="memo" value="review"></textarea>
    <button type="reset">처음으로</button>
</form>
```

<details>
<summary>예시 정답과 변경 실험</summary>

```html
<form>
    <input id="nickname" name="nickname" value="student">
    <textarea name="memo">review</textarea>
    <button type="reset">처음으로</button>
</form>
```

입력에 name과 실제 초기 value를 추가하고 textarea의 초기 내용을 태그 사이에 넣었다. 변경 후 reset을 누르면 student·review로 돌아간다. 실제 페이지를 완성할 때는 본문처럼 label도 연결한다. name만 learner로 바꾸는 실험에서는 id는 그대로이므로 label 연결과 제출 이름의 변화가 별개임을 설명한다.

</details>

## 채점과 복습

| 점검 | 스스로 확인할 것 |
| --- | --- |
| 예상 | 결과를 먼저 썼는가? |
| 설명 | 왜 그런지 태그·속성·위치로 설명했는가? |
| 수정 | 요구한 조건만 바꾸었는가? |
| 검증 | 저장·새로고침 후 실제 결과와 비교했는가? |

힌트와 현재 값, 초기값과 수정한 값, 보이는 상태와 제출 자격을 차례로 분리한다.

정답 글자를 외우기보다 원인을 설명하지 못한 부분을 [본문](../../07_HTML_폼과_입력요소.md)에서 다시 읽는다. 본문의 📚 출처는 배운 기능의 설명을 확인하는 근거이며, 💡 TIP은 선택 학습이다. 이 문제의 정답에 TIP 기능이 필수로 들어가지는 않는다.
