# 08. position — 이동의 기준과 원래 자리

[CSS 목차](README.md) · [읽기 안내](00_CSS_V3_동작_백과_읽기법.md)

top30px를 읽으면 무엇의 위에서30px인지부터 묻는다. 원래 배치 자리를 유지하는가도 별도 질문이다. 두 질문으로 relative와 absolute의 차이를 따라갈 수 있다.

<a id="chapter-toc"></a>

**이 장의 목차:** [목표](#learn) · [개념](#concepts) · [작은 예제](#example) · [내 코드](#my-code) · [연결](#connections) · [평가](#review) · [비교](#teacher) · [결과·실험](#results) · [TIP·출처](#tips) · [복습](#practice)

<a id="learn"></a>

## 1. 이 장에서 배울 것

static·relative·absolute·fixed·sticky의 기준을 구별한다. 원본 calc·CSS 변수·겹침 순서를 조건과 함께 읽는다.

이번 장의 개념과 원본 기능은 수업 범위다. 원본에 없는 선택 기능은 9절 TIP으로 구분한다. 결과를 읽을 때는 선택된 요소·속성·기준값·실행 상태를 함께 적는다.

<a id="concepts"></a>

## 2. 무엇이며, 왜 필요한가

일반 흐름은 요소들이 통상적인 순서와 배치 규칙으로 자리를 차지하는 상태다. relative는 원래 자리를 유지하고 거기서 보이는 위치를 옮긴다. absolute는 일반 흐름에서 빠지고 기준이 되는 포함 블록에 맞춰 배치한다. 수업에서는 가까운 position이 static이 아닌 조상이 있는지 먼저 찾는다. 그런 조상이 없다고 단순히 body 박스 기준이라고 외우지는 않는다. 초기 포함 블록을 기준으로 하는 경우와 구분한다.

| position | 원래 자리 | 이번 수업에서 확인할 기준 |
| --- | --- | --- |
| static | 유지 | 일반 배치, top·left로 이동하지 않음 |
| relative | 유지 | 원래 자기 위치에서 이동 |
| absolute | 일반 흐름에서 빠짐 | 위치 기준 조상·포함 블록 |
| fixed | 일반 흐름에서 빠짐 | 원본에서는 뷰포트 |
| sticky | 흐름에 자리 유지 | 스크롤 경계와 부모 범위 |

absolute를 주면 자식도 전부 absolute여야 한다거나 자동 inline-block이 된다는 설명은 정확하지 않다. 안쪽 자식은 일반 흐름으로 놓을 수 있다. z-index도 모든 부모 관계를 숫자 하나로 뚫는 전역 순위가 아니다.

> 📚 **출처 · 본문 설명 확인:** [W3C 위치 배치](https://www.w3.org/TR/css-position-3/). 설명과 비교 표는 수업 원본을 바탕으로 새로 풀어 썼다. 외부 원문을 직접 인용한 문장은 아니다. 확인일: 2026-10-28.

<a id="example"></a>

## 3. 작은 예제로 먼저 이해하기

**새 설명 예제 · 전체 파일.** [실행 파일](실습/책형_복습/08_CSS_Position과_요소위치.html)을 브라우저로 연다. 이 예제는 위 style 안에 CSS를 모두 넣어 외부 파일 연결이 필요 없다. 원본 CSS에 붙이면 다른 규칙이 섞일 수 있으므로 먼저 별도 파일로 확인한다.

```html
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>08. position — 이동의 기준과 원래 자리</title>
    <style>
        :root { --box-color: brown; }
        .parent { position: relative; width: 300px; height: 200px; border: 1px solid black; }
        .child { position: absolute; width: 100px; height: 50px; top: 30px; left: calc(50% - 50px); background-color: var(--box-color); }
        .relative { position: relative; top: 10px; background-color: lightblue; }
    </style>
</head>
<body>
    <h1>기준과 자리</h1>
    <div class="parent"><div class="child">absolute</div><p>일반 내용</p></div>
    <div class="relative">아래로10px 보임</div>
    <p>이 문단의 자리는 relative 이동만으로 당겨지지 않음</p>
</body>
</html>
```

parent의 relative가 자식의 기준을 만든다. 내용300px, padding0 조건에서 left는150-50=100px이고 top은30px다. child에는 별도 border가 없어100px 너비 전체의 중심을 맞췄다. absolute는 일반 흐름에서 빠져 p를 밀어 자리를 확보하지 않는다. relative 예제는 보이는 위치만10px 내려가 다음 문단의 원래 배치는 유지되므로 겹칠 가능성도 구분한다.

<a id="my-code"></a>

## 4. 내가 작성한 코드를 따라 읽기

아래는 **내 원본 발췌**다. 주석의 표현도 원문대로 두었다. 설명에서 교정한 내용을 원본에 이미 수정한 것처럼 읽지 않는다.

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_html/css/asset/css/08_position.css` 36–54행

```css
.parent .absolute {
    background: #f007;

    /* 
        원래 내가 가지고 있던 공간이 없어지며 이동함 
        부모중에 relative 등 static(정적/고정된) 아닌 것 기준으로 이동
        - 이러한 부모가 없을 경우 body 기준 
        absolute는 주었을 때 inline-block으로 바뀜
    */
    position: absolute;

    top: 0;
    left: 0;

    /* 남발하게 될 경우 모바일 등 브라우저 크기가 바뀌면 대응하기 어려움 
    하나를 absolute를 주면 하위 자식까지 absolute를 주어야 함*/
    top: 30px;
    /* left: 300px; */
}
```

**발췌 바로 풀이:** 기준 조상이 없을 때 단순히 body 박스라고 외우지 않고 초기 포함 블록과 구분한다. absolute는 자동 inline-block이라는 설명과도 다르며, 그 안의 자식을 모두 absolute로 만들 필요는 없다. 원래 자리·포함 블록·자식 배치를 각각 판단한다.

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_html/css/asset/css/08_position.css` 179–196행

```css
    /* 가운데 정렬을 하려면 부모/2-자식/2 
    더하기나 빼기는 앞 뒤로 띄어쓰기 해야 함*/
    top: calc( 400px/2 - 100px/2 );
    left: calc( 50% - (100px/2) );
}

/* --box-color라는 변수를 지정해두고 쓸 수 있음 */
:root {
    --box-color : brown;
}

.p1 {
    background: var(--box-color);
}
.c1 {
    /* background: pink; */
    background: var(--box-color);
}
```

**발췌 바로 풀이:** 내 주석은 calc의 덧셈·뺄셈 주변 공백과 변수 역할을 더 명확히 적었다. **calc·:root·--변수·var의 이 기본 사용은 본문**이다. 다크 모드·디자인 토큰 체계는 별도 확장이다.

내 .parent .absolute는 top0 뒤 top30이 있어 최종30px다. 주석의 ‘하위 자식까지 absolute’는 잘못된 일반화다. 두 번째 발췌의 calc는400/2-100/2=150px를 계산하고 --box-color를 root에 정의해 p1·c1에서 재사용한다. +·- 주변 공백 메모는 실제 작성에 도움이 된다. 원본 자식은 테두리까지102px이므로 엄밀한 정중앙은100px 내용만 빼는 계산과1px 차이가 있다.

<a id="connections"></a>

## 5. 파일·요소·값이 연결되는 흐름

HTML 부모의 rel class → position relative → absolute 포함 블록 기준 → top·left의 마지막 활성값 → 테두리 포함 크기 순서다. root의 --box-color → var 참조 → 두 배경 적용 흐름도 그린다. sticky는 top0 뒤50이므로 현재 경계50px이며 붙기 전 자리·스크롤 영역·부모 끝을 확인한다. 원본 fixed의 right10·bottom10 링크는 문서 스크롤 중 뷰포트 모서리에 남는 상황을 실험한다.

<a id="review"></a>

## 6. 잘한 점·아쉬운 점·개선 방향

**잘한 점:** calc 계산과 변수 재사용 이유를 남겼다. **아쉬운 점:** body 기준·자동 inline-block·자식 전부 absolute라는 메모는 고쳐야 한다. **개선 방향:** 전체 본문 배치보다 배지·겹침처럼 목적이 맞는 곳에 위치 배치를 쓰고, 기준 조상과 크기 전제를 함께 적는다. 모든 absolute가 나쁜 것이 아니라 남발하면 크기 변화에 대응하기 어려울 수 있다.

제안은 원본을 수정한 결과가 아니다. **실제 오류**, **관찰을 위한 수업용 단순화**, **목적에 따라 가능한 선택**을 구별한다. 단지 짧게 쓰거나 최신 기능을 쓴다고 더 좋은 코드는 아니다.

<a id="teacher"></a>

## 7. 강사님 코드가 도움이 되는 비교



양쪽의 핵심 위치·calc·변수 선언은 같아 중복 인용을 생략한다. 메뉴 hover의 submenu top은 강사님-1px, 나는1px라 이동 방향이 반대다. 포인터가 조건을 벗어나면 hover가 사라지는 실험으로, 완성된 메뉴 기능으로 평가하지 않는다. 같은 맥락의 z1·z2·z3 값2·300·99라면2번 상자가 앞이지만 다른 겹침 맥락까지 일반화하지 않는다.

<a id="results"></a>

## 8. 결과를 예상하고 한 가지 바꾸기

아래는 **명시한 조건에서의 코드 기준 예상**이다. 이번 편집에서 실제 브라우저 렌더링을 재실행했다는 기록과 구별한다. 매 실험은 원래 예제로 돌아가 한 조건만 바꾼다.

| 한 가지 변경 | 예상 | 기준 |
| --- | --- | --- |
| child top만50px |20px 더 아래 | 같은 포함 블록 |
| 원래 parent width만400px | left150px |50% 기준 변경 |
| 원래 --box-color만blue | child파랑 | var참조 |
| 원래 relative top만0 | 원래 위치 표시 | 흐름 자리는 유지 |

엉뚱한 위치로 가면 top 숫자를 고치기 전에 기준 조상을 찾는다. 스크롤하면 sticky가 항상 끝까지 고정된다는 가정도 피한다. 테두리를 포함한 중앙 배치는 [transform](13_CSS_Transform과_요소변형.md)에서 이어 본다.

<a id="tips"></a>

## 9. 추가로 알면 좋은 것과 출처

> 💡 **TIP · 수업 범위 밖:** transform 등에 의해 위치 기준이 달라지는 전체 경우·isolation·복잡한 겹침 맥락·포털 모달은 추가 학습이다. calc와 CSS 변수의 기본 사용은 실제 원본에 있어 본문이다.



이 절의 확장은 기본 문제의 필수 조건이 아니다. 2절의 📚 출처는 배운 기능의 설명을 확인하는 근거이며, 출처가 있다는 이유로 모두 수업 밖 내용인 것은 아니다.

<a id="practice"></a>

## 10. 복습과 빠른 정리

1. relative는 원래 자리를 없애는가?
2. absolute 부모의 자식은 전부 absolute여야 하는가?
3. top0 다음30이면 최종은?

<details>
<summary>짧은 풀이 — 먼저 답한 뒤 확인</summary>

relative의 배치 자리는 남는다. absolute 안의 자식은 일반 흐름도 가능하다. 같은 조건의 뒤 top30px가 적용된다.

</details>

| 확인 질문 | 볼 것 |
| --- | --- |
| 무엇에서 이동 | 포함 블록·원래 위치 |
| 자리 유지 | relative와absolute구분 |
| 계산 크기 | 내용·테두리 |
| 재사용 값 | --이름·var |

[장별 연습문제](실습/연습문제/08_CSS_Position과_요소위치_연습문제.md)에서 예상·설명·수정을 이어 간다. 다음은 [overflow](09_CSS_Overflow와_스크롤.md)다.

<!-- 이전 색인 이동 주소 보존 -->
<a id="css-10"></a>
<a id="css-14"></a>
<a id="css-18"></a>
<a id="css-23"></a>
<a id="css-31"></a>
<a id="css-34"></a>
<a id="css-45"></a>
<a id="css-47"></a>
<a id="css-48"></a>
<a id="css-50"></a>
<a id="css-71"></a>
<a id="index-section-100"></a>
<a id="index-section-5"></a>
<a id="section-1"></a>
<a id="section-2"></a>
<a id="section-3"></a>
<a id="section-4"></a>

이전 절 주소로 왔다면 [이 장의 목차](#chapter-toc)에서 현재 설명을 찾는다.
