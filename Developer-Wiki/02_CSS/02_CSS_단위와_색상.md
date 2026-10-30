# 02. 단위와 색상 — 값의 기준을 먼저 찾기

[CSS 목차](README.md) · [읽기 안내](00_CSS_V3_동작_백과_읽기법.md)

150%라는 숫자만으로는 실제 크기를 알 수 없다. 어느 속성에 썼으며 무엇이 기준인지 알아야 한다. 이 장은 길이의 기준과 색의 표현을 계산으로 연결한다.

<a id="chapter-toc"></a>

**이 장의 목차:** [목표](#learn) · [개념](#concepts) · [작은 예제](#example) · [내 코드](#my-code) · [연결](#connections) · [평가](#review) · [비교](#teacher) · [결과·실험](#results) · [TIP·출처](#tips) · [복습](#practice)

<a id="learn"></a>

## 1. 이 장에서 배울 것

font-size의 em·rem·%를 계산한다. 뷰포트 단위와 색상 축약·알파를 읽고, 다른 속성에서도 같은 기준이라고 일반화하지 않는다.

이번 장의 개념과 원본 기능은 수업 범위다. 원본에 없는 선택 기능은 9절 TIP으로 구분한다. 결과를 읽을 때는 선택된 요소·속성·기준값·실행 상태를 함께 적는다.

<a id="concepts"></a>

## 2. 무엇이며, 왜 필요한가

px는 CSS 픽셀 단위다. 화면의 물리 픽셀 한 개와 언제나 일치한다는 뜻은 아니다. font-size의 %·em은 부모 글자 크기를 기준으로 하고 rem은 루트 html의 글자 크기를 기준으로 한다. 부모 20px에 1.5em을 준 자식은 30px, 그 자식 안에서 다시 1.5em을 쓰면 45px다. 같은 1.5라는 숫자여도 기준이 단계마다 바뀐다.

| 값 | 기준 | 계산 예 |
| --- | --- | --- |
| font-size:150% | 부모 글자 크기 | 부모 20 → 30px |
| font-size:1.5em | 부모 글자 크기 | 부모 20 → 30px |
| font-size:1.5rem | 루트 글자 크기 | html 16 → 24px |
| 50vw / 50vh | 뷰포트 너비 / 높이 | 1000×600이면 500 / 300px |
| 90vmin / 90vmax | 두 축 중 작은 / 큰 길이 | 위 조건에서 540 / 900px |

em을 다른 속성에 쓰면 보통 자신의 글자 크기를 기준으로 하므로, %와 모든 상황에서 같다고 외우지 않는다. 높이의 %도 부모 높이가 정해진 방식이 중요하다.

색은 red 같은 이름, rgb의 채널값, 16진수 등으로 표현한다. #00ff00은 #0f0로 줄일 수 있지만 #123456을 #135로 바꿀 수는 없다. 축약은 **각 두 자리 쌍이 같은 경우**다. rgba의 마지막 값은 해당 색의 알파다. 부모 요소 전체를 합성하는 opacity와 구분한다.

> 📚 **출처 · 본문 설명 확인:** [W3C 값과 단위](https://www.w3.org/TR/css-values-4/) 및 [CSS 색상](https://www.w3.org/TR/css-color-4/). 설명과 비교 표는 수업 원본을 바탕으로 새로 풀어 썼다. 외부 원문을 직접 인용한 문장은 아니다. 확인일: 2026-10-28.

<a id="example"></a>

## 3. 작은 예제로 먼저 이해하기

**새 설명 예제 · 전체 파일.** [실행 파일](실습/책형_복습/02_CSS_단위와_색상.html)을 브라우저로 연다. 이 예제는 위 style 안에 CSS를 모두 넣어 외부 파일 연결이 필요 없다. 원본 CSS에 붙이면 다른 규칙이 섞일 수 있으므로 먼저 별도 파일로 확인한다.

```html
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>02. 단위와 색상 — 값의 기준을 먼저 찾기</title>
    <style>
        html { font-size: 16px; }
        .base { font-size: 20px; }
        .em { font-size: 1.5em; }
        .rem { font-size: 1.5rem; }
        .sample { color: #0f0; background-color: rgb(0, 0, 0); }
    </style>
</head>
<body>
    <h1>기준을 따라 계산</h1>
    <div class="base">20px
        <div class="em">30px <span class="em">45px</span></div>
        <div class="rem">24px <span class="rem">24px</span></div>
    </div>
    <p class="sample">초록 글자</p>
</body>
</html>
```

루트를 16px, 부모를 20px로 직접 지정해 기본 설정에 의존하지 않도록 했다. em은 20 → 30 → 45로 커지고 rem은 중첩해도 24px다. sample은 검정 바탕의 초록 글자다. 숫자는 각 요소가 상속·직접 지정으로 계산한 font-size이며 픽셀 단위로 재본 글자 그림 높이와는 다르다.

<a id="my-code"></a>

## 4. 내가 작성한 코드를 따라 읽기

아래는 **내 원본 발췌**다. 주석의 표현도 원문대로 두었다. 설명에서 교정한 내용을 원본에 이미 수정한 것처럼 읽지 않는다.

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_html/css/02_단위.html` 52–76행

```css
            /* em은 %와 같이 상대적인 크기이고 보통 글씨 단위에 쓰며, 퍼센트와 같음 */
            #em .box1 {
                font-size: 1.5em;
            }

            #em .box1 .box2 {
                font-size: 1.5em;
            }

            #em .box1 .box2 .box3 {
                font-size: 1.5em;
            }

            /* root em의 약자로 body의 크기를 활용한다(최상단의 크기 또는 기본값) */
            #rem .box1 {
                font-size: 1.5rem;
            }

            #rem .box1 .box2 {
                font-size: 1.5rem;
            }

            #rem .box1 .box2 .box3 {
                font-size: 1.5rem;
            }
