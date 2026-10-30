# 01. 영화 CSV — 파일 읽기·미리보기·ID 관계 검사부터 시작하기 — 연습문제

[본문](../../01_CSV읽기와_검증.md) · [문제 목차](README.md)

실제 수업 내용을 바탕으로 **새로 구성한 연습문제**다. 원본·당시 내 코드·새 개선안을 구별한다. 예상 → 이유 → 한 가지 변경 순서로 푼다.

## 목표와 준비

세 CSV의 역할과 movieId 관계를 설명한다. DataFrame 미리보기와 전체 자료를 구별하고 집합 차집합이 행 수가 아닌 고유 ID를 세는 이유를 이해한다. 파일 기준 경로·읽기 실패·타입 주석 문제를 따로 읽는다.

[본문 3절](../../01_CSV읽기와_검증.md#example)의 폴더·설치·입력·실행 조건부터 확인한다. 아래 필요한 파일 전체를 같은 구조로 저장한다. 가져오는 함수·모델 정의도 빠뜨리지 않는다.

## 문제 1. 실행 결과 예상

**movies.csv**

```csv
movieId,title,genres
1,Example Movie,Comedy|Drama
2,Second Movie,Action
```

**tags.csv**

```csv
userId,movieId,tag,timestamp
10,1,Fun,100
11,1,fun,110
12,9,unknown,120
13,9,unknown,130
```

**ratings.csv**

```csv
userId,movieId,rating,timestamp
10,1,4.0,100
10,2,5.0,110
11,9,2.5,120
```

**csv_tools.py**

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

**example.py**

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

실행 전에 결과를 먼저 적는다. 자료의 모양·분류 결과·확률·점수·현재 변수의 대상을 구별한다.

<details>
<summary>풀이</summary>

```text
행 수: 2 4 3
미리보기: Example Movie
태그의 미등록 ID: [9]
평점의 미등록 ID: [9]
평점 범위: 2.5 5.0
```

load_csv의 정의가 같은 폴더 파일을 읽어 DataFrame을 돌려준다. inspect_ids는 세 표를 받아 각 ID 집합의 차이를 계산한다. 태그 4행 중 영화 9는 두 번 있지만 결과 [9]에는 한 번만 나온다. 새 함수는 오류를 숨겨 None으로 바꾸지 않는 개선안이다. 원본처럼 읽기 실패를 처리하려면 호출자가 실패를 어떻게 알지 정해야 한다.

| 새 자료 | 행 수 | 고유 영화 ID |
| --- | ---: | --- |
|movies | 2 | 1·2 |
|tags | 4 | 1·9 |
|ratings | 3 | 1·2·9 |
|tags - movies | 행 수 아님 | 9 하나 |

</details>

## 문제 2. 이유 설명

1. 영화 9의 태그가 두 행인데 차집합 개수는 왜 하나인가?
2. head 결과는 전체 파일인가?
3. load_csv의 실패 None과 정상 빈 표는 같은가?

<details>
<summary>풀이</summary>

1. set이 같은 ID를 한 번만 남기기 때문이다.
2. 지정한 앞부분의 미리보기다.
3. 실패와 정상 반환 자료를 구별해야 한다.

</details>

## 문제 3. 한 가지만 바꾸기

| 한 가지만 변경 | 예상 |
| --- | --- |
|영화 9를 movies에 추가 | 두 미등록 ID 목록이 비어짐 |
|영화 9의 태그 행 하나 더 | 미등록 고유 ID는 여전히 하나 |
|head(1)을 head(2)로 | 미리보기 행 증가·CSV 수정 없음 |
|CSV 이름을 잘못 전달 | 새 예제는 파일 오류를 드러냄 |

<details>
<summary>막힐 때 확인</summary>

None에 head가 없으면 원래 파일 읽기 실패부터 확인한다. movieId KeyError는 파일과 헤더를 살핀다. ID 개수와 행 수가 다른 것은 set의 목적에 따른 결과일 수 있다. 평점 범위가 비어 있으면 유효한 평점 수와 결측을 먼저 확인한다.

</details>

## 채점과 복습

정상 출력뿐 아니라 입력 열·정답·분할·평가 대상의 차이도 설명한다. 새 예제는 독립 실행이며 실제 검색·AI 서비스 성공과 구별한다. TIP 확장은 필수 조건이 아니다. 정의→입력→호출→반환→다음 평가의 흐름을 연결한다.
