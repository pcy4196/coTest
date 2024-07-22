# 문제 URL : https://www.acmicpc.net/problem/11724
import sys
input = sys.stdin.readline

# 노드의 개수(N)와 간선의 개수(M)를 입력 받음
N, M = map(int, input().split())

# 그래프의 인접 리스트 초기화
adj = [[] for _ in range(N)]

# 모든 간선을 읽어 인접 리스트에 추가
for _ in range(M):
    a, b = map(int, input().split())
    a -= 1  # 입력 값은 1부터 시작하므로 0부터 시작하도록 조정
    b -= 1
    adj[a].append(b)
    adj[b].append(a)

# 각 노드의 방문 여부를 체크하는 리스트
chk = [0] * N

# 연결 요소의 개수를 세는 변수
ans = 0

# 모든 노드를 방문할 때까지 반복
while chk.count(0) > 0:
    q = []
    q.append(chk.index(0))  # 방문하지 않은 노드의 인덱스를 큐에 추가
    chk[q[0]] = 1           # 해당 노드를 방문했다고 표시
    
    # BFS를 사용하여 연결된 모든 노드를 방문
    while len(q) > 0:
        s = q.pop(0)
        for i in adj[s]:
            if chk[i] == 0:     # 방문하지 않은 노드를 찾으면
                chk[i] = 1      # 방문 표시를 하고
                q.append(i)     # 큐에 추가
    
    # 연결 요소의 개수 증가
    ans += 1

# 연결 요소의 개수를 출력
print(ans)