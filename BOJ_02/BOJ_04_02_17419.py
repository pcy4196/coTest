# 문제 URL : https://www.acmicpc.net/problem/17419
import sys
input = sys.stdin.readline

'''
K = K-(K&((~K)+1))

[1]
'10110'
~K
01001
(~K)+1
01010
K&((~K)+1)
00010
K-(K&((~K)+1))
10100

[2]
'10100'
~K
01011
(~K)+1
01100
K&((~K)+1)
00100
K-(K&((~K)+1))
10000

K = K - (K & ((~K) + 1)) 연산은 K에서 가장 마지막에 나타나는 1을 제거하는 역할을 합니다.
이 연산은 1의 개수를 세는 데 유용하며, 한 번 수행할 때마다 K의 마지막 1이 사라집니다.
결과적으로 K에 있는 1의 개수만큼 이 연산을 반복할 수 있습니다.
'''

N = int(input())
s = input().rstrip()
# ans: 이진수에 포함된 '1'의 개수를 저장하는 변수
ans = 0

# 이진수 문자열에서 '1'의 개수를 셈
for i in range(N):
    if s[i] == '1':  # 현재 문자가 '1'이면
        ans += 1  # ans 값을 1 증가

# 결과 출력: 이진수 문자열에서 '1'의 개수 출력
print(ans)