from plan_tools import plan_actions

documents = [{'id': 1, 'title': '안내'}]
actions = plan_actions(documents)
print('작업:', actions[0]['_index'], actions[0]['_id'])
print('본문 독립:', actions[0]['_source'] is not documents[0])
for invalid in [[{'title': '누락'}], [{'id': 1}, {'id': 1}]]:
    try:
        plan_actions(invalid)
    except ValueError as error:
        print(error)
print('빈 목록:', plan_actions([]))
