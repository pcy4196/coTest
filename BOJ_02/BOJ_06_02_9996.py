# 문제 URL : https://www.acmicpc.net/problem/9996
import sys
input = sys.stdin.readline

N = int(input())
p = input().rstrip()
pf = ''
pb = ''
for i in range(len(p)):
    if p[i] == '*':
        pf = p[:i]
        pb = p[i+1:]

aArr = []

for _ in range(N):
    s = input().rstrip()
    if len(s) >= len(pf) + len(pb) and s[:len(pf)] == pf and s[-len(pb):] == pb:
        aArr.append('DA')
    else:
        aArr.append('NE')

for ans in aArr:
    print(ans)