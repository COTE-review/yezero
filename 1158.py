import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
a = deque(range(1,n+1))
ans = []

for _ in range(n) :
    for _ in range(k-1):
        t = a.popleft()
        a.append(t)
    j = a.popleft()
    ans.append(j)

print('<', end='')
for x in ans:
    if x == ans[-1]:
        print(x, end='')
    else:
        print(x, end=', ')
print('>')

#n과 k를 입력받고
#1부터 n까지의 자연수를 a에 큐의 형태로 저장
#popleft함수를 이용하여 1~(k-1)번째 사람을 큐에서 삭제하고
#다시 append함수로 큐에 추가시킴
#k번째 사람은 큐에서 빼내서 ans 배열에 추가시킴
#이 과정을 반복

#배열 ans에 추가된 순서대로 숫자를 출력시킴