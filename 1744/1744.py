N = int(input())
arr = []
for i in range(N):
    arr.append(int(input()))

for i in range(N/2):
    for j in range(i):
        arr[j-1] * arr[j]