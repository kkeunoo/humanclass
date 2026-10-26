# 13. transform — 자리는 그대로, 보이는 모양 바꾸기

[CSS 목차](README.md)

transform으로 옮기거나 확대해도 주변 요소가 새 크기에 맞춰 일반 흐름을 다시 배치하는 것은 아니다. 큰 모양이 옆 요소와 겹칠 수 있다.

<!-- chapter-toc -->

- [1. 원본의 세 함수](#section-1)
- [2. 크기를 모를 때 중앙에 놓기](#section-2)
- [복습](#section-3)

<a id="section-1"></a>

## 1. 원본의 세 함수

| 원본 함수 | 동작 |
| --- | --- |
| translate(50%,50%) | 자신의 기준 상자 너비·높이의 절반만큼 이동 |
| scaleX(1.5) | 가로 방향 1.5배 |
| rotate(-30deg) | 원본의 기본 좌표에서 반시계 방향 30도 회전 |

양쪽 box는 content 100×100px, border 1px다. 이 일반 HTML 상자의 translate 50%는 테두리까지 102px의 절반인 51px다. 부모의 50%인 left·top과 다른 기준이다.

### 강사님 코드

`13_transform.html` 31~33행 — **원본 발췌**

```css
        .total:hover {
            transform: translate(50%, 50%) scale(1.5) rotate(-30deg);
        }
```

### 내 코드

`13_tranform.html` 35~38행 — **원본 발췌**

```css
            .total:hover {
                /* transform: rotate(30deg); */
                transform: translate(50%, 50%) scaleX(1.5) rotate(-30deg);
            }
```

강사님은 scale(1.5)로 가로·세로를 함께 키우고 나는 scaleX(1.5)로 가로만 키운다. **같은 결과가 아니다.** 두 축 확대를 원하면 강사님, 가로만 확대하려면 내 선언이 목적에 맞는다. 내 파일명은 원본 철자 그대로 `13_tranform.html`이다.

함수의 순서를 바꾸면 합성 결과가 달라질 수 있다. `translate(...) rotate(...)`와 `rotate(...) translate(...)`를 같은 이동·회전 결과라고 읽지 않는다. [transform 표준](https://www.w3.org/TR/css-transforms-1/)

<a id="section-2"></a>

## 2. 크기를 모를 때 중앙에 놓기

### 강사님 코드

`13_transform.html` 42~52행 — **원본 발췌**

```css
        .parent .child {
            border: 1px solid blueviolet;
            width: 30%;
            height: 30%;

            position: absolute;
            top: 50%;
            left: 50%;

            transform: translate(-50%, -50%);
        }
```

### 내 코드

`13_tranform.html` 48~59행 — **원본 발췌**

```css
            .parent .child {
                border: 1px solid blue;
                width: 30%;
                height: 30%;

                position: absolute;

                top: 50%;
                left: 50%;

                transform: translate(-50%, -50%);
            }
```

테두리 색 외에 배치 원리는 같다. 부모는 position:relative다. top·left의 50%는 부모 기준으로 자식의 왼쪽 위를 중앙까지 옮기고, translate의 -50%는 자식 자신의 크기 절반만큼 되돌린다. 그 결과 자식의 중심이 부모 중심과 맞는다.

앞 position 장의 calc 예제처럼 자식 width의 절반을 숫자로 직접 빼지 않아도 된다. 다만 이 원본은 margin이 없는 단순 상자 조건이다.

<a id="section-3"></a>

## 복습

top:50%; left:50%만 남기고 transform을 지우면 무엇이 중앙에 올까?

<details>
<summary>해설</summary>

자식의 중심이 아니라 왼쪽 위 기준점이 부모 중앙에 온다. 자식 크기 절반을 되돌리는 단계가 빠졌기 때문이다.

</details>

**추가로 알면 좋은 것:** 3D 변환·개별 translate/rotate/scale 속성·복잡한 모달 배치는 별도 확장이다.

<!-- legacy-migration -->

<a id="css-7"></a>
<a id="css-4"></a>
<a id="index-section-74"></a>
<a id="css-44"></a>
<a id="css-37"></a>
<a id="css-18"></a>
<a id="css-13"></a>
<a id="css-8"></a>

### 이전 색인 링크 안내

이전 절 주소를 보존한 이동 안내다. 옛 절 번호와 현재 절은 같지 않다. [현재 CSS 목차](README.md)에서 수업 본문과 **추가로 알면 좋은 것**을 구분해 찾는다.
