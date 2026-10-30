from chunk_tools import build_actions
from rank_tools import fuse
from rag_tools import ask_rag

documents = [
    {'id': 1, 'title': '메모리 안내', 'category': 'laptop', 'content': 'RAM은 16GB입니다.'},
    {'id': 2, 'title': '저장장치 안내', 'category': 'laptop', 'content': 'SSD는 512GB입니다.'},
]


def fixed_embedding(title, content):
    return [0.1, 0.2]


actions = []
for document in documents:
    actions.extend(build_actions(document, fixed_embedding))
hits = [{'_id': a['_id'], '_source': a['_source']} for a in actions]
text_hits = [hits[0]]
vector_hits = [hits[1], hits[0]]
combined = fuse(text_hits, vector_hits)
sent_prompts = []


def fixed_search(question):
    return combined


def fixed_generate(prompt):
    sent_prompts.append(prompt)
    return '고정 응답: RAM은 16GB입니다.'


print('준비 작업:', len(actions))
print('청크 ID:', [a['_id'] for a in actions])
print('합친 순서:', [row['id'] for row in combined['results']])
print(ask_rag('메모리는?', fixed_search, fixed_generate))
print('문맥의 메모리:', 'RAM은 16GB입니다.' in sent_prompts[0])
print('문맥의 저장장치:', 'SSD는 512GB입니다.' in sent_prompts[0])
print('생성 대역 호출:', len(sent_prompts))
print('외부 전송:', False)
