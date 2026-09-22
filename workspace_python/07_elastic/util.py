from pathlib import Path 
from elasticsearch import Elasticsearch
from config import ELASTIC_ENDPOINT, ELASTIC_API_KEY
import json

es = Elasticsearch(
    ELASTIC_ENDPOINT, # 쉽게 말해 DB 연결 주소
    api_key=ELASTIC_API_KEY # 쉽게 말해 DB 인증 키(계정)
)

# JSON 파일 읽어오기
def load_documents():
    print('__file__ : ', __file__) 

    BASE_DIR = Path(__file__).resolve().parents[0]
    DOCUMENT_FILE = BASE_DIR / 'data' / 'data.json' # 경로 합치기 Path의 경우 '/'로 +처럼 합침

    result = {}
    # with open('asdf', 'r') as file: # FileNotFoundError: [Errno 2] No such file or directory: 'asdf'
    try : # 혹시 파일이 없을경우 에러 발생 시 구동이 멈추지 않도록 try,except
        with open(DOCUMENT_FILE, 'r', encoding='UTF-8') as file: 
            # print(file) 

            # json을 dict로 변환해주는 lib
            result = json.load(file)
            # 참고로 dict를 json으로 변환 하려면 json.dump() 사용
            # print(result)
    except Exception as e :
        print('open 하다 오류 발생 : ', e)

    return result

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