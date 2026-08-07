# 🎨 CSS Developer-Wiki

> CSS 선택자와 단위부터 박스 모델, 배경, Typography, Position, Overflow,
> 시각 효과, Transition, Transform, 반응형 웹, Flexbox, 실무 코딩
> 스타일과 종합실습까지 단계적으로 학습할 수 있도록 정리한 문서입니다.
>
> 모든 학습 문서는 **실제 수업 코드**, **내 코드와 강사님 코드 비교**,
> **브라우저 동작 원리**, **오류와 개선 방향**, **실무 관점**을 공통
> 기준으로 작성했습니다.

------------------------------------------------------------------------

## 📌 학습 목표

이 과정을 통해 다음 내용을 학습합니다.

-   CSS 선택자와 적용 우선순위
-   절대·상대 단위와 색상 표현
-   Box Model과 요소 크기 계산
-   Display와 요소 배치 방식
-   요소 숨김과 투명도 처리
-   Background Image와 배경 속성
-   Text와 Font Styling
-   Position과 요소 위치 제어
-   Overflow와 Scroll 처리
-   Float와 Clear의 동작 원리
-   Shadow를 활용한 시각적 깊이 표현
-   Transition과 상태 변화
-   Transform과 요소 변형
-   Media Query와 반응형 웹
-   Flexbox 기반 유연한 Layout
-   유지보수하기 좋은 실무 CSS 작성
-   여러 CSS 개념을 연결한 반응형 UI 구현

------------------------------------------------------------------------

## 🗺️ 학습 로드맵

  -------------------------------------------------------------------------
  단계              문서 범위         학습 주제         목표
  ----------------- ----------------- ----------------- -------------------
  1\. CSS 시작      01\~02            선택자, 적용      CSS가 요소를
                                      방법, 단위, 색상  선택하고 값을
                                                        계산하는 기본
                                                        원리를 이해합니다.

  2\. 요소와 Box    03\~05            Box Model,        요소의
                                      Display, 투명도,  크기·배치·표시
                                      숨김              상태를 제어합니다.

  3\. 시각 표현     06\~07            Background, Text, 배경과 Typography를
                                      Font              이용해 콘텐츠의
                                                        시각적 표현을
                                                        설계합니다.

  4\. 위치와 흐름   08\~10            Position,         Normal Flow와
                                      Overflow, Float,  위치·넘침·Float의
                                      Clear             관계를 이해합니다.

  5\. UI 효과       11\~13            Shadow,           상태 변화와 시각적
                                      Transition,       피드백을
                                      Transform         구현합니다.

  6\. 반응형 Layout 14\~15            Media Query,      화면 크기와
                                      Responsive Web,   콘텐츠에 따라
                                      Flexbox           유연하게 변하는
                                                        Layout을
                                                        구현합니다.

  7\. 실무 적용     16\~17            실무 코딩 스타일, 학습한 CSS를
                                      종합실습          유지보수 가능한
                                                        구조와 반응형 UI에
                                                        적용합니다.
  -------------------------------------------------------------------------

------------------------------------------------------------------------

