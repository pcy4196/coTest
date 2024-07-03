# 문제 URL : https://www.acmicpc.net/problem/14465
import sys
input = sys.stdin.readline

# N: 신호등의 개수, K: 연속된 신호등의 개수, B: 고장난 신호등의 개수
N, K, B = map(int ,input().split())

# 신호등 상태를 저장할 리스트 (0: 정상, 1: 고장)
sinho = [0] * N

# 누적합을 저장할 리스트 (0번 인덱스는 0으로 초기화)
psum = [0] * (N + 1)

# 고장난 신호등의 위치를 입력받아 리스트에 반영
for _ in range(B):
    num = int(input())
    sinho[num-1] = 1  # 고장난 신호등 위치를 1로 표시

# 누적합 배열 생성 (1번 인덱스부터 시작)
for i in range(1, N+1):
    psum[i] = psum[i-1] + sinho[i-1]

# 고쳐야 하는 신호등의 개수를 저장할 리스트
ans = []

# K개의 연속된 구간에서 고장난 신호등의 수를 계산
for i in range(K, N+1):
    ans.append(psum[i] - psum[i-K])

# 가장 작은 고장난 신호등의 수를 출력
print(min(ans))