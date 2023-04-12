def solution(users, emoticons):
    #이모티콘 최대 사용자가 생겼을 때의 경우를 만들기
    #해당 경우의 최대 값을 결정하기
    dis = [10,20,30,40]
    plus_user = []
    emoticon_sum = []
    emoticon_case = []
    for i in users:
        e_pay = 0
        plus_u = 0
        for j in emoticons:
            for k in dis:
                if i[0] <= k:
                    e_pay =+ j * (100-k) / 100
        if e_pay >= i[1]:
            plus_u = 1
            e_pay = 0
        plus_user.append(plus_u)
        emoticon
            
    
    
    
    for i in emoticons:
        p_user = 0
        for j in users:
            for k in dis:
                if j[0] <= i:
                    sum_e =+ i * (100- k) / 100
                
            sum_e = 0
            if j[0] <= i:
                sum_e = sum(emoticons) * (100 - i) / 100
                print(sum_e)
                if sum_e >= j[1]:
                    sum_e = 0
                    p_user =+ 1
            emoticon_sum.append(sum_e)
            plus_user.append(p_user)
        sum_e = sum(emoticon_sum)
        emoticon_case.append([p_user, sum_e])
    e_max = plus_user.index(max(plus_user))
    print(emoticon_case)
    answer = [max(emoticon_case)]
    return answer