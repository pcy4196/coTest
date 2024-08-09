# 문제 URL : https://www.acmicpc.net/problem/1343
import sys
input = sys.stdin.readline

board = list(input().rstrip())

def sol():
    cnt = 0     # 'X'의 개수를 세는 카운터
    ans = ''    # 결과를 저장할 문자열

    for i in range(len(board)):
        if board[i] == 'X':     # 현재 문자가 'X'인 경우
            cnt += 1            # 'X'의 개수를 증가시킴
            if cnt == 4:        # 'X'가 4개가 되면
                ans += 'AAAA'   # 'AAAA'로 변환하여 추가
                cnt = 0         # 카운터를 초기화
        else:                   # 현재 문자가 '.'인 경우
            if cnt == 0:        # 'X'가 없는 경우 (이전 문자가 '.')
                ans += '.'      # 그대로 '.'을 추가
            elif cnt == 1:      # 'X'가 1개일 때는 덮을 수 없으므로 -1 반환
                return -1
            elif cnt == 2:      # 'X'가 2개일 때는 'BB'로 덮을 수 있음
                ans += 'BB.'    # 'BB'를 추가하고 '.'도 추가
                cnt = 0         # 카운터를 초기화
            else:               # 'X'가 3개일 경우 덮을 수 없으므로 -1 반환
                return -1
    
    # 반복문이 끝난 후 남아있는 'X'의 개수를 확인
    if cnt == 0:  # 남은 'X'가 없는 경우
        return ans  # 결과 반환
    elif cnt == 1:  # 'X'가 1개일 때는 덮을 수 없으므로 -1 반환
        return -1
    elif cnt == 2:  # 'X'가 2개일 때는 'BB'로 덮을 수 있음
        ans += 'BB'
        return ans  # 결과 반환
    else:  # 'X'가 3개일 경우 덮을 수 없으므로 -1 반환
        return -1

# 결과 출력
print(sol())
