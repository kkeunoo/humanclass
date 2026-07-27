a = 10
b = 5
print( 3 < a < 20 )

if True :
    print(1)
 #Indent가 들어가면 들여쓰기 오류
#  print(2) # IndentationError: unindent does not match any outer indentation level
    print(3)

    if True :
        print(4)

if True :
    pass # 아무 일도 하지 않고 넘어가는 것