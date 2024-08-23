# 문제 URL : https://www.acmicpc.net/problem/9342
import sys
input = sys.stdin.readline

T = int(input())
ans = []
for _ in range(T):
    str = input().rstrip()  # 문자열 입력받고 줄바꿈 문자 제거
    
    # 문자열의 길이가 3보다 작으면 조건을 만족할 수 없으므로 'Good'을 추가
    if len(str) < 3:
        ans.append('Good')
        continue
    
    # 문자열의 첫 문자가 'A'가 아니고, 'A'부터 'F'가 아닌 경우 'Good'을 추가
    if str[0] != 'A':
        if str[0] not in ['A', 'B', 'C', 'D', 'E', 'F']:
            ans.append('Good')
            continue
        # 첫 문자가 'A'부터 'F'라면 그 문자를 제외하고 계속 검사
        str = str[1:]
    
    # 문자열의 마지막 문자가 'C'가 아니고, 'A'부터 'F'가 아닌 경우 'Good'을 추가
    if str[-1] != 'C':
        if str[-1] not in ['A', 'B', 'C', 'D', 'E', 'F']:
            ans.append('Good')
            continue
        # 마지막 문자가 'A'부터 'F'라면 그 문자를 제외하고 계속 검사
        str = str[:-1]
    
    # 연속된 같은 문자를 하나로 압축하여 zStr에 저장
    zStr = str[0]
    for i in range(1, len(str)):
        if str[i] != str[i-1]:
            zStr += str[i]
    
    # 압축된 문자열이 'AFC'와 같으면 'Infected!' 추가, 아니면 'Good' 추가
    if zStr == 'AFC':
        ans.append('Infected!')
    else:
        ans.append('Good')

# 모든 테스트 케이스의 결과를 출력
for i in range(len(ans)):
    print(ans[i])
