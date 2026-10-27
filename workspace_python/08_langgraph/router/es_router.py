from fastapi import APIRouter, Query
import traceback
import util
import pandas as pd
from typing import Any

import os

from elasticsearch import helpers

router = APIRouter(tags=["엘라스틱서치"])

@router.get("/read/head")
# def read(fileName) :
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
    
def makeContent():
    df_movies = util.load_csv('movies.csv')
    df_tags = util.load_csv('tags.csv')

    # pandas
    # 데이터 프레임 : 2차원 배열
    # 시리즈(1줄 씩) : 1차원 값
    result = pd.DataFrame()
    result['movieId'] = df_movies['movieId']
    # df에서는 str로 형변환 해준 뒤에 strip해야 적용 됨
    result['title'] = df_movies['title'].astype(str).str.strip()

    # 장르는 a|b|c 형식으로 되어있다
    # 그래서 list로 바꾸겠다.
    def parse_genre(genres):
        result = []
        if str(genres).strip() == '' or str(genres).strip() == '(no genres listed)':
            return result

        list_genre = str(genres).split('|')
        for genre in list_genre :
            result.append(genre.strip().lower())

        return result

    # 장르의 리스트가 쌓임 (parse_genre에서 공백제거 후 담은것을)
    # pandas에서도 map을 제공해줌
    result['list_genre'] = df_movies['genres'].map(parse_genre)

    # 배열을 주면 여러 개의 컬럼을 가져올 수 있다
    # pandas에서도 깊은복사 copy()를 제공
    tags = df_tags[['movieId', 'tag']].copy()
    tags['tag'] = tags['tag'].astype(str).str.strip().str.lower()

    # pandas에서는 group by 처럼 중복을 제거해주는 함수가 제공됨
    tags = tags.drop_duplicates(['movieId', 'tag'])

    # pandas의 data frame 특성인데, 리스트 안에 컬럼이 아니라 True인것만 반복 시킬 수 있음
    # tags = tags[tags['tag'] != ''].drop_duplicates(['movieId', 'tag'])

    # print(tags.head())
    # return result

    movie_tags = {}
    # df를 딕셔너리로 변환
    for info in tags.to_dict(orient='records') :
        id = info['movieId']
        tag = info['tag']

        # dict의 key중에서 id가 없다면 key를 id로 추가 후 빈 list로
        if id not in movie_tags :
            movie_tags[id] = []
        movie_tags[id].append(tag)

    # 위 코드를 한 줄로 줄이면 아래처럼 할 수 있음
    # pandas 에는 groupby를 제공함, groupby한 tag를 list로 형변환하고 dict로 변환
    # tags.groupby('movieId') : data frame인 tags를 movieId로 groupby
    # ['tag'] : groupby한 것에서 tag항목을 꺼내고
    # agg(list) : 꺼낸 항목을 list로 만들어서
    # to_dict() : 딕셔너리로 변환
    '''
        to_dict() 까지 한 결과
        {
            movidId1 : [tag1, tag2],
            movieId2 : [tag11, tag12]
        }
    '''
    movie_tags = tags.groupby('movieId')['tag'].agg(list).to_dict()
    # print(movie_tags)

    # 람다를 사용해서 df_movies의 movieId를 전부 돌면서 movie_tags에서 해당하는 tag를 result['list_tag'] 에 저장
    # lambda는 넣게되면 하나하나 돌면서 lambda가 작동되기 때문에 이후 체이닝, 리턴 등 값으로 추가 작업할 수 있음
    # → 그때그때 처리해야 하는 일들을 풀어 적어놓고, 그때그때 동작하도록 (지금 동작하는 당시의)
    result['list_tag'] = df_movies['movieId'].map(lambda id : movie_tags.get(id, []))

    # 파이썬의 리스트는 +를 제공
    # [1,2] + [3,4] == [1,2,3,4]
    # list_temp = [result['title']] + result['list_genre'] + result['list_tag']
    # content_text = ' '.join(list_temp)

    # map() : 한 컬럼을 대상으로 반복
    # apply() : 모든 컬럼을 대상으로 반복 (axis : 축)
    # axis : 기본값은 0
    #           0 : 위에서 아래로 읽기
    #           1 : 왼쪽에서 오른쪽으로
    result['content_text'] = result.apply(
        lambda info : ' '.join([info['title']] + info['list_genre'] + info['list_tag']).strip(),
        axis=1
    )

    # * : 언팩킹, js의 ...와 같음
    # 배열을 하나씩 분리해 주는 것
    # *[1,2,3] = 1,2,3
    # result['content_text'] = result.apply(
    #     lambda info : ' '.join([info['title']] , *info['list_genre'] , *info['list_tag']).strip(),
    #     axis=1
    # )

    # reset_index : pandas 내부 index를 재정리
    # drop=True를 안 해주면, 132 라고하면 123이 아니라 1323이 되는것을 막기 위함 (새로 추가됨)
    # → 엉망인 것은 버려라
    return result.reset_index(drop=True)

