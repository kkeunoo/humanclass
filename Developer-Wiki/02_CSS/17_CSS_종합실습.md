# 17. 종합복습 — 실제 display 실습을 다시 설명하기

[CSS 목차](README.md)

이전의 큰 대시보드에는 Grid·다크 모드·새 설계 기법이 함께 들어 있었다. 기본 복습은 실제 수업 display 실습을 기준으로 바꿨다. 새 기능은 **추가로 알면 좋은 것**인 [학습 카드 프로젝트](추가로_알면_좋은_것/04_학습카드_확장프로젝트.md)로 분리했다.

강사님 경로는 `css/실습`, 내 경로는 `css/실습_tc`다. 두 폴더의 display1·display2는 내용이 같다. 폴더 이름만으로 내가 독립 구현한 정답이라고 단정하지 않는다.

<!-- chapter-toc -->

- [1. 제목·안내·버튼 모양 상자](#section-1)
- [2. 이미지·설명 두 칸](#section-2)
- [3. 먼저 직접 바꾸어 보기](#section-3)
- [4. 예상과 확인할 값](#section-4)

<a id="section-1"></a>

## 1. 제목·안내·버튼 모양 상자

### 강사님 코드

`실습/display1.html` 23~34행 — **원본 발췌**

```css
        #parent .d3{
            /* margin-top: 20px; */
            height: 40px;
            width: 200px;

            margin: 20px auto;
            
            background-color: rgba(250, 235, 215, 0.3);
        }
        #parent .d3:hover{
            background-color: rgba(250, 235, 215, 0.5);
        }
```

width:200px인 block을 좌우 auto margin으로 가운데 놓는다. hover하면 배경색의 알파가 0.3에서 0.5로 변한다. 기본 높이는 40px이며, 전체 선택자가 border 1px를 주므로 테두리까지 202×42px다.

### 내 코드

`실습_tc/display1.html` 23~34행 — **원본 발췌**

```css
        #parent .d3{
            /* margin-top: 20px; */
            height: 40px;
            width: 200px;

            margin: 20px auto;
            
            background-color: rgba(250, 235, 215, 0.3);
        }
        #parent .d3:hover{
            background-color: rgba(250, 235, 215, 0.5);
        }
```

코드가 같다. 표시 문구는 다음 단계로 진행하는 버튼처럼 보이지만 실제 HTML은 div다. 클릭으로 다음 화면이 열리는 기능은 없다. 표면 모양과 기능을 구분한다.

<a id="section-2"></a>

## 2. 이미지·설명 두 칸

### 강사님 코드

`실습/display2.html` 23~35행 — **원본 발췌**

```css
        #wrapper .content {
            display: inline-block;
            /* width: 198PX; */
            width: 45%;
            min-width: 200px;
            box-sizing: border-box;

            vertical-align: top;
        }

        #wrapper .content.left{
            margin-right: 20px;
            /* font-size: 0; */
```

각 칸을 inline-block 45%로 놓고 최소 너비 200px를 둔다. border-box이므로 오른쪽 설명에 padding을 더해도 지정한 width 안에 포함된다. 왼쪽 칸의 오른쪽 margin 20px와 HTML 공백은 별도다.

### 내 코드

`실습_tc/display2.html` 23~35행 — **원본 발췌**

```css
        #wrapper .content {
            display: inline-block;
            /* width: 198PX; */
            width: 45%;
            min-width: 200px;
            box-sizing: border-box;

            vertical-align: top;
        }

        #wrapper .content.left{
            margin-right: 20px;
            /* font-size: 0; */
```

원본이 같다. 두 칸 45%씩이라고 해서 모든 너비에서 한 줄에 들어가는 것은 아니다. 부모의 남는 10%가 margin·공백을 담을 수 있는지, min-width가 적용되는지 확인한다. 좁아지면 다음 줄로 내려갈 수 있다.

<a id="section-3"></a>

## 3. 먼저 직접 바꾸어 보기

1. display1의 상자 너비만 240px로 바꾸고 가운데 정렬이 유지되는지 예상한다.
2. display2의 양쪽 content에 표시된 border로 각 칸 경계를 읽는다.
3. 부모 너비를 줄이면서 두 칸이 언제 나뉘는지 관찰한다.
4. 오른쪽 padding을 늘릴 때 border-box를 켠 경우와 끈 경우를 비교한다.

원본 display2의 외부 이미지가 안 열리면 먼저 파일 로드를 확인한다. 아래 재구성은 외부 이미지 없이도 배치 계산을 연습하도록 왼쪽을 글 상자로 바꿨다. **원본 발췌가 아닌 수업 범위 재구성**이며 버튼에 추가 동작은 없다.

<details>
<summary>복습용 전체 HTML — 직접 작성한 뒤 비교</summary>

```html
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CSS 수업 복습</title>
    <style>
        body { margin: 0; }
        .wrapper {
            width: 90%;
            margin: 20px auto;
            padding: 20px 0;
            background-color: #eeeeee;
            text-align: center;
        }
        .content {
            display: inline-block;
            width: 45%;
            min-width: 200px;
            box-sizing: border-box;
            border: 1px solid gray;
            padding: 20px;
            vertical-align: top;
            text-align: left;
        }
        .left {
            margin-right: 20px;
            background-color: #abcdef;
        }
        .right { background-color: white; }
        button {
            width: 120px;
            height: 40px;
            border: 1px solid gray;
            background-color: white;
        }
        button:hover { background-color: #abcdef; }
    </style>
</head>
<body>
    <div class="wrapper">
        <div class="content left">
            <h1>CSS 복습</h1>
            <p>박스 크기와 줄바꿈을 확인합니다.</p>
        </div>
        <div class="content right">
            <h2>확인할 내용</h2>
            <ol>
                <li>너비와 padding</li>
                <li>좌우 margin과 공백</li>
                <li>좁은 화면의 줄바꿈</li>
            </ol>
            <button type="button">연습 버튼</button>
        </div>
    </div>
</body>
</html>
```

</details>

<a id="section-4"></a>

## 4. 예상과 확인할 값

부모 content가 900px라면 각 칸의 테두리까지 너비는 405px다. 두 칸 810px와 왼쪽 margin 20px, 사이의 공백을 합해 부모와 비교한다. 오른쪽의 content 너비는 405−40−2=363px다.

부모가 360px면 각 칸은 45%인 162px보다 min-width가 커서 200px가 된다. 두 칸은 한 줄에 들어가지 않는다. 이 예제는 작은 화면에서 min-width보다 더 줄어드는 완전한 반응형 설계를 목표로 하지 않는다.

같은 코드의 [실행용 HTML](실습/display_복습.html)을 제공한다. 브라우저에서 뷰포트 1000px일 때 부모 900px·자식 405px씩 같은 줄, 뷰포트 400px일 때 부모 360px·자식 200px씩 다음 줄 배치를 확인했다. GitHub에서는 소스로 보일 수 있으므로 내려받아 브라우저에서 연다.

기본 복습의 완료 기준은 두 칸의 크기와 줄바꿈을 설명하는 것이다. Grid·다크 모드 등 추가 기능은 이 문제의 정답에 요구하지 않는다.
