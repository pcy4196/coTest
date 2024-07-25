# 문제 URL : https://www.acmicpc.net/problem/11725
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)        # 재귀 호출 한도를 설정하여 깊은 재귀를 지원

# 입력
N = int(input())  # 노드의 개수
adj = [[] for _ in range(N+1)]      # 인접 리스트 초기화 (1부터 N까지 사용)

# 간선 입력 받아 인접 리스트에 저장
for _ in range(N-1):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

# 부모 노드를 저장할 배열 초기화
# 0번 인덱스는 사용하지 않고, parent[1]은 루트 노드이므로 0을 넣음
# 나머지는 아직 부모가 설정되지 않았음을 나타내기 위해 -1로 초기화
parent = [0] + [0] + [-1] * (N-1)

# DFS를 통해 각 노드의 부모 노드를 찾는 함수
def dfs(idx):
    for i in adj[idx]:          # 현재 노드와 연결된 노드들을 탐색
        if parent[i] == -1:     # 부모 노드가 아직 설정되지 않은 경우
            parent[i] = idx     # 현재 노드를 부모로 설정
            dfs(i)              # 연결된 노드에 대해 DFS 수행

dfs(1)  # 1번 노드가 루트이므로 DFS 시작

# 각 노드의 부모 노드 출력 (2번 노드부터 N번 노드까지)
for i in range(2, N+1):
    print(parent[i])