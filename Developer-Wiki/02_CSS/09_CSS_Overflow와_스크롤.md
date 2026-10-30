# 09. overflow — 상자 크기와 넘친 내용을 나누기

[CSS 목차](README.md) · [읽기 안내](00_CSS_V3_동작_백과_읽기법.md)

내용이 많을 때 상자를 늘릴지, 넘친 부분을 보이게 할지, 스크롤할지 구별해야 한다. overflow는 원하는 너비·높이를 대신 정해 주는 속성이 아니다.

<a id="chapter-toc"></a>

**이 장의 목차:** [목표](#learn) · [개념](#concepts) · [작은 예제](#example) · [내 코드](#my-code) · [연결](#connections) · [평가](#review) · [비교](#teacher) · [결과·실험](#results) · [TIP·출처](#tips) · [복습](#practice)

<a id="learn"></a>

## 1. 이 장에서 배울 것

visible·hidden·scroll·auto를 비교한다. nowrap·inline-block·박스 크기로 원본 가로 목록의 넘침을 설명한다.

이번 장의 개념과 원본 기능은 수업 범위다. 원본에 없는 선택 기능은 9절 TIP으로 구분한다. 결과를 읽을 때는 선택된 요소·속성·기준값·실행 상태를 함께 적는다.

<a id="concepts"></a>

## 2. 무엇이며, 왜 필요한가

상자의 정해진 영역 밖으로 내용이 나오는 것이 넘침이다. 높이50px 안에 높이100px 내용이 있다면 크기는 별도로 읽고 넘침 처리값을 살핀다. visible은 바깥으로 그려질 수 있고, hidden은 넘친 부분을 가린다. hidden도 원문 내용을 삭제하는 것은 아니다. auto는 넘침에 따라 스크롤 가능한 영역을 만들며 scroll은 내용이 적어도 스크롤 UI를 위한 상태다. 막대가 항상 눈에 보이는지는 운영체제·브라우저 표시 방식에 영향을 받는다.

| 확인 순서 | 질문 |
| --- | --- |
| 크기 | 상자 너비·높이는 정해졌는가? |
| 내용 | 내용 길이·자식 크기 때문에 실제로 넘치는가? |
| 줄바꿈 | nowrap이 가로 한 줄을 강제하는가? |
| 처리 | 어느 축의 overflow가 무엇인가? |

overflow-y:scroll만 썼다고 가로축은 언제나 visible이라고 단정하지 않는다. 두 축의 계산값이 서로 영향을 줄 수 있다. 한 축만 보아 원인을 결정하기보다 실제 가로·세로 넘침을 나눠 확인한다.

> 📚 **출처 · 본문 설명 확인:** [W3C overflow](https://www.w3.org/TR/css-overflow-3/). 설명과 비교 표는 수업 원본을 바탕으로 새로 풀어 썼다. 외부 원문을 직접 인용한 문장은 아니다. 확인일: 2026-10-28.

<a id="example"></a>

## 3. 작은 예제로 먼저 이해하기

**새 설명 예제 · 전체 파일.** [실행 파일](실습/책형_복습/09_CSS_Overflow와_스크롤.html)을 브라우저로 연다. 이 예제는 위 style 안에 CSS를 모두 넣어 외부 파일 연결이 필요 없다. 원본 CSS에 붙이면 다른 규칙이 섞일 수 있으므로 먼저 별도 파일로 확인한다.

```html
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>09. overflow — 상자 크기와 넘친 내용을 나누기</title>
    <style>
        .window { width: 200px; height: 60px; overflow: auto; border: 1px solid black; }
        .tall { height: 120px; background-color: lightblue; }
        .row { width: 200px; white-space: nowrap; overflow: auto; border: 1px solid red; }
        .item { display: inline-block; width: 100px; border: 1px solid blue; }
    </style>
</head>
<body>
    <h1>넘침의 두 축</h1>
    <div class="window"><div class="tall">높이120px 내용</div></div>
    <div class="row"><div class="item">A</div><div class="item">B</div><div class="item">C</div></div>
</body>
</html>
```

window는60px 영역 안에120px 자식을 담아 세로로 넘친다. row는200px 안에 테두리까지102px인 세 자식이 한 줄로 놓여 가로로 넘친다. 글자 공백을 없애려고 세 div를 이어 썼어도306px 자체가200보다 크다. 두 경우 모두 넘침 원인이 있는 상태에서 auto를 관찰한다.

<a id="my-code"></a>

## 4. 내가 작성한 코드를 따라 읽기

아래는 **내 원본 발췌**다. 주석의 표현도 원문대로 두었다. 설명에서 교정한 내용을 원본에 이미 수정한 것처럼 읽지 않는다.

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_html/css/09_overflow.html` 35–47행

```css
            .parent {
                border: 1px solid red;
                width: 300px;
                white-space: nowrap;
                overflow: auto;
            }

            .parent div {
                border: 1px solid brown;
                display: inline-block;
                width: 100px;
                margin: 5px;
            }
```

**발췌 바로 풀이:** 설정이 같다. 각 항목은 content 100 + border 2 + 좌우 margin 10 = 112px이고, HTML 공백도 사이에 있을 수 있다. 다섯 항목이 300px 안에 들어갈 수 없다. 이 계산은 기본 box-sizing 조건을 따른다.

원본 parent는300px, 자식은 내용100+테두리2+좌우margin10=112px다. 다섯 개면 최소560px이고 사이 HTML 공백도 있을 수 있어 한 줄로는 들어가지 않는다. nowrap은 줄바꿈을 억제하고 auto는 넘친 내용을 볼 통로를 만든다. 각 속성이 하는 일을 나누면 가로 스크롤 원인을 설명할 수 있다.

<a id="connections"></a>

## 5. 파일·요소·값이 연결되는 흐름

HTML 항목 다섯 개 → inline-block 한 줄 배치 → nowrap 유지 → 자식 총너비와 부모300px 비교 → overflow:auto 순서다. 원본 일반 box는 강사님100×130, 나는130×130이라 같은 텍스트도 줄 수·넘침량이 달라질 수 있다. 먼저 조건을 맞춘 뒤 속성 차이를 비교한다.

<a id="review"></a>

## 6. 잘한 점·아쉬운 점·개선 방향

**잘한 점:** 크기·줄바꿈·넘침 처리를 한 예제에 연결했다. **아쉬운 점:** ‘실무에서 auto를 자주 쓰지 않음’이라는 메모는 모든 프로젝트의 규칙이 아니다. **개선 방향:** 보려는 내용과 스크롤 목적을 먼저 정하고 auto·hidden을 고른다. 단순히 화면 밖 내용을 지우려고 hidden을 붙이면 필요한 내용도 가릴 수 있다.

제안은 원본을 수정한 결과가 아니다. **실제 오류**, **관찰을 위한 수업용 단순화**, **목적에 따라 가능한 선택**을 구별한다. 단지 짧게 쓰거나 최신 기능을 쓴다고 더 좋은 코드는 아니다.

<a id="teacher"></a>

## 7. 강사님 코드가 도움이 되는 비교



가로 목록 선언은 같아 강사님 원문을 중복 인용하지 않는다. 일반 box의 너비 차이는 같은 속성이 다른 결과처럼 보이게 할 수 있는 중요한 비교 조건이다. scroll의 막대 모양까지 양쪽 코드가 고정한다고 설명하지 않는다.

<a id="results"></a>

## 8. 결과를 예상하고 한 가지 바꾸기

아래는 **명시한 조건에서의 코드 기준 예상**이다. 이번 편집에서 실제 브라우저 렌더링을 재실행했다는 기록과 구별한다. 매 실험은 원래 예제로 돌아가 한 조건만 바꾼다.

| 한 가지 변경 | 예상 | 이유 |
| --- | --- | --- |
| window overflow만hidden | 넘친 부분 가림·일반 막대 없음 | 처리 변경 |
| 원래 tall 높이만30px | 세로 넘침 없어짐 | 내용이 작아짐 |
| 원래 row nowrap 제거 | 다음 줄 배치 가능 | 한 줄 조건 제거 |
| 원래 row width만400px | 세 항목 수용 | 총306px보다 큼 |

auto인데 차이가 없으면 내용이 실제로 넘치는지 본다. 넘침은 있는데 막대가 늘 보이지 않으면 환경의 자동 숨김 표시를 구분한다. hidden을 ‘데이터 삭제’라고 표현하지 않는다.

<a id="tips"></a>

## 9. 추가로 알면 좋은 것과 출처

> 💡 **TIP · 수업 범위 밖:** overflow:clip·overscroll-behavior·스크롤 잠금 모달 구현은 추가 학습이다. 기본 스크롤 실험의 정답에 필요하지 않다.



이 절의 확장은 기본 문제의 필수 조건이 아니다. 2절의 📚 출처는 배운 기능의 설명을 확인하는 근거이며, 출처가 있다는 이유로 모두 수업 밖 내용인 것은 아니다.

<a id="practice"></a>

## 10. 복습과 빠른 정리

1. hidden이면 내용이 지워지는가?
2. nowrap을 없애면 가로 넘침도 달라질 수 있는가?
3. 같은 속성이면 상자 너비가 달라도 같은 글줄인가?

<details>
<summary>짧은 풀이 — 먼저 답한 뒤 확인</summary>

원문 삭제가 아니다. 줄바꿈 조건이 달라지면 가로 넘침도 바뀔 수 있다. 너비가 다르면 글줄·넘침량이 달라질 수 있다.

</details>

| 원인 | 확인 |
| --- | --- |
| 가로 넘침 | 자식너비·nowrap |
| 세로 넘침 | 높이제한·내용높이 |
| 안 잘림 | 현재overflow·실제대상 |
| 막대 안 보임 | 넘침·환경표시 |

[장별 연습문제](실습/연습문제/09_CSS_Overflow와_스크롤_연습문제.md)에서 예상·설명·수정을 이어 간다. 다음은 [float와 clear](10_CSS_Float와_Clear.md)다.

<!-- 이전 색인 이동 주소 보존 -->
<a id="css-20"></a>
<a id="css-4"></a>
<a id="css-7"></a>
<a id="section-1"></a>
<a id="section-2"></a>
<a id="section-3"></a>

이전 절 주소로 왔다면 [이 장의 목차](#chapter-toc)에서 현재 설명을 찾는다.
