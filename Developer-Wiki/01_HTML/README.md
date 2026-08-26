# 📄 HTML Developer-Wiki

> **V3 Personal Lecture Encyclopedia** — 태그 요약이 아니라 브라우저가 문서를 파싱해 DOM을 만들고 링크·이미지·폼·접근성 기능으로 동작시키는 과정을 다시 재현하는 개인 강의 백과사전입니다.

## 🔎 V3에서 강화된 학습 규칙

기존 문서 정보, 학습 목표, 번호형 본문, 내 코드·강사님 코드 비교, 개선 예제, 디버깅, 실습·정답, 체크리스트와 핵심 요약을 유지하면서 다음 질문을 보강했습니다.

1. 이 요소는 무엇이며 어떤 의미를 전달하는가?
2. 브라우저는 소스를 어떤 부모·자식 DOM으로 해석하는가?
3. 속성값은 링크 이동·자원 요청·폼 제출 중 어디에 사용되는가?
4. 상대 경로는 어느 문서 URL을 기준으로 계산되는가?
5. 제출 시 어떤 `name=value` 데이터가 어떤 방식으로 전달되는가?
6. Elements·Network·Accessibility Tree에는 무엇이 나타나는가?
7. 내 코드와 강사님 코드의 어느 파일에서 확인하는가?

먼저 [HTML V3 동작 백과 읽기법](00_HTML_V3_동작_백과_읽기법.md)을 읽고 각 문서 마지막의 `V3 브라우저 해석 추적 카드`를 함께 확인합니다.

> **Learn • Compare • Improve • Archive**
>
> Web Content의 구조와 의미를 설계하는 기반  
> 실제 수업·실습 코드를 기반으로 개념, 비교, 개선, 복습 과정을 하나의 학습 흐름으로 정리합니다.

---

## 📌 학습 목표

- HTML의 핵심 개념과 동작 원리를 이해합니다.
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
| 01 | [01 HTML 기초와 문서구조](./01_HTML_기초와_문서구조.md) | 학습 |
| 02 | [02 HTML 기본태그](./02_HTML_기본태그.md) | 학습 |
| 03 | [03 HTML 링크와 경로](./03_HTML_링크와_경로.md) | 학습 |
| 04 | [04 HTML 목록태그](./04_HTML_목록태그.md) | 학습 |
| 05 | [05 HTML 테이블](./05_HTML_테이블.md) | 학습 |
| 06 | [06 HTML 이미지와 미디어](./06_HTML_이미지와_미디어.md) | 학습 |
| 07 | [07 HTML 폼과 입력요소](./07_HTML_폼과_입력요소.md) | 학습 |
| 08 | [08 HTML 시맨틱태그와 페이지구조](./08_HTML_시맨틱태그와_페이지구조.md) | 학습 |
| 09 | [09 HTML 실무 코딩스타일](./09_HTML_실무_코딩스타일.md) | 실무 |
| 10 | [10 HTML 종합실습](./10_HTML_종합실습.md) | 실습 |

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

[09 HTML 실무 코딩스타일](./09_HTML_실무_코딩스타일.md)

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

[10 HTML 종합실습](./10_HTML_종합실습.md)

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

HTML 문서를 완료하면 **직접 작성 → 실행 → 비교 → 문제 분석 → 개선 → 문서화**의 흐름으로 학습 내용을 설명하고 활용하는 것을 목표로 합니다.

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
| — | [🏠 Developer-Wiki](../README.md) | [🎨 CSS](../02_CSS/README.md) |

---

## 📚 Developer-Wiki

> **Learn • Compare • Improve • Archive**

배우고, 직접 작성하고, 비교하고, 개선한 내용을 다시 사용할 수 있는 개발 지식으로 축적합니다.
