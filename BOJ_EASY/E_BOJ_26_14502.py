# 문제 URL : https://www.acmicpc.net/problem/14502
import sys
input = sys.stdin.readline
from itertools import combinations
from collections import deque

N, M = map(int, input().split())
# 연구소의 상태를 저장할 2차원 리스트 brd 초기화
brd = []
for _ in range(N):
    # 연구소의 각 행을 입력받아 brd에 추가
    brd.append(list(map(int, input().split())))

# 빈 칸(0)의 좌표를 저장할 리스트 cell 초기화
cell = []
for x in range(N):
    for y in range(M):
        if brd[x][y] == 0:
            cell.append((x, y))  # 빈 칸 좌표를 cell 리스트에 추가

# 상하좌우 방향 이동을 위한 델타 값
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 최대 안전 영역의 크기를 저장할 변수 ans 초기화
ans = 0

# 빈 칸 중 3개를 선택하여 벽을 세우는 모든 조합을 생성
for com in combinations(cell, 3):
    # 선택된 3개의 좌표에 벽(1)을 세움
    for x, y in com:
        brd[x][y] = 1

    # 바이러스 확산을 체크하기 위한 2차원 리스트 chk 초기화
    chk = [[0] * M for _ in range(N)]
    dq = deque()  # BFS를 위한 덱 초기화

    # 연구소의 모든 위치를 탐색하여 바이러스(2) 위치를 큐에 추가
    for x in range(N):
        for y in range(M):
            if brd[x][y] == 2:
                dq.append((x, y))   # 바이러스 위치를 큐에 추가
                chk[x][y] = 1       # 바이러스 위치는 방문 처리

    # BFS를 사용하여 바이러스를 확산시킴
    while dq:
        x, y = dq.popleft()     # 큐에서 현재 위치를 꺼냄
        for i in range(4):      # 상하좌우로 이동
            nx = x + dx[i]
            ny = y + dy[i]
            # 이동한 위치가 연구소 범위 내에 있고, 빈 칸이며, 아직 방문하지 않았다면
            if 0 <= nx < N and 0 <= ny < M and brd[nx][ny] == 0 and chk[nx][ny] == 0:
                dq.append((nx, ny))     # 큐에 추가하여 확산 계속
                chk[nx][ny] = 1         # 방문 처리

    # 바이러스 확산이 끝난 후, 안전 영역(0의 개수)을 계산
    locAns = 0
    for x in range(N):
        for y in range(M):
            # 빈 칸이면서 바이러스가 퍼지지 않은 칸을 센다
            if brd[x][y] == 0 and chk[x][y] == 0:
                locAns += 1

    # 현재 조합에서의 최대 안전 영역 크기를 갱신
    ans = max(ans, locAns)

    # 벽을 세웠던 자리를 원래대로 복구
    for x, y in com:
        brd[x][y] = 0

# 최대로 확보할 수 있는 안전 영역의 크기를 출력
print(ans)