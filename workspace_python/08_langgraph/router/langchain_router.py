from fastapi import APIRouter, Query
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

from typing import Literal

from openai import OpenAI

from google import genai
from google.genai import types

from langchain_google_genai import ChatGoogleGenerativeAI

from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

from pydantic import BaseModel

from langchain_core.output_parsers import PydanticOutputParser, StrOutputParser

router = APIRouter(tags=["langchain"])
load_dotenv()

# 그냥 gpt에 말하기 - 단발성
@router.get("/langchain/gpt")
def gpt(prompt: str):
    model = ChatOpenAI(
        model='gpt-5.5',
        temperature=0,
        api_key=os.getenv("OPENAI_API_KEY")
    )
    output = model.invoke(prompt)
    return output

# langchain 모듈 사용
# 멀티턴으로 gpt에 말하기
@router.get("/langchain/gpt/multi")
def gpt2(prompt: str):
    model = ChatOpenAI(
        model='gpt-5.5',
        temperature=0,
        api_key=os.getenv("OPENAI_API_KEY")
    )

    messages = [
        {"role": "system", "content": "너는 친절한 조수야"},
        {"role": "user", "content": "내 이름은 근욱야."},
        {"role": "assistant", "content": "안녕하세요. 근욱님! 친절히 알려드릴께요"},
        {"role": "user", "content": prompt}
    ]

    output = model.invoke(messages)

    # 실제 대답은 output.content에 들어있다
    return output

# openai 모듈 사용
@router.get("/original/gpt")
def gpt3(prompt: str):
    # 쌩으로 openai 모듈 사용법
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    messages = [
        {"role": "system", "content": "너는 친절한 조수야"},
        {"role": "user", "content": "내 이름은 근욱이야."},
        {"role": "assistant", "content": "안녕하세요. 근욱님! 친절히 알려드릴께요"},
        {"role": "user", "content": prompt}
    ]

    output = client.chat.completions.create(
        model='gpt-5.5',
        messages=messages
    )
    # 실제 대답은 output.choices[0].message.content에 들어있다
    return output

# genai 모듈 사용
@router.get("/original/gemini")
def gemini1(prompt: str):
    # 쌩으로 genai 모듈 사용법
    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

    # genai를 사용할 때
    # role에 system 없음
    # parts로 적어야함
    messages = [
        {"role": "user", "parts": [{'text': "내 이름은 근욱이야."}]},
        {"role": "model", "parts": [{'text': "안녕하세요. 근욱님! 친절히 알려드릴께요"}]},
        {"role": "user", "parts": [{'text': prompt}]}
    ]

    output = client.models.generate_content(
        model='gemini-3.8-flash',
        contents=messages,
        config=types.GenerateContentConfig(
            system_instruction="너는 친절한 조수야",
            temperature=0.0
        )
    )

    # 실제 대답은 candidates[0].content.parts[0].text에 들어있다
    return output

# langchain 모듈 사용
@router.get("/langchain/gemini")
def gemini2(prompt: str):
    model = ChatGoogleGenerativeAI(
        model='gemini-3.8-flash',
        temperature=0,
        api_key=os.getenv("GEMINI_API_KEY")
    )

    messages = [
        {"role": "system", "content": "너는 친절한 조수야"},
        {"role": "user", "content": "내 이름은 근욱이야."},
        {"role": "assistant", "content": "안녕하세요. 근욱님! 친절히 알려드릴께요"},
        {"role": "user", "content": prompt}
    ]

    output = model.invoke(messages)

    # 실제 대답은 output.content[0].text에 들어있다
    return output


# langchain의 message 모듈 사용해서 질문하기
@router.get("/langchain/gpt/message")
def gpt4(prompt: str):
    model = ChatOpenAI(
        model='gpt-5.5',
        temperature=0,
        api_key=os.getenv("OPENAI_API_KEY")
    )

    # provider에 따라 형식을 맞춰준다
    messages = [
        SystemMessage("너는 친절한 조수야"),
        HumanMessage("내 이름은 근욱이야."),
        AIMessage("안녕하세요. 근욱님! 친절히 알려드릴께요"),
        HumanMessage(prompt)
    ]

    output = model.invoke(messages)

    # 실제 대답은 output.content에 들어있다
    return output

