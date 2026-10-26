# 02 CSS — 중간저장과 재개 기록

2026-09-18 · **이전 중간저장 이력**

이후 재개하여 작성한 [최종 개편·검증 기록](02_CSS_최종_검증기록.md)을 현재 상태의 기준으로 사용한다. 아래 내용은 당시 완료·미완료 상태를 보존한 기록이다. 최신 사용자 중지 기준은 20% 미만이며 아래의 25%는 과거 요청이다.

[현재 CSS 목차](../02_CSS/README.md)

사용자는 남은 사용량이 약 25%이면 저장하고 멈추도록 요청했다. 5시간 사용량 28% 잔여를 확인한 시점부터 새 편집을 중단하고 저장·검사만 진행했다. 주간 잔여는 당시 61%였다.

## 작성한 범위

- 01~15 기본 장: 양쪽 수업 원본 비교, 작동 설명, 잘못된 주석 교정, 짧은 복습 작성.
- 01-02 우선순위·상속, 03-02 마진·정렬: 긴 주제를 별도 문서로 분리.
- 16: 기본 교정 위치 안내와 학생 개인 실습의 border 오타 사례. 별도 추가편은 미작성.
- 17: 실제 display1·display2 비교, 기본 종합복습 재구성 및 실행용 HTML 1개.
- README: 완료 전임을 표시한 임시 목차. 전체 Wiki README는 만들지 않음.

## 원본 재대조로 수정한 판단

- vmin·vmax, calc, :root·CSS 변수·var, font-display:swap의 기본 사용은 실제 양쪽 원본에 있어 메인.
- flex-basis 명시적 실험과 그림자 spread 값은 비교 코드에 없어 추가편으로 분리. 초기 분류안보다 실제 원본을 우선했다. 검색 부재를 학습하지 않았다는 절대 증명으로 주장하지 않는다.
- 강사님 파일명은 04_dispaly.html·13_transform.html, 내 파일명은 04_display.html·13_tranform.html이다.
- 강사님 display 실습은 css/실습, 내 대응본은 css/실습_tc. display1·display2 내용이 같음을 확인했으므로 독립 구현의 우열을 만들지 않았다.
- 사용자가 제외한 바이브코딩 시험·Python 개인 CSS 프로젝트는 근거로 사용하지 않았다.

## 브라우저에서 실제 확인한 것

로컬 HTTP 서버와 Codex 내장 브라우저로 확인했다. 아래 표는 검사한 관찰만 기록한다. 모든 예제를 모든 브라우저에서 검증했다는 뜻은 아니다.

| 항목 | 관찰 결과 |
| --- | --- |
| 내 선택자 | div2 분홍 테두리, 자식 strong 40px·자손 strong 16px, 둘 다 파랑 |
| 체크 상태 | 두 번째 체크박스 선택 후 20px·다음 span 취소선 |
| 단위 | 루트 16px. 내 %·em 24/36/54, rem 24/24/24. 강사님 em 구역 24/36/24 |
| 내 단위 HTML | 닫는 div 부족으로 rem 구역의 실제 부모가 em 구역임 |
| 박스 모델 | second 212×262, box 302×302, border-box 상자 300×300 |
| 마진 | 부모 위에서 첫 자식까지 30px, 형제 사이 50px |
| inline-block | parent3 두 자식 각 202px, 같은 top, 간격 0 |
| 숨김 재구성 | 시작 버튼에서 Tab 후 투명한 버튼 포커스. hidden·none 제외, none 너비 0 |
| 배경 | contain·cover·fixed·center·auto 등 원본 속성의 계산값 확인. 외부 이미지의 시각 품질 검증은 별도 |
| 글꼴 원본 | p.size 자식 요소 없음, 자식이라 적힌 div는 body 아래 16px. weight 2000 무효로 400 |
| 말줄임 | clientWidth 200, scrollWidth 1677, ellipsis. 외부 폰트의 실제 글리프 사용은 확정하지 않음 |
| absolute | 기준 조상 유무에 따라 위치가 달라짐. 계산 display는 block |
| calc·변수 | 자식 중심이 부모 중심에서 x·y 각각 1px 차이, 배경 brown 확인 |
| sticky | 계산 top:50px만 확인. 스크롤 경계 실동작은 아직 확인하지 않음 |
| overflow | 가로 목록 clientWidth 300·scrollWidth 574, y:scroll 때 x:auto |
| clearfix | 부모 높이 122px, 후행 가상 요소 block·clear:both. 자식 float 유지 |
| 그림자 | text 2/2/4, box 4/4/6. hover 그림자 표시 후 상자 너비 152px 유지 |
| transition | hover 진입 때 0.5s·중간 너비, 최종 200px. 이탈 직후 0s·100px |
| transform | 중앙 정렬 자식과 부모 중심의 x·y 차이 0 |
| 미디어쿼리 | iframe 599·600px에서 li block·ul opacity 0, 601px에서 inline-block·opacity 1 |
| Flex | 현재 nowrap, 시각 순서 3/1/4/5/2, 높이 300px, grow 0. 주석 실험 활성화 검증은 미실시 |
| 기본 종합복습 | 1000px 화면: 부모 900·자식 405씩 같은 줄. 400px: 부모 360·자식 200씩 줄바꿈 |

