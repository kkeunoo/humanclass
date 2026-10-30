answer = 50
guesses = [20, 70, 50]  # 설명용 입력 순서
count = 0
for guess in guesses:
    count += 1
    if guess < answer:
        print('UP')
    elif guess > answer:
        print('DOWN')
    else:
        print('정답 시도', count)
        break
ballots = ['a', 'b', 'a', 'c', 'a']  # 설명용 투표 순서
counts = {}
for name in ballots:
    counts[name] = counts.get(name, 0) + 1
print(counts)
print('키의 max', max(counts))
winner = None
best_count = -1
for name, votes in counts.items():
    if votes > best_count:
        winner = name
        best_count = votes
print('최다', winner, best_count)
