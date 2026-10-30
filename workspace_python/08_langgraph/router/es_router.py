from fastapi import APIRouter, Query
import traceback
import util
import pandas as pd
from typing import Any

import os

from elasticsearch import helpers

from collections import Counter

import math

from surprise import Dataset, Reader, KNNWithMeans

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

###################
# 추천 시스템
###################

@router.get('/recommend/test/counter')
def test_counter():
    str = 'hello world'
    print( Counter(str) )
    # Counter({'l': 3, 'o': 2, 'h': 1, 'e': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1})

    list_counter = ['hi', 'hey', 'hi', 'hello', 'hi', 'nihao', 'hey']
    print( Counter(list_counter) )
    # Counter({'hi': 3, 'hey': 2, 'hello': 1, 'nihao': 1})

    food_counter = Counter()
    list_food = ['김밥', '달빵', '마라탕', '김밥', '김밥', '달빵']
    for food in list_food :
        food_counter.update(food)
    print(1, food_counter)
    # Counter({'김': 3, '밥': 3, '달': 2, '빵': 2, '마': 1, '라': 1, '탕': 1})

    food_counter2 = Counter()
    for food in [list_food] :
        food_counter2.update(food)
    print(2, food_counter2)
    # Counter({'김밥': 3, '달빵': 2, '마라탕': 1})

    favorite_foods = [
        ['밥', '치킨'],
        ['산낙지', '육회', '광어회'],
        ['밥', '라면', '짜장면'],
        ['햄버거', '라면', '밥']
    ]
    food_counter3 = Counter()
    for foods in favorite_foods :
        food_counter3.update(foods)
    print(3, food_counter3)
    #Counter({'밥': 3, '라면': 2, '치킨': 1, '산낙지': 1, '육회': 1, '광어회': 1, '짜장면': 1, '햄버거': 1})

# CBF(Content-Based Filtering) 콘텐츠 기반 필터링 추천
# '내가 뭘 좋아했지?'
def content_based_filtering(list_movieId: list):
    selected = terms_movieId(list_movieId)

    # return selected

    genre_counter = Counter()
    tag_counter = Counter()
    for hit in selected['hits']['hits'] :
        source = hit['_source']
        print(source)
        genre_counter.update( source.get('genres', []) )
        tag_counter.update( source.get('tags', []) )

    print('genre_counter : ', genre_counter)
    print('tag_counter : ', tag_counter)

    max = 5
    # 장르와 태그를 각각 집계한 뒤 빈도가 높은 것 부터 검색어에 반영한다
    # most_common() : 카운터에서 가장 일반적인 것 추출 (리턴은 내용, 숫자가 나옴)
    # - most_common의 기본값은 None이며 '모두 다'
    # terms_genre = [term for term, count in genre_counter.most_common(max)]
    # terms_tag = [term for term, count in tag_counter.most_common(max)]
    # 사용하지 않는 변수의 경우 보통 '_' 로 표기 함 (필수 리턴이나 사용하지 않기 때문에)
    terms_genre = [term for term, _ in genre_counter.most_common(max)]
    terms_tag = [term for term, _ in tag_counter.most_common(max)]

    # 배열 더하기로 합칠 수 있지만 하나씩 더해 나갈 때마다 메모리를 차지한다
    # terms = terms_genre + terms_tag

    terms = []
    terms.extend(terms_genre)
    terms.extend(terms_tag)
    # return terms

    # 단점 : 중복 데이터가 있을 수 있다
    # ' '.join(terms)
    # 그래서 set에 넣어보자
    # 단, set에 넣으면 순서를 보장하지 않게 된다
    # ' '.join( set(terms) )
    # 순서를 유지하면서 중복을 제거하고 싶을 때
    # dict.fromkeys() 를 사용하면 된다
    # [a,b,a] >>>> {a: None, b: None}
    # 이렇게 중복 제거 한 것을 join 하면 key만 빼올 수 있다
    query = ' '.join( dict.fromkeys(terms) )
    response = search_movies(query)

    return response


@router.get('/recommend/cbf')
def cbf(list_movieId: list[int] = Query(...)):
    response = content_based_filtering(list_movieId)

    return response['hits']['hits']

