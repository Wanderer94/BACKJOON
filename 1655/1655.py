# 정수 횟수 /2 한 다음 카운트 변화하기
#dp 사용해서 문제 풀기

N = int(input())
n_list = []
c_list = [0] * N
for i in range(N):
    n_list.append(int(input()))
    n_list.sort()
    print(n_list[i/2])