# stream으로 출력하기
@router.get("/langchain/gpt/stream")
def gpt5(prompt: str):
    model = ChatOpenAI(
        model='gpt-5.5',
        temperature=0,
        api_key=os.getenv("OPENAI_API_KEY")
    )

    # provider에 따라 형식을 맞춰준다
    messages = [
        SystemMessage("너는 친절한 조수야"),
        HumanMessage("내 이름은 근욱이야."),
        AIMessage("안녕하세요. 근욱님! 친절히 알려드릴께요"),
        HumanMessage(prompt)
    ]

    for chunk in model.stream(messages):
        print(chunk.content, end='', flush=True)

@router.get("/langchain/gpt/chat_prompt_template")
def chat_prompt_template(name: str, prompt: str):
    prompt_template = ChatPromptTemplate.from_messages([
        ("system", "너는 친절한 조수야"),
        ("human", "내 이름은 {name}이야."),
        ("ai", "안녕하세요. {name}님! 친절히 알려드릴께요"),
        ("human", '{prompt}') # 아직 '{prompt}'라는 글씨일 뿐이다
    ])

    prompt_template.invoke({
        "name": name, 
        "prompt": prompt
    })

    print(prompt_template)

@router.get("/langchain/gpt/messages_placeholder")
def messages_placeholder(name: str, prompt: str):
    prompt_template = ChatPromptTemplate.from_messages([
        ("system", "너는 친절한 조수야"),
        MessagesPlaceholder("history", optional=True), # optional=True는 선택사항으로 없어도 됨
        ("human", '{prompt}') # 아직 '{prompt}'라는 글씨일 뿐이다
    ])

    prompt_template.invoke({
        "history": [
            HumanMessage("내 이름은 근욱이야."),
            AIMessage("안녕하세요. 근욱님! 친절히 알려드릴께요"),
        ], 
        "prompt": prompt
    })

    print(prompt_template)

class Recipe(BaseModel):
    food: list[str]
    steps: list[str]

@router.get('/langchain/output_parser')
def output_parser(dish:str):

    output_parser = PydanticOutputParser(pydantic_object=Recipe)

    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                # ChatPromptTemplate.from_messages 에는 전달 요소가 2개가 되어야 함
                # "사용자가 입력한 요리의 레시피를 알려주세요." + "{format_instructions}" (',' 컴마가 없어서 합쳐짐)
                "사용자가 입력한 요리의 레시피를 알려주세요."
                "{format_instructions}"
            ),
            ("human", "{dish}")
        ]
    )

    prompt2 = prompt.partial(
        format_instructions=output_parser.get_format_instructions()
    )

    prompt_value = prompt2.invoke({
        "dish": dish
    })

    print(prompt_value)
    print('-'*30)

    model = ChatOpenAI(
        model='gpt-5.5',
        temperature=0,
        api_key=os.getenv("OPENAI_API_KEY")
    )

    ai_msg = model.invoke(prompt_value)
    print(ai_msg)

    result = output_parser.invoke(ai_msg)
    return result

@router.get('/langchain/str_output_parser')
def str_output_parser(dish:str):
    model = ChatOpenAI(
        model='gpt-5.5',
        temperature=0,
        api_key=os.getenv("OPENAI_API_KEY")
    )
    ai_msg = model.invoke(f'{dish}의 레시피를 간략히 알려줘.')

    # result = StrOutputParser().parse(ai_msg) # 전문이 다 나옴(json)
    result = StrOutputParser().invoke(ai_msg) # invoke사용 시 깔끔하게 content만 뽑아옴
    return result


