# 11. 그림자 — 이동·흐림·실제 상자 크기

[CSS 목차](README.md) · [읽기 안내](00_CSS_V3_동작_백과_읽기법.md)

그림자는 글자나 상자 주변에 덧그리는 시각 효과다. 어느 방향으로 얼마나 떨어뜨리고 얼마나 흐리게 하는지를 나누면 긴 선언도 읽기 쉽다.

<a id="chapter-toc"></a>

**이 장의 목차:** [목표](#learn) · [개념](#concepts) · [작은 예제](#example) · [내 코드](#my-code) · [연결](#connections) · [평가](#review) · [비교](#teacher) · [결과·실험](#results) · [TIP·출처](#tips) · [복습](#practice)

<a id="learn"></a>

## 1. 이 장에서 배울 것

text-shadow·box-shadow의 이동값과 blur를 구별한다. 그림자가 그려지는 범위와 레이아웃 크기, 포인터 모양과 기능을 분리한다.

이번 장의 개념과 원본 기능은 수업 범위다. 원본에 없는 선택 기능은 9절 TIP으로 구분한다. 결과를 읽을 때는 선택된 요소·속성·기준값·실행 상태를 함께 적는다.

<a id="concepts"></a>

## 2. 무엇이며, 왜 필요한가

text-shadow:2px 3px 4px red는 오른쪽2px·아래3px에 흐림 반경4px인 빨간 글자 그림자다. blur는 길이이며 opacity의0~1 투명도와 다르다. 본문 글자 색을 white로 주어도 빨간 그림자를 따로 그릴 수 있다.

box-shadow는 글자 윤곽이 아니라 상자에 그림자를 준다. 그림자가 바깥으로 그려진다고 width가 늘거나 다음 요소가 밀리는 것은 아니다. ‘보이는 범위’와 ‘배치 크기’를 나눠야 한다.

| 값 | 역할 | 바뀌지 않는 것 |
| --- | --- | --- |
| 첫 길이 | x방향 이동 | 요소의left값 |
| 둘째 길이 | y방향 이동 | 요소의top값 |
| 셋째 길이 | 흐림 반경 | opacity값 |
| 색 | 그림자 색 | 본문color는별도 |

hover는 상태 조건이다. cursor:pointer는 포인터 모양을 바꾸며 버튼의 역할이나 클릭 동작을 새로 만들지 않는다.

> 📚 **출처 · 본문 설명 확인:** [W3C 상자 그림자](https://www.w3.org/TR/css-backgrounds-3/#box-shadow). 설명과 비교 표는 수업 원본을 바탕으로 새로 풀어 썼다. 외부 원문을 직접 인용한 문장은 아니다. 확인일: 2026-10-28.

<a id="example"></a>

## 3. 작은 예제로 먼저 이해하기

**새 설명 예제 · 전체 파일.** [실행 파일](실습/책형_복습/11_CSS_그림자와_시각효과.html)을 브라우저로 연다. 이 예제는 위 style 안에 CSS를 모두 넣어 외부 파일 연결이 필요 없다. 원본 CSS에 붙이면 다른 규칙이 섞일 수 있으므로 먼저 별도 파일로 확인한다.

```html
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>11. 그림자 — 이동·흐림·실제 상자 크기</title>
    <style>
        .text { text-shadow: 2px 3px 4px red; }
        .box { width: 150px; height: 80px; border: 1px solid black; }
        .box:hover { box-shadow: 4px 4px 6px gray; cursor: pointer; }
    </style>
</head>
<body>
    <h1>그려지는 범위</h1>
    <p class="text">글자 그림자</p>
    <div class="box">상자에 포인터 올리기</div>
    <p>다음 문단</p>
</body>
</html>
```

text는 글자 주변에 빨간 그림자를 만든다. box는 포인터를 올릴 때만 회색 그림자가 나타난다. box 내용 너비150·테두리2=152px라는 계산은 그림자 전후에 그대로다. 그림자 크기만큼 다음 문단이 밀리는 배치는 아니다. 클릭 기능은 구현하지 않았다.

<a id="my-code"></a>

## 4. 내가 작성한 코드를 따라 읽기

아래는 **내 원본 발췌**다. 주석의 표현도 원문대로 두었다. 설명에서 교정한 내용을 원본에 이미 수정한 것처럼 읽지 않는다.

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_html/css/11_shadow.html` 8–17행

```css
            .red {
                /* offset-x, offset-y (떨어져있는 거리)만큼 띄워라 */
                text-shadow: 10px 3px red;
            }
            .blur {
                /* offset-x, offset-y (떨어져있는 거리)만큼 띄우고 blur투명도처리 */
                text-shadow: 2px 2px 4px red;
                color: white;
                font-size: 2em;
            }
```

**발췌 바로 풀이:** 선언은 같다. 내 주석의 “blur투명도처리”는 **흐림 반경**으로 고쳐 이해한다. opacity의 0~1 값과 달리 여기서는 px 길이다.

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_html/css/11_shadow.html` 24–35행

```css
            .box2 {
                border: 1px solid black;
                width: 150px;
                height: 200px;
                margin: 10px;
            }

            .box2:hover {
                box-shadow: 4px 4px 6px gray;

                cursor: pointer;
            }
```

**발췌 바로 풀이:** grey와 gray는 같은 색 이름이다. 포인터를 올리면 오른쪽·아래 4px, 흐림 6px의 그림자가 생긴다. 상자의 width·height가 그림자 크기만큼 늘어나거나 다음 요소를 밀어내지는 않는다.

내 .red는10px 3px red라 오른쪽10·아래3 그림자다. .blur는2px 2px 4px red에 실제 글자 white·2em을 따로 지정했다. ‘blur투명도처리’ 메모는 흐림 반경으로 교정한다. .box2의 hover 그림자는4·4·6px이며 gray와 강사님의 grey는 같은 색 이름이다.

<a id="connections"></a>

## 5. 파일·요소·값이 연결되는 흐름

요소의 class → text 또는 box 그림자 규칙 → 기본·hover 상태 → 그림 합성 순서다. 크기를 계산하는 width·padding·border에는 그림자의 흐림 길이를 넣지 않는다. 그림자가 주변 요소와 겹쳐 보이면 배치 이동과 구분해 확인한다.

<a id="review"></a>

## 6. 잘한 점·아쉬운 점·개선 방향

**잘한 점:** offset의 떨어진 거리를 주석으로 풀었다. **아쉬운 점:** 흐림과 투명도를 같은 말로 쓴 부분은 바꿔 기억한다. **개선 방향:** 인터랙션이 필요한 실제 화면이라면 역할에 맞는 HTML과 동작이 있어야 한다. 원본은 hover 시각 실험이므로 cursor:pointer만으로 완성 버튼이라고 평가하지 않는다.

제안은 원본을 수정한 결과가 아니다. **실제 오류**, **관찰을 위한 수업용 단순화**, **목적에 따라 가능한 선택**을 구별한다. 단지 짧게 쓰거나 최신 기능을 쓴다고 더 좋은 코드는 아니다.

<a id="teacher"></a>

## 7. 강사님 코드가 도움이 되는 비교



활성 선언은 같고 grey·gray도 동의 색상이라 중복 인용하지 않는다. 세 길이를 쓴 원본을 네 번째 spread까지 실험한 증거로 삼지 않는다.

<a id="results"></a>

## 8. 결과를 예상하고 한 가지 바꾸기

아래는 **명시한 조건에서의 코드 기준 예상**이다. 이번 편집에서 실제 브라우저 렌더링을 재실행했다는 기록과 구별한다. 매 실험은 원래 예제로 돌아가 한 조건만 바꾼다.

| 한 가지 변경 | 예상 | 구별 |
| --- | --- | --- |
| blur4만0px | 더선명한그림자 | 투명도아님 |
| x2만-2px | 왼쪽으로이동 | 본문글자위치유지 |
| box blur6만12px | 흐림범위변화 | width150유지 |
| cursor만제거 | 기본포인터로돌아감 | 클릭기능변화아님 |

그림자 색과 글자 color를 혼동하면 글자가 왜 하얀지 설명하지 못한다. 먼저 본문 color, 그다음 shadow 색을 별도 선언으로 읽는다.

<a id="tips"></a>

## 9. 추가로 알면 좋은 것과 출처

> 💡 **TIP · 수업 범위 밖:** spread·inset·다중 그림자와 그림자 토큰 체계는 원본 실행 예제 밖의 추가 학습이다. 아래 확장 표에서 구별한다.

이하의 내용은 **수업 원본에서 확인된 필수 진도가 아닌 추가 학습**이다. 위의 기본 설명을 이해한 뒤 필요할 때 읽는다.

<a id="extra-02-3"></a>

### 3. 배경·그림자·움직임 확장

```css
/* 추가 예제: x, y, blur, spread, 색 */
.raised { box-shadow: 0 4px 8px 2px #0003; }
```

여기서 2px는 spread다. 기본편의 원본은 세 길이만 있어 spread를 직접 실험한 코드로 보지 않았다. spread는 그림자 범위를 확장·축소하는 값이고 blur는 흐림이다. 둘은 다르다. [그림자 표준](https://www.w3.org/TR/css-backgrounds-3/#box-shadow)

| 기존 확장 주제 | 분리해 학습할 내용 |
| --- | --- |
| 다중 배경·gradient·origin/clip | 여러 층의 순서, 배경을 계산하고 칠하는 영역 |
| inset·다중 그림자 | 안쪽 그림자와 여러 그림자의 합성 |
| 3D 변환·개별 transform 속성 | 좌표·순서·기준의 추가 규칙 |
| transition delay·timing function | 전환 시작 지연과 진행 속도 |
| will-change·이벤트 | 성능 힌트와 JavaScript 동작. 무조건 붙이는 최적화가 아님 |
| prefers-reduced-motion | 사용자의 움직임 감소 선호를 반영하는 조건 |
| overflow:clip·overscroll-behavior | 잘림·스크롤 연결의 추가 제어 |

<a id="extra-02-5"></a>

### 선택 복습

새 함수를 많이 쓰면 기존 속성보다 항상 좋은 코드가 될까?

<details>
<summary>해설</summary>

아니다. 필요한 동작과 기준을 설명할 수 있어야 한다. 새 기능은 해결할 문제가 있을 때 하나씩 추가하고 결과를 비교한다.

</details>

이 절의 확장은 기본 문제의 필수 조건이 아니다. 2절의 📚 출처는 배운 기능의 설명을 확인하는 근거이며, 출처가 있다는 이유로 모두 수업 밖 내용인 것은 아니다.

<a id="practice"></a>

## 10. 복습과 빠른 정리

1. blur는0~1의 투명도값인가?
2. 그림자가 커지면 width도커지는가?
3. pointer를주면 클릭기능이생기는가?

<details>
<summary>짧은 풀이 — 먼저 답한 뒤 확인</summary>

blur는 이 예제에서 px길이다. 그림자는 원래 레이아웃 width를 늘리지 않는다. cursor는 포인터 모양이며 클릭기능을 만들지 않는다.

</details>

| 구분 | 읽을속성 |
| --- | --- |
| 글자그림자 | text-shadow |
| 상자그림자 | box-shadow |
| 흐림 | 셋째길이 |
| 조작기능 | 별도HTML·동작 |

[장별 연습문제](실습/연습문제/11_CSS_그림자와_시각효과_연습문제.md)에서 예상·설명·수정을 이어 간다. 다음은 [전환](12_CSS_Transition과_상태변화.md)이다.

<!-- 이전 색인 이동 주소 보존 -->
<a id="css-24"></a>
<a id="css-28"></a>
<a id="index-section-74"></a>
<a id="section-1"></a>
<a id="section-2"></a>
<a id="section-3"></a>

이전 절 주소로 왔다면 [이 장의 목차](#chapter-toc)에서 현재 설명을 찾는다.