@router.get('/make/content')
def content():
    # result는 data frame이기 때문에 dict로 변환해서 return
    dataFrame = makeContent()
    return dataFrame.head(10).to_dict(orient='records')

# 한 줄로 만들어진 content_text 를 적당히 쪼개고 겹쳐서 chunk로 만들기
def makeChunk():
    size_chunk = 50
    overlap:int = 15
    # 자료형을 미리 지정하기 chunks = []
    # Any를 import해서 object처럼 아무거나 들어와도 되도록 사용할 수 있음
    chunks:list[dict[str, Any]] = []

    dataFrame = makeContent()
    content = dataFrame.to_dict(orient='records')

    step = size_chunk - overlap
    for idx_content, info in enumerate(content) :
        text = info.get('content_text', '').strip()
        if not text :
            continue

        # for idx_start in range(0, len(text), step):
        for idx, idx_start in enumerate(range(0, len(text), step)):
            chunk = text[idx_start : idx_start+size_chunk]
            if chunk :
                chunks.append({
                    'index' : idx_content,
                    'movieId' : int(info['movieId']),
                    'title' : str(info['title']),
                    'genres' : list(info['list_genre']),
                    'tags' : list(info['list_tag']),
                    'content' : chunk,
                    'chunk_index' : idx
                })

    return chunks

@router.get('/make/chunk')
def chunk():
    return makeChunk()[0:10]

@router.get('/make/embedding/gemini')
def embedding():
    target = makeChunk()[0:10]
    actions = util.embedding_with_gemini(target)

    return actions

@router.get('/make/embedding/openai')
def embedding():
    target = makeChunk()[0:10]
    # target = makeChunk()
    actions = util.embedding_with_openai(target)

    return actions

@router.get('/es/health')
def health():
    return {
        'msg': util.es.ping()
    }

@router.post('/es/bulk')
def bulk():
    # target = makeChunk()[0:10]
    target = makeChunk()
    actions = util.embedding_with_openai(target)

    # 1. 만약에 엘라스틱서치에 인덱스가 없다면 새로 만들기(있으면 기존 인덱스에 데이터 넣기)
    # 있으면 삭제하기
    # if util.es.indices.exists(index=os.getenv('ES_INDEX')) :
    #     util.es.indices.delete(index=os.getenv('ES_INDEX'))

    # 없으면 create index
    if not util.es.indices.exists(index=os.getenv('ES_INDEX')) :
        '''
        # 기본 Chunk 구조
        {
            'index' : idx_content,
            'movieId' : int(info['movieId']),
            'title' : str(info['title']),
            'genres' : list(info['list_genre']),
            'tags' : list(info['list_tag']),
            'content' : chunk,
            'chunk_index' : idx,
            'embedding' : content의 벡터
        }
        '''

        mappings = {
            'properties': {
                'index' : {'type' : 'integer'},
                'movieId' : {'type' : 'integer'},
                'title' : {'type' : 'text'}, # 제목은 완벽히 같은 단어검색 용으로 keyword 사용
                'genres' : {'type' : 'keyword'},
                'tags' : {'type' : 'text'},
                'content' : {'type' : 'text'},
                'chunk_index' : {'type' : 'integer'},
                'embedding' : {
                    'type' : 'dense_vector',
                    'dims' : 768
                }, # 보통 실무에서는 마지막에 , 를 붙여놓음 (복붙하기 편하도록)
            }
        }

        util.es.indices.create(
            index=os.getenv('ES_INDEX'),
            mappings=mappings
        )

    # 2. bulk로 es에 데이터 넣기
    success, errors = helpers.bulk(
        util.es,
        actions,
        stats_only=False 
    )

    return {
        'msg' : {
            'succ' : success,
            'errors' : errors
        }
    }

def search_movies(keyword: str, size: int = 10):
    response = util.es.search(
        index=os.getenv('ES_INDEX'),
        query={
            'multi_match' : {
                'query' : keyword,
                # 'fields' : ['title', 'genres', 'tags', 'content']
                'fields' : ['title^4', 'genres', 'tags^2', 'content^3'] # ^Number 로 가중치를 줄 수 있음
            }
        },
        size=size
    )

    return response

@router.get('/es/select/multi_match')
def multi_match(keyword, size=10):
    response = search_movies(keyword, size)

    return {
        'msg' : util.formatter(response)
    }

def terms_movieId(ids: list):
    # term은 keyword (where id = 1)
    # terms는 list로 여러 개 검색 (where id in (1,2,3))
    response = util.es.search(
        index=os.getenv('ES_INDEX'),
        query={
            'terms' : {
                'movieId' : ids,
            }
        },
        size=len(ids)*5
    )

    return response

@router.get('/es/select/terms')
def terms(ids:list = Query()):
    response = terms_movieId(ids)

    return {
        'msg' : util.formatter(response)
    }
