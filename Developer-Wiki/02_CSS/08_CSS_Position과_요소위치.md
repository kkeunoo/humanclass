# 08. position — 어디를 기준으로 옮길까

[CSS 목차](README.md)

top:30px를 만나면 “무엇의 위에서 30px인가?”를 먼저 묻는다. 원본은 LOVE 네 상자로 자리 유지와 위치 기준을 비교한다.

| position | 원본에서 읽을 동작 |
| --- | --- |
| static | 일반 배치. top·left로 이동시키지 않음 |
| relative | 원래 배치 자리를 남기고 원래 위치에서 이동 |
| absolute | 일반 흐름에서 빠지고 기준이 되는 포함 블록에 맞추어 배치 |
| fixed | 원본에서는 뷰포트 기준. 문서를 스크롤해도 같은 위치 |
| sticky | 흐름에 자리를 두고 스크롤 중 지정한 경계에서 붙음 |

**설명용 예:** `position:relative; top:10px`인 상자는 원래 차지하던 자리를 남기고 아래로 10px 보인다. `position:absolute; top:10px`인 상자는 일반 흐름의 원래 자리를 남기지 않으며 위치 기준이 되는 포함 블록의 위에서 10px에 놓인다. 같은 `top`이어도 기준과 주변 상자에 미치는 영향이 다르다.

<!-- chapter-toc -->

- [1. absolute 원본 비교](08_CSS_Position과_요소위치.md#section-1)
- [2. fixed·sticky·겹침](08_CSS_Position과_요소위치.md#section-2)
- [3. calc와 CSS 변수도 실제 원본이다](08_CSS_Position과_요소위치.md#section-3)
- [복습](08_CSS_Position과_요소위치.md#section-4)

<a id="section-1"></a>

## 1. absolute 원본 비교

### 강사님 코드

`asset/css/08_position.css` 31~46행 — **원본 발췌**

```css
.parent .absolute {
    background-color: #f007;

    /*
        내가 가지고 있던 공간이 없어진다
        부모중에 relative 등 static이 아닌 것 기준으로 이동
        - 없으면 body 기준
        자동으로 inline-block으로 바뀐다
    */
    position: absolute;
    top: 0;
    left: 0;

    top: 30px;
    /* left: 300px; */
}
```

HTML에는 relative가 없는 parent와 `class="parent rel"` 두 경우가 있다. 후자는 `.rel { position:relative; }`이므로 absolute 자식의 기준이 된다. top은 뒤에서 30px로 다시 지정되어 최종값이 30px다.

### 내 코드

`asset/css/08_position.css` 36~54행 — **원본 발췌**

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

같은 배치 실험이다. 원본 주석 세 가지를 교정한다.

- 기준 조상이 없으면 단순히 body 박스가 아니라 **초기 포함 블록**을 기준으로 한다. 일반 화면에서는 뷰포트 크기와 연결되는 기준이다.
- absolute·fixed를 주면 자동으로 inline-block이라는 설명은 정확하지 않다. 일반 흐름에서 빠지고 display 계산도 영향을 받는 것으로 구분한다.
- 부모가 absolute여도 모든 자식을 absolute로 만들 필요는 없다. 자식은 안에서 일반 흐름으로 배치할 수 있다.

이 수업은 position이 있는 조상을 기준으로 살펴본다. transform 등으로 기준이 달라지는 추가 경우는 심화로 남긴다. [위치 배치 표준](https://www.w3.org/TR/css-position-3/)

<a id="section-2"></a>

## 2. fixed·sticky·겹침

양쪽 fixed는 right:10px, bottom:10px인 “맨 위로” 링크 상자다. absolute의 bottom/right와 달리 원본에서는 화면 모서리에 붙어 문서 스크롤을 따라간다.

sticky는 top:0 다음 top:50px를 썼으므로 현재 경계는 50px다. 붙기 전의 원래 자리와 부모 범위, 스크롤 영역을 함께 확인한다. “스크롤하면 영원히 화면에 고정”으로 외우지 않는다.

원본의 z1·z2·z3은 relative와 z-index 2·300·99를 함께 사용한다. 같은 겹침 맥락에서 2번이 앞선다. `.rel:hover`의 999는 포인터를 올린 상자의 순서를 바꾼다. 다른 부모의 겹침 맥락까지 숫자 하나로 무조건 뚫는 규칙은 아니다.

메뉴의 `:hover + .submenu`는 강사님 top:-1px, 내 top:1px라 이동 방향이 다르다. 포인터가 메뉴를 벗어나면 선택 조건이 사라지는 실험이므로 완성된 메뉴 기능이라고 부르지 않는다.

<a id="section-3"></a>

## 3. calc와 CSS 변수도 실제 원본이다

### 강사님 코드

`asset/css/08_position.css` 152~165행 — **원본 발췌**

```css
    top: calc( 400px/2 - 100px/2 );
    left: calc( 50% - (100px/2) )
}

:root {
    --box-color : brown;
}

.p1{
    background-color: var(--box-color);
}
.c1{
    background-color: var(--box-color);
}
```

400px의 절반에서 자식 100px의 절반을 빼 150px를 계산한다. `:root`에서 정한 --box-color를 두 상자의 배경에 재사용한다.

### 내 코드

`asset/css/08_position.css` 179~196행 — **원본 발췌**

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

내 주석은 calc의 덧셈·뺄셈 주변 공백과 변수 역할을 더 명확히 적었다. **calc·:root·--변수·var의 이 기본 사용은 본문**이다. 다크 모드·디자인 토큰 체계는 별도 확장이다.

원본의 계산은 자식 content 100px만 빼지만 자식에는 테두리 2px도 있다. 엄밀히 테두리 상자를 가운데 놓으면 102px의 절반인 51px를 빼야 한다. 크기가 바뀌는 경우는 [transform 중앙 정렬](13_CSS_Transform과_요소변형.md)에서 이어 본다.

<a id="section-4"></a>

## 복습

absolute인 O의 원래 자리를 V가 채우지만 relative인 O의 자리는 남는 이유는?

<details>
<summary>해설</summary>

absolute는 일반 흐름에서 빠지고 relative는 배치 자리를 유지한 채 보이는 위치를 옮기기 때문이다.

</details>

**추가로 알면 좋은 것:** isolation·복잡한 stacking context·포털 기반 모달은 기본 위치 실험 이후의 주제다.

<!-- legacy-migration -->

<a id="index-section-5"></a>
<a id="css-71"></a>
<a id="index-section-100"></a>
<a id="css-48"></a>
<a id="css-47"></a>
<a id="css-50"></a>
<a id="css-31"></a>
<a id="css-34"></a>
<a id="css-18"></a>
<a id="css-45"></a>
<a id="css-23"></a>
<a id="css-10"></a>
<a id="css-14"></a>

### 이전 색인 링크 안내

이전 절 주소를 보존한 이동 안내다. 옛 절 번호와 현재 절은 같지 않다. [현재 CSS 목차](README.md)에서 수업 본문과 **추가로 알면 좋은 것**을 구분해 찾는다.

---

[장별 연습문제 풀기](실습/연습문제/08_CSS_Position과_요소위치_연습문제.md)
