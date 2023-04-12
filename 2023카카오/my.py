def solution(today, terms, privacies):
    today = list(map(int,today.split('.')))
    terms_list = list(map(int, terms.split()))
    for i in privacies:
        # . 기준으로 split해서 day값으로 모두 환산
        i_s = i.split(' ')
        date_s = int(i[0].split('.'))
        #year
        y = today[0] - date_s[0]
        #month
        m = today[1] - date_s[1]
        #day
        d = today[2] - date_s[2]
        t_d = y*12*28 + m*28 + d
        
        
        k = terms.index(i[1])
        dd = 28 * terms[k]
        if dd < td:
            x = privacies.index(i) + 1
            answer.append(x)
    answer = []
    return answer