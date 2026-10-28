# 06. 배경 — 이미지의 크기와 놓는 위치 나누어 읽기

[CSS 목차](README.md)

배경 이미지는 요소 뒤에 그려진다. img처럼 이미지 자체가 내용의 크기를 만드는 것과 다르므로 원본은 height를 별도로 지정한다.

**설명용 예:** 가로로 긴 사진을 정사각형 상자의 배경으로 쓸 때 `background-size:contain`이면 사진 전체가 들어가되 빈 공간이 남을 수 있다. `cover`이면 상자를 덮되 사진 양끝이 잘릴 수 있다. 둘 다 원본 비율을 유지한다. 실제 파일 경로와 상자 크기는 아래 양쪽 코드에서 다시 확인한다.

<!-- chapter-toc -->

- [1. contain과 cover](06_CSS_배경이미지와_배경속성.md#section-1)
- [2. 원본의 다른 배경 실험](06_CSS_배경이미지와_배경속성.md#section-2)
- [3. 경로와 선언 순서](06_CSS_배경이미지와_배경속성.md#section-3)
- [복습](06_CSS_배경이미지와_배경속성.md#section-4)

<a id="section-1"></a>

## 1. contain과 cover

### 강사님 코드

`asset/css/06_background.css` 8~15행 — **원본 발췌**

```css
    background-repeat : /*repeat-x*/ /*repeat-y*/ no-repeat  ;

    /* background-size: 100px 200px; */
    /* background-size: 100% 50%; */
    /* background-size: 100% 100%; */
    /* background-size: cover; */
    background-size: contain;
}
```

현재 실행되는 값은 no-repeat와 contain이다. 주석의 cover·100% 100%가 동시에 적용되는 것이 아니다.

### 내 코드

`asset/css/06_background.css` 7~22행 — **원본 발췌**

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

동작은 같고 내 주석은 비율과 빈 공간을 구분한다. 양쪽 #back1의 이미지는 같은 외부 URL이며 높이는 250px다. 외부 주소가 차단되거나 없어지면 배경을 볼 수 없으므로, 파일을 읽는 실패와 크기 계산을 구분한다.

| 설정 | 비율 | 빈 공간·잘림 |
| --- | --- | --- |
| contain | 유지 | 이미지 전체가 들어가도록 맞춤. 남는 공간 가능 |
| cover | 유지 | 영역을 덮도록 맞춤. 일부 이미지가 잘릴 수 있음 |
| 100% 100% | 원본과 달라질 수 있음 | 가로·세로를 각각 영역에 맞춤 |
| no-repeat | 크기와 별개의 설정 | 남는 공간을 같은 이미지로 반복 채우지 않음 |

<a id="section-2"></a>

## 2. 원본의 다른 배경 실험

| 선택자 | 원본 설정 | 관찰할 것 |
| --- | --- | --- |
| #back2 | height:80vh, cover, attachment:fixed, overflow:auto | 배경 고정과 내부 내용 스크롤은 서로 다른 속성 |
| #back2 p | height:200vh | 부모보다 큰 내용이 내부 스크롤을 만듦 |
| .profile | 100×100, no-repeat, position:center, radius:50% | 이미지 중심을 놓음. size:contain은 주석이라 원본 크기 기준으로 잘릴 수 있음 |
| #back3 | background 단축 속성 다음 size:contain | 색·이미지·반복·위치와 크기를 함께 읽음 |

background-position:center는 상자 자체를 가운데로 옮기지 않는다. 배경을 그리는 위치를 정한다. fixed는 원본처럼 별도 기준을 만드는 조상이 없는 경우 뷰포트에 배경을 고정하며, 요소 자신을 화면에 고정하는 position:fixed와 다르다. [배경 표준](https://www.w3.org/TR/css-backgrounds-3/)

<a id="section-3"></a>

## 3. 경로와 선언 순서

외부 CSS 안의 상대 url은 **CSS 파일 위치**를 기준으로 해석한다. HTML과 CSS가 서로 다른 폴더에 있을 때 특히 확인한다.

```css
/* 설명용 재구성: 실제 이미지 파일을 준비한 뒤 경로를 맞춘다. */
.sample {
    height: 250px;
    background: #abcdef url("../image/lesson.png") no-repeat center;
    background-size: contain;
}
```

background 단축 선언은 생략한 관련 값도 초기화할 수 있다. size를 먼저 쓰고 background를 나중에 쓰면 size가 유지된다고 단정하지 않는다. 원본처럼 단축 선언 다음 size를 쓰는 순서를 읽는다.

<a id="section-4"></a>

## 복습

정사각형 영역에서 가로로 긴 사진 전체를 보여 주려면 contain과 cover 중 어느 쪽일까?

<details>
<summary>해설</summary>

contain이다. 위아래에 공간이 남을 수 있다. 사진 전체보다 영역을 꽉 덮는 것이 목표라면 cover를 비교한다.

</details>

**추가로 알면 좋은 것:** 다중 배경·gradient·background-origin/clip·배경 성능 설계는 이 수업 예제의 필수 전제가 아니다.

<!-- legacy-migration -->

<a id="css-19"></a>
<a id="css-13"></a>
<a id="index-section-56"></a>
<a id="css-36"></a>
<a id="css-28"></a>
<a id="css-18"></a>
<a id="index-section-76"></a>
<a id="css-27"></a>

### 이전 색인 링크 안내

이전 절 주소를 보존한 이동 안내다. 옛 절 번호와 현재 절은 같지 않다. [현재 CSS 목차](README.md)에서 수업 본문과 **추가로 알면 좋은 것**을 구분해 찾는다.

---

[장별 연습문제 풀기](실습/연습문제/06_CSS_배경이미지와_배경속성_연습문제.md)
