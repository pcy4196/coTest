# 문제 URL : https://www.acmicpc.net/problem/1946
import sys
input = sys.stdin.readline

ans = []
T = int(input())
for _ in range(T):
    N = int(input())
    arr = []
    for _ in range(N):
        arr.append(list(map(int, input().split())))
    arr.sort()
    cnt = 1
    rank = arr[0][1]
    for i in range(1, N):
        vsNum = arr[i][1]
        if vsNum < rank:
            cnt += 1
        rank = min(vsNum, rank)
    
    ans.append(cnt)

for i in range(T):
    print(ans[i])
