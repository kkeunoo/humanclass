text = '90 80 70 80'
parts = text.split()
if len(parts) != 4:
    print('점수 개수 확인')
else:
    a, b, c, d = int(parts[0]), int(parts[1]), int(parts[2]), int(parts[3])
    if 0 <= a <= 100 and 0 <= b <= 100 and 0 <= c <= 100 and 0 <= d <= 100:
        average = (a + b + c + d) / 4
        if average >= 80:
            print('합격', average)
        else:
            print('불합격', average)
    else:
        print('점수 범위 확인')
button = 2
if button == 1:
    print('콜라')
elif button == 2:
    print('사이다')
else:
    print('다른 번호')
month = 7
match month:
    case 6 | 7 | 8:
        print('여름')
    case _:
        print('다른 계절')
print('있음' if parts else '없음')
