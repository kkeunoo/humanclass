def build_context(results):
    contexts = []
    for index, result in enumerate(results):
        doc = result['document']
        contexts.append(
            f"[검색 결과 {index}] 문서ID={doc['id']} 청크={doc['chunk_index']}\n"
            f"제목={doc['title']}\n내용={doc['content']}"
        )
    return '\n-------\n'.join(contexts)


def ask_rag(question, search, generate):
    results = search(question)['results']
    if not results:
        return '제공된 문서에서 확인할 수 없습니다.'
    context = build_context(results)
    prompt = f'문맥에 있는 내용으로만 한국어로 답하세요.\n질문: {question}\n문맥:\n{context}'
    return generate(prompt)
