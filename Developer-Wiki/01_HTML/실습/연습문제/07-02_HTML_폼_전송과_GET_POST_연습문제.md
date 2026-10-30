# 제출 항목부터 요청까지 — 연습문제

[본문으로](../../07-02_HTML_폼_전송과_GET_POST.md) · [문제 목차](README.md)

이 파일은 수업 원본을 바탕으로 **새로 구성한 연습문제**다. 실제 강사님 퀴즈와 구분한다. 풀이 전에 예상과 이유를 직접 적고, 본문의 실행 파일에 적용해 확인한다.

## 목표와 실행 조건

name·선택·disabled를 기준으로 항목을 구성하고 GET·POST와 서버 응답을 구분한다.

HTML 조각은 본문에서 제공한 전체 파일의 적절한 위치에 넣는다. ‘코드로 예상한 결과’와 ‘브라우저에서 실제 확인한 결과’를 따로 적는다. 폼 요청은 로컬 HTTP 환경에서 관찰하고, 서버 저장 기능을 이 문제에 임의로 추가하지 않는다.

## 문제 1. 먼저 결과 예상하기

**새 설명 예제 · body 조각.** 아직 값을 바꾸지 않았다. GET 쿼리에 포함될 항목을 문서 순서대로 쓴다.

```html
<form method="get">
    <input name="q" value="html">
    <input id="hint" value="visible">
    <input name="fixed" value="A" readonly>
    <input name="off" value="B" disabled>
    <input type="checkbox" name="topic" value="table" checked>
    <input type="checkbox" name="topic" value="form">
    <button type="submit">검색</button>
</form>
```

<details>
<summary>힌트와 풀이</summary>

**힌트:** 속성 이름과 현재 값을 구별하고, 이 코드가 전체 문서인지 조각인지 먼저 확인한다.

`q=html&fixed=A&topic=table`이다. hint 입력은 name이 없고 off는 disabled여서 빠진다. readonly fixed는 name이 있으므로 포함된다. topic=form은 미선택이다. 제출 버튼에도 name이 없으므로 ‘검색’이 자동 항목으로 들어가지 않는다.

</details>

## 문제 2. 이유를 설명하기

method만 post로 바꾸면 항목의 이름·값은 모두 사라질까? POST 뒤 서버가 ‘허용하지 않는 메서드’ 같은 오류를 응답하면 요청도 보내지 않았다는 뜻일까?

<details>
<summary>풀이</summary>

항목 구성 원리는 그대로이고 기본 폼 인코딩에서는 POST 본문으로 보낸다. GET처럼 새 항목이 주소 쿼리에 붙는 방식과 구별한다. 오류 응답은 서버가 요청을 받은 뒤 해당 처리를 지원하지 않아 반환할 수도 있다. 요청 전송·응답 성공·실제 저장 성공은 같은 판단이 아니다.

</details>

## 문제 3. 고치고 한 가지 바꾸기

다음 목표에 맞게 첫 문제에서 최소한으로 수정한다. ① 두 topic을 모두 제출 ② visible도 info라는 이름으로 제출 ③ A는 그대로 제출 ④ B는 계속 제외. 처음 문제와 다른 예상 쿼리를 적고 수정 이유를 한 줄씩 설명한다.

<details>
<summary>예시 정답과 변경 실험</summary>

```html
<input id="hint" name="info" value="visible">
<input type="checkbox" name="topic" value="form" checked>
```

위 두 줄을 해당 줄과 교체한다. 나머지는 유지한다. 예상은 `q=html&info=visible&fixed=A&topic=table&topic=form`이다. 이름을 추가한 것과 선택 상태를 바꾼 것이 각 항목을 포함시킨다. A는 readonly와 name 유지, B는 disabled 유지다. 체크박스 값 하나만 삭제하는 별도 실험에서는 그 선택의 값이 on이 되는 조건을 설명한다.

</details>

## 채점과 복습

| 점검 | 스스로 확인할 것 |
| --- | --- |
| 예상 | 결과를 먼저 썼는가? |
| 설명 | 왜 그런지 태그·속성·위치로 설명했는가? |
| 수정 | 요구한 조건만 바꾸었는가? |
| 검증 | 저장·새로고침 후 실제 결과와 비교했는가? |

POST라는 이름만으로 저장이나 보안을 보장한다고 쓰지 않는다. 실제 확인은 HTTP 환경·요청 항목·서버 응답을 각각 기록한다.

정답 글자를 외우기보다 원인을 설명하지 못한 부분을 [본문](../../07-02_HTML_폼_전송과_GET_POST.md)에서 다시 읽는다. 본문의 📚 출처는 배운 기능의 설명을 확인하는 근거이며, 💡 TIP은 선택 학습이다. 이 문제의 정답에 TIP 기능이 필수로 들어가지는 않는다.
