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
else : 
    pass

if 1 :
    print('참')

'''
Python에서 False란?
False, None(JavaScript:null), 0, 0.0, 빈 컨테이너(비어있는 문자열, 리스트, 튜플, 딕셔너리) 
'''

a = []
if a :
    print('참')
else :
    print('거짓')

# 교재 174P 문제 평균구하기
'''
국어 = int(input('국어 점수를 입력하세요: '))
영어 = int(input('영어 점수를 입력하세요: '))
수학 = int(input('수학 점수를 입력하세요: '))
과학 = int(input('과학 점수를 입력하세요: '))

result = (국어 + 영어 + 수학 + 과학)/4

if result >= 80 :
    (print('합격입니다.'))
else :
    (print('불합격입니다.'))
'''

score = input('점수 4개 입력, 띄어쓰기로 구분 : ')
print(score, score.split(' '))
scores = score.split(' ')
sum = int(scores[0]) + int(scores[1]) + int(scores[2]) + int(scores[3])
avg = sum / len(scores) 

# \ 를 쓰게되면 엔터를 없앨 수 있어서, 실제 코드는 한 줄이지만 내릴 때 사용
if (0 <= int(scores[0]) <= 100) \
    and (0 <= int(scores[1]) <= 100) \
    and (0 <= int(scores[2]) <= 100) \
    and (0 <= int(scores[3]) <= 100) :

    if avg >= 80 :
        print('합격')
    else :
        print('불합격') 
else :
    print('잘못된 입력입니다.')

# 교재 178P 자판기 문제
button = int(input('번호를 입력하세요 : '))

if button == 1 :
    print('콜라')
elif button == 2 :
    print('사이다')
elif button == 3 :
    print('환타')
else :
    print('잘못 입력하셨습니다.')

# match , case문 / break 필요 없고 default 대신 case _ : 를 씀
# ~또는(or) 는 |로 구분해서 써줘야 함
# a = '여름' 
a = 7 
match a :
    case 6 | 7 | 8 :
        print('봄')
    case '여름' :
        print('여름')
    case _ :
        print('그 외')

# 값이 3 > 2 이면 3 출력, 아니라면 2 출력
print( 3 if 3 > 2 else 2)