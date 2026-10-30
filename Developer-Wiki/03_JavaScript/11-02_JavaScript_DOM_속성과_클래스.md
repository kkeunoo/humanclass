# 11-02. 속성과 클래스 — 읽기·변경·제거의 대상

[JavaScript 목차](README.md) · [읽기 안내](00_JavaScript_V3_동작_백과_읽기법.md)

선택한 요소에서 src·data-name같은 정보를 읽거나 class를 바꾸어 이미 배운CSS를 연결할 수 있다. 속성이 있는지 묻는 것, 그 값을 읽는 것, 요소 자체를 떼는 것은 각각 다른 동작이다. dataset은 실제 배웠다고 확인되어 본문에 둔다.

<a id="chapter-toc"></a>

**이 장의 목차:** [목표](#learn) · [개념](#concepts) · [예제](#example) · [내 코드](#my-code) · [연결](#connections) · [평가](#review) · [비교](#teacher) · [결과·실험](#results) · [TIP·출처](#tips) · [복습](#practice)

<a id="learn"></a>

## 1. 이 장에서 배울 것

속성 존재·값·쓰기·제거를 구분한다. dataset과 classList의 연속 상태, 클래스 제거와 요소 제거를 설명한다.

입력·현재 상태·실행 순서·결과를 분리해 설명한다. 실제 수업 원본은 아래에 표시하고, 원본에 없는 선택 학습은 9절 TIP에 둔다.

<a id="concepts"></a>

## 2. 무엇이며, 왜 필요한가

HTML 속성은 요소에 붙인 정보이며 class도 그중 하나다. hasAttribute는 존재의 참거짓, getAttribute는 문자열 값 또는 null을 준다. setAttribute는 추가·변경, removeAttribute는 속성 자체를 제거한다. 값을 읽는 함수를 속성명 가져오기로 설명하지 않는다.

classList는 class 항목을 다루는 인터페이스다. add는 중복 없이 추가하고, remove는 없어도 그대로 둔다. toggle은 있으면 빼고 없으면 넣으며 contains는 검사만 한다. CSS의 .blue 규칙이 있으면 클래스 변경이 표시와 연결된다. 규칙이 없어도 class 항목 자체는 바뀐다.

| 구분 | 효과 |
| --- | --- |
| classList.remove('blue') |클래스 항목 제거 |
| element.remove() |문서에서 요소 분리 |
| display:none |문서에 둔 채 박스 숨김 |
| dataset.name |data-name 속성값 읽기 |

data-name을 dataset.name으로 읽고 dataset.minsu에 대입하면 data-minsu를 쓴다. 기본 이름 사용과 복잡한 변환 규칙 전체는 구분한다.

> 📚 **출처 · 본문 설명 확인:** [MDN classList](https://developer.mozilla.org/en-US/docs/Web/API/Element/classList), [getAttribute](https://developer.mozilla.org/en-US/docs/Web/API/Element/getAttribute), [dataset](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/dataset). 배운 기능의 뜻을 확인한 근거다. 예제·표·풀이 흐름은 수업 코드를 바탕으로 새로 작성했으며 외부 문장을 직접 인용하지 않았다. 확인일: 2026-10-28.

<a id="example"></a>

## 3. 작은 예제로 먼저 이해하기

**새 설명 예제 · 전체 스크립트.** [HTML 실행 파일](실습/책형_복습/11-02_JavaScript_DOM_속성과_클래스.html)과 같은 폴더의 [JS 파일](실습/책형_복습/11-02_JavaScript_DOM_속성과_클래스.js)을 함께 내려받는다. HTML을 브라우저로 열고 Console에서 결과를 확인한다. script는 필요한 HTML 뒤에 연결한다. 콘솔 출력은 페이지 본문에 자동으로 쓰이지 않는다.

**먼저 준비할 HTML · body 안:**

```html
    <p id="notice" class="message" data-name="공지">안내</p>
```

**위 파일 head의 style:**

```css
        .blue { color: blue; }
```

```javascript
const notice = document.getElementById('notice');
console.log(notice.hasAttribute('data-name'));
console.log(notice.getAttribute('data-name'));
console.log(notice.dataset.name);
notice.classList.add('blue');
notice.classList.add('blue');
console.log(notice.classList.contains('blue'));
notice.classList.toggle('blue');
console.log(notice.classList.contains('blue'));
notice.dataset.minsu = '학생';
console.log(notice.getAttribute('data-minsu'));
```

data-name이 존재해 true, 두 읽기 방식 모두 공지를 얻는다. blue는 두 번 추가해도 하나이고 toggle로 제거해 최종 false다. 중간의 파란 화면이 매 단계 보인다고 보장하지 않고 최종 상태와 Console을 본다. 마지막 대입은 data-minsu 속성에 학생을 쓴다.

**예상 출력 또는 관찰:**

```text
true
공지
공지
true
false
학생
```

<a id="my-code"></a>

## 4. 내가 작성한 코드를 따라 읽기

아래는 원본의 일부다. 원본에 의존하는 앞 선언·HTML·함수는 다음 절의 연결까지 읽는다. 주석의 잘못된 표현도 원문대로 보존하고 설명에서 교정한다.

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_html/javascript/11_dom.html` 121–136행

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

**발췌 바로 풀이:** 두 코드의 결과는 같다. aha는 이미지 요소다. hasAttribute('src')는 속성이 있는지 검사하여 true를 반환한다. getAttribute('src')는 이미지 주소 **문자열**을 반환한다. 없는 src2 속성을 읽으면 null이다. 내 주석의 ‘속성명 가져오기’는 ‘속성값 가져오기’로 교정한다.

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_html/javascript/11_dom.html` 158–174행

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

**발췌 바로 풀이:** blue가 없던 상태에서 add두번은 하나만 추가하고, remove두번은 없는 상태를 유지한다. 이어 toggle두번이면 다시 없어져 contains는false다. contains는 검사만 한다. 최종클래스와 중간표현을 구분한다.

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_html/javascript/11_dom.html` 176–180행

```javascript
            div2.classList.add('blue')

            // remove()로 DOM을 지우면 되돌릴 수 없음
            // 보통은 display:none으로 잠깐 안 보이게 했다가 나오게 함
            div2.remove()
```

**발췌 바로 풀이:** classList.remove('blue')는 클래스 하나를 제거한다. div2.remove()는 div2 요소를 문서에서 떼어 낸다. 내 주석의 ‘되돌릴 수 없음’은 정확하지 않다. div2 변수가 여전히 요소를 참조하고 있으므로, 다음 장에서 배울 append로 다시 연결할 수 있다. display:none은 문서에 요소를 둔 채 표시를 숨기는 방법이라 remove와 동작이 다르다.

내 aha는 이미지이며 src 존재 검사는 true, src 값 읽기는 주소 문자열, 없는 src2는 null이다. 원본은2초 뒤 src 변경만 예약하고 human 추가·삭제는 타이머 밖에서 먼저 끝낸다. 내 classList의 add 두 번·remove 두 번·toggle 두 번 뒤 blue는 없어 contains 결과 false다. 마지막 div2.remove()는 class 제거가 아닌 요소 분리다.

<a id="connections"></a>

## 5. 선언·호출·파일이 연결되는 흐름

HTML의 class·data 속성 → 선택한 요소 → 속성 또는 classList 조작 → CSS 조건·DOM 상태 순서다. 강사님 피자 퀴즈는 pizza가 select를 가리키고 options[selectedIndex]로 현재 option을 얻어 data-name을 두 방식으로 읽는다. 값10과 이름 불고기를 별도 보관하는 의미다. 내11번에 없는 dataset 코드를 학생 원본으로 만들지 않는다.

<a id="review"></a>

## 6. 잘한 점·아쉬운 점·개선 방향

**잘한 점:** toggle 주석은 상태 반전을 명확히 설명한다. **교정:** remove하면 되돌릴 수 없다는 메모는 정확하지 않다. 변수의 참조가 남으면 요소는 자동 null이 되지 않고 뒤 append 학습으로 다시 연결할 수 있다. **개선 방향:** 무엇을 제거하는지 메서드의 주체를 확인하고 이미지 src 변경과 실제 다운로드 성공도 구분한다.

개선안은 원본을 수정한 결과가 아니다. 실제 오류, 수업용 단순화, 목적에 따른 선택을 구별해 판단한다.

<a id="teacher"></a>

## 7. 강사님 코드가 도움이 되는 비교

출처: `D:/workspace_teacher/workspace_html/javascript/퀴즈/이벤트.html` 122–128행

```javascript
        console.log(pizza.options)
        console.log(pizza.selectedIndex)
        const option = pizza.options[pizza.selectedIndex]
        console.log(option.innerText)
        console.log(option.getAttribute('data-name'))
        console.log(option.dataset.name)
        option.dataset.minsu = '강사'
```

위 dataset은 강사님 퀴즈에만 있지만 학습 확인을 근거로 본문에 넣었다. 학생 코드가 없는 차이를 숨기지 않고 내 getAttribute와 연결한다. 같은 classList 코드는 중복 인용하지 않는다. 주문 계산 전체는 이후 이벤트 실습에서 다룬다.

<a id="results"></a>

## 8. 결과를 추적하고 한 가지 바꾸기

| 원본 blue 조작 직후 | 상태 |
| --- | --- |
| add·add |있음·중복 없음 |
| remove·remove |없음·그대로 |
| toggle |있음 |
| 다시 toggle |없음 |
| contains |false·변경 없음 |

하나의 스크립트가 바로 실행되면 중간 색들이 화면에 차례로 보이지 않을 수 있다. 중간 상태 검사는 출력으로, 최종 표시는 최종 클래스로 구분한다.

| 한 가지 변경 | 예상 | 이유 |
| --- | --- | --- |
| 작은예제toggle만제거 |contains둘다true |blue유지 |
| 원래data-name값만복습으로 |두읽기결과복습 |같은속성 |
| 원래CSS.blue규칙만제거 |class결과는같음 |표시와속성분리 |

속성값 null과 존재 검사 false를 혼동하지 않는다. 색이 그대로라고 class 추가 실패부터 판단하지 말고 CSS 규칙·우선순위·최종 클래스를 본다. 요소가 없으면 속성 메서드를 호출하기 전 선택 결과를 확인한다.

<a id="tips"></a>

## 9. 추가로 알면 좋은 것과 출처

> 💡 **TIP · 수업 범위 밖:** dataset의 복잡한 이름 변환·속성 전체 순회 도구는 추가 학습이다. 기본은 data-name 읽기와 data-minsu 쓰기까지다.



이 절의 확장은 기본 문제의 필수 조건이 아니다. 📚 출처가 있다는 것과 수업 밖 기능이라는 것은 다른 구분이다.

<a id="practice"></a>

## 10. 복습과 빠른 정리

1. 문자열 값을 주는 속성 읽기는?
2. blue가 없는 상태에서 toggle 두 번 후는?
3. remove 후 변수는 자동 null인가?

<details>
<summary>짧은 풀이 — 먼저 답한 뒤 확인</summary>

getAttribute이며 없는 속성은 null이다. toggle 두 번이면 다시 없다. 요소가 분리되어도 변수 참조는 자동 null이 아니다.

</details>

| 목적 | 도구 |
| --- | --- |
| 존재 |hasAttribute |
| 값 |get/setAttribute |
| 클래스 |classList |
| data속성 |dataset |

[장별 연습문제](실습/연습문제/11-02_JavaScript_DOM_속성과_클래스_연습문제.md)에서 예상·설명·수정을 이어 간다. 다음은 [콘텐츠](12_JavaScript_DOM_콘텐츠생성과_스타일조작.md)다.

<!-- 이전 색인 이동 주소 보존 -->
<a id="section-1"></a>
<a id="section-2"></a>
<a id="section-3"></a>
<a id="section-4"></a>
<a id="section-5"></a>
<a id="section-6"></a>

[이 장의 목차](#chapter-toc)에서 현재 설명을 찾는다.
