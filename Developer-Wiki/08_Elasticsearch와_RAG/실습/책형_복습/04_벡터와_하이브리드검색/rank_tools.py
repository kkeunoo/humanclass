def fuse(text_hits, vector_hits, rank_constant=60, size=10):
    scores = {}
    for hits in [text_hits, vector_hits]:
        for rank, hit in enumerate(hits, start=1):
            doc_id = hit['_id']
            if doc_id not in scores:
                scores[doc_id] = {'score': 0.0, 'source': hit['_source']}
            scores[doc_id]['score'] += 1 / (rank_constant + rank)
    ordered = sorted(scores.items(), key=lambda item: item[1]['score'], reverse=True)
    results = []
    for doc_id, data in ordered[:size]:
        results.append({'id': doc_id, 'document': data['source'], 'score': data['score']})
    return {'results': results, 'total': len(scores)}
