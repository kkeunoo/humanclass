from pathlib import Path
import pandas as pd
import traceback

from dotenv import load_dotenv
load_dotenv()
import os

from google import genai
from google.genai import types
from openai import OpenAI

import time

from elasticsearch import Elasticsearch
es = Elasticsearch(os.getenv('ELASTIC_ENDPOINT'))

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

def embedding_with_gemini(chunks):
    # 임베딩 모델 가져오기
    api_key = os.getenv('GEMINI_API_KEY')
    client = genai.Client(api_key=api_key)

    actions = []
    for chunk in chunks :
        # 임베딩 하기
        result = client.models.embed_content(
            model='gemini-embedding-2',
            contents=[
                types.Content(
                    parts=[
                        types.Part.from_text(text=chunk['content'])
                    ]
                )
            ],
            # 384, 768은 64의 배수로 딱 떨어지는 수
            config=types.EmbedContentConfig(
                # 디멘션이 달라진다고 해도 실질적인 토큰에는 영향을 주지 않는다
                # 단, 벡터가 많아지기에 저장공간이 커지고 검색이 느려진다
                output_dimensionality=768
            )
        )
        # 임베딩 한 결과 저장
        chunk['embedding'] = result.embeddings[0].values

        # ES용 데이터 형식으로 저장
        actions.append({
            '_index': os.getenv('ES_INDEX'),
            '_id': f'{chunk["movieId"]}-{chunk["chunk_index"]}',
            '_source': chunk
        })
        # gemini가 1분당 제한이 있기 때문에 0.7초로 sleep을 걸어줌
        time.sleep(0.7)

    return actions

def embedding_with_openai(chunks):
    # 임베딩 모델 가져오기
    api_key = os.getenv('OPENAI_API_KEY')
    client = OpenAI(api_key=api_key)

    actions = []
    last_index = 0
    time_before = time.time()

    contents = [ chunk['content'] for chunk in chunks ]

    for idx_start in range(0, len(contents), 2047) :
        contents_part = contents[idx_start: idx_start + 2047]

        # 임베딩 하기
        # OpenAI의 경우 list를 주면 결과도 list로 나온다
        result = client.embeddings.create(
            model='text-embedding-3-small',
            input=contents_part,
            encoding_format='float', # 기본값: base64 형태(양방향 암호화)
            # dimensions=1
            dimensions=768
        )

        # print(result)

        # 혹시 몰라서 내용 중 'index' 기준으로 정렬
        '''
        CreateEmbeddingResponse(
            data=[
                Embedding(embedding=[1.0], index=0, object='embedding'), 
                Embedding(embedding=[1.0], index=1, object='embedding')
            ], 
            model='text-embedding-3-small', 
            object='list', 
            usage=Usage(
                prompt_tokens=17, 
                total_tokens=17)
            )
        '''
        vectors = [ sort_data.embedding for sort_data in sorted(result.data, key=lambda item : item.index) ]

        for idx, vector in enumerate(vectors) :
            chunks[last_index]['embedding'] = vector
            # chunk['embedding'] = vectors[idx]

            # ES용 데이터 형식으로 저장
            actions.append({
                '_index': os.getenv('ES_INDEX'),
                '_id': f'{chunks[last_index]["movieId"]}-{chunks[last_index]["chunk_index"]}',
                '_source': chunks[last_index]
            })

            last_index += 1

        time_after = time.time()
        print('걸린 시간 (2047개) : ', time_after - time_before)
        time_before = time.time()

    return actions

def formatter(resp):
    results = []
    for hit in resp['hits']['hits'] :
        document = hit.get('_source', {})
        
        results.append({
            'document' : hit.get('_source', {}),
            'score' : hit.get('_score')
        })

    return {
        'results' : results,
        'total' : resp['hits']['total']['value']
    }