# 문제 URL : https://www.acmicpc.net/problem/1816

# 수의 개수 입력
N = int(input())

# 수를 담아두는 배열 선언
numArr = []
# 암호 입력 받기
for i in range(N):
    numArr.append(int(input()))

# 적절한 암호 여부 확인
for i in range(len(numArr)):
    for j in range(2, 1000001):
        if numArr[i] % j == 0:
            # 1,000,000 까지 소수 여부 확인
            print('NO')
            break
        if j == 1000000:
            print('YES')
