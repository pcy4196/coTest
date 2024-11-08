# 문제 URL : https://www.acmicpc.net/problem/6118
import sys
input = sys.stdin.readline
from collections import deque

# 정점의 개수 N과 간선의 개수 M 입력
N, M = map(int, input().split())

# 그래프를 인접 리스트 방식으로 초기화
v = [[] for _ in range(N + 1)]

# 각 간선 정보 입력
for _ in range(M):
    a, b = map(int, input().split())
    v[a].append(b)
    v[b].append(a)

# 각 정점까지의 최단 거리를 저장할 배열 dis, 초기값은 매우 큰 값으로 설정
dis = [sys.maxsize] * (N + 1)

# 시작 정점 1의 거리를 0으로 설정
dis[1] = 0

# BFS를 위한 큐 생성 및 시작 정점 1 추가
q = deque()
q.append(1)

# BFS 수행
while len(q) > 0:
    # 큐에서 현재 정점 꺼내기
    cur = q.popleft()
    
    # 현재 정점과 연결된 모든 인접 정점 i에 대해
    for i in v[cur]:
        # 현재 정점을 거쳐 i로 가는 거리가 기존 거리보다 짧다면 갱신
        if dis[cur] + 1 < dis[i]:
            dis[i] = dis[cur] + 1  # 최단 거리 갱신
            q.append(i)  # 큐에 i를 추가하여 다음에 탐색

# 최장 거리(mNum)를 dis에서 1번 정점을 제외한 부분에서 찾기
mNum = max(dis[1:])

# 가장 멀리 있는 헛간 번호와 그 거리, 그리고 같은 거리를 가지는 헛간 수 초기화
aNum = 0
cNum = 0

# 각 정점에 대해 가장 멀리 있는 헛간 번호(aNum)와 동일 거리 헛간 수(cNum) 찾기
for i in range(1, N + 1):
    if dis[i] == mNum:
        # aNum이 아직 설정되지 않았다면 i로 설정
        if aNum == 0:
            aNum = i
        # 동일 거리 헛간 수 증가
        cNum += 1

# 가장 멀리 있는 헛간 번호, 거리, 동일 거리 헛간 수 출력
print(aNum, mNum, cNum)