# 문제 URL : https://www.acmicpc.net/problem/2417
import sys
input = sys.stdin.readline

# 입력값 n을 정수로 읽어들임
n = int(input())

# 이분 탐색을 위한 시작점과 끝점 설정
s = 0 
e = 2**63
ans = -1

# 이분 탐색 수행
while s <= e:
    mid = (s + e) // 2  # 중간값 계산
    if mid**2 >= n:     # 중간값의 제곱이 n보다 크거나 같은 경우
        ans = mid       # 가능한 답으로 설정
        e = mid - 1     # 더 작은 범위에서 탐색 계속
    else:
        s = mid + 1     # 중간값의 제곱이 n보다 작은 경우 더 큰 범위에서 탐색

# 정답 출력
print(ans)