from collections import deque
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
A = deque(list(map(int, input().split()))) # 내구도
robots = deque([0] * N) # 로봇 위치(앞쪽 N칸만)

step = 0

while True:
    step += 1

    # 1. 벨트 + 로봇 회전
    A.rotate(1) # 벨트 회전
    robots.rotate(1) # 벨트가 회전함에 따라 로봇도 같이 회전
    robots[-1] = 0 # 내리는 위치에서 로봇 제거

    # 2. 로봇 이동(앞 칸이 비어있으면 스스로 이동)
    for i in range(N-2, -1, -1): # 뒤에서부터
        if robots[i] == 1 and robots[i+1] == 0 and A[i+1] > 0:
            robots[i] = 0
            robots[i+1] = 1
            A[i+1] -= 1

    robots[-1] = 0 # 내리는 위치에서 로봇 제거
        
    # 3. 올리는 칸에 로봇 올리기
    if A[0] > 0 and robots[0] == 0:
        robots[0] = 1
        A[0] -= 1

    # 4. 내구도 0인 칸의 개수 세기
    if A.count(0) >= K:
        break

print(step)
        