from document_tools import load_documents, build_actions

mappings = {'properties': {
    'title': {'type': 'text'},
    'category': {'type': 'keyword'},
    'price': {'type': 'integer'},
}}
documents = load_documents()
actions = build_actions(documents)
print('문서 수:', len(documents))
print('대상·ID:', actions[0]['_index'], actions[0]['_id'])
print('본문 제목:', actions[0]['_source']['title'])
print('분류 타입:', mappings['properties']['category']['type'])
print('전송 여부:', False)
