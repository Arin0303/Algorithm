from collections import deque

def solution(maps):
    n = len(maps) # 행
    m = len(maps[0]) # 열

    # 상하좌우
    dr = [1, -1, 0, 0]
    dc = [0, 0, -1, 1]

    # 시작점, 레버 위치 찾기
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 'S':
                sr, sc = i, j

            elif maps[i][j] == 'L':
                lr, lc = i, j

    def bfs(sr, sc, target):

        visited = [[0 for _ in range(m)] for _ in range(n)]

        queue = deque([(sr, sc)])
        visited[sr][sc] = 1

        while(queue):

            r, c = queue.popleft()

            # 목표 도착
            if maps[r][c] == target:
                return visited[r][c] - 1

            for i in range(4):

                nr = r + dr[i]
                nc = c + dc[i]

                # 맵 안
                if (nr >= 0 and nr < n) and (nc >= 0 and nc < m):

                    # 벽 아니고 방문 안했으면
                    if maps[nr][nc] != 'X' and visited[nr][nc] == 0:

                        visited[nr][nc] = visited[r][c] + 1
                        queue.append((nr, nc))

        return -1

    # 시작 -> 레버
    lever_distance = bfs(sr, sc, 'L')

    if lever_distance == -1:
        return -1

    # 레버 -> 출구
    exit_distance = bfs(lr, lc, 'E')

    if exit_distance == -1:
        return -1

    return lever_distance + exit_distance