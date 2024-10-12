# 문제 URL : https://www.acmicpc.net/problem/2458
import sys
input = sys.stdin.readline

def dfs(cur, edge):

    for i in edge[cur]:
        if chk[i] == 0:
            chk[i] = 1
            dfs(i, edge)

N, M = map(int, input().split())
v = [[] for i in range(N+1)]
rv = [[] for i in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    v[a].append(b)
    rv[b].append(a)

ans = 0
for i in range(1, N+1):
    chk = [0] * (N+1)

    dfs(i, v)
    dfs(i, rv)

    if sum(chk) == N-1:
        ans += 1

print(ans)