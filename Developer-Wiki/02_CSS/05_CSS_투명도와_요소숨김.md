# 05. 투명도와 숨김 — 보임·자리·조작을 따로 묻기

[CSS 목차](README.md) · [읽기 안내](00_CSS_V3_동작_백과_읽기법.md)

화면에서 안 보인다는 결과가 같아도 자리와 조작 상태가 같지는 않다. 숨김을 세 질문으로 나누면 원본 메모의 장점과 한계를 함께 이해할 수 있다.

<a id="chapter-toc"></a>

**이 장의 목차:** [목표](#learn) · [개념](#concepts) · [작은 예제](#example) · [내 코드](#my-code) · [연결](#connections) · [평가](#review) · [비교](#teacher) · [결과·실험](#results) · [TIP·출처](#tips) · [복습](#practice)

<a id="learn"></a>

## 1. 이 장에서 배울 것

display:none·visibility:hidden·opacity:0을 비교한다. 요소 전체의 opacity와 배경색 알파를 구분한다.

이번 장의 개념과 원본 기능은 수업 범위다. 원본에 없는 선택 기능은 9절 TIP으로 구분한다. 결과를 읽을 때는 선택된 요소·속성·기준값·실행 상태를 함께 적는다.

<a id="concepts"></a>

## 2. 무엇이며, 왜 필요한가

display:none은 박스를 배치에서 제외한다. visibility:hidden은 보이지 않게 하지만 자리는 유지한다. opacity:0은 요소 전체를 완전히 투명하게 합성하지만 이것만으로 클릭이나 키보드 포커스를 차단하지 않는다. ‘안 보임’은 조작 불가능과 같은 말이 아니다.

| 설정 | 자리 | 자신이 보임 | 일반적인 자신의 클릭·포커스 |
| --- | --- | --- | --- |
| display:none | 없음 | 안 보임 | 제외 |
| visibility:hidden | 유지 | 안 보임 | 제외 |
| opacity:0 | 유지 | 투명 | 이것만으로 차단하지 않음 |

표는 자식에서 visibility를 다시 바꾸는 등의 조건을 넣지 않은 기본 실험이다. display:none도 원본 HTML을 삭제하거나 주석으로 바꾸지는 않는다. 스타일을 바꾸면 다시 표시할 수 있다.

opacity를 부모에 적용하면 자식 글자도 함께 합성된다. 자식에 opacity:1을 주어 부모의 투명도를 취소하는 방식은 아니다. 배경색만 반투명하게 하려면 rgba의 알파를 비교한다. 이는 글자까지 함께 흐리는 것과 다른 목적이다.

> 📚 **출처 · 본문 설명 확인:** [MDN opacity](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/opacity), [visibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/visibility), [display](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/display). 설명과 비교 표는 수업 원본을 바탕으로 새로 풀어 썼다. 외부 원문을 직접 인용한 문장은 아니다. 확인일: 2026-10-28.

<a id="example"></a>

## 3. 작은 예제로 먼저 이해하기

**새 설명 예제 · 전체 파일.** [실행 파일](실습/책형_복습/05_CSS_투명도와_요소숨김.html)을 브라우저로 연다. 이 예제는 위 style 안에 CSS를 모두 넣어 외부 파일 연결이 필요 없다. 원본 CSS에 붙이면 다른 규칙이 섞일 수 있으므로 먼저 별도 파일로 확인한다.

```html
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>05. 투명도와 숨김 — 보임·자리·조작을 따로 묻기</title>
    <style>
        .hidden { visibility: hidden; }
        .none { display: none; }
        .transparent { opacity: 0; }
    </style>
</head>
<body>
    <h1>자리를 보며 비교</h1>
    <p>시작</p>
    <p class="hidden">hidden 문단</p>
    <p class="none">none 문단</p>
    <p class="transparent">투명 문단</p>
    <p>끝</p>
    <button type="button">첫 버튼</button>
    <button type="button" class="transparent">투명한 버튼</button>
    <button type="button">마지막 버튼</button>
</body>
</html>
```

중간 세 문단은 안 보이지만 none 문단만 배치에서 빠진다. hidden·투명 문단의 자리는 남아 끝 문단 위치에 영향을 준다. 첫 버튼에서 Tab 이동하면 투명한 버튼도 포커스를 받을 수 있다. 이 버튼에는 별도 이벤트가 없으므로 클릭 기능 실행을 관찰했다고 적지는 않는다. 포커스 가능 여부와 비즈니스 동작 실행은 별개다.

<a id="my-code"></a>

## 4. 내가 작성한 코드를 따라 읽기

아래는 **내 원본 발췌**다. 주석의 표현도 원문대로 두었다. 설명에서 교정한 내용을 원본에 이미 수정한 것처럼 읽지 않는다.

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_html/css/05_opacity.html` 8–22행

```css
            .hidden {
                visibility: hidden;
            }

            /* 자리까지 없어지기때문에 보통 display를 주로 씀 */
            .none {
                display: none;
            }

            /* 글씨,그림 모두 투명도를 민들 수 있음 */
            /* visibility:hidden과 opacity:0은 동일하게 자리는 있으나 투명하게 만듦 */
            .opacity {
                /* opacity: 0.3; */
                opacity: 0;
            }
```

**발췌 바로 풀이:** 실행 선언은 같다. 내 “동일하게 자리는 있으나 투명하게”라는 메모는 **화면과 자리**에 대한 관찰까지만 맞다. 클릭·포커스 동작까지 같다는 뜻으로 읽으면 안 된다.

내 원본은 문단에 세 속성을 적용했다. ‘동일하게 자리는 있으나 투명’이라는 주석은 visibility와 opacity의 화면·자리 관찰까지만 설명한다. 클릭·포커스까지 같다고 넓히면 틀린다. ‘보통 display를 씀’도 모든 숨김 목적의 정답이 아니라 자리를 없애려는 경우의 선택이다.

<a id="connections"></a>

## 5. 파일·요소·값이 연결되는 흐름

class→숨김 속성→박스 존재·그림 합성→주변 위치·조작 상태 순서로 나눠 본다. 원본 문단은 입력이나 버튼이 아니어서 포커스 차이를 직접 비교하기 어렵다. 작은 예제에서 이미 배운 button으로 대상을 바꾼 이유가 그것이다. 이 예제는 원본 출력이 아니라 설명용 재구성이다.

<a id="review"></a>

## 6. 잘한 점·아쉬운 점·개선 방향

**잘한 점:** 자리 유무를 비교한 메모는 초보자의 관찰 출발점으로 유익하다. **아쉬운 점:** ‘같음’의 범위가 화면인지 조작인지 빠져 있다. **개선 방향:** 숨길 목적을 먼저 적는다. 자리를 제거할 것인가, 자리만 유지할 것인가, 조작도 막을 것인가를 묻고 해당 기능을 선택한다.

제안은 원본을 수정한 결과가 아니다. **실제 오류**, **관찰을 위한 수업용 단순화**, **목적에 따라 가능한 선택**을 구별한다. 단지 짧게 쓰거나 최신 기능을 쓴다고 더 좋은 코드는 아니다.

<a id="teacher"></a>

## 7. 강사님 코드가 도움이 되는 비교



강사님과 내 활성 선언은 같아 원문을 중복 인용하지 않는다. 어느 쪽의 문단 실험도 실제 버튼 포커스까지 검증한 예제가 아니므로 그 결과를 원본에 있었다고 설명하지 않는다.

<a id="results"></a>

## 8. 결과를 예상하고 한 가지 바꾸기

아래는 **명시한 조건에서의 코드 기준 예상**이다. 이번 편집에서 실제 브라우저 렌더링을 재실행했다는 기록과 구별한다. 매 실험은 원래 예제로 돌아가 한 조건만 바꾼다.

| 한 가지 변경 | 예상 | 이유 |
| --- | --- | --- |
| hidden 문단만 visibility:visible | 같은 자리에 보임 | 자리는 원래 유지 |
| none 문단만 display:block | 문단이 배치에 복귀 | 박스 생성 |
| 투명 문단만 opacity:0.5 | 자리 유지·반투명 | 합성값 변경 |
| 투명 버튼만 display:none | 자리·일반 포커스 대상에서 제외 | 단순 투명과 다름 |

‘끝’이 당겨진 원인은 none 문단이다. opacity0 버튼이 남아 있는 자리를 클릭할 수 있다는 이유만으로 CSS가 실패한 것은 아니다. 투명도는 조작 차단 기능이 아니기 때문이다.

<a id="tips"></a>

## 9. 추가로 알면 좋은 것과 출처

> 💡 **TIP · 수업 범위 밖:** inert·aria-hidden·모달의 포커스 관리는 별도 HTML·접근성 학습이다. 이 세 속성을 안다고 전체 접근성 구현을 배웠다고 보지는 않는다.



이 절의 확장은 기본 문제의 필수 조건이 아니다. 2절의 📚 출처는 배운 기능의 설명을 확인하는 근거이며, 출처가 있다는 이유로 모두 수업 밖 내용인 것은 아니다.

<a id="practice"></a>

## 10. 복습과 빠른 정리

1. opacity0이면 자리가 없어지는가?
2. 부모 opacity0.5를 자식 opacity1로 취소할 수 있는가?
3. display:none은 HTML 삭제인가?

<details>
<summary>짧은 풀이 — 먼저 답한 뒤 확인</summary>

자리는 남는다. 자식 값으로 부모 전체 합성을 취소하지 못한다. display:none은 박스 표시 방식이며 HTML 소스 삭제가 아니다.

</details>

| 목적 | 비교 시작점 |
| --- | --- |
| 자리도 제거 | display:none |
| 자리 유지·숨김 | visibility:hidden |
| 전체 투명도 | opacity |
| 배경색만 알파 | rgba 등 색상값 |

[장별 연습문제](실습/연습문제/05_CSS_투명도와_요소숨김_연습문제.md)에서 예상·설명·수정을 이어 간다. 다음은 [배경](06_CSS_배경이미지와_배경속성.md)이다.

<!-- 이전 색인 이동 주소 보존 -->
<a id="css-12"></a>
<a id="css-21"></a>
<a id="css-24"></a>
<a id="css-28"></a>
<a id="css-30"></a>
<a id="css-6"></a>
<a id="css-9"></a>
<a id="section-1"></a>
<a id="section-2"></a>
<a id="section-3"></a>
<a id="section-4"></a>

이전 절 주소로 왔다면 [이 장의 목차](#chapter-toc)에서 현재 설명을 찾는다.
