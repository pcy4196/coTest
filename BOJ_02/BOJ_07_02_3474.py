# 문제 URL : https://www.acmicpc.net/problem/3474
import sys
input = sys.stdin.readline

# 결과를 저장할 배열 aArr 생성
aArr = []

# 테스트 케이스 수 T 입력
T = int(input())

# 각 테스트 케이스에 대해 반복
for _ in range(T):
    # 입력받은 수 n
    n = int(input())
    
    # n!에서 끝자리의 0의 개수를 저장할 cnt 초기화
    cnt = 0
    
    # 5의 배수만큼 나누기 위해 초기값 di를 5로 설정
    di = 5
    
    # n 이상이 될 때까지 반복 (n!에서 5의 배수가 포함된 개수를 찾는 과정)
    while di <= n:
        # n을 현재 di(5의 배수)로 나눈 몫을 cnt에 더함
        # (각 단계에서 5의 배수가 몇 번 곱해지는지 세기 위함)
        cnt += n // di
        
        # di를 다음 5의 배수로 증가
        di = di * 5
    
    # 각 테스트 케이스 결과를 aArr에 추가
    aArr.append(cnt)

# 각 테스트 케이스에 대한 결과를 출력
for ans in aArr:
    print(ans)