---
title: Developer Wiki Audit Report
category: Project
last_updated: 2026-07-27
status: Active
---

# Developer Wiki Audit Report


## 대상

- 개인 `workspace_html`
- 개인 `workspace_python`
- 강사 `workspace_html`
- 기존 `Developer-Wiki`
- `BACKUP`은 범위 판단에서 제외

## 확인된 수업 범위

HTML 기본 태그·목록·표·링크·이미지·폼, CSS 선택자·박스·display·배경·투명도·글꼴·position·overflow·float·shadow·transition·transform·flex·media query, JavaScript 변수·연산자·조건문·반복문·배열·Date·함수·문자열·DOM·이벤트·폼·비동기·JSON·AJAX·지도·Gemini·Discord, Python hello·변수/연산·문자열·list/range·tuple.

## 확장 원칙

수업 코드에 설명이 부족한 부분은 같은 범위 안에서 동작 원리, 비교 예제, 실무 연결, 주의사항을 보강했다. CSS Display는 block, inline, inline-block, none의 차이를 실행 가능한 비교 예제로 확장했다.

## 제외 및 제한

- BACKUP 문서의 BOM 등 미학습 심화 내용
- CSS Grid 독립 문서
- localStorage 독립 문서
- 정규표현식 독립 심화 문서
- React 등 후속 기술 설명

단, `dataset`처럼 실제 수업 문제 코드에서 사용된 개념은 해당 문제 이해에 필요한 최소 범위에서만 언급했다.

## 문제 주석 탐색

`// 문제`, `//문제1-1`, 여러 줄 `/* ... 문제 ... */`, HTML title의 문제 표기를 기준으로 탐색했다. 문제 풀이가 확인된 연산자, 조건문, 반복문, 배열, 문자열, DOM, 이벤트·폼을 별도 문서로 정리했다.