## 📚 Documentation

  ----------------------------------------------------------------------------------------------------------------
           No          Document                                           핵심 내용                   분류
  -------------------- -------------------------------------------------- ------------------- --------------------
           01          [선택자와 적용방법](./01_CSS_선택자와_적용방법.md) CSS 적용 방식,              기초
                                                                          기본·복합 선택자,   
                                                                          가상 클래스·가상    
                                                                          요소, 명시도        

           02          [단위와 색상](./02_CSS_단위와_색상.md)             `px`, `%`, `em`,            기초
                                                                          `rem`, Viewport     
                                                                          단위, HEX, RGB,     
                                                                          RGBA, 상속          

           03          [박스모델](./03_CSS_박스모델.md)                   `width`, `height`,          Box
                                                                          Margin, Padding,    
                                                                          Border,             
                                                                          `box-sizing`,       
                                                                          Margin Collapse     

           04          [Display와                                         Block, Inline,             Layout
                       요소배치](./04_CSS_Display와_요소배치.md)          Inline Block,       
                                                                          Display와 요소 배치 

           05          [투명도와 요소숨김](./05_CSS_투명도와_요소숨김.md) `opacity`,                  상태
                                                                          `visibility`,       
                                                                          `display`, 요소     
                                                                          숨김 방식과 차이    

           06          [배경이미지와                                      Background Image,           시각
                       배경속성](./06_CSS_배경이미지와_배경속성.md)       Repeat, Position,   
                                                                          Size, Attachment,   
                                                                          Gradient            

           07          [텍스트와 글꼴](./07_CSS_텍스트와_글꼴.md)         Font, Text               Typography
                                                                          Alignment, Line     
                                                                          Height, Decoration, 
                                                                          Web Font            

           08          [Position과                                        Static, Relative,          Layout
                       요소위치](./08_CSS_Position과_요소위치.md)         Absolute, Fixed,    
                                                                          Sticky, `z-index`   

           09          [Overflow와 스크롤](./09_CSS_Overflow와_스크롤.md) Overflow, Scroll,          Layout
                                                                          Clip, Text          
                                                                          Overflow, 가로 넘침 
                                                                          Debugging           

           10          [Float와 Clear](./10_CSS_Float와_Clear.md)         Float, Clear, Text         Layout
                                                                          Flow, `flow-root`,  
                                                                          Legacy Layout 이해  

           11          [그림자와 시각효과](./11_CSS_그림자와_시각효과.md) `text-shadow`,              효과
                                                                          `box-shadow`,       
                                                                          Inset, 다중 Shadow, 
                                                                          Hover 효과          

           12          [Transition과                                      Transition                  효과
                       상태변화](./12_CSS_Transition과_상태변화.md)       Property, Duration, 
                                                                          Timing Function,    
                                                                          Delay, 상태 변화    

           13          [Transform과                                       Translate, Scale,           효과
                       요소변형](./13_CSS_Transform과_요소변형.md)        Rotate, Skew,       
                                                                          Transform 조합과    
                                                                          기준점              

           14          [미디어쿼리와                                      `@media`,                  반응형
                       반응형](./14_CSS_미디어쿼리와_반응형.md)           Breakpoint, Mobile  
                                                                          First, 반응형 메뉴, 
                                                                          입력 환경 조건      

           15          [Flexbox와 유연한                                  Flex                       Layout
                       레이아웃](./15_CSS_Flexbox와_유연한_레이아웃.md)   Container·Item,     
                                                                          주축·교차축, 정렬,  
                                                                          Wrap,               
                                                                          Grow·Shrink·Basis   

           16          [실무 코딩 스타일](./16_CSS_실무_코딩스타일.md)    네이밍, 명시도,             실무
                                                                          Cascade, Token,     
                                                                          상태, 접근성,       
                                                                          반응형 설계         

           17          [종합실습](./17_CSS_종합실습.md)                   01\~16번을 연결한           실습
                                                                          반응형 교육 과정    
                                                                          대시보드 구현       
  ----------------------------------------------------------------------------------------------------------------

------------------------------------------------------------------------

## 🧭 추천 학습 방법

  -----------------------------------------------------------------------
  순서                                학습 방법
  ----------------------------------- -----------------------------------
  1                                   문서의 개요와 학습 목표를 먼저
                                      확인합니다.

  2                                   HTML과 CSS 예제 코드를 직접
                                      입력하고 Browser에서 확인합니다.

  3                                   개발자 도구에서 적용된 Selector와
                                      Box Model을 확인합니다.

  4                                   내 코드와 강사님 코드의 차이가 있는
                                      문서는 결과뿐 아니라 작성 의도를
                                      비교합니다.

  5                                   대표 오류와 개선 사례를 확인하고
                                      같은 문제를 직접 재현해 봅니다.

  6                                   화면 너비와 콘텐츠 길이를 바꾸며
                                      Layout이 어떻게 달라지는지
                                      확인합니다.

  7                                   문서 마지막 체크리스트로 속성의
                                      동작과 실무 선택 기준을 점검합니다.

  8                                   16번 실무 코딩 스타일과 17번
                                      종합실습으로 전체 내용을 하나의 UI
                                      설계 흐름으로 연결합니다.
  -----------------------------------------------------------------------

