todo_list = []

d1 = {
    'id' : 1684,
    'item' : 'item1'
}
todo_list.append(d1)
print(todo_list)

d2 = {
    'id' : 29681,
    'item' : 'item2'
}
todo_list.append(d2)
print(todo_list)

# id가 2인 것의 모든 딕셔너리 출력
# print(todo_list[1].get('id'))

for i in todo_list :
    # print(i.get('id'))
    if i.get('id') == 29681 :
        print(i)

# update
for todo in todo_list :
    if todo.get('id') == 29681 :
        todo['item'] = '아이템2'
print(todo_list)

# id가 29681인 것의 index를 찾아내고, pop으로 해당 index를 지우세요
for i in range(len(todo_list)) :
    print('i', i)
    if todo_list[i].get('id') == 29681:
        todo_list.pop(i)
        break
print(todo_list)

todo_list = [ todo for todo in todo_list if todo.get('id') != 29681 ]
print(todo_list)


print(todo_list)

# 할 일
# crud.py 생성 후 라우팅
# todo_list를 전역변수를 만들고 CRUD하는 라우터를 설정하고, 
# api.py를 실행해서 테스트 진행
# 생성하면 list를 return, 읽을 땐 id를 받아서 상세 내역만 보이게
# 업데이트 시 리스트 전체가 return, 삭제를 해도 리스트 전체 return