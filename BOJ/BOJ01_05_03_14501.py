# 문제 URL : https://www.acmicpc.net/problem/14501
import sys
input = sys.stdin.readline

# 입력받는 부분
# 전체 상담 기간 (N일)
N = int(input())
# 각 일자별 상담 기간과 수익
sd = [list(map(int, input().split())) for _ in range(N)]  

ans = -1  # 최대 수익을 저장할 변수, 초기값은 -1로 설정

# 재귀함수 정의
def rec(day, price):
    global ans      # 전역변수 ans를 사용하기 위해 선언
    if day < N:     # 현재 날짜가 전체 기간보다 작을 때
        ans = max(price, ans)  # 현재 수익과 기존 최대 수익을 비교하여 더 큰 값을 ans에 저장
    elif day == N:    # 현재 날짜가 전체 기간과 같을 때
        ans = max(price, ans)  # 현재 수익과 기존 최대 수익을 비교하여 더 큰 값을 ans에 저장
        return      # 함수 종료
    elif day > N:     # 현재 날짜가 전체 기간을 초과할 때
        return      # 함수 종료
    # 현재 상담을 선택하는 경우
    rec(day + sd[day][0], price + sd[day][1])  # 상담을 진행한 후 날짜와 수익을 갱신하여 재귀 호출
    # 현재 상담을 선택하지 않는 경우
    rec(day + 1, price)  # 다음 날로 넘어가서 재귀 호출

rec(0, 0)  # 재귀함수 최초 호출, 첫날부터 시작하며 초기 수익은 0

print(ans)  # 최대 수익 출력