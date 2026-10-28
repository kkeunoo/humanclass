# JavaScript — 수업 원본 기반 개편본

강사님 코드와 내 실제 수업 코드를 비교해 원본 번호 **01–22의 학습 내용**을 정리했습니다. 읽기 편하도록 분리한 본문 34개와 기존 자료 분류 추가편이 있습니다. 17장 폼 제출과 메뉴·Todo의 주요 동작은 외부 전송 없이 로컬 화면에서 확인했습니다. 기존 Wiki의 파일 이름 28개는 모두 이 폴더에서 열리며, 옛 문서 **내부의 모든 앵커 주소까지 동일하게 유지한 것은 아닙니다.**

처음부터 다시 공부할 때는 [JavaScript 코드를 읽는 순서](00_JavaScript_V3_동작_백과_읽기법.md)로 **입력·현재 상태·실행 시점·결과**를 먼저 적는다. 각 장은 개념과 작은 결과를 이해한 뒤 양쪽 원본의 같은 점과 다른 점을 비교한다. 새 연습문제는 본문에서 아직 배우지 않은 문법을 필수 조건으로 앞당기지 않도록 읽는 순서에 맞췄다.

## 읽는 순서

- [01_JavaScript_변수와_자료형](01_JavaScript_변수와_자료형.md)
- [02_JavaScript_연산자](02_JavaScript_연산자.md)
- [03_JavaScript_조건문과_Switch](03_JavaScript_조건문과_Switch.md)
- [04_JavaScript_반복문과_배열순회](04_JavaScript_반복문과_배열순회.md)
- [05_JavaScript_While과_DoWhile](05_JavaScript_While과_DoWhile.md)
- [06_JavaScript_배열과_배열메서드](06_JavaScript_배열과_배열메서드.md)
- [07_JavaScript_Date와_날짜처리](07_JavaScript_Date와_날짜처리.md)
- [08_JavaScript_함수와_콜백_타이머](08_JavaScript_함수와_콜백_타이머.md)
- [08-02_JavaScript_함수참조와_콜백](08-02_JavaScript_함수참조와_콜백.md)
- [08-03_JavaScript_타이머와_취소](08-03_JavaScript_타이머와_취소.md)
- [09_JavaScript_화살표함수와_TV상태관리](09_JavaScript_화살표함수와_TV상태관리.md)
- [09-02_JavaScript_TV상태관리](09-02_JavaScript_TV상태관리.md)
- [10_JavaScript_문자열과_문자열메서드](10_JavaScript_문자열과_문자열메서드.md)
- [11_JavaScript_DOM_선택과_속성_클래스조작](11_JavaScript_DOM_선택과_속성_클래스조작.md)
- [11-02_JavaScript_DOM_속성과_클래스](11-02_JavaScript_DOM_속성과_클래스.md)
- [12_JavaScript_DOM_콘텐츠생성과_스타일조작](12_JavaScript_DOM_콘텐츠생성과_스타일조작.md)
- [12-02_JavaScript_DOM_요소생성과_삽입](12-02_JavaScript_DOM_요소생성과_삽입.md)
- [12-03_JavaScript_DOM_스타일과_퀴즈](12-03_JavaScript_DOM_스타일과_퀴즈.md)
- [13_JavaScript_DOM_폼요소와_입력값처리](13_JavaScript_DOM_폼요소와_입력값처리.md)
- [14_JavaScript_동기비동기와_이벤트루프](14_JavaScript_동기비동기와_이벤트루프.md)
- [15_JavaScript_DOM이벤트와_키보드스크롤제어](15_JavaScript_DOM이벤트와_키보드스크롤제어.md)
- [15-02_JavaScript_키보드와_스크롤](15-02_JavaScript_키보드와_스크롤.md)
- [16_JavaScript_마우스이벤트와_드래그복사제어](16_JavaScript_마우스이벤트와_드래그복사제어.md)
- [16-02_JavaScript_선택과_복사이벤트](16-02_JavaScript_선택과_복사이벤트.md)
- [17_JavaScript_폼이벤트와_이벤트전파_실전문제](17_JavaScript_폼이벤트와_이벤트전파_실전문제.md)
- [17-02_JavaScript_이벤트전파와_위임](17-02_JavaScript_이벤트전파와_위임.md)
- [17-03_JavaScript_주문_로그인_피자실습](17-03_JavaScript_주문_로그인_피자실습.md)
- [17-04_JavaScript_메뉴와_Todo실습](17-04_JavaScript_메뉴와_Todo실습.md)
- [18_JavaScript_브라우저이동과_지도우편번호](18_JavaScript_브라우저이동과_지도우편번호.md)
- [19_JavaScript_객체와_JSON](19_JavaScript_객체와_JSON.md)
- [20_JavaScript_AJAX와_fetch](20_JavaScript_AJAX와_fetch.md)
- [20-02_JavaScript_날씨응답_필터와_표시](20-02_JavaScript_날씨응답_필터와_표시.md)
- [21_JavaScript_외부AI_API요청과_대화기록](21_JavaScript_외부AI_API요청과_대화기록.md)
- [22_JavaScript_웹훅_POST요청](22_JavaScript_웹훅_POST요청.md)

## 복습과 새로 구성한 실습

- [실습 폴더 — 34개 장별 연습문제](실습/README.md)
- [23 실무 코딩 스타일](23_JavaScript_실무_코딩스타일.md) — 수업 코드에서 확인한 오류를 바탕으로 새 예제 검토
- [24 종합실습](24_JavaScript_종합실습.md) — 메뉴·Todo·폼·이벤트 연결

위 세 자료는 **원본 수업 23·24번 파일이 아니라 새로 작성한 연습**이다. 원본 퀴즈와 내 당시 풀이의 비교는 해당 본문 17장에 남겨 둔다.

## 추가로 알면 좋은 것

- [기존 자료의 학습 범위 분류](추가편_기존자료_학습범위_분류.md)
- [옛 99장 메서드 치트시트 안내](99_JavaScript_자료형별_메서드_치트시트.md)

## 학습 범위와 검증

양쪽 `workspace_html/javascript`에는 23·24·99 번호의 수업 원본 파일이 없습니다. 23·24는 **수업에서 배운 문법을 다시 적용하는 새 연습**으로 작성했고 원본이라고 표시하지 않았습니다. 기존 Wiki의 수업 밖 내용은 [추가로 알면 좋은 것](추가편_기존자료_학습범위_분류.md)으로 구분했습니다. `dataset`은 강사님 퀴즈와 사용자 확인에 따라 [17-03 실습](17-03_JavaScript_주문_로그인_피자실습.md)의 본문에 포함했습니다.

원본 발췌·문서 링크와 로컬 화면 검수 범위는 [최종 검증 기록](../편집기록/03_JavaScript_최종_검증기록.md)에 있습니다. 외부 날씨·AI·웹훅 서비스의 실제 응답은 검증하지 않았으며, 요청 구조와 수업 코드의 실행 흐름을 설명합니다. 다른 과목은 [전체 Wiki 첫 화면](../README.md)에서 이어 읽습니다.

[BACKUP 대응표](../편집기록/03_JavaScript_BACKUP_대응표.md) · [진행 기록](../편집기록/03_JavaScript_진행과_재개기록.md)
