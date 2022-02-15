#for문 돌려서 count 재귀적으로 구해볼것
n_list = list()
for z in range(0,1):
    n_list.append(int(input()))

for n in n_list:
    num_result = [0,0,0,0,0,0,0,0,0,0]
    for i in range(1,n+1):
        str_i = str(i)
        for tmp in str_i:
            num_result[int(tmp)]+=1
    print(num_result)