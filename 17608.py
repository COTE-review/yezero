import sys
input = sys.stdin.readline

t = int(input())
stack = []

for _ in range(t):
    stack.append(int(input()))
count = 0
max = 0
for x in reversed(stack):
    if max < x:
        max = x
        count += 1

print(count)

#막대기가 한 개씩 추가될 때
#이전에 추가된 막대기보다 작거나 같으면
#stack 리스트에서 없애버리기
#로 하려고 했는데 시간초과가 떠서
#그냥 리스트를 역순으로 정렬해서
#하나씩 비교하는 걸로 바꿈