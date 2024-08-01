# 문제 URL : https://www.acmicpc.net/problem/1463
import sys
input = sys.stdin.readline

# 정수 N을 입력 받습니다.
N = int(input())

# 최소 연산 횟수를 저장할 배열을 N+1 크기로 초기화합니다.
# 인덱스 0은 사용되지 않으므로 N+1 크기로 설정
dArr = [0] * (N+1)

# 1은 연산 필요 없음 (0번의 연산으로 가능)
dArr[1] = 0

# 2부터 N까지 순회하면서 최소 연산 횟수를 계산
for i in range(2, N+1):
    # 기본적으로 1을 빼는 연산을 가정
    dArr[i] = 1 + dArr[i-1]
    
    # 3으로 나누어 떨어질 때, 3으로 나누는 연산을 고려
    if i % 3 == 0:
        cnt = 1 + dArr[i // 3]
        # 3으로 나누는 것이 더 적은 연산을 필요로 할 경우 업데이트
        dArr[i] = min(cnt, dArr[i])
        
    # 2로 나누어 떨어질 때, 2로 나누는 연산을 고려
    if i % 2 == 0:
        cnt = 1 + dArr[i // 2]
        # 2로 나누는 것이 더 적은 연산을 필요로 할 경우 업데이트
        dArr[i] = min(cnt, dArr[i])

# N을 1로 만드는 데 필요한 최소 연산 횟수를 출력
print(dArr[N])