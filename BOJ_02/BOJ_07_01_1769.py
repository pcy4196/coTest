# 문제 URL : https://www.acmicpc.net/problem/1769
import sys
input = sys.stdin.readline

N = int(input())
n = str(N)
cnt = 0
while len(n) > 1:
    num = 0
    for i in n:
        num += int(i)
    cnt += 1
    n = str(num)

print(cnt)
if n == '3' or n == '6' or n == '9':
    print('YES')
else:
    print('NO')