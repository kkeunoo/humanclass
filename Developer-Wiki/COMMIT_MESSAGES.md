---
title: Git Commit Message
version: v3.0
last_updated: 2026-07-27
status: Completed
---

# Git Commit Message

이번 배포본은 전체 ZIP을 한 번에 교체하는 방식이므로 통합 커밋 하나만 사용한다.

## Commit Message

```text
0727_DeveloperWiki_1.수업범위 기반 상세 학습문서와 문제풀이 개선완료
```

## 포함 파일

- `Developer-Wiki/` 내부 전체 파일
- 기존 문서 수정 내역
- 상세 문제 해결 과정이 추가된 Problems 문서
- 비교 기준과 변경 내역 문서

## Git 명령어

저장소 루트가 `Developer-Wiki` 폴더 내부인 경우:

```bash
git add -A
git commit -m "0727_DeveloperWiki_1.수업범위 기반 상세 학습문서와 문제풀이 개선완료"
```

상위 저장소에서 `Developer-Wiki` 폴더만 관리하는 경우:

```bash
git add -A Developer-Wiki/
git commit -m "0727_DeveloperWiki_1.수업범위 기반 상세 학습문서와 문제풀이 개선완료"
```

커밋 전에는 반드시 다음 명령으로 다른 작업이 함께 포함되지 않았는지 확인한다.

```bash
git status
git diff --stat
```
