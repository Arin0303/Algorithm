import sys
input = sys.stdin.readline

n = int(input())
 # 사용자의 입력값이 cnt의 인덱스값이 된다. 
 # 입력값의 범위가 1~ 10000이므로 cnt의 크기는 10001로 지정(배열은 인덱스 0부터 시작하기 때문에 +1)
cnt = [0] * 10001

for _ in range(n):
    num = int(input()) # 사용자의 입력값을 받을 리스트를 따로 지정하지 않고 바로 cnt 하나로 해결 가능
    cnt[num] += 1

for i in range(len(cnt)):
    if cnt[i] != 0:
        for _ in range(cnt[i]):
            print(i)


