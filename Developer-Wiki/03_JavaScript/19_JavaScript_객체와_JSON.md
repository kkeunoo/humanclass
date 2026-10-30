# 19. 객체와 JSON — 속성이 있는 값과 전송할 문자열을 구별하기

[JavaScript 목차](README.md) · [읽기 안내](00_JavaScript_V3_동작_백과_읽기법.md)

변수 이름이 json이라고 해서 그 값이 JSON 문자열인 것은 아니다. 수업의 첫 값은 함수를 포함한 JavaScript 객체이며 stringify 뒤에야 JSON 문자열이 된다. 모양이 비슷한 두 표현을 자료형과 가능한 작업으로 구별해 보자.

<a id="chapter-toc"></a>

**이 장의 목차:** [목표](#learn) · [개념](#concepts) · [예제](#example) · [내 코드](#my-code) · [연결](#connections) · [평가](#review) · [비교](#teacher) · [결과·실험](#results) · [TIP·출처](#tips) · [복습](#practice)

<a id="learn"></a>

## 1. 이 장에서 배울 것

속성의 읽기·변경·추가·삭제를 설명한다. 객체와 배열·JSON 문자열, 함수 참조와 호출을 구분하고 stringify와 parse 사이에서 함수 속성이 사라지는 결과를 추적한다.

입력·현재 상태·실행 순서·결과를 분리해 설명한다. 실제 수업 원본은 아래에 표시하고, 원본에 없는 선택 학습은 9절 TIP에 둔다.

<a id="concepts"></a>

## 2. 무엇이며, 왜 필요한가

객체는 이름이 있는 속성들을 묶은 값이다. 예를 들어 person.name은 person 객체의 name 속성이다. 배열이 순서 있는 항목을 담는다면 객체는 이름으로 값을 찾는다. 속성 값에는 문자열·숫자·함수·다른 객체가 들어갈 수 있다.

| 표현 | 값의 종류 | 사용할 작업 |
| --- | --- | --- |
| { name: '민지', age: 20 } | 객체 | .name으로 속성 읽기 |
| [{ name: '민지' }] | 객체를 담은 배열 | 반복하여 각 객체 읽기 |
| '{"name":"민지"}' | JSON 형식의 문자열 | parse하여 값으로 해석 |
| JSON.stringify(객체) | 문자열 변환 결과 | 문자 출력·요청 본문 등에 활용 |

점 표기와 대괄호 표기는 속성을 읽는 두 방법이다. person.name과 person['name']은 여기서 같다. 'k1-1'처럼 하이픈이 든 이름은 대괄호 문자열로 읽는다. person.k1-1은 그 이름을 읽는 표기가 아니라 뺄셈을 포함하는 식으로 해석된다.

JSON은 값의 문자 표현 형식이다. 속성 이름과 문자열에 큰따옴표를 쓰며 함수 본문은 담지 않는다. JavaScript 객체 리터럴의 작은따옴표·함수·마지막 쉼표까지 그대로 허용하는 문자열 형식이라고 생각하지 않는다.

> 📚 **출처 · 본문 설명 확인:** [MDN JSON.stringify](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify), [JSON.parse](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/parse), [Object.keys](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/keys). 배운 기능의 뜻을 확인한 근거다. 예제·표·풀이 흐름은 수업 코드를 바탕으로 새로 작성했으며 외부 문장을 직접 인용하지 않았다. 확인일: 2026-10-28.

<a id="example"></a>

## 3. 작은 예제로 먼저 이해하기

**새 설명 예제 · 전체 스크립트.** [HTML 실행 파일](실습/책형_복습/19_JavaScript_객체와_JSON.html)과 같은 폴더의 [JS 파일](실습/책형_복습/19_JavaScript_객체와_JSON.js)을 함께 내려받는다. HTML을 브라우저로 열고 Console에서 결과를 확인한다. script는 필요한 HTML 뒤에 연결한다. 콘솔 출력은 페이지 본문에 자동으로 쓰이지 않는다.

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

age는 기존 속성이어서 21로 바뀌고 city는 없던 속성이어서 추가된다. greet()는 함수 본문을 호출해 안녕을 출력한다. stringify 결과는 문자열이며 객체의 함수 속성 greet는 빠진다. parse는 그 문자열을 다시 값으로 읽지만 빠진 함수를 복원하지 않는다. restored.greet의 typeof는 undefined다. delete 뒤 city도 없는 속성으로 읽힌다. 마지막 반복은 배열의 각 객체를 받아 이름을 출력한다. 새 예제이며 원본 json 변수의 값과 혼동하지 않는다.

**예상 출력 또는 관찰:**

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

<a id="my-code"></a>

## 4. 내가 작성한 코드를 따라 읽기

아래는 원본의 일부다. 원본에 의존하는 앞 선언·HTML·함수는 다음 절의 연결까지 읽는다. 주석의 잘못된 표현도 원문대로 보존하고 설명에서 교정한다.

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_html/javascript/19_json.html` 11–26행

```javascript
            // json 선언 (배열과 다르게 중괄호로 선언)
            // value에는 변수에 담을 수 있는 모든것이 들어감 (함수,변수 등)
            let json = {}
            json = {
                "key": "value",
                "num": 1234,
                "fn": function() {
                    console.log(1)
                },
                "k1": {
                    "k1-1": 1,
                    "k1-2": 2
                },
                // javascript 한정 key도 ""없이 쓸 수 있음 ,가 마지막에 있어도 괜춘
                k2 : 'k3',
            }
```

**발췌 바로 풀이:** `{}`는 빈 객체다. `key`, `num`, `fn`, `k1`, `k2`가 속성 이름이고, 값으로 문자열·숫자·함수·다른 객체가 들어 있다. 내 코드에는 강사님 코드의 중첩 속성 `k`가 빠져 있다. 따라서 아래에서 내 코드의 `json.k1.k`는 `undefined`이며 강사님 것은 `3`이다. **같은 결과라고 묶어 설명하면 안 된다.**

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_html/javascript/19_json.html` 31–56행

```javascript
            // 값에 접근하는 방법
            // 방법1 : 배열처럼
            console.log( "json['key'] : " , json['key'] )
            console.log( "json['num'] : ", json['num'] )
            console.log( "json['k1']['k1-1'] : ", json['k1']['k1-1'] )

            // 방법2 : 프로퍼티처럼 .으로 접근 가능
            console.log( 'json.key : ', json.key )
            // 아래처럼 value값에 '-'가 있을 때 마이너스로 인식하여, NaN이 발생됨
            // console.log( 'json.k1.k1-2 : ', json.k1.k1-2 )
            console.log( 'json.k1.k : ', json.k1.k)

            json['fn']()
            json.fn()

            // 값 넣기 (변수처럼 값을 넣을 수 있음)
            // key가 있으면 덮어쓰기, 없다면 추가됨
            json.num = 456
            console.log(json.num)
            // not defined가 아니라, 있을 것 같지만 값이 없어서 undefined가 나옴
            console.log(json.num2)
            json.num2 = 222
            console.log(json.num2)

            // 배열의 push처럼 넣지 않아도, 값을 넣으면 자동적으로 들어감
            console.log( json )
```

**발췌 바로 풀이:** `json['key']`와 `json.key`는 이 키에서 같은 값을 읽는다. `k1-1`처럼 하이픈이 있는 이름은 `json['k1']['k1-1']`로 읽는다. `json.k1.k1-2`는 원하는 키를 가리키는 표기가 아니다. 기존 `num`에 대입하면 값이 바뀌고, 없던 `num2`에 대입하면 속성이 추가된다. 대입 전 `json.num2`를 읽으면 `undefined`가 나온다. 내 코드의 ‘not defined가 아님’이라는 메모도 이 차이를 말한다.

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_html/javascript/19_json.html` 58–78행

```javascript
            // 네트워크 통신할 때 무조건 문자로 보내야 함
            // json도 배열을 join()으로 문자값으로 바꾼 것 처럼 작업해야 함
            // 아래와 같이 대문자 JSON에 stringify를 하면 글씨로 바꿔줌 
            // 단, 값이 함수인 것은 제외함
            const str = JSON.stringify(json)
            console.log(str)

            // parse(분석)을 이용해서 문자열로 바꾼 값을 다시 json으로 바꿀 수 있음
            const json2 = JSON.parse(str)
            console.log(json2)

            //Uncaught Syntax(오타)Error: Unexpected token 
            // '<', "<h1>" is not valid JSON(JSON이 아니다)
            // at JSON.parse (<anonymous>)
            // JSON.parse('<h1>')
            
            // 배열안에 JSON이 있는 경우도 허용해줌
            let j = JSON.parse('{}')
            console.log(j)
            j = JSON.parse('[{}]')
            console.log(j)
```

**발췌 바로 풀이:** `JSON.stringify(json)`은 객체를 JSON **문자열**로 만든다. 이 객체의 `fn`처럼 함수 값은 결과에서 빠진다. `JSON.parse(str)`은 유효한 JSON 문자열을 다시 JavaScript 값으로 읽는다. 따라서 `json2.fn`은 없다. `JSON.parse('{}')`는 객체, `JSON.parse('[{}]')`는 객체가 하나 담긴 배열을 만든다. 주석 처리된 `JSON.parse('<h1>')`는 실제로 실행하면 오류가 난다. 원본에서는 주석이라 페이지 실행을 멈추지 않는다.

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_html/javascript/19_json.html` 80–103행

```javascript
            const temple = [{
                이름: '그랜절',
                주소: '광장',
                가격: 300000
            }, {
                이름: '만우절',
                주소: '없음',
                가격: 2147483647
            }]
            // json 배열도 동일하게 사용할 수 있음
            for(let t of temple) {
                console.log(t.이름)
            }
            for(let i in temple) {
                console.log(temple[i].가격)
            }

            // json의 모든 key를 배열로 돌려줌
            const keys = Object.keys(json)
            console.log(keys)

            // key 삭제 (실무해서는 실제 삭제하지는 않음)
            delete json.num
            console.log(json)
```

**발췌 바로 풀이:** `for...of`는 배열의 각 객체를 `t`로 받으므로 `t.이름`을 읽는다. `for...in`은 이 배열의 인덱스 키를 `i`로 받아 `temple[i].가격`을 읽는다. `Object.keys(json)`은 객체 자신의 열거 가능한 키를 배열로 준다. `delete json.num` 뒤에는 해당 속성이 없다. 원본의 `temple`은 이름·주소·가격을 가진 **객체의 배열**이지 JSON 문자열이 아니다.

내 json에는 key·num·fn·k1·k2가 있다. fn은 함수이고 k1은 중첩 객체다. 강사님 k1 안에는 k:3도 있지만 내 코드에는 없어 json.k1.k 출력이 undefined다. 두 코드를 같은 결과로 묶으면 안 된다. num은 456으로 변경하고 num2는 추가하기 전에 읽으면 undefined, 대입 뒤에는 222다. json.fn()과 json['fn']()는 이 키의 같은 함수를 호출하므로 각각 1을 출력한다.

<a id="connections"></a>

## 5. 선언·호출·파일이 연결되는 흐름

객체 준비 → 속성 읽기·함수 호출 → 값 변경·추가 → JSON.stringify로 문자열 생성 → JSON.parse로 새 값 해석 → 배열 반복·Object.keys·delete 순서다. 원본 fn의 정의는 첫 객체 안에 있고 호출은 다음 발췌에 있다. 정의가 있다는 사실만으로 1이 출력되는 것이 아니라 괄호를 붙여 호출할 때 실행된다. parse 뒤에는 fn 속성이 빠져 있으므로 같은 호출을 계속할 수 있다고 설명하지 않는다.

<a id="review"></a>

## 6. 잘한 점·아쉬운 점·개선 방향

**잘한 점:** 내 코드가 num2 대입 전후를 따로 출력하여 없는 속성과 새 속성을 비교할 수 있다. **교정:** 하이픈은 속성의 값이 아니라 이름에 있으며 대괄호로 읽어야 한다. 네트워크는 무조건 문자열만 전송한다는 주석은 이 JSON 연습의 단순화다. **공통 한계:** stringify·parse는 함수를 포함한 모든 객체를 원형 그대로 보존하는 복사법이 아니다. **주석 교정:** 실무에서 delete를 절대 쓰지 않는다는 규칙도 아니다. 목적에 맞게 속성을 제거하는 연산이다.

개선안은 원본을 수정한 결과가 아니다. 실제 오류, 수업용 단순화, 목적에 따른 선택을 구별해 판단한다.

<a id="teacher"></a>

## 7. 강사님 코드가 도움이 되는 비교



핵심 사용법은 같아 강사님 객체 전체를 다시 인용하지 않는다. 중첩 속성 k의 유무가 결과를 바꾸는 차이를 표에서 비교한다. 강사님에만 있는 속성을 내 코드 출력에 추가하지 않고 실제로 선언된 값을 기준으로 읽는다.

<a id="results"></a>

## 8. 결과를 추적하고 한 가지 바꾸기

| 관찰 | 강사님 원본 | 내 원본 |
| --- | --- | --- |
| json.k1.k | 3 | undefined |
| json.fn() 한 번 호출 | 1 출력 | 1 출력 |
| num 변경 뒤 | 456 | 456 |
| num2 추가 전 | undefined | undefined |
| stringify 뒤 fn 속성 | 문자열에 없음 | 문자열에 없음 |

Object.keys는 객체 자신의 열거 가능한 문자열 키들을 배열로 준다. for...of는 배열 항목을 받고 for...in은 원본 배열의 키를 받아 temple[i]로 접근한다. 둘의 변수에 같은 것이 들어간다고 설명하지 않는다. JSON.parse('<h1>')는 원본에서 주석이므로 자동 실행되지 않지만, 직접 실행하면 유효한 JSON이 아니어서 오류가 난다.

| 한 가지만 변경 | 예상 | 이유 |
| --- | --- | --- |
| 내 k1에 k:3 추가 | 해당 속성 출력 3 | 값의 유무 차이 |
| JSON 문자열의 큰따옴표를 작은따옴표로 변경 | parse 오류 | JSON 문법 차이 |
| 문자열 만들기 전에 age 변경 | 문자열에 새 나이 | 변환 시점의 값 사용 |
| 문자열 만든 뒤 원본 age만 변경 | 이미 만든 text는 그대로 | 저장된 문자열이 자동 갱신되지 않음 |

undefined가 보이면 속성 이름과 실제 선언을 확인한다. 선언하지 않은 변수의 ReferenceError와 없는 속성 읽기를 구분한다. parse 오류는 함수가 아니라 입력 문자열의 형식부터 본다. 함수가 복원되지 않은 것은 parse 실패가 아니라 stringify 때 해당 속성이 빠진 결과다.

<a id="tips"></a>

## 9. 추가로 알면 좋은 것과 출처

> 💡 **TIP · 수업 범위 밖:** 외부 문자열의 parse 오류 처리, 함수·날짜·순환 참조가 있는 값의 별도 변환 정책, 다양한 전송 데이터 형식은 추가 학습이다. 이 장의 기본은 실제 실습한 객체 속성과 JSON 변환이다.



이 절의 확장은 기본 문제의 필수 조건이 아니다. 📚 출처가 있다는 것과 수업 밖 기능이라는 것은 다른 구분이다.

<a id="practice"></a>

## 10. 복습과 빠른 정리

1. 변수 이름이 json이면 문자열인가?
2. stringify 뒤 함수 속성은 parse로 돌아오는가?
3. 내 json.k1.k가 undefined인 이유는?
4. for...of와 for...in의 반복 값은 같은가?

<details>
<summary>짧은 풀이 — 먼저 답한 뒤 확인</summary>

이름만으로 자료형은 정해지지 않는다. 원본 객체의 함수 속성은 JSON 문자열에서 빠져 돌아오지 않는다. 내 중첩 객체에는 k를 선언하지 않았다. of는 배열 항목, in은 키를 받는다.

</details>

| 단계 | 자료형 확인 |
| --- | --- |
| 객체 | 속성으로 값을 읽음 |
| stringify | 문자열을 만듦 |
| parse | 문자열에서 값을 읽음 |
| 반복 | 항목과 키 구별 |

[장별 연습문제](실습/연습문제/19_JavaScript_객체와_JSON_연습문제.md)에서 예상·설명·수정을 이어 간다. 다음은 [AJAX·fetch](20_JavaScript_AJAX와_fetch.md)다.

<!-- 이전 색인 이동 주소 보존 -->
<a id="section-1"></a>
<a id="section-2"></a>
<a id="section-3"></a>
<a id="section-4"></a>
<a id="section-5"></a>
<a id="section-6"></a>

[이 장의 목차](#chapter-toc)에서 현재 설명을 찾는다.
