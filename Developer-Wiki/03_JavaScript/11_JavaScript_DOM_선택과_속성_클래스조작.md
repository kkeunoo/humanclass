# 11. DOM 선택 — 요소 하나와 요소 목록 구분하기

[JavaScript 목차](README.md) · [이전: 문자열](10_JavaScript_문자열과_문자열메서드.md) · [다음: 속성·클래스](11-02_JavaScript_DOM_속성과_클래스.md)

기준은 양쪽 `11_dom.html`이다. DOM은 브라우저가 HTML을 읽어 만든 문서 객체 구조다. 화면을 바꾸려면 먼저 원하는 요소를 찾아 변수에 담는다. 이 장에서는 **찾은 결과가 요소 하나인지, 여러 요소의 목록인지**부터 구분한다.

**요소 선택이란?** HTML에 있는 태그를 JavaScript가 다룰 수 있는 값으로 가져오는 일이다. 아래는 원본 발췌가 아닌 **설명용 작은 예제**이며, HTML을 만든 뒤 스크립트를 실행한다.

```html
<h1 id="title">안녕</h1>
<p class="note">첫째</p>
<p class="note">둘째</p>
<script>
  console.log(document.getElementById('title').textContent); // 안녕
  console.log(document.querySelectorAll('.note').length);  // 2
</script>
```

첫 줄은 요소 **하나**의 글자를 읽고, 둘째는 일치하는 요소 **목록**의 개수를 읽는다. 이제 원본에서 각 선택 함수가 무엇을 반환하는지 비교한다.

<!-- chapter-toc -->

