# 문제 URL : https://www.acmicpc.net/problem/1759
import sys
input = sys.stdin.readline

# L: 암호의 길이, C: 사용할 수 있는 알파벳의 개수
L, C = map(int, input().split())

# zipArr: 사용할 수 있는 알파벳 리스트
zipArr = list(input().split())

# 알파벳을 사전순으로 정렬
zipArr.sort(key=lambda x: x)

# 재귀함수를 이용해 가능한 암호를 생성하는 함수
def rec(start, level, code):
    # base case: 암호의 길이가 L에 도달했을 때
    if level >= L:
        cnt1 = 0    # 모음의 개수를 세기 위한 변수
        cnt2 = 0    # 자음의 개수를 세기 위한 변수
        
        # 생성된 암호에서 모음과 자음의 개수를 센다
        for i in range(L):
            if code[i] in ['a', 'e', 'i', 'o', 'u']:
                cnt1 += 1
            else:
                cnt2 += 1
        
        # 모음이 최소 1개, 자음이 최소 2개 있는 경우에만 암호 출력
        if cnt1 >= 1 and cnt2 >= 2:
            print(code)
        return
    
    # start부터 C까지 반복하면서 가능한 알파벳 조합을 찾음
    for i in range(start, C):
        # 재귀 호출로 다음 레벨의 알파벳을 추가하며 암호 생성
        rec(i + 1, level + 1, code + zipArr[i])

# 초기 호출: start=0, level=0, code=''로 시작
rec(0, 0, '')
