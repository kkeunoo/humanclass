from langchain_core.messages import HumanMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

template = ChatPromptTemplate.from_messages([
    ('system', '영화 도우미'),
    MessagesPlaceholder('history', optional=True),
    ('human', '{question}'),
])
prompt = template.invoke({
    'history': [HumanMessage('액션을 좋아해요')],
    'question': '영화 하나 추천해 주세요',
})
for message in prompt.to_messages():
    print(message.type, message.content)
