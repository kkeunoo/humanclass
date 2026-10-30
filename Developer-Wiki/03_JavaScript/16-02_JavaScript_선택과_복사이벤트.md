# 16-02. 선택과 복사 — 기본 동작을 취소하고 데이터를 지정하기

[JavaScript 목차](README.md) · [읽기 안내](00_JavaScript_V3_동작_백과_읽기법.md)

선택한 글자, 복사 이벤트, 클립보드에 지정할 데이터는 서로 다른 단계다. 이 장에서는 브라우저가 원래 하려는 일을 취소하는 것과 우리 함수가 실행을 끝내는 것을 구별한다. 창 크기도 문서 전체 크기와 나누어 읽는다.

<a id="chapter-toc"></a>

**이 장의 목차:** [목표](#learn) · [개념](#concepts) · [예제](#example) · [내 코드](#my-code) · [연결](#connections) · [평가](#review) · [비교](#teacher) · [결과·실험](#results) · [TIP·출처](#tips) · [복습](#practice)

<a id="learn"></a>

## 1. 이 장에서 배울 것

선택 내용 읽기 → 빈 선택 검사 → 문자열 만들기 → 복사 데이터 지정 흐름을 설명한다. return·preventDefault와 이벤트 처리 방식의 차이, innerWidth·innerHeight의 기준을 구분한다.

입력·현재 상태·실행 순서·결과를 분리해 설명한다. 실제 수업 원본은 아래에 표시하고, 원본에 없는 선택 학습은 9절 TIP에 둔다.

<a id="concepts"></a>

## 2. 무엇이며, 왜 필요한가

기본 동작은 브라우저가 해당 사건에 원래 연결해 둔 작업이다. 복사 이벤트에서 preventDefault()를 호출하면 취소 가능한 기본 복사를 취소한다. return은 현재 함수를 끝낼 뿐이며, addEventListener의 콜백에서 return false만 쓴다고 기본 동작이 자동으로 취소되지 않는다.

| 기능 | 하는 일 | 하지 않는 일 |
| --- | --- | --- |
| getSelection().toString() | 현재 선택 글자를 문자열로 읽음 | 클립보드 전체를 읽지 않음 |
| preventDefault() | 취소 가능한 기본 동작 취소 | 함수 실행·전파를 자동 중단하지 않음 |
| return | 현재 함수 종료 | 그 자체로 기본 복사를 취소하지 않음 |
| clipboardData.setData | 이번 복사 이벤트의 데이터 지정 | 출처 주소를 자동 탐색하지 않음 |

oncontextmenu처럼 이벤트 처리 속성에 넣은 함수의 false 반환은 해당 기본 동작 취소에 쓰인다. 이를 addEventListener 콜백의 일반 반환값과 혼동하지 않는다. onselectstart를 막는 것은 글자 선택 시작을 제한하는 실습이며 모든 요소 드래그나 문서 복제를 막는 장치가 아니다.

> 📚 **출처 · 본문 설명 확인:** [MDN copy 이벤트](https://developer.mozilla.org/en-US/docs/Web/API/Element/copy_event), [innerWidth](https://developer.mozilla.org/en-US/docs/Web/API/Window/innerWidth). 배운 기능의 뜻을 확인한 근거다. 예제·표·풀이 흐름은 수업 코드를 바탕으로 새로 작성했으며 외부 문장을 직접 인용하지 않았다. 확인일: 2026-10-28.

<a id="example"></a>

## 3. 작은 예제로 먼저 이해하기

**새 설명 예제 · 전체 스크립트.** [HTML 실행 파일](실습/책형_복습/16-02_JavaScript_선택과_복사이벤트.html)과 같은 폴더의 [JS 파일](실습/책형_복습/16-02_JavaScript_선택과_복사이벤트.js)을 함께 내려받는다. HTML을 브라우저로 열고 Console에서 결과를 확인한다. script는 필요한 HTML 뒤에 연결한다. 콘솔 출력은 페이지 본문에 자동으로 쓰이지 않는다.

**먼저 준비할 HTML · body 안:**

```html
    <p id="area" tabindex="0">복사 연습</p>
    <button id="preview" type="button">문자열 결과 미리 보기</button>
    <p id="result"></p>
    <p id="size">창 크기를 바꾸면 표시합니다.</p>
```

```javascript
const area = document.getElementById('area');
function makeCopyText(selection) {
    return selection + '[출처] www.naver.com';
}
document.getElementById('preview').addEventListener('click', function () {
    const result = makeCopyText('복사 연습');
    document.getElementById('result').textContent = result;
    console.log(result);
});
area.addEventListener('copy', function (event) {
    event.preventDefault();
    const selection = window.getSelection().toString();
    if (selection.length === 0) return;
    event.clipboardData.setData('text/plain', makeCopyText(selection));
});
window.addEventListener('resize', function () {
    document.getElementById('size').textContent =
        '가로 ' + window.innerWidth + ', 세로 ' + window.innerHeight;
});
```

먼저 미리 보기 버튼을 누르면 같은 문자열 처리 함수를 호출해 결과를 화면과 Console에 보여 준다. 이 버튼은 클립보드에 쓰지 않는다. 별도로 area의 글자를 선택하고 복사하면 copy 리스너가 선택 내용을 읽어 이번 복사 데이터를 지정한다. 함수 makeCopyText는 문자열을 받아 출처 문구를 붙인 문자열을 반환한다. 함수 정의·미리 보기 호출·복사 처리 호출을 모두 실어 연결을 따라갈 수 있게 했다. 자동 검증은 미리 보기 결과를 확인했으며, 운영체제 클립보드에 실제로 복사한 것으로 보고하지 않는다.

**예상 출력 또는 관찰:**

```text
복사 연습[출처] www.naver.com
```

<a id="my-code"></a>

## 4. 내가 작성한 코드를 따라 읽기

아래는 원본의 일부다. 원본에 의존하는 앞 선언·HTML·함수는 다음 절의 연결까지 읽는다. 주석의 잘못된 표현도 원문대로 보존하고 설명에서 교정한다.

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_html/javascript/asset/js/16_event_mouse.js` 21–32행

```javascript
    // 우클릭 하는 메뉴를 컨텍스트 메뉴라고 함
    const area = document.querySelector('#area')
    // contextmenu를 false로 주게되면 해당 영역은 우클릭 메뉴를 사용할 수 없음
    area.oncontextmenu = () => {
        alert('오른쪽 버튼 금지입니다')
        return false;
    }

    // selectstart로 해당 영역 드래그를 막을 수 있음
    area.onselectstart = function() {
        return false;
    }
```

**발췌 바로 풀이:** oncontextmenu 함수는 안내창을 띄운 뒤 false를 반환하여 해당 메뉴의 기본 동작을 취소한다. onselectstart의 false는 글자 선택이 시작되는 기본 동작을 막는다. 내 주석의 ‘드래그 막기’는 여기서 **글자 선택 시작을 막기**로 정확히 읽는다. 앞 장에서 구현한 모든 요소 이동 기능을 금지하는 것은 아니다.

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_html/javascript/asset/js/16_event_mouse.js` 34–53행

```javascript
    const area2 = document.querySelector('#area2')
    // oncopy는 ctrl+c 등 복사할 때 발생하는 이벤트 (클립보드에 저장되는 것)
    area2.addEventListener('copy', function(event) {
        // preventDefault는 ctrl+c 등이 하는 기본을 막아주는 것
        event.preventDefault()
        
        // selection은 드래그를 했을 때 영역을 알려줌
        const selection = window.getSelection().toString()
        console.log(selection)
        if(selection.length == 0) {
            return
        }

        // 아래처럼 clipboard 영역에 str로 추가해주면, 출처가 붙어서 나옴
        const str = '[출처] www.naver.com'
        const result = selection + str

        // plain은 텍스트에 순수한 글씨, 거기에 result를 추가
        event.clipboardData.setData('text/plain', result)
    })
```

**발췌 바로 풀이:** 양쪽 로직은 같다. #area2에서 copy 이벤트가 발생하면 기본 복사를 취소하고 현재 선택된 글자를 문자열로 읽는다. 비어 있으면 함수를 끝내고, 글자가 있으면 정해 둔 출처 문구를 이어 붙여 복사 데이터를 지정한다.

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_html/javascript/asset/js/16_event_mouse.js` 138–145행

```javascript
    window.addEventListener('resize', function(evt) {
        // 아래와 같이 입력하면, w와 h에 브라우저 안쪽 width, height를 알 수 있음
        // 단, 스크롤 영역을 제외한 부분이기 때문에 그 부분까지면 아우터를 써야 함
        const w = window.innerWidth
        const h = window.innerHeight

        log(`화면w:${w}, 높이h:${h}`)
    })
```

**발췌 바로 풀이:** 창 크기가 바뀌면 가로·세로 값을 읽어 log에 표시한다. 숫자는 현재 환경에 따라 달라지므로 고정 정답으로 적지 않는다. 이벤트를 등록했다는 이유만으로 최초 한 번 자동 출력되는 것도 아니다.

양쪽 원본은 기본 복사를 먼저 취소하고 선택 글자를 읽는다. 빈 문자열이면 return으로 끝내며 그 아래 setData는 실행하지 않는다. 선택이 있으면 고정 출처 문구를 바로 붙인다. 사이에 공백이나 줄바꿈을 넣는 코드가 없으므로 결과에도 임의로 넣지 않는다. www.naver.com은 실습에 적은 고정 문자열일 뿐, 선택 글의 실제 출처를 알아낸 결과가 아니다. 문자열을 이어 붙이는 작업은 해당 사이트로 요청을 보내지 않는다.

<a id="connections"></a>

## 5. 선언·호출·파일이 연결되는 흐름

HTML의 area2 → load 후 bind에서 copy 리스너 등록 → 사용자의 선택·복사 → 이벤트 객체 전달 → 선택 문자열 읽기 → 빈 문자열이면 종료 → 결과 문자열 생성 → clipboardData.setData 순서다. 새 예제는 중복되는 문자열 생성을 makeCopyText로 분리한 개선 예제다. resize 함수는 창 크기가 바뀔 때 실행하며, 등록한 것만으로 최초 값이 자동 출력되지는 않는다.

<a id="review"></a>

## 6. 잘한 점·아쉬운 점·개선 방향

**잘한 점:** 내 주석은 선택 내용·문자열 연결·복사 데이터 지정의 목적을 짚었다. **교정:** selectstart에서 막는 것은 글자 선택 시작이다. innerWidth·innerHeight는 뷰포트 안쪽 크기이며 표시되는 스크롤바를 포함할 수 있다. outerWidth·outerHeight는 브라우저 창 바깥 크기이지 문서 전체 크기가 아니다. **조건 확인:** 기본 취소가 빈 선택 검사보다 먼저 있으므로 빈 선택에서도 이미 취소한 상태다. 새 예제도 이 순서를 유지한다.

개선안은 원본을 수정한 결과가 아니다. 실제 오류, 수업용 단순화, 목적에 따른 선택을 구별해 판단한다.

<a id="teacher"></a>

## 7. 강사님 코드가 도움이 되는 비교



양쪽의 핵심 복사 로직은 같아 강사님 코드를 반복하지 않는다. 내 주석 중 스크롤 영역을 포함하려면 outer를 쓴다는 설명은 교정해야 한다. 이것은 학생 코드의 출력 오류가 아니라 크기 API를 설명한 주석의 오류다. resize의 실제 숫자는 환경에 따라 바뀌므로 특정 화면 크기를 모든 사람의 정답으로 싣지 않는다.

<a id="results"></a>

## 8. 결과를 추적하고 한 가지 바꾸기

| 순서 | 선택이 '복사 연습'인 경우 | 빈 선택인 경우 |
| --- | --- | --- |
| preventDefault | 기본 복사 취소 | 기본 복사 취소 |
| 선택 글자 읽기 | '복사 연습' | '' |
| 길이 검사 | 계속 진행 | return으로 종료 |
| setData | 출처를 붙인 문자열 지정 | 실행하지 않음 |

15장의 Ctrl+C 안내창은 키 조합을 보고 알림을 띄운다. 이 장의 copy 처리는 복사 사건의 기본 동작을 취소하고 데이터를 지정한다. 같은 키를 눌렀을 때 보였다는 이유로 두 처리를 같은 기능이라고 설명하지 않는다.

| 한 가지만 변경 | 예상 결과 | 확인 지점 |
| --- | --- | --- |
| 출처 앞에 공백 한 칸 추가 | 결과 사이에도 공백 추가 | 문자열 그대로 연결 |
| 미리 보기 인수를 '연습'으로 변경 | 연습 뒤에 출처 문구 | 함수 입력과 반환 |
| resize 대신 최초 한 번 크기 읽기 | 이후 크기 변경은 반영 안 됨 | 관찰 시점과 등록의 차이 |

출처가 붙지 않으면 글자를 선택한 영역과 copy 등록 대상을 확인한다. 빈 선택이면 원본은 setData 전에 끝난다. 미리 보기 버튼으로 출력만 확인했다고 실제 복사가 완료되었다고 판단하지 않는다. 창 크기가 처음 안 보이면 resize가 실제 발생했는지 확인한다.

<a id="tips"></a>

## 9. 추가로 알면 좋은 것과 출처

> 💡 **TIP · 수업 범위 밖:** navigator.clipboard의 별도 읽기·쓰기와 권한 처리, 모바일 선택 UI 지원은 추가 학습이다. 본문은 수업의 copy 이벤트와 clipboardData를 중심으로 읽는다.



이 절의 확장은 기본 문제의 필수 조건이 아니다. 📚 출처가 있다는 것과 수업 밖 기능이라는 것은 다른 구분이다.

<a id="practice"></a>

## 10. 복습과 빠른 정리

1. 빈 선택이면 기본 복사가 취소되기 전인가, 후인가?
2. makeCopyText는 클립보드에 직접 쓰는가?
3. innerHeight는 문서 전체 콘텐츠 높이인가?

<details>
<summary>짧은 풀이 — 먼저 답한 뒤 확인</summary>

이미 취소한 뒤 return으로 끝난다. makeCopyText는 문자열을 반환할 뿐이며 실제 데이터 지정은 copy 리스너의 setData가 한다. innerHeight는 뷰포트 안쪽 높이로 문서 전체 높이와 다르다.

</details>

| 구분 | 질문 |
| --- | --- |
| 선택 | 현재 어떤 글자를 골랐나? |
| 반환 | 함수가 어떤 문자열을 돌려주나? |
| 복사 | 이벤트 데이터에 무엇을 지정하나? |
| 크기 | 뷰포트와 창·문서를 구분했나? |

[장별 연습문제](실습/연습문제/16-02_JavaScript_선택과_복사이벤트_연습문제.md)에서 예상·설명·수정을 이어 간다. 다음은 [폼 이벤트](17_JavaScript_폼이벤트와_이벤트전파_실전문제.md)다.

<!-- 이전 색인 이동 주소 보존 -->
<a id="section-1"></a>
<a id="section-2"></a>
<a id="section-3"></a>
<a id="section-4"></a>
<a id="section-5"></a>
<a id="section-6"></a>

[이 장의 목차](#chapter-toc)에서 현재 설명을 찾는다.
