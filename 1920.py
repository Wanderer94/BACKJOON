def binary_search_recursion(target, start, end, data):
    if start > end:
        print("0")
        return None
        

    mid = (start + end) // 2

    if data[mid] == target:
        print("1")
        return mid
        
    elif data[mid] > target:
        end = mid - 1
    else:
        start = mid + 1        

    return binary_search_recursion(target, start, end, data)

N = int(input())
A = list(map(int,input().split()))
A.sort()

M = int(input())
B = list(map(int,input().split()))

for i in B:
    binary_search_recursion(i,0,N-1,A)
