"""
f(0)=0
f(1)=1
"""

n = int(input())

def f(n):
    if n==0:
        return 0
    if n==1:
        return 1
    else:
        return f(n-1) + f(n-2)

print(f(n))