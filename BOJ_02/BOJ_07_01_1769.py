# 문제 URL : https://www.acmicpc.net/problem/1769
import sys
input = sys.stdin.readline

# 입력된 숫자를 정수로 변환하여 변수 N에 저장
N = int(input())

# N을 문자열로 변환하여 n에 저장 (각 자리 숫자를 다루기 위함)
n = str(N)

# 반복 횟수를 카운트할 변수 cnt를 0으로 초기화
cnt = 0

# n의 길이가 1보다 큰 동안 반복 (한 자리 수가 될 때까지 반복)
while len(n) > 1:
    # 각 자리 수를 더한 값을 저장할 변수 num 초기화
    num = 0
    
    # 문자열 n의 각 문자(각 자리 숫자)에 대해 반복
    for i in n:
        # 각 문자를 정수로 변환하여 num에 더함
        num += int(i)
    
    # 한 번 더할 때마다 반복 횟수를 카운트
    cnt += 1
    
    # 각 자리수를 더한 결과 num을 문자열로 변환하여 n에 저장 (n의 자릿수를 줄이기 위해)
    n = str(num)

# cnt 출력 (몇 번의 반복을 거쳤는지)
print(cnt)

# 마지막 남은 n이 '3', '6', '9' 중 하나라면 'YES' 출력, 그렇지 않으면 'NO' 출력
if n == '3' or n == '6' or n == '9':
    print('YES')
else:
    print('NO')