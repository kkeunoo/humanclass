# w : 수정 가능
file = open('hello.txt', 'w') # 파일이 없으면 만들고, 있다면 그 파일을 엶
file.write('eng\n123\n한글') # write로 쓸 내용 작성
file.flush() # flush는 버퍼가 꽉 차지 않아도 내보내기 (즉시 반영)
file.close()

# 한글 charset 
# 1. utf-8 , 2. euc-kr , 3. cp949
file = open('hello2.txt', 'w', encoding='utf-8') # encoding으로 utf-8등 지정해놓을 수 있음
file.write('eng\n123\n한글') 
file.close()

# r : 읽기 전용(readonly)
file = open('hello.txt', 'r') 
s = file.read()
file.close()
print(s)

# UnicodeDecodeError: 'cp949' codec can't decode byte 0xed in position 10: illegal multibyte sequence
# 윈도우용 한글 인코딩 에러가 발생하기 때문에 읽을때도 encoding 필요
file = open('hello2.txt', 'r', encoding='utf-8') # 기본적으로 euc-kr로 읽기 때문에 에러
s = file.read()
file.close()
print(s)

print('-'*20)
file = open('hello.txt', 'r') 
s = file.read(10) # 2Byte만 읽도록 인자값을 줄 수 있음
file.close()
print(s)

print('-'*20)
file = open('hello.txt', 'r', buffering=1) 
s = file.read()
file.close()
print(s)

print('-'*20)
text = ''
file = open('hello.txt', 'r') 
while True :
    chunk = file.read(2)
    if not chunk : 
        break
    text += chunk
    print(chunk)
file.close()    
print(text)
# 결과물
# en
# g

# 12
# 3

# 한글

# file = open('a.webp', 'rb') #binary 는 2진수를 뜻 함
# s = file.read()
# file.close()
# print(s)

file = open('hello.txt', 'r') 
s = file.read()
file.close()
print(s)

# with를 쓰면 close를 없앨 수 있음, 끝나면 알아서 종료 됨
with open('hello.txt', 'r') as file :
    s = file.read()
    print(s)

a = [1,2,3,4]

with open('array1.txt', 'w') as file :
    # file.write(str(file))
    file.write(str(a))
print(str(a))

with open('array1.txt', 'r') as file :
    b = file.read()
    print( type(b) , b)
    c = list(b)
    print( type(c) , c) # 리스트로 바꿔 저장하면 '[', '1', ',' 처럼 한개씩 쪼개어 저장됨

import pickle

name = 'eng'
age = 20
address = '한글'
arr = [1,2,3,4]
scores = {
    'k' : 1,
    'k2' : 'val'
}

# dump 함수에는 'wirte'가 내재되어있음
# 실무에서는 dump 1개만 사용함, 여러개로 하면 그 줄을 계속 넘어가야 하기 때문에
with open('pickle.p', 'wb') as f :
    pickle.dump(name, f)
    pickle.dump(age, f)
    pickle.dump(address, f)
    pickle.dump(arr, f)
    pickle.dump(scores, f)

with open('pickle.p', 'rb') as f :
    p1 = pickle.load(f)
    print(p1)
    p2 = pickle.load(f) # 저장 한 'int' 형태가 그대로 돌아옴
    print(p2, type(p2))
    p2 = pickle.load(f) 
    print(p2, type(p2))
    p2 = pickle.load(f) 
    print(p2, type(p2))
    p2 = pickle.load(f) 
    print(p2['k'], type(p2))
    # p2 = pickle.load(f) # EOFError: Ran out of input , 파일을 다 읽었는데 지나갈 때 End of File Error 출력
    # print(p2, type(p2))

    # dump 한 만큼만 꺼낼 수 있다
    # import joblib 는 pickle보다 더 대용량 처리 할 때 사용

with open('hello.txt', 'a') as f : # 'a'는 이어 쓰기(append)
    f.write('123')
    # f.read() # io.UnsupportedOperation: not readable / 읽을 수 없다는 에러 발생

# + 가 쓰기 계열에 붙어있으면, 읽기 가능해짐
# + 가 읽기 계열에 붙어있으면, 쓰기 가능해짐

# with open('word.txt', 'r') as file :
#     b = str(file.read().split(' ')).replace(',', '')
#     print(b)
#     for value in b :
#         if b.get('c') :
#             value += b
#             print(value,end='')

print('-'*30)
# 단어 중 대소문자 구분없이 c를 포함하는 단어를 출력하시오. 단 , . 은 출력하지 마시오
with open('word.txt', 'r') as file :
    # vf_파일 read하며 반복문에 넣어 바로 대소문자 검사 및 strip으로 ',' '.' 제거 후 출력
    for word in file.read().split(' ') :
        if 'c' in word.lower() :
            print(word.replace(',','').replace('.',''), end=' ')
print()

    # words = file.read().split(' ')
    # word.txt를 읽어오며 공백으로 split하여 words에 저장
    # print(words, type(words)) 

    # v1_range(len(words)) 는 그냥 'words'와 같기에 다음방법
    # print(words[0])
    # for i in range(len(words)) :
    #     if words[i].find('c') != -1 : 
    #         print(words[i].replace(',', ''))

    # v2_words 안에서 검사하되 출력 시 ,과 . replace 진행 + 대소문자 구분위해 lower() 사용
    # for word in words :
    #     if word.lower().find('c') != -1 : # find도 -1반환으로 알 수 있지만 문제풀었던 것 처럼 in 사용
    #         print(word.replace(',','').replace('.',''))

    # v3_words 안에 담긴 ,과 .를 미리 제거한 후 'c' 유효 검사
    # for word in words :
    #     word = word.replace(',','').replace('.','')
    #     if 'c' in word.lower() : # 대소문자 구분위해 lower() 사용
    #         print(word,end=' ')
print('-'*30)

# print('\n','-'*30)
# with open('test.txt', 'w+', encoding='utf-8') as f :
#     a = f.read().split('\n')
#     print(a)

    # f.write('test')
    # b = f.read().split()
    # print(b) 

# a = 7,8,9
# with open('test.txt', 'r+') as f :
#     print(f.read())

#     f.write(str(list(a)))
#     print(f.read())

a = [1,2,3,4,5]
print(a)
print(b)