- [1. 무엇을 돌려받는가](11_JavaScript_DOM_선택과_속성_클래스조작.md#section-1)
- [2. 하나 선택하기와 null](11_JavaScript_DOM_선택과_속성_클래스조작.md#section-2)
- [3. 빈 목록도 조건식에서는 참이다](11_JavaScript_DOM_선택과_속성_클래스조작.md#section-3)
- [4. 어디에서 찾는지에 따라 개수가 달라진다](11_JavaScript_DOM_선택과_속성_클래스조작.md#section-4)
- [5. querySelector와 querySelectorAll 비교](11_JavaScript_DOM_선택과_속성_클래스조작.md#section-5)
- [6. 복습](11_JavaScript_DOM_선택과_속성_클래스조작.md#section-6)
- [추가로 알면 좋은 것](11_JavaScript_DOM_선택과_속성_클래스조작.md#section-7)

<a id="section-1"></a>

## 1. 무엇을 돌려받는가

| 호출 | 찾는 기준 | 찾았을 때 | 없을 때 |
| --- | --- | --- | --- |
| document.getElementById('title') | id 값 | 요소 하나 | null |
| document.querySelector('#title') | CSS 선택자 | 첫 번째 요소 하나 | null |
| document.getElementsByTagName('div') | 태그 이름 | HTMLCollection | 길이 0인 HTMLCollection |
| document.getElementsByClassName('menu') | 클래스 이름 | HTMLCollection | 길이 0인 HTMLCollection |
| document.querySelectorAll('.menu') | CSS 선택자 | NodeList | 길이 0인 NodeList |

`getElementById`에는 #을 붙이지 않는다. `querySelector`에는 `#title`, `.menu`, `div` 같은 CSS 선택자를 쓴다. CSS 선택자는 **요소를 찾는 문법**이지 style 태그의 내용을 읽는다는 뜻이 아니다.

HTMLCollection과 NodeList는 배열이 아니다. 다만 이 실습에서는 `.length`, `[0]`, for문으로 여러 요소에 접근할 수 있다. 배열의 모든 메서드가 그대로 있다고 가정하지 않는다.

<a id="section-2"></a>

## 2. 하나 선택하기와 null

### 강사님 코드

출처: `teacher/workspace_html/javascript/11_dom.html` 55–67행 · **원본 발췌**

```javascript
        // id 속성으로 DOM을 가져오기
        const title = document.getElementById('title')
        console.log(title)
        console.log(''+title)

        // 없으면 null
        const title2 = document.getElementById('title2')
        console.log(title2)
        
        // 동일한 id가 여러개 있어도
        // 첫번째 DOM만 가져온다
        const view = document.getElementById('view')
        console.log(view)
```

### 내 코드

출처: `me/workspace_html/javascript/11_dom.html` 55–71행 · **원본 발췌**

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

동작은 같다. title은 `<h1 id="title">` 요소이고 title2는 null이다. null은 여기서 **조건에 맞는 요소를 찾지 못했다는 결과**다. `'' + title`의 `[object HTMLHeadingElement]`는 객체를 문자열로 바꾼 표현이며 메모리 주소를 출력한 것이 아니다. 내 주석의 주소 설명은 이 의미로 고쳐 읽는다.

원본은 선택 결과를 비교하려고 `id="view"`를 두 번 쓴다. getElementById는 첫 번째를 선택한다. 실제 문서 작성에서는 id를 고유하게 지정한다. ‘JavaScript는 같은 id를 가진 나머지 요소를 전혀 읽지 못한다’는 뜻은 아니다.

<a id="section-3"></a>

## 3. 빈 목록도 조건식에서는 참이다

### 강사님 코드

출처: `teacher/workspace_html/javascript/11_dom.html` 70–80행 · **원본 발췌**

```javascript
        // tag로 찾기
        let divs = document.getElementsByTagName('div')
        console.log(divs)
        
        // 없으면 length가 0인 배열
        let divs2 = document.getElementsByTagName('div2')
        console.log(divs2)

        if(divs2){
            console.log('참')
        }
```

### 내 코드

출처: `me/workspace_html/javascript/11_dom.html` 73–85행 · **원본 발췌**

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

양쪽 문서에 `<div2>`는 없다. divs2.length는 0이지만 divs2 자체는 객체여서 if(divs2)는 참이다. 양쪽의 ‘배열’ 주석을 정확히는 **HTMLCollection**으로 읽는다. 실제 요소가 있는지 검사하려면 길이를 확인한다.

**설명용 교정 예제 — 원본 발췌 아님**

```javascript
if (divs2.length > 0) {
    console.log('요소가 있다')
}
if (title2 !== null) {
    console.log(title2.textContent)
}
```

단일 선택 결과에 null 검사를 하고, 여러 개 선택한 결과에는 length 검사를 한다. null에 속성을 읽으려 하면 오류가 난다.

<a id="section-4"></a>

## 4. 어디에서 찾는지에 따라 개수가 달라진다

### 강사님 코드

출처: `teacher/workspace_html/javascript/11_dom.html` 82–91행 · **원본 발췌**

```javascript
        // class로 찾기
        let menus = document.getElementsByClassName('menu')
        console.log(menus)

        // 직접 #메뉴를 가져오세요
        let 메뉴 = document.getElementById('메뉴')

        // 특정 DOM 안에서도 찾을 수 있다
        let pizza = 메뉴.getElementsByClassName('pizza')
        console.log(pizza)
```

### 내 코드

출처: `me/workspace_html/javascript/11_dom.html` 87–97행 · **원본 발췌**

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

document에서 찾은 menu 클래스는 강사님 문서에 6개, 내 문서에 3개다. 강사님에게는 두 번째 목록 `#메뉴2`도 있기 때문이다. 코드의 우열이나 선택 함수의 차이가 아니라 **HTML 구성의 차이**다.

반면 `메뉴.getElementsByClassName('pizza')`는 `#메뉴`의 자손 안에서 찾으므로 양쪽 모두 1개다. 문서 전체에서 찾을지 특정 요소 안에서 찾을지를 먼저 정한다.

<a id="section-5"></a>

## 5. querySelector와 querySelectorAll 비교

### 강사님 코드

출처: `teacher/workspace_html/javascript/11_dom.html` 98–108행 · **원본 발췌**

```javascript
        let view2 = document.querySelector('#view.pizza')
        console.log(view2)

        let view3 = document.querySelector('div#view')
        console.log(view3)

        let view4 = document.querySelector('div#view4')
        console.log(view4)

        let qsa = document.querySelectorAll('#view')
        console.log(qsa)
```

### 내 코드

출처: `me/workspace_html/javascript/11_dom.html` 102–116행 · **원본 발췌**

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

| 변수 | 양쪽 원본 결과 | 이유 |
| --- | --- | --- |
| view2 | 두 번째 view 요소 | id가 view이면서 pizza 클래스가 있음 |
| view3 | 첫 번째 view 요소 | div이며 id가 view인 첫 요소 |
| view4 | null | 해당 요소 없음 |
| qsa | 요소 2개가 든 NodeList | 조건에 맞는 모든 요소 선택 |

`#view.pizza`는 한 요소가 두 조건을 모두 만족한다는 뜻이다. 사이에 공백을 넣으면 자손을 찾는 다른 선택자가 된다.

이 실습에서 getElementsByTagName/ClassName의 HTMLCollection은 문서 변경에 따라 갱신된다. 처음 divs.length는 4지만 뒤의 div2.remove() 후에는 3이다. querySelectorAll은 **선택 당시의 목록**을 반환한다. 목록의 갱신 여부와 목록 안 요소의 속성이 바뀌는 것은 다른 이야기다. [MDN querySelectorAll](https://developer.mozilla.org/en-US/docs/Web/API/Document/querySelectorAll)

<a id="section-6"></a>

## 6. 복습

1. querySelector('.missing')과 querySelectorAll('.missing')은 각각 무엇인가?
2. 빈 HTMLCollection에 if문을 쓰면 왜 참인가?
3. 강사님 menus.length와 내 menus.length가 다른 이유는?
4. 원본 스크립트를 요소보다 앞에 옮기면 항상 같은 결과가 나올까?

<details>
<summary>정답과 확인 순서</summary>

1. null과 길이 0인 NodeList다.
2. 조건은 객체 자체를 평가한다. 요소 개수는 length로 따로 검사한다.
3. 강사님 HTML에 menu 클래스가 있는 두 번째 목록이 더 있다.
4. 아니다. 원본처럼 즉시 실행하는 일반 스크립트가 요소보다 먼저 실행되면 아직 만들어지지 않은 요소는 찾지 못한다. 원본은 대상 요소 뒤에서 실행한다.

</details>

<a id="section-7"></a>

## 추가로 알면 좋은 것

Array.from으로 목록을 배열로 바꾸는 방법, defer 등 스크립트 로딩 전략의 상세는 추가 학습이다. 이 장의 기본 문제는 원본의 선택 함수와 for문만으로 해결한다.

**이 장을 읽은 뒤:** [장별 연습문제 풀기](실습/연습문제/11_JavaScript_DOM_선택과_속성_클래스조작_연습문제.md) → [다음: 속성과 클래스](11-02_JavaScript_DOM_속성과_클래스.md)

