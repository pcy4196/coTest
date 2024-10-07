# 문제 URL : https://www.acmicpc.net/problem/17451
import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

ans = arr[N-1]

for i in range(N-1)[::-1]:
    if ans % arr[i] == 0:
        continue

    ans = (ans // arr[i] + 1) * arr[i]

print(ans)
