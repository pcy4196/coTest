# 문제 URL : https://www.acmicpc.net/problem/2596
import sys
input = sys.stdin.readline

# 각 알파벳에 해당하는 6자리 이진 문자열을 딕셔너리로 정의
sArr = {}
sArr['A'] = '000000'
sArr['B'] = '001111'
sArr['C'] = '010011'
sArr['D'] = '011100'
sArr['E'] = '100110'
sArr['F'] = '101001'
sArr['G'] = '110101'
sArr['H'] = '111010'

ans = []                # 정답을 저장할 리스트
N = int(input())        # 문자의 개수 입력
S = input().rstrip()    # 입력받은 문자열을 저장, 공백 제거

# N개의 문자에 대해 반복
for i in range(N):
    # 현재 문자의 6자리 이진 문자열을 추출
    s = S[i*6:(i+1)*6]
    
    # 딕셔너리에 있는 문자들과 비교
    for k, v in sArr.items():
        cnt = 0                 # 다른 비트의 개수를 세는 변수
        # 각 문자와 대응하는 6자리 이진 문자열과 비교
        for j in range(6):
            if s[j] != v[j]:    # 한 비트가 다르면 cnt 증가
                cnt += 1
        if cnt <= 1:            # 비트가 1개 이하로 다르면 해당 문자가 맞다고 판단
            ans.append(k)

    # 만약 현재 문자가 어떤 문자와도 1비트 이하로 다르지 않으면 에러 발생
    if len(ans) != (i+1):
        print(i+1)  # 에러 발생 시, 해당 문자의 위치 출력
        sys.exit()  # 프로그램 종료

# 정상적으로 모든 문자를 해독한 경우 결과 출력
for i in range(len(ans)):
    if i != (N-1):  # 마지막 문자 앞까지는 이어서 출력
        print(ans[i], end='')
    else:           # 마지막 문자는 줄을 바꿔서 출력
        print(ans[i])