t = int(input())
stack = []

for _ in range(t):
    bar = int(input())

    while stack and stack[-1] <= bar:
        stack.pop()
    stack.append(bar)

print(len(stack))

#막대기가 한 개씩 추가될 때
#이전에 추가된 막대기보다 작거나 같으면
#stack 리스트에서 없애버리기