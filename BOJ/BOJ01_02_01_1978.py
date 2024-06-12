# 문제 URL : https://www.acmicpc.net/problem/1978
import sys
input = sys.stdin.readline

# 소수여부 판단하는 함수
# 소수가 아닌 경우 -1 반환
def chkPrime(num):
    if num == 1:
        return 1
    if num == 2 or num == 3:
        return 0
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return 1
    return 0

# 수의 개수 입력 처리
N = int(input())
arr = list(map(int, input().split()))

# 소수의 개수를 출력
ans = N

for i in arr:
    ans -= chkPrime(i)

print(ans)
