# 19. 객체와 JSON — 값을 묶고 문자열로 바꾸기

[JavaScript 목차](README.md) · [이전: 브라우저 이동·지도](18_JavaScript_브라우저이동과_지도우편번호.md)

원본 파일 이름은 `19_json.html`이다. 하지만 첫 부분의 `json` 변수에는 **함수까지 들어간 JavaScript 객체**가 있다. `JSON.stringify`를 거쳐 나온 문자열이 JSON 형식이다. 객체와 JSON 문자열을 구별하면 뒤의 `parse`가 이해된다.

**객체란?** 이름이 있는 값들을 한데 묶은 JavaScript 자료형이다. **JSON은?** 이 값을 정해진 형식의 글자로 표현한 것이다. 아래는 원본 발췌가 아닌 **설명용 작은 예제**다.

```javascript
const person = { name: '민지', age: 20 };
console.log(person.name); // 민지
const text = JSON.stringify(person);
console.log(text); // {"name":"민지","age":20} 형태의 문자열
```

`person`은 속성을 읽을 수 있는 객체이고 `text`는 문자열이다. 수업 원본에서는 함수가 든 객체를 문자열로 바꿀 때 어떤 값이 빠지는지도 확인한다.

<!-- chapter-toc -->

- [1. 객체의 키와 값](19_JavaScript_객체와_JSON.md#section-1)
- [2. 읽기·변경·추가](19_JavaScript_객체와_JSON.md#section-2)
- [3. 객체 → JSON 문자열 → 다시 값](19_JavaScript_객체와_JSON.md#section-3)
- [4. 객체 배열과 속성 목록](19_JavaScript_객체와_JSON.md#section-4)
- [직접 확인할 질문](19_JavaScript_객체와_JSON.md#section-5)
- [추가로 알면 좋은 것](19_JavaScript_객체와_JSON.md#section-6)

<a id="section-1"></a>

## 1. 객체의 키와 값

### 강사님 코드

출처: `teacher/workspace_html/javascript/19_json.html` 12~26행 · **원본 발췌**

```javascript
        // json 선언
        let json = {}
        json = {
            "key": "value",
            "num": 1234,
            "fn": function(){
                console.log(1)
            }, 
            "k1": {
                "k1-1": 1,
                "k1-2": 2,
                k:3
            }, 
            k2 : 'k3',
        }
```

### 내 코드

출처: `me/workspace_html/javascript/19_json.html` 11~26행 · **원본 발췌**

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

`{}`는 빈 객체다. `key`, `num`, `fn`, `k1`, `k2`가 속성 이름이고, 값으로 문자열·숫자·함수·다른 객체가 들어 있다. 내 코드에는 강사님 코드의 중첩 속성 `k`가 빠져 있다. 따라서 아래에서 내 코드의 `json.k1.k`는 `undefined`이며 강사님 것은 `3`이다. **같은 결과라고 묶어 설명하면 안 된다.**

<a id="section-2"></a>

## 2. 읽기·변경·추가

### 강사님 코드

출처: `teacher/workspace_html/javascript/19_json.html` 31~52행 · **원본 발췌**

```javascript
        // 값에 접근하는 방법
        // 방법1 : 배열처럼
        console.log( "json['key'] : ", json['key'] )
        console.log( "json['num'] : ", json['num'] )
        console.log( "json['k1']['k1-1'] : ", json['k1']['k1-1'] )

        // 방법2 : 프로퍼티처럼
        console.log( 'json.key : ', json.key )
        // console.log( 'json.k1.k1-2 : ', json.k1.k1-2 )
        console.log( 'json.k1.k : ', json.k1.k )

        json['fn']()
        json.fn()

        // 값 넣기
        // key가 있으면 덮어쓰기
        // key가 없으면 추가
        json.num = 456
        console.log(json.num)
        console.log(json.num2)
        json.num2 = 222
        console.log(json)
```

### 내 코드

출처: `me/workspace_html/javascript/19_json.html` 31~56행 · **원본 발췌**

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

`json['key']`와 `json.key`는 이 키에서 같은 값을 읽는다. `k1-1`처럼 하이픈이 있는 이름은 `json['k1']['k1-1']`로 읽는다. `json.k1.k1-2`는 원하는 키를 가리키는 표기가 아니다. 기존 `num`에 대입하면 값이 바뀌고, 없던 `num2`에 대입하면 속성이 추가된다. 대입 전 `json.num2`를 읽으면 `undefined`가 나온다. 내 코드의 ‘not defined가 아님’이라는 메모도 이 차이를 말한다.

<a id="section-3"></a>

## 3. 객체 → JSON 문자열 → 다시 값

### 강사님 코드

출처: `teacher/workspace_html/javascript/19_json.html` 54~66행 · **원본 발췌**

```javascript
        // 네트워크 통신할 때 무조건 문자로 전송한다
        // stringify : json을 문자열로 만들어 준다
        // 단, 값이 함수인 것은 제외
        const str = JSON.stringify(json)
        console.log(str)

        // 글씨를 json으로 
        const json2 = JSON.parse(str)
        console.log(json2)

        // JSON.parse('<h1>')
        let j = JSON.parse('{}')
        j = JSON.parse('[{}]')
```

### 내 코드

출처: `me/workspace_html/javascript/19_json.html` 58~78행 · **원본 발췌**

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

`JSON.stringify(json)`은 객체를 JSON **문자열**로 만든다. 이 객체의 `fn`처럼 함수 값은 결과에서 빠진다. `JSON.parse(str)`은 유효한 JSON 문자열을 다시 JavaScript 값으로 읽는다. 따라서 `json2.fn`은 없다. `JSON.parse('{}')`는 객체, `JSON.parse('[{}]')`는 객체가 하나 담긴 배열을 만든다. 주석 처리된 `JSON.parse('<h1>')`는 실제로 실행하면 오류가 난다. 원본에서는 주석이라 페이지 실행을 멈추지 않는다.

원본 주석의 ‘네트워크 통신은 무조건 문자로 전송’은 이 연습을 위한 단순화다. 여기서 확실히 배운 것은 **객체를 JSON 문자열로 만드는 방법과 그 역변환**이다.

<a id="section-4"></a>

## 4. 객체 배열과 속성 목록

### 강사님 코드

출처: `teacher/workspace_html/javascript/19_json.html` 68~90행 · **원본 발췌**

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
        for(let t of temple){
            console.log(t.이름)
        }
        for(let i in temple){
            console.log(temple[i].가격)
        }

        // json의 모든 key를 배열로 돌려줌
        const keys = Object.keys(json)
        console.log(keys)

        // key 삭제
        delete json.num
        console.log(json)
```

### 내 코드

출처: `me/workspace_html/javascript/19_json.html` 80~103행 · **원본 발췌**

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

`for...of`는 배열의 각 객체를 `t`로 받으므로 `t.이름`을 읽는다. `for...in`은 이 배열의 인덱스 키를 `i`로 받아 `temple[i].가격`을 읽는다. `Object.keys(json)`은 객체 자신의 열거 가능한 키를 배열로 준다. `delete json.num` 뒤에는 해당 속성이 없다. 원본의 `temple`은 이름·주소·가격을 가진 **객체의 배열**이지 JSON 문자열이 아니다.

<a id="section-5"></a>

## 직접 확인할 질문

1. `JSON.stringify` 뒤의 `str`과 `JSON.parse(str)` 뒤의 `json2`는 각각 어떤 자료형일까?
2. 내 코드에서 `json.k1.k`를 읽으면 왜 강사님과 다르게 나올까?
3. `for...of`의 `t`와 `for...in`의 `i`에는 각각 무엇이 들어갈까?

<a id="section-6"></a>

## 추가로 알면 좋은 것

실제로 외부에서 받은 문자열은 JSON 형식이 아닐 수 있으므로 `JSON.parse` 오류 처리도 고려한다. 이 원본에는 오류를 잡는 코드가 없다.

**이 장을 읽은 뒤:** [장별 연습문제 풀기](실습/연습문제/19_JavaScript_객체와_JSON_연습문제.md) → [다음: AJAX와 fetch](20_JavaScript_AJAX와_fetch.md)

