# 10. float와 clear — 글 감싸기와 다음 흐름 — 연습문제

[본문](../../10_CSS_Float와_Clear.md) · [문제 목차](README.md)

이 파일은 실제 수업 기능을 바탕으로 **새로 구성한 연습문제**다. 강사님이 내주신 원본 퀴즈와 구분한다. 결과 예상 → 이유 설명 → 수정·검증 순서로 풀고, 각 정답은 먼저 생각한 뒤 펼친다.

## 목표와 실행 조건

float와 absolute·inline-block의 차이를 구분한다. 후행 clear와 가상 요소 clearfix가 부모 높이에 주는 영향을 추적한다.

본문의 [전체 실행 파일](../책형_복습/10_CSS_Float와_Clear.html)을 별도로 열어 실험한다. 아래 조각을 다른 원본 CSS에 그대로 덧붙이면 기존 규칙과 경쟁할 수 있다. 실험 전 원래 파일을 보존하고 매번 한 조건만 바꾼다. 브라우저에서 확인한 것과 코드 기준 예상을 따로 적는다.

## 문제 1. 작은 예제의 결과 예상

**새 설명 예제의 CSS와 body 조각**이다. 전체 파일은 위 링크에 있다. 어떤 요소가 선택되고 무엇이 어떻게 보일지 적는다. 크기가 있으면 내용·테두리 기준도 구분한다.

```css
        .parent { border: 1px solid black; }
        .left { float: left; width: 100px; height: 60px; background-color: lightblue; }
        .right { float: right; width: 100px; height: 80px; background-color: pink; }
        .clearFix:after { content: ""; display: block; clear: both; }
```

```html
    <h1>부모가 감싸는 높이</h1>
    <div class="parent clearFix">
        <div class="left">왼쪽</div>
        <div class="right">오른쪽</div>
    </div>
    <p>그다음 내용</p>
```

<details>
<summary>힌트와 풀이</summary>

**힌트:** 선택자 → 속성 → 기준값 → 상태 순서로 읽는다. 주석은 실행하지 않는다.

충분한 가로 공간에서 자식은 좌우에 놓이고 높이는60·80px다. 후행 가상 박스가 두 float 아래에서 정리되어 부모는 그 높이를 감싼다. 다음 p는 정리된 부모 뒤에 이어진다. class를 지웠을 때의 차이는 부모 높이와 다음 글 흐름을 각각 관찰한다.

</details>

## 문제 2. 비슷한 개념을 설명하기

1. clear는 앞 float를none으로 바꾸는가?
2. clearfix는 어느 요소에 연결하는가?
3. 주석 .test는 현재 실행되는가?

숫자나 속성 이름만 적지 말고 왜 그런지 문장으로 설명한다. 필요한 전제도 함께 쓴다.

<details>
<summary>풀이와 원본으로 돌아갈 지점</summary>

float 선언 자체는 유지한다. float 자식을 감쌀 부모에 clearFix를 연결한다. 주석 .test는 실행되지 않는다.

실제 작성 기록에서 확인할 부분은 다음과 같다.

내 clearFix:after는 content 빈 문자열·display block·clear both로 구성된다. 뒤의 .test는 주석이므로 test class를 붙였다는 사실만으로 실행된다고 읽지 않는다. 함께 인용한 HTML은 부모에 clearFix를 주고 안쪽 두 float를 배치한 연결이다. 내 ‘초기화’ 메모는 자식 float를 지우는 것이 아니라 뒤 흐름을 정리한다는 뜻으로 고쳐 읽는다.

</details>

## 문제 3. 한 조건을 바꾸고 확인하기

먼저 **부모 clearFix class만제거**를 적용했을 때의 차이를 예상한다. 예상한 뒤 실제 파일의 해당 선언 하나를 바꾸고 저장·새로고침하여 비교한다. 이후 나머지 변경도 한 번에 하나씩 실험한다. 전환·hover는 상태 변화 전후를, 너비 조건은 경계값을 구분한다.

<details>
<summary>변경 실험의 예상과 점검</summary>

| 한 가지 변경 | 예상 | 관찰 대상 |
| --- | --- | --- |
| 부모 clearFix class만제거 | 부모 높이가 float를 기대대로 못 감쌀 수 있음 | 경계·다음글 |
| 원래 right 높이만120px | 정리된 부모가 더 길어짐 | 더큰float |
| 원래 left float만none | 일반흐름 요소로 바뀜 | clear와다른수정 |

clearFix의 대소문자와 실제 부모 적용을 먼저 확인한다. ‘다음 글이 아래에 있다’는 관찰만으로 자식 float가 사라졌다고 결론 내리지 않는다. 브라우저에서 각 요소의 현재 float도 나눠 본다.

</details>

## 채점과 복습

| 점검 | 확인할 것 |
| --- | --- |
| 예측 | 실행 전에 결과·전제를 적었는가? |
| 근거 | 태그·선택자·속성·기준으로 설명했는가? |
| 수정 | 원래 코드에서 한 조건만 바꾸었는가? |
| 비교 | 예상과 실제 확인을 구분했는가? |

결과가 맞아도 이유를 설명하지 못했다면 [본문의 개념과 내 원본 풀이](../../10_CSS_Float와_Clear.md)로 돌아간다. 이 문제는 수업 범위 안에서 풀 수 있으며 하단 TIP의 새 기능이 필수 답안은 아니다.
