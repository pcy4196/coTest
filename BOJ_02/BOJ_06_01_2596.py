# 문제 URL : https://www.acmicpc.net/problem/2596
import sys
input = sys.stdin.readline

sArr = {}
sArr['A'] = '000000'
sArr['B'] = '001111'
sArr['C'] = '010011'
sArr['D'] = '011100'
sArr['E'] = '100110'
sArr['F'] = '101001'
sArr['G'] = '110101'
sArr['H'] = '111010'

ans = []
N = int(input())
S = input().rstrip()

for i in range(N):
    s = S[i*6:(i+1)*6]
    
    for k, v in sArr.items():
        cnt = 0
        for j in range(6):
            if s[j] != v[j]:
                cnt += 1
        if cnt <= 1:
            ans.append(k)

    if len(ans) != (i+1):
        print(i+1)
        sys.exit()

for i in range(len(ans)):
    if i != (N-1):
        print(ans[i], end='')
    else:
        print(ans[i])
