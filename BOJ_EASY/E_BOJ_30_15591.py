# 문제 URL : https://www.acmicpc.net/problem/15591
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)  # 재귀 호출 깊이 제한을 늘려줌

# N: 동영상의 수, Q: 쿼리의 수
N, Q = map(int, input().split())

# 인접 리스트를 사용해 그래프를 표현 (1부터 N까지 노드)
adj = [[] for _ in range(N + 1)]

# 그래프의 간선 정보 입력
for _ in range(N - 1):
    x, y, r = map(int, input().split())
    adj[x].append([y, r])  # 노드 x와 노드 y를 연결하는 유사도 r
    adj[y].append([x, r])  # 무방향 그래프이므로 양쪽에 추가

# DFS 함수 정의
def DFS(s, usado):
    global cnt      # 전역 변수 cnt를 사용
    if usado >= K:  # 현재 경로의 최소 유사도(usado)가 K 이상인 경우
        cnt += 1

    # 인접한 노드를 순회
    for i in range(len(adj[s])):
        d = adj[s][i][0]            # 인접 노드
        r = adj[s][i][1]            # 인접 노드와의 유사도

        if chk[d] == 0:             # 방문하지 않은 노드인 경우
            chk[d] = 1              # 방문 처리
            DFS(d, min(r, usado))   # 현재까지의 최소 유사도를 다음 노드로 전달

ans = []  # 결과를 저장할 리스트

# 각 쿼리에 대해 수행
for _ in range(Q):
    K, S = map(int, input().split())  # 유사도 K와 시작 노드 S 입력
    cnt = 0                 # 쿼리마다 cnt 초기화
    chk = [0] * (N + 1)     # 방문 체크 배열 초기화
    chk[S] = 1              # 시작 노드를 방문 처리
    DFS(S, sys.maxsize)     # DFS 시작 (유사도는 매우 큰 값으로 시작)
    ans.append(cnt - 1)     # 결과 저장 (시작 노드는 제외)

# 쿼리 결과 출력
for val in ans:
    print(val)