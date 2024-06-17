# 문제 URL : https://www.acmicpc.net/problem/1912
import sys
input = sys.stdin.readline

# 첫 번째 줄에서 n을 입력받음 (수열의 크기)
n = int(input())
# 수열을 입력받아 리스트로 저장
arr = list(map(int, input().split()))

# 누적 최대 합을 담을 리스트 선언, 길이는 n+1로 설정
prefix = [0] * (n + 1)

# 누적 최대 합 계산
for i in range(n):
    # 이전까지의 누적합에 현재 원소를 더한 값과 현재 원소 중 최대값을 선택
    prefix[i + 1] = max(prefix[i] + arr[i], arr[i])

# 누적합 리스트에서 첫 번째 원소를 제외한 값들 중 최대값을 출력
print(max(prefix[1:]))
