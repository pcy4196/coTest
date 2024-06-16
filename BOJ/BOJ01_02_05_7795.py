# 문제 URL : https://www.acmicpc.net/problem/7795
import sys
input = sys.stdin.readline

# 각 테스트 케이스 수를 입력받음
T = int(input())
# 각 테스트 케이스의 결과를 저장할 리스트
ans = [0] * T

for i in range(T):
    # 각 테스트 케이스에서 N과 M을 입력받음
    N, M = map(int, input().split())
    # A와 B 리스트를 입력받고 정렬함
    A = sorted(list(map(int, input().split())))
    B = sorted(list(map(int, input().split())))
    
    cnt = 0     # 큰 쌍의 개수를 세기 위한 변수
    a = 0       # A 리스트의 인덱스
    b = 0       # B 리스트의 인덱스

    # A 리스트의 모든 원소를 확인할 때까지 반복
    while a < N:
        if b == M:    # B 리스트의 끝에 도달한 경우
            cnt += b  # 현재까지의 b 값을 cnt에 더함
            a += 1    # A 리스트의 다음 원소로 이동
        else:
            if A[a] <= B[b]:  # A의 현재 원소가 B의 현재 원소보다 작거나 같은 경우
                cnt += b  # 현재까지의 b 값을 cnt에 더함
                a += 1    # A 리스트의 다음 원소로 이동
            else:
                b += 1  # A의 현재 원소가 B의 현재 원소보다 큰 경우, B의 다음 원소로 이동

    # 현재 테스트 케이스의 결과를 저장
    ans[i] = cnt

# 각 테스트 케이스의 결과를 출력
for i in range(len(ans)):
    print(ans[i])
