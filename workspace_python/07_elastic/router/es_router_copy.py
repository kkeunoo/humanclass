from fastapi import APIRouter

from config import ELASTIC_ENDPOINT, ELASTIC_API_KEY

from elasticsearch import Elasticsearch
from elasticsearch import helpers

from pathlib import Path # 경로 관련 lib

import json

# 엘라스틱 서치의 특징
# 모든 요청은 REST API를 사용한다 (즉, 주소 기반으로 CRUD가 동작 됨)

# 엘라스틱서치 vs RDBMS
#   index    :  table (RDBMS에서 index는 접근 루트이기 때문에 정의가 다름)
#   document :  줄, row, record, 튜플
#   field    :  column, field, 변수, 클래스
#   mapping  :  type (int, varchar 등)

router = APIRouter(tags=['엘라스틱서치 관련 라우터']) # tags 는 스웨거 용 글씨

es = Elasticsearch(
    ELASTIC_ENDPOINT, # 쉽게 말해 DB 연결 주소
    api_key=ELASTIC_API_KEY # 쉽게 말해 DB 인증 키(계정)
)

@router.get('/es/health')
def health():
    connected = es.ping() # ping은 True/False로 값이 나옴
    print('엘라스틱서치 연결 상태 : ', connected)
    return {
        'connected' : connected,
        'msg' : 'Elasticsearch 연결 ' + '성공' if connected else '실패'
    }

@router.post('/es/create')
def create_index():
    result = {
        'msg' : None
    }

    # indices.exists 로 이미 index가 있는지 검증
    if es.indices.exists(index='computer_copy'):
        print('computer index가 이미 존재합니다.')

        result['msg'] = 'computer : index가 이미 존재합니다.'
        return result

    # indices는 index의 복수형 중에 하나
    es.indices.create(
        index='computer_copy',
        mappings={
            "properties": {
                "id": {
                    "type": "integer"
                },
                "title": {
                    "type": "text"
                },
                "category": {
                    "type": "keyword"
                },
                "brand": {
                    "type": "keyword"
                },
                "os": {
                    "type": "keyword"
                },
                "status": {
                    "type": "keyword"
                },
                "tags": {
                    "type": "keyword"
                },
                "price": {
                    "type": "integer"
                },
                "rating": {
                    "type": "float"
                },
                "created_at": {
                    "type": "date"
                },
                "content": {
                    "type": "text"
                }
            }
        }
    )
    print('computer : index 생성 완료')

    result['msg'] = 'computer : index 생성 완료'
    return result

@router.post('/es/insert/bulk')
def ingest_documents():
    documents = load_documents()

    actions = []

    for doc in documents :
        actions.append({
            '_index' : 'computer_copy',
            '_id' : doc['id'], # '_id' : doc.get('id', None),
            '_source' : doc
        })

    success, errors = helpers.bulk(es, actions, stats_only=False) # stats_only=False 를 쓰면 성공/실패 값을 돌려줌, 아닐 시 성공만
    print('success : ', success)
    print('errors : ', len(errors), errors)

    return {
        'msg' : {
            'success' : success,
            'errors' : errors
        }
    }

def load_documents():

    print('__file__ : ', __file__) # __file__ :  D:\workspace\workspace_python\07_elastic\router\es_router.py
    # __file__ : 현재 실행한 파일의 전체 경로

    # Path(__file__).resolve().parents[2] : 부모 폴더 몇 개 올라가는지
    print( Path(__file__).resolve() ) # D:\workspace\workspace_python\07_elastic\router\es_router.py
    print( Path(__file__).resolve().parents[2] ) # D:\workspace\workspace_python
    print( Path(__file__).resolve().parents[1] ) # D:\workspace\workspace_python\07_elastic
    print( Path(__file__).resolve().parents[0] ) # D:\workspace\workspace_python\07_elastic\router

    BASE_DIR = Path(__file__).resolve().parents[1]
    DOCUMENT_FILE = BASE_DIR / 'data' / 'data.json' # 경로 합치기 Path의 경우 '/'로 +처럼 합침

    result = {}
    # with open('asdf', 'r') as file: # FileNotFoundError: [Errno 2] No such file or directory: 'asdf'
    try : # 혹시 파일이 없을경우 에러 발생 시 구동이 멈추지 않도록 try,except
        with open(DOCUMENT_FILE, 'r', encoding='UTF-8') as file: 
            # print(file) 

            # json을 dict로 변환해주는 lib
            result = json.load(file)
            # 참고로 dict를 json으로 변환 하려면 json.dump() 사용
            print(result)
    except Exception as e :
        print('open 하다 오류 발생 : ', e)

    return result

