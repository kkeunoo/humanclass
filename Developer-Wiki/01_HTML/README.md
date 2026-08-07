# 🧱 HTML Developer-Wiki

> HTML 문서의 기본 구조부터 Text, Link, List, Table, Image·Media, Form, Semantic HTML, 실무 코딩 스타일과 종합실습까지 단계적으로 학습할 수 있도록 정리한 문서입니다.
>
> 모든 학습 문서는 **실제 수업 코드**, **내 코드와 강사님 코드 비교**, **브라우저 동작 원리**, **원본 오류와 개선 방향**, **접근성과 실무 관점**을 공통 기준으로 작성했습니다.

---

## 📌 학습 목표

이 과정을 통해 다음 내용을 학습합니다.

- HTML5 기본 문서 구조와 Metadata
- Tag, Element, Attribute, Comment
- Heading과 Paragraph를 이용한 문서 계층
- 의미에 맞는 Text Element 사용
- Link와 상대·절대·Root Relative 경로
- 순서 있는 목록·순서 없는 목록·설명 목록
- Table의 Row·Column 관계와 Header Cell
- Image `alt`와 Media 접근성
- Form Control과 사용자 입력 데이터
- `name`, `value`, `label`, GET·POST
- Semantic HTML과 Landmark
- Heading Structure와 Reading Order
- Native HTML과 ARIA의 역할 구분
- 유지보수하기 좋은 실무 HTML 작성
- 여러 HTML 개념을 연결한 실제 Page 구조 설계

---

## 🗺️ 학습 로드맵

| 단계 | 문서 범위 | 학습 주제 | 목표 |
| --- | --- | --- | --- |
| 1. HTML 시작 | 01~02 | 문서 구조, 기본 Tag, Text | HTML이 Content의 구조와 의미를 표현하는 원리를 이해합니다. |
| 2. 연결과 목록 | 03~04 | Link, 경로, List | Page와 Resource를 연결하고 항목 관계를 구조화합니다. |
| 3. 데이터와 Media | 05~06 | Table, Image, Video, Audio, `iframe` | 표 형식 Data와 시각·음성 Media를 의미 있게 제공합니다. |
| 4. 사용자 입력 | 07 | Form, Input, Label, GET·POST | 사용자가 입력한 값을 구조화하고 제출 과정을 이해합니다. |
| 5. Page 구조 | 08 | Semantic HTML, Landmark, Heading | 앞선 요소를 실제 Page 골격으로 조립합니다. |
| 6. 실무 적용 | 09~10 | 실무 코딩 스타일, 종합실습 | 접근 가능하고 유지보수하기 좋은 HTML을 실제 Page로 완성합니다. |

---

## 📚 Documentation

| No | Document | 핵심 내용 | 분류 |
|:--:|---|---|:--:|
| 01 | [기초와 문서구조](./01_HTML_기초와_문서구조.md) | HTML 역할, Tag·Element·Attribute, Comment, 기본 HTML5 Document, `src`, `title`, `alt` | 기초 |
| 02 | [기본태그](./02_HTML_기본태그.md) | `h1`~`h6`, `p`, `br`, `hr`, `strong`, `em`, `mark`, `del`, `pre`, Entity | Text |
| 03 | [링크와 경로](./03_HTML_링크와_경로.md) | `a`, `href`, `target`, URL Scheme, 상대 경로, Fragment Link, Download | Link |
| 04 | [목록태그](./04_HTML_목록태그.md) | `ul`, `ol`, `li`, `dl`, `dt`, `dd`, 중첩 목록, Navigation List | List |
| 05 | [테이블](./05_HTML_테이블.md) | `table`, `caption`, `thead`, `tbody`, `tr`, `th`, `td`, `scope`, 셀 병합 | Data |
| 06 | [이미지와 미디어](./06_HTML_이미지와_미디어.md) | `img`, `alt`, 반응형 Image, `figure`, `picture`, `video`, `audio`, `iframe` | Media |
| 07 | [폼과 입력요소](./07_HTML_폼과_입력요소.md) | `form`, `input`, `label`, Checkbox, Radio, Select, Textarea, GET·POST | Form |
| 08 | [시맨틱태그와 페이지구조](./08_HTML_시맨틱태그와_페이지구조.md) | `header`, `nav`, `main`, `section`, `article`, `aside`, `footer`, Landmark | Semantic |
| 09 | [실무 코딩스타일](./09_HTML_실무_코딩스타일.md) | Semantic 구조, Heading, Link·Button, 접근성, 네이밍, Validator, Code Review | 실무 |
| 10 | [종합실습](./10_HTML_종합실습.md) | 01~09를 연결한 IT 교육 과정 소개·상담 신청 Page 구현 | 실습 |

---

## 🧭 추천 학습 방법

