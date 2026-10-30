import re


def split_text(text, chunk_size=30, overlap_size=6):
    sentences = re.split(r'(?<=[.!?])\s+', text.strip())
    sentences = [s.strip() for s in sentences if s.strip()]
    chunks = []
    temp = ''
    for sentence in sentences:
        candidate = f'{temp} {sentence}' if temp else sentence
        if len(candidate) <= chunk_size:
            temp = candidate
        else:
            if temp:
                chunks.append(temp)
            temp = sentence
    if temp:
        chunks.append(temp)
    overlap_chunks = []
    for index, chunk in enumerate(chunks):
        if index == 0:
            overlap_chunks.append(chunk)
        else:
            prefix = chunks[index - 1][-overlap_size:] if overlap_size > 0 else ''
            overlap_chunks.append(f'{prefix} {chunk}'.strip())
    return overlap_chunks


def build_actions(doc, embed):
    actions = []
    for index, chunk in enumerate(split_text(doc['content'])):
        vector = embed(doc['title'], chunk)
        source = {**doc, 'content': chunk, 'chunk_index': index, 'embedding': vector}
        actions.append({'_index': 'computer_chunk', '_id': f'{doc["id"]}-{index}', '_source': source})
    return actions
