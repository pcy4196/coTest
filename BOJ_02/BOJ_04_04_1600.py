# 문제 URL : https://www.acmicpc.net/problem/1600
import sys
input = sys.stdin.readline
from collections import deque

K = int(input())
Y, X = map(int, input().split())
arr = []
for i in range(X):
    arr.append(list(map(int, input().split())))

visited = [[[False] * (K + 1) for _ in range(Y)] for _ in range(X)]
dist = [[[-1] * (K + 1) for _ in range(Y)] for _ in range(X)]

dist[0][0][K] = 0

q = deque()
q.append([0, 0, K])

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

dx2 = [-2, -2, -1, -1, 1, 1, 2, 2]
dy2 = [-1, 1, -2, 2, -2, 2, -1, 1]

while q:
    x, y, k = q.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= X or ny < 0 or ny >= Y:
            continue
        if arr[nx][ny] != 1 and not visited[nx][ny][k]:
            visited[nx][ny][k] = True
            dist[nx][ny][k] = dist[x][y][k] + 1
            q.append([nx, ny, k])
    
    for i in range(8):
        nx = x + dx2[i]
        ny = y + dy2[i]

        if nx < 0 or nx >= X or ny < 0 or ny >= Y:
            continue
        if arr[nx][ny] != 1 and k > 0 and not visited[nx][ny][k-1]:
            visited[nx][ny][k-1] = True
            dist[nx][ny][k-1] = dist[x][y][k] + 1
            q.append([nx, ny, k-1])

ans = sys.maxsize
for num in dist[X-1][Y-1]:
    if num != -1:
        ans = min(num, ans)

if ans == sys.maxsize:
    print(-1)
else:
    print(ans)
