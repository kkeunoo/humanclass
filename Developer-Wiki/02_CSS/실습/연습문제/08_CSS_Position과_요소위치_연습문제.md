# 08. position — 이동의 기준과 원래 자리 — 연습문제

[본문](../../08_CSS_Position과_요소위치.md) · [문제 목차](README.md)

이 파일은 실제 수업 기능을 바탕으로 **새로 구성한 연습문제**다. 강사님이 내주신 원본 퀴즈와 구분한다. 결과 예상 → 이유 설명 → 수정·검증 순서로 풀고, 각 정답은 먼저 생각한 뒤 펼친다.

## 목표와 실행 조건

static·relative·absolute·fixed·sticky의 기준을 구별한다. 원본 calc·CSS 변수·겹침 순서를 조건과 함께 읽는다.

본문의 [전체 실행 파일](../책형_복습/08_CSS_Position과_요소위치.html)을 별도로 열어 실험한다. 아래 조각을 다른 원본 CSS에 그대로 덧붙이면 기존 규칙과 경쟁할 수 있다. 실험 전 원래 파일을 보존하고 매번 한 조건만 바꾼다. 브라우저에서 확인한 것과 코드 기준 예상을 따로 적는다.

## 문제 1. 작은 예제의 결과 예상

**새 설명 예제의 CSS와 body 조각**이다. 전체 파일은 위 링크에 있다. 어떤 요소가 선택되고 무엇이 어떻게 보일지 적는다. 크기가 있으면 내용·테두리 기준도 구분한다.

```css
        :root { --box-color: brown; }
        .parent { position: relative; width: 300px; height: 200px; border: 1px solid black; }
        .child { position: absolute; width: 100px; height: 50px; top: 30px; left: calc(50% - 50px); background-color: var(--box-color); }
        .relative { position: relative; top: 10px; background-color: lightblue; }
```

```html
    <h1>기준과 자리</h1>
    <div class="parent"><div class="child">absolute</div><p>일반 내용</p></div>
    <div class="relative">아래로10px 보임</div>
    <p>이 문단의 자리는 relative 이동만으로 당겨지지 않음</p>
```

<details>
<summary>힌트와 풀이</summary>

**힌트:** 선택자 → 속성 → 기준값 → 상태 순서로 읽는다. 주석은 실행하지 않는다.

parent의 relative가 자식의 기준을 만든다. 내용300px, padding0 조건에서 left는150-50=100px이고 top은30px다. child에는 별도 border가 없어100px 너비 전체의 중심을 맞췄다. absolute는 일반 흐름에서 빠져 p를 밀어 자리를 확보하지 않는다. relative 예제는 보이는 위치만10px 내려가 다음 문단의 원래 배치는 유지되므로 겹칠 가능성도 구분한다.

</details>

## 문제 2. 비슷한 개념을 설명하기

1. relative는 원래 자리를 없애는가?
2. absolute 부모의 자식은 전부 absolute여야 하는가?
3. top0 다음30이면 최종은?

숫자나 속성 이름만 적지 말고 왜 그런지 문장으로 설명한다. 필요한 전제도 함께 쓴다.

<details>
<summary>풀이와 원본으로 돌아갈 지점</summary>

relative의 배치 자리는 남는다. absolute 안의 자식은 일반 흐름도 가능하다. 같은 조건의 뒤 top30px가 적용된다.

실제 작성 기록에서 확인할 부분은 다음과 같다.

내 .parent .absolute는 top0 뒤 top30이 있어 최종30px다. 주석의 ‘하위 자식까지 absolute’는 잘못된 일반화다. 두 번째 발췌의 calc는400/2-100/2=150px를 계산하고 --box-color를 root에 정의해 p1·c1에서 재사용한다. +·- 주변 공백 메모는 실제 작성에 도움이 된다. 원본 자식은 테두리까지102px이므로 엄밀한 정중앙은100px 내용만 빼는 계산과1px 차이가 있다.

</details>

## 문제 3. 한 조건을 바꾸고 확인하기

먼저 **child top만50px**를 적용했을 때의 차이를 예상한다. 예상한 뒤 실제 파일의 해당 선언 하나를 바꾸고 저장·새로고침하여 비교한다. 이후 나머지 변경도 한 번에 하나씩 실험한다. 전환·hover는 상태 변화 전후를, 너비 조건은 경계값을 구분한다.

<details>
<summary>변경 실험의 예상과 점검</summary>

| 한 가지 변경 | 예상 | 기준 |
| --- | --- | --- |
| child top만50px |20px 더 아래 | 같은 포함 블록 |
| 원래 parent width만400px | left150px |50% 기준 변경 |
| 원래 --box-color만blue | child파랑 | var참조 |
| 원래 relative top만0 | 원래 위치 표시 | 흐름 자리는 유지 |

엉뚱한 위치로 가면 top 숫자를 고치기 전에 기준 조상을 찾는다. 스크롤하면 sticky가 항상 끝까지 고정된다는 가정도 피한다. 테두리를 포함한 중앙 배치는 [transform](../../13_CSS_Transform과_요소변형.md)에서 이어 본다.

</details>

## 채점과 복습

| 점검 | 확인할 것 |
| --- | --- |
| 예측 | 실행 전에 결과·전제를 적었는가? |
| 근거 | 태그·선택자·속성·기준으로 설명했는가? |
| 수정 | 원래 코드에서 한 조건만 바꾸었는가? |
| 비교 | 예상과 실제 확인을 구분했는가? |

결과가 맞아도 이유를 설명하지 못했다면 [본문의 개념과 내 원본 풀이](../../08_CSS_Position과_요소위치.md)로 돌아간다. 이 문제는 수업 범위 안에서 풀 수 있으며 하단 TIP의 새 기능이 필수 답안은 아니다.
