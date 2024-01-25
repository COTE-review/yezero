import sys
from collections import deque

t = int(input())

for i in range(t):
    n, m = map(int, input().split())
    queue = deque(list(map(int, sys.stdin.readline().split())))
    count = 0
    while queue:
        best = max(queue)
        front = queue.popleft()
        m = m - 1

        if best == front:
            count = count + 1
            if m < 0:
                print(count)
                break

        else:
            queue.append(front)
            if m < 0:
                m = len(queue) - 1

#input으로 입력받고
#'best'에 큐의 최댓값을 저장
#큐의 front를 뽑음
#뽑았으니까 m은 1감소
                
#front가 중요도가 제일 크면
#count를 1 증가시키고
#m이 음수가 되었으면 과정을 종료하고 count를 출력한다
                
#front가 중요도가 제일 큰 문서가 아니라면
#해당 문서를 큐의 맨 뒤에 추가시킨다
#이 과정을 반복