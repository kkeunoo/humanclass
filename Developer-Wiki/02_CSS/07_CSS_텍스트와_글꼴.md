# 07. 글꼴과 텍스트 — 글자 모양과 줄 배치 구분하기

[CSS 목차](README.md)

<!-- chapter-toc -->

- [1. 웹폰트 등록과 사용](#section-1)
- [2. 원본을 교정하며 읽기](#section-2)
- [3. 줄 높이와 정렬](#section-3)
- [4. 한 줄 말줄임](#section-4)
- [복습](#section-5)

<a id="section-1"></a>

## 1. 웹폰트 등록과 사용

### 강사님 코드

`asset/css/07_font.css` 1~14행 — **원본 발췌**

```css
/* 웹폰트 */
@font-face {
    font-family: 'OngleipParkDahyeon';
    src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/2411-3@1.0/Ownglyph_ParkDaHyun.woff2') format('woff2');
    font-weight: normal;
    font-display: swap;
}

.size{
    font-size: 32px;
}
.font {
    font-family: 'OngleipParkDahyeon', Arial
}
```

font-face는 사용할 글꼴 이름과 파일을 연결한다. 등록만으로 모든 글자가 바뀌지는 않고 `.font`에서 그 이름을 사용한다. 로드되지 않거나 필요한 문자가 없으면 뒤의 글꼴 등으로 대체될 수 있다.

### 내 코드

`asset/css/07_font.css` 1~15행 — **원본 발췌**

```css
/* 웹폰트, 컴퓨터에 설치 없어도 쓰게 할 수 있도록 링크를 다운받아놓는 선언 */
@font-face {
    font-family: 'NostalgicPoliceVibe';
    src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/2601-6@1.0/Griun_PolSensibility-Rg.woff2') format('woff2');
    font-weight: normal;
    font-display: swap;
}

.size {
    font-size: 32px;
}

.font {
    font-family: 'NostalgicPoliceVibe', Arial;
}
```

구조는 같고 글꼴 이름·URL이 다르다. 두 코드 모두 `font-display:swap`을 썼으므로 **이 속성의 기본 역할은 학습 본문**에 둔다. 대체 글꼴로 글자를 먼저 표시하고 웹폰트가 준비되면 바꿔 표시할 수 있게 하는 설정이다. 이름만 바꾸고 src를 그대로 두면 다른 폰트 파일이 되는 것은 아니다.

<a id="section-2"></a>

## 2. 원본을 교정하며 읽기

양쪽 `07_font.html` 11~22행은 p 안에 div를 넣었다. 브라우저는 div 앞에서 p를 닫아 해석하므로, 들여쓰기만 보고 div가 p의 글자 크기·폰트를 상속받는다고 판단하면 안 된다.

```html
<!-- 상속 관찰을 위한 구조 교정. 원본 발췌 아님 -->
<div class="size">
    부모 글씨
    <div>자식 글씨</div>
</div>
```

| 원본 주제 | 올바르게 읽을 기준 |
| --- | --- |
| font-size:32px | 크기. 실제 부모·자식 구조에서 상속 확인 |
| font-style:italic | 기울인 표현. HTML em의 강조 의미와 구분 |
| font-weight | normal은 400, bold는 700. “기본값 500” 주석 교정 |
| fw-2000 | 2000은 허용 범위 밖이라 선언이 무효. 가장 굵은 글자가 아님 |
| letter-spacing | 강사님 -0.1em, 나는 0em이 최종 실행값이라 간격 차이 발생 |
| fake-h1 | 크게·굵게 보여도 실제 h1 의미가 생기지 않음 |

현재 숫자 굵기의 허용 범위는 1~1000이고 반드시 100 단위만 가능한 것은 아니다. 실제 모양은 폰트가 제공하는 굵기에 영향을 받는다. 가변 글꼴 상세 구현은 추가 학습이다. [글꼴 표준](https://www.w3.org/TR/css-fonts-4/#font-weight-prop)

<a id="section-3"></a>

## 3. 줄 높이와 정렬

`.lh`의 line-height:300%는 해당 글자 크기의 3배인 줄 높이다. `.middle`은 높이와 line-height를 모두 100px로 하여 **한 줄 텍스트**를 세로 가운데쯤 놓는다. 여러 줄·줄바꿈까지 같은 방식으로 해결되는 것은 아니다.

text-align은 상자 안의 인라인 내용을 정렬한다. 원본처럼 `.right`를 div에 주면 그 안의 링크가 오른쪽으로 간다. 링크 자체에만 주는 것과 결과를 구분한다. 강사님 HTML은 두 경우를 직접 비교하지만 내 첫 링크에는 right 클래스가 없어 비교 조건이 다르다.

text-decoration의 underline·line-through·none은 각각 밑줄·취소선·선 제거다. 원본의 :link·:visited는 미방문·방문 링크를 구분하지만 양쪽을 같은 aqua로 지정해서 색 차이가 안 보인다.

<a id="section-4"></a>

## 4. 한 줄 말줄임

### 강사님 코드

`asset/css/07_font.css` 74~81행 — **원본 발췌**

```css
.nowrap {
    border: 1px solid red;
    width: 200px;

    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
}
```

### 내 코드

`asset/css/07_font.css` 87~95행 — **원본 발췌**

```css
.nowrap {
    border: 1px solid red;
    width: 200px;

    /* 3개가 조합으로 많이 쓰임, 가린 뒤 ... 표시를 하기 위해 */
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
}
```

선언과 조건이 같다. 제한된 너비, 줄바꿈 억제, 넘친 부분 숨김이 함께 있어야 원본처럼 말줄임을 관찰할 수 있다. ellipsis만 붙인다고 모든 긴 글이 자동으로 잘리는 것은 아니다. 원본 title에는 전체 문장을 넣었지만 모든 입력 환경에서 전체 내용을 보여 주는 수단이라고 보장하지는 않는다.

`word-wrap:break-word`는 긴 단어를 필요하면 나누고, `word-break:break-all`은 더 적극적으로 글자 사이의 줄바꿈을 허용한다. HTML 원문 내용이 삭제되는 것은 아니다.

<a id="section-5"></a>

## 복습

폰트 상속이 안 되는 것처럼 보일 때 크기 숫자를 더 키우기 전에 무엇을 확인할까?

<details>
<summary>해설</summary>

CSS 파일 연결, 폰트 이름·파일 로드, 실제 요소 중첩, 자식에 별도 선언이 있는지 확인한다. 양쪽 p/div 예제에서는 먼저 HTML 구조를 교정한다.

</details>

**추가로 알면 좋은 것:** 폰트 사전 로드·파일 분할·고급 타이포그래피 체계는 원본 font-display의 기본 역할과 구분한다.

<!-- legacy-migration -->

<a id="index-section-22"></a>
<a id="css-44"></a>
<a id="index-section-107"></a>
<a id="css-25"></a>
<a id="css-54"></a>
<a id="index-section-19"></a>
<a id="css-46"></a>

### 이전 색인 링크 안내

이전 절 주소를 보존한 이동 안내다. 옛 절 번호와 현재 절은 같지 않다. [현재 CSS 목차](README.md)에서 수업 본문과 **추가로 알면 좋은 것**을 구분해 찾는다.
