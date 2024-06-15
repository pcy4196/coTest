# 문제 URL : https://www.acmicpc.net/problem/14252
import sys
input = sys.stdin.readline

# 숫자 입력 처리
N = int(input())  # N: 숫자의 개수

# 공약수 비교할 숫자 입력 처리(정렬)
nArr = sorted(list(map(int, input().split())))  # nArr: 입력된 숫자들을 정렬하여 저장

# 정답 출력 변수
ans = 0  # ans: 정답을 저장하는 변수

# 공약수 구하는 함수 선언
def gcd(a, b):
    # 유클리드 호제법을 사용하여 최대공약수 구하기
    while a % b != 0:
        tmp = a % b
        a = b
        b = tmp
    return b  # b: 최대공약수

# 인접한 두 수의 공약수가 1인 여부 확인
for i in range(N-1):
    if gcd(nArr[i], nArr[i+1]) != 1:  # 공약수가 1이 아닌 경우
        for j in range(nArr[i] + 1, nArr[i+1]):
            if gcd(nArr[i], j) == 1 and gcd(j, nArr[i+1]) == 1:  # 공약수가 1인 수가 있다면
                ans += 1
                break
            if j == nArr[i+1] - 1:  # 두 수 사이에 공약수가 1인 수가 없다면
                ans += 2

print(ans)