@router.get('/es/select/all')
def select_all():
    # 정렬 없이 전체 선택 (select * from computer)
    # response = es.search(
    #     index='computer',
    #     query={'match_all' : {}} # match는 엇비슷한 것, term은 정확한 것
    # )
    # # print(response)
    # # return response

    # 정렬하여 선택 (select * from computer order by category asc, price desc)
    # response = es.search(
    #     index='computer',
    #     query={'match_all' : {}},
    #     sort=[{
    #             'category' : {
    #                 'order': 'asc'
    #             },
    #             'price': {'order': 'desc'}
    #     }]
    # )

    # OFFSET, LIMIT
    # '''
    #     select * from computer
    #     -- limit 5, 10 # 5개 건너뛰고 부터 10개

    #     offset 5 # 5개 건너뛰고
    #     limit 10 # 10개
    # '''
    # response = es.search(
    #     index='computer',
    #     query={'match_all' : {}},
    #     sort=[{'id' : {'order': 'asc'}}],
    #     from_=3, # 3개 건너뛰고
    #     size=4 # 4개 제한 출력
    # )

    # GROUP BY , aggregation : 집합
    # select category from computer 
    # group by category
    response = es.search(
        index='computer_copy',
        query={'match_all' : {}},
        aggs={
            'categories' : { # 가지고 있는 column이 아닌 정해진 key값
                'terms' : {'field' : 'category'} # category가 column명(field)
            }
        }
    )
    '''
    "aggregations": {
        "categories": {
          "doc_count_error_upper_bound": 0,
          "sum_other_doc_count": 0,
          "buckets": [
            {
              "key": "노트북",
              "doc_count": 3
            },
            {
              "key": "네트워크",
              "doc_count": 2
            },
            {
              "key": "모니터",
              "doc_count": 1
            },
            {
              "key": "저장장치",
              "doc_count": 1
            },
            {
              "key": "주변기기",
              "doc_count": 1
            }
          ]
        }
      }
    },
    '''
    print(response)

    results = []
    for hit in response['hits']['hits'] :
        document = hit.get('_source', {})
        results.append(document)

    return {
        'msg' : {
            'results' : results,
            'total' : response['hits']['total']['value']
        }
    }

def formatter(resp):
    results = []
    for hit in resp['hits']['hits'] :
        # document = hit.get('_source', {})
        results.append({
            'document' : hit.get('_source', {}),
            'score' : hit.get('_score')
        })

    return {
        'results' : results,
        'total' : resp['hits']['total']['value']
    }

# match는 where와 비슷하며 백터 검색(자연어 검색)
# 검색어를 분석한 뒤에 토큰 단위로 검색
# '노트북에' 로 검색하면 '노트북을' 도 나온다
@router.get('/es/select/match')
def match(keyword:str):
    response = es.search(
        index='computer_copy',
        query={'match' : {
            'content' : keyword # 'Field명' : 'keyword'
        }} 
    )

    return {"msg" : formatter(response)}

# title, content안에 keyword가 들어가 있으면 검색
@router.get('/es/select/multi_match')
def multi_match(keyword:str):
    response = es.search(
        index='computer_copy',
        query={'multi_match' : { 
            'query': keyword,
            'fields': ['title', 'content'] # 제목, 내용, 제목+내용 으로 검색하는 형식
        }} 
    )

    return {"msg" : formatter(response)}

# select의 like처럼 정확히 일치하는 값을 검ㅅ개
@router.get('/es/select/term')
def term(keyword:str):
    response = es.search(
        index='computer_copy',
        query={'term' : {
            # 'category' : keyword 
            'content' : keyword 
        }} 
    )

    return {"msg" : formatter(response)}

@router.get('/es/select/range')
def range_(max:int, min:int = 0):
    response = es.search(
        index='computer_copy',
        query={'range' : {
            'price' : {
                'gte' : min,
                'lte' : max
            } 
        }} 
    )

    return {"msg" : formatter(response)}

# bool 복합 쿼리
# filter : 쿼리가 참인 것 검색 (score 계산을 하지 않아 빠르다), 여러 개 쓰면 AND 조건이 됨
# must : 쿼리가 참인 것 검색 (점수가 좋은 것들 중에서)
# must_not : 쿼리가 거짓인 것 검색
# should : 쿼리가 참인 것의 점수를 높인다 (must랑 같이 사용), 여러 개 쓰면 OR 조건이 됨
@router.get('/es/select/filter')
def filter_(category, keyword):
    response = es.search(
        index='computer_copy',
        query={'bool' : {
            'filter': [{
                'term' : {'category': category}
            }],
            'must' : [{
                'match': {'content': keyword}
            }]
        }} 
    )

    return {"msg" : formatter(response)}

@router.get('/es/select/orderby')
def orderby(sort_field, order = 'asc'):

    # 아래처럼 했을 때 참/거짓을 잘 구분해서 or나 and를 써야 함
    # if not(order == 'asc' or order == 'desc'):
    if order != 'asc' and order != 'desc':
        return {"msg" : 'order는 asc 또는 desc여야 합니다.'}
    
    response = es.search(
        index='computer_copy',
        query={'match_all' : {}}, 
        sort=[{
            sort_field : {'order': order},
        }],
        size=20
    )

    return {"msg" : formatter(response)}

