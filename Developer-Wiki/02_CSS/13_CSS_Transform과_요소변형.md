# 13. transform — 자기 기준으로 보이는 모양 바꾸기

[CSS 목차](README.md) · [읽기 안내](00_CSS_V3_동작_백과_읽기법.md)

상자를 옮기거나 확대해도 주변 요소가 새 모양을 피해서 다시 배치되는 것은 아니다. transform은 원래 배치와 보이는 결과를 나누어 이해해야 한다.

<a id="chapter-toc"></a>

**이 장의 목차:** [목표](#learn) · [개념](#concepts) · [작은 예제](#example) · [내 코드](#my-code) · [연결](#connections) · [평가](#review) · [비교](#teacher) · [결과·실험](#results) · [TIP·출처](#tips) · [복습](#practice)

<a id="learn"></a>

## 1. 이 장에서 배울 것

translate·scale·scaleX·rotate를 구별한다. top·left의 부모 기준과 translate의 자기 기준으로 중앙 배치를 설명한다.

이번 장의 개념과 원본 기능은 수업 범위다. 원본에 없는 선택 기능은 9절 TIP으로 구분한다. 결과를 읽을 때는 선택된 요소·속성·기준값·실행 상태를 함께 적는다.

<a id="concepts"></a>

## 2. 무엇이며, 왜 필요한가

translate는 보이는 위치를 옮기고 scale은 크기를 확대·축소하며 rotate는 회전한다. 변형으로 커진 모양은 주변 요소와 겹칠 수 있다. 기존 일반 흐름이 새 크기만큼 자리를 다시 잡는다는 뜻은 아니다.

| 함수 | 이번 수업에서 읽는 값 |
| --- | --- |
| translate(20px,0) | 오른쪽 20px 이동 |
| translate(50%,50%) | 자기 기준 상자의 가로·세로 절반 이동 |
| scale(1.5) | 가로·세로 모두 1.5배 |
| scaleX(1.5) | 가로축만 1.5배 |
| rotate(-30deg) | 원본 기본 좌표에서 반시계 방향 30도 |

일반 HTML 상자의 translate %는 기본적으로 자신의 테두리까지 상자 크기와 연결된다. 내용 100px·양쪽 테두리 1px인 상자는 102px의 절반인 51px다. 반면 위치 배치의 left:50%는 부모 포함 블록의 너비 기준이다.

이 두 기준을 조합하면 중앙을 맞춘다. top·left:50%로 자식의 왼쪽 위를 부모 중앙에 놓고, translate(-50%,-50%)로 자식 크기의 절반을 되돌린다. 함수 목록의 순서를 바꾸면 합성 결과도 달라질 수 있으므로 순서를 무시한 독립 명령 모음으로 읽지 않는다.

> 📚 **출처 · 본문 설명 확인:** [W3C transforms](https://www.w3.org/TR/css-transforms-1/). 설명과 비교 표는 수업 원본을 바탕으로 새로 풀어 썼다. 외부 원문을 직접 인용한 문장은 아니다. 확인일: 2026-10-28.

<a id="example"></a>

## 3. 작은 예제로 먼저 이해하기

**새 설명 예제 · 전체 파일.** [실행 파일](실습/책형_복습/13_CSS_Transform과_요소변형.html)을 브라우저로 연다. 이 예제는 위 style 안에 CSS를 모두 넣어 외부 파일 연결이 필요 없다. 원본 CSS에 붙이면 다른 규칙이 섞일 수 있으므로 먼저 별도 파일로 확인한다.

```html
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>13. transform — 자기 기준으로 보이는 모양 바꾸기</title>
    <style>
        .parent { position: relative; width: 300px; height: 200px; border: 1px solid black; }
        .child { position: absolute; top: 50%; left: 50%; width: 100px; height: 50px; border: 1px solid blue; transform: translate(-50%, -50%); }
        .sample { width: 100px; border: 1px solid red; }
        .sample:hover { transform: scaleX(1.5); }
    </style>
</head>
<body>
    <h1>부모와 자기 기준</h1>
    <div class="parent"><div class="child">중앙</div></div>
    <p class="sample">가로 확대</p>
    <p>원래 배치 기준의 다음 문단</p>
</body>
</html>
```

parent는 300×200의 내용 영역이고 자식은 테두리까지 102×52px다. left 150·top 100에서 자신의 절반인 51·26px를 되돌려 99·74px 위치로 간다. 자식의 중심이 부모의 150·100px 지점에 맞는다. sample의 가로 확대는 주변 글 흐름을 새 너비에 맞게 재배치하는 기능이 아니다.

<a id="my-code"></a>

## 4. 내가 작성한 코드를 따라 읽기

아래는 **내 원본 발췌**다. 주석의 표현도 원문대로 두었다. 설명에서 교정한 내용을 원본에 이미 수정한 것처럼 읽지 않는다.

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_html/css/13_tranform.html` 35–38행

```css
            .total:hover {
                /* transform: rotate(30deg); */
                transform: translate(50%, 50%) scaleX(1.5) rotate(-30deg);
            }
```

**발췌 바로 풀이:** 강사님은 scale(1.5)로 가로·세로를 함께 키우고 나는 scaleX(1.5)로 가로만 키운다. **같은 결과가 아니다.** 두 축 확대를 원하면 강사님, 가로만 확대하려면 내 선언이 목적에 맞는다. 내 파일명은 원본 철자 그대로 `13_tranform.html`이다.

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_html/css/13_tranform.html` 48–59행

```css
            .parent .child {
                border: 1px solid blue;
                width: 30%;
                height: 30%;

                position: absolute;

                top: 50%;
                left: 50%;

                transform: translate(-50%, -50%);
            }
```

**발췌 바로 풀이:** 테두리 색 외에 배치 원리는 같다. 부모는 position:relative다. top·left의 50%는 부모 기준으로 자식의 왼쪽 위를 중앙까지 옮기고, translate의 -50%는 자식 자신의 크기 절반만큼 되돌린다. 그 결과 자식의 중심이 부모 중심과 맞는다.

내 total hover는 translate·scaleX·rotate를 합쳤다. 강사님은 scale을 사용했다. 가로만 확대하는 것과 두 축 확대는 같은 결과가 아니다. 두 번째 원본은 부모 relative와 자식 absolute를 연결하고, top·left 50%와 자기 절반 이동으로 중앙을 만든다. 내 테두리 blue와 강사님 blueviolet의 차이는 색이며 중앙 배치 원리는 같다.

<a id="connections"></a>

## 5. 파일·요소·값이 연결되는 흐름

부모의 position → 자식 top·left 기준 → 자식 border-box 크기 → translate의 음수 절반 순서로 추적한다. 앞 position 장의 calc는 자식 크기의 숫자를 직접 빼지만 이 방식은 자기 크기에 따라 되돌린다. 내 원본 파일명은 13_tranform.html, 강사님은 13_transform.html이므로 실제 철자를 확인한다.

<a id="review"></a>

## 6. 잘한 점·아쉬운 점·개선 방향

**잘한 점:** 여러 함수의 합성과 중앙 배치를 함께 실험했다. **설계 선택:** 가로만 늘리는 목적이면 내 scaleX가 맞다. 두 축 확대가 목적이면 강사님 scale이 맞다. **개선 방향:** translate·scale·rotate를 따로 확인한 뒤 결합하고, 원하는 최종 모양과 주변 겹침도 확인한다. 함수가 많다고 더 좋은 코드는 아니다.

제안은 원본을 수정한 결과가 아니다. **실제 오류**, **관찰을 위한 수업용 단순화**, **목적에 따라 가능한 선택**을 구별한다. 단지 짧게 쓰거나 최신 기능을 쓴다고 더 좋은 코드는 아니다.

<a id="teacher"></a>

## 7. 강사님 코드가 도움이 되는 비교

출처: `D:/workspace_teacher/workspace_html/css/13_transform.html` 31–33행

```css
        .total:hover {
            transform: translate(50%, 50%) scale(1.5) rotate(-30deg);
        }
```

위 강사님 발췌는 두 축 scale을 쓰므로 실제 차이를 판단하는 데 필요해 인용했다. 내 scaleX와 비교하여 세로 크기 변화를 설명한다. 중앙 코드는 원리가 같아 추가로 중복하지 않았다. 함수 순서를 바꾸는 경우 같은 결과라고 단정하지 않는다.

<a id="results"></a>

## 8. 결과를 예상하고 한 가지 바꾸기

아래는 **명시한 조건에서의 코드 기준 예상**이다. 이번 편집에서 실제 브라우저 렌더링을 재실행했다는 기록과 구별한다. 매 실험은 원래 예제로 돌아가 한 조건만 바꾼다.

| 한 가지 변경 | 예상 | 기준 |
| --- | --- | --- |
| child의 transform만 제거 | 왼쪽 위가 부모 중앙 | 자기 절반 보정 없음 |
| 원래 child의 width만 140px | 자기 절반 71px로 변경·중심 유지 | 자기 크기 기준 |
| 원래 sample의 scaleX만 scale로 | 세로도 확대 | 두 축 |
| 원래 parent의 width만 400px | 부모 중앙도 이동 | 포함 블록 기준 |

‘50%를 두 번 썼으니 상쇄되어 0’으로 계산하지 않는다. 각각 부모와 자기라는 다른 기준이다. margin이나 다른 변형 조건이 있는 복잡한 배치를 이 단순 예제와 같다고 판단하지 않는다.

<a id="tips"></a>

## 9. 추가로 알면 좋은 것과 출처

> 💡 **TIP · 수업 범위 밖:** 3D 변환·개별 translate/rotate/scale 속성·복잡한 모달 배치는 추가 학습이다. 기본 중앙 배치를 새 라이브러리로 교체하지 않아도 이해할 수 있다.



이 절의 확장은 기본 문제의 필수 조건이 아니다. 2절의 📚 출처는 배운 기능의 설명을 확인하는 근거이며, 출처가 있다는 이유로 모두 수업 밖 내용인 것은 아니다.

<a id="practice"></a>

## 10. 복습과 빠른 정리

1. left의 50%와 translate의 50%는 기준이 같은가?
2. scaleX는 세로도 1.5배인가?
3. transform 확대가 다음 요소를 자동으로 밀어내는가?

<details>
<summary>짧은 풀이 — 먼저 답한 뒤 확인</summary>

부모 포함 블록과 자기라는 서로 다른 기준이다. scaleX는 가로축이다. 변형된 그림 크기에 맞춰 일반 흐름이 재배치되는 것은 아니다.

</details>

| 개념 | 핵심 |
| --- | --- |
| translate | 보이는 위치 이동 |
| scale / scaleX | 두 축 / 가로축 |
| 중앙 | 부모 절반에서 자기 절반 되돌림 |
| 합성 | 함수 순서 확인 |

[장별 연습문제](실습/연습문제/13_CSS_Transform과_요소변형_연습문제.md)에서 예상·설명·수정을 이어 간다. 다음은 [미디어쿼리](14_CSS_미디어쿼리와_반응형.md)다.

<!-- 이전 색인 이동 주소 보존 -->
<a id="css-13"></a>
<a id="css-18"></a>
<a id="css-37"></a>
<a id="css-4"></a>
<a id="css-44"></a>
<a id="css-7"></a>
<a id="css-8"></a>
<a id="index-section-74"></a>
<a id="section-1"></a>
<a id="section-2"></a>
<a id="section-3"></a>

이전 절 주소로 왔다면 [이 장의 목차](#chapter-toc)에서 현재 설명을 찾는다.
