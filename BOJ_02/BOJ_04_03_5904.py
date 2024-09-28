# 문제 URL : https://www.acmicpc.net/problem/5904
import sys
input = sys.stdin.readline

N = int(input())

# N이 1이면 'm', 2 이상 3 이하이면 'o'
if N <= 3:
    if N == 1:
        print('m')
    else:
        print('o')
    exit()

# lnth 배열은 Moo 수열의 각 단계의 길이를 저장
# 첫 번째 Moo 수열의 길이는 3 (기본값: "moo")
lnth = [3]
i = 0

# Moo 수열의 길이를 단계별로 구하는 과정
# Moo(k) = Moo(k-1) + (k+3의 길이) + Moo(k-1)
# 현재 길이가 N보다 클 때까지 계산
while True:
    nxt = (lnth[i] * 2) + (i + 4)   # 다음 단계의 Moo 수열 길이
    lnth.append(nxt)                # 수열 길이를 리스트에 추가
    i += 1
    if nxt > N:  # 현재 계산된 수열 길이가 N보다 크면 반복문 종료
        break

# 큰 수열에서 작은 수열로 점점 줄여가며 N의 위치를 찾는 과정
while True:
    i -= 1  # 단계 감소 (Moo 수열의 이전 단계로 이동)
    # N이 앞의 Moo 수열 + 가운데 부분보다 큰 경우
    if N > lnth[i] + (i + 4):
        N = N - (lnth[i] + (i + 4))  # N에서 앞의 Moo 수열 + 가운데 길이만큼 빼줌
        if N <= 3:  # N이 3보다 작거나 같으면 결과 결정
            break
    # N이 앞의 Moo 수열보다 크고, 가운데 부분에 속하는 경우
    elif N > lnth[i]:
        N = N - lnth[i]  # N에서 앞의 Moo 수열 길이만큼 빼줌
        break

# N이 1이면 'm', 그렇지 않으면 'o'
# 'm'은 가운데 부분의 첫 번째, 나머지 'o'는 두 번째 이후
if N == 1:
    print('m')
else:
    print('o')