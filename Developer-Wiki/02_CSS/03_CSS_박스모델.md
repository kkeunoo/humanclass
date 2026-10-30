# 03. 박스 모델 — width와 실제 상자 너비

[CSS 목차](README.md) · [읽기 안내](00_CSS_V3_동작_백과_읽기법.md)

width를 300px로 썼는데 테두리까지 재면 302px일 수 있다. 내용·안쪽 여백·테두리·바깥 간격을 나누어 계산하면 그 차이를 설명할 수 있다.

<a id="chapter-toc"></a>

**이 장의 목차:** [목표](#learn) · [개념](#concepts) · [작은 예제](#example) · [내 코드](#my-code) · [연결](#connections) · [평가](#review) · [비교](#teacher) · [결과·실험](#results) · [TIP·출처](#tips) · [복습](#practice)

<a id="learn"></a>

## 1. 이 장에서 배울 것

content·padding·border·margin을 구별하고 content-box와 border-box의 크기를 계산한다. 축약 선언의 방향과 min·max 제한도 읽는다.

이번 장의 개념과 원본 기능은 수업 범위다. 원본에 없는 선택 기능은 9절 TIP으로 구분한다. 결과를 읽을 때는 선택된 요소·속성·기준값·실행 상태를 함께 적는다.

<a id="concepts"></a>

## 2. 무엇이며, 왜 필요한가

박스는 내용(content)을 안쪽 여백(padding)이 감싸고, 그 바깥에 테두리(border)가 있으며, 다른 상자와의 바깥 간격은 margin으로 둔다. 포장 상자에 비유하면 내용물과 완충 공간, 상자 벽을 나누는 셈이다. 다만 margin은 내 배경을 칠하는 상자 내부 공간이 아니다.

```text
margin 바깥 간격
┌ border ────────────────────┐
│ padding 안쪽 여백           │
│   ┌ content 내용 ──────┐   │
│   └───────────────────┘   │
└───────────────────────────┘
```

일반적인 기본 content-box에서 width는 내용 너비다. 테두리까지는 width + 좌우 padding + 좌우 border를 더한다. border-box는 width 안에 padding·border를 포함하므로 내용에 남는 너비를 역산한다. margin은 어느 쪽 width에도 들어가지 않는다.

| 축약 값 | 방향 |
| --- | --- |
| 10px | 사방 |
| 10px 20px | 위아래 / 좌우 |
| 10px 20px 30px | 위 / 좌우 / 아래 |
| 10px 20px 30px 40px | 위 / 오른쪽 / 아래 / 왼쪽 |

이 표는 margin·padding의 방향이다. border-radius 네 값은 왼쪽 위부터 모서리를 도는 순서이므로 동일한 표로 외우지 않는다.

> 📚 **출처 · 본문 설명 확인:** [W3C 박스 모델](https://www.w3.org/TR/CSS2/box.html) 및 [box-sizing](https://www.w3.org/TR/css-sizing-3/#box-sizing). 설명과 비교 표는 수업 원본을 바탕으로 새로 풀어 썼다. 외부 원문을 직접 인용한 문장은 아니다. 확인일: 2026-10-28.

<a id="example"></a>

## 3. 작은 예제로 먼저 이해하기

**새 설명 예제 · 전체 파일.** [실행 파일](실습/책형_복습/03_CSS_박스모델.html)을 브라우저로 연다. 이 예제는 위 style 안에 CSS를 모두 넣어 외부 파일 연결이 필요 없다. 원본 CSS에 붙이면 다른 규칙이 섞일 수 있으므로 먼저 별도 파일로 확인한다.

```html
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>03. 박스 모델 — width와 실제 상자 너비</title>
    <style>
        .box { width: 100px; padding: 10px; border: 1px solid red; margin: 10px; }
        .included { box-sizing: border-box; }
    </style>
</head>
<body>
    <h1>상자 너비 계산</h1>
    <div class="box">내용 기준</div>
    <div class="box included">테두리 포함</div>
</body>
</html>
```

첫 상자의 테두리까지 너비는 100+20+2=122px다. 둘째는 100px 안에 여백·테두리가 들어가 내용 너비가 78px다. margin은 각각 바깥 10px이며 테두리까지 너비에 더하지 않았다. 둘째에 두 클래스가 함께 있으므로 .box의 기본 선언과 .included의 변경이 같이 적용된다.

<a id="my-code"></a>

## 4. 내가 작성한 코드를 따라 읽기

아래는 **내 원본 발췌**다. 주석의 표현도 원문대로 두었다. 설명에서 교정한 내용을 원본에 이미 수정한 것처럼 읽지 않는다.

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_html/css/asset/css/03_box.css` 102–117행

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

**발췌 바로 풀이:** 선언과 계산 결과가 같다. 내 주석은 width의 기준이 바뀐다는 점을 설명한다. “margin까지 width 안에 들어간다”로 확대하면 안 된다.

내 첫 .box는 내용 300px, padding 0, border 좌우 1px씩이므로 302px다. .box.box-sizing은 300px에 padding 좌우 50px씩과 border를 포함하므로 내용이 198px다. 내 주석은 width 기준 전환을 설명한 점이 좋다. 주석의 오타 boder-box를 실제 속성값으로 따라 쓰지 않도록 주의한다. 실제 선언은 border-box로 올바르게 작성되어 있다.

<a id="connections"></a>

## 5. 파일·요소·값이 연결되는 흐름

HTML class="box box-sizing" → 두 클래스 규칙 결합 → box-sizing 기준 선택 → 내용·여백·테두리 계산 순서다. 원본 div.second는 축약 선언을 여러 번 썼으므로 마지막 활성값을 읽는다. width 150·height 200, padding 30, border 1이면 테두리까지 212×262px다. 이전 선언들의 여백을 모두 누적하지 않는다.

<a id="review"></a>

## 6. 잘한 점·아쉬운 점·개선 방향

**잘한 점:** 같은 기본 클래스에 차이만 추가하여 계산 기준을 비교한다. **수업용 단순화:** 같은 속성을 연속으로 바꾸는 코드가 실험 기록으로 남아 있다. **개선 방향:** 공유할 결과물에서는 최종 의도를 남기고, 실험값은 별도 기록으로 구분하면 실제 적용값을 빨리 찾을 수 있다. border-box가 margin까지 포함한다고 설명하면 잘못이다.

제안은 원본을 수정한 결과가 아니다. **실제 오류**, **관찰을 위한 수업용 단순화**, **목적에 따라 가능한 선택**을 구별한다. 단지 짧게 쓰거나 최신 기능을 쓴다고 더 좋은 코드는 아니다.

<a id="teacher"></a>

## 7. 강사님 코드가 도움이 되는 비교



양쪽 .box와 .box-sizing의 활성 선언·계산 결과가 같아 강사님 원문은 중복 인용하지 않는다. 원본 첫 상자는 padding이 없고 두 번째에만 50px가 있으므로 단순히 ‘둘 다 같은 크기에 옵션만 다르다’고 읽으면 안 된다.

<a id="results"></a>

## 8. 결과를 예상하고 한 가지 바꾸기

아래는 **명시한 조건에서의 코드 기준 예상**이다. 이번 편집에서 실제 브라우저 렌더링을 재실행했다는 기록과 구별한다. 매 실험은 원래 예제로 돌아가 한 조건만 바꾼다.

| 한 가지 변경 | 테두리까지 너비 | 내용 너비 |
| --- | --- | --- |
| 원래 예제 첫 box | 122px | 100px |
| 첫 box padding만 20px | 142px | 100px |
| 원래 예제 둘째 padding만 20px | 100px | 58px |
| 원래 둘째 margin만 30px | 100px | 78px |

원본 .width는 width:70%, min-width:400px, max-width:600px다. 부모 내용 너비 500px이면 350 대신 최소 400, 1000px이면 700 대신 최대 600이 사용된다. content-box 테두리 2px가 양쪽에 더 붙는 조건도 구분한다. 최소 너비보다 화면이 작으면 %를 썼어도 넘칠 수 있다. 원본 이미지 200×200에 radius 50%는 원을 만들지만 가로세로가 다르면 타원일 수 있다.

<a id="tips"></a>

## 9. 추가로 알면 좋은 것과 출처

> 💡 **TIP · 수업 범위 밖:** 논리 방향 속성·border-image 상세는 선택 학습이다. 먼저 현재 예제의 물리적 네 방향과 크기 기준을 정확히 계산한다.



이 절의 확장은 기본 문제의 필수 조건이 아니다. 2절의 📚 출처는 배운 기능의 설명을 확인하는 근거이며, 출처가 있다는 이유로 모두 수업 밖 내용인 것은 아니다.

<a id="practice"></a>

## 10. 복습과 빠른 정리

1. width200·padding20·border2인 content-box의 테두리 너비는?
2. border-box로만 바꾸면 내용 너비는?
3. margin도 width 안에 들어가는가?

<details>
<summary>짧은 풀이 — 먼저 답한 뒤 확인</summary>

244px다. border-box에서는 테두리까지 200px이고 내용은 156px다. margin은 포함되지 않는다.

</details>

| 용어 | 영역 |
| --- | --- |
| content | 내용 |
| padding | 테두리 안쪽 여백 |
| border | 경계 |
| margin | 테두리 바깥 간격 |

[장별 연습문제](실습/연습문제/03_CSS_박스모델_연습문제.md)에서 예상·설명·수정을 이어 간다. 다음은 [마진과 가운데 정렬](03-02_CSS_마진과_가운데정렬.md)이다.

<!-- 이전 색인 이동 주소 보존 -->
<a id="css-14"></a>
<a id="css-18"></a>
<a id="css-33"></a>
<a id="css-39"></a>
<a id="css-4"></a>
<a id="css-40"></a>
<a id="css-48"></a>
<a id="css-50"></a>
<a id="css-6"></a>
<a id="css-62"></a>
<a id="css-9"></a>
<a id="index-section-101"></a>
<a id="index-section-68"></a>
<a id="index-section-81"></a>
<a id="section-1"></a>
<a id="section-2"></a>
<a id="section-3"></a>
<a id="section-4"></a>

이전 절 주소로 왔다면 [이 장의 목차](#chapter-toc)에서 현재 설명을 찾는다.
