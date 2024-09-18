# 문제 URL : https://www.acmicpc.net/problem/1417
import sys
input = sys.stdin.readline

# N : 후보의 수
N = int(input())
x = 0       # 첫 번째 후보인 다솜이의 득표수
arr = []    # 나머지 후보들의 득표수를 저장할 리스트

# 각 후보들의 득표수를 입력받는 과정
for i in range(N):
    if i == 0:
        x = int(input())            # 첫 번째 후보인 다솜이의 득표수를 입력받음
    else:
        arr.append(int(input()))    # 나머지 후보들의 득표수를 리스트에 저장

ans = 0  # 다솜이가 승리하기 위해 필요한 매수의 최소 횟수

# 후보가 2명 이상일 때 처리 (경쟁 후보가 있을 경우)
while N > 1:
    arr.sort()      # 나머지 후보들의 득표수를 오름차순으로 정렬
    mx = arr.pop()  # 가장 많은 득표수를 가진 후보의 득표수를 꺼냄 (최대값)
    
    # 다솜이의 득표수가 가장 많은 후보의 득표수보다 크면 더 이상 매수할 필요가 없음
    if x > mx:
        break
    else:
        ans += 1        # 매수 횟수 증가
        x += 1          # 다솜이의 득표수 증가
        mx -= 1         # 가장 많은 득표수를 가진 후보의 득표수 감소
        arr.append(mx)  # 다시 리스트에 해당 후보의 갱신된 득표수를 추가

# 결과 출력 (다솜이가 승리하기 위해 필요한 최소 매수 횟수)
print(ans)