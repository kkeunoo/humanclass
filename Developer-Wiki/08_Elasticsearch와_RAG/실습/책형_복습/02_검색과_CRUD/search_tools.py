def formatter(resp):
    results = []
    for hit in resp['hits']['hits']:
        results.append({
            'document': hit.get('_source', {}),
            'score': hit.get('_score'),
        })
    return {'results': results, 'total': resp['hits']['total']['value']}
