import sys
input = sys.stdin.readline

n = int(input())
list_ans = []
list_ans = list(map(int, input().split()))

m = int(input())
list_find = []
list_find = list(map(int, input().split()))

set_ans = set(list_ans) # 집합으로 변환(중복 제거)


for i in range(m):
    if(list_find[i] in set_ans):
        print(1)
    else:
        print(0)