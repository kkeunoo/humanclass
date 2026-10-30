# 19. 객체와 JSON — 속성이 있는 값과 전송할 문자열을 구별하기 — 연습문제

[본문](../../19_JavaScript_객체와_JSON.md) · [문제 목차](README.md)

실제 수업 기능을 바탕으로 **새로 구성한 연습문제**다. 강사님 원본 퀴즈와 구분한다. 예상 → 이유 → 수정 순서로 풀고, 정답은 먼저 답한 뒤 펼친다.

## 목표와 실행 조건

속성의 읽기·변경·추가·삭제를 설명한다. 객체와 배열·JSON 문자열, 함수 참조와 호출을 구분하고 stringify와 parse 사이에서 함수 속성이 사라지는 결과를 추적한다.

[전체 실행 HTML](../책형_복습/19_JavaScript_객체와_JSON.html)과 같은 폴더의 JS를 함께 준비한다. Console을 열고 새로고침하면 처음부터 실행한다. 원본과 별도 파일이므로 기존 변수·타이머·출력 변경 실험의 영향을 섞지 않는다. 실제 입력·현재 시각·난수는 고정 결과와 구별한다.

입력·버튼·키보드·스크롤 예제는 [본문의 3절](../../19_JavaScript_객체와_JSON.md#example)에 적힌 조작 순서대로 결과를 예상한다. 통신 예제는 해당 절의 가상 JSON 파일과 로컬 웹 실행 준비가 필요하며 HTML을 직접 여는 조건과 다르다. Console 출력이 없는 문제는 화면의 값·개수·선택 상태를 답한다.

## 문제 1. 실행 순서와 결과 예상

다음은 **새 설명 예제**다. 출력 전에 어떤 값이 어떤 순서로 만들어지는지 적는다.

```javascript
const person = {
    name: '민지',
    age: 20,
    detail: { 'study-year': 1 },
    greet: function () { console.log('안녕'); }
};
console.log(person.name);
console.log(person.detail['study-year']);
person.age = 21;
person.city = '서울';
person.greet();
const text = JSON.stringify(person);
console.log(typeof text);
console.log(text);
const restored = JSON.parse(text);
console.log(restored.age);
console.log(typeof restored.greet);
console.log(Object.keys(restored).join(', '));
delete restored.city;
console.log(restored.city);
const students = [{ name: '민지' }, { name: '준호' }];
for (const student of students) console.log(student.name);
```

<details>
<summary>힌트와 풀이</summary>

**힌트:** 입력·현재 상태·실행 시점·반환값을 따로 표시한다.

```text
민지
1
안녕
string
{"name":"민지","age":21,"detail":{"study-year":1},"city":"서울"}
21
undefined
name, age, detail, city
undefined
민지
준호
```

age는 기존 속성이어서 21로 바뀌고 city는 없던 속성이어서 추가된다. greet()는 함수 본문을 호출해 안녕을 출력한다. stringify 결과는 문자열이며 객체의 함수 속성 greet는 빠진다. parse는 그 문자열을 다시 값으로 읽지만 빠진 함수를 복원하지 않는다. restored.greet의 typeof는 undefined다. delete 뒤 city도 없는 속성으로 읽힌다. 마지막 반복은 배열의 각 객체를 받아 이름을 출력한다. 새 예제이며 원본 json 변수의 값과 혼동하지 않는다.

</details>

## 문제 2. 개념을 자신의 말로 설명

1. 변수 이름이 json이면 문자열인가?
2. stringify 뒤 함수 속성은 parse로 돌아오는가?
3. 내 json.k1.k가 undefined인 이유는?
4. for...of와 for...in의 반복 값은 같은가?

<details>
<summary>풀이</summary>

이름만으로 자료형은 정해지지 않는다. 원본 객체의 함수 속성은 JSON 문자열에서 빠져 돌아오지 않는다. 내 중첩 객체에는 k를 선언하지 않았다. of는 배열 항목, in은 키를 받는다.

| 관찰 | 강사님 원본 | 내 원본 |
| --- | --- | --- |
| json.k1.k | 3 | undefined |
| json.fn() 한 번 호출 | 1 출력 | 1 출력 |
| num 변경 뒤 | 456 | 456 |
| num2 추가 전 | undefined | undefined |
| stringify 뒤 fn 속성 | 문자열에 없음 | 문자열에 없음 |

Object.keys는 객체 자신의 열거 가능한 문자열 키들을 배열로 준다. for...of는 배열 항목을 받고 for...in은 원본 배열의 키를 받아 temple[i]로 접근한다. 둘의 변수에 같은 것이 들어간다고 설명하지 않는다. JSON.parse('<h1>')는 원본에서 주석이므로 자동 실행되지 않지만, 직접 실행하면 유효한 JSON이 아니어서 오류가 난다.

</details>

## 문제 3. 한 가지를 바꾸어 확인

먼저 **내 k1에 k:3 추가**를 바꾸면 무엇이 달라질지 적는다. 그다음 실행 파일에 해당 변경만 적용해 실제 결과와 비교한다. 나머지 실험도 원래 예제로 돌아가 하나씩 수행한다.

<details>
<summary>변경 결과와 막힐 때 확인</summary>

| 한 가지만 변경 | 예상 | 이유 |
| --- | --- | --- |
| 내 k1에 k:3 추가 | 해당 속성 출력 3 | 값의 유무 차이 |
| JSON 문자열의 큰따옴표를 작은따옴표로 변경 | parse 오류 | JSON 문법 차이 |
| 문자열 만들기 전에 age 변경 | 문자열에 새 나이 | 변환 시점의 값 사용 |
| 문자열 만든 뒤 원본 age만 변경 | 이미 만든 text는 그대로 | 저장된 문자열이 자동 갱신되지 않음 |

undefined가 보이면 속성 이름과 실제 선언을 확인한다. 선언하지 않은 변수의 ReferenceError와 없는 속성 읽기를 구분한다. parse 오류는 함수가 아니라 입력 문자열의 형식부터 본다. 함수가 복원되지 않은 것은 parse 실패가 아니라 stringify 때 해당 속성이 빠진 결과다.

</details>

## 채점과 복습

| 점검 | 확인할 것 |
| --- | --- |
| 예측 | 실행 전에 출력·상태를 적었는가? |
| 근거 | 문법·조건·반환·순서로 설명했는가? |
| 수정 | 한 조건만 바꾸었는가? |
| 확인 | 실제 관찰과 코드 기준 예상을 구분했는가? |

틀린 이유를 설명할 수 없다면 [본문](../../19_JavaScript_객체와_JSON.md)의 작은 예제·내 원본 풀이로 돌아간다. TIP의 미학습 기능은 이 문제의 필수 정답이 아니다.
