from collections import deque

def solution(maps):
    dr = [1,-1,0,0]
    dc = [0,0,-1,1]
    
    n = len(maps) # 행의 수
    m = len(maps[0]) # 열의 수
    
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 'S':
                S = [i,j]
            elif maps[i][j] == 'L':
                L = [i,j]
            elif maps[i][j] == 'E':
                E = [i,j]    
                
    def bfs(start, end):
        visited = [[0] * m for _ in range(n)]
        q = deque()
        q.append(start)
        
        while(q):
            r, c = q.popleft() # 현재위치

            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]

                if (nr >= 0 and nr < n) and (nc >= 0 and nc < m):

                    if maps[nr][nc] != 'X' and visited[nr][nc] == 0:
                        visited[nr][nc] = visited[r][c] + 1
                        q.append([nr,nc])
                        
                        if [nr, nc] == end:
                            return visited[nr][nc]

        return -1
                
    result1 = bfs(S, L)
    result2 = bfs(L, E)
    
    if result1 == -1 or result2 == -1:
        return -1
    
    return result1+result2
        