# 문제 URL : https://www.acmicpc.net/problem/2941
import sys
input = sys.stdin.readline

# 입력 문자열을 읽고, 오른쪽 끝의 공백 문자를 제거합니다.
S = input().rstrip()

# 크로아티아 알파벳의 개수를 세기 위한 변수를 초기화합니다.
ans = 0

# 문자열 S의 각 문자를 순회합니다.
for i in range(len(S)):
    # 현재 문자가 '-' 또는 '='인 경우 (이 문자는 크로아티아 알파벳의 일부일 수 있음)
    if S[i] in ['-', '=']:
        # 현재 문자 이전의 문자를 확인하기 위해 인덱스 j를 설정합니다.
        j = i - 1
        
        # 만약 이전 문자가 'z'라면, 'dz='를 검사해야 합니다.
        if S[j] == 'z':
            # 'dz=' 패턴을 확인하기 위해 더 앞의 문자가 'd'인지 확인합니다.
            if S[j-1] == 'd':
                # 'dz='는 하나의 크로아티아 알파벳이므로, 세어질 문자 개수를 2개 줄입니다.
                ans -= 2  
            else:
                # 'z='는 하나의 크로아티아 알파벳이므로, 세어질 문자 개수를 1개 줄입니다.
                ans -= 1  
        else:
            ans -= 1  # '-' 또는 '='가 단독으로 나타나는 경우, 세어질 문자 개수를 1개 줄입니다.
    # 'j' 문자가 나올 경우
    elif S[i] in ['j']:
        j = i - 1  # 'j' 이전의 문자를 확인합니다.
        # 만약 이전 문자가 'l' 또는 'n'인 경우, 'lj' 또는 'nj' 패턴을 확인합니다.
        if S[j] in ['l', 'n']:
            ans -= 1  # 'lj' 또는 'nj'는 하나의 크로아티아 알파벳이므로, 세어질 문자 개수를 1개 줄입니다.
    
    # 모든 경우에 대해, 현재 문자를 하나의 크로아티아 알파벳으로 세어줍니다.
    ans += 1

# 최종적으로 크로아티아 알파벳의 개수를 출력합니다.
print(ans)