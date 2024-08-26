# 문제 URL : https://www.acmicpc.net/problem/1316
import sys
input = sys.stdin.readline

N = int(input())
ans = 0
for _ in range(N):
    str = input().rstrip() 
    
    if len(str) == 1:  # 단어의 길이가 1이면 무조건 그룹 단어
        ans += 1
        continue
    
    dic = {}     # 각 문자가 등장했는지 여부를 체크하기 위한 딕셔너리
    chk = True  # 그룹 단어인지 체크하는 변수
    
    for i in range(len(str) - 1):
        if i == 0:          # 첫 번째 문자 처리
            dic[str[i]] = 1  # 첫 문자는 무조건 처음 등장하므로 기록
        
        # 연속된 문자가 달라지는 경우
        if str[i] != str[i+1]:
            # 다음 문자가 이미 등장한 적이 있는지 체크
            if str[i+1] in dic:
                chk = False         # 이미 등장한 문자면 그룹 단어가 아님
                break               # 그룹 단어가 아니므로 더 이상 검사할 필요 없음
            else:
                dic[str[i+1]] = 1   # 처음 등장한 문자면 딕셔너리에 기록
    
    if chk:  # 그룹 단어라면 결과에 추가
        ans += 1

print(ans)  # 그룹 단어의 개수 출력