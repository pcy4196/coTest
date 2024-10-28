# 문제 URL : https://www.acmicpc.net/problem/3474
import sys
input = sys.stdin.readline

aArr = []
T = int(input())

for _ in range(T):
    n = int(input())
    cnt = 0
    di = 5
    while di <= n:
        cnt += n // di
        di = di * 5
    aArr.append(cnt)

for ans in aArr:
    print(ans)