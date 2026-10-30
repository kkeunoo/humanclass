# 10. float와 clear — 글 감싸기와 다음 흐름

[CSS 목차](README.md) · [읽기 안내](00_CSS_V3_동작_백과_읽기법.md)

float는 요소를 한쪽에 두고 주변 글줄이 그 옆으로 흐르게 한다. clear는 이어지는 요소의 위치를 정리한다. 떠 있는 요소의 선언을 삭제하는 기능으로 외우지 않는다.

<a id="chapter-toc"></a>

**이 장의 목차:** [목표](#learn) · [개념](#concepts) · [작은 예제](#example) · [내 코드](#my-code) · [연결](#connections) · [평가](#review) · [비교](#teacher) · [결과·실험](#results) · [TIP·출처](#tips) · [복습](#practice)

<a id="learn"></a>

## 1. 이 장에서 배울 것

float와 absolute·inline-block의 차이를 구분한다. 후행 clear와 가상 요소 clearfix가 부모 높이에 주는 영향을 추적한다.

이번 장의 개념과 원본 기능은 수업 범위다. 원본에 없는 선택 기능은 9절 TIP으로 구분한다. 결과를 읽을 때는 선택된 요소·속성·기준값·실행 상태를 함께 적는다.

<a id="concepts"></a>

## 2. 무엇이며, 왜 필요한가

float:right인 작은 그림 옆으로 뒤의 글줄이 돌아 흐를 수 있다. 주변 내용이 아무 영향도 받지 않는 absolute와 같지 않다. clear:both는 앞선 float 아래로 해당 요소가 내려오게 하는 조건이며 float:left를 none으로 바꾸지는 않는다.

float 자식만 가진 일반 부모는 기대한 높이로 감싸지 못할 수 있다. 부모 안 마지막에 block과 clear:both를 가진 후행 박스를 두면 그 위치가 부모 높이 계산에 연결된다. clearfix는 실제 빈 div 대신 가상 요소로 이 역할을 구성한 방식이다.

| 방법 | 무엇을 만드는가? |
| --- | --- |
| 빈 div의 clear | 실제 HTML 후행 요소 |
| :after의 content와 clear | CSS 생성 후행 박스 |
| float:none | float 선언 자체를 바꿈 — 위 둘과 다름 |

가상 요소는 실제 HTML에 자식 태그를 추가한 것과 구별한다. 부모 높이를 정리해도 float 자식의 왼쪽·오른쪽 배치 의도는 유지된다.

> 📚 **출처 · 본문 설명 확인:** [W3C float·clear](https://www.w3.org/TR/CSS2/visuren.html#floats). 설명과 비교 표는 수업 원본을 바탕으로 새로 풀어 썼다. 외부 원문을 직접 인용한 문장은 아니다. 확인일: 2026-10-28.

<a id="example"></a>

## 3. 작은 예제로 먼저 이해하기

**새 설명 예제 · 전체 파일.** [실행 파일](실습/책형_복습/10_CSS_Float와_Clear.html)을 브라우저로 연다. 이 예제는 위 style 안에 CSS를 모두 넣어 외부 파일 연결이 필요 없다. 원본 CSS에 붙이면 다른 규칙이 섞일 수 있으므로 먼저 별도 파일로 확인한다.

```html
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>10. float와 clear — 글 감싸기와 다음 흐름</title>
    <style>
        .parent { border: 1px solid black; }
        .left { float: left; width: 100px; height: 60px; background-color: lightblue; }
        .right { float: right; width: 100px; height: 80px; background-color: pink; }
        .clearFix:after { content: ""; display: block; clear: both; }
    </style>
</head>
<body>
    <h1>부모가 감싸는 높이</h1>
    <div class="parent clearFix">
        <div class="left">왼쪽</div>
        <div class="right">오른쪽</div>
    </div>
    <p>그다음 내용</p>
</body>
</html>
```

충분한 가로 공간에서 자식은 좌우에 놓이고 높이는60·80px다. 후행 가상 박스가 두 float 아래에서 정리되어 부모는 그 높이를 감싼다. 다음 p는 정리된 부모 뒤에 이어진다. class를 지웠을 때의 차이는 부모 높이와 다음 글 흐름을 각각 관찰한다.

<a id="my-code"></a>

## 4. 내가 작성한 코드를 따라 읽기

아래는 **내 원본 발췌**다. 주석의 표현도 원문대로 두었다. 설명에서 교정한 내용을 원본에 이미 수정한 것처럼 읽지 않는다.

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_html/css/asset/css/10_float.css` 29–38행

```css
/* float을 clear:both로 내린다고 해도 그 층에 남아있음 */
.clearFix:after {
    content: "";
    display: block;
    clear: both;
}

/* .test {
    clear: both;
} */
```

**발췌 바로 풀이:** 실행되는 clearfix는 같다. `.test`의 clear는 주석 상태다. 부모의 class가 정확히 clearFix인지도 확인한다. 내 HTML의 “float을 초기화”는 **자식의 float 선언을 지우는 것**이 아니라 이후 흐름과 부모 높이를 정리한다는 뜻으로 읽는다.

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_html/css/10_float.html` 26–30행

```html
        <div class="clearFix">
            <div class="box left">왼쪽</div>
            <div class="box right">오른쪽</div>
        </div>
        <div class="test" style="border: 1px solid red;">다른 내용의 시작</div>
```

**발췌 바로 풀이:** 부모가 float 자식 두 개와 가상 요소를 감싸고 다음 내용이 아래에 이어진다. 원본 앞부분의 `<div style="clear:both"></div>`는 실제 빈 요소를 쓰는 방식이고, clearfix는 가상 요소로 같은 종류의 후행 정리 역할을 한다. [float·clear 표준](https://www.w3.org/TR/CSS2/visuren.html#floats)

내 clearFix:after는 content 빈 문자열·display block·clear both로 구성된다. 뒤의 .test는 주석이므로 test class를 붙였다는 사실만으로 실행된다고 읽지 않는다. 함께 인용한 HTML은 부모에 clearFix를 주고 안쪽 두 float를 배치한 연결이다. 내 ‘초기화’ 메모는 자식 float를 지우는 것이 아니라 뒤 흐름을 정리한다는 뜻으로 고쳐 읽는다.

<a id="connections"></a>

## 5. 파일·요소·값이 연결되는 흐름

부모 class="clearFix" → :after 선택 → 부모 내용 끝의 생성 박스 → clear:both → 부모 높이와 다음 내용 위치 순서다. 원본 article의 width100 img·float:right에서는 글 감싸기를 별도로 관찰한다. right float 여러 개는 소스 순서와 화면 왼쪽부터 읽는 순서가 달라질 수 있다.

<a id="review"></a>

## 6. 잘한 점·아쉬운 점·개선 방향

**잘한 점:** CSS 규칙과 부모 HTML 연결을 남겨 clearfix가 어디에 적용되는지 찾기 쉽다. **교정:** float가 자동 inline-block으로 바뀐다는 메모는 정확하지 않다. **설계 한계:** 원본 헤더의 좌우 메뉴 폭이 다르면 남은 영역 가운데와 화면 전체 정중앙이 다를 수 있다. 내 coup 선택자는 해당 HTML 요소가 없어 매칭되지 않는 부분도 구분한다.

제안은 원본을 수정한 결과가 아니다. **실제 오류**, **관찰을 위한 수업용 단순화**, **목적에 따라 가능한 선택**을 구별한다. 단지 짧게 쓰거나 최신 기능을 쓴다고 더 좋은 코드는 아니다.

<a id="teacher"></a>

## 7. 강사님 코드가 도움이 되는 비교



양쪽 clearfix와 부모 연결은 같아 중복 인용하지 않는다. 내 test class는 주석 규칙 때문에 현재 동작 차이를 만들지 않는다. 새 기술로 결과만 바꾸기 전에 배운 float·clear의 영향을 설명할 수 있어야 한다.

<a id="results"></a>

## 8. 결과를 예상하고 한 가지 바꾸기

아래는 **명시한 조건에서의 코드 기준 예상**이다. 이번 편집에서 실제 브라우저 렌더링을 재실행했다는 기록과 구별한다. 매 실험은 원래 예제로 돌아가 한 조건만 바꾼다.

| 한 가지 변경 | 예상 | 관찰 대상 |
| --- | --- | --- |
| 부모 clearFix class만제거 | 부모 높이가 float를 기대대로 못 감쌀 수 있음 | 경계·다음글 |
| 원래 right 높이만120px | 정리된 부모가 더 길어짐 | 더큰float |
| 원래 left float만none | 일반흐름 요소로 바뀜 | clear와다른수정 |

clearFix의 대소문자와 실제 부모 적용을 먼저 확인한다. ‘다음 글이 아래에 있다’는 관찰만으로 자식 float가 사라졌다고 결론 내리지 않는다. 브라우저에서 각 요소의 현재 float도 나눠 본다.

<a id="tips"></a>

## 9. 추가로 알면 좋은 것과 출처

> 💡 **TIP · 수업 범위 밖:** flow-root·shape-outside·Grid 헤더 대체는 추가 학습이다. 수업의 가상 요소·clear를 설명한 뒤 다른 방법과 비교한다.

이하의 내용은 **수업 원본에서 확인된 필수 진도가 아닌 추가 학습**이다. 위의 기본 설명을 이해한 뒤 필요할 때 읽는다.

<a id="extra-01-3"></a>

### 3. float 이후의 flow-root

```css
/* 추가 예제: float 자식을 감싸는 부모 */
.float-parent { display: flow-root; }
```

새 블록 서식 맥락을 만들어 float 자식을 감싸는 높이 계산에 사용할 수 있다. 기존 clearfix의 역할을 비교할 때 유용하지만, 수업에서 배운 가상 요소·clear를 설명하지 못한 채 이것만 정답으로 외우지는 않는다. [CSS display 표준](https://www.w3.org/TR/css-display-3/#valdef-display-flow-root)

display:contents는 요소의 박스와 의미·접근성 영향을 따로 검토해야 한다. shape-outside·복잡한 겹침 맥락·isolation도 별도 심화다.

이 절의 확장은 기본 문제의 필수 조건이 아니다. 2절의 📚 출처는 배운 기능의 설명을 확인하는 근거이며, 출처가 있다는 이유로 모두 수업 밖 내용인 것은 아니다.

<a id="practice"></a>

## 10. 복습과 빠른 정리

1. clear는 앞 float를none으로 바꾸는가?
2. clearfix는 어느 요소에 연결하는가?
3. 주석 .test는 현재 실행되는가?

<details>
<summary>짧은 풀이 — 먼저 답한 뒤 확인</summary>

float 선언 자체는 유지한다. float 자식을 감쌀 부모에 clearFix를 연결한다. 주석 .test는 실행되지 않는다.

</details>

| 기능 | 역할 |
| --- | --- |
| float | 한쪽배치·글흐름 |
| clear | 앞float아래로정리 |
| clearfix | 생성후행박스로정리 |
| 주석 | 현재실행에서제외 |

[장별 연습문제](실습/연습문제/10_CSS_Float와_Clear_연습문제.md)에서 예상·설명·수정을 이어 간다. 다음은 [그림자](11_CSS_그림자와_시각효과.md)다.

<!-- 이전 색인 이동 주소 보존 -->
<a id="css-18"></a>
<a id="css-4"></a>
<a id="section-1"></a>
<a id="section-2"></a>
<a id="section-3"></a>
<a id="section-4"></a>

이전 절 주소로 왔다면 [이 장의 목차](#chapter-toc)에서 현재 설명을 찾는다.
