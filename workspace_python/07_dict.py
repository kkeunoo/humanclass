
# 딕셔너리 선언
a = {}
a = dict()
print(type(a))

b = {
    # key는 javascript와 다르게 ''를 써줘야 함 (웬만해선 str)
    # 중복된 key값이 2개일 경우, 뒤에 오는 value를 가져옴
    '이름': '홍길동',
    '직업': '도적',
    '스킬': {
        '공격': '훔치기',
        '방어': '도망가기',
        'javascript': '중'
    }
}

print(b)

c = dict(a=10, b=20)
print(c)

# b.이름
print( b['이름'] )
# print( b['이름2'] ) # 없는 key일 경우 KeyError: '이름2'

print( b.get('이름') )
print( b.get('이름2') ) # get으로 받을 경우 'None'이 나옴, 더 안전한 방법
print( b.get('이름2', '이름없음') ) # 있으면 그 값이 나오고, 없을 경우 두 번째 인자값이 나옴

d = b['스킬']
d['공격']
b['스킬']['공격']
print( b['스킬']['공격'] )

print( b.get('스킬').get('공격') )
# print( b.get('스킬2').get('공격') ) # AttributeError: 'NoneType' object has no attribute 'get'
print( b.get('스킬2', {}).get('공격', 0) ) # 스킬2라는 key가 없어도 에러가 나지 않도록 빈 dict 생성

b['직업'] = '전사' # dict key에 value 할당하기
print( b )

b['직업2'] = '전사2' # 가지고 올 때만 없으면 안 되는 것이고, 없으면 추가함
print( b )

print( '스킬' in b ) # True
print( '공격' in b['스킬']) # True
print( '공격' not in b['스킬']) # False
print( '공격' in b.get('스킬')) # True

print( len(b) ) # key의 개수를 알 수 있음

e = b.keys() # dict_keys(['이름', '직업', '스킬', '직업2']), 유사배열로 나옴 (list형변환 해서 사용)
print( e )

f = b.values() # dict_values(['홍길동', '전사', {'공격': '훔치기', '방어': '도망가기', 'javascript': '중'}, '전사2'])
print( f )
# print( f[0] ) # 배열이 아니기 때문에 못 씀
print( list(f)[0] ) 

g = b.items() # key,value를 tuple로 저장해줌
print( g )

# b['스킬']['버프'] = '힐'
# print(b)

a = 'hello'
print( list(a) ) # ['h', 'e', 'l', 'l', 'o']
print( set(a) ) # {'o', 'e', 'l', 'h'} , 중복은 제거하지만 순서는 중요하지 않음 (jason key값이 set으로 관리되기 때문에 중복 없음)