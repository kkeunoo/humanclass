# 01. 영화 CSV — 파일 읽기·미리보기·ID 관계 검사부터 시작하기

[영화 자료·추천 목차](README.md) · [읽기 안내](00_영화자료와_추천_읽기안내.md)

영화·태그·평점은 서로 다른 표다. 모델이나 검색에 넣기 전에 한 행의 의미와 연결 키, 파일을 읽지 못한 경우를 먼저 이해한다. 현재 수업 파일이 확장되었으므로 옛 행 번호와 미완성 안내도 다시 확인한다.

**이 장의 목차:** [목표](#learn) · [개념](#concepts) · [예제](#example) · [내 코드](#my-code) · [연결](#connections) · [평가](#review) · [비교](#teacher) · [결과·실험](#results) · [TIP·출처](#tips) · [복습](#practice)

<a id="learn"></a>

## 1. 이 장에서 배울 것

세 CSV의 역할과 movieId 관계를 설명한다. DataFrame 미리보기와 전체 자료를 구별하고 집합 차집합이 행 수가 아닌 고유 ID를 세는 이유를 이해한다. 파일 기준 경로·읽기 실패·타입 주석 문제를 따로 읽는다.

<a id="concepts"></a>

## 2. 무엇이며, 왜 필요한가

### 같은 영화가 여러 표에 나오는 이유

movies의 한 행은 영화 한 건이고, tags는 사용자가 영화에 붙인 태그 기록, ratings는 사용자의 평점 기록이다. 태그와 평점에는 같은 movieId가 여러 번 나올 수 있다. 사용자·시점이 다른 기록이기 때문이다. 같은 ID가 보인다는 사실만으로 모두 잘못된 중복이라고 지우면 안 된다.

| 표 | 연결에 쓰는 열 | 다른 핵심 열 | 한 영화의 행 |
| --- | --- | --- | --- |
| movies | movieId | title·genres | 영화 목록의 기준 |
| tags | movieId | userId·tag·timestamp | 여러 태그 가능 |
| ratings | movieId | userId·rating·timestamp | 여러 평점 가능 |

이 관계는 SQL의 여러 표를 ID로 연결하는 생각과 통한다. 다만 여기서는 파일을 읽어 pandas로 직접 검사한다. CSV에 있다고 DB의 외래키 제약이 자동으로 걸리는 것은 아니다.

### 행 수와 서로 다른 ID 수는 다르다

태그에 없는 영화 9의 기록이 두 번 있다면 잘못 연결된 행은 두 개일 수 있지만 고유 ID는 하나다. `set(tag_ids) - set(movie_ids)`는 태그 쪽에만 있는 ID를 남긴다. dropna는 비교 전에 비어 있는 ID를 빼고 set은 같은 값을 한 번만 남긴다. 이 검사는 빠진 ID 자체를 채우거나 CSV를 수정하지 않는다.

head()는 기본 앞 다섯 행의 미리보기다. `to_dict(orient='records')`는 행마다 dict를 만든 목록으로 바꾼다. 미리보기 결과를 받았다고 전체 파일을 다 전송한 것이 아니며, 표를 출력한 것과 자료 검증을 끝낸 것도 다르다.

### 파일 경로와 프로그램 실행 위치

__file__은 현재 모듈 파일의 위치다. Path로 그 파일의 폴더를 구해 data 아래 경로를 만들면 터미널의 작업 폴더에 덜 의존할 수 있다. 원본 load_csv는 실패를 출력한 뒤 None을 반환하므로 다음 코드에서 head나 열 선택을 하려면 성공 여부를 확인해야 한다. “파일 없음”과 “읽었지만 행 없음”은 다른 상태다.

> 📚 **출처 · 본문 설명 확인:** [pandas read_csv](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html) · [DataFrame.to_dict](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_dict.html) · [Python 집합](https://docs.python.org/ko/3/library/stdtypes.html#set-types-set-frozenset). 배운 의미 확인 근거다. 아래 표·전체 예제·풀이를 외부 문장 그대로 옮기지 않았다. 확인일: 2026-10-30.

<a id="example"></a>

## 3. 작은 예제로 먼저 이해하기

**새 설명 예제 · 필요한 파일 전체.** 같은 장의 폴더 구조를 유지한다. pandas가 필요하다. 아래 다섯 파일을 같은 폴더에 저장하고 `python example.py`를 실행한다. CSV는 관계를 보여 주기 위한 가상 자료이며 실제 MovieLens의 특정 행이 아니다. 원본 폴더·외부 서버를 읽거나 바꾸지 않는다.



**[movies.csv](실습/책형_복습/01_CSV읽기와_검증/movies.csv) — 새 예제 전체 파일**

```csv
movieId,title,genres
1,Example Movie,Comedy|Drama
2,Second Movie,Action
```

**[tags.csv](실습/책형_복습/01_CSV읽기와_검증/tags.csv) — 새 예제 전체 파일**

```csv
userId,movieId,tag,timestamp
10,1,Fun,100
11,1,fun,110
12,9,unknown,120
13,9,unknown,130
```

**[ratings.csv](실습/책형_복습/01_CSV읽기와_검증/ratings.csv) — 새 예제 전체 파일**

```csv
userId,movieId,rating,timestamp
10,1,4.0,100
10,2,5.0,110
11,9,2.5,120
```

**[csv_tools.py](실습/책형_복습/01_CSV읽기와_검증/csv_tools.py) — 새 예제 전체 파일**

```python
from pathlib import Path
import pandas as pd


def load_csv(name):
    path = Path(__file__).resolve().parent / name
    return pd.read_csv(path)


def inspect_ids(movies, tags, ratings):
    movie_ids = set(movies['movieId'].dropna())
    tag_ids = set(tags['movieId'].dropna())
    rating_ids = set(ratings['movieId'].dropna())
    return {
        'tag_unknown_ids': sorted(tag_ids - movie_ids),
        'rating_unknown_ids': sorted(rating_ids - movie_ids),
        'rating_min': float(ratings['rating'].min()),
        'rating_max': float(ratings['rating'].max()),
    }
```

**[example.py](실습/책형_복습/01_CSV읽기와_검증/example.py) — 새 예제 전체 파일**

```python
from csv_tools import load_csv, inspect_ids

movies = load_csv('movies.csv')
tags = load_csv('tags.csv')
ratings = load_csv('ratings.csv')
result = inspect_ids(movies, tags, ratings)
print('행 수:', len(movies), len(tags), len(ratings))
print('미리보기:', movies.head(1).to_dict(orient='records')[0]['title'])
print('태그의 미등록 ID:', result['tag_unknown_ids'])
print('평점의 미등록 ID:', result['rating_unknown_ids'])
print('평점 범위:', result['rating_min'], result['rating_max'])
```

load_csv의 정의가 같은 폴더 파일을 읽어 DataFrame을 돌려준다. inspect_ids는 세 표를 받아 각 ID 집합의 차이를 계산한다. 태그 4행 중 영화 9는 두 번 있지만 결과 [9]에는 한 번만 나온다. 새 함수는 오류를 숨겨 None으로 바꾸지 않는 개선안이다. 원본처럼 읽기 실패를 처리하려면 호출자가 실패를 어떻게 알지 정해야 한다.

**실행 결과:**

```text
행 수: 2 4 3
미리보기: Example Movie
태그의 미등록 ID: [9]
평점의 미등록 ID: [9]
평점 범위: 2.5 5.0
```

<a id="my-code"></a>

## 4. 내가 작성한 코드를 따라 읽기

### 내 코드 — 원본

출처: `D:/workspace/workspace_python/08_langgraph/util.py` 18–30행 · **원본 발췌**

```python
def load_csv(fileName) :
    BASE_DIR = Path(__file__).resolve().parents[0] # 08_langgraph 폴더로 이동
    DOCUMENT_FILE = BASE_DIR / "data" / "ml-latest-small" / fileName
    # print(DOCUMENT_FILE)

    frame = None
    try:
        frame = pd.read_csv(DOCUMENT_FILE)
    except Exception as e :
        traceback.print_exc()
        print('read_csv 파일 로딩 오류', e)

    return frame
```

**발췌 바로 풀이:** util.py 기준 data/ml-latest-small 아래를 읽는다. 실패하면 traceback을 출력하고 초기값 None을 돌려준다. CSV 읽기 성공과 뒤의 열 선택 성공을 같은 단계로 생각하지 않는다. 키나 환경변수의 실제 값을 공개할 필요는 없다.
### 내 코드 — 원본

출처: `D:/workspace/workspace_python/08_langgraph/router/es_router.py` 38–64행 · **원본 발췌**

```python
def valid():
    df_movies = util.load_csv('movies.csv')
    df_tags = util.load_csv('tags.csv')
    df_ratings = util.load_csv('ratings.csv')

    # pandas에서 movieId를 전체 select 
    # dropna : N/A(Not Available) 결측치, 즉 없는걸 제외해라
    notnull = df_movies['movieId'].dropna()

    # set 타입의 속성을 이용해서 id 중복 제거
    # set 타입은 json, list와 다르게 중복을 관리해 줌 { 1, 2 } key만 있는 것
    movie_ids = set(notnull)
    tag_ids = set(df_tags['movieId'].dropna())
    rating_ids = set(df_ratings['movieId'].dropna())

    # 중복되지 않은 ID가 있다면 길이를 체크하여 표시
    result = {}
    result['no_id'] = {}
    result['no_id']['tags'] = len(tag_ids - movie_ids)
    result['no_id']['ratings'] = len(rating_ids - movie_ids)

    # 별점의 min, max 확인
    result['rating range'] = {}
    result['rating range']['min'] = float(df_ratings['rating'].min())
    result['rating range']['max'] = float(df_ratings['rating'].max())

    return result
```

**발췌 바로 풀이:** 세 표의 movieId를 각각 집합으로 만들고 차집합의 길이를 센다. 결과는 고유 미등록 ID 수이며 해당 행 수와 다르다. 평점의 최소·최대도 반환하지만 범위를 벗어난 행을 삭제하는 코드는 없다.
### 내 코드 — 원본

출처: `D:/workspace/workspace_python/08_langgraph/router/es_router.py` 21–35행 · **원본 발췌**

```python
def read(fileName : Literal['movies.csv', 'tags.csv', 'ratings.csv'] = 'movies.csv') :
    print('fileName :', fileName)
    frame = util.load_csv(fileName)
    if frame is None :
        return {'ERROR': "파일을 불러오지 못했습니다"}

    '''
        head : 상위 몇 개의 데이터만 추출 (기본값 : 5)
        astype : 형변환, 기본값:NumPy.int64
        to_dict : dict로 변환
        orient='records' : 컬럼명:값 형태 
                           기본값=dict : 인덱스가 키가 된다
    '''
    preview = frame.head().astype(object).to_dict(orient='records')
    return preview
```

**발췌 바로 풀이:** read는 로딩 결과가 None이면 안내를 먼저 반환하고, 성공하면 앞 다섯 행을 object 변환 뒤 records 목록으로 만든다. Literal 이름은 import가 빠져 있다. 현재 Python 3.14 검사에서는 지연된 주석을 실제로 평가할 때 NameError가 났다. 모든 버전에서 함수 정의 즉시 실패한다고 단정하지 않는다.

현재 read는 load_csv의 반환이 None이면 오류 안내를 먼저 반환한다. 반면 valid는 세 표를 바로 사용하므로 같은 실패 보호가 있는 것은 아니다. read의 타입 주석에는 여전히 Literal을 사용하지만 import에는 Any만 있다. Python 버전과 주석 평가 방식에 따라 함수 정의 또는 FastAPI의 경로 등록·타입 해석 시 이름 해석 문제가 생길 수 있다. from typing import Any, Literal을 추가하는 것은 원본에 적용하지 않은 개선안이다. 검증에서는 라우터 전체를 몰래 고쳐 실행하지 않고 필요한 정의와 타입 문제를 따로 확인한다.

<a id="connections"></a>

## 5. import·함수·입력·출력이 연결되는 흐름

`read/valid 경로 → util.load_csv 전체 정의 → util.py 기준 data/ml-latest-small → pandas 표 → head 또는 ID 집합 검사 → dict 반환`이다. 새 csv_tools의 두 함수도 전체 정의를 제공했다. ratings의 userId는 뒤 협업 필터링의 사용자, movieId는 영화이며 서로 바꿔 쓰지 않는다.

<a id="review"></a>

## 6. 잘한 점·아쉬운 점·개선 방향

**잘한 점:** 경로를 모듈 기준으로 구성하고 미리보기·ID 관계·평점 범위를 확인했다. **아쉬운 점:** None 반환 뒤 호출자가 바로 열을 선택하면 읽기 오류가 다른 오류로 이어질 수 있다. **개선:** 실패와 빈 표를 구별하고 ID 누락 행·중복 행·고유 미등록 ID를 각각 기록한다. 최신 원본의 수정도 함께 반영해 과거 결함을 현재 상태로 남기지 않는다.

원본 오류·수업용 단순화·목적에 따른 설계를 나눈다. 새 개선안은 당시 내 코드나 D 드라이브 수정본이 아니다.

<a id="teacher"></a>

## 7. 강사님 코드가 도움이 되는 비교



load_csv와 valid의 핵심 알고리즘은 양쪽이 같아 중복 인용을 줄였다. read의 None 확인과 Literal 이름 해석도 양쪽에 같은 기준을 적용한다. 주석이 더 길다는 이유가 아니라 반환 계약과 실제 입력 조건을 기준으로 비교한다.

<a id="results"></a>

## 8. 결과를 추적하고 한 가지 바꾸기

| 새 자료 | 행 수 | 고유 영화 ID |
| --- | ---: | --- |
|movies | 2 | 1·2 |
|tags | 4 | 1·9 |
|ratings | 3 | 1·2·9 |
|tags - movies | 행 수 아님 | 9 하나 |

| 한 가지만 변경 | 예상 |
| --- | --- |
|영화 9를 movies에 추가 | 두 미등록 ID 목록이 비어짐 |
|영화 9의 태그 행 하나 더 | 미등록 고유 ID는 여전히 하나 |
|head(1)을 head(2)로 | 미리보기 행 증가·CSV 수정 없음 |
|CSV 이름을 잘못 전달 | 새 예제는 파일 오류를 드러냄 |

None에 head가 없으면 원래 파일 읽기 실패부터 확인한다. movieId KeyError는 파일과 헤더를 살핀다. ID 개수와 행 수가 다른 것은 set의 목적에 따른 결과일 수 있다. 평점 범위가 비어 있으면 유효한 평점 수와 결측을 먼저 확인한다.

**확인 범위:** 새 예제는 임시 폴더에서 Python 처리·요청 모양·고정 응답 가공을 확인한다. Elasticsearch나 AI 서비스의 실제 연결·적재·검색·임베딩·답변 성공을 재현한 것은 아니다. 원본 함수의 별도 검사도 외부 호출을 기록 대역으로 바꾼 범위이며 원본 파일과 패키지는 수정하지 않는다.

<a id="tips"></a>

## 9. 추가로 알면 좋은 것과 출처

> 💡 **TIP · 수업 범위 밖:** 결측·중복을 자동 보정하는 파이프라인·파일 업로드·엄격한 스키마 검증은 추가 학습이다. 실제 MovieLens 원자료의 이용 조건은 데이터에 포함된 README를 따른다. 이 작은 예제는 새 가상 자료다.



09 소스는 작업 중 변경을 감지해 2026-10-30 확보한 사본을 기준으로 집필했다. 이후 변경은 별도 재검토 대상이다. 확인한 라이브러리 의미와 수업 밖 확장을 구분한다. 위 출처는 본문의 설명 근거이며 TIP에 적힌 새 주제를 이미 배운 것으로 간주하지 않는다.

<a id="practice"></a>

## 10. 복습과 빠른 정리

1. 영화 9의 태그가 두 행인데 차집합 개수는 왜 하나인가?
2. head 결과는 전체 파일인가?
3. load_csv의 실패 None과 정상 빈 표는 같은가?

<details>
<summary>풀이 — 먼저 결과와 이유를 적은 뒤 펼치기</summary>

1. set이 같은 ID를 한 번만 남기기 때문이다.
2. 지정한 앞부분의 미리보기다.
3. 실패와 정상 반환 자료를 구별해야 한다.

</details>

| 빠른 찾기 | 핵심 |
| --- | --- |
|movieId | 영화 연결 키 |
|set 차집합 | 고유 미등록 ID |
|head | 미리보기 |
|records | 행별 dict 목록 |

[장별 연습문제](실습/연습문제/01_CSV읽기와_검증_연습문제.md) · [다음: 영화 텍스트와 청크](02_영화텍스트와_청크.md)
