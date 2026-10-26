# 15. Flexbox — 부모의 축과 자식의 크기 나누어 읽기

[CSS 목차](README.md)

Flexbox는 부모에 display:flex를 지정하고, 직접 자식들을 한 축을 중심으로 배치한다. 부모의 정렬 속성과 자식의 크기·순서 속성을 구분한다.

<!-- chapter-toc -->

- [1. 현재 실행 중인 상태](#section-1)
- [2. 축을 먼저 확인하기](#section-2)
- [3. 주석 실험을 한 번에 하나씩 켜기](#section-3)
- [4. grow와 shrink를 과장하지 않기](#section-4)
- [복습](#section-5)

<a id="section-1"></a>

## 1. 현재 실행 중인 상태

양쪽 `15_flex.html`은 같은 코드다. container는 300×300px, display:flex, flex-direction:row다. wrap·정렬 실험 대부분과 item의 width는 **주석**이다.

### 강사님 코드

`15_flex.html` 95~101행 — **원본 발췌**

```html
    <div class="container">
        <div class="item">1</div>
        <div class="item" style="order: 1">2</div>
        <div class="item" style="order: -1">3</div>
        <div class="item" style="flex-grow: 0; flex-shrink: 3; min-width: 50px;">4</div>
        <div class="item" style="flex-grow: 0; flex-shrink: 2;">5</div>
    </div>
```

### 내 코드

`15_flex.html` 95~101행 — **원본 발췌**

```html
    <div class="container">
        <div class="item">1</div>
        <div class="item" style="order: 1">2</div>
        <div class="item" style="order: -1">3</div>
        <div class="item" style="flex-grow: 0; flex-shrink: 3; min-width: 50px;">4</div>
        <div class="item" style="flex-grow: 0; flex-shrink: 2;">5</div>
    </div>
```

순서는 order 작은 값부터이므로 화면 왼쪽부터 **3 → 1 → 4 → 5 → 2**다. 같은 order에서는 원본 순서를 따른다. HTML 자체의 순서가 바뀐 것은 아니다. order를 읽기 순서를 마음대로 고치는 도구로 사용하지 않는다.

<a id="section-2"></a>

## 2. 축을 먼저 확인하기

| 부모 속성 | 원본의 주석 실험 | 무엇을 바꾸는가 |
| --- | --- | --- |
| display | flex / inline-flex | 바깥쪽에서 부모 상자가 놓이는 방식 차이 |
| flex-direction | row·row-reverse·column·column-reverse | 주축의 방향 |
| flex-wrap | nowrap·wrap·wrap-reverse | 한 줄 유지 또는 여러 줄·줄 쌓이는 방향 |
| justify-content | start·end·center·space-between/around/evenly 계열 | 주축의 남은 공간 배분 |
| align-items | stretch·flex-start·flex-end·center | 각 줄 안에서 교차축 방향으로 항목 정렬 |
| align-content | stretch·정렬·공간 배분 | 여러 줄을 담는 컨테이너의 교차축 여유 공간 배분 |

표의 start·end는 원본의 `flex-start`·`flex-end`를 가리킨다. 이 문서의 기본 row는 가로 주축, 세로 교차축이다. column으로 바꾸면 두 축의 역할도 바뀐다. 쓰기 방향이 다른 문서까지 row를 항상 왼쪽→오른쪽이라고 일반화하지 않는다.

space-between은 양 끝 항목을 끝에 놓고 사이 간격을 나눈다. space-around는 항목 양옆 공간이라 내부 간격이 끝 공간의 두 배가 될 수 있다. space-evenly는 끝과 사이를 같은 간격으로 나눈다. **분배할 남은 공간이 있는지** 먼저 확인한다.

<a id="section-3"></a>

## 3. 주석 실험을 한 번에 하나씩 켜기

1. 현재 상태에서 순서와 항목 높이를 확인한다. 높이를 따로 주지 않아 기본 stretch 결과가 보인다.
2. justify-content:center만 켜 주축 방향 이동을 본다.
3. align-items:center를 추가하고 항목 높이가 어떻게 달라지는지 본다.
4. 두 정렬을 다시 끄고, item width:100px와 flex-wrap:wrap을 켜 줄바꿈을 본다.
5. 여러 줄과 교차축 여유가 생긴 상태에서 align-content를 비교한다.

align-content가 nowrap의 한 줄 컨테이너에서 아무 변화가 없는 것은 오타 때문만은 아니다. 항목들이 줄로 나뉠 조건을 먼저 확인한다. [Flexbox 표준](https://www.w3.org/TR/css-flexbox-1/)

<a id="section-4"></a>

## 4. grow와 shrink를 과장하지 않기

원본 4·5번의 flex-grow는 0이다. 따라서 남는 너비를 그 항목들이 grow로 나누어 차지하지 않는다. flex-shrink는 각각 3·2지만, 현재 한 자리 숫자 다섯 개는 300px 안에 들어가므로 **축소가 일어나지 않으면 차이도 보이지 않는다.**

shrink 숫자는 최종 너비 비율 자체가 아니다. 공간 부족량과 항목의 기준 크기에 영향을 받으며, 4번의 min-width:50px 같은 제한도 적용된다. “3:2니까 결과 너비가 3:2”라는 설명은 피한다.

flex-basis의 명시적 설정·축약 flex 계산은 비교 수업 코드에서 확인되지 않았다. 현재 기본값의 세부 계산 이론을 기본 문제에 요구하지 않고 추가편으로 분리한다.

<a id="section-5"></a>

## 복습

align-items:center를 켰는데 가로 가운데에 모이지 않는다. 먼저 무엇을 볼까?

<details>
<summary>해설</summary>

flex-direction을 확인한다. 현재 row에서 align-items는 세로 교차축, 가로 주축은 justify-content가 담당한다.

</details>

**추가로 알면 좋은 것:** flex-basis·flex 축약의 상세 계산, Grid 비교, 원본 밖 컴포넌트 설계는 별도 확장이다.

<!-- legacy-migration -->

<a id="css-4"></a>
<a id="css-47"></a>
<a id="css-41"></a>
<a id="css-60"></a>
<a id="css-12"></a>
<a id="css-52"></a>
<a id="css-27"></a>
<a id="css-15"></a>
<a id="css-16"></a>

### 이전 색인 링크 안내

이전 절 주소를 보존한 이동 안내다. 옛 절 번호와 현재 절은 같지 않다. [현재 CSS 목차](README.md)에서 수업 본문과 **추가로 알면 좋은 것**을 구분해 찾는다.
