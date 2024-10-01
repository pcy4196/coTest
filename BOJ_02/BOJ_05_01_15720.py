# 문제 URL : https://www.acmicpc.net/problem/15720
import sys
input = sys.stdin.readline

B, C, D = map(int, input().split())

mNum = min(B, C, D)
arr1 = sorted(list(map(int, input().split())), key=lambda x : -x)
arr2 = sorted(list(map(int, input().split())), key=lambda x : -x)
arr3 = sorted(list(map(int, input().split())), key=lambda x : -x)

ans = sum(arr1) + sum(arr2) + sum(arr3)

print(ans)

for i in range(mNum):
    ans -= int((arr1[i] + arr2[i] + arr3[i]) * 0.1)

print(ans)
