# 문제 URL : https://www.acmicpc.net/problem/19942
import sys
input = sys.stdin.readline

N = int(input())
p, f, s, v = map(int, input().split())
igd = [list(map(int, input().split())) for _ in range(N)]

# 가격
vol = sys.maxsize
ansIgd = []
locIgd = []

def rec(idx, mp, mf, ms, mv, mVol):
    global vol
    global ansIgd
    global locIgd
    if mp >= p and mf >= f and ms >= s and mv >= v and vol > mVol:
        vol = mVol
        ansIgd = locIgd.copy()
    if idx == N:
        return
    locIgd.append(idx+1)
    rec(idx+1, mp + igd[idx][0], mf+ igd[idx][1], ms + igd[idx][2], mv + igd[idx][3], mVol + igd[idx][4])
    locIgd.pop()
    rec(idx+1, mp, mf, ms, mv, mVol)

rec(0,0,0,0,0,0)

if len(ansIgd) > 0:
    print(vol)
    print(*ansIgd)
else:
    print(-1)