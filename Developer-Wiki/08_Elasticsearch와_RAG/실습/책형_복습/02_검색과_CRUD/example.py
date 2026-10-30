from search_tools import formatter

query = {'bool': {
    'filter': [{'term': {'category': 'laptop'}}],
    'must': [{'match': {'content': '메모리'}}],
}}
response = {'hits': {
    'total': {'value': 1, 'relation': 'eq'},
    'hits': [{'_id': '1', '_score': 2.0, '_source': {
        'id': 1, 'title': '메모리 안내', 'price': 100,
    }}],
}}
result = formatter(response)
print('필터:', query['bool']['filter'][0]['term'])
print('총수·반환수:', result['total'], len(result['results']))
print('제목·점수:', result['results'][0]['document']['title'], result['results'][0]['score'])
document = {'id': 1, 'title': '메모리 안내', 'price': 100}
print('잘못된 키:', document.get(id, -1))
print('문자열 키:', document.get('id', -1))
document.update({'price': 120})
print('부분 변경 뒤:', document['title'], document['price'])
