def attach_vectors(chunks, response_rows, index_name, dimensions=2):
    rows = sorted(response_rows, key=lambda row: row['index'])
    if [row['index'] for row in rows] != list(range(len(chunks))):
        raise ValueError('입력과 응답 index를 확인하세요.')
    actions = []
    for chunk, row in zip(chunks, rows):
        vector = row['embedding']
        if len(vector) != dimensions:
            raise ValueError('벡터 차원을 확인하세요.')
        source = {**chunk, 'embedding': vector}
        actions.append({
            '_index': index_name,
            '_id': f'{chunk["movieId"]}-{chunk["chunk_index"]}',
            '_source': source,
        })
    return actions
