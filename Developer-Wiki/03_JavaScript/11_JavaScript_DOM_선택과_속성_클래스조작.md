# 11. DOM 선택 — 요소 하나와 목록부터 구분하기

[JavaScript 목차](README.md) · [읽기 안내](00_JavaScript_V3_동작_백과_읽기법.md)

DOM은 브라우저가 HTML을 읽어 만든 문서 객체 구조다. JavaScript로 화면을 바꾸려면 먼저 그 구조에서 대상을 찾는다. 반환값이 요소 하나인지 목록인지 알아야 이후 속성 읽기와 반복을 올바르게 연결할 수 있다.

<a id="chapter-toc"></a>

**이 장의 목차:** [목표](#learn) · [개념](#concepts) · [예제](#example) · [내 코드](#my-code) · [연결](#connections) · [평가](#review) · [비교](#teacher) · [결과·실험](#results) · [TIP·출처](#tips) · [복습](#practice)

<a id="learn"></a>

## 1. 이 장에서 배울 것

DOM 선택 함수의 기준·반환·없을 때 결과를 비교한다. 찾는 범위와 실행 시점, 빈 목록의 참거짓을 설명한다.

입력·현재 상태·실행 순서·결과를 분리해 설명한다. 실제 수업 원본은 아래에 표시하고, 원본에 없는 선택 학습은 9절 TIP에 둔다.

<a id="concepts"></a>

## 2. 무엇이며, 왜 필요한가

HTML의 부모·자식 관계가 DOM에서도 요소 객체 관계로 표현된다. document는 현재 문서를 다루는 출발점이며 선택 메서드는 조건에 맞는 요소를 반환한다. 요소를 담은 변수는 그 태그의 문자열만을 저장한 것이 아니다. 그 객체의 textContent 등을 읽어 글자를 얻는다.

| 메서드 | 입력 | 반환 | 없을 때 |
| --- | --- | --- | --- |
| getElementById |ID값, #없음 |요소하나 |null |
| querySelector |CSS선택자 |첫요소하나 |null |
| getElementsByTagName |태그이름 |HTMLCollection |길이0목록 |
| getElementsByClassName |클래스이름,점없음 |HTMLCollection |길이0목록 |
| querySelectorAll |CSS선택자 |NodeList |길이0목록 |

목록은 배열 자체가 아니다. 이 수업에서는 length·[0]·for로 접근하지만 모든 배열 메서드가 있다고 가정하지 않는다. 빈 목록 객체도 if에서 참이므로 요소 존재 여부는 length를 확인한다. 단일 선택은null 여부를 본다.

document 전체와 특정 요소 안은 검색 범위가 다르다. 부모를 먼저 찾고 parent.querySelectorAll처럼 그 안에서 고르면 문서 다른 부분의 같은 클래스는 제외된다. 선택자는 CSS 조건을 빌려 대상을 찾는 것이지 style태그의 글자를 읽는 것이 아니다.

> 📚 **출처 · 본문 설명 확인:** [MDN DOM 소개](https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model/Introduction), [querySelectorAll](https://developer.mozilla.org/en-US/docs/Web/API/Document/querySelectorAll), [getElementById](https://developer.mozilla.org/en-US/docs/Web/API/Document/getElementById). 배운 기능의 뜻을 확인한 근거다. 예제·표·풀이 흐름은 수업 코드를 바탕으로 새로 작성했으며 외부 문장을 직접 인용하지 않았다. 확인일: 2026-10-28.

<a id="example"></a>

## 3. 작은 예제로 먼저 이해하기

**새 설명 예제 · 전체 스크립트.** [HTML 실행 파일](실습/책형_복습/11_JavaScript_DOM_선택과_속성_클래스조작.html)과 같은 폴더의 [JS 파일](실습/책형_복습/11_JavaScript_DOM_선택과_속성_클래스조작.js)을 함께 내려받는다. HTML을 브라우저로 열고 Console에서 결과를 확인한다. script는 필요한 HTML 뒤에 연결한다. 콘솔 출력은 페이지 본문에 자동으로 쓰이지 않는다.

**먼저 준비할 HTML · body 안:**

```html
    <div id="panel">
        <h2 id="book-title">안녕</h2>
        <p class="note">첫째</p>
        <p class="note">둘째</p>
    </div>
```

```javascript
const title = document.getElementById('book-title');
console.log(title.textContent);
const notes = document.querySelectorAll('#panel .note');
console.log(notes.length);
console.log(notes[0].textContent);
console.log(document.querySelector('.missing'));
const missing = document.querySelectorAll('.missing');
console.log(missing.length);
if (missing) {
    console.log('목록 객체 있음');
}
```

title은 h2 하나이고 notes는 두 p의 목록이다. notes[0]은 첫 요소이며 그 textContent는 첫째다. 단일 선택의 missing은 null, 전체 선택은 길이0인 목록이다. 마지막 if는 원소가 있어서가 아니라 목록 객체가 존재해 실행된다. 스크립트는 이 HTML이 만들어진 뒤 연결한다.

**예상 출력 또는 관찰:**

```text
안녕
2
첫째
null
0
목록 객체 있음
```

<a id="my-code"></a>

## 4. 내가 작성한 코드를 따라 읽기

아래는 원본의 일부다. 원본에 의존하는 앞 선언·HTML·함수는 다음 절의 연결까지 읽는다. 주석의 잘못된 표현도 원문대로 보존하고 설명에서 교정한다.

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_html/javascript/11_dom.html` 55–71행

```javascript
            // id속성으로 DOM을 가져오기
            // html body에 있는 h1이 가져와진 것
            const title = document.getElementById('title')
            console.log(title)
            // [object HTMLHeadingElement] 가 나오는데, heap영역의 주소값이 나옴
            // javascript는 주소값을 가려서 보여주기 때문에 위 멘트로 나옴
            console.log(''+title)

            // 아래처럼 없는 id 등 선언되지 않은 것을 불러오면 'null = 주소값이 없다'
            // undefined처럼 일반적인 값이 없을 때와는 다름
            // 에드블럭같은 경우 광고값의 id를 불러오고 null이면 광고가 없다? 지워졌다?
            const title2 = document.getElementById('title2')
            console.log(title2)

            // javascript는 같은 ID가 있어도 첫번째 나온 DOM만 읽고 나머지는 읽지 않음
            const view = document.getElementById('view')
            console.log(view)
```

**발췌 바로 풀이:** 동작은 같다. title은 `<h1 id="title">` 요소이고 title2는 null이다. null은 여기서 **조건에 맞는 요소를 찾지 못했다는 결과**다. `'' + title`의 `[object HTMLHeadingElement]`는 객체를 문자열로 바꾼 표현이며 메모리 주소를 출력한 것이 아니다. 내 주석의 주소 설명은 이 의미로 고쳐 읽는다.

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_html/javascript/11_dom.html` 73–85행

```javascript
            // tag속성으로 DOM을 가져오기
            // Element's'로 가져오면 유사 배열로 가져오게 됨 (HTMLCollection배열)
            let divs = document.getElementsByTagName('div')
            console.log('divs',divs)

            // 선언 된 것이 없을 경우 null이 아닌, length가 0인 빈 배열을 가져옴
            let divs2 = document.getElementsByTagName('div2')
            console.log(divs2)

            // 배열이 비어있다고 해도 true(참)으로 판단함
            if(divs2) {
                console.log('참')
            }
```

**발췌 바로 풀이:** 양쪽 문서에 `<div2>`는 없다. divs2.length는 0이지만 divs2 자체는 객체여서 if(divs2)는 참이다. 양쪽의 ‘배열’ 주석을 정확히는 **HTMLCollection**으로 읽는다. 실제 요소가 있는지 검사하려면 길이를 확인한다.

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_html/javascript/11_dom.html` 87–97행

```javascript
            // class로 DOM을 가져오기 (class는 포함 한 정보 모두를 가져옴)
            // console창에서 div#view, li.menu.li1 등 가장 빠른 경로를 알려줌
            let menus = document.getElementsByClassName('menu')
            console.log(menus)

            // ul에 있는 #메뉴 id를 가져오며 다른 dom으로 대체가능
            // 특정 DOM안에서도 class나 tag를 찾을 수 있다
            let 메뉴 = document.getElementById('메뉴')
            // let pizza = 메뉴.getElementsByTagName('li')
            let pizza = 메뉴.getElementsByClassName('pizza')
            console.log(pizza)
```

**발췌 바로 풀이:** document에서 찾은 menu 클래스는 강사님 문서에 6개, 내 문서에 3개다. 강사님에게는 두 번째 목록 `#메뉴2`도 있기 때문이다. 코드의 우열이나 선택 함수의 차이가 아니라 **HTML 구성의 차이**다.

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_html/javascript/11_dom.html` 102–116행

```javascript
            let view2 = document.querySelector('#view.pizza')
            console.log(view2)

            // querySelector를 사용해도 같은 #view가 있을 때 첫번째 값만 가져옴
            // let view3 = document.querySelector('#view')
            let view3 = document.querySelector('div#view')
            console.log(view3)
    
            // div#view4라는게 없기 때문에 연결이 안 되어 'null'값이 나옴
            let view4 = document.querySelector('div#view4')
            console.log(view4)

            // All을 사용하면, 해당 ID또는 Class등 지정 된 것 모두를 가져옴
            let qsa = document.querySelectorAll('#view')
            console.log(qsa)
```

**발췌 바로 풀이:** #view.pizza는 같은 요소가 ID와class 두 조건을 모두 만족해야 한다. div#view는 첫 일치, div#view4는null, querySelectorAll(#view)은 두 요소의 목록이다. 원본의 ID중복은 관찰용이며 실제문서에서는 고유하게 쓴다.

내 title 선택은 h1을 얻고 title2는 null이다. 빈 문자열+title의 [object HTMLHeadingElement]는 객체의 문자열 표현이지 메모리 주소 출력이 아니다. div2 태그가 없는 목록도 객체여서 if(divs2)는 참이다. 원본 view는 ID 중복을 실험하지만 실제 문서는 ID를 고유하게 둔다. 같은 ID의 나머지 요소를 JavaScript가 전혀 읽지 못한다는 뜻은 아니다.

<a id="connections"></a>

## 5. 선언·호출·파일이 연결되는 흐름

HTML 요소 생성 → script 실행 → 선택 메서드 → 요소 또는 목록 변수 → 속성 읽기 순서다. 원본의 메뉴 변수는 ID가 메뉴인 ul이고 그 안의 pizza를 검색한다. 강사님 문서의 menu는6개·내 문서는3개지만 강사님의 두 번째 목록 때문이며 함수 차이가 아니다. 해당 메뉴 안의 pizza는 양쪽1개다.

<a id="review"></a>

## 6. 잘한 점·아쉬운 점·개선 방향

**잘한 점:** 단일 결과와 없는 결과, 검색 범위를 주석으로 관찰했다. **교정:** 객체 문자열은 주소가 아니고 HTMLCollection도 배열 그 자체가 아니다. **수업용 실험:** 중복 ID에서 첫 선택을 관찰한 것을 실제 문서의 권장 구조로 옮기지 않는다. **개선 방향:** 선택 실패를 속성 읽기 전에 검사하고 목록은 length로 확인한다.

개선안은 원본을 수정한 결과가 아니다. 실제 오류, 수업용 단순화, 목적에 따른 선택을 구별해 판단한다.

<a id="teacher"></a>

## 7. 강사님 코드가 도움이 되는 비교



선택 호출이 같아 중복 인용하지 않는다. 개수 차이는 실제 HTML 구성을 먼저 맞춰야 평가할 수 있다. 내 주석의 Console 요소 표시도 항상 가장 빠른 경로를 보장하는 분석 결과가 아니라 선택한 요소를 알아보기 위한 표현이다.

<a id="results"></a>

## 8. 결과를 추적하고 한 가지 바꾸기

| 원본 변수 | 결과 | 조건 |
| --- | --- | --- |
| view2 |두 번째 view |#view.pizza 두 조건 |
| view3 |첫 번째 view |div#view 첫 일치 |
| view4 |null |해당 요소 없음 |
| qsa |NodeList 2개 |#view 전체 일치 |

getElementsByTagName/ClassName의 HTMLCollection은 문서 변경을 반영한다. 원본 divs는 처음4개지만 뒤 div2.remove() 후3개다. querySelectorAll 목록은 선택 당시의 목록이며 그 안 요소의 속성 변경까지 멈추는 것은 아니다. 뒤 장의 remove를 배운 후 연결해 다시 확인한다.

| 한 가지 변경 | 예상 | 이유 |
| --- | --- | --- |
| 첫선택ID만없는값으로 |null속성읽기오류 |존재확인필요 |
| notes선택자만#panel로 |목록길이1 |부모하나선택 |
| 마지막if를missing.length>0으로 |마지막문구없음 |원소수검사 |

null이면 ID·선택자 철자·검색 범위·script 실행 시점을 본다. 목록에 바로 textContent를 읽는 대신 필요한 원소를 선택하거나 반복한다. 스크립트를 요소 앞으로 옮기면 아직 요소가 없어 결과가 달라질 수 있다.

<a id="tips"></a>

## 9. 추가로 알면 좋은 것과 출처

> 💡 **TIP · 수업 범위 밖:** Array.from 변환·defer 등 로딩 전략 상세는 추가 학습이다. 기본은 원본 선택 함수와 for만으로 풀 수 있다.



이 절의 확장은 기본 문제의 필수 조건이 아니다. 📚 출처가 있다는 것과 수업 밖 기능이라는 것은 다른 구분이다.

<a id="practice"></a>

## 10. 복습과 빠른 정리

1. querySelector와 All이 못 찾았을 때 각각 무엇인가?
2. 빈 목록이 참이면 원소도 있는가?
3. 부모 안 검색과 document 검색은 같은가?

<details>
<summary>짧은 풀이 — 먼저 답한 뒤 확인</summary>

null과 길이0 목록이다. 목록 객체가 참이라는 것과 원소 수는 별개다. 검색 범위가 달라 개수도 다를 수 있다.

</details>

| 반환 | 다음확인 |
| --- | --- |
| 요소하나 |null검사 |
| 목록 |length·인덱스 |
| 선택오류 |조건·범위·시점 |
| 객체문자열 |주소출력아님 |

[장별 연습문제](실습/연습문제/11_JavaScript_DOM_선택과_속성_클래스조작_연습문제.md)에서 예상·설명·수정을 이어 간다. 다음은 [속성과 클래스](11-02_JavaScript_DOM_속성과_클래스.md)다.

<!-- 이전 색인 이동 주소 보존 -->
<a id="section-1"></a>
<a id="section-2"></a>
<a id="section-3"></a>
<a id="section-4"></a>
<a id="section-5"></a>
<a id="section-6"></a>
<a id="section-7"></a>

[이 장의 목차](#chapter-toc)에서 현재 설명을 찾는다.
