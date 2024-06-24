# 문제 URL : https://www.acmicpc.net/problem/19942
import sys
input = sys.stdin.readline

# 입력 처리
N = int(input())  # 재료의 개수
p, f, s, v = map(int, input().split())  # 최소 필요 영양소 (단백질, 지방, 탄수화물, 비타민)
igd = [list(map(int, input().split())) for _ in range(N)]  # 각 재료의 영양소와 가격 정보

# 초기값 설정
vol = sys.maxsize   # 최소 비용을 저장할 변수, 초기값은 매우 큰 값으로 설정
ansIgd = []         # 최소 비용을 만족하는 재료들의 인덱스를 저장할 리스트
locIgd = []         # 현재 재귀 호출에서 선택된 재료들의 인덱스를 저장할 리스트

# 재귀 함수 정의
def rec(idx, mp, mf, ms, mv, mVol):
    global vol
    global ansIgd
    global locIgd

    # 현재까지의 영양소와 비용이 최소 조건을 만족하고 비용이 최소일 경우 갱신
    if mp >= p and mf >= f and ms >= s and mv >= v and vol > mVol:
        vol = mVol
        ansIgd = locIgd.copy()  # 현재 선택된 재료들로 갱신
    
    # 모든 재료를 다 확인한 경우 재귀 종료
    if idx == N:
        return

    # 현재 재료를 선택하는 경우
    locIgd.append(idx+1)
    rec(idx+1, mp + igd[idx][0], mf + igd[idx][1], ms + igd[idx][2], mv + igd[idx][3], mVol + igd[idx][4])
    locIgd.pop()

    # 현재 재료를 선택하지 않는 경우
    rec(idx+1, mp, mf, ms, mv, mVol)

# 재귀 함수 호출 초기값 설정
rec(0, 0, 0, 0, 0, 0)

# 결과 출력
if len(ansIgd) > 0:
    print(vol)
    print(*ansIgd)
else:
    print(-1)