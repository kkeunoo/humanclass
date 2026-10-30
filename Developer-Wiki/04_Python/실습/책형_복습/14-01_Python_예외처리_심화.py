def divide(x, y):
    result = None
    try:
        result = x / y
    except ZeroDivisionError as error:
        print('0 나눗셈 처리')
    except TypeError as error:
        print('종류 오류 처리')
    else:
        print('정상 else')
    finally:
        print('정리 finally')
    return result
for x, y in [(7, 2), (7, 0), (7, 'a')]:
    print('반환', divide(x, y))
def early_return():
    try:
        return 10
    except Exception:
        print('예외')
    else:
        print('여기 else는 실행 안 됨')
    finally:
        print('반환 중 finally')
print(early_return())
