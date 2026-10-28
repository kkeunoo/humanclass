# 05. 투명도와 숨김 — 안 보인다고 없는 것은 아니다

[CSS 목차](README.md)

요소를 숨길 때는 **화면에 보이는가**, **원래 자리가 남는가**, **사용자가 조작할 수 있는가**를 각각 물어야 한다. 이 세 질문을 한꺼번에 “숨김”이라고 부르면 원본의 `display`, `visibility`, `opacity` 차이를 놓친다.

먼저 수업의 문단 실험을 **보임과 자리**의 관점에서 읽는다. 그 뒤 버튼으로 바꾸어 보는 설명용 예제로 조작 차이를 확인한다. 버튼 예제는 강사님·내 원본의 출력이 아니다.

**설명용 작은 예:** 나란한 문단 세 개 중 가운데 문단에 `display:none`을 주면 마지막 문단이 그 자리로 올라온다. `visibility:hidden`이나 `opacity:0`을 주면 가운데 자리는 남는다. 여기까지는 화면과 자리의 결과이며, 클릭·포커스의 차이는 아래 원본 비교 뒤에 확인한다.

<!-- chapter-toc -->

- [1. 문단에 적용한 강사님 코드](05_CSS_투명도와_요소숨김.md#section-1)
- [2. 내 코드와 결과 비교](05_CSS_투명도와_요소숨김.md#section-2)
- [3. 요소 전체와 배경색 알파](05_CSS_투명도와_요소숨김.md#section-3)
- [복습](05_CSS_투명도와_요소숨김.md#section-4)

<a id="section-1"></a>

## 1. 강사님 코드

`05_opacity.html` 8~17행 — **원본 발췌**

```css
        .hidden {
            visibility: hidden;
        }
        .none {
            display: none;
        }
        .opacity{
            /* opacity: 0.7; */
            opacity: 0;
        }
```

원본의 둘째 문단은 hidden, 셋째는 none, 넷째는 opacity 클래스다. hidden과 opacity 문단은 자리를 유지하지만 none 문단의 박스는 배치에서 빠진다.

<a id="section-2"></a>

## 2. 내 코드

`05_opacity.html` 8~22행 — **원본 발췌**

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

실행 선언은 같다. 내 “동일하게 자리는 있으나 투명하게”라는 메모는 **화면과 자리**에 대한 관찰까지만 맞다. 클릭·포커스 동작까지 같다는 뜻으로 읽으면 안 된다.

| 설정 | 자신의 박스 자리 | 자신이 그려짐 | 일반적인 자신의 클릭·키보드 포커스 |
| --- | --- | --- | --- |
| display:none | 없음 | 안 보임 | 대상에서 제외 |
| visibility:hidden | 유지 | 안 보임 | 대상에서 제외 |
| opacity:0 | 유지 | 완전히 투명 | 이것만으로 차단하지 않음 |

visibility를 자식에서 다시 visible로 지정하는 경우 등은 이 단순 실험과 구분한다. 원본은 문단뿐이라 클릭·포커스 차이를 직접 보여 주지는 않는다. 아래는 **배운 버튼으로 관찰 대상을 바꾼 설명용 재구성**이다.

```html
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <title>숨김 비교</title>
    <style>
        .hidden { visibility: hidden; }
        .none { display: none; }
        .opacity { opacity: 0; }
    </style>
</head>
<body>
    <button>시작</button>
    <button class="hidden">hidden</button>
    <button class="none">none</button>
    <button class="opacity">투명한 버튼</button>
    <button>끝</button>
</body>
</html>
```

시작 버튼에서 Tab으로 이동하면 hidden·none은 건너뛰지만 투명한 버튼은 포커스를 받을 수 있다. 안 보이는 버튼 위에 포인터를 놓아도 투명도만으로 클릭이 차단되지는 않는다. 단순히 안 보이게 하려는지, 자리도 없앨지, 조작도 막을지 먼저 정한다.

<a id="section-3"></a>

## 3. 요소 전체와 배경색 알파

opacity를 부모에 적용하면 그 요소와 자식이 함께 합성되어 흐려진다. 자식에 opacity:1을 줘도 부모의 투명도를 취소하는 방법이 되지 않는다. 배경만 흐리게 하고 글자는 그대로 두려면 앞 장의 rgba 배경색과 비교한다. [CSS 색과 opacity 표준](https://www.w3.org/TR/css-color-4/#transparency)

display:none은 HTML을 삭제하거나 주석으로 바꾸는 기능도 아니다. 스타일을 바꾸면 다시 표시할 수 있다.

<a id="section-4"></a>

## 복습

원본에서 다섯째 문단이 위로 당겨지는 원인은 hidden일까, none일까?

<details>
<summary>해설</summary>

none이다. hidden과 opacity 문단의 자리는 남는다. opacity:0인 입력을 숨긴 것만으로 조작 불가능해졌다고 판단하면 안 된다.

</details>

**추가로 알면 좋은 것:** inert·aria-hidden·모달의 포커스 관리·접근성 구현은 이 세 속성의 차이와 분리하여 배운다.

<!-- legacy-migration -->

<a id="css-6"></a>
<a id="css-9"></a>
<a id="css-30"></a>
<a id="css-28"></a>
<a id="css-21"></a>
<a id="css-24"></a>
<a id="css-12"></a>

### 이전 색인 링크 안내

이전 절 주소를 보존한 이동 안내다. 옛 절 번호와 현재 절은 같지 않다. [현재 CSS 목차](README.md)에서 수업 본문과 **추가로 알면 좋은 것**을 구분해 찾는다.

---

[장별 연습문제 풀기](실습/연습문제/05_CSS_투명도와_요소숨김_연습문제.md)