def split_train_test(test_size: float = 0.2):
    '''
        과거 평점을 학습시켜고, 미래 평점으로 평가하자
        test_size : 미래 평점의 비율(평가, 테스트용 정답 데이터의 비율)

        사용자 별로
        최신 평점은 평가용
        과거 평점은 학습용

        평점이 한 건 뿐인 사용자는 학습 데이터에만 둔다
        만약에 timestamp가 같다면 원본 행 순서로 정렬한다
    '''

    # 평점 파일 읽기
    frame_ratings = util.load_csv('ratings.csv')

    # 원본 유지를 위해 깊은복사하여 사용
    data = frame_ratings.copy()

    # 읽어 온 csv의 길이를 가져와서 원본의 순서대로 row num 생성
    data['original_order'] = range( len(data) )

    # timestamp를 숫자타입으로 변경
    # errors='coerce' : 변경이 안 되는 것은 NaN으로 강제로 변경
    # errors='ignore' : 변경 실패 시 원본 유지
    # errors='raise' : ValueError 발생하고 즉시 중단
    valid_data = pd.to_numeric( data['timestamp'], errors='coerce' )

    # N/A가 아닌 것만 뽑아준다 
    # data[ True or False] >>>> 참인 행(row, document)만 반환
    valid_data = data[data['timestamp'].notna()].copy()

    # 시간이 N/A 즉, 비어있는 것만 뽑아준다
    no_time = data[data['timestamp'].isna()].copy()

    test_indices = []

    # userId가 같은 데이터끼리 group by 한다
    # sort의 기본값은 True이고, userId로 정렬하지 않고 원래 등장 순서를 유지
    # False로 하면서 userId로 다시 한 번 정렬하는 것
    # 원래 id, value이나 id를 사용하지 않을 것이기 때문에 '_' 로 처리
    for _, group in valid_data.groupby('userId', sort=False) :

        # 평점을 하나만 준 사용자는 건너뛰기
        # 하나만 있는 것은 학습과 정답 데이터로 나눌 수 없기 때문에 건너뜀
        if len(group) <= 1 :
            continue

        # 과거와 미래를 나누기 위해서 timestamp 기준으로 정렬한다
        # sort_values : 같은 게 있다면 original_order 기준으로 정렬해라
        # kind='stable' : 그래도 같은게 있다면, 정렬 전 순서 유지
        # kind에 사용할 수 있는 것
        # quicksort(기본값), mergesort, heapsort, stable
        # 오름차순
        ordered = group.sort_values(['timestamp', 'original_order'], kind='stable')

        # 전체 데이터 중 test_size 비율로 뽑았다
        # 소수점으로 나올 수 있기 때문에 0.4등의 결과를 1로 ceil을 사용하여 올림 처리
        # test_count = math.ceil(len(ordered) * test_size)
        # if test_count < 1 :
        #     test_count = 1

        # if test_count > len(ordered) - 1 :
        #     test_count = len(ordered) - 1

        # max : 둘 중에 큰 값을 돌려준다
        # 그걸 이용하여 최소값을 지정할 때 사용
        # max(1, test_count)
        # min : 둘 중에 작은 값을 돌려준다
        # 그걸 이용하여 최대값을 지정할 때 사용
        # min(test_count, len(ordered) - 1)

        # 위에 있는 코드를 아래처럼 합칠 수 있다
        test_count = min(len(ordered) - 1, max(1, math.ceil(len(ordered) * test_size)))

        # 슬라이싱을 써도 되지만, tail로 사용
        # tail : 끝에서 몇 개 (head와 반대, 기본값은 5)
        # 미리 시간 오름차순으로 정렬해 두었기 때문에 최신 데이터는 끝에 있다
        # .index : index만 모은다(dataframe이 가진 PK) 이후 원본에서 이걸 제외하면 train data
        test_indices.extend(ordered.tail(test_count).index.tolist())

    # 실제 테스트 데이터 추출
    # loc[]에 index를 주면 해당 index 자료만 뽑아 옴
    test = valid_data.loc[test_indices].copy()
    
    # 학습 데이터 추출
    train = valid_data.drop(index=test_indices)

    # 내가 활용하기 위해 추가한 row num으로 원래 순서대로 재정렬(복구) 후 컬럼 지우기
    # 그러면 거의 원본에서 필요한 데이터만 추출한 결과를 만들 수 있다
    test = test.sort_values('original_order', kind='stable').drop(columns='original_order')
    train = train.sort_values('original_order', kind='stable').drop(columns='original_order')

    # reset_index : pandas 내부 index를 재정리
    # drop=True를 안 해주면, 132 라고하면 123이 아니라 1323이 되는것을 막기 위함 (새로 추가됨)
    # → 엉망인 것은 버려라
    return test.reset_index(drop=True), train.reset_index(drop=True)

