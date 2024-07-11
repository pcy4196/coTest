# 문제 URL : https://www.acmicpc.net/problem/14888
import sys
input = sys.stdin.readline

# 첫째 줄에 수의 개수 N을 입력받음
N = int(input().strip())

# 둘째 줄에 N개의 수를 리스트로 입력받음
arr = list(map(int, input().strip().split()))

# 셋째 줄에 덧셈, 뺄셈, 곱셈, 나눗셈 연산자의 개수를 입력받음
A, B, C, D = map(int, input().strip().split())

# 결과를 저장할 변수들을 초기화
maxAns = -1000000000  # 최대값을 저장할 변수
minAns = 1000000000   # 최소값을 저장할 변수

# 재귀 함수를 정의하여 모든 경우의 수를 탐색
def rec(n, sm, a, b, c, d):
    global maxAns
    global minAns

    if sm > 1000000000 or sm < -1000000000:
        return

    # 종료 조건: 모든 수를 사용한 경우
    if n == N:
        maxAns = max(maxAns, sm)  # 최대값 갱신
        minAns = min(minAns, sm)  # 최소값 갱신
        return
    
    # 각 연산자를 사용할 수 있는지 체크하고, 사용할 수 있으면 재귀 호출
    if a > 0:  # 덧셈 연산자가 남아 있는 경우
        rec(n+1, sm+arr[n], a-1, b, c, d)
    if b > 0:  # 뺄셈 연산자가 남아 있는 경우
        rec(n+1, sm-arr[n], a, b-1, c, d)
    if c > 0:  # 곱셈 연산자가 남아 있는 경우
        rec(n+1, sm*arr[n], a, b, c-1, d)
    if d > 0:  # 나눗셈 연산자가 남아 있는 경우
        rec(n+1, int(sm/arr[n]), a, b, c, d-1)  # 나눗셈은 정수 나눗셈을 사용

# 재귀 함수 호출을 시작, 첫 번째 수는 이미 사용한 것으로 처리
rec(1, arr[0], A, B, C, D)
print(maxAns)
print(minAns)