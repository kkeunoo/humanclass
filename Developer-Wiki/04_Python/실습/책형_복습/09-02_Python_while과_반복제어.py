rolls = [1, 5, 3]  # 실제 난수가 아닌 설명용 뽑기 순서
count = 0
dice = 0
while dice != 3:
    dice = rolls[count]
    count += 1
    print('뽑기', count, dice)
print('끝', count)
for target in [2, 20]:
    index = 0
    while index < 4:
        if index == target:
            print('찾음', target)
            break
        index += 1
    else:
        print('못찾음', target)
