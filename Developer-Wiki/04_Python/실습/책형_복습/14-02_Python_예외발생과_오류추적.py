import traceback
def check_fields(user, password):
    if user == '':
        raise Exception('code:1')
    if password == '':
        raise TypeError('code:2')
    return True
for user, password in [('', 'practice'), ('student', ''), ('student', 'practice')]:
    try:
        print('입력 확인', check_fields(user, password))
    except TypeError as error:
        print('객체 직접 비교', error == 'code:2')
        print('메시지 비교', str(error) == 'code:2')
        print('비밀번호 안내')
    except Exception as error:
        if str(error) == 'code:1':
            print('아이디 안내')
try:
    result = 3 / 0
except ZeroDivisionError as error:
    trace = traceback.format_exc()
    print(str(error))
    print('종류가 기록됨', 'ZeroDivisionError' in trace)
