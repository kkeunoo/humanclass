# 14. 미디어쿼리 — 조건이 맞을 때 규칙 더하기

[CSS 목차](README.md) · [읽기 안내](00_CSS_V3_동작_백과_읽기법.md)

좁은 화면에서 같은 목록을 세로로 보이게 하려면 조건에 따라 CSS를 적용할 수 있다. 기존 CSS를 지우고 새 파일로 갈아끼우는 동작이 아니라 조건에 맞는 선언이 후보에 더해지는 것이다.

<a id="chapter-toc"></a>

**이 장의 목차:** [목표](#learn) · [개념](#concepts) · [작은 예제](#example) · [내 코드](#my-code) · [연결](#connections) · [평가](#review) · [비교](#teacher) · [결과·실험](#results) · [TIP·출처](#tips) · [복습](#practice)

<a id="learn"></a>

## 1. 이 장에서 배울 것

max-width 경계의 포함 여부를 예상한다. 기본 규칙과 조건 규칙을 함께 읽고, 투명도·hover·박스 크기 문제와 조건 불일치를 구분한다.

이번 장의 개념과 원본 기능은 수업 범위다. 원본에 없는 선택 기능은 9절 TIP으로 구분한다. 결과를 읽을 때는 선택된 요소·속성·기준값·실행 상태를 함께 적는다.

<a id="concepts"></a>

## 2. 무엇이며, 왜 필요한가

@media는 현재 환경의 조건이 맞을 때 안쪽 규칙을 적용한다. max-width:600px는 600px를 포함한 이하, min-width:500px는 500px를 포함한 이상이다. and로 연결하면 둘 다 만족해야 한다. 조건값은 이 예제에서 CSS 픽셀의 뷰포트 너비로 읽는다.

| 조건 | 499px | 500px | 600px | 601px |
| --- | --- | --- | --- | --- |
| max-width:600px | 맞음 | 맞음 | 맞음 | 아님 |
| min-width:500px and max-width:600px | 아님 | 맞음 | 맞음 | 아님 |

쿼리가 맞아도 모든 속성이 새 값이 되는 것은 아니다. 안쪽에서 선언한 속성이 현재 요소에 맞는지, 기본 규칙과 경쟁할 때 무엇이 적용되는지도 본다. 작은 화면을 고려하는 반응형은 조건문 하나의 존재뿐 아니라 내용과 박스가 실제로 들어가는지까지 살펴야 한다.

viewport 메타는 모바일에서 레이아웃 뷰포트를 기기 너비에 맞춰 보려는 설정이다. 화면의 물리 픽셀 수만 보고 조건을 판정하지 않는다.

> 📚 **출처 · 본문 설명 확인:** [W3C media queries](https://www.w3.org/TR/mediaqueries-4/). 설명과 비교 표는 수업 원본을 바탕으로 새로 풀어 썼다. 외부 원문을 직접 인용한 문장은 아니다. 확인일: 2026-10-28.

<a id="example"></a>

## 3. 작은 예제로 먼저 이해하기

**새 설명 예제 · 전체 파일.** [실행 파일](실습/책형_복습/14_CSS_미디어쿼리와_반응형.html)을 브라우저로 연다. 이 예제는 위 style 안에 CSS를 모두 넣어 외부 파일 연결이 필요 없다. 원본 CSS에 붙이면 다른 규칙이 섞일 수 있으므로 먼저 별도 파일로 확인한다.

```html
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>14. 미디어쿼리 — 조건이 맞을 때 규칙 더하기</title>
    <style>
        .item { display: inline-block; width: 100px; border: 1px solid black; box-sizing: border-box; }
        .notice { display: none; }
        @media screen and (max-width: 600px) {
            .item { display: block; width: 100%; }
            .notice { display: inline; }
        }
    </style>
</head>
<body>
    <h1>600px 경계 관찰</h1>
    <p class="notice">좁은 화면</p>
    <div class="item">HTML</div>
    <div class="item">CSS</div>
</body>
</html>
```

601px 이상에서는 두 항목이 inline-block·100px이고 안내는 숨긴다. 600px에서는 block·100%와 안내 inline이 적용된다. 새 예제는 원본의 hover 메뉴를 제거하여 너비 조건만 관찰한다. item의 border-box로 100% 안에 테두리가 포함되도록 했다. 601·600·599px를 각각 확인하면 경계 해석을 점검할 수 있다.

<a id="my-code"></a>

## 4. 내가 작성한 코드를 따라 읽기

아래는 **내 원본 발췌**다. 주석의 표현도 원문대로 두었다. 설명에서 교정한 내용을 원본에 이미 수정한 것처럼 읽지 않는다.

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_html/css/14_media.html` 25–37행

```css
        @media screen 
        and (max-width: 600px)
        /* and (min-width: 500px) */
        {
            /* 또 다른 CSS 영역 */
            li {
                display: block;
                width: 100%;
            }

            span {
                display: inline;
            }
```

**발췌 바로 풀이:** 이 파일은 양쪽 내용이 같다. min-width:500px는 주석이므로 현재 500px보다 작은 화면도 조건에 맞는다. 주석을 해제해 and로 연결하면 500~600px 사이만 만족한다.

내 원본과 강사님 파일은 같다. min-width:500px는 주석이라 현재 499px에서도 max-width:600px 조건에 맞는다. 원본 ul은 좁은 화면에서 opacity:0·top:-20px로 설정하고 span:hover + ul일 때 opacity:1·top:0으로 바뀐다. 조건이 맞는데 메뉴가 안 보이는 상황은 쿼리 실패가 아니라 안쪽 숨김 규칙 때문일 수 있다.

<a id="connections"></a>

## 5. 파일·요소·값이 연결되는 흐름

뷰포트 너비 → 쿼리 일치 → li 배치·span 표시·ul 투명도 각각 적용 → hover 상태 → 실제 메뉴 관찰 순서다. opacity:0은 자리를 없애지 않는다. span에서 ul로 포인터가 옮겨 가면 hover가 풀릴 수 있고, span은 일반적인 키보드 버튼 역할을 자동으로 갖지 않는다.

<a id="review"></a>

## 6. 잘한 점·아쉬운 점·개선 방향

**잘한 점:** 하나의 600px 경계로 배치와 안내 표시를 비교할 수 있다. **실제 한계:** 터치·키보드까지 완성된 메뉴가 아니다. hover에만 있는 transition은 복귀가 비대칭이고, width:100%의 content-box 테두리 때문에 2px 넘칠 수 있다. **개선 방향:** 먼저 배운 border-box로 너비 넘침을 교정하고, 완성된 토글 구현은 새 학습으로 구별한다.

제안은 원본을 수정한 결과가 아니다. **실제 오류**, **관찰을 위한 수업용 단순화**, **목적에 따라 가능한 선택**을 구별한다. 단지 짧게 쓰거나 최신 기능을 쓴다고 더 좋은 코드는 아니다.

<a id="teacher"></a>

## 7. 강사님 코드가 도움이 되는 비교



같은 파일을 두 번 인용하지 않고 내 발췌를 기준으로 설명한다. 같은 코드라는 사실이 완성 메뉴를 보장하지는 않는다. 강사님 코드도 수업 관찰 목적의 짧은 예제일 수 있으므로 제품 기능의 완성도와 배운 조건을 공정하게 나눠 평가한다.

<a id="results"></a>

## 8. 결과를 예상하고 한 가지 바꾸기

아래는 **명시한 조건에서의 코드 기준 예상**이다. 이번 편집에서 실제 브라우저 렌더링을 재실행했다는 기록과 구별한다. 매 실험은 원래 예제로 돌아가 한 조건만 바꾼다.

| 한 가지 변경 | 예상 | 비교 |
| --- | --- | --- |
| max 값만 500px | 경계가 500px로 이동 | 500px 포함 |
| 원래 조건에 min-width:500px 추가 | 500~600px에서만 적용 | and 조건 |
| 원래 item의 box-sizing만 content-box | 100%에 테두리 추가 가능 | 조건은 같음 |
| 원래 notice 표시 규칙만 제거 | 조건이 맞아도 안내 숨김 | 속성별 확인 |

좁은 화면에서 안 보이면 조건·선택자·display·opacity를 나누어 본다. 브라우저 창 전체 폭과 실제 페이지 뷰포트 폭을 혼동하지 않는다. 경계 검사 기록에는 사용한 너비를 적는다.

<a id="tips"></a>

## 9. 추가로 알면 좋은 것과 출처

> 💡 **TIP · 수업 범위 밖:** Container Query·새 장치 조건·키보드와 터치를 지원하는 토글 메뉴 전체 구현은 추가 학습이다. 수업 미디어쿼리의 정답에 임의로 요구하지 않는다.

이하의 내용은 **수업 원본에서 확인된 필수 진도가 아닌 추가 학습**이다. 위의 기본 설명을 이해한 뒤 필요할 때 읽는다.

<a id="extra-01-4"></a>

### 4. 미디어쿼리와 Container Query

```css
/* 추가 예제: 부모의 가로 크기를 기준으로 자식 표현 변경 */
.panel { container-type: inline-size; }
@container (min-width: 500px) {
    .panel-content { display: flex; }
}
```

수업의 미디어쿼리는 뷰포트 조건을 보지만, 이 예제는 크기 질의 컨테이너가 된 부모의 너비를 본다. 같은 화면에서도 좁은 사이드바와 넓은 본문에 들어간 컴포넌트가 달리 반응하게 만들 때 학습할 수 있다. [컨테이너 질의 표준](https://www.w3.org/TR/css-contain-3/)

이 절의 확장은 기본 문제의 필수 조건이 아니다. 2절의 📚 출처는 배운 기능의 설명을 확인하는 근거이며, 출처가 있다는 이유로 모두 수업 밖 내용인 것은 아니다.

<a id="practice"></a>

## 10. 복습과 빠른 정리

1. 600px도 max-width:600px에 맞는가?
2. min-width:500px가 주석이면 499px는 제외되는가?
3. 쿼리 일치가 메뉴 표시 성공과 같은가?

<details>
<summary>짧은 풀이 — 먼저 답한 뒤 확인</summary>

600px는 포함한다. 주석의 min 조건은 실행되지 않아 499px도 max 조건에 맞는다. 안쪽 opacity 등 다른 속성 때문에 안 보일 수 있다.

</details>

| 확인 | 질문 |
| --- | --- |
| 경계 | 이하·이상의 포함 여부 |
| 조건 조합 | and·주석 |
| 표시 | display·opacity |
| 너비 | content-box·border-box |

[장별 연습문제](실습/연습문제/14_CSS_미디어쿼리와_반응형_연습문제.md)에서 예상·설명·수정을 이어 간다. 다음은 [Flexbox](15_CSS_Flexbox와_유연한_레이아웃.md)다.

<!-- 이전 색인 이동 주소 보존 -->
<a id="css-11"></a>
<a id="css-12"></a>
<a id="css-16"></a>
<a id="css-18"></a>
<a id="css-21"></a>
<a id="css-23"></a>
<a id="css-24"></a>
<a id="css-26"></a>
<a id="css-37"></a>
<a id="css-4"></a>
<a id="css-46"></a>
<a id="css-48"></a>
<a id="css-6"></a>
<a id="section-1"></a>
<a id="section-2"></a>
<a id="section-3"></a>

이전 절 주소로 왔다면 [이 장의 목차](#chapter-toc)에서 현재 설명을 찾는다.
