# 문제 URL : https://www.acmicpc.net/problem/14267
import sys
input = sys.stdin.readline

# n: 직원의 수, m: 칭찬 횟수
n, m = map(int, input().split())
# parent: 각 직원의 상사 번호 (-1은 루트)
parent = list(map(int, input().split()))

# 상사의 번호를 0부터 시작하도록 조정
for i in range(n):
    if parent[i] != -1:
        parent[i] -= 1

# praise: 각 직원이 받은 칭찬의 수를 저장하는 리스트
praise = [0] * n

# m번의 칭찬 정보를 입력받아 처리
for _ in range(m):
    idx, cnt = map(int, input().split())
    praise[idx - 1] += cnt  # 해당 직원의 칭찬 수에 추가

# 칭찬을 전달하는 과정
# 루트 직원(0번)을 제외한 나머지 직원들에 대해 칭찬을 상사로부터 전달받음
for i in range(1, n):
    praise[i] += praise[parent[i]]

# 각 직원이 받은 최종 칭찬 수를 출력
print(*praise)