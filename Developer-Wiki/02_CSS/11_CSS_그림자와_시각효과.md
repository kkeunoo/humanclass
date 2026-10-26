# 11. 그림자 — 이동 거리와 흐림을 나누어 읽기

[CSS 목차](README.md)

<!-- chapter-toc -->

- [1. 글자 그림자](11_CSS_그림자와_시각효과.md#section-1)
- [2. 상자 그림자와 hover](11_CSS_그림자와_시각효과.md#section-2)
- [복습](11_CSS_그림자와_시각효과.md#section-3)

<a id="section-1"></a>

## 1. 글자 그림자

### 강사님 코드

`11_shadow.html` 8~17행 — **원본 발췌**

```css
        .red {
            /* offset-x offset-y color */
            text-shadow: 10px 3px red;
        }
        .blur {
            /* offset-x offset-y blur-radius color */
            text-shadow: 2px 2px 4px red;
            color: white;
            font-size: 2em;
        }
```

첫 그림자는 오른쪽 10px·아래 3px에 빨강으로 표시한다. 두 번째는 오른쪽·아래 2px에 흐림 반경 4px를 더했다. 실제 글자 색은 white이고 빨간 것은 그림자다.

### 내 코드

`11_shadow.html` 8~17행 — **원본 발췌**

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

선언은 같다. 내 주석의 “blur투명도처리”는 **흐림 반경**으로 고쳐 이해한다. opacity의 0~1 값과 달리 여기서는 px 길이다.

<a id="section-2"></a>

## 2. 상자 그림자와 hover

### 강사님 코드

`11_shadow.html` 26~36행 — **원본 발췌**

```css
        .box2 {
            border: 1px solid black;
            width: 150px;
            height: 200px;
            margin: 10px;
        }
        .box2:hover {
            box-shadow: 4px 4px 6px grey;

            cursor: pointer;
        }
```

### 내 코드

`11_shadow.html` 24~35행 — **원본 발췌**

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

grey와 gray는 같은 색 이름이다. 포인터를 올리면 오른쪽·아래 4px, 흐림 6px의 그림자가 생긴다. 상자의 width·height가 그림자 크기만큼 늘어나거나 다음 요소를 밀어내지는 않는다.

cursor:pointer는 포인터 모양을 바꾼다. 클릭 기능이나 HTML button의 역할을 자동으로 만들지는 않는다. 원본은 hover 시각 효과 실험이다. [상자 그림자 표준](https://www.w3.org/TR/css-backgrounds-3/#box-shadow)

<a id="section-3"></a>

## 복습

box-shadow의 6px를 12px로 바꾸면 상자 width 150px가 162px가 될까?

<details>
<summary>해설</summary>

아니다. 흐림이 달라질 뿐 width 선언의 값은 그대로다. 그림자가 그려지는 영역과 레이아웃 박스 크기를 구분한다.

</details>

**추가로 알면 좋은 것:** 네 번째 길이인 spread, inset·다중 그림자, 그림자 토큰 체계는 비교 원본의 실행 예제에 없어 추가편으로 구분한다. 초기 분류안의 spread 본문 포함 판단은 실제 코드 대조 후 수정했다.

<!-- legacy-migration -->

<a id="css-28"></a>
<a id="index-section-74"></a>
<a id="css-24"></a>

### 이전 색인 링크 안내

이전 절 주소를 보존한 이동 안내다. 옛 절 번호와 현재 절은 같지 않다. [현재 CSS 목차](README.md)에서 수업 본문과 **추가로 알면 좋은 것**을 구분해 찾는다.

<!-- inlined-extra-2026 -->

**이 장을 읽은 뒤:** [장별 연습문제 풀기](실습/연습문제/11_CSS_그림자와_시각효과_연습문제.md)

## 추가로 알면 좋은 것

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
