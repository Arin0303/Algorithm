"""
케이스 수 t
가로길이m, 세로길이n, 배추 개수k
위치 x,y
"""

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def dfs(x, y):
    visited[y][x] = True

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < m and 0 <= ny < n:
            if graph[ny][nx] == 1 and not visited[ny][nx]:
                dfs(nx, ny)



t = int(input())

for i in range(t):

    m, n, k = map(int, input().split())

    graph = [[0] * m for _ in range(n)]
    visited = [[False] * m for _ in range(n)]

    for _ in range(k):
        x, y = map(int, input().split())
        graph[y][x] = 1

    count = 0

    for y in range(n):
        for x in range(m):
            if graph[y][x] == 1 and not visited[y][x]:
                dfs(x, y)
                count += 1
    print(count)
    
