# 문제 URL : https://www.acmicpc.net/problem/14381
import sys
input = sys.stdin.readline

T = int(input())
ansArr = []

# 각 테스트 케이스 처리
for i in range(1, T+1):
    n = int(input())
    
    # n이 0일 경우 "INSOMNIA"를 출력
    # (0을 곱하면 아무리 곱해도 새로운 숫자가 나오지 않기 때문)
    if n == 0:
        ansArr.append('Case #' + str(i) + ': INSOMNIA')
        continue

    # num 배열은 0부터 9까지의 숫자가 등장했는지 여부를 기록하는 리스트
    num = [0] * 10
    x = n  # x는 n의 배수를 저장할 변수

    # num 리스트가 1로 가득 차면(모든 숫자를 확인했으면) 반복 종료
    while True:
        s = str(x)              # x를 문자열로 변환하여 자릿수를 하나씩 확인
        for j in range(len(s)): # 각 자릿수 숫자를 확인
            num[int(s[j])] = 1  # 해당 자릿수의 숫자가 등장했음을 기록
        if sum(num) == 10:      # 모든 숫자가 한 번 이상 등장했는지 확인
            break  
        x += n                  # 아직 모든 숫자가 등장하지 않았으면 n을 더하여 다음 배수로 진행

    # 결과를 리스트에 추가
    ansArr.append('Case #' + str(i) + ': ' + str(x))

# 모든 테스트 케이스에 대한 결과 출력
for ans in ansArr:
    print(ans)