@router.get('/langchain/chain')
def chain(name:str, dish:str):
    prompt_template = ChatPromptTemplate.from_messages([
        ("system", "너는 친절한 조수야"),
        ("human", "내 이름은 {name}이야."),
        ("ai", "안녕하세요. {name}님! 친절히 알려드릴께요"),
        ("human", '{prompt}') 
    ])

    model = ChatOpenAI(
        model='gpt-5.5',
        temperature=0,
        api_key=os.getenv("OPENAI_API_KEY")
    )

    # chain을 | 로 연결하게 되면 여러 작업을 한 번에 할 수 있다
    chain = prompt_template | model | StrOutputParser()
    result = chain.invoke({
        'name' : name,
        'prompt': f'{dish}의 레시피를 간략히 알려줘.'
    })

    return result

@router.get('/langchain/chain/pydantic')
def chain_pydantic(dish:str):

    output_parser = PydanticOutputParser(pydantic_object=Recipe)

    prompt = ChatPromptTemplate.from_messages([
        (
            'system',
            '너는 미슐랭 쉐프야. 나는 요리 초보고, 자취생이라 기구가 거의 없어'
            '내가 쉽고 빠르게 만들 수 있는 레시피를 알려줘'
            '{format_instructions}' # 필수는 아니자만, Pydantic의 형식을 미리 보여줌
        ),
        ('human', '{dish}')
    ]).partial( # .partial의 경우 이미 Pydantic을 가져가기 때문에 key값과 양식을 맞추어 줌
        format_instructions=output_parser.get_format_instructions()
    )

    model = ChatOpenAI(
        model='gpt-5.5',
        temperature=0,
        api_key=os.getenv("OPENAI_API_KEY")
    ).bind(
        # 출력 양식을 json으로 한다
        # .bind의 경우 json type으로 응답양식을 맞추지만 Pydantic과 무조건 key값이 일치한다고 보장할 수 없음 
        response_format={'type':'json_object'}
    )

    chain = prompt | model | output_parser

    result = chain.invoke({
        'dish' : dish
    })
    return result

@router.get('/langchain/chain/with_structured_output')
def chain_with_structured_output(dish:str):

    prompt = ChatPromptTemplate.from_messages([
        (
            'system',
            '너는 미슐랭 쉐프야. 나는 요리 초보고, 자취생이라 기구가 거의 없어'
            '내가 쉽고 빠르게 만들 수 있는 레시피를 알려줘. 계량도 내 것만으로 할 수 있도록'
        ),
        ('human', '{dish}')
    ])

    model = ChatOpenAI(
        model='gpt-5.5',
        temperature=0,
        api_key=os.getenv("OPENAI_API_KEY")
    )

    chain = prompt | model.with_structured_output(Recipe)

    return chain.invoke({
        'dish' : dish
    })

# import es_router
# 최상위 기준 절대경로이기 때문에 현재 폴더 기준으로 쓰려면 from .es_router로 해야 함
from router import es_router

# class hybrid_model(BaseModel):
#     # movies: dict[str, dict[str, str | float]]