| 순서 | 학습 방법 |
| --- | --- |
| 1 | 문서의 개요와 학습 목표를 먼저 확인합니다. |
| 2 | 예제 HTML을 직접 입력하고 Browser에서 렌더링 결과를 확인합니다. |
| 3 | Elements Panel에서 Browser가 실제로 만든 DOM 구조를 확인합니다. |
| 4 | 내 코드와 강사님 코드의 차이가 있는 문서는 결과뿐 아니라 작성 의도를 비교합니다. |
| 5 | 원본의 오류를 직접 재현하고 왜 Browser가 예상과 다르게 처리하는지 확인합니다. |
| 6 | CSS를 끈 상태에서도 문서의 Heading·List·Table·Form 구조가 이해되는지 확인합니다. |
| 7 | Keyboard만으로 Link·Form·`details` 등 기본 기능을 사용할 수 있는지 점검합니다. |
| 8 | 각 문서의 최종 체크리스트로 Markup과 접근성을 검수합니다. |
| 9 | 09번 실무 코딩 스타일에서 작성 기준을 정리합니다. |
| 10 | 10번 종합실습에서 전체 내용을 하나의 Semantic Page로 연결합니다. |

---

## 💼 실무 코딩 스타일

[09_HTML_실무_코딩스타일.md](./09_HTML_실무_코딩스타일.md)는 새로운 Tag를 추가로 암기하는 문서가 아니라, 이미 학습한 HTML을 **실제 Project에서 어떤 기준으로 선택·작성·리팩토링하는지** 설명하는 기준 문서입니다.

주요 학습 내용:

- HTML5 Document Structure
- Semantic Element와 `div` 선택 기준
- Heading Hierarchy
- Link와 Button 역할 구분
- List·Table·Media·Form의 의미 구조
- Image `alt` 작성 기준
- Form Label과 `name`
- `id`, `class`, `name`, `data-*`, `aria-*` 역할 구분
- Native HTML 우선 원칙
- Boolean Attribute 작성
- Relative Path와 Asset 관리
- Comment 보안과 작업 기록 분리
- 역할 기반 Class·ID Naming
- Duplicate ID 방지
- Browser DOM 자동 보정 이해
- Validator·DevTools·Keyboard·Screen Reader 검수
- HTML 01~08에서 실제 발견한 Before → After 리팩토링 사례

---

## 🚀 종합실습

[10_HTML_종합실습.md](./10_HTML_종합실습.md)는 01~09에서 학습한 내용을 개별 Tag가 아닌 **하나의 실제 Page 제작 과정**으로 연결합니다.

종합실습의 주제는 **IT 교육 과정 소개·상담 신청 Page**입니다.

| 영역 | 활용 내용 |
| --- | --- |
| Document | `doctype`, `lang`, `charset`, `viewport`, `title`, `description` |
| Page Structure | `header`, `nav`, `main`, `section`, `article`, `aside`, `footer` |
| Text | Heading, Paragraph, `abbr`, `time` |
| Navigation | Link, Fragment, `aria-current`, 전화 Link, Download |
| List | 과정 Stack, 학습 순서, Footer Navigation, 과정 정보 |
| Table | `caption`, `thead`, `tbody`, `scope` |
| Media | Image, `figure`, Video, `track`, `iframe` |
| Form | Text, Email, Tel, Select, Radio, Checkbox, Textarea, Submit |
| Accessibility | `alt`, Label, `fieldset`, `legend`, ARIA 연결 |
| Quality | Relative Path, Validator, DevTools, Keyboard 검수 |

완성 HTML에는 Header, Hero, Course Card, 학습 순서, 시간표, 수업 Media, 안내 영역, 상담 신청 Form, FAQ, Footer를 하나의 Semantic Document로 구성했습니다.

---

## ⭐ Documentation Features

HTML Developer-Wiki 문서는 다음 원칙을 기준으로 작성했습니다.

- ✅ 실제 수업 코드 기반
- ✅ 내 코드와 강사님 코드 비교
- ✅ 존재하지 않는 차이는 만들지 않음
- ✅ 원본의 오류와 부정확한 설명 검토
- ✅ Browser의 실제 Parsing·DOM 동작 보완
- ✅ Tag 모양보다 Content 의미를 우선
- ✅ 접근성과 Keyboard 사용 환경 고려
- ✅ Relative Path와 Resource 경로 검증
- ✅ 대표 오류와 Debugging 방법 정리
- ✅ 종합실습과 최종 체크리스트 제공
- ✅ Markdown 문서 구조와 V2 품질 기준 통일

> 08번은 독립된 원본 `08_*.html` 수업 파일이 없기 때문에 존재하지 않는 내 코드·강사님 코드 비교를 만들지 않고, 01~07 내용을 실제 Semantic Page 구조로 연결하는 확장 단원으로 구성했습니다.

---

## 📖 Documentation Structure

HTML 01~08의 일반 학습 문서는 주제에 따라 세부 항목 수는 다르지만 다음 흐름을 공통 기준으로 사용합니다.

