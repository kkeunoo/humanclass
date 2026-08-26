# 🎨 CSS Developer-Wiki

> **V3 Personal Lecture Encyclopedia** — 속성 요약이 아니라 브라우저가 선택자를 연결하고 값을 계산해 박스를 배치하고 화면에 그리는 과정을 다시 재현하는 개인 강의 백과사전입니다.

## 🔎 V3에서 강화된 학습 규칙

기존 문서 정보, 학습 목표, 번호형 본문, 내 코드·강사님 코드 비교, 개선 예제, 디버깅, 실습·정답, 체크리스트와 핵심 요약을 유지하면서 다음 질문을 보강했습니다.

1. 이 속성과 레이아웃은 무엇이며 왜 배우는가?
2. 선택자는 실제 어느 HTML 요소와 일치하는가?
3. 캐스케이드·상속·우선순위에서 어떤 선언이 왜 이기는가?
4. 길이와 퍼센트는 어느 요소·글자·viewport를 기준으로 계산되는가?
5. content·padding·border·margin과 최종 위치는 얼마인가?
6. 화면 결과와 Styles·Computed·Layout 패널에는 무엇이 보이는가?
7. 내 코드와 강사님 코드의 어느 파일에서 확인하는가?

먼저 [CSS V3 동작 백과 읽기법](00_CSS_V3_동작_백과_읽기법.md)을 읽고 각 문서 마지막의 `V3 렌더링 추적 카드`를 함께 확인합니다.

> **Learn • Compare • Improve • Archive**
>
> HTML 구조를 Layout과 Visual Interface로 표현  
> 실제 수업·실습 코드를 기반으로 개념, 비교, 개선, 복습 과정을 하나의 학습 흐름으로 정리합니다.

---

## 📌 학습 목표

- CSS의 핵심 개념과 동작 원리를 이해합니다.
- 예제를 직접 작성하고 실행 결과를 확인합니다.
- 내 코드와 강사 코드의 실제 차이를 비교합니다.
- 오류 원인을 찾고 더 나은 작성 방식으로 개선합니다.
- 실무 코딩 스타일을 적용해 가독성과 유지보수성을 높입니다.
- 종합실습으로 개별 개념을 하나의 흐름으로 연결합니다.

---

## 🗺️ 학습 흐름

```text
기초 개념
    ↓
핵심 문법과 예제
    ↓
응용과 실습
    ↓
코드 비교와 오류 분석
    ↓
실무 코딩 스타일
    ↓
종합실습
    ↓
Reference
```

---

## 📚 Documentation

| No | Document | 분류 |
|:--:|---|:--:|
| 01 | [01 CSS 선택자와 적용방법](./01_CSS_선택자와_적용방법.md) | 학습 |
| 02 | [02 CSS 단위와 색상](./02_CSS_단위와_색상.md) | 학습 |
| 03 | [03 CSS 박스모델](./03_CSS_박스모델.md) | 학습 |
| 04 | [04 CSS Display와 요소배치](./04_CSS_Display와_요소배치.md) | 학습 |
| 05 | [05 CSS 투명도와 요소숨김](./05_CSS_투명도와_요소숨김.md) | 학습 |
| 06 | [06 CSS 배경이미지와 배경속성](./06_CSS_배경이미지와_배경속성.md) | 학습 |
| 07 | [07 CSS 텍스트와 글꼴](./07_CSS_텍스트와_글꼴.md) | 학습 |
| 08 | [08 CSS Position과 요소위치](./08_CSS_Position과_요소위치.md) | 학습 |
| 09 | [09 CSS Overflow와 스크롤](./09_CSS_Overflow와_스크롤.md) | 학습 |
| 10 | [10 CSS Float와 Clear](./10_CSS_Float와_Clear.md) | 학습 |
| 11 | [11 CSS 그림자와 시각효과](./11_CSS_그림자와_시각효과.md) | 학습 |
| 12 | [12 CSS Transition과 상태변화](./12_CSS_Transition과_상태변화.md) | 학습 |
| 13 | [13 CSS Transform과 요소변형](./13_CSS_Transform과_요소변형.md) | 학습 |
| 14 | [14 CSS 미디어쿼리와 반응형](./14_CSS_미디어쿼리와_반응형.md) | 학습 |
| 15 | [15 CSS Flexbox와 유연한 레이아웃](./15_CSS_Flexbox와_유연한_레이아웃.md) | 학습 |
| 16 | [16 CSS 실무 코딩스타일](./16_CSS_실무_코딩스타일.md) | 실무 |
| 17 | [17 CSS 종합실습](./17_CSS_종합실습.md) | 실습 |