# chain을 이용하여 CBF, CF를 llm을 사용해 답변 받아보기 (직접풀기)
@router.get('/langchain/recommend/hybrid/personal')
def recommend_hybrid(
    userId: int,                                # CF에서 사용 할 사용자 id
    provider: Literal['gemini', 'gpt'] = 'gpt', # 검색에 사용 할 LLM 선택
    top_k:int = 10,                             # 결과 개수
    candidate_size:int = 50,                    # 각각의 추천에의 후보 수
    list_movieId: list[int] = Query(...)        # CBF에서 사용 할 영화 목록
):
    '''
    def hybrid(
        userId: int,                # CF에서 사용 할 사용자 id
        top_k:int = 10,             # 결과 개수
        candidate_size:int = 50,     # 각각의 추천에의 후보 수
        list_movieId: list[int] = Query(...)    # CBF에서 사용 할 영화 목록
    ):  
    '''
    # 예전에 만들어 뒀던 hybrid 추천 결과를 그대로 가져와서
    # langchain으로 LLM에게 예쁘게 포장해달라고 해서 그 결과를 출력한다
    # 단, 사용자가 gpt와 gemini를 선택할 수 있게 하자
    print(provider, type(provider))

    hybrid = es_router.hybrid(userId, top_k, candidate_size, list_movieId)
    print('hybrid : ', hybrid)

    # output_parser = PydanticOutputParser(pydantic_object=hybrid_model)

    # prompt = ChatPromptTemplate.from_messages([
    #     (
    #         'system',
    #         '지금 결과물을 사용자에게 어떤 기준인지, 왜 추천했는지 정리해서 알려줘.'
    #         '정리할 땐 기존 JSON 형식을 네가 따로 표로 정리하는 형태로 해줘.'
    #         '{format_instructions}'
    #     ),
    #     ('human', '{hybrid}')
    # ]).partial(
    #     format_instructions=output_parser.get_format_instructions()
    # )
    prompt = ChatPromptTemplate.from_messages([
        (
            'system',
            '지금 결과물은 CBF + CF 하이브리드 추천 결과물이야.'
            '각 연관도에 따라 RRF로 점수를 매겼어.'
            '이 중에서 가장 추천하고 싶은 영화가 무엇인지 생각해.'
            '그 영화의 줄거리, 등장인물 등 주된 부분을 간략히 요약해서 알려줘.'
            '추가로 이 외에 2가지정도를 한 줄 정도로 더 추천해.'
            '최종은 HTML형태로 줘. MD형식이 아니라.'
        ),
        ('human', '{hybrid}')
    ])

    if provider == 'gemini':
        model = ChatGoogleGenerativeAI(
            model='gemini-3.8-flash',
            temperature=0,
            api_key=os.getenv("GEMINI_API_KEY")
        )

    elif provider == 'gpt' :
        model = ChatOpenAI(
            model='gpt-5.5',
            temperature=0,
            api_key=os.getenv("OPENAI_API_KEY")
        )

    chain = prompt | model | StrOutputParser()

    result = chain.invoke({
        'hybrid' : hybrid
    })

    print('-'*50)
    print(result)
    return result

# 강사님과 같이 풀이
@router.get('/langchain/recommend/hybrid')
def recommend_hybrid(
    userId: int,                # CF에서 사용 할 사용자 id
    provider: Literal['gemini', 'gpt'] = 'gpt',
    top_k:int = 10,             # 결과 개수
    candidate_size:int = 50,     # 각각의 추천에의 후보 수
    list_movieId: list[int] = Query(...)    # CBF에서 사용 할 영화 목록
):
    '''
    def hybrid(
        userId: int,                # CF에서 사용 할 사용자 id
        top_k:int = 10,             # 결과 개수
        candidate_size:int = 50,     # 각각의 추천에의 후보 수
        list_movieId: list[int] = Query(...)    # CBF에서 사용 할 영화 목록
    ):  
    '''
    # 예전에 만들어 뒀던 hybrid 추천 결과를 그대로 가져와서
    # langchain으로 LLM에게 예쁘게 포장해달라고 해서 그 결과를 출력한다
    # 단, 사용자가 gpt와 gemini를 선택할 수 있게 하자

    prompt = ChatPromptTemplate.from_messages([
        (
            'system',
            '너는 영화 추천 서비스의 설명 도우미야.'
            '필요하다면 인터넷 검색을 해서 알아봐.'
            '입력 받은 추천 결과만 사용해서 설명해야돼.'
            '결과는 구조적인 JSON으로 알려줘.'
        ),
        ('human', 
            'CBF, CF의 Hybrid추천 결과물 : {hybrid}'
            '제목을 한국(한글) 제목으로 변경해서도 알려줘. 단, 제목을 추측하지마.'
            '영화 줄거리도 알려줘. 단, 줄거리를 추측하지마.'
            '순위를 보고 3개 정도만 정리해주면 돼.'
        )
    ])

    hybrid = es_router.hybrid(userId, top_k, candidate_size, list_movieId)

    if provider == 'gemini':
        model = ChatGoogleGenerativeAI(
            model='gemini-3.8-flash',
            temperature=0,
            api_key=os.getenv("GEMINI_API_KEY")
        )

    else :
        model = ChatOpenAI(
            model='gpt-5.5',
            temperature=0,
            api_key=os.getenv("OPENAI_API_KEY")
        )

    chain = prompt | model | StrOutputParser()

    return chain.invoke({
        'hybrid' : hybrid
    })

