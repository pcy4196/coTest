# 문제 URL : https://www.acmicpc.net/problem/15927
import sys
input = sys.stdin.readline

str = input().rstrip()

same = True
for s in str:
    if s != str[0]:
        same = False
        break

if same:
    print(-1)
elif str != str[::-1]:
    print(len(str))
else:
    print(len(str) - 1)
