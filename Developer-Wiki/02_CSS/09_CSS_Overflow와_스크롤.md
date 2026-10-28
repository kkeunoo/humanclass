# 09. overflow — 넘친 내용을 어떻게 보여 줄까

[CSS 목차](README.md)

내용이 상자보다 많아졌을 때 상자의 크기와 넘친 부분의 처리 방식을 나누어 읽는다. overflow 자체가 원하는 너비·높이를 정해 주지는 않는다.

**설명용 예:** 높이 50px 상자에 100px 높이의 내용이 들어갔다고 하자. `overflow:hidden`이면 넘친 부분이 화면에서 잘리고, `overflow:auto`이면 내용을 스크롤해 볼 수 있는 영역이 된다. 내용이 상자 안에 모두 들어가면 차이를 관찰하기 어려우므로 아래 원본에서는 상자 크기와 내용부터 확인한다.

<!-- chapter-toc -->

- [1. 원본의 기본 비교](09_CSS_Overflow와_스크롤.md#section-1)
- [2. 가로 항목 목록](09_CSS_Overflow와_스크롤.md#section-2)
- [복습](09_CSS_Overflow와_스크롤.md#section-3)

<a id="section-1"></a>

## 1. 원본의 기본 비교

강사님 `.box`는 width:100px·height:130px, 내 `.box`는 width:130px·height:130px다. 같은 속성을 써도 글줄 수와 넘치는 양이 달라질 수 있다. 동작 차이를 비교할 때는 크기와 텍스트 조건부터 맞춘다.

| 설정 | 원본에서 관찰할 것 |
| --- | --- |
| visible | 기본적으로 바깥까지 그려질 수 있음 |
| hidden | 넘친 부분을 가리고 일반 스크롤 막대를 제공하지 않음 |
| scroll | 내용이 적어도 스크롤 UI를 위한 상태. 막대 모양·상시 표시는 환경에 따라 다름 |
| auto | 넘침에 따라 스크롤 가능한 영역을 만듦 |
| overflow-y:scroll | 세로축을 지정. 반대 축의 계산도 함께 확인 |

원본의 짧은 Lorem ipsum 상자도 scroll을 써서 auto와 차이를 관찰한다. hidden이라고 내용 자체가 삭제되는 것은 아니다. 내 “실무에서는 auto를 자주 쓰지 않음” 주석은 모든 프로젝트의 규칙으로 삼지 않는다.

<a id="section-2"></a>

## 2. 가로 항목 목록

### 강사님 코드

`09_overflow.html` 31~42행 — **원본 발췌**

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

부모는 300px, 자식은 inline-block 5개다. nowrap이 한 줄을 유지하고 auto가 넘친 가로 내용을 스크롤할 수 있게 한다.

### 내 코드

`09_overflow.html` 35~47행 — **원본 발췌**

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

설정이 같다. 각 항목은 content 100 + border 2 + 좌우 margin 10 = 112px이고, HTML 공백도 사이에 있을 수 있다. 다섯 항목이 300px 안에 들어갈 수 없다. 이 계산은 기본 box-sizing 조건을 따른다.

`overflow-y:scroll`만 써도 반대 축 visible이 그대로 유지되지 않고 auto로 계산될 수 있다. “y만 지정했으니 가로는 어떤 경우에도 스크롤이 없다”고 단정하지 않는다. [overflow 표준](https://www.w3.org/TR/css-overflow-3/)

<a id="section-3"></a>

## 복습

가로 목록에서 white-space:nowrap을 지우면 어떤 결과를 먼저 예상할까?

<details>
<summary>해설</summary>

inline-block이 공간에 따라 다음 줄로 내려갈 수 있다. 가로 스크롤이 줄거나 없어질 수 있으므로 넘침 설정뿐 아니라 줄바꿈 조건을 같이 읽는다.

</details>

**추가로 알면 좋은 것:** overflow:clip·overscroll-behavior·스크롤 잠금 모달 구현은 별도 학습이다.

<!-- legacy-migration -->

<a id="css-4"></a>
<a id="css-20"></a>
<a id="css-7"></a>

### 이전 색인 링크 안내

이전 절 주소를 보존한 이동 안내다. 옛 절 번호와 현재 절은 같지 않다. [현재 CSS 목차](README.md)에서 수업 본문과 **추가로 알면 좋은 것**을 구분해 찾는다.

---

[장별 연습문제 풀기](실습/연습문제/09_CSS_Overflow와_스크롤_연습문제.md)
