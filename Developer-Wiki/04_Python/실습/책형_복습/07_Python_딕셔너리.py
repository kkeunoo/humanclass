item = {'가격': 1000, '수량': 2, '상세': {'이름': '공책'}}
print(item['가격'])
print(item.get('쿠폰'))
print(item.get('쿠폰', 0))
print('이름' in item, '이름' in item['상세'])
item['수량'] = 3
item['색상'] = '파랑'
print(len(item))
for key, value in item.items():
    print(key, value)
item.update(수량=4, 할인=100)
discount = item.pop('할인')
print(discount, item.get('할인'))
print(item.pop('할인', 0))
pair = item.popitem()
print(pair)
print(list(item.keys()))
defaults = dict.fromkeys(['a', 'b'])
print(defaults)
letters = set('hello')
print(len(letters), 'l' in letters)
