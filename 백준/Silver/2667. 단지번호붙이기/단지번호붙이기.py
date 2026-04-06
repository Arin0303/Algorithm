import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())

"""
house = []
for i in range(n):
    row = list(map(int, input().strip())) 
    house.append(row)
"""

house = [list(map(int, input().strip())) for _ in range(n)]


"""
visited = []
for i in range(n):
    temp_row = []
    for j in range(n):
        temp_row.append(False)
    visited.append(temp_row)
"""

visited = [[False] * n for _ in range(n)]

# 방향 벡터 (상, 하, 좌, 우)
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def dfs(r,c):
    visited[r][c] = True

    global count # 단지 내 집 개수
    count += 1

    for i in range(4):
        # 다음에 이동할 좌표
        nr = r + dr[i]
        nc = c + dc[i]

        # 지도 범위 내에 있다면 (0 ~ N-1)
        if 0 <= nr < n and 0 <= nc < n:
            # 그 곳에 집이 있고, 아직 방문하지 않았다면 
            if house[nr][nc] == 1 and not visited[nr][nc]:
                # 탐색 시작
                dfs(nr, nc)

result_counts = [] # 각 단지 내 집 개수

for i in range(n):
    for j in range(n):
        if house[i][j] == 1 and not visited[i][j]:
            count = 0
            dfs(i,j)
            result_counts.append(count)

result_counts.sort()
print(len(result_counts))
for c in result_counts:
    print(c)