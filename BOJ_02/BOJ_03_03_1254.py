# 문제 URL : https://www.acmicpc.net/problem/1254
import sys
input = sys.stdin.readline

S = input().rstrip()

for i in range(len(S)):
    p = S[i:]
    rP = ''
    for j in p:
        rP = j + rP
    if p == rP:
        print(len(S) + i)
        break
    