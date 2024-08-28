# 문제 URL : https://www.acmicpc.net/problem/4673
num = [0] * 10001  # 배열 초기화

# 1부터 10000까지의 모든 숫자에 대해 생성자를 계산
for i in range(1, len(num)):
    s = i           # 현재 숫자 i를 s에 저장
    sNum = str(i)   # 숫자 i를 문자열로 변환하여 각 자리수를 다루기 쉽게 함
    for j in range(len(sNum)):
        s += int(sNum[j])   # 각 자리수의 값을 s에 더함, s는 d(i) 값을 나타냄
    if s < len(num):
        num[s] += 1         # d(i) 결과로 나온 s에 대해 생성자가 있음을 표시

# 1부터 10000까지의 모든 숫자에 대해 셀프 넘버를 판별
for i in range(1, len(num)):
    if num[i] == 0:     # 생성자가 없는 숫자, 즉 셀프 넘버인 경우
        print(i)        # 셀프 넘버 출력