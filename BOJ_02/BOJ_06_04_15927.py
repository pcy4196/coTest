# 문제 URL : https://www.acmicpc.net/problem/15927
import sys
input = sys.stdin.readline

# 문자열을 입력받고 양 끝의 공백 문자를 제거합니다.
str = input().rstrip()

# 문자열의 모든 문자가 동일한지 확인하기 위한 변수입니다. 
same = True
for s in str:
    # 문자열의 모든 문자가 같지 않다면 same을 False로 설정하고 반복문을 종료합니다.
    if s != str[0]:
        same = False
        break

# 문자열의 모든 문자가 동일한 경우 팰린드롬 판별이 불필요하므로 -1을 출력합니다.
if same:
    print(-1)
# 문자열이 팰린드롬이 아닌 경우(거꾸로 해도 같은 문자열이 아닌 경우) 문자열 길이를 출력합니다.
elif str != str[::-1]:
    print(len(str))
# 문자열이 팰린드롬인 경우, 최대 길이의 팰린드롬이므로 길이 -1을 출력합니다.
else:
    print(len(str) - 1)