------------------------------------------------------------------------

## 💼 실무 코딩 스타일

[16_CSS_실무_코딩스타일.md](./16_CSS_실무_코딩스타일.md)는 새로운 CSS
속성을 추가로 외우는 문서가 아니라, 이미 학습한 CSS를 **실제
프로젝트에서는 어떤 기준으로 선택하고 구조화하는지** 설명하는
문서입니다.

주요 학습 내용:

-   역할 기반 Class 네이밍
-   낮고 예측 가능한 명시도
-   Cascade와 `!important` 사용 기준
-   CSS Custom Property와 Design Token
-   Spacing·Color·Radius·Shadow Scale
-   Component와 Page Layout 책임 분리
-   Flexbox·Grid·Position의 사용 목적 구분
-   상태 Class와 ARIA Attribute 활용
-   Hover·Focus·Disabled 상태 설계
-   Mobile First와 Layout 기준 Breakpoint
-   Transition·Transform 성능 기준
-   Reduced Motion과 Keyboard 접근성
-   Before/After 기반 CSS 리팩토링
-   Stylelint·Formatter·DevTools 기반 검수

------------------------------------------------------------------------

## 🚀 종합실습

[17_CSS_종합실습.md](./17_CSS_종합실습.md)는 01\~16번에서 학습한 내용을
개별 속성이 아닌 **하나의 반응형 UI 제작 과정**으로 연결합니다.

종합실습에서는 다음 내용을 함께 활용합니다.

  영역            활용 내용
  --------------- --------------------------------------------------
  기본 Style      Selector, Cascade, 단위, 색상, Box Model
  디자인 시스템   Custom Property, Spacing, Radius, Shadow
  콘텐츠 표현     Background, Typography, Overflow
  Layout          Display, Position, Flexbox, Grid
  상태 변화       Hover, Focus, Disabled, Transition, Transform
  반응형          Mobile First, Media Query, `clamp()`, `minmax()`
  접근성          Focus Style, ARIA, Reduced Motion
  실무 구조       Component Class, Modifier, Token, 역할 분리

실습 결과물은 **반응형 교육 과정 대시보드**이며 Header, Hero, Toolbar,
Course Card, Sidebar, Progress, CTA, Footer를 하나의 페이지로
구성합니다.

------------------------------------------------------------------------

## ⭐ Documentation Features

CSS Developer-Wiki 문서는 다음 원칙을 기준으로 작성했습니다.

-   ✅ 실제 수업 코드 기반
-   ✅ 내 코드와 강사님 코드 비교
-   ✅ 원본의 오류와 부정확한 설명 검토
-   ✅ Browser 동작 원리 보완
-   ✅ 단순 암기보다 적용 조건과 차이 설명
-   ✅ 실무 활용 예제 추가
-   ✅ 접근성과 반응형 환경 고려
-   ✅ 대표 오류와 Debugging 방법 정리
-   ✅ 종합실습과 체크리스트 제공
-   ✅ Markdown 형식과 문서 품질 통일

------------------------------------------------------------------------

## 📖 Documentation Structure

CSS 학습 문서는 주제에 따라 세부 항목 수는 달라지지만 다음 흐름을 공통
기준으로 사용합니다.

``` text
문서 정보
    │
    ├── 개요 / 학습 목표
    ├── 핵심 개념
    ├── 문법과 동작 원리
    ├── 원본 코드 분석
    ├── 내 코드와 강사님 코드 비교
    ├── 개선 방향
    ├── 실무 활용
    ├── 대표 오류와 Debugging
    ├── 종합실습
    ├── 정답과 해설
    ├── 최종 체크리스트
    └── 핵심 요약
```

16번과 17번은 일반 개념 문서와 목적이 다릅니다.

``` text
16 실무 코딩 스타일
→ CSS 설계·작성·리팩토링 기준

17 종합실습
→ 01~16 내용을 실제 반응형 UI로 연결
```

