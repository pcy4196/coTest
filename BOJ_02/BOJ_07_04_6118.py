# 문제 URL : https://www.acmicpc.net/problem/6118
import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
v = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    v[a].append(b)
    v[b].append(a)
dis = [sys.maxsize] * (N+1)
dis[1] = 0
q = deque()
q.append(1)

while len(q) > 0:
    cur = q.popleft()
    for i in v[cur]:
        if dis[cur] + 1 < dis[i]:
            dis[i] = dis[cur] + 1
            q.append(i)

mNum = max(dis[1:])
aNum = 0
cNum = 0
for i in range(1, N+1):
    if dis[i] == mNum:
        if aNum == 0:
            aNum = i
        cNum += 1

print(aNum, mNum, cNum)