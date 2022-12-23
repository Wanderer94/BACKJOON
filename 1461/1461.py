import heapq 
N, M = map(int, input().split())
book = list(map(int, input().split()))
sum = 0
book.sort()
for j in book:
    for i in range(M):
        if i == 0:
            a = book.pop(0)
            a = abs(a)
            sum = sum + a*2
        else:
            b = book.pop(0)
print(sum)