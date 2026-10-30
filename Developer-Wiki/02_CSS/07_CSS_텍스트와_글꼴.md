# 07. 글꼴과 텍스트 — 모양·줄 높이·잘림을 따로 읽기

[CSS 목차](README.md) · [읽기 안내](00_CSS_V3_동작_백과_읽기법.md)

글꼴은 글자 모양이고 font-size는 크기이며 line-height는 줄 배치에 쓰는 높이다. 여기에 줄바꿈과 넘침 조건이 더해져 화면의 글줄이 정해진다. 글꼴 등록과 실제 사용도 두 단계로 나눈다.

<a id="chapter-toc"></a>

**이 장의 목차:** [목표](#learn) · [개념](#concepts) · [작은 예제](#example) · [내 코드](#my-code) · [연결](#connections) · [평가](#review) · [비교](#teacher) · [결과·실험](#results) · [TIP·출처](#tips) · [복습](#practice)

<a id="learn"></a>

## 1. 이 장에서 배울 것

웹폰트 등록·선택·대체 글꼴을 연결한다. 한 줄 말줄임 조건과 줄 높이·정렬을 설명하고 원본 구조·무효값을 교정한다.

이번 장의 개념과 원본 기능은 수업 범위다. 원본에 없는 선택 기능은 9절 TIP으로 구분한다. 결과를 읽을 때는 선택된 요소·속성·기준값·실행 상태를 함께 적는다.

<a id="concepts"></a>

## 2. 무엇이며, 왜 필요한가

@font-face는 사용할 이름과 파일을 연결한다. 등록만으로 모든 요소가 그 폰트를 쓰지는 않는다. font-family에서 같은 이름을 지정해야 하며 로드 실패·문자 지원 여부에 따라 뒤의 글꼴 등으로 대체된다. 이름만 바꾸고 src가 같으면 새 글꼴 파일로 바뀌는 것이 아니다. 원본 font-display:swap은 대체 글꼴로 먼저 표시하고 준비된 웹폰트로 바꿀 수 있게 하는 설정으로, 실제 배운 기본 사용이다.

font-size20px에 line-height:2면 줄 높이는40px다. 글자 그림 자체가40px가 되었다는 뜻은 아니다. 한 줄 텍스트의 상자 높이와 line-height를 같게 하여 가운데쯤 놓는 기법은 여러 줄까지 같은 해법으로 보장되지 않는다.

| 설정 | 역할·주의 |
| --- | --- |
| font-style:italic | 기울인 표현, em의 강조 의미와 다름 |
| font-weight | normal400·bold700, 숫자2000은 허용 범위 밖 |
| letter-spacing | 글자 간격 |
| text-align | 상자 안 인라인 내용의 정렬 |
| text-decoration | 밑줄·취소선 등 |
| white-space:nowrap | 줄바꿈 억제 |
| overflow:hidden + text-overflow:ellipsis | 제한된 너비에서 넘침 숨김과 말줄임 표시 |

ellipsis만으로 글이 자동 삭제되지는 않는다. 줄바꿈을 막고 실제 넘침이 생길 너비 조건까지 함께 확인한다.

> 📚 **출처 · 본문 설명 확인:** [W3C 글꼴·굵기](https://www.w3.org/TR/css-fonts-4/)와 [MDN text-overflow](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-overflow). 설명과 비교 표는 수업 원본을 바탕으로 새로 풀어 썼다. 외부 원문을 직접 인용한 문장은 아니다. 확인일: 2026-10-28.

<a id="example"></a>

## 3. 작은 예제로 먼저 이해하기

**새 설명 예제 · 전체 파일.** [실행 파일](실습/책형_복습/07_CSS_텍스트와_글꼴.html)을 브라우저로 연다. 이 예제는 위 style 안에 CSS를 모두 넣어 외부 파일 연결이 필요 없다. 원본 CSS에 붙이면 다른 규칙이 섞일 수 있으므로 먼저 별도 파일로 확인한다.

```html
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>07. 글꼴과 텍스트 — 모양·줄 높이·잘림을 따로 읽기</title>
    <style>
        .text { font-family: Arial, sans-serif; font-size: 20px; line-height: 2; }
        .short { width: 160px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; border: 1px solid red; }
    </style>
</head>
<body>
    <h1>글줄 관찰</h1>
    <div class="text">첫째 줄<br>둘째 줄</div>
    <p class="short" title="긴 학습 내용을 한 줄로 표시하는 예제입니다.">긴 학습 내용을 한 줄로 표시하는 예제입니다.</p>
</body>
</html>
```

text는20px 글자 크기와40px 줄 높이다. short는160px를 넘는 한 줄을 숨기고 말줄임을 표시한다. 외부 폰트 로드가 필요 없도록 작은 예제는 시스템 글꼴을 사용했다. 정확히 어느 글자에서 잘리는지는 실제 글꼴·환경에 따라 달라지므로 마지막 글자까지 고정 출력으로 쓰지 않는다. title은 보충 설명일 뿐 모든 환경에서 전체 내용을 제공하는 완전한 대책으로 보장하지 않는다.

<a id="my-code"></a>

## 4. 내가 작성한 코드를 따라 읽기

아래는 **내 원본 발췌**다. 주석의 표현도 원문대로 두었다. 설명에서 교정한 내용을 원본에 이미 수정한 것처럼 읽지 않는다.

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_html/css/asset/css/07_font.css` 1–15행

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

**발췌 바로 풀이:** 구조는 같고 글꼴 이름·URL이 다르다. 두 코드 모두 `font-display:swap`을 썼으므로 **이 속성의 기본 역할은 학습 본문**에 둔다. 대체 글꼴로 글자를 먼저 표시하고 웹폰트가 준비되면 바꿔 표시할 수 있게 하는 설정이다. 이름만 바꾸고 src를 그대로 두면 다른 폰트 파일이 되는 것은 아니다.

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_html/css/asset/css/07_font.css` 87–95행

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

**발췌 바로 풀이:** 선언과 조건이 같다. 제한된 너비, 줄바꿈 억제, 넘친 부분 숨김이 함께 있어야 원본처럼 말줄임을 관찰할 수 있다. ellipsis만 붙인다고 모든 긴 글이 자동으로 잘리는 것은 아니다. 원본 title에는 전체 문장을 넣었지만 모든 입력 환경에서 전체 내용을 보여 주는 수단이라고 보장하지는 않는다.

내 폰트 이름은 NostalgicPoliceVibe이고 src도 강사님과 다르다. @font-face에서 등록하고 .font가 그 이름을 선택한다. .nowrap은 width200·nowrap·hidden·ellipsis를 함께 썼다. 내 ‘3개 조합’ 메모는 유익하지만 너비 제한도 전제다. 이름이나 메모만 보지 말고 실제 URL·등록명·사용명을 순서대로 맞춘다.

<a id="connections"></a>

## 5. 파일·요소·값이 연결되는 흐름

HTML link → CSS @font-face 이름·src → 요소의 font-family → 파일 로딩·대체 → 글줄 배치 순서다. 원본 HTML은 p 안에 div를 두어 브라우저가 p를 먼저 닫아 해석할 수 있다. 들여쓰기만 보고 div가 p의 폰트를 상속한다고 판단하지 않는다. 상속 관찰은 div 안 div처럼 허용 구조로 고친 개선 예제로 따로 확인한다.

<a id="review"></a>

## 6. 잘한 점·아쉬운 점·개선 방향

**잘한 점:** 웹폰트의 이유와 말줄임 조합을 남겼다. **실제 오류:** fw-2000은 가장 굵은 설정이 아니라 무효 선언이다. 숫자 굵기 허용 범위1~1000과 실제 폰트의 제공 굵기를 구분한다. **조건 차이:** 강사님 letter-spacing 최종-0.1em, 나는0em이며 내 첫 링크에는 right class가 없어 정렬 비교 조건도 다르다. 크게 꾸민 fake-h1이 실제 제목 의미를 갖지는 않는다.

제안은 원본을 수정한 결과가 아니다. **실제 오류**, **관찰을 위한 수업용 단순화**, **목적에 따라 가능한 선택**을 구별한다. 단지 짧게 쓰거나 최신 기능을 쓴다고 더 좋은 코드는 아니다.

<a id="teacher"></a>

## 7. 강사님 코드가 도움이 되는 비교



font-face 구조와 한 줄 말줄임 선언은 같아 중복 원문을 인용하지 않는다. 양쪽 :link·:visited가 같은 aqua라면 방문 여부를 다르게 선택해도 색상 차이는 나타나지 않는다. 비교는 코드의 조건과 지정값을 함께 보아야 한다.

<a id="results"></a>

## 8. 결과를 예상하고 한 가지 바꾸기

아래는 **명시한 조건에서의 코드 기준 예상**이다. 이번 편집에서 실제 브라우저 렌더링을 재실행했다는 기록과 구별한다. 매 실험은 원래 예제로 돌아가 한 조건만 바꾼다.

| 한 가지 변경 | 예상 | 확인 |
| --- | --- | --- |
| text line-height만1 | 줄 높이20px | 글자 크기는20 유지 |
| 원래 short width만320px | 더 많은 글자 표시 | 넘침량 감소 |
| 원래 short nowrap 제거 | 여러 줄 가능 | 한 줄 전제 변경 |
| 원래 short ellipsis 제거 | 점표시 없이 잘릴 수 있음 | 숨김과 표시 분리 |

폰트가 안 바뀌면 CSS 연결·이름 일치·파일 로딩·실제 중첩·자식의 별도 선언을 확인한다. word-wrap:break-word와 word-break:break-all은 긴 내용의 줄바꿈 기회를 다르게 다룬다. 원문 텍스트가 삭제된 것이 아니다.

<a id="tips"></a>

## 9. 추가로 알면 좋은 것과 출처

> 💡 **TIP · 수업 범위 밖:** 가변 폰트 구현·사전 로드·파일 분할·다중 줄 말줄임·고급 타이포그래피 체계는 추가 학습이다. 원본에 있는 font-display 기본 설명까지 TIP으로 숨기지 않는다.

이하의 내용은 **수업 원본에서 확인된 필수 진도가 아닌 추가 학습**이다. 위의 기본 설명을 이해한 뒤 필요할 때 읽는다.

<a id="extra-02-4"></a>

### 4. BACKUP의 글자·폰트 확장

pre·pre-wrap·pre-line, keep-all, 여러 줄 말줄임, writing-mode·direction, user-select는 각각 공백·줄바꿈·쓰기 방향·선택 정책을 다룬다. 본문은 원본의 nowrap·word-wrap·break-all·한 줄 ellipsis를 중심으로 읽는다.

폰트 굵기별 등록·가변 폰트·사전 로드·파일 분할·배포 최적화는 후속 주제다. 원본의 `font-display:swap` 기본 역할을 이 심화 묶음에 숨기지 않는다.

이 절의 확장은 기본 문제의 필수 조건이 아니다. 2절의 📚 출처는 배운 기능의 설명을 확인하는 근거이며, 출처가 있다는 이유로 모두 수업 밖 내용인 것은 아니다.

<a id="practice"></a>

## 10. 복습과 빠른 정리

1. 글꼴 등록만으로 모든 요소가 바뀌는가?
2. 20px·line-height300%의 줄 높이는?
3. ellipsis만 지정하면 항상 말줄임되는가?

<details>
<summary>짧은 풀이 — 먼저 답한 뒤 확인</summary>

등록 후 사용명 지정을 확인한다. 줄 높이는60px다. 너비 제한·nowrap·넘침 처리 등 조건이 필요하다.

</details>

| 구분 | 속성 |
| --- | --- |
| 모양 | font-family |
| 크기 | font-size |
| 줄 높이 | line-height |
| 줄바꿈·잘림 | white-space·overflow·text-overflow |

[장별 연습문제](실습/연습문제/07_CSS_텍스트와_글꼴_연습문제.md)에서 예상·설명·수정을 이어 간다. 다음은 [위치 배치](08_CSS_Position과_요소위치.md)다.

<!-- 이전 색인 이동 주소 보존 -->
<a id="css-25"></a>
<a id="css-44"></a>
<a id="css-46"></a>
<a id="css-54"></a>
<a id="index-section-107"></a>
<a id="index-section-19"></a>
<a id="index-section-22"></a>
<a id="section-1"></a>
<a id="section-2"></a>
<a id="section-3"></a>
<a id="section-4"></a>
<a id="section-5"></a>

이전 절 주소로 왔다면 [이 장의 목차](#chapter-toc)에서 현재 설명을 찾는다.
