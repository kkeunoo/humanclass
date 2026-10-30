# 04. display — 같은 요소를 어떤 방식으로 배치할까 — 연습문제

[본문](../../04_CSS_Display와_요소배치.md) · [문제 목차](README.md)

이 파일은 실제 수업 기능을 바탕으로 **새로 구성한 연습문제**다. 강사님이 내주신 원본 퀴즈와 구분한다. 결과 예상 → 이유 설명 → 수정·검증 순서로 풀고, 각 정답은 먼저 생각한 뒤 펼친다.

## 목표와 실행 조건

block·inline·inline-block의 줄 배치와 크기 적용을 구분한다. inline-block의 공백·baseline, HTML 중첩 오류를 설명한다.

본문의 [전체 실행 파일](../책형_복습/04_CSS_Display와_요소배치.html)을 별도로 열어 실험한다. 아래 조각을 다른 원본 CSS에 그대로 덧붙이면 기존 규칙과 경쟁할 수 있다. 실험 전 원래 파일을 보존하고 매번 한 조건만 바꾼다. 브라우저에서 확인한 것과 코드 기준 예상을 따로 적는다.

## 문제 1. 작은 예제의 결과 예상

**새 설명 예제의 CSS와 body 조각**이다. 전체 파일은 위 링크에 있다. 어떤 요소가 선택되고 무엇이 어떻게 보일지 적는다. 크기가 있으면 내용·테두리 기준도 구분한다.

```css
        .row { font-size: 0; border: 1px solid black; }
        .item { display: inline-block; width: 100px; height: 50px; border: 1px solid red; vertical-align: top; font-size: 16px; }
        .block { display: block; width: 100px; border: 1px solid blue; }
```

```html
    <h1>한 줄과 새 줄</h1>
    <div class="row">
        <div class="item">A</div>
        <div class="item">B<br>둘째 줄</div>
    </div>
    <div class="block">C</div>
    <div class="block">D</div>
```

<details>
<summary>힌트와 풀이</summary>

**힌트:** 선택자 → 속성 → 기준값 → 상태 순서로 읽는다. 주석은 실행하지 않는다.

각 item은 내용100+테두리2=102px다. 공간이 충분하면 A·B가 나란히 놓이며 윗부분을 맞춘다. 부모 font-size0은 요소 사이 줄바꿈 공백의 글자 폭을 줄이고, 자식은16px로 복원한다. C·D는 너비가100이어도 일반 block이어서 각각 다음 줄이다. 좁은 화면에서 한 줄 수용 여부는 부모 공간까지 확인한다.

</details>

## 문제 2. 비슷한 개념을 설명하기

1. block 너비를100px로 줄이면 다음 block이 자동 옆으로 붙는가?
2. 일반 span과 img의 width 규칙을 똑같이 설명해도 되는가?
3. inline-block 공백은 늘4px인가?

숫자나 속성 이름만 적지 말고 왜 그런지 문장으로 설명한다. 필요한 전제도 함께 쓴다.

<details>
<summary>풀이와 원본으로 돌아갈 지점</summary>

자동으로 옆으로 붙지 않는다. 일반 비대체 inline과 대체 요소는 구분한다. 공백 폭은 글꼴·크기 등 조건에 따라 달라진다.

실제 작성 기록에서 확인할 부분은 다음과 같다.

내 parent3의 자식은 width100·padding50·border1이므로 실제너비202px다. font-size0과 자식16px 복원, vertical-align:top은 서로 다른 문제를 다룬다. 앞의 것은 글자 공백, 뒤의 것은 inline-block의 수직 정렬이다. baseline은 글자를 놓는 기준선이며 내용 줄 수 등에 따라 상자 정렬이 예상과 다르게 보일 수 있다. ‘공백4px’는 당시 관찰값이며 항상 같은 상수는 아니다.

</details>

## 문제 3. 한 조건을 바꾸고 확인하기

먼저 **부모 font-size만16px**를 적용했을 때의 차이를 예상한다. 예상한 뒤 실제 파일의 해당 선언 하나를 바꾸고 저장·새로고침하여 비교한다. 이후 나머지 변경도 한 번에 하나씩 실험한다. 전환·hover는 상태 변화 전후를, 너비 조건은 경계값을 구분한다.

<details>
<summary>변경 실험의 예상과 점검</summary>

| 한 가지 변경 | 예상 | 확인 원리 |
| --- | --- | --- |
| 부모 font-size만16px | 공백 폭 생길 수 있음 | HTML 공백 텍스트 |
| 원래 item display만block | 각각 새 줄 | 배치 방식 |
| 원래 item width만200px | 실제202px | 박스 계산 |
| 원래 vertical-align만baseline | 내용 기준선에 맞춤 | 수직 정렬 |

공백을 제거해도 부모200px에 원본202px 상자 두 개가 들어갈 수는 없다. 글자 공백과 박스 너비 부족을 따로 계산한다. -webkit- 접두 표기를 ‘숨겨진 옵션’이라고 외우지 말고 해당 속성의 지원·표준 여부를 따로 확인한다.

</details>

## 채점과 복습

| 점검 | 확인할 것 |
| --- | --- |
| 예측 | 실행 전에 결과·전제를 적었는가? |
| 근거 | 태그·선택자·속성·기준으로 설명했는가? |
| 수정 | 원래 코드에서 한 조건만 바꾸었는가? |
| 비교 | 예상과 실제 확인을 구분했는가? |

결과가 맞아도 이유를 설명하지 못했다면 [본문의 개념과 내 원본 풀이](../../04_CSS_Display와_요소배치.md)로 돌아간다. 이 문제는 수업 범위 안에서 풀 수 있으며 하단 TIP의 새 기능이 필수 답안은 아니다.
