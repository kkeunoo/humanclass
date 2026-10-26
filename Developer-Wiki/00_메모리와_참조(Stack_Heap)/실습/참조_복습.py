"""새로 구성한 복습 파일. 출력부터 예상한 뒤 실행한다."""

original = [1, 2]
same = original
copied = original.copy()

same.append(3)
copied[0] = 9

print("original:", original)
print("same is original:", same is original)
print("copied:", copied)
