# 문제 URL : https://www.acmicpc.net/problem/11403
import sys
input = sys.stdin.readline

N = int(input())

# arr[i][j]는 i번 정점에서 j번 정점으로 가는 간선이 있는지 여부(1: 있음, 0: 없음)
arr = [list(map(int, input().split())) for _ in range(N)]

# 깊이 우선 탐색(DFS) 함수 정의
def dfs(cur):
    # 현재 노드 cur에서 인접한 모든 노드를 탐색
    for i in range(len(arr[cur])):  # arr[cur]의 각 노드에 대해
        # 아직 방문하지 않은 노드(i),
        # arr[cur][i]가 1이면 경로가 존재함을 의미
        if visited[i] == 0 and arr[cur][i] == 1:
            visited[i] = 1  # 방문 표시
            dfs(i)          # i번 노드에서 다시 DFS 탐색

# 모든 정점 i에 대해 DFS 실행
for i in range(N):
    # 각 i에 대해 방문 여부를 저장하는 리스트, 매번 새롭게 초기화
    visited = [0] * N  
    dfs(i)
    print(*visited)