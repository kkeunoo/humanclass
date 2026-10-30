# 06. 배경 — 이미지의 크기·반복·위치를 나누기

[CSS 목차](README.md) · [읽기 안내](00_CSS_V3_동작_백과_읽기법.md)

배경 이미지는 요소 뒤에 그려진다. 이미지가 있다고 요소 높이가 자동으로 생기는 것은 아니므로 배경을 담을 상자의 크기부터 확인한다. 그다음 어떤 비율로 어느 위치에 그릴지를 정한다.

<a id="chapter-toc"></a>

**이 장의 목차:** [목표](#learn) · [개념](#concepts) · [작은 예제](#example) · [내 코드](#my-code) · [연결](#connections) · [평가](#review) · [비교](#teacher) · [결과·실험](#results) · [TIP·출처](#tips) · [복습](#practice)

<a id="learn"></a>

## 1. 이 장에서 배울 것

contain·cover·반복·위치를 구분하고, 이미지 크기와 상자 크기를 수치로 비교한다. 외부 CSS의 url 기준과 단축 선언 순서도 읽는다.

이번 장의 개념과 원본 기능은 수업 범위다. 원본에 없는 선택 기능은 9절 TIP으로 구분한다. 결과를 읽을 때는 선택된 요소·속성·기준값·실행 상태를 함께 적는다.

<a id="concepts"></a>

## 2. 무엇이며, 왜 필요한가

contain은 이미지 전체가 영역 안에 들어오도록 비율을 유지하며 맞춘다. cover는 영역을 모두 덮도록 비율을 유지하며 맞춘다. 앞은 빈 공간이, 뒤는 이미지 일부 잘림이 생길 수 있다. 100% 100%는 두 축을 각각 맞춰 원래 비율과 다를 수 있다. no-repeat는 이미지를 반복하지 않는 설정이지 크기 설정이 아니다.

| 속성 | 답하는 질문 |
| --- | --- |
| background-image | 어느 이미지를 그리는가? |
| background-size | 얼마나 크게 그리는가? |
| background-position | 남는 공간에서 어디에 놓는가? |
| background-repeat | 반복해서 채우는가? |
| background-attachment | 스크롤과 배경 기준을 어떻게 연결하는가? |

background-position:center는 요소 자체를 가운데로 이동시키지 않는다. 이미 주어진 영역 안에서 배경 위치를 정한다. background는 여러 배경 속성을 묶는 단축 선언이라, 나중에 쓰면 앞서 준 size 등 생략된 관련 값을 초기화할 수 있다.

> 📚 **출처 · 본문 설명 확인:** [MDN background-size](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-size)와 [background 단축 선언](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background). 설명과 비교 표는 수업 원본을 바탕으로 새로 풀어 썼다. 외부 원문을 직접 인용한 문장은 아니다. 확인일: 2026-10-28.

<a id="example"></a>

## 3. 작은 예제로 먼저 이해하기

**새 설명 예제 · 전체 파일.** [실행 파일](실습/책형_복습/06_CSS_배경이미지와_배경속성.html)을 브라우저로 연다. 이 예제는 위 style 안에 CSS를 모두 넣어 외부 파일 연결이 필요 없다. 원본 CSS에 붙이면 다른 규칙이 섞일 수 있으므로 먼저 별도 파일로 확인한다.

```html
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>06. 배경 — 이미지의 크기·반복·위치를 나누기</title>
    <style>
        .picture { width: 200px; height: 200px; border: 1px solid black; background: lightgray url("assets/lesson-character.png") no-repeat center; background-size: contain; }
        .cover { background-size: cover; }
    </style>
</head>
<body>
    <h1>같은 이미지를 다른 기준으로</h1>
    <p>contain</p><div class="picture"></div>
    <p>cover</p><div class="picture cover"></div>
</body>
</html>
```

같은 폴더의 assets에 원본100×83 PNG를 제공한다. 200×200 내용 영역에서 contain은200×166으로 그려져 위아래 합34px 공간이 남는다. center라 위아래17px씩이다. cover는 높이를200에 맞춰 너비가 약240.96px가 되고 가로 일부가 잘린다. 실제 수업 이미지를 편집하지 않고 배경 표시만 바꾼 예제다. 그림은 장식 실험이며 해당 div 자체에 의미 있는 내용 설명을 의존하지 않는다.

<a id="my-code"></a>

## 4. 내가 작성한 코드를 따라 읽기

아래는 **내 원본 발췌**다. 주석의 표현도 원문대로 두었다. 설명에서 교정한 내용을 원본에 이미 수정한 것처럼 읽지 않는다.

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_html/css/asset/css/06_background.css` 7–22행

```css
    /* repeat 기본값은 x,y축 반복 */
    background-repeat: 
    /*repeat-x*/ 
    /*repeat-y*/ 
    no-repeat;

    /* background-size: 100px 200px; */
    /* background-size: 100% 50%; */
    /* background-size: 100% 100%; */

    /* cover는 원본의 비율을 해치지 않고 전체를 덮어주는 것 */
    /* background-size: cover; */

    /* 꽉 차지 않더라도 사진을 다 보여주고 싶다면 contain */
    background-size: contain;
}
```

**발췌 바로 풀이:** 동작은 같고 내 주석은 비율과 빈 공간을 구분한다. 양쪽 #back1의 이미지는 같은 외부 URL이며 높이는 250px다. 외부 주소가 차단되거나 없어지면 배경을 볼 수 없으므로, 파일을 읽는 실패와 크기 계산을 구분한다.

내 back1은 no-repeat와 contain이 활성값이다. cover와100%100%는 주석 안에 있으므로 동시에 적용되지 않는다. 내 메모는 원본 비율 유지와 빈 공간의 차이를 잘 표현했다. 원본은 높이250px와 외부 이미지 URL을 사용한다. 주소가 현재 로드되지 않는 문제를 크기 계산 오류로 혼동하지 않는다.

<a id="connections"></a>

## 5. 파일·요소·값이 연결되는 흐름

HTML의 높이가 있는 영역 → background 이미지 로딩 → 크기 계산 → 위치 → 반복 여부 순서다. back2는 height80vh·cover·attachment fixed와 overflow auto를 섞고, 안의 p는200vh로 넘치게 만든다. 배경 고정과 내부 내용 스크롤은 각각 다른 속성이다. 원본처럼 별도 기준을 바꾸는 조건이 없는 실험에서 fixed 배경은 뷰포트에 연결되며, 요소 자체의 position:fixed와 다르다. profile은100×100·position center지만 size contain이 주석이라 원본 크기 기준 잘림을 확인한다.

<a id="review"></a>

## 6. 잘한 점·아쉬운 점·개선 방향

**잘한 점:** cover와 contain의 목적을 주석으로 나눴다. **실행 전제:** 외부 자원은 접근 가능해야 보인다. **개선 방향:** 복습 파일은 제공한 로컬 이미지로 반복 관찰하고 원본 외부 자원 성공 여부는 따로 적는다. 설명이 필요한 실제 내용 이미지는 HTML img·alt와 역할을 비교한다.

제안은 원본을 수정한 결과가 아니다. **실제 오류**, **관찰을 위한 수업용 단순화**, **목적에 따라 가능한 선택**을 구별한다. 단지 짧게 쓰거나 최신 기능을 쓴다고 더 좋은 코드는 아니다.

<a id="teacher"></a>

## 7. 강사님 코드가 도움이 되는 비교



양쪽 활성값·외부 이미지·상자 높이가 같아 중복 인용하지 않는다. 단축 background 다음에 size:contain을 두는 원본의 순서는 유지할 가치가 있다. 순서를 뒤집어도 이전 size가 보존된다고 가정하지 않는다.

<a id="results"></a>

## 8. 결과를 예상하고 한 가지 바꾸기

아래는 **명시한 조건에서의 코드 기준 예상**이다. 이번 편집에서 실제 브라우저 렌더링을 재실행했다는 기록과 구별한다. 매 실험은 원래 예제로 돌아가 한 조건만 바꾼다.

| 한 가지 변경 | 예상 | 이유 |
| --- | --- | --- |
| 첫 배경 position만top | 빈 공간이 아래쪽으로 | 크기는 유지 |
| 원래 첫 size만100% 100% | 200×200으로 비율 변경 가능 | 두 축 각각 맞춤 |
| 원래 첫 url만없는파일로 | 이미지가 안 보임 | 크기 아닌 로드 실패 |
| 원래 첫 repeat만repeat | 빈 영역 반복 여부 변화 | size와 독립 |

외부 CSS에서 url("../image/a.png")는 HTML이 아니라 그 CSS 파일 위치 기준이다. 위 작은 예제는 내부 style이어서 HTML 기준으로 assets를 찾는다. 높이 없는 빈 div에는 표시 영역이 없을 수 있으므로 자원만 확인하지 말고 상자 크기도 본다.

<a id="tips"></a>

## 9. 추가로 알면 좋은 것과 출처

> 💡 **TIP · 수업 범위 밖:** 다중 배경·gradient·background-origin/clip·성능 설계 전체는 추가 학습이다. 배경을 많이 썼다는 사실만으로 이런 기능을 배웠다고 보지는 않는다.



이 절의 확장은 기본 문제의 필수 조건이 아니다. 2절의 📚 출처는 배운 기능의 설명을 확인하는 근거이며, 출처가 있다는 이유로 모두 수업 밖 내용인 것은 아니다.

<a id="practice"></a>

## 10. 복습과 빠른 정리

1. 전체 그림을 보여 주려면 contain과 cover 중 무엇인가?
2. center는 상자를 옮기는가?
3. 외부 CSS의 상대 url 기준은?

<details>
<summary>짧은 풀이 — 먼저 답한 뒤 확인</summary>

전체 그림은 contain이 적합하며 빈 공간이 가능하다. center는 영역 안 배경의 위치다. 외부 CSS의 자원 경로는 CSS 파일 위치 기준이다.

</details>

| 목표 | 값·확인 |
| --- | --- |
| 전체 그림 | contain |
| 영역 채우기 | cover |
| 위치 | position |
| 안 보임 | 경로·영역크기·로드 |

[장별 연습문제](실습/연습문제/06_CSS_배경이미지와_배경속성_연습문제.md)에서 예상·설명·수정을 이어 간다. 다음은 [글꼴·텍스트](07_CSS_텍스트와_글꼴.md)다.

<!-- 이전 색인 이동 주소 보존 -->
<a id="css-13"></a>
<a id="css-18"></a>
<a id="css-19"></a>
<a id="css-27"></a>
<a id="css-28"></a>
<a id="css-36"></a>
<a id="index-section-56"></a>
<a id="index-section-76"></a>
<a id="section-1"></a>
<a id="section-2"></a>
<a id="section-3"></a>
<a id="section-4"></a>

이전 절 주소로 왔다면 [이 장의 목차](#chapter-toc)에서 현재 설명을 찾는다.
