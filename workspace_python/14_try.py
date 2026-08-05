# try, except 사용 전 방법 1
def div(x, y) :
    if y != 0 :
        result = x / y
    else :
        print('두 번째 숫자는 0이 올 수 없습니다')
    return result

# try, except 사용 (무중단 시스템 구현 기초)
def div2(x, y) :
    result = 0
    try : # Error가 발생하면, 정지하지 않고 except로 내려감
        result = x / y # y에서 Error가 났기 때문에 result로 넘어가지 않고 내려 간 상태
    except :
        print('예외 발생')
    return result

def div3(x, y) :
    result = 0
    try : 
        result = x / y 
    except ZeroDivisionError : # Error Type별로 except를 지정해서 예외처리를 할 수 있음
        print('0으로 나눌 수 없습니다.')
    except TypeError : # ZeroDivision이 먼저 발생했다면, if elif처럼 먼저 발생 된 것에서 처리됨
        print('숫자만 넣어주세요.')
    return result

def div4(x, y) :
    result = 0
    try : 
        result = x / y 
    except ZeroDivisionError as e: # as e 처럼 e에 넣어둔다면, 예외 Error 메세지도 출력 됨
        print('0으로 나눌 수 없습니다.', e) 
    except TypeError as e: 
        print('숫자만 넣어주세요.', e)
    return result

def div5(x, y) :
    result = 0
    try : 
        result = x / y 
    except Exception as e: # Exception은 모든 Error의 부모 / 단, KeyboardInterrupt 등 ctrl+c 같은건 별개로 지정필요
        print('예외 발생', e) 
    return result

def div6(x, y) :
    result = 0
    try : 
        result = x / y 
    except Exception as e:
        print('예외 발생', e) 
    else : # try가 문제 없이 실행되었다면 else로 출력 가능
        print('문제 없었음')
    return result

def div7(x, y) :
    result = 0
    try : 
        result = x / y 
        return result # return을 위에 두어도 finally는 실행 됨
    except Exception as e:
        print('예외 발생', e) 
    else : 
        print('문제 없었음')
    finally : # finally는 무슨 일이 있어도 실행 됨, file에서 닫아주거나 할 때도 사용함
        print('무조건 실행완료')
    return result

a = div(7, 3)
print(a)

# a = div(7, 0)
# a = div2(7, 0)
# a = div(7, '3')
print(a)

div3(7, 0)
div3(7, 'a')

div4(7, 0)
div4(7, 'a')

div5(7, 0)
div5(7, 'a')

div6(7, 0)
div6(7, 2)

div7(7, 0)
div7(7, 2)

# raise Exception('메세지')

def loginCheck(id, pw) :
    if id == 'admin' and pw == '1234' :
        print('로그인 성공')
        return 0
    elif id == '' :
        print('아이디를 입력해주세요')
        return 1

def login() :
    id = 'admin'
    pw = '1234'
    result = loginCheck(id, pw)

    if result == 0 :
        print('메인 페이지로 이동')
    elif result == 1 :
        print('alert(아이디를 입력하세요)')

login()

def loginCheck2(id, pw) :
    if id == 'admin' and pw == '1234' :
        print('로그인 성공')
        return 0
    elif id == '' :
        print('아이디를 입력해주세요')
        raise Exception('code:1') # code:1 처럼 별도의 ErrMsg를 작성해서 그것으로도 판단할 수 있음
    
    elif pw == '' :
        print('비밀번호를 입력해주세요')
        raise TypeError('code:2')

def login2() :
    id = '111'
    pw = ''
    try : 
        result = loginCheck2(id, pw)
        if result == 0 :
            print('메인 페이지로 이동')
    except TypeError as e: # Exception이 더 큰 범위이기 때문에, TypeError가 있다면 위로 올려줌
        print(e)
        if e == 'code:2' :
            print('alert(비밀번호를 입력하세요)')
    except Exception as e:
        print(e)
        if e == 'code:1' :
            print('alert(아이디를 입력하세요)')

login2()

import traceback
try:
    a = 3 / 0
except Exception as e :
    print(e)
    traceback.print_exc() # 원래의 Error msg를 text로 담아와주는 모듈
    a = traceback.format_exc() # 변수에 Error msg를 변수에 담아둘 수 있음
    print('-'*30)
    print(a)

# *이터레이터와 제너레이터 구분 법 및 차이 설명 필요
# __iter__(이터레이터) 와 __next__ (다음)이 사실상 반복되는 것에 들어가있었고,
# 이터레이터와 next가 돌아가면서 값이 끝났을 때 StopInteration가 동작해서 멈춤
# 제너레이터는 yield에 값을 넣어서 하나씩 꺼내와 읽을 수 있음

# 코루틴은 제너레이터와 다르게 읽고 쓰기도 가능, 다만 실무 중요치는 없음

# 정규표현식도 간단하게 정리 필요