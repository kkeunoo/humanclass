# 12. transition — 바뀌는 값 사이에 시간을 주기

[CSS 목차](README.md)

hover는 상태 조건이고 transition은 값이 바뀌는 과정의 시간 설정이다. transition만 적고 바뀔 값이 없으면 원본 같은 크기 변화가 시작되지 않는다.

**설명용 예:** `.box { background-color: blue; transition: background-color .5s; } .box:hover { background-color: red; }`에서는 포인터가 들어갈 때 파랑에서 빨강으로, 나올 때 빨강에서 파랑으로 전환한다. 전환 선언이 기본 상태에 남아 있기 때문이다. 양쪽 수업 원본은 전환 선언을 hover 안에 두었으므로 돌아올 때 결과를 비교해야 한다.

<!-- chapter-toc -->

- [1. hover 안에 있는 transition](12_CSS_Transition과_상태변화.md#section-1)
- [2. 양방향 전환으로 교정하기](12_CSS_Transition과_상태변화.md#section-2)
- [복습](12_CSS_Transition과_상태변화.md#section-3)

<a id="section-1"></a>

## 1. hover 안에 있는 transition

### 강사님 코드

`12_transition.html` 26~33행 — **원본 발췌**

```css
        .box2:hover {
            background-color: red;
            border-radius: 50%;
            width: 200px;
            height: 200px;

            transition: all 0.5s;
        }
```

기본 box는 초록 100×100px다. box2 위에 포인터를 올리면 빨강 200×200px, 둥근 모서리로 바뀌며 0.5초 전환을 사용한다.

### 내 코드

`12_transition.html` 27~34행 — **원본 발췌**

```css
            .box2:hover {
                background: red;
                border-radius: 50%;
                width: 200px;
                height: 200px;
                /* hover자체에 transition을 두면 hover자체에만 먹음 */
                transition: all 0.5s;
            }
```

background-color 대신 background를 쓴 차이가 있지만 이 예제에서는 같은 색 변화다. 내 주석처럼 transition이 hover 규칙에만 있어 **들어갈 때와 나올 때가 대칭적이지 않다.** 밖으로 나오면 기본 상태에 transition이 없어 즉시 돌아간다.

기본 `.box`의 transition 두 줄은 양쪽 모두 주석이다. 그래서 box1은 hover에 transition도 없어 즉시 바뀐다. 주석까지 실행 중이라고 가정하면 두 상자의 차이를 설명할 수 없다.

<a id="section-2"></a>

## 2. 양방향 전환으로 교정하기

```css
/* 설명용 수정: 원본의 .box에 추가하고 :hover 안에서는 제거 */
.box {
    transition: all 0.5s;
}
```

기본 상태에도 전환이 있으면 들어갈 때뿐 아니라 원래 값으로 돌아갈 때도 전환할 수 있다. 원본의 주석 실험인 `transition:width 1s`를 대신 쓰면 너비만 1초 동안 바뀌고 나머지는 즉시 바뀌는 것을 비교할 수 있다.

all은 모든 속성이 반드시 부드럽게 변한다는 보장이 아니라 전환 대상을 넓게 지정하는 값이다. 실제로 전환 가능한 속성과 전·후 값이어야 한다. [transition 표준](https://www.w3.org/TR/css-transitions-1/)

<a id="section-3"></a>

## 복습

box2에서 포인터를 빼면 곧바로 작아진다. 0.5s가 잘못된 단위일까?

<details>
<summary>해설</summary>

아니다. s는 초이며 0.5초는 올바른 값이다. 기본 상태의 transition 선언 유무를 확인한다.

</details>

**추가로 알면 좋은 것:** 지연·속도 함수의 상세 설계, will-change, transition 이벤트, reduced-motion 대응은 추가 학습으로 분리한다.

<!-- legacy-migration -->

<a id="css-4"></a>
<a id="css-28"></a>
<a id="css-33"></a>
<a id="css-19"></a>
<a id="css-43"></a>
<a id="index-section-25"></a>
<a id="index-section-71"></a>
<a id="index-section-77"></a>
<a id="index-section-24"></a>

### 이전 색인 링크 안내

이전 절 주소를 보존한 이동 안내다. 옛 절 번호와 현재 절은 같지 않다. [현재 CSS 목차](README.md)에서 수업 본문과 **추가로 알면 좋은 것**을 구분해 찾는다.

---

[장별 연습문제 풀기](실습/연습문제/12_CSS_Transition과_상태변화_연습문제.md)
