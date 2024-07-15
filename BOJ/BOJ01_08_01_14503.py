# 문제 URL : https://www.acmicpc.net/problem/14503
import sys
input = sys.stdin.readline

# 방향 벡터: 북, 서, 남, 동
di = [-1, 0, 1, 0]
dj = [0, -1, 0, 1]

"""
방향 매핑:
0 -> 0 (북)
1 -> 3 (서)
2 -> 2 (남)
3 -> 1 (동)
"""

# 그리드 크기 입력
N, M = map(int, input().split())

# 시작 위치와 방향 입력
si, sj, sd = map(int, input().split())

# 그리드 맵 입력
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

ans = 0  # 청소한 구역의 수

# 초기 방향 조정
if sd % 2 != 0:
    if sd == 1:
        sd = 3  # 동 -> 서
    else:
        sd = 1  # 서 -> 동

chk = True
while chk:
    # 현재 위치가 청소되지 않은 경우 청소
    if arr[si][sj] == 0:
        arr[si][sj] = 2
        ans += 1

    for i in range(1, 5):
        # 왼쪽 방향으로 회전
        nd = (sd + i) % 4
        ni, nj = si + di[nd], sj + dj[nd]
        # 청소하지 않은 공간이 있는 경우 이동
        if arr[ni][nj] == 0:
            si, sj, sd = ni, nj, nd
            break
    else:
        # 네 방향 모두 청소가 되어 있거나 벽인 경우 후진
        ni, nj = si - di[sd], sj - dj[sd]
        if arr[ni][nj] == 1:
            chk = False  # 후진할 수 없으면 종료
        else:
            si, sj = ni, nj  # 후진

# 청소한 구역의 수 출력
print(ans)
