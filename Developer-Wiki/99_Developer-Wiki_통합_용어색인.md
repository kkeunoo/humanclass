# 통합 용어색인

[Developer-Wiki 첫 화면](README.md)

단어에서 **정의·작은 전체 예제·결과·실제 코드 풀이가 있는 본문**으로 이동한다. 본문 내부 목차의 개념·예제·연결·빠른 정리를 사용한다. 과목별 전체 순서는 각 README에 있다. 수업 밖 확장 개념은 색인의 메인 항목으로 늘리지 않았다.

## HTML·CSS

| 찾는 말 | 설명 위치 |
| --- | --- |
| 태그·속성·문서 구조 | [HTML 기초](01_HTML/01_HTML_기초와_문서구조.md) |
| 링크·상대 경로 | [HTML 링크와 경로](01_HTML/03_HTML_링크와_경로.md) |
| `form`·`name`·입력값 | [HTML 폼](01_HTML/07_HTML_폼과_입력요소.md), [GET·POST 전송](01_HTML/07-02_HTML_폼_전송과_GET_POST.md) |
| CSS 선택자·상속 | [선택자](02_CSS/01_CSS_선택자와_적용방법.md), [우선순위와 상속](02_CSS/01-02_CSS_우선순위와_상속.md) |
| 박스 크기·배치 | [박스 모델](02_CSS/03_CSS_박스모델.md), [Flexbox](02_CSS/15_CSS_Flexbox와_유연한_레이아웃.md) |

## JavaScript

| 찾는 말 | 설명 위치 |
| --- | --- |
| 변수·자료형 | [JS 변수와 자료형](03_JavaScript/01_JavaScript_변수와_자료형.md) |
| 배열·반복 | [JS 배열 메서드](03_JavaScript/06_JavaScript_배열과_배열메서드.md) |
| 함수·콜백·타이머 | [JS 함수·콜백·타이머](03_JavaScript/08_JavaScript_함수와_콜백_타이머.md) |
| 시계·현재 시각·`setInterval` | [DOM에 시각 표시](03_JavaScript/12_JavaScript_DOM_콘텐츠생성과_스타일조작.md) |
| DOM 선택·속성·클래스 | [DOM 선택과 조작](03_JavaScript/11_JavaScript_DOM_선택과_속성_클래스조작.md) |
| `dataset`·`data-name` | [DOM 속성과 클래스](03_JavaScript/11-02_JavaScript_DOM_속성과_클래스.md) |
| 폼 입력값 | [DOM 폼과 입력값](03_JavaScript/13_JavaScript_DOM_폼요소와_입력값처리.md) |
| 이벤트 전파·위임 | [이벤트 전파와 위임](03_JavaScript/17-02_JavaScript_이벤트전파와_위임.md) |
| JSON·객체 | [객체와 JSON](03_JavaScript/19_JavaScript_객체와_JSON.md) |
| `fetch`·AJAX | [AJAX와 Fetch API](03_JavaScript/20_JavaScript_AJAX와_Fetch_API.md) |

## Python·메모리

| 찾는 말 | 설명 위치 |
| --- | --- |
| 참조·변경·복사 | [메모리와 참조](00_메모리와_참조%28Stack_Heap%29/README.md) |
| 자료형·변수·연산자 | [Python 변수와 연산자](04_Python/02_Python_변수와_연산자_입출력.md) |
| 함수·매개변수·반환 | [함수와 반환값](04_Python/11-01_Python_함수와_반환값.md), [인자 전달](04_Python/11-02_Python_함수_인자전달.md) |
| 리스트·딕셔너리 | [리스트](04_Python/04_Python_리스트와_데이터처리.md), [딕셔너리](04_Python/07_Python_딕셔너리.md) |
| 클래스·상속 | [클래스](04_Python/12_Python_클래스.md), [상속](04_Python/13_Python_상속과_다형성.md) |
| 예외·파일 | [예외](04_Python/14_Python_예외처리.md), [파일 입출력](04_Python/10_Python_파일입출력과_직렬화.md) |

## SQL·FastAPI

| 찾는 말 | 설명 위치 |
| --- | --- |
| `SELECT`·`WHERE` | [SQL SELECT](05_SQL/01_SQL_기초와_SELECT.md), [조건](05_SQL/02_SQL_WHERE와_조건연산자.md) |
| `JOIN`·서브쿼리 | [SQL JOIN](05_SQL/12_SQL_JOIN.md), [서브쿼리](05_SQL/11_SQL_서브쿼리.md) |
| DDL·DML·트랜잭션 | [SQL DDL](05_SQL/14_SQL_DDL과_제약조건.md), [DML](05_SQL/15_SQL_DML.md), [트랜잭션](05_SQL/16_SQL_Transaction.md) |
| 재귀 CTE·부모/자식 댓글 연습 | [SQL 재귀 CTE](05_SQL/18_SQL_Recursive_CTE.md) |
| `APIRouter`·CORS·폼·Pydantic | [FastAPI Router와 입력](06_FastAPI/02_FastAPI_Router_Request_Pydantic_CRUD.md) |
| Jinja `extends`·`include`·매크로 | [Jinja 템플릿](06_FastAPI/03_FastAPI_Jinja2_템플릿.md) |
| `RedirectResponse`·303·307 | [함수 호출과 리다이렉트](06_FastAPI/04_FastAPI_Response_Redirect_의존성주입.md) |
| SQLite·`commit()`·`rollback()` | [Python SQLite](06_FastAPI/06_Python_SQLite와_Transaction.md) |
| SQLModel·`Depends(get_session)` | [FastAPI DB CRUD](06_FastAPI/07_FastAPI_MariaDB_SQLModel_사원_CRUD.md) |
| 비밀번호 해시·`verify()` | [해시 실습](06_FastAPI/07-02_비밀번호_해시_실습.md) |
| `UploadFile`·`FileResponse` | [파일 업로드·다운로드](06_FastAPI/08_FastAPI_파일업로드_다운로드.md) |
| `Cookie()`·세션·미들웨어 | [쿠키·세션·로그인 검사](06_FastAPI/09_FastAPI_Cookie_Session_로그인.md) |

