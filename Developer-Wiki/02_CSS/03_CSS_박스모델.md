# 03. 박스 모델 — width와 화면 너비가 다른 이유

[CSS 목차](README.md) · [마진과 가운데 정렬](03-02_CSS_마진과_가운데정렬.md)

요소의 크기는 **내용(content) → 안쪽 여백(padding) → 테두리(border) → 바깥 여백(margin)** 순서로 읽는다. margin은 테두리 바깥이므로 배경색을 칠하는 영역이 아니다.

**설명용 계산:** `width:100px; padding:10px; border:1px solid`인 기본 `content-box` 상자의 테두리까지 너비는 `100 + 10×2 + 1×2 = 122px`이다. `width`가 내용 영역을 가리키기 때문이다. 같은 상자에 `box-sizing:border-box`를 주면 테두리까지 너비가 100px이고 내용 너비가 78px이 된다. 이제 원본의 300px 상자에 같은 계산을 적용한다.

<!-- chapter-toc -->

- [1. 원본의 300px 상자 비교](03_CSS_박스모델.md#section-1)
- [2. 원본을 위에서 아래로 읽기](03_CSS_박스모델.md#section-2)
- [3. width에 상한·하한을 더하기](03_CSS_박스모델.md#section-3)
- [복습](03_CSS_박스모델.md#section-4)

<a id="section-1"></a>

## 1. 원본의 300px 상자 비교

### 강사님 코드

`asset/css/03_box.css` 94~107행 — **원본 발췌**

```css
.box {
    border: 1px solid red;

    width: 300px;
    height: 300px;

    margin: 50px;
}

.box-sizing {
    padding: 50px;

    box-sizing: border-box;
}
```

HTML의 첫 요소는 `class="box"`, 다음 요소는 `class="box box-sizing"`이다. 두 번째는 두 클래스의 규칙을 함께 받는다. box-sizing이 없을 때와 있을 때의 width 기준을 비교한 실험이다.

### 내 코드

`asset/css/03_box.css` 102~117행 — **원본 발췌**

```css
.box {
    border: 1px solid red;

    width: 300px;
    height: 300px;

    margin: 50px;
}

.box-sizing {
    padding: 50px;

    /* box-sizing boder-box를 주게된다면, border+padding+content 사이즈까지 width,height영역으로 바뀜 */
    /* 기본값은 content-box로 되어 있어서 content의 사이즈면 조절됨 */
    box-sizing: border-box;
}
```

선언과 계산 결과가 같다. 내 주석은 width의 기준이 바뀐다는 점을 설명한다. “margin까지 width 안에 들어간다”로 확대하면 안 된다.

| 원본 요소 | content 너비 | 좌우 padding | 좌우 border | 테두리까지 너비 |
| --- | --- | --- | --- | --- |
| `.box` | 300 | 0+0 | 1+1 | 302px |
| `.box.box-sizing` | 198 | 50+50 | 1+1 | 300px |

첫 번째의 `width:300px`는 content 기준이다. 두 번째의 `width:300px`는 border-box 기준이므로 content에 남는 너비가 198px이다. 양쪽 margin 50px는 이 표의 테두리 너비에 포함하지 않았다.

<a id="section-2"></a>

## 2. 원본을 위에서 아래로 읽기

양쪽 `div.second`는 여러 선언을 연달아 실험한다. 마지막으로 적용되는 값은 `margin:30px`, `padding:30px`, `border:1px solid red`다. 앞에서 준 서로 다른 방향의 값들이 모두 누적되는 것이 아니다.

| 축약 값의 개수 | 적용 방향 |
| --- | --- |
| 1개 | 네 방향 모두 |
| 2개 | 위·아래 / 왼쪽·오른쪽 |
| 3개 | 위 / 왼쪽·오른쪽 / 아래 |
| 4개 | 위 → 오른쪽 → 아래 → 왼쪽 |

원본 second의 content는 150×200px, padding은 사방 30px, border는 사방 1px이므로 테두리까지 **212×262px**이다. border-radius는 모서리 모양을 바꾸며 이 너비·높이를 없애지 않는다.

원본 `.profile img`는 너비·높이 모두 200px와 `border-radius:50%`로 원 모양을 만든다. 가로세로 크기가 다르면 50%만으로 원이 되지는 않는다. `.chat.right`의 `10px 0 10px 10px`는 왼쪽 위 → 오른쪽 위 → 오른쪽 아래 → 왼쪽 아래 순이다. margin의 4방향 순서와 혼동하지 않는다.

<a id="section-3"></a>

## 3. width에 상한·하한을 더하기

양쪽 `.width`는 `width:70%`, `min-width:400px`, `max-width:600px`다. 부모의 content 너비가 500px이면 70%인 350px 대신 최소 400px, 1000px이면 700px 대신 최대 600px가 사용된다. 이 원본은 content-box이므로 border 2px가 별도로 붙는다.

최소 너비보다 화면이 작으면 가로로 넘칠 수 있다. “%이니 모든 화면에 자동으로 맞는다”는 결론은 틀리다. [박스 모델 표준](https://www.w3.org/TR/CSS2/box.html)

<a id="section-4"></a>

## 복습

`width:200px; padding:20px; border:2px solid;`의 테두리까지 너비는? border-box를 추가하면?

<details>
<summary>해설</summary>

content-box에서는 244px다. border-box에서는 테두리까지 200px이고 content는 156px다. margin은 두 계산에 넣지 않는다.

</details>

**추가로 알면 좋은 것:** 논리 속성, border-image 상세, 새로운 카드 설계는 기본 크기 계산과 분리한다.

<!-- legacy-migration -->

<a id="css-4"></a>
<a id="css-48"></a>
<a id="index-section-81"></a>
<a id="css-33"></a>
<a id="css-40"></a>
<a id="index-section-101"></a>
<a id="index-section-68"></a>
<a id="css-39"></a>
<a id="css-18"></a>
<a id="css-50"></a>
<a id="css-6"></a>
<a id="css-9"></a>
<a id="css-62"></a>
<a id="css-14"></a>

### 이전 색인 링크 안내

이전 절 주소를 보존한 이동 안내다. 옛 절 번호와 현재 절은 같지 않다. 크기 계산은 이 문서, 간격은 [마진·가운데 정렬](03-02_CSS_마진과_가운데정렬.md)에서 읽는다.

---

[장별 연습문제 풀기](실습/연습문제/03_CSS_박스모델_연습문제.md)
