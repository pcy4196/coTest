# 문제 URL : https://www.acmicpc.net/problem/1254
import sys
input = sys.stdin.readline

S = input().rstrip()

# 문자열 S의 각 부분 문자열을 순차적으로 확인
for i in range(len(S)):
    p = S[i:]   # S의 i번째 인덱스부터 끝까지의 부분 문자열을 p에 저장
    rP = ''     # p의 역순 문자열을 저장할 변수
    
    # 부분 문자열 p를 역순으로 만들어 rP에 저장
    for j in p:
        rP = j + rP
    
    # 부분 문자열 p가 그 역순인 rP와 같다면 펠린드롬 
    # 아닌 부분의 개수만 추가하여 전체 문자를 펠드롬 처리
    if p == rP:
        print(len(S) + i)
        break