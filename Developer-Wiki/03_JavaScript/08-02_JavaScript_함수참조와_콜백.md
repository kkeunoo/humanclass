# 08-02. 함수 참조와 콜백 — 함수 전달과 호출 결과

[JavaScript 목차](README.md) · [읽기 안내](00_JavaScript_V3_동작_백과_읽기법.md)

함수를 지금 실행할 때는 괄호를 붙이고, 실행을 다른 곳에 맡기려면 함수 값을 전달한다. 괄호 하나의 차이가 무엇을 넘기는지 바꾼다.

<a id="chapter-toc"></a>

**이 장의 목차:** [목표](#learn) · [개념](#concepts) · [예제](#example) · [내 코드](#my-code) · [연결](#connections) · [평가](#review) · [비교](#teacher) · [결과·실험](#results) · [TIP·출처](#tips) · [복습](#practice)

<a id="learn"></a>

## 1. 이 장에서 배울 것

함수 값·호출·반환값을 구분한다. 전달받은 함수가 어디에서 실제 호출되는지 찾고 콜백이 항상 비동기는 아님을 설명한다.

입력·현재 상태·실행 순서·결과를 분리해 설명한다. 실제 수업 원본은 아래에 표시하고, 원본에 없는 선택 학습은 9절 TIP에 둔다.

<a id="concepts"></a>

## 2. 무엇이며, 왜 필요한가

함수도 값으로 변수에 담을 수 있다. let later=sayHi는 같은 함수를 다른 이름으로 가리키며 본문을 복사한 새 함수 정의는 아니다. later()에서 호출한다. 함수 표현식은 변수에 함수 값을 넣는 방식이고 함수 선언문과 모든 선언 규칙이 같은 것은 아니다.

콜백은 다른 함수에 전달하여 실행을 맡긴 함수다. ‘나중’이라는 말은 반드시 시간이 지난 뒤라는 뜻이 아니다. 받는 함수가 현재 호출 중 즉시 실행할 수도 있다. 원본 test는 fn이함수인지 확인하고 fn()을 바로 호출한다.

| 표현 | 전달하는 것 | 실행 |
| --- | --- | --- |
| test1 |함수 자체 |전달만으로본문실행안함 |
| test1() |호출 결과 |먼저본문실행 |
| fn() |받은 함수 호출 |이위치에서본문실행 |

전달받은 값을 출력만 하는 test2는 함수 참조를 받아도 자동 호출하지 않는다. 실행 여부는 받은 코드 안에서 괄호로 호출하는 지점을 찾아 판단한다.

> 📚 **출처 · 본문 설명 확인:** [MDN 함수](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Functions)와 [콜백 함수](https://developer.mozilla.org/en-US/docs/Glossary/Callback_function). 배운 기능의 뜻을 확인한 근거다. 예제·표·풀이 흐름은 수업 코드를 바탕으로 새로 작성했으며 외부 문장을 직접 인용하지 않았다. 확인일: 2026-10-28.

<a id="example"></a>

## 3. 작은 예제로 먼저 이해하기

**새 설명 예제 · 전체 스크립트.** [HTML 실행 파일](실습/책형_복습/08-02_JavaScript_함수참조와_콜백.html)과 같은 폴더의 [JS 파일](실습/책형_복습/08-02_JavaScript_함수참조와_콜백.js)을 함께 내려받는다. HTML을 브라우저로 열고 Console에서 결과를 확인한다. script는 필요한 HTML 뒤에 연결한다. 콘솔 출력은 페이지 본문에 자동으로 쓰이지 않는다.

```javascript
function sayHi() {
    console.log('안녕');
}
function run(fn) {
    console.log('시작');
    console.log(typeof fn);
    if (typeof fn === 'function') {
        fn();
    }
    console.log('끝');
}
const later = sayHi;
run(later);
```

later에 담을 때는 안녕이 출력되지 않는다. run이 시작을 출력하고 fn의 종류를 확인한 다음 fn()에서 sayHi를 호출한다. 이 호출이 끝나 돌아와 끝을 출력한다. 모든 과정이 현재 호출 안에서 순서대로 이루어져 비동기 예약은 없다.

**예상 출력 또는 관찰:**

```text
시작
function
안녕
끝
```

<a id="my-code"></a>

## 4. 내가 작성한 코드를 따라 읽기

아래는 원본의 일부다. 원본에 의존하는 앞 선언·HTML·함수는 다음 절의 연결까지 읽는다. 주석의 잘못된 표현도 원문대로 보존하고 설명에서 교정한다.

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_html/javascript/08_function.html` 144–152행

```javascript
            // fn이 noName 함수를 인자로 받았는데, 이럴 때 fn을 '콜백함수'라고 부른다.
            function test( fn ) {
                console.log('test 실행중')
                console.log(typeof fn)
                if (typeof fn == 'function') {
                    fn()
                }
            }
            test( noName )
```

**발췌 바로 풀이:** 같은 구조다. noName을 fn으로 받아 함수인지 확인한 뒤 fn()으로 실행한다. 다른 함수에 전달해 실행을 맡긴 함수를 콜백이라고 한다. **콜백이 반드시 나중에 비동기로 실행되는 것은 아니다.** 여기서는 test가 호출되는 동안 즉시 fn을 실행한다.

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_html/javascript/08_function.html` 191–204행

```javascript
            function test1() {
                console.log('test1')
                return 3
            }
            function test2( a ) {
                console.log('test2')
                console.log(a)
            }

            // ()가 있으면 실행의 결과물을 주는것이고, 괄호가 없으면 함수의 내용 자체가 들어감
            test2( test1() )
            // 즉 x = test1()_실행 > test2(x) 가 된 것
            test2 ( test1 )
            // x = test1 함수 내용만 넣기 > text2(x)
```

**발췌 바로 풀이:** test1은 test1문구를 출력하고3을 반환한다. test2는 test2문구와 받은a를 출력할 뿐a()로 호출하지 않는다. 따라서 첫 호출은 test1이 먼저 실행되어3을 전달하고, 둘째는 함수를 전달하되 그 본문은 실행하지 않는다.

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_html/javascript/08_function.html` 133–135행

```javascript
            let noName = function() {
                console.log('익명함수')
            }
```

내 test(noName)은 fn으로 noName을 받아 함수이면 호출한다. 함께 실은 noName 정의는 익명함수라는 글자를 출력하며 반환값은undefined다. test2(test1())은 먼저test1을 실행해3을 넘기지만 test2(test1)은함수자체를 넘긴다. test2는받은a를출력만하고a()로호출하지않아두번째의test1본문은실행되지않는다.

<a id="connections"></a>

## 5. 선언·호출·파일이 연결되는 흐름

noName 정의 → test(noName) 전달 → 매개변수fn → typeof확인 → fn() → noName본문 → test복귀 순서다. 이 흐름에서 정의가 빠지면 처음 읽는 사람은 fn이 무엇인지 알 수 없으므로 원본 정의를 함께 실었다. 여러 파일을 연결하는 실제 프로젝트에서도 사용처만 보여 주지 말고 그 함수 정의와 반환까지 찾아 읽는다.

<a id="review"></a>

## 6. 잘한 점·아쉬운 점·개선 방향

**잘한 점:** 내 주석은 괄호가 있으면 실행 결과를 전달한다는 차이를 짚었다. **보완:** 괄호 없이 ‘함수 내용이 들어감’은 텍스트 복사보다 함수 값을 전달한다고 이해하는 편이 정확하다. **주의:** console.log변경 실험이 뒤 출력에 영향을 줄 수 있으므로 독립 예제로 확인한다.

개선안은 원본을 수정한 결과가 아니다. 실제 오류, 수업용 단순화, 목적에 따른 선택을 구별해 판단한다.

<a id="teacher"></a>

## 7. 강사님 코드가 도움이 되는 비교



강사님은 중간x에함수 또는결과를 담아 같은 흐름을 다시 실행한다. 내 코드는 그 반복 실행을 주석 설명으로 남겨 출력이 덜 반복된다. 어느 방식이 필요한지는 중간값 관찰 목적에 달렸으며 같은 함수를 중복 인용하지 않는다.

<a id="results"></a>

## 8. 결과를 추적하고 한 가지 바꾸기

| 원본 호출 | 출력 흐름 | 이유 |
| --- | --- | --- |
| test2(test1()) |test1→test2→3 |인수계산이먼저 |
| test2(test1) |test2→함수표시 |test2는a호출안함 |

양쪽 원본은 원래 console.log를 c1에 저장한 뒤 숫자3과 새 함수로 바꾸는 실험도 한다. 숫자인 동안 호출하면 함수가 아니어서 오류지만 해당 호출은 주석이다. 새 함수 안에서 다시 console.log를 부르면 자기 자신을 반복 호출할 수 있어 원본은 c1을 쓴다. 실습 문구는 실제 침입 증거가 아니다. 복구하려면 console.log=c1을 쓰는 설명용 수정을 할 수 있다. 원본 desc의 sort().reverse는 배열 장과 같이 원본 변경·기본 문자 정렬의 한계를 가진다.

| 한 가지 변경 | 예상 | 이유 |
| --- | --- | --- |
| run(later)를run(later())로 |안녕→시작→undefined→끝 |먼저실행결과전달 |
| 원래run의fn()만제거 |시작·function·끝 |전달해도호출안함 |
| 원래run인수만3으로 |시작·number·끝 |종류검사로호출안함 |

함수로 받은 줄 알았는데 undefined이면 호출 괄호를 확인한다. 로그가 평소와 다르면 출력 함수를 덮는 원본 실험과 섞였는지 본다. 콜백의 정의·전달·실제 호출 위치를 각각 찾는다.

<a id="tips"></a>

## 9. 추가로 알면 좋은 것과 출처

> 💡 **TIP · 수업 범위 밖:** this·바인딩·고급 함수 조합·범용 래퍼 설계는 추가 학습이다. 콜백이라는 이름만으로 비동기 큐 전체를 미리 요구하지 않는다.



이 절의 확장은 기본 문제의 필수 조건이 아니다. 📚 출처가 있다는 것과 수업 밖 기능이라는 것은 다른 구분이다.

<a id="practice"></a>

## 10. 복습과 빠른 정리

1. 나중에 호출하도록 함수 값을 넘기려면 fn과 fn() 중 무엇인가?
2. 콜백은 반드시 비동기인가?
3. test2가 함수를 받으면 자동 호출되는가?

<details>
<summary>짧은 풀이 — 먼저 답한 뒤 확인</summary>

fn을 넘긴다. fn()은 지금 호출한 결과다. 콜백은 즉시 호출될 수 있다. test2처럼 받은 값을 출력만 하면 자동 호출하지 않는다.

</details>

| 찾을 것 | 질문 |
| --- | --- |
| 정의 |무슨일을하나 |
| 전달 |함수값인가결과인가 |
| 호출 |어디서괄호를붙이나 |
| 출력실험 |기본log가바뀌었나 |

[장별 연습문제](실습/연습문제/08-02_JavaScript_함수참조와_콜백_연습문제.md)에서 예상·설명·수정을 이어 간다. 다음은 [타이머](08-03_JavaScript_타이머와_취소.md)다.

<!-- 이전 색인 이동 주소 보존 -->
<a id="section-1"></a>
<a id="section-2"></a>
<a id="section-3"></a>
<a id="section-4"></a>
<a id="section-5"></a>

[이 장의 목차](#chapter-toc)에서 현재 설명을 찾는다.
