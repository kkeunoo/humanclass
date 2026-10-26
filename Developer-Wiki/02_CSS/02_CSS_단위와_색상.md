# 02. 단위와 색상 — 숫자의 기준을 먼저 찾기

[CSS 목차](README.md)

`150%`만 읽어서는 실제 크기를 알 수 없다. 어떤 속성에 썼는지, 무엇을 기준으로 계산하는지 함께 읽어야 한다.

<!-- chapter-toc -->

- [1. em과 rem을 비교한 원본](#section-1)
- [2. 수업 단위의 기준표](#section-2)
- [3. 색과 투명도](#section-3)
- [복습](#section-4)

<a id="section-1"></a>

## 1. em과 rem을 비교한 원본

### 강사님 코드

`02_단위.html` 49~58행 — **원본 발췌**

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

첫째와 둘째는 부모 글자 크기의 1.5배다. 셋째만 rem으로 바꿔 부모를 따라 계속 커지는 것과 루트 기준으로 고정되는 것을 비교했다.

### 내 코드

`02_단위.html` 52~76행 — **원본 발췌**

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

내 코드는 em 3단계와 rem 3단계를 별도 구역으로 나누어 비교한다. **같은 단위를 반복했을 때의 차이**를 복습하기에는 이 구성이 더 명확하다. 다만 양쪽 주석의 “rem은 body 기준”은 **루트 요소인 html의 글자 크기 기준**으로 교정한다.

부모·루트 글자 크기가 16px라고 가정하면 다음과 같다. 브라우저 기본 글자 크기가 언제나 16px라고 가정하지 말고 실제 설정을 확인한다.

| 원본 실험 | box1 | box2 | box3 |
| --- | --- | --- | --- |
| 양쪽 percent: 모두 150% | 24px | 36px | 54px |
| 강사님 em 구역: 마지막 rem | 24px | 36px | 24px |
| 내 em 구역: 모두 em | 24px | 36px | 54px |
| 내 rem 구역: 모두 rem | 24px | 24px | 24px |

내 HTML의 em·rem 구역에는 각각 닫는 div가 하나씩 부족하다. 브라우저가 보정하여 보여 주는 화면을 올바른 중첩의 증거로 삼지 않는다. 다음과 같이 각 구역을 완전히 닫는다.

```html
<!-- 구조 교정 예시: 원본 발췌 아님. 두 구역에 각각 적용 -->
<div id="em">
    <div class="box1">box1
        <div class="box2">box2
            <div class="box3">box3</div>
        </div>
    </div>
</div>
```

<a id="section-2"></a>

## 2. 수업 단위의 기준표

| 단위 | 기준·주의 |
| --- | --- |
| px | CSS 픽셀. 물리적인 화면 픽셀 하나와 항상 같지 않음 |
| % | 속성에 따라 기준이 다름. font-size에서는 부모 글자 크기 |
| em | font-size에서는 부모 글자 크기, 다른 속성에서는 보통 자신의 글자 크기 |
| rem | 루트 요소의 글자 크기 |
| vw / vh | 뷰포트 너비 / 높이의 1% |
| vmin / vmax | 뷰포트 너비·높이 중 작은 값 / 큰 값의 1% |

양쪽 `#v1`은 `height:100vh`, `#v2`는 `width:50vw`, `#v3`·`#v4`는 높이에 `90vmin`·`90vmax`를 쓴다. vmin·vmax도 실제 원본에 있으므로 본문 범위다. `%`와 `em`을 모든 속성에서 같은 단위라고 외우지 않는다. 높이의 `%`는 부모의 높이가 어떻게 정해졌는지에 따라 달라지며 “내 콘텐츠의 몇 %”라는 뜻으로 일반화하지 않는다. [CSS 단위 표준](https://www.w3.org/TR/css-values-4/)

<a id="section-3"></a>

## 3. 색과 투명도

### 강사님 코드

`02_단위.html` 16~21행 — **원본 발췌**

```css
            background-color: rgb(255,0,0);

            /* color : #F0EEE9; */
            color : #00ffaa;
            color : #0fa;
        }
```

`#00ffaa`와 `#0fa`는 같은 색이다. 뒤의 선언이 최종 적용되어도 색이 달라지지 않는다.

### 내 코드

`02_단위.html` 13~20행 — **원본 발췌**

```css
                /* background컬러는 상속은 안되지만, 나머지가 투명하기에 모두 붉게 보이는 것 */
                background-color: rgb(255, 0, 0);
                
                /* 2개씩 코드가 반복 될 때에는 한글자로 줄여서 쓸 수 있음 */
                /* color: #F0EEE9;
                color: #00ff00; */
                color: #0f0;
            }
```

내 `#0f0`는 `#00ff00`이므로 강사님과 다른 초록색이다. 축약하려면 **각 자리 쌍**이 반복되어야 한다. `#123456`을 `#135`로 줄일 수는 없다.

양쪽 box2의 `rgba(0,0,255,0.4)`는 파랑 배경색의 알파가 0.4라는 뜻이다. box3의 `#00ff00a0`는 뒤의 `a0`가 알파이며 약 0.627이다. 부모 배경과 겹치면 합성된 색으로 보인다. 배경색의 알파와 요소 전체의 `opacity`는 구별한다. [투명도와 숨김](05_CSS_투명도와_요소숨김.md)

<a id="section-4"></a>

## 복습

루트가 20px, 부모가 30px일 때 자식의 `font-size:1.5em`과 `1.5rem`은?

<details>
<summary>해설</summary>

각각 45px와 30px다. em은 여기서 부모, rem은 루트가 기준이다.

</details>

**추가로 알면 좋은 것:** ch·lh·svh·dvh·clamp와 다크 모드 색상 체계는 이 원본 계산과 별도로 학습한다.

<!-- legacy-migration -->

<a id="index-section-87"></a>
<a id="css-67"></a>
<a id="css-16"></a>
<a id="css-47"></a>
<a id="css-22"></a>
<a id="index-section-89"></a>
<a id="css-34"></a>
<a id="css-31"></a>
<a id="css-35"></a>
<a id="css-51"></a>
<a id="css-49"></a>
<a id="css-12"></a>
<a id="index-section-71"></a>
<a id="index-section-72"></a>
<a id="css-32"></a>
<a id="css-7"></a>
<a id="index-section-74"></a>
<a id="css-48"></a>
<a id="index-section-73"></a>
<a id="css-24"></a>
<a id="css-27"></a>
<a id="css-26"></a>
<a id="css-23"></a>

### 이전 색인 링크 안내

이전 절 주소를 보존한 이동 안내다. 옛 절 번호와 현재 절은 같지 않다. [현재 CSS 목차](README.md)에서 수업 본문과 **추가로 알면 좋은 것**을 구분해 찾는다.
