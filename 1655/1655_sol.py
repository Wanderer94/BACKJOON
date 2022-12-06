import heapq

# 시간 오류 크게 나는것 힙을 2개 써서 문제 해결 가능하다.
N = int(input())
max_h = []
min_h = []

for _ in range(N):
    num = int(input())
    if len(max_h) == len(min_h):
        heapq.heappush(max_h, -num)
    else:
        heapq.heappush(min_h, num)
    
    if len(max_h) >= 1 and len(min_h) >=1 and max_h[0] * -1 > min_h[0]:
        max_value = heapq.heappop(max_h) * -1
        min_value = heapq.heappop(min_h)
        
        heapq.heappush(max_h, min_value * -1)
        heapq.heappush(min_h, max_value)
    print(max_h[0] * -1)
    