검증용 도구에서 첫 숨김 실행 파일 추출이 원본 조각을 선택하는 오류가 있었다. 전체 DOCTYPE 예제를 추출하도록 고친 후 다시 검증했다. iframe 조회·숫자 변환의 도구 제한도 문서 내용 오류와 구분하여 다른 읽기 방식으로 확인했다.

## 중간저장 무결성 검사

- 현재 Markdown 21개, 내부 링크 57개: 대상 확인.
- 원본 인용 55곳: 원본 해당 행과 일치.
- 보존 원본 524개: 해시 일치.
- 코드블록·접기 여닫기 및 실행용 HTML 1개와 문서 내용 일치 확인.
- 옛 CSS 앵커 호환성과 최종 렌더링 검사는 아직 수행하지 않았다.

## 재개 순서

1. 사용량부터 새로 확인한다. 25% 중지 기준을 유지한다.
2. 현재 01~17 초안에서 누락·중복·표현·원본 대응을 한 번 더 검토한다. 원본 발췌는 임의 수정하지 않는다.
3. 미검증 범위 중 학습 설명에 필요한 것만 보완한다: fixed·sticky 스크롤, transform 합성 차이, Flex 주석 실험, 배경 비교 및 수정 예제 등. 실제 확인과 원리 설명을 구분한다.
4. 기존 16·17과 BACKUP의 추가 기능을 추가편으로 재구성한다. Grid·BEM·새 선택자·논리 속성·clamp·새 뷰포트 단위·flex-basis·spread·다크 모드·reduced-motion 등의 분류를 반영한다. 기본 문제에 요구하지 않는다.
5. 기존 00 읽기 안내·REFACTOR_REVIEW 처리, 옛 색인의 CSS 링크·앵커 이동 안내, BACKUP 11개 문서의 처리 위치를 정리한다.
6. Markdown 표시·접기·내부 링크, 기본 실습과 문서 일치, 원본 해시를 최종 검사한다. CSS README를 완성하고 최종 기록·완성 ZIP을 만든다.
7. CSS 전체 완료 후 사용량을 보고하고 다음 과목으로 넘어가기 전에 멈춘다. 전체 Wiki README·통합 색인은 마지막에 편집한다.

## 작업 파일

- `work/css-excerpts.json`: 원본 인용 경로·행·내용 55곳.
- `work/fill-css.mjs`: 새 excerpt 표식만 원문으로 치환. 기존 본문을 다시 만들지 않음.
- `work/prepare-css-preview.mjs`: 원본의 로컬 검증용 복사본과 경계 검사 페이지 생성.
- `work/css-preview`: 로컬 검증 자료. 원본 수정이 아님.
- `work/css-checkpoint.mjs`, `work/css-checkpoint-check.json`: 무결성 검사와 결과.
- `work/css-resume.json`: 재개 상태.

서버를 다시 열 때는 작업 폴더의 work/css-preview를 로컬 127.0.0.1:8765로 제공한다. 브라우저 검증 탭과 서버는 이번 저장 후 닫는다. 다음 작업은 CSS의 남은 부분이며 JavaScript가 아니다.
