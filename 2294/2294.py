n, k = map(int, input().split())
n_list= []
for i in range(n):
    n_list.append(int(input()))

dp = [0] * (k+1)
dp[0] = 1
for i in range(n):
    for j in range(n_list[i], k+1):
        dp[j] += dp[j - n_list[i]]

print(dp[k])
