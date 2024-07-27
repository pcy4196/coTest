# 문제 URL : https://www.acmicpc.net/problem/1238
import sys
input = sys.stdin.readline
from queue import PriorityQueue
# N: 노드 수 (마을 수), M: 간선 수 (도로 수), X: 파티가 열리는 마을 번호
N, M, X = map(int, input().split())

# adj: 각 노드에서 다른 노드로 가는 도로의 정보를 저장하는 인접 리스트
# radj: 도로의 방향을 반대로 하여 저장한 인접 리스트
adj  = [[] for _ in range(N+1)]
radj = [[] for _ in range(N+1)] 

# 간선 정보 입력 받기
for _ in range(M):
    a, b, t = map(int, input().split())
    adj[a].append((b, t))  # a에서 b로 가는 도로, 시간 t
    radj[b].append((a, t)) # b에서 a로 가는 도로, 시간 t (역방향)

# dist: X 마을에서 다른 마을로 가는 최단 거리
# rdist: 다른 마을에서 X 마을로 돌아오는 최단 거리
dist  = [sys.maxsize] * (N+1)
rdist = [sys.maxsize] * (N+1)
pq = PriorityQueue()

# 다익스트라 알고리즘을 사용하여 X에서 각 마을까지의 최단 거리 계산
dist[X] = 0
pq.put((0, X))
while pq.qsize() > 0:
    w, u = pq.get()
    for v, t in adj[u]:
        if dist[v] > dist[u] + t:
            dist[v] = dist[u] + t
            pq.put((dist[v], v))

# 역방향 그래프에 대해서도 같은 작업 수행하여 X로 돌아오는 최단 거리 계산
pq = PriorityQueue()
rdist[X] = 0
pq.put((0, X))
while pq.qsize() > 0:
    w, u = pq.get()
    for v, t in radj[u]:
        if rdist[v] > rdist[u] + t:
            rdist[v] = rdist[u] + t
            pq.put((rdist[v], v))

# 가장 오래 걸리는 왕복 시간을 계산
ans = -sys.maxsize
for i in range(1, N+1):
    ans = max(ans, dist[i] + rdist[i])

# 결과 출력
print(ans)