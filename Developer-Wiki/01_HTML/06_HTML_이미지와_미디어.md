# 06. 이미지와 동영상 — 파일 위치와 표시 속성 구분하기

[HTML 읽기 안내](README.md) · [이전: 표](05_HTML_테이블.md) · [다음: 폼 입력요소](07_HTML_폼과_입력요소.md)

이미지가 보이지 않으면 먼저 `src`가 실제 파일을 가리키는지 확인한다. 보이지만 찌그러지면 크기 설정을 확인한다. 이 장은 양쪽 `workspace_html/06_img.html`의 `img`와 `video`를 기준으로 한다.

## 목차

1. [이미지 크기 원본 비교](#image)
2. [`src`·`alt`와 경로](#attributes)
3. [동영상 원본 비교](#video)
4. [원본 주석 교정과 복습](#practice)

<a id="image"></a>

## 1. 같은 이미지를 200 × 300으로 표시하기

### 강사님 코드 — 원본 발췌

강사님 `workspace_html/06_img.html` 11~15행

```html
    <img   
         src="asset/Spongebob-Christmas-PNG-Picture.png" 
         alt="스폰지밥이 웃고있는 사진"
         width="200"
         height="300">
```

속성을 여러 줄로 나누어 작성했다. 속성명이 나뉜 것은 아니므로 한 줄로 쓴 것과 같은 설정이다.

### 내 코드 — 원본 발췌

내 코드 `workspace_html/06_img.html` 18~18행

```html
        <img src="asset/Spongebob-Christmas-PNG-Picture.png" alt="스폰지밥이 웃고있는 사진" width="200" height="300">
```

파일·대체 텍스트·너비·높이가 같다. 내 코드는 한 줄, 강사님 코드는 여러 줄이라는 가독성 차이가 있다. 속성이 많아지면 강사님처럼 줄을 나누면 비교하기 쉽다.

| 속성 | 원본 값 | 역할 |
| --- | --- | --- |
| `src` | `asset/...png` | 표시할 이미지의 경로 |
| `alt` | 스폰지밥이 웃고있는 사진 | 이미지를 대신할 텍스트 |
| `width` | `200` | 이미지 표시 너비 |
| `height` | `300` | 이미지 표시 높이 |

추가 CSS가 없는 이 예제는 너비 200, 높이 300 CSS 픽셀로 표시한다. 원본 이미지 비율이 2:3이 아니면 가로·세로 비율이 달라져 찌그러져 보일 수 있다. 파일 자체의 픽셀 데이터를 200 × 300으로 편집한 것은 아니다.

설명용 수정 — 보통의 비율이 있는 이미지에서 너비만 지정해 비율을 유지한다.

```html
<img src="asset/Spongebob-Christmas-PNG-Picture.png"
     alt="스폰지밥이 웃고있는 사진"
     width="200">
```

이 예제는 **해당 이미지 파일이 실제 경로에 있어야** 확인할 수 있다. 제공된 양쪽 ZIP에는 같은 이미지가 있었고, 자연 크기는 100×83이었다. 로컬 브라우저에서 너비만 200으로 지정하면 200×166, 너비·높이를 함께 지정하면 200×300으로 표시되는 것을 확인했다. CSS로 크기를 덮어쓰면 결과가 달라지므로, HTML 속성만 있는 조건과 구분한다.

<a id="attributes"></a>

## 2. `src`는 파일 위치, `alt`는 내용의 대체 설명

원본 문서 `06_img.html` 옆에 `asset` 폴더가 있으므로 `asset/파일명.png`를 사용했다. 문서를 다른 폴더로 옮기면 상대 경로도 다시 계산해야 한다. 파일명·확장자·대소문자와 서버 루트를 확인한다.

`alt`에는 단순히 “이미지가 없습니다”보다 **원래 이미지가 전달하려던 정보**를 적는 편이 도움이 된다. 원본의 대체 텍스트는 이미지의 대상을 설명한다. `title` 속성과 달리 마우스를 올리는 상황에만 쓰는 보충 설명이 아니다.

내 주석의 “이후 이미지로 표기되게 할 수도 있음”을 `alt`가 이미지를 생성하거나 교체한다는 뜻으로 읽지 않는다. `alt`는 텍스트다. 또한 브라우저가 이미지를 항상 특정 임시 폴더에 저장한 후 표시한다고 외우지 않는다. 캐시 내부 동작은 이번 필수 진도에 포함하지 않는다.

<a id="video"></a>

## 3. `video`의 재생 제어와 반복

### 강사님 코드 — 원본 발췌

강사님 `workspace_html/06_img.html` 18~22행

```html
    <video 
        controls="controls"
        loop="loop"
        src="https://www.w3schools.com/tags/movie.mp4"
        ></video>
```

`controls`는 브라우저가 제공하는 재생 제어를 요청하고, `loop`는 재생이 끝나면 반복하도록 설정한다.

### 내 코드 — 원본 발췌

내 코드 `workspace_html/06_img.html` 28~32행

```html
        <video 
            controls="controls" 
            loop="loop"
            src="https://www.w3schools.com/tags/movie.mp4">
        </video>
```

들여쓰기와 닫기 태그의 위치만 다르며 실제 설정은 같다. `src`가 외부 주소이므로 네트워크·서버 응답·지원 형식에 따라 실제 재생 가능 여부가 달라질 수 있다.

| 설정 | 이 코드의 의미 |
| --- | --- |
| `src` | 불러올 동영상 주소 |
| `controls` | 재생·정지 등 제어 UI 표시 |
| `loop` | 끝난 뒤 반복 재생 |

`controls`와 `loop`는 불리언 속성이다. `controls="controls"`와 `controls`는 둘 다 켜진 상태를 표현한다. 끄려면 속성을 제거한다. `controls="false"`처럼 적어도 속성이 존재하므로 끄는 표현이 아니다.

원본에는 자동 재생을 요청하는 `autoplay`가 없다. `loop`를 지정했다고 문서를 여는 즉시 자동 재생되는 것은 아니다. 재생 UI 모양은 브라우저마다 달라질 수 있다.

이번 확인 환경에서는 원본 외부 영상이 로드되었고, 재생 버튼을 누른 뒤 재생 시간이 진행되는 것을 확인했다. 약 12.6초 길이의 이 영상이 앞으로도 같은 주소에서 제공된다는 보장은 아니다. 반복 속성은 확인했지만 반복 경계를 정밀하게 측정한 검사는 아니다.

<a id="practice"></a>

## 4. 복습과 추가 범위

1. 너비·높이를 동시에 지정한 뒤 그림이 찌그러졌다. 무엇을 확인할까?
2. 동영상 반복을 끄려면 `loop="false"`로 바꿀까, 속성을 지울까?
3. `alt`에 파일을 지정하면 다른 이미지로 바뀔까?

<details>
<summary>정답과 이유</summary>

1. 지정한 너비·높이의 비율과 원본 이미지 비율을 비교한다. 너비만 지정하는 방법도 확인한다.
2. `loop` 속성을 제거한다.
3. 바뀌지 않는다. 이미지 위치는 `src`, 대체 텍스트는 `alt`다.

</details>

**추가로 알면 좋은 것:** `picture`·`srcset`·지연 로딩·`audio`·자막용 `track`은 별도 확장 내용이다. 내 원본의 YouTube `iframe`은 주석 처리된 붙여넣기 예제이므로, 그 안의 권한·리퍼러·전체 화면 속성을 상세하게 배운 것으로 간주하지 않는다.

정확성 참고: [HTML 표준 — 이미지](https://html.spec.whatwg.org/dev/embedded-content.html#the-img-element), [동영상과 미디어 속성](https://html.spec.whatwg.org/dev/media.html).

[다음: 폼 입력요소](07_HTML_폼과_입력요소.md)

<!-- legacy-migration -->

<a id="index-section-70"></a>
<a id="index-section-14"></a>
<a id="html-16"></a>
<a id="html-7"></a>
<a id="html-17"></a>
<a id="html-43"></a>
<a id="index-section-42"></a>
<a id="html-31"></a>
<a id="html-36"></a>
<a id="index-section-68"></a>
<a id="html-18"></a>
<a id="html-32"></a>
<a id="html-4"></a>
<a id="index-section-69"></a>
<a id="html-20"></a>
<a id="html-29"></a>
<a id="html-27"></a>
<a id="html-5"></a>
<a id="html-22"></a>
<a id="html-11"></a>
<a id="html-25"></a>

### 이전 색인 링크 안내

이전 절 주소를 보존한 안내 위치다. 개편 전 절 번호와 현재 절 번호는 서로 다르다. 수업 이미지·동영상은 이 문서, 반응형 이미지·추가 미디어 요소는 [추가 미디어](추가로_알면_좋은_것/02_확장_요소와_속성.md#media)에서 읽는다.
