from sys import stdin, stdout

n = stdin.readline()
N = sorted(map(int, stdin.readline().split()))
m = stdin.readline()
M = map(int, stdin.readline().split())

def binary(l, N, start, end):
    if start > end :
        return 0
    m = (start+end)//2
    if l == N[m]:
        return 1
    elif l < N[m]:
        return binary(l, N, start, m-1)
    else:
        return binary(l, N, m+1, end)
    
for l in M:
    start = 0
    end = len(N) - 1
    print(binary(l, N, start, end))

#첫번째 집합(A)과 두번째 집합(B)를 입력받음
#A 집합을 입력받을 때 오름차순으로 정렬함
#이진 탐색을 구현함
#A집합의 중간값부터 B집합의 값을 각각 비교하여
#있으면 1을, 없으면 0을 반환