# CF(Collaborative Filtering) 협업 필터링 추천
# '다른 사람들은 뭘 좋아했지?'
def collaborative_filtering(userId, top_k=10):
    test, train = split_train_test()

    # 판다스에서 []안에 []를 넣으면 여러 컬럼을 지정할 수 있음 (보통 2차원 배열)
    # 판다스에서 한 줄 : 시리즈 / 엑셀처럼 2차원 : 데이터프레임
    # 아래에서 []를 하나 빼면 시리즈처럼 한 줄로 쭉 나오게 됨
    data = train[['userId', 'movieId', 'rating']].copy()
    if userId not in data['userId'] :
        raise ValueError(f'{userId}을/를 찾을 수 없습니다. 일단 차가운 시선을 듣고 다시 시도해주세요.')

    # Reader는 필수
    # 평점 데이터를 해석할 수 있도록 해주는 것(기왕이면 범위도 알려줌)
    # 만약 rating_scale을 아래와 같이 줬는데 0.3이라면 이상치로 판단하여 쳐냄
    reader = Reader(rating_scale=(0.5, 5.0))

    # pandas의 DataFrame을 Surprise의 데이터셋으로 변경한다
    data_set = Dataset.load_from_df(
        data[ ['userId', 'movieId', 'rating'] ],
        reader
    )

    # 위에서 surprise가 알아듣게 바꾸고, 지금은 모델 학습에 사용할 자료 구조로 변환한다
    train_set = data_set.build_full_trainset()

    # 유클리드 거리
    #   - 피타고라스 정리 같이 직선 거리를 뜻 함
    # 코사인 거리
    #   - 거리를 보지 않고 방향(각도)만 비교
    #   - 100편 액션 영화를 좋아한 사람과, 1편의 액션을 좋아한 사람은 같은 취향(방향)
    #   - 문서 길이나 단어의 빈도 수는 달라도 주제가 비슷한지 판단할 때 좋다

    # sim_options의 name에 들어갈 수 있는 것들
    # msd(거리) : 기본값(Mean Squared Difference), 빠르고 대용량 데이터에 좋음 (평균 제곱을 하면 더 극명해짐)
    # cosine(방향) : 코사인 유사도(Cosine Similarity), 무난하고 취향 패턴 분석에 좋음
    # pearson : 피어슨 상관계수(애매한 값들), 편향 완화가 필요할 때 좋음
    # pearson_baseline : 피어슨 베이스라인, 조금 느리고 연산이 많아 데이터가 부족한데 정밀한 예측이 필요할 때 

    # user_based : 사용자 기반인지 아이템 기반인지
    #   - True : 내 취향과 평점 패턴이 비슷한 다른 사용자(이웃)이 이 아이템에 몇점을 주었는가?
    #   - False : 이 아이템을 좋아하는 사람들이 좋아하는 다른 유사한 아이템은 무엇인가?
    n_neighbors = 30
    model = KNNWithMeans(
        k=n_neighbors,
        sim_options={
            'name': 'cosine',
            'user_based': True
        },
        verbose=False # 학습 과정 출력 여부
    )

    # 사용 할 모델에게 학습
    model.fit(train_set)

    # 내가 평가 한 목록을 구한다
    # to_inner_uid : 사용자 id로 Surprise 내부 index를 변환한다
    inner_user_id = train_set.to_inner_uid(userId)

    # ur : user rating
    #   - user1이 영화1에는 3점, 영화2에는 3.5점을 줬다고 할 때 사용자 중심의 정보
    # ir : item rating
    #   - 영화1은 user1에게 3점 user2에게 1.5점을 받았다고 할 때 아이템 중심의 정보
    # Surprise용으로 바꿔놓은 train_set안에서 uid에 대한 movieId와 rating이 나옴
    rated_movies = set()
    for inner_movie_id, rating in train_set.ur[inner_user_id] :
        # to_raw_iid : inner_movie_id를 원본의(raw) iid(item id)로 바꿔라
        #   - 내부 영화 index를 원래 movieId로 바꿔주는 것
        rated_movies.add(train_set.to_raw_iid(inner_movie_id))

    # 학습 데이터 중 없는 목록을 구한다
    candidate_movies = [ 
        train_set.to_raw_iid(inner_movie_id)
        for inner_movie_id in range(train_set.n_items) 
        if train_set.to_raw_iid(inner_movie_id) not in rated_movies
    ]
    # n_items : length
    # for inner_movie_id in range(train_set.n_items) :
    #     if train_set.to_raw_iid(inner_movie_id) not in rated_movies :
    #         candidate_movies.append(train_set.to_raw_iid(inner_movie_id))

    # 그 목록의 예상 평점을 계산한다
    # 너라면 이 영화에 평점을 얼마 줄 것 같다는 예측
    recommend = []
    for movieId in candidate_movies :
        # 예상 평점 (학습한 모델을 쓰는 유일한 구간)
        # est : estimated 예측/추정의 약자, 예측한 평점
        # score = model.predict(userId, movieId).est : 예측의 추정치를 꺼냄
        score = model.predict(userId, movieId).est
        recommend.append({
            'movieId' : movieId,
            'score' : score
        })

    # 평점이 높은 순으로 정렬(내림차순 reverse=True)
    recommend.sort(key=lambda x:x['score'], reverse=True)

    return recommend[:top_k]

