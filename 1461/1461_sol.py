import heapq 
N, M = map(int, input().split())
book = list(map(int, input().split()))

R = []
L = []
for i in book:
    if i < 0:
        L.append(abs(i))
    elif i > 0:
        R.append(i)

R.sort(reverse=True)        
L.sort(reverse=True)   
dis = []

for j in range(len(R)//M):
    dis.append(R[j*M])
if len(R)%M>0:
    dis.append7 (R[(len(R)//M)*M])

for k in range(len(L)//M):
    dis.append(L[k*M])
if len(L)%M>0:
    dis.append(L[(len(L)//M)*M])

dis.sort()

result = dis.pop()
result += 2*sum(dis)

print(result)