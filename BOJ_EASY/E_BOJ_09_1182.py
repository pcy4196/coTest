# 문제 URL : https://www.acmicpc.net/problem/1182
import sys
input = sys.stdin.readline

N, S = map(int, input().split())
num = list(map(int, input().split()))
ans = 0

def DFS(lvl, sum):
    global ans
    
    if lvl >= N:
        if sum == S:
            ans += 1
        return
    
    DFS(lvl+1, sum+num[lvl])
    DFS(lvl+1, sum)

DFS(0, 0)
if S == 0:
    ans -= 1
print(ans)