def plan_actions(documents):
    actions = []
    seen_ids = set()
    for doc in documents:
        doc_id = doc.get('id')
        if doc_id is None:
            raise ValueError('문서 id가 필요합니다.')
        if doc_id in seen_ids:
            raise ValueError('중복 id를 확인하세요.')
        seen_ids.add(doc_id)
        source = {**doc}
        actions.append({'_index': 'computer', '_id': doc_id, '_source': source})
    return actions