request.headers 직접 읽기와 response_model은 수업 밖 TIP이다. 범위 분류 문서는 안내이며 실제 보충은 관련 본문 하단에서 읽는다.

## 데이터 분석·기초 머신러닝

| 찾는 말 | 설명 위치 |
| --- | --- |
| pandas·`DataFrame`·`read_csv` | [와인 CSV와 입력·정답](07_데이터분석과_머신러닝/01_Pandas_와인데이터와_학습입력.md) |
| `train_test_split`·`stratify` | [학습·시험 분리](07_데이터분석과_머신러닝/01_Pandas_와인데이터와_학습입력.md) |
| `RandomForestClassifier`·`fit`·`predict_proba` | [학습과 예측](07_데이터분석과_머신러닝/02_RandomForest_학습과_예측.md) |
| F1·ROC AUC·`GridSearchCV`·`StratifiedKFold` | [평가와 교차 검증](07_데이터분석과_머신러닝/03_평가와_교차검증.md) |

## Elasticsearch·RAG

| 찾는 말 | 설명 위치 |
| --- | --- |
| Elasticsearch `text`·`keyword`·`bulk` | [연결·적재](08_Elasticsearch와_RAG/01_연결과_문서적재.md) |
| `match`·`term`·`range`·CRUD | [검색과 수정](08_Elasticsearch와_RAG/02_검색과_CRUD.md) |
| 청크·겹침·`dense_vector`·임베딩 | [청크와 임베딩](08_Elasticsearch와_RAG/03_청크와_임베딩.md) |
| `knn`·하이브리드·RRF | [벡터와 하이브리드 검색](08_Elasticsearch와_RAG/04_벡터와_하이브리드검색.md) |
| RAG·검색 문맥·답변 | [RAG 질문응답](08_Elasticsearch와_RAG/05_RAG_질문응답.md) |

## 영화 CSV·청크·임베딩

| 찾는 말 | 설명 위치 |
| --- | --- |
| MovieLens·`movieId`·`read_csv` | [CSV 읽기와 검증](09_영화CSV_청크와_임베딩/01_CSV읽기와_검증.md) |
| 장르·태그·`groupby`·겹치는 청크 | [영화 텍스트와 청크](09_영화CSV_청크와_임베딩/02_영화텍스트와_청크.md) |
| Gemini·OpenAI 임베딩·action 목록 | [임베딩과 벌크 적재](09_영화CSV_청크와_임베딩/03_임베딩과_미완성경계.md) |


## 영화 추천·시간·평가

| 찾는 말 | 설명 위치 |
| --- | --- |
| Counter·most_common·CBF | [특징으로 검색문 만들기](09_영화CSV_청크와_임베딩/04_영화검색과_콘텐츠기반추천.md) |
| 사용자별 최신 평점·test/train | [시간 분할](09_영화CSV_청크와_임베딩/05_시간분할과_협업필터링.md#concepts) |
| KNNWithMeans·cosine·raw/inner ID | [협업 필터링](09_영화CSV_청크와_임베딩/05_시간분할과_협업필터링.md) |
| Recall@K·threshold·관련 영화 | [추천 평가](09_영화CSV_청크와_임베딩/06_Recall_at_K_추천평가.md) |
| 복사한 후반부의 출처 | [영화 단원 목차](09_영화CSV_청크와_임베딩/README.md) |

## 증상에서 다시 찾기

| 막힌 지점 | 먼저 확인할 본문 |
| --- | --- |
| print와 return이 헷갈림 | [Python 반환값](04_Python/11-01_Python_함수와_반환값.md) |
| 같은 리스트·dict가 같이 바뀜 | [참조](00_메모리와_참조%28Stack_Heap%29/README.md), [청크의 공유 참조](08_Elasticsearch와_RAG/03_청크와_임베딩.md) |
| 수정 뒤 화면과 저장값이 다름 | [화면 Todo](06_FastAPI/05_FastAPI_Jinja_Todo_CRUD.md) |
| F1·AUC가 다른 방향으로 변함 | [모델 평가](07_데이터분석과_머신러닝/03_평가와_교차검증.md), [실제 CSV 종합실습](07_데이터분석과_머신러닝/종합실습.md) |
| 검색 결과 총수와 목록 길이가 다름 | [검색 응답](08_Elasticsearch와_RAG/02_검색과_CRUD.md), [RRF 후보 총수](08_Elasticsearch와_RAG/04_벡터와_하이브리드검색.md) |
| 사용자가 있는데 없다고 나옴 | [Series 포함 검사](09_영화CSV_청크와_임베딩/05_시간분할과_협업필터링.md) |
| Recall이 -1.0 | [평가할 관련 영화 없음](09_영화CSV_청크와_임베딩/06_Recall_at_K_추천평가.md) |

확인되지 않은 그래프 실행·운영 서비스·고급 지표는 색인의 필수 진도로 늘리지 않았다. [전체 순서](README.md) · [첨부 메모 대응](편집기록/99_첨부메모_반영_및_이후첨부.md)

<!-- 이전 목차 주소 보존 -->
<a id="elasticsearchrag"></a>
<a id="htmlcss"></a>
<a id="javascript"></a>
<a id="python메모리"></a>
<a id="sqlfastapi"></a>
<a id="데이터-분석기초-머신러닝"></a>
<a id="영화-csv청크임베딩"></a>
<a id="통합-용어색인"></a>
