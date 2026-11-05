from fastapi import APIRouter, Query
import os
from dotenv import load_dotenv
from pydantic import BaseModel

from typing import Literal, Optional

from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI

from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import PydanticOutputParser, StrOutputParser

from langgraph.graph import StateGraph, START, END

# from router import es_router
from router.es_router import (
    content_based_filtering, 
    collaborative_filtering, 
    search_movies,
    term_movieId
)

router = APIRouter(tags=["langgraph"])
load_dotenv()

'''
    1. list_movieId, userId와 실제 질문을 입력한다.
    2. 추천 방식을 분석하고 선정한다.
    3. 선정 된 방식으로 추천한다.
    4. 추천 받은 결과를 LLM에 전달해서 포장 후 출력한다.
'''

# 상태 클래스 : langgraph에서 공유 할 객체
class State(BaseModel):
    list_movieId: Optional[list[int]] = None        # CBF에서 사용 할 영화 ID 목록
    userId: Optional[int] = None                    # CF에서 사용 할 유저 ID
    top_k: int = 10                                 # 가져올 결과 값 개수
    question: str                                   # 사용자 질문

    recommend_type: Optional[str] = None            # 사용할 추천 방식, 3개 말고는 못 들어옴
    recommend_type_reason: Optional[str] = None     # 추천 타입 선정의 이유

    recommends: Optional[list[dict]] = []           # 추천 목록들

    explain: Optional[str] = 'LLM 응답 없음'         # 최종 답변

    error: Optional[str] = None                     # 에러 메세지

class RecommendType(BaseModel):
    recommend_type: Literal['CBF', 'CF', 'BM25']    # 사용할 추천 방식, 3개 말고는 못 들어옴
    recommend_type_reason: str                      # 추천 타입 선정의 이유

# 질문을 기반으로 추천 방식을 분석하고 선택한다
def recommend_select(state: State):
    # question = state.question

    # 프롬프트 준비
    prompt = ChatPromptTemplate.from_messages([
        ('system', '''
            당신은 영화 추천 시스템의 추천 방식을 선택하는 역할이다.
            사용자 질문의 의도를 분석하고 파악해서 세 가지 중 하나만 선택하시오.

            1. [CBF]
                - 특정 영화와 비슷한 영화를 찾는 경우
                - 장르와 사용자들의 태그 기반으로 추천하는 경우
            2. [CF]
                - 사용자의 취향과 비슷한 다른 사용자들의 평점 패턴 분석 기반으로 추천하는 경우
            3. [BM25]
                - 제목, 장르, 태그 등의 키워드로 검색하는 경우
        '''),
        ('human', '*** 사용자 질문 : {question}')
    ])

    # 모델 준비
    model = ChatOpenAI(
        model='gpt-5.5',
        temperature=0,
        api_key=os.getenv("OPENAI_API_KEY")
    )

    # chain 후 invoke
    # with_structured_output는 해당 Pydantic을 가져간 뒤 맞는 양식으로 넣게끔 할 수 있음
    chain = prompt | model.with_structured_output(RecommendType) 

    # chain 실행 결과를 State의 필드에 맞게 저장하도록 리턴
    result = chain.invoke({
        'question' : state.question
    })
    print(' recommend_select >>> result : ', result)

    return {
        'recommend_type' : result.recommend_type,
        'recommend_type_reason' : result.recommend_type_reason
    }

def nomarlize(response, top_k = 10):
    movieIds = set()
    recommends = []

    for hit in response['hits']['hits'] :
        source = hit['_source']

        movieId = source.get('movieId')
        if movieId not in movieIds :
            movieIds.add(movieId)

            recommends.append({
                'movieId' : movieId,
                'title' : source.get('title', ''),
                'genres' : source.get('genres', []),
                'tags' : source.get('tags', []),
                'score' : hit.get('_score', -1)
            })
        # top_k개가 지나면 break로 끝낼수도 있다

    return recommends[:top_k]

def cbf(state: State):
    # def content_based_filtering(list_movieId: list, top_k:int = 10):
    response = content_based_filtering(state.list_movieId)

    recommends = nomarlize(response, state.top_k)

    # return 은 json형식으로 해줘야 basemodel에 들어감
    return {
        'recommends' : recommends
    }

