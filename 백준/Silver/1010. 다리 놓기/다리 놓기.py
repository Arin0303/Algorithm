import math

t = int(input())
cases = []
for _ in range(t):
    n, m = map(int, input().split())
    cases.append((n,m)) # 튜플로 리스트에 추가

for n, m in cases:
    print(math.comb(m,n))
