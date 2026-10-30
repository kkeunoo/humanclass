# 06. 배열과 메서드 — 원본 상태와 반환값

[JavaScript 목차](README.md) · [읽기 안내](00_JavaScript_V3_동작_백과_읽기법.md)

여러 값을 순서대로 저장하고 번호로 꺼내는 자료가 배열이다. 메서드를 호출할 때는 ‘원본이 어떻게 바뀌는가’와 ‘호출한 쪽에 무엇을 돌려주는가’를 따로 적는다. 이 두 질문으로 추가·삭제·복사·정렬을 연결한다.

<a id="chapter-toc"></a>

**이 장의 목차:** [목표](#learn) · [개념](#concepts) · [예제](#example) · [내 코드](#my-code) · [연결](#connections) · [평가](#review) · [비교](#teacher) · [결과·실험](#results) · [TIP·출처](#tips) · [복습](#practice)

<a id="learn"></a>

## 1. 이 장에서 배울 것

인덱스·length·중첩 배열·const를 구분한다. 각 메서드의 변경·반환을 비교하고 실제 query 분리·미완주자·로또 풀이를 평가한다.

입력·현재 상태·실행 순서·결과를 분리해 설명한다. 실제 수업 원본은 아래에 표시하고, 원본에 없는 선택 학습은 9절 TIP에 둔다.

<a id="concepts"></a>

## 2. 무엇이며, 왜 필요한가

배열의 첫 인덱스는0이며 length는 마지막 인덱스+1과 연결된다. 인덱스는 실제 메모리 주소가 아니다. 숫자·문자열·불리언·다른 배열을 함께 담을 수 있고 typeof는object다. 메서드는 객체에 속한 함수이므로 arr.push(값)은 arr를 대상으로 호출한다.

const 배열도 arr[0]=10이나 push는 가능하다. arr라는 이름에 다른 배열을 재대입하는 것과 배열 내부 변경이 다르기 때문이다. 반대로 let은 새 배열로 재대입할 수 있다. ‘재선언’과 ‘재대입’도 구별한다.

| 메서드 | 원본 변경 | 반환 |
| --- | --- | --- |
| push·unshift |뒤·앞 추가 |새 길이 |
| pop·shift |뒤·앞 제거 |제거 값,빈 배열이면undefined |
| reverse·sort |순서 변경 |같은 배열 |
| slice(시작,끝) |변경 안 함 |끝 제외한 새 배열 |
| splice(시작,개수) |구간 제거 |제거된 값의 배열 |
| indexOf |변경 안 함 |첫 인덱스 또는-1 |
| join |변경 안 함 |구분자로 연결한 문자열 |

split은 문자열을 나누어 배열을 만드는 **문자열 메서드**다. push로 뒤에 넣고 shift로 앞에서 꺼내면 먼저 넣은 값부터 나오지만, unshift와 shift는 같은 앞쪽이라 최근 값부터 나온다. slice는 얕은 복사여서 중첩 객체까지 독립 복사가 되지는 않는다.

> 📚 **출처 · 본문 설명 확인:** [MDN Array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array), [slice](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/slice), [sort](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/sort). 배운 기능의 뜻을 확인한 근거다. 예제·표·풀이 흐름은 수업 코드를 바탕으로 새로 작성했으며 외부 문장을 직접 인용하지 않았다. 확인일: 2026-10-28.

<a id="example"></a>

## 3. 작은 예제로 먼저 이해하기

**새 설명 예제 · 전체 스크립트.** [HTML 실행 파일](실습/책형_복습/06_JavaScript_배열과_배열메서드.html)과 같은 폴더의 [JS 파일](실습/책형_복습/06_JavaScript_배열과_배열메서드.js)을 함께 내려받는다. HTML을 브라우저로 열고 Console에서 결과를 확인한다. script는 필요한 HTML 뒤에 연결한다. 콘솔 출력은 페이지 본문에 자동으로 쓰이지 않는다.

```javascript
const numbers = [10, 20];
const length = numbers.push(30);
console.log(length);
console.log(numbers.join(','));
const removed = numbers.pop();
console.log(removed);
console.log(numbers.join(','));
const copied = numbers.slice(0, 1);
copied[0] = 99;
console.log(copied.join(','));
console.log(numbers.join(','));
```

push가 반환한3은 추가한 값30이 아니라 새 길이다. pop은30을 제거하고 그 값을 돌려준다. slice(0,1)은 인덱스0만 담은 새 배열이어서 copied[0]을99로 바꿔도 numbers의10은 그대로다. 예제는 숫자 원소만 쓰며 중첩 객체 공유까지 실험한 것은 아니다. join은 출력 문자열을 일정하게 보려는 수업 메서드 사용이다.

**예상 출력 또는 관찰:**

```text
3
10,20,30
30
10,20
99
10,20
```

<a id="my-code"></a>

## 4. 내가 작성한 코드를 따라 읽기

아래는 원본의 일부다. 원본에 의존하는 앞 선언·HTML·함수는 다음 절의 연결까지 읽는다. 주석의 잘못된 표현도 원문대로 보존하고 설명에서 교정한다.

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_html/javascript/06_array.html` 33–49행

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

**발췌 바로 풀이:** 강사님은 arr3를 let으로 선언하여 원소 변경과 배열 전체 재대입을 모두 실행했다. 내 코드는 const로 선언하고 재대입을 주석 처리했다. **const여도 arr3[0]=10은 가능하다.** const가 금지하는 것은 arr3라는 이름에 다른 값을 재대입하는 일이다. 내 20행의 ‘중복 선언 불가’와 재대입 불가를 구분한다. 01장의 선언·대입 설명과 연결되는 좋은 비교다.

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_html/javascript/06_array.html` 106–110행

```javascript
            for(let j=0; j<음식.length; j++) {
                for(let i=0; i<음식[j].length; i++) {
                    console.log(음식[j][i])
                }
            }
```

**발췌 바로 풀이:** 같은 구조다. 음식은 앞에서 만든 양식·중식·일식 배열을 원소로 가진다. 음식.length는 3, 음식[0].length는 5, 음식[1].length는 7이다. 바깥은 종류를, 안쪽은 해당 종류의 메뉴를 순회한다. 길이를 5로 고정하면 중식 일부를 빠뜨린다. 음식[0][2]는 첫 종류의 세 번째 메뉴인 스테이크다. 내 주석의 ‘1차원 배열에 [][]’는 이 예제에서는 **배열 안에 배열을 넣은 중첩 배열**로 고친다.

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_html/javascript/06_array.html` 114–133행

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

**발췌 바로 풀이:** 둘 다 [1,2,3,4] → push 후 [1,2,3,4,5] → unshift 후 [0,1,2,3,4,5]가 된다. pop은 5를 꺼내고 shift는 0을 꺼내므로 마지막 배열은 다시 [1,2,3,4]다. 반환값 pop·shift와 남은 배열을 함께 출력한 점이 양쪽 모두 좋다.

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_html/javascript/06_array.html` 186–189행

```javascript
            // 3, 5, 10으로 정렬이 되어야 하는데 10, 3, 5 순으로 정렬됨
            // 숫자로 바꾸면 되겠지만, 배열 안에 있는건 이미 숫자이기 때문에 함수로 나중에 바꾸어야 함
            arr = [10, 5, 3]
            console.log(arr.sort())
```

**발췌 바로 풀이:** 양쪽 결과는 [10,3,5]다. 숫자로 변환하여 다시 넣는 것만으로 해결되지 않는다는 내 주석은 정확하다. 원소는 이미 숫자지만 기본 sort가 문자열 표현 기준으로 비교하기 때문이다. 04장에서 배운 비교 함수로 `arr.sort((a,b) => a-b)`를 쓰면 [3,5,10]이 된다. 반대는 b-a다. sort().reverse()를 써도 최초 sort가 숫자 오름차순이 아니면 숫자 내림차순을 보장하지 못한다. [MDN sort](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/sort)

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_html/javascript/06_array.html` 222–234행

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

**발췌 바로 풀이:** url은 각 발췌 바로 앞에 선언한 원본 검색 주소다. 두 주소의 마지막 ackey 값은 다르지만 query는 모두 1234다. ?로 주소와 쿼리 부분 분리 → &로 항목 분리 → =로 이름과 값 분리 → name이 query이면 값 출력의 순서다. 내 코드는 중간 배열에 temp·qs 라벨을 출력해 디버깅하기 좋다.

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_html/javascript/06_array.html` 366–386행

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

**발췌 바로 풀이:** 각 참가자를 볼 때 result_check=false로 새로 시작하고, 완주 목록에서 찾으면 true와 break를 쓰는 구조가 좋다. 매번 다른 완주자와 비교할 때의 else if는 없어도 된다. 배열 결과를 유지하려면 += 대신 앞에서 배운 push를 쓴다.

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_html/javascript/06_array.html` 496–516행

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

**발췌 바로 풀이:** 후보가 중복이면 i--로 성공 횟수를 되돌리고, for의 i++와 상쇄시켜 같은 차례를 다시 시도한다. 중복이 없을 때만 push한다. 이 개선 과정은 내 코드의 장점이다. 마지막 sort()는 숫자 크기순이 아니므로 `q7_lotto.sort((a,b) => a-b)`로 바꾸면 읽기 좋다. 임의 추출의 종료까지 최대 몇 번이라고 보장하는 코드는 아니다.

내 arr3는const라 원소 변경은 하고 전체 재대입을 주석으로 남겼다. 강사님 let과의 차이가 선언·값 변경을 이해하기 좋다. 음식 중첩 반복은 바깥 종류3개, 안쪽은 해당 배열의 실제 length를 사용한다. 첫 종류5개·둘째7개라 길이를5로 고정하면 일부를 놓친다. 음식[0][2]는 첫 종류의 세 번째 메뉴다.

추가·삭제는[1,2,3,4]→push5→unshift0→pop5→shift0으로 다시 처음 값 목록으로 돌아간다. 기본 sort의[10,5,3]은[10,3,5]다. 원소가 숫자여도 기본 비교는 문자열 표현을 보기 때문이다. 내 ‘이미 숫자’ 메모는 좋은 관찰이며, 숫자 오름차순은 비교 함수 a-b를 사용한다.

query 분리는 ?→&→= 순으로 배열을 만들어 이름이query인 값을 출력한다. 양쪽 원본 query는1234이며 내 temp·qs 라벨은 중간 상태를 찾기 좋다. 미완주자에서는 참가자마다 검색 상태를 다시false로 하고 찾으면break한다. 결과를[]로 시작했어도 +=를 쓰면 문자열로 바뀌므로 배열 유지 목적에는push가 맞다. 마지막 q7 로또는 모든 기존 값과 중복을 검사한 뒤 추가해 앞선 시도보다 개선되었다.

<a id="connections"></a>

## 5. 선언·호출·파일이 연결되는 흐름

배열 이름 → 메서드 호출 → 원본 상태 변화 → 반환값 저장 → 출력 순서다. `const sort=arr.sort()`는 복사본이 아닌 같은 배열이라 뒤 reverse가 sort로 읽는 순서에도 반영된다. query 발췌의 url, 음식의 하위 배열, 미완주자의 entry·finisher·결과 초기 배열은 앞 선언에서 온다. 발췌만 독립 실행하려면 이 초기값도 준비한다. 문자열+배열은 문자열 변환이 섞이므로 console.log의 여러 인자와도 구분한다.

<a id="review"></a>

## 6. 잘한 점·아쉬운 점·개선 방향

**잘한 점:** 상태와 반환값을 같이 출력했고, 검색 성공flag·중복 후보 검사로 풀이를 개선했다. **교정:** 모든 메서드가 원본을 바꾼다는 메모와 고정Byte·Stack/Heap크기 메모는 일반 규칙이 아니다. **한계:** query의 단순split은?가 없거나 값에=·인코딩·동일이름이 있는 일반URL을 처리하지 않는다. **개선 방향:** 결과 자료형을 끝까지 유지하고 입력 조건을 명시한다. 숫자 로또 정렬도 기본sort 대신 비교 함수를 적용한다.

개선안은 원본을 수정한 결과가 아니다. 실제 오류, 수업용 단순화, 목적에 따른 선택을 구별해 판단한다.

<a id="teacher"></a>

## 7. 강사님 코드가 도움이 되는 비교

출처: `D:/workspace_teacher/workspace_html/javascript/06_array.html` 257–258행

```javascript
        arr = [1,2,3,4,5]
        arr.splice(2, 1) // 2번 index부터 몇개를 뺄 것인가?
```

위 강사님 splice는 내 파일에 같은 실행 코드가 없어 삭제 기능의 수업 근거로 필요한 부분만 인용한다. [1,2,3,4,5]에서 splice(2,1)은 값3을 제거해 원본[1,2,4,5], 반환[3]이다. 원본은 반환을 저장하지 않았다. 삽입·교체 전체 변형까지 배운 것으로 넓히지는 않는다. 나머지 같은 메서드 코드는 중복 인용하지 않는다.

<a id="results"></a>

## 8. 결과를 추적하고 한 가지 바꾸기

| 원본 학습 기록 | 판단 |
| --- | --- |
| arr[60] 읽기·쓰기 |읽기는undefined,쓰기후length61·중간은0채움아님 |
| arr['문자'] 추가 |이름속성,길이62로늘리는인덱스아님 |
| slice(2,5) |[0~6]에서[2,3,4],끝제외 |
| 배열 생성·개수 |1~10생성,홀수4개,4보다큰값3개 |
| 미완주자 첫시도 |이른break·답미리제거시도,완성아님 |
| 미완주자 검색형 |3을찾지만+=로결과문자열화 |
| 무작위 이름 누적 |미완주자찾기와다름 |
| 예약·숫자야구 |주석·구상·미완성,완료로표시안함 |

q5 로또는 검사 중 값을 바꾸어 앞선 값과 새 중복이 생길 수 있고, q6는 아직 없는 인덱스를 비교한다. 마지막 q7은 중복이면 i--로 성공 차례를 되돌려 for의i++와 상쇄한다. 최대 시도 횟수까지 보장하는 것은 아니다. 미완주자 검색 예제도 이름 중복 없는 조건이며 중복 인원 전체를 처리하는 일반 해법은 아니다.

| 한 가지 변경 | 예상 | 이유 |
| --- | --- | --- |
| push값만40 |길이3·제거40 |반환길이와값분리 |
| 원래slice끝만2 |두원소복사·원본유지 |끝제외 |
| 원래copied를numbers로직접대입 |copied수정이원본에반영 |같은배열참조 |

slice의 끝과 splice의 개수를 혼동하지 않는다. indexOf는 값·자료형을 구분한다. 미완주자 출력이 맞더라도 결과가 문자열인지 배열인지 확인한다. sort().reverse()도 기본 sort가 숫자순이 아니면 숫자 내림차순을 보장하지 않는다.

<a id="tips"></a>

## 9. 추가로 알면 좋은 것과 출처

> 💡 **TIP · 수업 범위 밖:** URLSearchParams·Set·새 복사 정렬 API·중복 이름을 고려한 일반 해법은 추가 학습이다. 기본 정답을 새 API로 통째로 바꾸지 않는다.



이 절의 확장은 기본 문제의 필수 조건이 아니다. 📚 출처가 있다는 것과 수업 밖 기능이라는 것은 다른 구분이다.

<a id="practice"></a>

## 10. 복습과 빠른 정리

1. push는 추가 값과 길이 중 무엇을 반환하는가?
2. const 배열의 원소를 바꿀 수 있는가?
3. slice와 splice의 두 번째 값은 같은 뜻인가?

<details>
<summary>짧은 풀이 — 먼저 답한 뒤 확인</summary>

새 길이다. const는 이름 재대입을 막으며 원소 변경은 가능하다. slice는 끝 인덱스 제외, splice는 제거 개수다.

</details>

| 질문 | 확인 |
| --- | --- |
| 원본바뀜 | 변경형/비변경형 |
| 반환 | 길이·값·배열·문자열 |
| 복사 | 얕은복사·같은참조 |
| 정렬 | 기본문자비교·비교함수 |

[장별 연습문제](실습/연습문제/06_JavaScript_배열과_배열메서드_연습문제.md)에서 예상·설명·수정을 이어 간다. 다음은 [Date](07_JavaScript_Date와_날짜처리.md)다.

<!-- 이전 색인 이동 주소 보존 -->
<a id="section-1"></a>
<a id="section-2"></a>
<a id="section-3"></a>
<a id="section-4"></a>
<a id="section-5"></a>
<a id="section-6"></a>
<a id="section-7"></a>
<a id="section-8"></a>

[이 장의 목차](#chapter-toc)에서 현재 설명을 찾는다.
