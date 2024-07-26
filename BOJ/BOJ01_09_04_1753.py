# 문제 URL : https://www.acmicpc.net/problem/1753
import sys
input = sys.stdin.readline
from queue import PriorityQueue

V, E = map(int, input().split())    # 정점의 수 V와 간선의 수 E 입력 받음
K = int(input())                    # 시작 정점 K 입력 받음
adj = [[] for _ in range(V+1)]      # 인접 리스트 초기화, 정점 번호는 1부터 시작하므로 V+1 크기로 생성
for _ in range(E):
    u, v, w = map(int, input().split())  # 간선 정보 입력 받음: u에서 v로 가는 가중치 w인 간선
    adj[u].append((v, w))                # 인접 리스트에 간선 정보 추가

pq = PriorityQueue()        # 우선순위 큐 생성
dist = [0] + [10**9] * V    # 거리 리스트 초기화, 무한대를 나타내기 위해 큰 수(10**9) 사용

dist[K] = 0     # 시작 정점 K의 거리를 0으로 설정
pq.put((0, K))  # 시작 정점을 우선순위 큐에 삽입

while pq.qsize() > 0:   # 큐가 빌 때까지 반복
    w, u = pq.get()     # 큐에서 가장 짧은 거리를 가진 정점 꺼내기

    for v, w1 in adj[u]:            # 현재 정점 u에서 이동할 수 있는 모든 정점 v에 대해
        if dist[v] > dist[u] + w1:  # 기존 거리보다 현재 경로를 통한 거리가 더 짧다면
            dist[v] = dist[u] + w1  # 거리 갱신
            pq.put((dist[v], v))    # 갱신된 거리와 정점을 큐에 삽입

for i in range(1, V+1):             # 1번 정점부터 V번 정점까지 거리 출력
    if dist[i] == 10**9:            # 무한대 거리라면 도달할 수 없는 정점이므로
        print('INF')                # 'INF' 출력
    else:
        print(dist[i])              # 도달 가능한 거리 출력
