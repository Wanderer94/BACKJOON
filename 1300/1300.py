#배열 정렬하기ㅜ ㅠ

N = int(input())
k = int(input())
B = [] 
c = 0
for i in range(1,N+1):
    for j in range(1,N+1):
        B.append(i*j)
B.sort()

print(B[k])
# 메모리 이슈 발생했음 정렬 시간은 문제가 되지 않을듯 문제는 메모리, 규칙성을 찾아서 리스트 크기를 한정하자