------------------------------------------------------------------------

## 🎯 Learning Outcome

CSS 문서를 모두 학습하면 다음 내용을 직접 설명하고 구현하는 것을 목표로
합니다.

-   Selector와 Cascade를 고려해 안전하게 Style을 적용할 수 있습니다.
-   Box Model을 기준으로 요소의 실제 크기를 계산할 수 있습니다.
-   Display와 Normal Flow를 이해하고 Layout 문제를 추적할 수 있습니다.
-   Background와 Typography를 목적에 맞게 사용할 수 있습니다.
-   Position·Overflow·Float의 동작과 사용 목적을 구분할 수 있습니다.
-   Shadow·Transition·Transform으로 UI 상태와 피드백을 표현할 수
    있습니다.
-   Media Query를 이용해 Mobile·Tablet·Desktop Layout을 구성할 수
    있습니다.
-   Flexbox를 이용해 정렬·분배·줄바꿈을 구현할 수 있습니다.
-   Hover뿐 아니라 Keyboard Focus와 Touch 환경을 고려할 수 있습니다.
-   Custom Property와 Design Token으로 반복되는 값을 관리할 수 있습니다.
-   유지보수하기 좋은 Component 중심 CSS를 작성할 수 있습니다.
-   여러 CSS 개념을 연결해 반응형 페이지를 완성할 수 있습니다.

------------------------------------------------------------------------

## 📂 Folder Policy

`02_CSS` 폴더는 다음 원칙으로 관리합니다.

-   실제 수업 코드와 실습 내용을 문서화합니다.
-   내 코드와 강사님 코드를 비교하되 존재하지 않는 차이를 만들지
    않습니다.
-   원본의 오류는 조용히 수정하지 않고 문제와 개선 방향을 구분합니다.
-   학습 문서 파일명은 `번호_CSS_주제.md` 형식을 유지합니다.
-   `README.md`는 CSS 전체 목차와 학습 가이드 역할을 담당합니다.
-   상세 문서는 README의 상대 경로 링크를 통해 이동합니다.
-   실무 코딩 스타일과 종합실습은 일반 개념 문서 뒤에 배치합니다.
-   완료된 문서도 전체 Wiki 구조와 품질 기준에 맞춰 지속적으로
    개선합니다.

------------------------------------------------------------------------

## 🔗 GitHub 상대 경로 규칙

CSS 폴더의 `README.md`를 기준으로 같은 폴더의 문서는 `./파일명.md`
형식으로 연결합니다.

``` text
Developer-Wiki/
├── README.md
├── 01_HTML/
│   └── README.md
├── 02_CSS/
│   ├── README.md
│   ├── 01_CSS_선택자와_적용방법.md
│   ├── ...
│   └── 17_CSS_종합실습.md
├── 03_JavaScript/
│   └── README.md
└── 04_Python/
    └── README.md
```

주요 상대 경로:

  목적                  상대 경로
  --------------------- ---------------------------------
  CSS 문서              `./01_CSS_선택자와_적용방법.md`
  이전 HTML             `../01_HTML/README.md`
  Developer-Wiki Home   `../README.md`
  다음 JavaScript       `../03_JavaScript/README.md`

------------------------------------------------------------------------

## 📎 Navigation

  -------------------------------------------------------------------------------------------------------
            Previous                         Home                                 Next
  ----------------------------- ------------------------------- -----------------------------------------
               [📄                            [🏠                                  [⚡
   HTML](../01_HTML/README.md)   Developer-Wiki](../README.md)   JavaScript](../03_JavaScript/README.md)

  -------------------------------------------------------------------------------------------------------

------------------------------------------------------------------------

## 📚 Developer-Wiki

> **Learn • Compare • Improve • Archive**

CSS는 단순히 화면을 꾸미는 기술에서 끝나지 않습니다.

**HTML 구조 위에 일관된 시각 규칙을 만들고, 다양한 화면과 입력 환경에서
안정적으로 동작하며, 다른 개발자가 안전하게 수정하고 확장할 수 있는 UI를
설계하는 과정**입니다.
