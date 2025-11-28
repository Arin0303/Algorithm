import sys

input = sys.stdin.readline



n = int(input()) # 근무일(1일~n일)



dp = [0]*(n+1) # i번째 날까지 일했을 때 최대 수익



for i in range(1, n+1):

    t, p = map(int, input().split()) # t일, 수익P

    dp[i] = max(dp[i], dp[i-1]) # 현재 날까지의 최대 수익 vs 전날까지의 최대 수익

    if i+t-1 <= n:

        dp[i+t-1] = max(dp[i+t-1], p + dp[i-1]) # 상담을 마친 날의 최대 수익 vs 그 날의 기존 최대 수익 + 현재 날의 전까지의 최대 수익



print(dp[-1])