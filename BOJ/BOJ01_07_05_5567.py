# 문제 URL : https://www.acmicpc.net/problem/5567
import sys
input = sys.stdin.readline

# 입력받기
n = int(input())  # n: 사람의 수 (상근이 포함)
m = int(input())  # m: 친구 관계의 수
adj = [[] for _ in range(n)]  # 인접 리스트 생성 (각 사람마다 친구 목록)

f1 = [0] * n  # 상근이의 친구 목록
f2 = [0] * n  # 상근이 친구의 친구 목록

# 친구 관계 입력받기
for _ in range(m):
    a, b = map(int, input().split())
    adj[a-1].append(b-1)  # 인접 리스트에 친구 추가 (0-indexed)
    adj[b-1].append(a-1)  # 양방향 관계이므로 양쪽에 추가

# 상근이의 친구 찾기
for i in adj[0]:  # 상근이의 친구들을 순회
    f1[i] = 1  # 친구로 표시

# 상근이 친구의 친구 찾기
for i in range(n):
    if f1[i] != 1:  # 상근이의 친구가 아니면 무시
        continue
    
    for j in adj[i]:  # 상근이 친구의 친구들을 순회
        if j != 0 and f1[j] == 0:  # 상근이 본인이 아니고, 이미 친구로 표시된 적이 없으면
            f2[j] = 1  # 친구의 친구로 표시

# 상근이의 친구와 친구의 친구의 수를 더하여 출력
print(sum(f1) + sum(f2))
