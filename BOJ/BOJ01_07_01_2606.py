# 문제 URL : https://www.acmicpc.net/problem/2606
import sys
input = sys.stdin.readline

# 컴퓨터(노드)의 수를 입력받음
N = int(input())
# 그래프를 저장할 인접 리스트를 초기화 (1번 인덱스부터 사용하기 위해 N+1)
adj = [[] for _ in range(N+1)]

# 연결된 컴퓨터 쌍의 수를 입력받음
T = int(input())
# 각 연결 정보를 입력받아 인접 리스트에 추가
for _ in range(T):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

# 각 컴퓨터의 방문 여부를 저장할 리스트를 초기화 (처음엔 모두 방문하지 않음)
visited = [0] * (N+1)

# BFS를 위한 큐를 초기화하고, 1번 컴퓨터(감염된 컴퓨터)를 큐에 추가
q = []
q.append(1)
visited[1] = 1  # 1번 컴퓨터를 방문 처리
ans = 0         # 감염된 컴퓨터 수를 세기 위한 변수

# 큐가 빌 때까지 반복
while q:
    s = q.pop(0)            # 큐의 앞에서부터 노드를 꺼냄
    for i in adj[s]:        # 꺼낸 노드와 연결된 모든 노드를 확인
        if visited[i] == 0: # 만약 해당 노드를 아직 방문하지 않았다면
            q.append(i)     # 큐에 추가하고
            visited[i] = 1  # 방문 처리
            ans += 1        # 감염된 컴퓨터 수 증가

# 감염된 컴퓨터 수를 출력
print(ans)
