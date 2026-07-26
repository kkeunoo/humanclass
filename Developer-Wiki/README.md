---
title: Developer-Wiki
version: v1.0
last_updated: 2026-07-25
status: Completed
---

# Developer-Wiki

> 국비 IT 교육 과정과 직접 작성한 코드를 기반으로 장기간 복습하고 실무에서도 참고할 수 있도록 관리하는 개인 개발 위키

## 자료 우선순위

1. `workspace_teacher` — 수업 범위와 강사님 기준 코드
2. `workspace_html` — 개인 작성 코드, 주석, 문제 풀이, 수정 과정
3. 기존 `Developer-Wiki` — 비교·정리·통합 대상

## 문서 원칙

- 강사님이 다룬 범위 안에서만 문서화한다.
- 같은 개념은 하나의 문서에서 관리한다.
- 문서는 가능한 한 **개념 → 문법 → 예제 → 실무 예제 → 주의사항 → 면접 포인트 → 요약** 순서를 따른다.
- 개인 풀이와 강사님 풀이가 구분되면 비교하고, 구분이 어려우면 공통 수업 코드로 취합한다.
- 수정 시 부분 패치가 아니라 전체 Markdown 완성본을 다시 생성한다.
- 새 규칙은 먼저 README의 Decision Log에 기록한다.

## 구조

```text
Developer-Wiki/
├── README.md
├── AUDIT_REPORT.md
├── CHANGELOG.md
├── COMMIT_MESSAGES.md
├── Comparisons/
└── Frontend/
    ├── HTML/Basic/
    ├── CSS/Basic/
    └── JavaScript/Basic/
```

## Decision Log

| 날짜 | 결정 |
|---|---|
| 2026-07-25 | README를 프로젝트의 최상위 헌법으로 지정 |
| 2026-07-25 | 강사 자료를 최우선 기준으로 사용 |
| 2026-07-25 | 실무 예제는 현재 학습 범위 안에서만 추가 |
| 2026-07-25 | 동일 개념은 하나의 문서에서 관리 |
| 2026-07-25 | 범위 초과 또는 과도하게 깊은 기존 문서는 삭제하거나 수업 수준으로 재작성 |
| 2026-07-25 | 완성본은 최상위 `Developer-Wiki` 폴더 전체를 ZIP으로 배포 |
| 2026-07-25 | 커밋 메시지는 `날짜_영역_순번.내용` 형식으로 관리 |
