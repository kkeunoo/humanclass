# pip install elasticsearch fastapi uvicorn python-dotenv google-genai

# dotenv 사용법
# python-dotenv 는 env파일 등 가져오는것을 도와주는 lib
from dotenv import load_dotenv
load_dotenv() # 사용하게 되면 window 시스템 환경 변수로 .env가 들어감

import os
key1 = os.getenv('key1')
key2 = os.getenv('key2')
key3 = os.getenv('key3')

print('key1 : ',key1)
print('key2 : ',key2)
print('key3 : ',key3)

# if not key3 :
#     raise ValueError('key3 환경변수가 없습니다. .env 파일을 확인하세요.')

# import config
# config.ELASTIC_ENDPOINT
from config import ELASTIC_ENDPOINT, ELASTIC_API_KEY
from elasticsearch import Elasticsearch

# 엘라스틱서치용 파일은 이것과 index생성부터 같이 놓으면 좋음
es = Elasticsearch(
    ELASTIC_ENDPOINT, # 쉽게 말해 DB 연결 주소
    api_key=ELASTIC_API_KEY # 쉽게 말해 DB 인증 키(계정)
)

connected = es.ping() # ping은 True/False로 값이 나옴
print('엘라스틱서치 연결 상태 : ', connected)

# 파일 읽기
from pathlib import Path # 경로 관련 lib
print('__file__ : ', __file__) # __file__ :  D:\workspace\workspace_python\07_elastic\run.py
# __file__ : 현재 실행한 파일의 전체 경로

# Path(__file__).resolve().parents[2] : 부모 폴더 몇 개 올라가는지
print( Path(__file__).resolve() ) # D:\workspace\workspace_python\07_elastic\run.py
print( Path(__file__).resolve().parents[2] ) # D:\workspace
print( Path(__file__).resolve().parents[1] ) # D:\workspace\workspace_python
print( Path(__file__).resolve().parents[0] ) # D:\workspace\workspace_python\07_elastic

BASE_DIR = Path(__file__).resolve().parents[0]
DOCUMENT_FILE = BASE_DIR / 'data' / 'data.json' # 경로 합치기 Path의 경우 '/'로 +처럼 합침

import json
def load_documents():
    result = {}
    # with open('asdf', 'r') as file: # FileNotFoundError: [Errno 2] No such file or directory: 'asdf'
    try : # 혹시 파일이 없을경우 에러 발생 시 구동이 멈추지 않도록 try,except
        with open(DOCUMENT_FILE, 'r', encoding='UTF-8') as file: 
            # print(file) <_io.TextIOWrapper name='D:\\workspace\\workspace_python\\07_elastic\\data\\data.json' mode='r' encoding='cp949'>
            
            # json을 dict로 변환해주는 lib
            result = json.load(file)
            # 참고로 dict를 json으로 변환 하려면 json.dump() 사용
            print(result)
    except Exception as e :
        print('open 하다 오류 발생 : ', e)

    return result

# 엘라스틱 서치의 특징
# 모든 요청은 REST API를 사용한다 (즉, 주소 기반으로 CRUD가 동작 됨)

# 엘라스틱서치 vs RDBMS
#   index    :  table (RDBMS에서 index는 접근 루트이기 때문에 정의가 다름)
#   document :  줄, row, record, 튜플
#   field    :  column, field, 변수, 클래스
#   mapping  :  type (int, varchar 등)

########################
# index 생성(table 생성)
########################
def create_index():

    if es.indices.exists(index='computer'):
        print('computer index가 이미 존재합니다.')
        return 

    # indices는 index의 복수형 중에 하나
    es.indices.create(
        index='computer',
        mappings={
            'properties' : {
                'id':{'type':'integer'},
                'title':{'type':'text'}, # text type은 벡터로 분석해서 유연한 검색이 가능한 글씨
                'category':{'type':'keyword'}, # keyword type은 태그처럼 인식되는 것, 완전 똑같은 단어로만 검색이 가능한 글씨
                'price':{'type':'integer'},
                'rating':{'type':'float'},
                'created_at':{'type':'date'},
                'content':{'type':'text'},
            }
        }
    )
    print('index 생성 완료')

# create_index()

# insert를 할 때 엘라스틱서치는 수집한다는 뜻의 ingest를 사용
from elasticsearch import helpers
def ingest_documents():
    documents = load_documents()

    actions = []

    for doc in documents :
        actions.append({
            '_index' : 'computer',
            '_id' : doc['id'], # '_id' : doc.get('id', None),
            '_source' : doc
        })

    success, errors = helpers.bulk(es, actions, stats_only=False) # stats_only=False 를 쓰면 성공/실패 값을 돌려줌, 아닐 시 성공만
    print('success : ', success)
    print('errors : ', len(errors), errors)

ingest_documents()
    