---

## 🧭 추천 학습 방법

1. README에서 전체 문서 범위를 확인합니다.
2. 번호 순서대로 문서를 읽고 예제를 직접 작성합니다.
3. 실행 결과와 실제 동작을 확인합니다.
4. 비교 항목이 있으면 내 코드와 강사 코드의 차이를 확인합니다.
5. 원본 오류와 개선 사항을 구분해서 이해합니다.
6. 대표 오류와 Debugging 과정을 다시 재현합니다.
7. 실무 코딩 스타일에서 작성 기준을 정리합니다.
8. 종합실습에서 앞의 내용을 연결합니다.

---

## 💼 실무 코딩 스타일

[16 CSS 실무 코딩스타일](./16_CSS_실무_코딩스타일.md)

앞에서 학습한 문법을 반복하기보다 실제 Project에서 코드를 어떻게 작성·구조화·리팩토링할지에 집중합니다.

```text
Naming
→ Structure
→ Readability
→ Maintainability
→ Error Prevention
→ Refactoring
→ Review
```

---

## 🚀 종합실습

[17 CSS 종합실습](./17_CSS_종합실습.md)

앞에서 학습한 내용을 하나의 문제 해결 과정으로 연결합니다.

```text
개념 학습
    ↓
예제 작성
    ↓
코드 비교
    ↓
오류 분석
    ↓
실무 작성 기준
    ↓
종합실습
```

---

## ⭐ Documentation Features

- ✅ 실제 수업·실습 코드 기반
- ✅ 내 코드와 강사 코드 비교
- ✅ 존재하지 않는 차이는 임의로 만들지 않음
- ✅ 원본 오류와 개선 방향 구분
- ✅ 실제 동작 원리와 실무 활용 설명
- ✅ 대표 오류와 Debugging 정리
- ✅ 실무 코딩 스타일 제공
- ✅ 종합실습 제공
- ✅ GitHub 상대 경로 Navigation 통일

---

## 📖 Documentation Structure

```text
Document Information
        ↓
Learning Objectives
        ↓
Core Concepts
        ↓
Syntax & Examples
        ↓
Practical Usage
        ↓
Code Comparison
        ↓
Improvements
        ↓
Common Mistakes
        ↓
Problems & Answers
        ↓
Final Checklist
        ↓
Key Summary
```

> 실제 원본이나 비교 대상이 없는 경우에는 존재하지 않는 비교 내용을 만들지 않고 해당 주제에 필요한 개념과 검수 내용을 중심으로 구성합니다.

---

## 🎯 Learning Outcome

CSS 문서를 완료하면 **직접 작성 → 실행 → 비교 → 문제 분석 → 개선 → 문서화**의 흐름으로 학습 내용을 설명하고 활용하는 것을 목표로 합니다.

---

## 📂 Folder Policy

- 학습 문서는 번호 순서를 유지합니다.
- `README.md`는 해당 Subject의 목차와 학습 가이드 역할을 담당합니다.
- 같은 폴더 문서는 `./파일명.md`로 연결합니다.
- Developer-Wiki Home은 `../README.md`로 연결합니다.
- 이전·다음 Subject는 `../폴더명/README.md`로 연결합니다.
- 실무 코딩 스타일과 종합실습은 정규 학습 마지막 단계에 배치합니다.
- `99_` 문서는 정규 순서와 분리된 Reference로 관리합니다.

---

## 📎 Navigation

| Previous | Home | Next |
|:---:|:---:|:---:|
| [📄 HTML](../01_HTML/README.md) | [🏠 Developer-Wiki](../README.md) | [⚡ JavaScript](../03_JavaScript/README.md) |

---

## 📚 Developer-Wiki

> **Learn • Compare • Improve • Archive**

배우고, 직접 작성하고, 비교하고, 개선한 내용을 다시 사용할 수 있는 개발 지식으로 축적합니다.
