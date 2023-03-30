N = int(input())
count = 0
case = []
for i in range(1000):
    count = i * 5
    for j in range(1667):
        count += j * 3
        if N == count:
            x = i + j
            case.append(x)
        count = i * 5

if case == []:
    print(-1)
else:
    print(min(case))