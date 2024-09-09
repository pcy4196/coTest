# 문제 URL : https://www.acmicpc.net/problem/2037
import sys
input = sys.stdin.readline

# 각 문자에 대응되는 숫자와 해당 숫자를 몇 번 눌러야 하는지 저장한 리스트
# 'A' ~ 'Z'까지의 문자는 2 ~ 9번 키에 각각 배치되어 있음
num = [2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 9, 9, 9, 9]
cnt = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 4, 1, 2, 3, 1, 2, 3, 4]

# 입력받는 문자에 따라 p와 w를 받음
# p: 각 버튼을 누를 때 걸리는 시간
# w: 같은 버튼을 연속으로 누를 때의 대기 시간
p, w = map(int, input().split())

# 입력받은 메시지 (공백을 포함)
s = input().rstrip()

ans = 0  # 최종 시간을 저장할 변수

# 입력받은 문자열을 순회하면서 시간 계산
for i in range(len(s)):
    if s[i] == ' ':
        ans += p    # 공백은 한 번 눌러야 하므로 p만큼 시간 소요
        continue

    # 현재 문자를 눌러야 하는 시간을 계산 (cnt와 num을 이용)
    ans += p * cnt[ord(s[i]) - ord('A')]  # cnt 배열에서 누른 횟수에 따른 시간 추가

    # 만약 이전 문자와 현재 문자가 같은 번호에 할당되어 있다면 대기 시간 추가
    if i > 0 and s[i-1] != ' ' \
        and num[ord(s[i]) - ord('A')] == num[ord(s[i-1]) - ord('A')]:
        ans += w  # 같은 번호에 할당된 문자는 w만큼 대기 시간 소요

# 최종 결과 출력
print(ans)