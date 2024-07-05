# 문제 URL : https://www.acmicpc.net/problem/1068
import sys
input = sys.stdin.readline

# 입력 받기
N = int(input())                            # 노드의 수
parent = list(map(int, input().split()))    # 각 노드의 부모 노드
rmv = int(input())                          # 제거할 노드의 번호

# 루트 노드 찾기
root = -1
for i in range(N):
    if parent[i] == -1:  # 부모가 -1인 노드가 루트 노드
        root = i
        break

# rNode 배열을 사용하여 제거된 노드와 그 자식 노드를 표시
rNode = [0] * N
for i in range(N):
    u = i
    while True:
        if u == rmv:        # 현재 노드가 제거된 노드와 같으면
            rNode[i] = 1    # 제거된 노드로 표시
            break
        if u == root:       # 루트 노드에 도달하면 PASS
            break
        u = parent[u]       # 부모 노드로 이동

# pNode 배열을 사용하여 부모가 제거되지 않은 노드를 표시
pNode = [0] * N
for i in range(N):
    if i == root:           # 루트 노드는 제외
        continue
    if rNode[i] == 1:       # 제거된 노드는 제외
        continue
    pNode[parent[i]] = 1    # 부모 노드를 표시

# 리프 노드의 개수를 세기
ans = 0
for i in range(N):
    if rNode[i] != 1 and pNode[i] != 1: # 제거된 노드가 아니고 부모가 아닌 노드
        ans += 1                        # 리프 노드로 간주하고 개수를 증가

print(ans)  # 리프 노드의 수를 출력