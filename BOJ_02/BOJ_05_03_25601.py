# 문제 URL : https://www.acmicpc.net/problem/25601
import sys
input = sys.stdin.readline

N = int(input())
par = {}
for _ in range(N-1):
    a, b = input().split()
    par[a] = b

a, b = input().split()
ans = 0
for i in range(2):
    if i == 0:
        x = a
        chk = b
    else:
        x = b
        chk = a
    
    while x in par:
        x = par[x]
        if x == chk:
            ans = 1
            break

print(ans)
