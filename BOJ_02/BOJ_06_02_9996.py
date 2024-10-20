# 문제 URL : https://www.acmicpc.net/problem/9996
import sys
input = sys.stdin.readline

N = int(input())        # 입력받을 문자열의 개수
p = input().rstrip()    # 패턴 문자열을 입력받고 공백 제거
pf = ''                 # 패턴의 앞부분을 저장할 변수
pb = ''                 # 패턴의 뒷부분을 저장할 변수

# 패턴에서 '*'를 기준으로 앞부분과 뒷부분을 나누기 위한 반복문
for i in range(len(p)):
    if p[i] == '*':     # '*'를 찾으면
        pf = p[:i]      # '*' 앞부분을 pf에 저장
        pb = p[i+1:]    # '*' 뒷부분을 pb에 저장

aArr = []  # 결과를 저장할 배열

# N개의 문자열에 대해 반복
for _ in range(N):
    s = input().rstrip()  # 각 문자열 입력받기
    # 문자열의 길이가 패턴의 앞부분과 뒷부분의 길이 합보다 길거나 같고,
    # 앞부분과 뒷부분이 각각 패턴의 앞부분, 뒷부분과 일치하면
    if len(s) >= len(pf) + len(pb) and s[:len(pf)] == pf and s[-len(pb):] == pb:
        aArr.append('DA')  # 조건이 만족하면 'DA' (맞다) 추가
    else:
        aArr.append('NE')  # 조건이 맞지 않으면 'NE' (아니다) 추가

# 저장된 결과 출력
for ans in aArr:
    print(ans)  # 한 줄씩 결과 출력