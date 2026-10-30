import json
from pathlib import Path


def load_documents():
    path = Path(__file__).resolve().parent / 'documents.json'
    with path.open(encoding='utf-8') as file:
        return json.load(file)


def build_actions(documents):
    actions = []
    for doc in documents:
        actions.append({'_index': 'computer', '_id': doc['id'], '_source': doc})
    return actions
