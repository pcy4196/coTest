# 문제 URL : https://www.acmicpc.net/problem/2458
import sys
input = sys.stdin.readline

def dfs(cur, edge):
    # 현재 노드 cur에서 시작해 DFS 탐색을 수행하는 함수
    for i in edge[cur]:     # 현재 노드와 연결된 모든 노드를 탐색
        if chk[i] == 0:     # 아직 방문하지 않은 노드라면
            chk[i] = 1      # 해당 노드를 방문 처리
            dfs(i, edge)    # 해당 노드로부터 DFS 탐색을 계속함

N, M = map(int, input().split())    # N: 학생 수, M: 비교 횟수 (엣지 수)
v = [[] for i in range(N+1)]        # 정방향
rv = [[] for i in range(N+1)]       # 역방향

for _ in range(M):
    a, b = map(int, input().split())    # a < b (a는 b보다 키가 작다)
    v[a].append(b)                      # a -> b (정방향 그래프에 추가)
    rv[b].append(a)                     # b <- a (역방향 그래프에 추가)

ans = 0                     # 자신이 몇 번째인지 정확히 알 수 있는 학생 수를 저장할 변수
for i in range(1, N+1):
    chk = [0] * (N+1)       # 각 학생이 방문되었는지를 표시하는 리스트, 초기화 (1-based index)

    dfs(i, v)   # i번 학생을 기준으로 키가 큰 학생들을 탐색 (정방향 그래프 탐색)
    dfs(i, rv)  # i번 학생을 기준으로 키가 작은 학생들을 탐색 (역방향 그래프 탐색)

    # i번 학생을 기준으로 키가 큰 학생들과 작은 학생들을 모두 탐색한 결과
    # 자신을 제외한 모든 학생들과의 비교가 가능한 경우
    if sum(chk) == N-1:     # 자신을 제외한 N-1명이 모두 chk 배열에 체크되었으면
        ans += 1            # 자신의 순서를 정확히 알 수 있는 학생으로 카운트

print(ans)  # 자신이 몇 번째인지 정확히 알 수 있는 학생의 수 출력