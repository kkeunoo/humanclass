"""설명용 새 모듈. 한 단계 리스트의 입력 변경과 새 결과를 비교한다."""


def append_in_place(items, item):
    items.append(item)


def with_added_item(items, item):
    new_items = items.copy()
    new_items.append(item)
    return new_items