```

**발췌 바로 풀이:** 내 코드는 em 3단계와 rem 3단계를 별도 구역으로 나누어 비교한다. **같은 단위를 반복했을 때의 차이**를 복습하기에는 이 구성이 더 명확하다. 다만 양쪽 주석의 “rem은 body 기준”은 **루트 요소인 html의 글자 크기 기준**으로 교정한다.

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_html/css/02_단위.html` 13–20행

```css
                /* background컬러는 상속은 안되지만, 나머지가 투명하기에 모두 붉게 보이는 것 */
                background-color: rgb(255, 0, 0);
                
                /* 2개씩 코드가 반복 될 때에는 한글자로 줄여서 쓸 수 있음 */
                /* color: #F0EEE9;
                color: #00ff00; */
                color: #0f0;
            }
```

**발췌 바로 풀이:** 내 `#0f0`는 `#00ff00`이므로 강사님과 다른 초록색이다. 축약하려면 **각 자리 쌍**이 반복되어야 한다. `#123456`을 `#135`로 줄일 수는 없다.

내 코드는 em 세 단계와 rem 세 단계를 구역별로 나눴다. 첫 주석의 ‘퍼센트와 같음’은 font-size 조건에서 이해하고 모든 속성으로 넓히지 않는다. rem의 ‘body 기준’ 메모는 루트 html 기준으로 교정한다. 내 #0f0는 강사님 #0fa와 다른 색이다. 전자는 #00ff00, 후자는 #00ffaa다. 배경이 투명해서 부모 색이 보인다는 내 주석은 상속과 표시를 구분하는 데 도움이 된다.

<a id="connections"></a>

## 5. 파일·요소·값이 연결되는 흐름

부모의 계산된 글자 크기 → 자식의 em·% 계산, html의 글자 크기 → 각 rem 계산으로 화살표를 그린다. 내 원본 em·rem HTML은 각각 닫는 div가 부족해 구역 경계가 의도와 어긋날 수 있다. 화면이 나오는 것만으로 올바른 중첩이라고 보지 말고, 먼저 시작·끝 태그를 맞춘다. 위 전체 예제는 각 구역을 완전히 닫았다.

<a id="review"></a>

## 6. 잘한 점·아쉬운 점·개선 방향

**잘한 점:** em과 rem을 별도 구역으로 반복해 중첩 효과를 비교하기 쉽다. **아쉬운 점:** rem 기준 주석과 누락된 닫는 태그는 교정이 필요하다. **개선 방향:** 루트·부모 기준값을 먼저 적고, 결과 표와 HTML 중첩을 함께 맞춘다. 브라우저 기본값이 언제나 16px라는 가정은 피한다.

제안은 원본을 수정한 결과가 아니다. **실제 오류**, **관찰을 위한 수업용 단순화**, **목적에 따라 가능한 선택**을 구별한다. 단지 짧게 쓰거나 최신 기능을 쓴다고 더 좋은 코드는 아니다.

<a id="teacher"></a>

## 7. 강사님 코드가 도움이 되는 비교

출처: `D:/workspace_teacher/workspace_html/css/02_단위.html` 49–58행

```css
        #em .box1 {
            font-size: 1.5em;
        }
        #em .box1 .box2 {
            font-size: 1.5em;
        }
        /* rem : root em, body의 크기를 활용한다 */
        #em .box1 .box2 .box3 {
            font-size: 1.5rem;
        }
```

강사님은 em 구역의 세 번째 단계만 rem으로 바꿨다. 부모·루트가 모두 16px라는 별도 조건이면 24 → 36 → 24px다. 내 구역의 전부 em은 24 → 36 → 54px, 전부 rem은 24 → 24 → 24px다. 마지막 값만 바꾼 강사님 실험은 기준 전환을, 구역을 나눈 내 실험은 같은 단위 반복을 비교하기 좋다. 양쪽의 body 기준 주석은 동일하게 교정한다.

<a id="results"></a>

## 8. 결과를 예상하고 한 가지 바꾸기

