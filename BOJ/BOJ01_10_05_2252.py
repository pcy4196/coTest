# 문제 URL : https://www.acmicpc.net/problem/2252
from queue import PriorityQueue
import sys
input = sys.stdin.readline

N, M = map(int, input().split())    # N: 학생 수, M: 정보의 수 (간선의 수)
adj = [[] for _ in range(N+1)]      # 인접 리스트 초기화
inD = [-1] + [0] * N                # 각 노드의 진입차수를 저장할 리스트 초기화

for _ in range(M):
    a, b = map(int, input().split())    # a에서 b로 가는 간선 정보 입력
    adj[a].append(b)                    # 인접 리스트에 간선 추가
    inD[b] += 1                         # b의 진입차수 증가

pq = PriorityQueue()                    # 우선순위 큐 생성
for i in range(1, N+1):
    if inD[i] == 0:                     # 진입차수가 0인 노드를 큐에 추가
        pq.put(i)

ans = []                                # 정렬된 결과를 저장할 리스트
while pq.qsize() > 0:                   # 큐가 빌 때까지 반복
    n = pq.get()                        # 큐에서 노드를 꺼냄
    ans.append(n)                       # 결과 리스트에 추가
    for i in adj[n]:                    # 현재 노드와 연결된 모든 노드에 대해
        inD[i] -= 1                     # 연결된 노드의 진입차수를 감소
        if inD[i] == 0:                 # 진입차수가 0이 되면
            pq.put(i)                   # 큐에 추가

print(*ans)  # 결과 출력