# 문제 URL : https://www.acmicpc.net/problem/1748
import sys
input = sys.stdin.readline

# 입력을 받아서 정수형으로 변환
N = int(input())

# 자리수(i)와 결과값(ans)를 초기화
i = 1
ans = 0

while True:
    # 현재 자리수에서의 마지막 수(end)를 계산
    end = int('9' * i)
    # 현재 자리수에서의 시작 수(start)를 계산
    start = 1 * 10 ** (i - 1)
    
    # 입력받은 수 N이 현재 자리수의 마지막 수(end)보다 큰 경우
    if N > end:
        # 현재 자리수의 모든 수들의 자릿수를 더함
        ans += (end - start + 1) * i
        # 자리수를 증가시킴
        i += 1
    else:
        # N이 현재 자리수의 범위 안에 있는 경우
        # N까지의 수들의 자릿수를 더하고 루프를 종료
        ans += (N - start + 1) * i
        break

# 최종 결과값 출력
print(ans)