아래는 **명시한 조건에서의 코드 기준 예상**이다. 이번 편집에서 실제 브라우저 렌더링을 재실행했다는 기록과 구별한다. 매 실험은 원래 예제로 돌아가 한 조건만 바꾼다.

| 한 가지 변경 | 예상 | 이유 |
| --- | --- | --- |
| 새 예제 html만 20px | rem 둘 다 30px | 루트 변경 |
| 원래 예제 base만 30px | em 45·67.5px, rem 24px | 부모 기준만 변경 |
| #0f0만 #0fa로 | 글자 색 달라짐 | 축약 채널값 자체가 다름 |

값이 예상과 다르면 기준값·선택자·실제 중첩을 먼저 확인한다. 원본 #v1의 100vh, #v2의 50vw, #v3·#v4의 90vmin·90vmax는 뷰포트 단위 실험이다. #00ff00a0의 뒤 a0는 16진수 160/255, 약 0.627 알파다. 배경과 합성된 화면 색을 원래 채널값과 혼동하지 않는다.

<a id="tips"></a>

## 9. 추가로 알면 좋은 것과 출처

> 💡 **TIP · 수업 범위 밖:** ch·lh·svh·dvh·clamp와 다크 모드 전체 설계는 선택 학습이다. 수업에 실제 있는 vmin·vmax·calc·CSS 변수 사용까지 미학습으로 빼지는 않는다.

이하의 내용은 **수업 원본에서 확인된 필수 진도가 아닌 추가 학습**이다. 위의 기본 설명을 이해한 뒤 필요할 때 읽는다.

<a id="extra-02-2"></a>

### 2. 크기·방향·색의 확장

| 기능 | 역할과 주의 |
| --- | --- |
| ch·lh | 글꼴의 문자 폭·줄 높이와 연결되는 길이. 항상 한 글자의 실제 폭과 같다고 단정하지 않음 |
| svh·lvh·dvh | 브라우저 UI 변화에 따른 뷰포트 높이 기준을 나누어 검토 |
| clamp | 최소·선호·최대 값을 함께 제한 |
| margin-inline·padding-block 등 | 물리적 좌우·상하 대신 쓰기 방향의 축으로 표현 |
| 색상 토큰·다크 모드 | 배경·글자·경계·상태 색을 함께 설계 |

```css
/* 추가 예제: 최소 1rem, 선호 2vw, 최대 1.5rem */
.fluid-text { font-size: clamp(1rem, 2vw, 1.5rem); }
```

수업의 calc·vmin/vmax·CSS 변수는 [단위](02_CSS_단위와_색상.md)와 [position](08_CSS_Position과_요소위치.md)에 있다. 변수를 사용했다고 디자인 토큰·다크 모드 전체를 배운 것은 아니다. [단위 표준](https://www.w3.org/TR/css-values-4/)

이 절의 확장은 기본 문제의 필수 조건이 아니다. 2절의 📚 출처는 배운 기능의 설명을 확인하는 근거이며, 출처가 있다는 이유로 모두 수업 밖 내용인 것은 아니다.

<a id="practice"></a>

## 10. 복습과 빠른 정리

1. 루트 20px·부모 30px일 때 font-size 1.5em과 1.5rem은?
2. #aabbcc는 축약 가능한가?
3. CSS 픽셀은 항상 물리 픽셀 하나인가?

<details>
<summary>짧은 풀이 — 먼저 답한 뒤 확인</summary>

각각 45px와 30px다. #aabbcc는 #abc로 축약한다. CSS 픽셀과 장치 픽셀의 대응은 화면·확대 등의 조건에 따라 다르다.

</details>

| 기준 | 단위 |
| --- | --- |
| 부모 글자 크기 | font-size의 em·% |
| 루트 글자 크기 | rem |
| 뷰포트 축 | vw·vh·vmin·vmax |
| 색의 알파 | rgba·8자리 16진수 |

[장별 연습문제](실습/연습문제/02_CSS_단위와_색상_연습문제.md)에서 예상·설명·수정을 이어 간다. 다음은 [박스 모델](03_CSS_박스모델.md)이다.

<!-- 이전 색인 이동 주소 보존 -->
<a id="css-12"></a>
<a id="css-16"></a>
<a id="css-22"></a>
<a id="css-23"></a>
<a id="css-24"></a>
<a id="css-26"></a>
<a id="css-27"></a>
<a id="css-31"></a>
<a id="css-32"></a>
<a id="css-34"></a>
<a id="css-35"></a>
<a id="css-47"></a>
<a id="css-48"></a>
<a id="css-49"></a>
<a id="css-51"></a>
<a id="css-67"></a>
<a id="css-7"></a>
<a id="index-section-71"></a>
<a id="index-section-72"></a>
<a id="index-section-73"></a>
<a id="index-section-74"></a>
<a id="index-section-87"></a>
<a id="index-section-89"></a>
<a id="section-1"></a>
<a id="section-2"></a>
<a id="section-3"></a>
<a id="section-4"></a>

이전 절 주소로 왔다면 [이 장의 목차](#chapter-toc)에서 현재 설명을 찾는다.
