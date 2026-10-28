# 11-02. 속성·클래스 — 선택한 요소의 상태 바꾸기

[JavaScript 목차](README.md) · [이전: DOM 선택](11_JavaScript_DOM_선택과_속성_클래스조작.md)

기준은 양쪽 `11_dom.html`과 강사님 `퀴즈/이벤트.html`이다. **dataset은 실제로 배웠다고 확인한 내용이므로 본문**에 둔다. 선택 함수의 반환값은 앞 장에서 복습하고, 여기서는 선택한 요소를 어떻게 바꾸는지 본다.

**속성과 클래스는 무엇인가?** 속성은 HTML 요소에 적힌 `src`, `data-name` 같은 정보이고, `class`는 그중 여러 이름을 가질 수 있는 속성이다. 아래는 원본 발췌가 아닌 **설명용 작은 예제**다.

```html
<p id="notice" class="message" data-name="공지">안내</p>
<script>
  const notice = document.getElementById('notice');
  console.log(notice.dataset.name); // 공지
  notice.classList.add('active');
  console.log(notice.classList.contains('active')); // true
</script>
```

이제 원본에서 속성의 존재·값을 읽는 방법과 클래스를 순서대로 바꾼 결과를 살핀다.

<!-- chapter-toc -->

- [1. 속성의 존재와 값을 구분하기](11-02_JavaScript_DOM_속성과_클래스.md#section-1)
- [2. data-name과 dataset.name](11-02_JavaScript_DOM_속성과_클래스.md#section-2)
- [3. classList의 상태를 한 줄씩 추적하기](11-02_JavaScript_DOM_속성과_클래스.md#section-3)
- [4. 클래스 제거와 요소 제거는 다르다](11-02_JavaScript_DOM_속성과_클래스.md#section-4)
- [5. 복습](11-02_JavaScript_DOM_속성과_클래스.md#section-5)
- [추가로 알면 좋은 것](11-02_JavaScript_DOM_속성과_클래스.md#section-6)

<a id="section-1"></a>

## 1. 속성의 존재와 값을 구분하기

### 강사님 코드

출처: `teacher/workspace_html/javascript/11_dom.html` 116–131행 · **원본 발췌**

```javascript
        let aha = document.querySelector('#aha')
        console.log(aha)

        // 속성명이 있는가?
        // readonly, disabled, required 등 검사할 때 좋다
        let isSrc = aha.hasAttribute('src')
        console.log('isSrc', isSrc)


        // 속성값 가져오기
        let src = aha.getAttribute('src')
        console.log('src', src)

        // 없으면 null
        let src2 = aha.getAttribute('src2')
        console.log('src2', src2)
```

### 내 코드

출처: `me/workspace_html/javascript/11_dom.html` 121–136행 · **원본 발췌**

```javascript
            let aha = document.querySelector('#aha')
            console.log(aha)

            // 있느냐 없느냐 할 때 isOOO를 많이 씀
            // hasAttribute로 속성명이 있는가를 찾을 수 있음
            // readonly, disabled, required 등 검사할 때 좋음
            let isSrc = aha.hasAttribute('src')
            console.log('isSrc : ', isSrc)

            // 속성명 가져오기
            let src = aha.getAttribute('src')
            console.log('src : ',src)

            // 없으면 null 반환
            let src2 = aha.getAttribute('src2')
            console.log('src : ',src2)
```

두 코드의 결과는 같다. aha는 이미지 요소다. hasAttribute('src')는 속성이 있는지 검사하여 true를 반환한다. getAttribute('src')는 이미지 주소 **문자열**을 반환한다. 없는 src2 속성을 읽으면 null이다. 내 주석의 ‘속성명 가져오기’는 ‘속성값 가져오기’로 교정한다.

| 목적 | 원본 호출 | 결과 |
| --- | --- | --- |
| 있는지 확인 | aha.hasAttribute('src') | true/false |
| 값 읽기 | aha.getAttribute('src') | 문자열 또는 null |
| 값 쓰기 | aha.setAttribute('human', '교육센터') | 속성이 없으면 추가, 있으면 변경 |
| 속성 제거 | aha.removeAttribute('human') | human 속성 자체 제거 |

양쪽은 setTimeout 안에서 2초 지연으로 src를 바꾼다. human 속성 추가와 삭제는 타이머 바깥이므로 먼저 끝난다. 이미지가 실제로 보이는지는 외부 주소의 응답에도 달려 있다. src 변경과 이미지 다운로드 성공은 같은 판단이 아니다.

<a id="section-2"></a>

## 2. data-name과 dataset.name

강사님 피자 퀴즈의 option은 `value="10" data-name="불고기"`처럼 값과 이름을 별도로 보관한다. 아래 코드는 pizza 변수가 해당 select를 가리키는 상황의 원본이다.

### 강사님 코드

출처: `teacher/workspace_html/javascript/퀴즈/이벤트.html` 122–128행 · **원본 발췌**

```javascript
        console.log(pizza.options)
        console.log(pizza.selectedIndex)
        const option = pizza.options[pizza.selectedIndex]
        console.log(option.innerText)
        console.log(option.getAttribute('data-name'))
        console.log(option.dataset.name)
        option.dataset.minsu = '강사'
```

options는 select의 option 목록이고 selectedIndex는 현재 선택 위치다. 그 위치의 option을 가져온 뒤 두 방식으로 같은 data-name 값을 읽는다. 불고기가 선택되어 있으면 두 출력은 모두 '불고기'다. `option.dataset.minsu = '강사'`는 그 option의 `data-minsu` 속성을 설정한다. [MDN dataset](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/dataset)

### 내 코드와의 대응

내 11번에는 위 dataset 예제가 없다. 대신 바로 앞 절의 getAttribute 사용과 연결하여 이해할 수 있다. 없는 학생 코드를 만들어 원본처럼 붙이지 않는다. 이 내용은 강사님 이벤트 퀴즈와 학습 여부 확인을 근거로 포함했다. 주문 계산 전체는 이후 17 이벤트 실습에서 다룬다.

**수업 문법으로 재구성한 짧은 예제 — 원본 발췌 아님**

```html
<div id="pizzaInfo" data-name="불고기">피자 정보</div>
<script>
    const pizzaInfo = document.querySelector('#pizzaInfo')
    console.log(pizzaInfo.getAttribute('data-name')) // '불고기'
    console.log(pizzaInfo.dataset.name)             // '불고기'
</script>
```

<a id="section-3"></a>

## 3. classList의 상태를 한 줄씩 추적하기

classList는 클래스 이름을 다루는 DOMTokenList다. 양쪽 원본 주석의 ‘배열’은 정확한 자료형 이름이 아니다. 요소가 가진 모든 클래스를 문자열로 다시 작성하지 않고 개별 클래스를 추가·제거할 수 있다.

### 강사님 코드

출처: `teacher/workspace_html/javascript/11_dom.html` 157–172행 · **원본 발췌**

```javascript
        // add : class 추가
        div1.classList.add('blue')
        // 이미 있는것은 추가하지 않는다
        div1.classList.add('blue')

        // remove : class 빼기
        div1.classList.remove('blue')
        // 없어도 에러 없음
        div1.classList.remove('blue')
        
        div1.classList.toggle('blue')
        div1.classList.toggle('blue')
        
        
        let isBlue = div1.classList.contains('blue')
        console.log('isBlue', isBlue)
```

### 내 코드

출처: `me/workspace_html/javascript/11_dom.html` 158–174행 · **원본 발췌**

```javascript
            // add는 class 추가이지만, 중복으로 추가하지는 않음
            div1.classList.add('blue')
            div1.classList.add('blue')
            
            // remove는 class 제거이지만, 없어도 에러나지 않음
            div1.classList.remove('blue')
            div1.classList.remove('blue')
            
            // toggle은 상태를 반전시킬 수 있음
            // blue가 없으면 켜주고, blue가 있으면 꺼줌
            div1.classList.toggle('blue')
            div1.classList.toggle('blue')

            // 해당 class가 있는지 없는지 true/false 값으로 알려줌
            // blue가 있고 없고에 따라 add/remove도 해볼 수 있음
            let isBlue = div1.classList.contains('blue')
            console.log(isBlue)
```

| 실행 직후 | div1에 blue가 있는가 | 이유 |
| --- | --- | --- |
| 첫 add | 있음 | 추가 |
| 두 번째 add | 있음 | 중복하여 넣지 않음 |
| 첫 remove | 없음 | 제거 |
| 두 번째 remove | 없음 | 없어도 그대로 |
| 첫 toggle | 있음 | 없으므로 추가 |
| 두 번째 toggle | 없음 | 있으므로 제거 |
| contains | false 반환 | 검사만 하며 상태는 바꾸지 않음 |

내 코드와 강사님 코드는 같은 흐름이다. 내 toggle 주석은 상태 반전을 읽기 좋게 설명한다. 한 스크립트에서 곧바로 추가·제거하므로 화면에서 매 단계의 색 변화가 보이지 않을 수 있다. 최종 상태와 중간 코드를 구분한다.

<a id="section-4"></a>

## 4. 클래스 제거와 요소 제거는 다르다

### 강사님 코드

출처: `teacher/workspace_html/javascript/11_dom.html` 174–178행 · **원본 발췌**

```javascript
        // div2를 가져와서
        // .blue 적용
        div2.classList.add('blue')

        div2.remove()
```

### 내 코드

출처: `me/workspace_html/javascript/11_dom.html` 176–180행 · **원본 발췌**

```javascript
            div2.classList.add('blue')

            // remove()로 DOM을 지우면 되돌릴 수 없음
            // 보통은 display:none으로 잠깐 안 보이게 했다가 나오게 함
            div2.remove()
```

classList.remove('blue')는 클래스 하나를 제거한다. div2.remove()는 div2 요소를 문서에서 떼어 낸다. 내 주석의 ‘되돌릴 수 없음’은 정확하지 않다. div2 변수가 여전히 요소를 참조하고 있으므로, 다음 장에서 배울 append로 다시 연결할 수 있다. display:none은 문서에 요소를 둔 채 표시를 숨기는 방법이라 remove와 동작이 다르다.

<a id="section-5"></a>

## 5. 복습

1. hasAttribute와 getAttribute 중 문자열 값을 얻는 것은?
2. blue가 없는 상태에서 toggle을 두 번 호출한 뒤 contains 결과는?
3. data-name 속성을 dataset으로 어떻게 읽는가?
4. remove 후 변수가 자동으로 null로 바뀌는가?

<details>
<summary>정답</summary>

1. getAttribute다. 없는 속성이면 null이다.
2. false다.
3. element.dataset.name으로 읽는다.
4. 아니다. 문서에서 분리되어도 변수의 참조가 자동으로 null이 되지는 않는다.

</details>

<a id="section-6"></a>

## 추가로 알면 좋은 것

dataset의 복잡한 이름 변환 규칙이나 속성 전체를 순회하는 도구는 확장 학습으로 둔다. 본문에서는 수업의 data-name 읽기와 data-minsu 쓰기까지 익힌다.

**이 장을 읽은 뒤:** [장별 연습문제 풀기](실습/연습문제/11-02_JavaScript_DOM_속성과_클래스_연습문제.md) → [다음: 내용과 요소 만들기](12_JavaScript_DOM_콘텐츠생성과_스타일조작.md)

