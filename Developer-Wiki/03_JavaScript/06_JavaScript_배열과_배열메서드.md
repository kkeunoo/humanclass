# 06. 배열과 메서드 — 원본이 바뀌는가, 무엇을 돌려주는가

[JavaScript 목차](README.md) · [이전: while](05_JavaScript_While과_DoWhile.md) · [다음: 날짜](07_JavaScript_Date와_날짜처리.md)

기준은 양쪽 `06_array.html`이다. [04장](04_JavaScript_반복문과_배열순회.md)의 순회·map·filter를 익혔다면, 여기서는 **인덱스·원본 변경·반환값**을 중심으로 읽는다. 메서드는 객체에 속한 함수다. 예를 들어 arr.push(5)는 arr에 값을 추가하는 메서드 호출이다.

**배열**은 여러 값을 순서대로 담고 0부터 시작하는 번호로 꺼내는 자료다. 먼저 **설명용 예제**를 보자.

```javascript
const numbers = [10, 20];
console.log(numbers[0]);       // 10
console.log(numbers.push(30)); // 3: 새 배열 길이
console.log(numbers);          // [10, 20, 30]
```

`push`는 원본 배열을 바꾸지만 반환하는 값은 **추가한 30이 아니라 새 길이 3**이다. 아래 양쪽 코드에서도 메서드를 볼 때마다 원본 상태와 반환값을 따로 적는다.

<!-- chapter-toc -->

