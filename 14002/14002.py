N = int(input())
A = list(map(int, input().split()))

n_list = []

for i in range(N):
    c_list = []
    c = A[i]
    c_list.append(c)
    for j in range(i, N):
        if c < A[j]:
            c = A[j]
            c_list.append(A[j])
    if len(c_list) > len(n_list):
        n_list = c_list
    print(n_list)
print(len(n_list))
print(n_list)