```text
문서 정보
    │
    ├── 개요 / 학습 목표
    ├── 핵심 개념
    ├── 문법과 동작 원리
    ├── 원본 코드 분석
    ├── 내 코드와 강사님 코드 비교
    ├── 오류와 개선 방향
    ├── 실무 활용
    ├── 대표 오류와 Debugging
    ├── 종합실습
    ├── 정답과 해설
    ├── 최종 체크리스트
    └── 핵심 요약
```

09번과 10번은 일반 개념 문서와 목적이 다릅니다.

```text
09 실무 코딩 스타일
→ HTML 설계·작성·리팩토링·검수 기준

10 종합실습
→ 01~09 내용을 하나의 실제 Semantic Page로 연결
```

---

## 🎯 Learning Outcome

HTML 문서를 모두 학습하면 다음 내용을 직접 설명하고 구현하는 것을 목표로 합니다.

- HTML5 Document Structure를 처음부터 작성할 수 있습니다.
- Tag, Element, Attribute, Content의 차이를 설명할 수 있습니다.
- Heading과 Paragraph를 이용해 문서 정보 계층을 구성할 수 있습니다.
- Link와 상대 경로를 이용해 Page와 Resource를 연결할 수 있습니다.
- `ul`, `ol`, `dl`을 항목 관계에 따라 선택할 수 있습니다.
- Table의 Row·Column 관계를 `th`, `scope`, `caption`으로 표현할 수 있습니다.
- Image의 정보 목적에 맞는 `alt`를 작성할 수 있습니다.
- Video·Audio·`iframe`의 기본 접근성 요구사항을 설명할 수 있습니다.
- Form Control에 Label과 제출 `name`을 연결할 수 있습니다.
- Checkbox·Radio·Select·Textarea를 실제 Form에 사용할 수 있습니다.
- GET·POST·HTTPS의 역할 차이를 설명할 수 있습니다.
- Semantic Element와 `div`를 목적에 맞게 선택할 수 있습니다.
- Heading·Landmark·Reading Order를 고려한 Page를 설계할 수 있습니다.
- Native HTML과 ARIA의 역할을 구분할 수 있습니다.
- Browser가 잘못된 Markup을 자동 보정할 수 있음을 이해할 수 있습니다.
- Validator와 DevTools로 HTML 구조를 검수할 수 있습니다.
- CSS와 JavaScript를 적용하기 전에도 이해 가능한 Semantic Page를 작성할 수 있습니다.

---

## 📂 Folder Policy

`01_HTML` 폴더는 다음 원칙으로 관리합니다.

- 실제 수업 코드와 실습 내용을 문서화합니다.
- 내 코드와 강사님 코드를 비교하되 존재하지 않는 차이를 만들지 않습니다.
- 원본의 오류는 조용히 수정하지 않고 문제와 개선 방향을 구분합니다.
- 학습 문서 파일명은 `번호_HTML_주제.md` 형식을 유지합니다.
- `README.md`는 HTML 전체 목차와 학습 가이드 역할을 담당합니다.
- 상세 문서는 README의 상대 경로 Link를 통해 이동합니다.
- 실무 코딩 스타일과 종합실습은 일반 개념 문서 뒤에 배치합니다.
- CSS·JavaScript와 관련된 표현은 HTML의 의미 구조를 설명하는 데 필요한 범위만 사용합니다.
- 완료된 문서도 전체 Developer-Wiki 구조와 품질 기준에 맞춰 지속적으로 개선합니다.

---

## 🔗 GitHub 상대 경로 규칙

HTML 폴더의 `README.md`를 기준으로 같은 폴더의 문서는 `./파일명.md` 형식으로 연결합니다.

```text
Developer-Wiki/
├── README.md
├── 01_HTML/
│   ├── README.md
│   ├── 01_HTML_기초와_문서구조.md
│   ├── ...
│   └── 10_HTML_종합실습.md
├── 02_CSS/
│   └── README.md
├── 03_JavaScript/
│   └── README.md
└── 04_Python/
    └── README.md
```

주요 상대 경로:

| 목적 | 상대 경로 |
| --- | --- |
| HTML 문서 | `./01_HTML_기초와_문서구조.md` |
| Developer-Wiki Home | `../README.md` |
| 다음 CSS | `../02_CSS/README.md` |

---

## 📎 Navigation

| Previous | Home | Next |
|:---:|:---:|:---:|
| — | [🏠 Developer-Wiki](../README.md) | [🎨 CSS](../02_CSS/README.md) |

---

## 📚 Developer-Wiki

> **Learn • Compare • Improve • Archive**

HTML은 단순히 Tag를 나열해 Browser에 화면을 출력하는 기술에서 끝나지 않습니다.

**Content의 의미와 관계를 문서 구조로 표현하고, Browser·Search Engine·Screen Reader·CSS·JavaScript가 같은 구조를 이해할 수 있도록 만드는 Web의 기반**입니다.
