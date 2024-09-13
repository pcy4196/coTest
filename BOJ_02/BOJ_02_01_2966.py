# 문제 URL : https://www.acmicpc.net/problem/2966
import sys
input = sys.stdin.readline

# 각 참가자의 정답 패턴
Adrian = 'ABC'      # Adrian의 반복되는 패턴 (3글자)
Bruno = 'BABC'      # Bruno의 반복되는 패턴 (4글자)
Goran = 'CCAABB'    # Goran의 반복되는 패턴 (6글자)

N = int(input())
s = input().rstrip()

# 각 참가자의 맞춘 문제 개수를 저장할 변수
cnt1 = 0  # Adrian이 맞춘 문제 개수
cnt2 = 0  # Bruno가 맞춘 문제 개수
cnt3 = 0  # Goran이 맞춘 문제 개수

# 각 문제에 대해 정답을 확인
for i in range(N):
    # i번째 문제의 정답을 각 참가자의 패턴과 비교
    if s[i] == Adrian[i % 3]:   # Adrian의 패턴에서 i번째 문제에 해당하는 답
        cnt1 += 1
    if s[i] == Bruno[i % 4]:    # Bruno의 패턴에서 i번째 문제에 해당하는 답
        cnt2 += 1
    if s[i] == Goran[i % 6]:    # Goran의 패턴에서 i번째 문제에 해당하는 답
        cnt3 += 1

# 세 명 중 가장 많이 맞춘 개수를 구함
maxNum = max(cnt1, cnt2, cnt3)

# 가장 많이 맞춘 문제 개수 출력
print(maxNum)

# 가장 많이 맞춘 참가자를 출력
if maxNum == cnt1:
    print('Adrian')     # Adrian이 가장 많이 맞춘 경우
if maxNum == cnt2:
    print('Bruno')      # Bruno가 가장 많이 맞춘 경우
if maxNum == cnt3:
    print('Goran')      # Goran이 가장 많이 맞춘 경우