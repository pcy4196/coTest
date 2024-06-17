# 문제 URL : https://www.acmicpc.net/problem/2559
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
# 측정한 온도를 리스트로 입력받음
arr = list(map(int, input().split()))
# 누적합을 담을 리스트 선언, 길이는 N+1로 설정
prefix = [0] * (N + 1)

# 누적합 계산
for i in range(N):
    prefix[i + 1] = prefix[i] + arr[i]

# 최대 합을 찾기 위한 리스트 선언
ans = []
# K일간의 합을 구해서 리스트에 추가
for i in range(K, len(prefix)):
    ans.append(prefix[i] - prefix[i - K])

# 최대 합 출력
print(max(ans))