- [1. 배열과 const](06_JavaScript_배열과_배열메서드.md#section-1)
- [2. 인덱스·length·중첩 배열](06_JavaScript_배열과_배열메서드.md#section-2)
- [3. 추가·삭제·복사·정렬 표](06_JavaScript_배열과_배열메서드.md#section-3)
- [4. sort: 숫자 배열이라고 숫자 크기로 정렬되지는 않는다](06_JavaScript_배열과_배열메서드.md#section-4)
- [5. split으로 실제 query 값 찾기](06_JavaScript_배열과_배열메서드.md#section-5)
- [6. 실습 풀이에서 유지할 점과 고칠 점](06_JavaScript_배열과_배열메서드.md#section-6)
- [7. 짧은 복습](06_JavaScript_배열과_배열메서드.md#section-7)
- [추가로 알면 좋은 것](06_JavaScript_배열과_배열메서드.md#section-8)

<a id="section-1"></a>

## 1. 배열과 const

배열은 여러 값을 인덱스로 접근하는 객체다. 독립 변수를 여러 개 선언하는 것과 완전히 같지는 않다. typeof 배열은 'object'다. 한 배열에 숫자·문자열·불리언·다른 배열을 함께 담을 수도 있다.

### 강사님 코드

출처: `teacher/workspace_html/javascript/06_array.html` 22–30행 · **원본 발췌**

```javascript
        let arr3 = [1, 2, "글씨", false, 3.14, arr1]
        const arr4 = new Array(1, 2, "글씨", false, 3.14, arr1)

        console.log( 'arr3:', arr3 )
        console.log( 'arr3[0]:', arr3[0] )
        console.log( typeof arr3[0] )

        arr3[0] = 10
        arr3 = [1,2,3]
```

### 내 코드

출처: `me/workspace_html/javascript/06_array.html` 33–49행 · **원본 발췌**

```javascript
            const arr3 = [1, 2, "글씨", false, 3.14, arr1]
            const arr4 = new Array(1, 2, "글씨", false, 3.14, arr1)

            // +를 하게되면 배열이 ''+배열 이기 때문에 문자화되어 출력된다
            // ,를 하게되면 배열에 들어있는 객체 그 자체가 출력됨 (키 0에 1을 넣고...key: value)
            // let i = 2 > arr3[2] == arr3[i] 
            console.log( 'arr3[0]:'+ arr3 )
            console.log( 'arr3[0]:', arr3 )
            console.log( 'arr3[0]:', arr3[0] )
            // arr3[] 자체가 변수가 되었으며 본래 식별자(id)라고도 부름
            console.log( typeof arr3[0] )

            arr3[0] = 10
            // arr3 = [1, 2, 3] 은 const로 선언했기 때문에 =으로 바꿀 수 없음(내용물은 바꿀 수 있음)
            // 만약 let으로 arr3를 선언했다면 내용물 자체가 [1, 2, 3]으로 바뀔 수 있음
            console.log( 'arr3[0]:', arr3 )
            console.log( 'arr3[0]:', arr3[0] )
```

강사님은 arr3를 let으로 선언하여 원소 변경과 배열 전체 재대입을 모두 실행했다. 내 코드는 const로 선언하고 재대입을 주석 처리했다. **const여도 arr3[0]=10은 가능하다.** const가 금지하는 것은 arr3라는 이름에 다른 값을 재대입하는 일이다. 내 20행의 ‘중복 선언 불가’와 재대입 불가를 구분한다. 01장의 선언·대입 설명과 연결되는 좋은 비교다.

내 51–52행의 ‘문자 1Byte·숫자 4Byte, stack KB·heap GB’는 JavaScript의 고정 저장 규칙이 아니다. 원소 인덱스를 실제 메모리 주소라고 생각하지 않는다. 구현 내부의 저장·회수 상세는 추가 학습으로 분리한다.

<a id="section-2"></a>

## 2. 인덱스·length·중첩 배열

원본 arr[60] 읽기는 undefined이고, arr[60]=60 이후 length는 61이다. 중간의 빈칸이 자동으로 0으로 채워지는 것은 아니다. arr['문자']='문자'는 이름 있는 속성을 추가하며 length를 62로 늘리지 않는다. 배열을 새 값으로 재대입한 뒤에는 이전 속성과 원소가 새 배열로 따라오지 않는다.

### 강사님 중첩 반복

출처: `teacher/workspace_html/javascript/06_array.html` 100–104행 · **원본 발췌**

```javascript
        for(let j=0; j<음식.length; j++){
            for(let i=0; i<음식[j].length; i++){
                console.log(음식[j][i])
            }
        }
```

### 내 중첩 반복

출처: `me/workspace_html/javascript/06_array.html` 106–110행 · **원본 발췌**

```javascript
            for(let j=0; j<음식.length; j++) {
                for(let i=0; i<음식[j].length; i++) {
                    console.log(음식[j][i])
                }
            }
```

같은 구조다. 음식은 앞에서 만든 양식·중식·일식 배열을 원소로 가진다. 음식.length는 3, 음식[0].length는 5, 음식[1].length는 7이다. 바깥은 종류를, 안쪽은 해당 종류의 메뉴를 순회한다. 길이를 5로 고정하면 중식 일부를 빠뜨린다. 음식[0][2]는 첫 종류의 세 번째 메뉴인 스테이크다. 내 주석의 ‘1차원 배열에 [][]’는 이 예제에서는 **배열 안에 배열을 넣은 중첩 배열**로 고친다.

<a id="section-3"></a>

## 3. 추가·삭제·복사·정렬 표

| 메서드 | 원본 변경 | 반환값 | 수업에서 확인할 점 |
| --- | --- | --- | --- |
| push(값) | 뒤에 추가 | 새 length | 추가한 값 자체가 아님 |
| unshift(값) | 앞에 추가 | 새 length | 기존 인덱스가 뒤로 밀림 |
| pop() | 뒤에서 제거 | 제거한 값 | 빈 배열이면 undefined |
| shift() | 앞에서 제거 | 제거한 값 | 빈 배열이면 undefined |
| reverse() | 순서 반전 | 같은 배열 | 복사본 생성이 아님 |
| sort() | 순서 정렬 | 같은 배열 | 기본 비교는 문자열 기준 |
| slice(시작, 끝) | 변경 안 함 | 새 배열 | 끝 인덱스 제외 |
| splice(시작, 개수) | 지정 구간 제거 | 제거된 값의 배열 | 두 번째 인자는 끝 인덱스가 아님 |
| indexOf(값) | 변경 안 함 | 처음 찾은 인덱스, 없으면 -1 | 값과 자료형을 구분 |
| join(구분자) | 변경 안 함 | 문자열 | 생략한 구분자는 쉼표 |

split은 배열 메서드가 아니라 **문자열을 나누어 배열을 돌려주는 문자열 메서드**다. 모든 배열 메서드가 원본을 바꾼다는 내 주석은 위 표처럼 구분한다. 또 unshift와 shift를 짝지으면 같은 앞쪽에서 넣고 빼므로 가장 최근에 넣은 값이 먼저 나온다. 선입선출 큐의 수업 수준 예는 push로 뒤에 넣고 shift로 앞에서 꺼내는 조합이다.

### 강사님: 추가·삭제

출처: `teacher/workspace_html/javascript/06_array.html` 107–127행 · **원본 발췌**

```javascript
        arr = [1,2,3,4]

        // 맨 마지막에 하나 추가
        arr.push(5)
        console.log(arr)
        
        // 맨 앞에 추가하기
        arr.unshift(0)
        console.log(arr)
        
        // 맨 마지막 것 빼기
        // 뺀 값은 돌려준다
        // arr.pop()
        let pop = arr.pop()
        console.log(arr)
        console.log(pop)

        // 맨 처음 것 빼서 돌려주기
        let shift = arr.shift()
        console.log(arr)
        console.log(shift)
```

### 내 코드

출처: `me/workspace_html/javascript/06_array.html` 114–133행 · **원본 발췌**

```javascript
            arr = [1, 2, 3, 4]

            // 맨 마지막에 하나 추가
            arr.push(5)
            console.log(arr)

            // 맨 앞에 하나 추가
            arr.unshift(0)
            console.log(arr)

            // 맨 마지막에 하나 제거, 변수에 제거한 값을 넣을 수 있음 (return)
            // 원 배열에서 마지막 값 제거 후 그 값을 따로 사용 할 때 let 변수 = 배열.pop() 사용
            let pop = arr.pop()
            console.log(arr)
            console.log(pop)

            // 맨 처음 것 제거, 변수에 제거한 값을 넣을 수 있음 (return)
            let shift = arr.shift()
            console.log(arr)
            console.log(shift)
```

둘 다 [1,2,3,4] → push 후 [1,2,3,4,5] → unshift 후 [0,1,2,3,4,5]가 된다. pop은 5를 꺼내고 shift는 0을 꺼내므로 마지막 배열은 다시 [1,2,3,4]다. 반환값 pop·shift와 남은 배열을 함께 출력한 점이 양쪽 모두 좋다.

### slice와 splice 비교

강사님 145–153행과 내 154–164행은 같은 slice 실험이다. [0,1,2,3,4,5,6]에서 slice(2,5)는 [2,3,4], slice(2,50)과 slice(2)는 [2,3,4,5,6]이다. 원본 배열은 그대로다. 이는 얕은 복사이므로 중첩 객체까지 독립 복사한다고 설명하지 않는다. [MDN slice](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/slice)

강사님 파일 마지막의 splice 예제는 내 파일에 같은 실행 코드가 없다.

출처: `teacher/workspace_html/javascript/06_array.html` 257–258행 · **원본 발췌**

```javascript
        arr = [1,2,3,4,5]
        arr.splice(2, 1) // 2번 index부터 몇개를 뺄 것인가?
```

인덱스 2의 값 3을 한 개 제거하여 원본은 [1,2,4,5]가 된다. 호출 반환값은 [3]이지만 원본에서는 변수에 저장하거나 출력하지 않았다. 이 장에서는 실제 사용한 삭제 범위를 본문으로 두며 삽입·교체의 모든 변형까지 필수로 확대하지 않는다. [MDN splice](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/splice)

<a id="section-4"></a>

## 4. sort: 숫자 배열이라고 숫자 크기로 정렬되지는 않는다

### 강사님 코드

출처: `teacher/workspace_html/javascript/06_array.html` 174–175행 · **원본 발췌**

```javascript
        arr = [10, 5, 3]
        console.log( arr.sort() )
```

### 내 코드

출처: `me/workspace_html/javascript/06_array.html` 186–189행 · **원본 발췌**

```javascript
            // 3, 5, 10으로 정렬이 되어야 하는데 10, 3, 5 순으로 정렬됨
            // 숫자로 바꾸면 되겠지만, 배열 안에 있는건 이미 숫자이기 때문에 함수로 나중에 바꾸어야 함
            arr = [10, 5, 3]
            console.log(arr.sort())
```

양쪽 결과는 [10,3,5]다. 숫자로 변환하여 다시 넣는 것만으로 해결되지 않는다는 내 주석은 정확하다. 원소는 이미 숫자지만 기본 sort가 문자열 표현 기준으로 비교하기 때문이다. 04장에서 배운 비교 함수로 `arr.sort((a,b) => a-b)`를 쓰면 [3,5,10]이 된다. 반대는 b-a다. sort().reverse()를 써도 최초 sort가 숫자 오름차순이 아니면 숫자 내림차순을 보장하지 못한다. [MDN sort](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/sort)

원본의 `const sort = arr.sort()`는 같은 배열을 가리킨다. 이어 arr.sort().reverse()를 실행하면 sort로 읽는 순서도 달라진다. const는 배열 내용 변경을 막지 않는다.

<a id="section-5"></a>

## 5. split으로 실제 query 값 찾기

### 강사님 코드

출처: `teacher/workspace_html/javascript/06_array.html` 196–208행 · **원본 발췌**

```javascript
        let temp = url.split('?')
        console.log(temp)
        let qs = temp[1]
        qs = qs.split('&')
        console.log(qs)
        for(let i=0; i<qs.length; i++){
            let q = qs[i].split('=')
            let name = q[0]
            let value = q[1]
            if(name == 'query'){
                console.log(value)
            }
        }
```

### 내 코드

출처: `me/workspace_html/javascript/06_array.html` 222–234행 · **원본 발췌**

```javascript
            let temp = url.split('?')
            console.log('temp', temp)
            let qs = temp[1]
            qs = qs.split('&')
            console.log('qs', qs)
            for(let i=0; i<qs.length; i++) {
                let q = qs[i].split('=')
                let name = q[0]
                let value = q[1]
                if(name == 'query') {
                    console.log(value)
                }
            }
```

url은 각 발췌 바로 앞에 선언한 원본 검색 주소다. 두 주소의 마지막 ackey 값은 다르지만 query는 모두 1234다. ?로 주소와 쿼리 부분 분리 → &로 항목 분리 → =로 이름과 값 분리 → name이 query이면 값 출력의 순서다. 내 코드는 중간 배열에 temp·qs 라벨을 출력해 디버깅하기 좋다.

이 방식은 **수업의 단순 문자열 조건에 대한 풀이**다. 물음표가 없으면 temp[1]이 없고, 값 안의 =나 인코딩·동일 이름 여러 개를 일반적으로 처리하지 않는다. URLSearchParams를 기본 정답으로 바꾸지 않고 추가 학습으로 둔다. 내 236–243행 이메일 분리도 같은 split 연습이며 어떤 이메일 형식이든 검증하는 코드가 아니다.

<a id="section-6"></a>

## 6. 실습 풀이에서 유지할 점과 고칠 점

강사님 211–242행에는 배열 자동 생성·개수 세기·미완주자·예약·중복 없는 로또 문제가 있고, 다음은 내 실제 풀이를 기준으로 평가한다.

| 내 원본 | 결과·판단 |
| --- | --- |
| 276–283행 | push와 반복으로 1–10 배열 생성 성공 |
| 289–300행 | [3,4,7,5,1,6]의 홀수 4개. 값도 함께 출력한 점이 좋음 |
| 303–313행 | 4보다 큰 수는 7·5·6 세 개. 출력 제목 ‘홀수의 개수’를 ‘4보다 큰 수의 개수’로 교정 |
| 318–338행 | 답 3을 문자열에서 미리 제거하는 시도와 너무 이른 break가 섞임. 완성 풀이로 소개하지 않음 |
| 342–386행 | 참가자마다 검색 여부를 초기화하여 미완주자 3을 찾음. 다만 []로 시작한 결과에 +=를 써 문자열로 바뀜 |
| 411–426행 | 무작위로 고른 같은 이름을 누적하므로 미완주자 루피를 찾는 풀이가 아님 |
| 438–458행 | 예약 코드가 주석 처리된 미완성 시도. 중복 예약·현황·잔여 좌석 미완료 |
| 518–527행 | 숫자야구 문제와 구상만 있음 |

### 미완주자 찾기 — 내 코드의 핵심

강사님 파일에는 대응 문제 조건만 있고 완성 코드가 없다.

출처: `me/workspace_html/javascript/06_array.html` 366–386행 · **원본 발췌**

```javascript
            for(let j=0; j<entry.length; j++) {
                let result_check = false

                for(let i=0; i<finisher.length; i++) {
                    if(entry[j] == finisher[i]) {
                        result_check = true
                        break;
                    } else if(entry[j] !== finisher[i]){
                        result_check = false
                    }
                }

                if(result_check == true) {
                    result_success += entry[j]+' '
                } else if(result_check == false) {
                    result_fail += entry[j]+' '
                }
            }
            // console.log(result_rand)
            console.log(`완주자 : ${result_success}`)
            console.log(`미완주자 : ${result_fail}`)
```

각 참가자를 볼 때 result_check=false로 새로 시작하고, 완주 목록에서 찾으면 true와 break를 쓰는 구조가 좋다. 매번 다른 완주자와 비교할 때의 else if는 없어도 된다. 배열 결과를 유지하려면 += 대신 앞에서 배운 push를 쓴다. 아래는 **이 원본을 교정한 설명 예제**이며, 이름이 서로 중복되지 않는 수업 조건을 전제로 한다.

```javascript
const entry = [1,2,3,4,5];
const finisher = [2,4,5,1];
const result_fail = [];
for (let j=0; j<entry.length; j++) {
    let found = false;
    for (let i=0; i<finisher.length; i++) {
        if (entry[j] === finisher[i]) {
            found = true;
            break;
        }
    }
    if (!found) result_fail.push(entry[j]);
}
console.log(result_fail); // [3]
```

### 중복 없는 로또 — 내 마지막 풀이

강사님 문제는 1–45에서 중복 없이 여섯 수다. 내 q5_lotto는 검사 중 마지막 원소를 교체하면서 앞서 검사한 값과 새 중복이 생길 수 있다. q6_lotto는 새로 추가할 인덱스 i의 아직 없는 값을 비교하므로 이전 원소들을 검사하지 못한다. 마지막 q7_lotto는 후보를 전체 기존 원소와 비교한다.

출처: `me/workspace_html/javascript/06_array.html` 496–516행 · **원본 발췌**

```javascript
            let q7_lotto = []
            let q7_number;
            
            for(let i=0; i<6; i++) {
                q7_number = parseInt(Math.random() * 45) + 1
                let q7_check = false;
                
                for(let j=0; j<q7_lotto.length; j++) {
                    if(q7_lotto[j] === q7_number) {
                        q7_check = true;
                        break;
                    } 
                }

                if(!q7_check) {
                    q7_lotto.push(q7_number)
                } else {
                    i--;
                }
            }
            console.log(`- - - - - 문제7 - - - - -\n나의 번호 : ${q7_lotto.sort()}`)
```

후보가 중복이면 i--로 성공 횟수를 되돌리고, for의 i++와 상쇄시켜 같은 차례를 다시 시도한다. 중복이 없을 때만 push한다. 이 개선 과정은 내 코드의 장점이다. 마지막 sort()는 숫자 크기순이 아니므로 `q7_lotto.sort((a,b) => a-b)`로 바꾸면 읽기 좋다. 임의 추출의 종료까지 최대 몇 번이라고 보장하는 코드는 아니다.

강사님 숫자야구 주석의 정답 123·입력 367은 1스트라이크가 아니라 **1볼**이다. 3은 존재하지만 위치가 다르기 때문이다. 문제 조건도 코드처럼 재검토한다.

<a id="section-7"></a>

## 7. 짧은 복습

1. const 배열에서 push는 가능한가?
2. [1,2,3,4]의 slice(1,3)과 splice(1,3)은 어떻게 다른가? 각각 새 원본으로 시작한다.
3. result_fail을 배열로 유지하려면 +=와 push 중 무엇을 쓰는가?

<details>
<summary>정답 확인</summary>

1. 가능하다. 같은 이름에 다른 배열을 재대입하는 것과 다르다.
2. slice는 [2,3] 반환·원본 유지. splice는 [2,3,4] 반환·원본 [1]로 변경.
3. push다.

</details>

<a id="section-8"></a>

## 추가로 알면 좋은 것

Array.from·Set·URLSearchParams, 중복 이름까지 다루는 빈도표, 완성된 예약 앱, splice 삽입·교체 확장은 이 장의 기본 풀이와 분리한다. 실제 배열·반복·조건문으로 작성한 풀이를 먼저 이해한다.

---

[장별 연습문제 풀기](실습/연습문제/06_JavaScript_배열과_배열메서드_연습문제.md) · [다음: 날짜](07_JavaScript_Date와_날짜처리.md)

