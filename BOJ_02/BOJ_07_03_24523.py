# 문제 URL : https://www.acmicpc.net/problem/24523
import sys
input = sys.stdin.readline

N = int(input())
arr = [0] + list(map(int, input().split()))
aArr = [-1] * (N+1)
stack = []
for i in range(1, N+1):

    while len(stack) > 0 and arr[stack[-1]] != arr[i]:
        aArr[stack[-1]] = i
        stack.pop()

    stack.append(i)

print(*aArr[1:])