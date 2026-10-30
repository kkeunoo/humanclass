# 08. 함수 — 입력을 받아 계산하고 반환하기

[JavaScript 목차](README.md) · [읽기 안내](00_JavaScript_V3_동작_백과_읽기법.md)

같은 계산을 여러 곳에서 하려면 코드 묶음에 이름을 붙이고 필요한 값을 전달한다. 함수는 작은 작업 단위를 만들며, 출력만 하는 것과 다음 계산에 쓸 결과를 반환하는 것은 다르다.

<a id="chapter-toc"></a>

**이 장의 목차:** [목표](#learn) · [개념](#concepts) · [예제](#example) · [내 코드](#my-code) · [연결](#connections) · [평가](#review) · [비교](#teacher) · [결과·실험](#results) · [TIP·출처](#tips) · [복습](#practice)

<a id="learn"></a>

## 1. 이 장에서 배울 것

정의·호출·매개변수·인수·반환을 구분한다. 함수 정의부터 호출과 결과 사용까지 따라가고 범위·기본값을 설명한다.

입력·현재 상태·실행 순서·결과를 분리해 설명한다. 실제 수업 원본은 아래에 표시하고, 원본에 없는 선택 학습은 9절 TIP에 둔다.

<a id="concepts"></a>

## 2. 무엇이며, 왜 필요한가

function double(number){ return number*2; }는 함수 정의다. double(3)은 호출이고,3은 인수,number는 전달값을 받는 매개변수다. 정의만 했다고 본문이 실행되지는 않는다. 호출하면 본문에서 계산하고 return이 결과를 돌려주며 그 호출을 끝낸다.

| 용어 | 코드에서 찾을 것 |
| --- | --- |
| 매개변수 |정의 괄호 안의 받을 이름 |
| 인수 |호출 괄호 안의 전달값 |
| 지역변수 |함수 안에서 만든 이름 |
| 반환값 |호출 결과로 받은 값 |
| 출력 |Console에 보여 준 내용 |

console.log로200을 보여 준다고 그 함수가200을 반환하는 것은 아니다. 명시적 반환이 없으면 호출 결과는undefined다. 반대로 return200을 한 함수도 호출한 쪽이 출력하지 않으면 Console에 자동으로200이 나오지 않는다.

함수 안 지역변수와 바깥의 같은 이름은 서로 다른 범위일 수 있다. 안에서는 바깥을 읽을 수 있지만 바깥에서 안의 이름을 그대로 읽을 수는 없다. 기본 매개변수 y=0은 전달값이undefined일 때 사용하며 null까지 자동으로0으로 바꾸는 기능은 아니다.

> 📚 **출처 · 본문 설명 확인:** [MDN 함수](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Functions)와 [기본 매개변수](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Default_parameters). 배운 기능의 뜻을 확인한 근거다. 예제·표·풀이 흐름은 수업 코드를 바탕으로 새로 작성했으며 외부 문장을 직접 인용하지 않았다. 확인일: 2026-10-28.

<a id="example"></a>

## 3. 작은 예제로 먼저 이해하기

**새 설명 예제 · 전체 스크립트.** [HTML 실행 파일](실습/책형_복습/08_JavaScript_함수와_콜백_타이머.html)과 같은 폴더의 [JS 파일](실습/책형_복습/08_JavaScript_함수와_콜백_타이머.js)을 함께 내려받는다. HTML을 브라우저로 열고 Console에서 결과를 확인한다. script는 필요한 HTML 뒤에 연결한다. 콘솔 출력은 페이지 본문에 자동으로 쓰이지 않는다.

```javascript
function showDouble(number) {
    console.log(number * 2);
}
function getDouble(number) {
    return number * 2;
}
const shown = showDouble(3);
console.log(shown);
const result = getDouble(3);
console.log(result + 1);
```

showDouble은6을 출력하지만 반환하지 않아 shown은undefined다. getDouble은6을 반환하여 result에 저장하고, 다음 식이1을 더해7을 출력한다. 함수 정의 두 개와 호출 위치를 모두 보여 주므로 다른 파일의 숨은 함수 없이 따라갈 수 있다.

**예상 출력 또는 관찰:**

```text
6
undefined
7
```

<a id="my-code"></a>

## 4. 내가 작성한 코드를 따라 읽기

아래는 원본의 일부다. 원본에 의존하는 앞 선언·HTML·함수는 다음 절의 연결까지 읽는다. 주석의 잘못된 표현도 원문대로 보존하고 설명에서 교정한다.

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_html/javascript/08_function.html` 18–35행

```javascript
            function getArea(width, height) {
                console.log(`width: ${width}, height: ${height}`)
                let area = width * height;
                console.log('면적 : ', area);
            }
            
            getArea(10, 20);
            
            // 함수는 이름이 같을 경우 아래것을 덮어쓰게 됨
            function getArea2(width, height) {
                console.log(`width: ${width}, height: ${height}`)
                let area = width * height;
                return area;
            }

            // 200을 리턴했으니 아래 getArea2가 200이라는 값을 가지게 됨
            let result = getArea2(10, 20);
            console.log(result)
```

**발췌 바로 풀이:** 같은 비교다. getArea는 면적 200을 **출력**하지만 값을 반환하지 않아 호출 결과는 undefined다. getArea2는 200을 반환하므로 result에 저장해 다음 계산에 쓸 수 있다. 내 주석의 ‘getArea2가 200이라는 값을 가짐’은 **getArea2(10,20) 호출 결과가 200**이라는 뜻으로 읽는다. 함수 자체가 숫자 200으로 바뀌지는 않는다.

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_html/javascript/08_function.html` 107–129행

```javascript
            // 전달인자의 값이 undefined 일 때 기본 값 지정
            // 전달 받은 값이 있으면 사용하고, 없으면 기본 값 사용
            function plus3(x, y=0) {
                console.log('x : ', x)
                console.log('y : ', y)
                // if(y == undefined) y = 0
                if(y == undefined) {
                    y = 0
                }

                const z = x + y
                return z;
            }

            // 전달인자를 적게 줘도 에러는 나지 않음
            // 기본값을 지정해주지 않으면 undefined로 나옴
            a = plus3(2)
            console.log(a)

            // 인수가 2개가 들어가야 하는데, 3개를 주면 3번째 인수는 무시함
            // 받을 만큼만 가져감 (아래에서 4는 없어지는 값)
            a = plus3(2, 3, 4)
            console.log(a)
```

**발췌 바로 풀이:** 같은 동작이며 내 코드는 인수 셋을 준 결과도 출력한다. y=0은 y가 undefined일 때 적용되는 기본값이다. plus3(2)는 2, plus3(2,3,4)는 이 함수 본문이 x·y만 사용하므로 5다. 추가 인수가 언어 차원에서 반드시 ‘사라진다’는 뜻은 아니다. 이 본문에서 사용하지 않는다고 설명한다. [MDN 기본 매개변수](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Default_parameters)

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_html/javascript/08_function.html` 39–45행

```javascript
            function plus(x, y) {
                console.log('x : ', x)
                console.log('y : ', y)

                const z = x + y
                return z;
            }
```

내 getArea는 폭·높이와면적200을 출력만 하고 getArea2는 area를 반환해 result에 저장한다. ‘getArea2가200값을 가짐’이라는 주석은 함수 자체가 숫자로 바뀌는 것이 아니라 그 호출의 결과가200이라는 뜻으로 고쳐 읽는다. 아래에 plus의 실제 정의도 함께 실어 뒤 중첩 호출에서 무엇을 계산하는지 연결했다. plus3는 y=0과 본문의 느슨한 undefined비교를 둘 다 가지고 있다.

<a id="connections"></a>

## 5. 선언·호출·파일이 연결되는 흐름

plus(x,y)의 정의 → const z=x+y → return z → 호출한 식으로 결과 전달 흐름이다. 강사님의 plus(2,plus(5,6))은 안쪽11을 바깥에 전달해13이다. 내 plus(2,plus(result,6))은 앞에서 result=plus(2,3)으로5를 만든 조건에서13이다. result가 바뀌면 항상 같은 식은 아니다.

함수 내부 const z와 바깥 const z는 다른 범위다. 원본 블록은 안쪽이 바깥a를 읽고 바깥은 안쪽b를 읽지 못한다. 같은 이름의 안쪽a를 만드는 주석 실험은 바깥값을 가릴 수 있지만 현재 주석이라 실행 중 오류로 표시하지 않는다. 같은 print 함수 선언 두 개의 일반 스크립트 실험도 let재선언 규칙과 혼동하지 않는다.

<a id="review"></a>

## 6. 잘한 점·아쉬운 점·개선 방향

**잘한 점:** 면적의 출력·반환을 별도 함수로 비교하고 인수 부족·추가의 결과도 확인했다. **교정:** 호출 결과와 함수 자체를 같은 값으로 설명하지 않는다. **중복:** y=0이 이미undefined를 처리해 본문의 같은 검사가 겹치지만, 느슨한 비교는null까지 포함하므로 완전히 같은 조건은 아니다. **개선 방향:** 반환값을 쓰려는 목적을 먼저 정하고, 함수 정의·호출·사용을 함께 보여 준다.

개선안은 원본을 수정한 결과가 아니다. 실제 오류, 수업용 단순화, 목적에 따른 선택을 구별해 판단한다.

<a id="teacher"></a>

## 7. 강사님 코드가 도움이 되는 비교



면적·기본 매개변수는 양쪽 핵심이 같아 중복 인용하지 않는다. 내 코드는 인수 셋을 준 결과도 출력해 확인하기 좋다. 다만 ‘세 번째 인수는 언어 차원에서 사라진다’보다 이 함수 본문이 x·y만 사용한다고 설명한다. 어떤 함수든 인수가 부족해도 오류 없다는 일반 보장은 아니다.

<a id="results"></a>

## 8. 결과를 추적하고 한 가지 바꾸기

| 원본 호출 | 매개변수 처리 | 반환 |
| --- | --- | --- |
| getArea(10,20) |출력만 함 |undefined |
| getArea2(10,20) |면적 계산 후return |200 |
| plus3(2) |y가undefined라 기본0 |2 |
| plus3(2,3,4) |본문에서x·y만 사용 |5 |
| plus3(2,null) |기본값은null유지,본문==검사가0으로변경 |2 |

마지막 결과를 기본 매개변수가null까지 처리했다고 설명하면 원인을 잘못 짚은 것이다. 실행 순서와 별도 if가 핵심이다.

| 한 가지 변경 | 예상 | 이유 |
| --- | --- | --- |
| getDouble의return만제거 |마지막NaN |undefined+1 |
| 원래인수3만4로 |해당호출결과8 |전달값변경 |
| 원래result+1만result로 |마지막6 |반환뒤사용변경 |

함수를 만들었는데 출력이 없으면 호출했는지 확인한다. 출력은 있는데 계산에undefined가 들어가면return을 확인한다. 함수 안 이름을 바깥에서 읽으려다 오류가 나면 반환으로 전달할 값인지 검토한다.

<a id="tips"></a>

## 9. 추가로 알면 좋은 것과 출처

> 💡 **TIP · 수업 범위 밖:** 인수 전체를 처리하는 고급 패턴·호이스팅 내부 모델·유틸리티 체계 설계는 추가 학습이다. 먼저 원본의 범위와 반환을 정확히 설명한다.



이 절의 확장은 기본 문제의 필수 조건이 아니다. 📚 출처가 있다는 것과 수업 밖 기능이라는 것은 다른 구분이다.

<a id="practice"></a>

## 10. 복습과 빠른 정리

1. 출력만 하는 함수의 반환은?
2. plus(2,plus(5,6))의 바깥 인수는?
3. y=0 자체가null도 처리하는가?

<details>
<summary>짧은 풀이 — 먼저 답한 뒤 확인</summary>

명시적 반환이 없으면undefined다. 바깥에는2와11이 전달된다. 기본 매개변수 자체는null을0으로 바꾸지 않는다.

</details>

| 구분 | 뜻 |
| --- | --- |
| 정의 |작업묶음준비 |
| 호출 |실행요청 |
| 인수/매개변수 |보낸값/받는이름 |
| log/return |출력/결과전달 |

[장별 연습문제](실습/연습문제/08_JavaScript_함수와_콜백_타이머_연습문제.md)에서 예상·설명·수정을 이어 간다. 다음은 [함수 참조와 콜백](08-02_JavaScript_함수참조와_콜백.md)이다.

<!-- 이전 색인 이동 주소 보존 -->
<a id="section-1"></a>
<a id="section-2"></a>
<a id="section-3"></a>
<a id="section-4"></a>
<a id="section-5"></a>
<a id="section-6"></a>

[이 장의 목차](#chapter-toc)에서 현재 설명을 찾는다.
