# 문제 URL : https://www.acmicpc.net/problem/1389
import sys
input = sys.stdin.readline

# N: 사람의 수, M: 친구 관계의 수
N, M = map(int, input().split())
# 인접 리스트를 이용하여 친구 관계를 저장
adj = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    a -= 1  # 입력이 1부터 시작하므로 0부터 시작하도록 조정
    b -= 1
    adj[a].append(b)
    adj[b].append(a)

minNum = sys.maxsize    # 최소 케빈 베이컨 수를 초기화
minIdx = -1             # 최소 케빈 베이컨 수를 가진 사람의 인덱스를 초기화

# 각 사람에 대해 BFS를 수행하여 케빈 베이컨 수를 계산
for i in range(N):
    dist = [-1] * N     # 각 사람까지의 거리를 저장하는 리스트, 초기값 -1
    chk = [0] * N       # 방문 여부를 체크하는 리스트
    q = [i]             # BFS를 위한 큐, 시작점은 i
    chk[i] = 1          # 시작점 방문 체크
    dist[i] = 0         # 시작점의 거리는 0
    
    while len(q) > 0:
        s = q.pop(0)            # 큐에서 하나의 정점을 꺼냄
        for j in adj[s]:        # 꺼낸 정점과 인접한 모든 정점에 대해
            if chk[j] == 0:     # 아직 방문하지 않았다면
                chk[j] = 1      # 방문 체크
                q.append(j)     # 큐에 추가
                dist[j] = dist[s] + 1  # 거리 갱신 (현재 정점의 거리 + 1)
    
    dNum = sum(dist)    # 모든 거리의 합 (케빈 베이컨 수)
    if dNum < minNum:   # 현재의 케빈 베이컨 수가 최소값보다 작다면
        minNum = dNum   # 최소값 갱신
        minIdx = i      # 최소값을 가진 사람의 인덱스 갱신

print(minIdx + 1)       # 1부터 시작하는 인덱스로 출력