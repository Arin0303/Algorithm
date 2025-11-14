import sys
input = sys.stdin.readline # 빠른 입력
def fib(n):
    # === dp 배열 초기화 ===
    dp = [0]*(n+1)
    dp[0] = 0
    dp[1] = 1

    for i in range(2, n+1): # i = 2 ~ n
        dp[i] = dp[i-1] + dp[i-2]

    return dp[n]

n = int(input())
print(fib(n))