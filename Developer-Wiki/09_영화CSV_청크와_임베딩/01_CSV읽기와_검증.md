# 01. CSV를 읽고 영화 ID의 관계를 확인하기

[목차](README.md) · [다음: 영화 텍스트와 청크](02_영화텍스트와_청크.md)

`movies.csv`에는 영화와 장르, `tags.csv`에는 사용자가 붙인 태그, `ratings.csv`에는 평점이 있다. 연결 키는 `movieId`다. 전체 행을 API로 내보내기 전에 일부 행을 보고, 태그·평점이 영화 목록에 없는 ID를 가리키는지 확인한다.

## 먼저: 세 CSV는 어떻게 이어지나?

영화 한 건의 기준 ID가 `movieId`다. `movies.csv`의 영화 목록을 기준으로, 같은 ID를 가진 태그와 평점을 연결해 생각한다. 이 장은 **데이터를 바꾸기 전 파일 읽기와 관계 검사**를 다룬다.

| 이해용 행 | `movieId` | 의미 |
| --- | ---: | --- |
| 영화 목록 | 1 | 영화 1이 존재 |
| 태그 목록 | 1 | 영화 1에 붙은 태그 |
| 태그 목록 | 9 | 영화 목록에 9가 없으면 연결되지 않은 ID |

이 표는 **새로 만든 개념 예시**이고 실제 CSV의 검사 결과가 아니다. 아래 `set` 차집합은 이런 연결되지 않은 **서로 다른 ID**를 세는 데 쓴다.

## CSV 파일 찾기

`Path(__file__).resolve().parents[0]`에서 현재 `util.py`의 폴더를 잡고, 그 아래 `data/ml-latest-small`에서 파일을 찾는다. 실행하는 터미널의 현재 위치가 달라도 소스 파일을 기준으로 경로를 만들려는 코드다.

### 강사님 코드 — 원본 발췌

출처: `D:/workspace_teacher/workspace_python/08_langgraph/util.py` 5–17행

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

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_python/08_langgraph/util.py` 15–27행

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

둘 다 현재 `util.py`의 위치에서 `data/ml-latest-small/파일명`을 만들고 `pd.read_csv()`로 읽는다. 읽기 오류가 나면 예외를 출력하고 `None`을 반환한다. `/read/head`는 그다음 `head()`의 기본 앞 5행을 `to_dict(orient='records')`로 바꾼다. 이는 전체 CSV가 아니라 미리보기다.

## 연결되지 않은 ID와 평점 범위

`dropna()`는 ID가 비어 있는 행을 비교 대상에서 빼고, `set`은 같은 ID가 여러 번 나온 경우 한 번만 남긴다. `tag_ids - movie_ids`는 태그 쪽에만 있는 ID 집합이다. `len(...)`은 **태그 행 수**가 아니라 그 집합의 원소 수다.

### 강사님 코드 — 원본 발췌

출처: `D:/workspace_teacher/workspace_python/08_langgraph/router/es_router.py` 27–50행

```python
@router.get('/read/valid')
def valid():
    df_movies = util.load_csv('movies.csv')
    df_tags = util.load_csv('tags.csv')
    df_ratings = util.load_csv('ratings.csv')

    # dropna : N/A 즉 결측치 즉 없는 것 제외
    notnull = df_movies['movieId'].dropna()

    # set 타입의 속성을 이용해서 id 중복 제거
    movie_ids = set(notnull)
    tag_ids = set(df_tags['movieId'].dropna())
    rating_ids = set(df_ratings['movieId'].dropna())

    result = {}
    result['no_id'] = {}
    result['no_id']['tags'] = len(tag_ids - movie_ids)
    result['no_id']['ratings'] = len(rating_ids - movie_ids)

    result['rating range'] = {}
    result['rating range']['min'] = float(df_ratings['rating'].min())
    result['rating range']['max'] = float(df_ratings['rating'].max())

    return result
```

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_python/08_langgraph/router/es_router.py` 27–54행

```python
@router.get('/read/valid')
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

`dropna()`로 빠진 ID를 제외하고 집합으로 중복 ID를 제거한다. `tag_ids - movie_ids`는 태그에는 있지만 영화 목록에는 없는 **서로 다른 ID의 개수**를 세기 위한 것이다. `rating`의 `min`, `max`도 숫자로 바꿔 반환한다. 이 코드는 CSV를 **검사**할 뿐 CSV를 수정하지 않는다. 두 원본의 알고리즘은 같다.

## 먼저 고쳐야 하는 실행 문제

아래는 자료의 내용과 별개로 **모듈을 불러올 때** 확인해야 할 부분이다. 두 원본 모두 `Literal[...]`을 사용하지만 그 이름을 import하지 않았다. 개선 예시는 원본 코드를 바꾼 기록이 아니다.

### 강사님 코드 — 원본 발췌

출처: `D:/workspace_teacher/workspace_python/08_langgraph/router/es_router.py` 1–11행

```python
from fastapi import APIRouter
import traceback
import util
import pandas as pd
from typing import Any

router = APIRouter(tags=["엘라스틱서치"])

@router.get("/read/head")
# def read(fileName) :
def read(fileName : Literal['movies.csv', 'tags.csv', 'ratings.csv'] = 'movies.csv') :
```

### 내 코드 — 원본 발췌

출처: `D:/workspace/workspace_python/08_langgraph/router/es_router.py` 1–11행

```python
from fastapi import APIRouter
import traceback
import util
import pandas as pd
from typing import Any

router = APIRouter(tags=["엘라스틱서치"])

@router.get("/read/head")
# def read(fileName) :
def read(fileName : Literal['movies.csv', 'tags.csv', 'ratings.csv'] = 'movies.csv') :
```

`read()`의 형식 주석에 `Literal`을 썼지만 양쪽 import 목록에는 `Literal`이 없다. 이 파일을 그대로 import하면 함수를 정의하는 시점에 이름을 찾지 못할 수 있다. `from typing import Any, Literal`을 추가하는 것이 작은 수정이다. 이것은 **원본에 적용한 변경이 아니라 검토로 찾은 개선 제안**이다.

## 직접 확인할 질문

1. `tags.csv`와 `movies.csv`는 어느 열로 연결하는가?
2. `set`으로 바꾼 뒤 `len`을 구하면 행 개수와 무엇이 다른가?
3. `head()`를 통해 받은 값은 CSV 전체인가?

## 추가로 알면 좋은 것

> 💡 **TIP · 수업 범위 밖:** 결측치·중복 태그를 자동으로 고치는 파이프라인은 이 검증 함수에 없다. 검사 결과를 보고 별도로 결정해야 한다.

**이 장을 읽은 뒤:** [장별 연습문제 풀기](실습/연습문제/01_CSV읽기와_검증_연습문제.md) → [다음 장에서 영화 텍스트 만들기](02_영화텍스트와_청크.md)