def cf(state:State):
    '''
    [{
        'movieId' : movieId,
        'score' : score
    }]   
    '''
    result = collaborative_filtering(state.userId)
    movieIds = set()

    for info in result :
        movieIds.add( info.get('movieId', 0) )

    response = term_movieId(movieIds)

    recommends = nomarlize(response, state.top_k)
    return {
        'recommends' : recommends
    }

def bm25(state: State):
    response = search_movies(state.question)

    recommends = nomarlize(response, state.top_k)
    return {
        'recommends' : recommends
    }

def explain(state: State) :
    # 프롬프트 준비
    prompt = ChatPromptTemplate.from_messages([
        ('system', '''
            당신은 영화 추천 시스템의 추천 결과를 설명하는 역할이다. 
            설명을 섹시하게 해서 꼭 볼 수 밖에 없는 설득력을 가지고 있다.
            간략하게 중요 내용만 설명한다.

            [주의사항]
                - 결과에 없는 영화를 추천하지 않는다.
                - 제목을 한국것으로 검색해서 원제와 함께 알려준다.
        '''),
        ('human', '''
            [사용자 질문] : {question}
            [검색 방식] : {recommend_type}
            [검색 결과] : 
            {recommends}
            [할 일] : 위 정보로 사용자에게 잘 설명하시오.
        ''')
    ])

    # 모델 준비
    model = ChatOpenAI(
        model='gpt-5.5',
        temperature=0,
        api_key=os.getenv("OPENAI_API_KEY")
    )

    # chain 후 invoke
    # with_structured_output는 해당 Pydantic을 가져간 뒤 맞는 양식으로 넣게끔 할 수 있음
    chain = prompt | model | StrOutputParser()

    # chain 실행 결과를 State의 필드에 맞게 저장하도록 리턴
    result = chain.invoke({
        'question' : state.question,
        'recommend_type' : state.recommend_type,
        'recommends' : state.recommends,
    })
    print(' recommend_select >>> result : ', result)

    return {
        'explain' : result
    }

def validator(state: State):
    type = state.recommend_type
    if type == 'CBF':
        if state.list_movieId is None :
            return 'ERROR'
        # else :
        #     return type

    elif type == 'CF':
        if state.userId is None :
            return 'ERROR'
        # else :
        #     return type

    return type

def makeErrorMessage(state: State):

    error = None

    type = state.recommend_type
    if type == 'CBF':
        error = 'list_movieId는 필수입니다.'
    elif type == 'CF':
        error = 'userId는 필수입니다.'

    return {
        'error' : error
    }

# Body의 Data를 받아야 해서 post
@router.post('/langgraph/recommend')
def recommend(param: State):
    print(param)
    # question = param.question

    # langgraph 생성
    graph = StateGraph(State)

    # langgraph용 node 등록
    graph.add_node('select', recommend_select)
    graph.add_node('CBF', cbf)
    graph.add_node('CF', cf)
    graph.add_node('BM25', bm25)
    graph.add_node('explain', explain)

    graph.add_node('validator', validator)
    graph.add_node('makeErrorMessage', makeErrorMessage)

    # node간의 edge설정
    graph.add_edge(START, 'select')

    graph.add_conditional_edges(
        'select',
        # lambda s: s.recommend_type,
        'validator',
        {
            'CBF': 'CBF',
            'CF': 'CF',
            'BM25': 'BM25',
            'ERROR': 'makeErrorMessage'
        }
    )

    graph.add_edge('CBF', 'explain')
    graph.add_edge('CF', 'explain')
    graph.add_edge('BM25', 'explain')

    graph.add_edge('explain', END)
    graph.add_edge('makeErrorMessage', END)

    # 실행 가능한 langgraph객체로 만들기
    recommend_graph = graph.compile()
    result = recommend_graph.invoke({
        'list_movieId' : param.list_movieId,
        'userId' : param.userId,
        'top_k' : param.top_k,
        'question' : param.question,
        'recommedns': []
    })

    return result
