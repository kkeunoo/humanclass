from fastapi import APIRouter
from elasticsearch import helpers

# 정규표현식 (regular expression, regExp) 사용을 위한 모듈
import re 
from util import es, load_documents, formatter

router = APIRouter(tags=['임베딩 관련 라우터']) 

@router.get('/embed/split')
def split(text):
    return split_text(text)

def split_text(text):
    # print('text : ', text)
    sentences = re.split(
        r"(?<=[.!?])\s+",   # . ! ? 다음에 공백(\s+)이 있으면 분리하는 정규표현식
        text.strip()        # 문자의 앞/뒤 공백 제거한 것을 대상으로
    )
    # print('sentences : ', sentences)
    # return sentences

    # 혹시 몰라서 각 리스트 요소의 양쪽 공백 제거
    sentences2 = []
    for s in sentences :
        if s.strip(): # 공백 제거 후에도 글이 있으면
            sentences2.append(s.strip()) # 그 글로 리스트에 추가

    sentences = sentences2

    chunks = []
    chunk_size = 30
    '''
        고양이는 귀엽다. 고양이는 털이 많다. 이미지도 너무 깔끔해요.
        [
            '고양이는 털이 많다.', 
            '고양이는 귀엽다.',
            '이미지도 깔끔해요.'
        ]
    '''
    # 청크보다 작은 문장은 합칠 수 있으면 합치자
    # 큰 건 어쩔 수 없고

    # 임시 저장소
    temp = ''
    for sentence in sentences :
        # print('길이, 글씨 : ', len(sentence), sentence)
        '''
            길이, 글씨 :  9 고양이는 귀엽다.
            길이, 글씨 :  11 고양이는 털이 많다.
            길이, 글씨 :  13 이미지도 너무 깔끔해요.
        '''
        # chunk_size 보다 짧은데 최대한 채워서 chunk에 넣겠다
        candidate = '' # 결국 일단 다음 문장을 붙여본다

        # 이전 문장이 있으면 
        if len(temp) > 0:
            # 뒤에 지금 문장을 이어붙인다
            candidate = f'{temp} {sentence}'
        else :
            candidate = sentence

        # 붙인게 아직 모자라면 더 붙여보기
        if len(candidate) <= chunk_size :
            temp = candidate
        else :
            # 붙인게 넘치면 붙이기 전의 안 붙은걸 청크로 확정한다
            if len(temp) > 0 :
                chunks.append(temp)

            temp = sentence

    if len(temp) > 0 :
        chunks.append(temp)

    # print('chunks : ', chunks)
    # chunks :  ['고양이는 귀엽다. 고양이는 털이 많다.', '이미지도 너무 깔끔해요.']

        #연습용##########################################
        # candidate = ''
        # result = ''
        # if len(sentence) > chunk_size :
        #     candidate = sentence
        # else :
        #     temp = sentence

        # if temp:
        #     candidate = f'{temp} {sentence}'
        #     if len(candidate) > chunk_size :
        #         result = candidate
        #     else :
        #         result = f'{candidate} {sentence}'
        # else :
        #     result = candidate
        # print(result)
        ################################################

    overlap_size = 6
    overlap_chunks = []
    for index, chunk in enumerate(chunks) :
        if index == 0:
            overlap_chunks.append(chunk)
            continue

        before = chunks[index - 1]
        prefix = before[-overlap_size:] # 뒤에서 overlap_size만큼 부터 끝까지
        now = f'{prefix} {chunk}'.strip() 
        overlap_chunks.append(now)

    # print('overlap_chunks : ', overlap_chunks)
    return overlap_chunks

@router.post('/embed/create')
def create_embed_index():
    if es.indices.exists(index='computer_chunk'):
        # es.indices.delete(index='computer_chunk') # 테이블(index) 삭제
        
        # 테이블(index) 안에 내용 지우기
        # es.delete_by_query(
        #     index='computer_chunk',
        #     query={
        #         'match_all' : {} # 모든 문서 대상
        #     },
        #     refresh=True # 삭제 결과를 즉시 검색에 반영
        # )
        return 'computer_chunk가 이미 있습니다.'

    es.indices.create(
        index='computer_chunk',
        mappings={
            'properties' : {
                'id':{'type':'integer'},
                'title':{'type':'text'}, 
                'category':{'type':'keyword'}, 
                'price':{'type':'integer'},
                'rating':{'type':'float'},
                'created_at':{'type':'date'},
                'content':{'type':'text'},
                'chunk_index':{'type':'integer'},
                'embedding':{
                    'type':'dense_vector',
                    # 'dims':768  # 64의 배수라서 CPU연산 단위와 호환이 잘 됨 
                    #             # 512도 주로 사용, 256은 뉘앙스에 조금 약하다
                    'dims' : 384
                }
            }
        }
    )    

    return 'computer_chunk index 생성 완료'

@router.post('/embed/insert/bulk')
def ingest_embed_documents():
    # json 가져오기
    documents = load_documents()

    actions = []

    for doc in documents :
        # chunk 만들기
        chunks = split_text(doc['content'])

        for index, chunk in enumerate(chunks) :
            # 백터로 변환
            embedding = get_embedding(doc['title'], chunk)

            # 살짝 변형
            doc2 = doc
            doc2['chunk_index'] = index
            doc2['embedding'] = embedding

            # actions에 추가
            actions.append({
                '_index' : 'computer_chunk',
                '_id' : f'{doc2["id"]}-{index}',
                '_source' : doc2
            })
            
    success, errors = helpers.bulk(
        es,
        actions,
        stats_only=False # 기본값 True, 
                         # True: 성공/실패 숫자만
                         # False: 성공/실패 숫자 + 에러 메시지
    )

    return {'msg' : {'success' : success, 'errors' : errors}}

