# import는 숫자로 시작하면 안된다
# 폴더가 있을 경우 .으로 구분한다

# import로 하던, from으로 하던 메모리의 용량 차이는 없으며 경로를 알려주는 것

# import fn.fn_15_1 
import fn.fn_15_1 as fn1 # import로 가져와 as로 별칭을 정할 수 있음

# a = fn.fn_15_1.add(1,2)
a = fn1.add(1,2)
print(a)

from fn.fn_15_1 import add as addd, sub as subb
from fn.fn_15_1 import sub # from으로 가져와 그 안에있는 특정 함수만 import로 가져올 수 있음
b = sub(3,2)
print(b)

import random
print(random.random())

# from random import random
from random import random as rand
# print(random())
print(rand())

from fn.fn_15_1 import Hero # 다른 file의 class의 def를 가져오는 방법
h = Hero()
h.attack()

import urllib.request
response = urllib.request.urlopen('http://www.google.co.kr')
print(response.read().decode('utf-8'))