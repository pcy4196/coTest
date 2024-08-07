# 문제 URL : https://www.acmicpc.net/problem/14916
import sys
input = sys.stdin.readline

# 입력값 N을 정수로 읽어들임
N = int(input())

# 0부터 N // 2까지의 범위를 순회
for i in range(N // 2 + 1):
    # N에서 2*i를 뺀 값이 5로 나누어 떨어지는지 확인
    if (N - 2 * i) % 5 == 0:
        cnt2 = i                    # 2원 동전의 개수는 i
        cnt5 = (N - 2 * i) // 5     # 5원 동전의 개수는 (N - 2*i) // 5
        # 총 동전 개수를 출력하고 프로그램 종료
        print(cnt2 + cnt5)
        sys.exit()

# 2원과 5원 동전으로 N을 만들 수 없는 경우 -1 출력
print(-1)