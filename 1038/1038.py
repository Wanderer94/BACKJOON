N = int(input())
i = 0   #기준되는 수
a = 0   #count 변수
while a < N:
    i_str = str(i)    #str 변환시키기
    k = 10  #각 자리수는 절대로 한자리수를 벗어나지 않는다
    check = 1
    for j in i_str:
        j_int = int(j)
        if k <= j_int:  #단 한번이라도 순서를 어기면 해당되지 않는 점을 힌트로 작성
            check = 0
        k = j_int
    if check == 1:
        a = a + 1
    i  = i + 1

    if a == N:
        print("N번쨰수는", i)