@router.get('/es/recommend/cf/')
def cf(userId:int, top_k:int = 10):
    return collaborative_filtering(userId, top_k)

# Recall@K
# 전체 추천 개수 중에 정답 개수, 순위(순서)는 보지 않는다
# 내 정답 개수 / 전체 정답 개수
def recall_at_k(
    userId:int, 
    test:pd.DataFrame,   # 정답 데이터
    recommend:list[dict], # 추천 목록
    threshold: float = 4.0, # 경계선에 대한 범위
    k:int=10
):
    # loc[]는 where조건처럼 사용할 수 있음
    # 내가 평점을 threshold 이상을 준 정답만 뽑자
    # 첫 번째 전달인자 : 조건
    # 두 번째 전달인자 : 특정 컬럼만 가져오기
    # relevant_movies  relevant(관련된)
    # 나와 관련된 영화 목록
    # pandas.Series 객체는 set으로 자동 형변환이 안된다
    # 그래서 set()으로 명시적 형변환
    relevant_movies = set(test.loc[ 
        # 첫 번째
        (test['userId'] == userId)
        & (test['rating'] >= threshold),

        # 두 번째
        'movieId'
    ])
    # 정답 데이터에 조건이 맞는 영화가 없어서 Recall 계산할 수 없다
    if len(relevant_movies) == 0 :
        return -1.0

    # 암시적, 묵시적 형변환
    recommend_moives = {
        item['movieId'] for item in recommend[:k]
    }

    # 추천 목록 중에서 내가 좋아하는 영화의 개수
    # 추천 중 정답 개수
    # & : 교집합
    hit_count = len(relevant_movies & recommend_moives)

    print('hit_count', hit_count)
    print('len(relevant_movies)', len(relevant_movies))

    # Recall@K = 맞힌 개수 / 전체 정답
    result = hit_count / len(relevant_movies)
    return result

@router.get('/recommend/recall')
def recall(userId:int):
    test,_ = split_train_test()
    recommend = collaborative_filtering(userId, 50)
    threshold = 2.0
    k = 50

    return recall_at_k(userId, test, recommend, threshold, k)