def get_embedding(title, content):
    text = f'title:{title}\ncontent:{content}'

    # 엘라스틱서치의 임베딩 모델 (임베딩을 저장용으로 요청한다)
    result = es.inference.text_embedding(
        inference_id=".multilingual-e5-small-elasticsearch",
        input=text,
        input_type="ingest" # ingest : 저장할 때 사용 # search : 검색할 때 사용
    )
    # print('-'*30)
    # print('text : ', text)
    # print('result : ', result)

    # 생성한 백터를 반환한다
    return result['text_embedding'][0]['embedding']

def get_keyword_embedding(keyword):
    # 엘라스틱서치의 임베딩 모델 (임베딩을 검색용으로 요청한다)
    result = es.inference.text_embedding(
        # 저장과 검색의 모델이 동일해야 함
        inference_id=".multilingual-e5-small-elasticsearch", 
        input=keyword,
        input_type="search" # ingest : 저장할 때 사용 # search : 검색할 때 사용
    )

    # 생성한 백터를 반환한다
    return result['text_embedding'][0]['embedding']

# @router.get('/embed/chunk/select')
# def select_all():
#     response = es.search(
#         index='computer_chunk',
#         query={'match_all' : {}}
#     )

#     return response

@router.get('/embed/search/vector')
def search_vector(keyword):
    # 검색어를 검색용 백터로 변환한다
    vector_keyword = get_keyword_embedding(keyword)

    # Elasticsearch에서 KNN(K-Nearest Neighbors) 백터 검색을 한다
    '''
        KNN(K-Nearest Neighbors) 특징
        1. 새로운 데이터와 가장 가까운 'K'개를 비교해서 가장 많이 속해있는(교집합이 많은) 값을 예측
        2. 원리가 단순해서 쉽게 이해할 수 있다
        3. 따로 저장해 두지 않고 매 번 수행한다(미리 학습X)
        4. 매 번 수행하기 때문에 대용량 일 때는 느리다
        5. 민감해서 전처리가 중요하다(공백제거, NULL제거 등)
        6. 성능이 달라지기 때문에 'K'값 선정이 중요하다(범위가 과하게 넓으면 거짓 된 정보가 올 수 있으니 유의)
    '''
    size = 5
    response = es.search(
        index='computer_chunk',
        knn={
            # 백터 필드명
            'field': 'embedding',
            # 사용자가 입력한 검색어의 백터를 해당 필드의 백터와 유사도 비교
            'query_vector':vector_keyword,
            # 실제 검색 후보로 검토할 청크의 수(아래처럼 할 경우 50개를 가져옴)
            # 'K'보다 많은 후보를 먼저 찾고 그 중에서 가장 유사한 'K(size)'개를 선택
            # 아래처럼 max(a,b)를 사용하는 것은 둘 중에 큰 수가 나오기에 최소 50개를 보장한다
            'num_candidates':max(size*10, 50), 
            # KNN에서 사용 할 'K'값 지정(가장 유사한 size개의 청크를 찾는다)
            # '노트북'으로 검색한다면 가까운 것 뿐만 아니라 후보지를 모두 다 가져옴
            'k':size
        },
        size=size
    )

    return formatter(response)

@router.get('/embed/search/hybrid')
def hybrid(keyword):
    # match, 유사도(vector) 검색을 함께 하는 하이브리드 검색

    # match 검색(BM25) : 검색어의 형태소(을,를,의 등)가 포함 된 단어
    # 유사도(백터) 검색(KNN) : 검색어와 유사한 단어 검색
    #   - 이미 학습되어 있는 머신러닝 모델을 활용한다

    # 두 결과를 RRF 방식으로 합쳐서 최종적으로 관련성 높은 문서만 반환한다
    
    # 검색어를 검색용 백터로 변환한다
    vector_keyword = get_keyword_embedding(keyword)

    size=5
    response = es.search(
        index='computer_chunk',
        size=size,
        # 리트리버(Retriever) : 두 가지 검색 결과를 결합하기 위해 사용
        retriever={
            # RRF(Reciprocal Rank Fusion) : 상호간의 랭킹을 통한 융합
            # 검색은 1등, 백터는 10등 한 것과 검색 5등, 백터 2등이 있을 경우
            # 둘 다 높은 순위가 최종 순위에서도 높은 순위를 받을 가능성이 높다
            'rrf': {
                # 계산에 사용되는 상수값 (정해진 값. 보통 60을 사용함)
                # 높은 순위와 낮은 순위의 영향력 조절 
                'rank_constant': 60,
                # retrievers에서 검색 한 순위 결합에 사용할 결과의 범위
                'rank_window_size': max(size*10, 50),
                'retrievers': [
                    # keyword match 검색
                    {
                        'standard':{
                            'query':{
                                # match : 한 필드에서 형태소 검색
                                # multi_match : 여러 필드에서 형태소 검색
                                # term : 한 필드에서 정확히 일치하는 검색
                                'multi_match':{
                                    'query': keyword,
                                    # title, content의 keyword의 형태소 검색
                                    'fields': ['title', 'content']
                                }
                            }
                        }
                    },
                    # keyword KNN 검색
                    {
                        'knn':{
                            'field': 'embedding',
                            'query_vector':vector_keyword,
                            'num_candidates':max(size*20, 100), 
                            'k':size*10
                        }
                    }
                ]
            }
        }
    )

    return formatter(response)





