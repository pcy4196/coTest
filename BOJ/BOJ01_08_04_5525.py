# 문제 URL : https://www.acmicpc.net/problem/5525
import sys
input = sys.stdin.readline

# N: IOI 패턴의 반복 횟수
N = int(input())
# M: 문자열 S의 길이
M = int(input())
# S: 주어진 문자열
S = input()

i = 0          # 현재 문자열 S에서의 인덱스
pCnt = 0       # IOI 패턴의 현재 반복 횟수
ans = 0        # 찾은 패턴의 총 개수

# 문자열의 끝까지 검사
while i < (M-1):
    # 'IOI' 패턴을 찾았을 때
    if S[i] == 'I' and S[i+1] == 'O' and S[i+2] == 'I':
        pCnt += 1        # IOI 패턴의 반복 횟수를 증가
        i += 2           # 패턴이 겹치므로 2칸 전진
        # 패턴이 N번 반복되면 정답 카운트 증가
        if pCnt == N:
            ans += 1
            pCnt -= 1    # 중복된 패턴을 고려하기 위해서 pCnt를 1 감소
    else:
        pCnt = 0         # 패턴이 끊기면 pCnt를 초기화
        i += 1           # 1칸 전진

# 최종적으로 찾은 패턴의 개수 출력
print(ans)