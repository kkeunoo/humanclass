# 12 CSS Transition과 상태변화 — 연습문제

[해당 본문](../../12_CSS_Transition과_상태변화.md) · [장별 문제 목차](README.md)

**새로 구성한 문제**다. 먼저 강사님·내 코드의 실제 결과를 읽고 아래 조건을 직접 구현하거나 계산하자.

## 문제

hover에 배경색을 바꾸고 마우스를 뗄 때도 부드럽게 돌아오게 하자.

**확인 기준:** 마우스를 올릴 때와 뗄 때 각각 즉시 바뀌는지, 시간에 걸쳐 바뀌는지 관찰한다. 배경색의 시작값도 정한다.

<details>
<summary>해설 — 먼저 풀고 펼치기</summary>

```css
.button { background-color: skyblue; transition: background-color 0.3s; }
.button:hover { background-color: navy; }
```
기본 상태에 전환을 두면 들어갈 때와 돌아올 때 모두 같은 시간 설정을 사용한다. hover 안에만 전환을 두면 마우스를 뗄 때는 그 규칙이 더 이상 적용되지 않아 돌아오는 모습이 달라질 수 있다.

</details>

## 원본과 연결하기

강사님·내 원본은 hover 안에 `transition`을 둔 사례다. 위 정답은 **그 원본을 그대로 발췌한 코드가 아니라**, 양방향 전환을 확인하도록 위치를 바꾼 교정 예제다.
