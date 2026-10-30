# 04. display — 같은 요소를 어떤 방식으로 배치할까

[CSS 목차](README.md) · [읽기 안내](00_CSS_V3_동작_백과_읽기법.md)

너비를 줄였는데도 다음 상자가 옆에 붙지 않거나, span의 width가 듣지 않는 이유는 배치 방식과 관련 있다. 태그의 의미와 CSS 박스 배치를 나누어 이해한다.

<a id="chapter-toc"></a>

**이 장의 목차:** [목표](#learn) · [개념](#concepts) · [작은 예제](#example) · [내 코드](#my-code) · [연결](#connections) · [평가](#review) · [비교](#teacher) · [결과·실험](#results) · [TIP·출처](#tips) · [복습](#practice)

<a id="learn"></a>

## 1. 이 장에서 배울 것

block·inline·inline-block의 줄 배치와 크기 적용을 구분한다. inline-block의 공백·baseline, HTML 중첩 오류를 설명한다.

이번 장의 개념과 원본 기능은 수업 범위다. 원본에 없는 선택 기능은 9절 TIP으로 구분한다. 결과를 읽을 때는 선택된 요소·속성·기준값·실행 상태를 함께 적는다.

<a id="concepts"></a>

## 2. 무엇이며, 왜 필요한가

일반 block은 새 줄을 차지한다. width로 너비를 줄여도 다음 일반 block이 자동으로 옆에 붙지는 않는다. 일반 글자 span 같은 inline은 글 흐름 안에 놓이며 width·height로 상자 크기를 정하는 방식이 아니다. inline-block은 한 줄 흐름에 참여하면서 너비·높이도 가진다. 단, img 같은 대체 요소의 크기 규칙은 일반 글자 inline과 다르다.

| display | 주변 배치 | 크기·주의 |
| --- | --- | --- |
| block | 일반 흐름에서 새 줄 | 남는 공간과 width 확인 |
| inline | 글 흐름에 참여 | 일반 비대체 inline의 width·height는 적용 대상 아님 |
| inline-block | 글 흐름에서 하나의 상자 | width·height, 공백과 수직 정렬 확인 |
| table / table-cell | 표 형태 박스 배치 | HTML table의 의미를 부여하지 않음 |
| none | 박스 생성에서 제외 | 다음 숨김 장에서 비교 |

일반 inline의 위아래 padding·border도 그려진다. 다만 줄 높이를 그 크기만큼 늘려 주는 방식이 아니어서 인접 줄과 겹칠 수 있다. ‘가짜 border’라고 외우기보다 **그려지는 영역과 줄 배치 계산의 차이**로 이해한다. vertical-align도 모든 block을 부모 가운데 놓아 주는 속성은 아니다.

> 📚 **출처 · 본문 설명 확인:** [MDN display](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/display)와 [W3C 인라인 배치](https://www.w3.org/TR/CSS2/visuren.html#inline-formatting). 설명과 비교 표는 수업 원본을 바탕으로 새로 풀어 썼다. 외부 원문을 직접 인용한 문장은 아니다. 확인일: 2026-10-28.

<a id="example"></a>

## 3. 작은 예제로 먼저 이해하기

**새 설명 예제 · 전체 파일.** [실행 파일](실습/책형_복습/04_CSS_Display와_요소배치.html)을 브라우저로 연다. 이 예제는 위 style 안에 CSS를 모두 넣어 외부 파일 연결이 필요 없다. 원본 CSS에 붙이면 다른 규칙이 섞일 수 있으므로 먼저 별도 파일로 확인한다.

```html
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>04. display — 같은 요소를 어떤 방식으로 배치할까</title>
    <style>
        .row { font-size: 0; border: 1px solid black; }
        .item { display: inline-block; width: 100px; height: 50px; border: 1px solid red; vertical-align: top; font-size: 16px; }
        .block { display: block; width: 100px; border: 1px solid blue; }
    </style>
</head>
<body>
    <h1>한 줄과 새 줄</h1>
    <div class="row">
        <div class="item">A</div>
        <div class="item">B<br>둘째 줄</div>
    </div>
    <div class="block">C</div>
    <div class="block">D</div>
</body>
</html>
```

각 item은 내용100+테두리2=102px다. 공간이 충분하면 A·B가 나란히 놓이며 윗부분을 맞춘다. 부모 font-size0은 요소 사이 줄바꿈 공백의 글자 폭을 줄이고, 자식은16px로 복원한다. C·D는 너비가100이어도 일반 block이어서 각각 다음 줄이다. 좁은 화면에서 한 줄 수용 여부는 부모 공간까지 확인한다.

<a id="my-code"></a>

## 4. 내가 작성한 코드를 따라 읽기

아래는 **내 원본 발췌**다. 주석의 표현도 원문대로 두었다. 설명에서 교정한 내용을 원본에 이미 수정한 것처럼 읽지 않는다.

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_html/css/asset/css/04_display.css` 77–98행

```css
.parent3 {
    border: 1px dotted rgb(255, 0, 255);
    font-size: 0px;
}

/* 아래처럼 2줄을 적었을 때 맨 아래 줄 내용(baseline)을 기준으로 줄이 맞춰지기 때문에 약간 올라간 모습 */
/* 아래와 같은 경우 vertical-align으로 정렬을 해줄 수 있다 */
.parent3 > div {
    border: 1px solid red;
    display:inline-block;
    
    width: 100px;
    height: 50px;

    padding: 50px;

    /* vertical은 세로정렬이며 inline에서만 적용 됨(inline, inline-block) */
    vertical-align: top;
    
    /* 4px 공백을 해소하기 위해 부모에 font-size 0을 주고, 하위 자식들에게 별도 font-size를 줌 */
    font-size: 16px;
}
```

**발췌 바로 풀이:** 선언과 결과가 같다. 내 주석의 “4px 공백”은 이때의 관찰값에 가깝다. 공백 폭은 글꼴·글자 크기 등에 따라 달라지므로 항상 4px라고 가정해 음수 margin을 넣지 않는다.

내 parent3의 자식은 width100·padding50·border1이므로 실제너비202px다. font-size0과 자식16px 복원, vertical-align:top은 서로 다른 문제를 다룬다. 앞의 것은 글자 공백, 뒤의 것은 inline-block의 수직 정렬이다. baseline은 글자를 놓는 기준선이며 내용 줄 수 등에 따라 상자 정렬이 예상과 다르게 보일 수 있다. ‘공백4px’는 당시 관찰값이며 항상 같은 상수는 아니다.

<a id="connections"></a>

## 5. 파일·요소·값이 연결되는 흐름

HTML에서 형제 박스 사이 공백 텍스트 존재 → inline 흐름이 공백 폭을 가짐 → 부모 글자 크기 변경의 영향 → 자식 글자 복원 순으로 읽는다. parent2의 text-align:center는 안쪽 inline-block을 정렬하는 부모 규칙이다. 자식 안의 글자 정렬과 구분한다.

<a id="review"></a>

## 6. 잘한 점·아쉬운 점·개선 방향

**잘한 점:** 공백 처리와 수직 정렬 이유를 메모했다. **실제 오류:** 양쪽의 span 안 div 중첩은 허용 콘텐츠에 맞지 않는다. div.block*2가 펼쳐지지 않은 텍스트로 남은 부분도 화면에 나올 수 있다. **개선안:** 바깥을 div로 바꾸거나 안쪽을 span으로 바꾸어 올바른 구조를 먼저 만들고 display로 표시를 정한다. CSS는 잘못된 HTML 의미 구조를 교정하지 않는다.

제안은 원본을 수정한 결과가 아니다. **실제 오류**, **관찰을 위한 수업용 단순화**, **목적에 따라 가능한 선택**을 구별한다. 단지 짧게 쓰거나 최신 기능을 쓴다고 더 좋은 코드는 아니다.

<a id="teacher"></a>

## 7. 강사님 코드가 도움이 되는 비교



강사님 파일은 04_dispaly.html, 내 파일은04_display.html로 철자가 다르다. 실제 파일명을 기준으로 연다. 핵심 CSS 동작이 같아 중복 인용은 생략했다. 강사님의 border 관련 짧은 주석도 인라인 배치의 정확한 규칙으로 보완해서 이해한다.

<a id="results"></a>

## 8. 결과를 예상하고 한 가지 바꾸기

아래는 **명시한 조건에서의 코드 기준 예상**이다. 이번 편집에서 실제 브라우저 렌더링을 재실행했다는 기록과 구별한다. 매 실험은 원래 예제로 돌아가 한 조건만 바꾼다.

| 한 가지 변경 | 예상 | 확인 원리 |
| --- | --- | --- |
| 부모 font-size만16px | 공백 폭 생길 수 있음 | HTML 공백 텍스트 |
| 원래 item display만block | 각각 새 줄 | 배치 방식 |
| 원래 item width만200px | 실제202px | 박스 계산 |
| 원래 vertical-align만baseline | 내용 기준선에 맞춤 | 수직 정렬 |

공백을 제거해도 부모200px에 원본202px 상자 두 개가 들어갈 수는 없다. 글자 공백과 박스 너비 부족을 따로 계산한다. -webkit- 접두 표기를 ‘숨겨진 옵션’이라고 외우지 말고 해당 속성의 지원·표준 여부를 따로 확인한다.

<a id="tips"></a>

## 9. 추가로 알면 좋은 것과 출처

> 💡 **TIP · 수업 범위 밖:** display:contents와 Grid로 재설계하는 방식은 별도 확장이다. Flex는 뒤의 실제 수업 장에서 다루지만 지금 문제의 필수 답안은 아니다.



이 절의 확장은 기본 문제의 필수 조건이 아니다. 2절의 📚 출처는 배운 기능의 설명을 확인하는 근거이며, 출처가 있다는 이유로 모두 수업 밖 내용인 것은 아니다.

<a id="practice"></a>

## 10. 복습과 빠른 정리

1. block 너비를100px로 줄이면 다음 block이 자동 옆으로 붙는가?
2. 일반 span과 img의 width 규칙을 똑같이 설명해도 되는가?
3. inline-block 공백은 늘4px인가?

<details>
<summary>짧은 풀이 — 먼저 답한 뒤 확인</summary>

자동으로 옆으로 붙지 않는다. 일반 비대체 inline과 대체 요소는 구분한다. 공백 폭은 글꼴·크기 등 조건에 따라 달라진다.

</details>

| 문제 | 구분할 것 |
| --- | --- |
| 옆 배치 | display |
| 가로 수용 | border·padding 포함 너비 |
| 틈 | 공백 텍스트 |
| 위아래 어긋남 | baseline·vertical-align |

[장별 연습문제](실습/연습문제/04_CSS_Display와_요소배치_연습문제.md)에서 예상·설명·수정을 이어 간다. 다음은 [투명도와 숨김](05_CSS_투명도와_요소숨김.md)이다.

<!-- 이전 색인 이동 주소 보존 -->
<a id="css-10"></a>
<a id="css-12"></a>
<a id="css-39"></a>
<a id="css-4"></a>
<a id="css-42"></a>
<a id="css-57"></a>
<a id="section-1"></a>
<a id="section-2"></a>
<a id="section-3"></a>
<a id="section-4"></a>

이전 절 주소로 왔다면 [이 장의 목차](#chapter-toc)에서 현재 설명을 찾는다.
