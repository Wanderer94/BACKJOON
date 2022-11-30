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
