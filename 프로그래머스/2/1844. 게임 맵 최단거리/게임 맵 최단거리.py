from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    
    # 상, 하, 좌, 우
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    
    queue = deque([(0, 0)])
    
    while queue:
        # 현재 위치 꺼내기
        r, c = queue.popleft()
        
        # 도착점에 도달하면 바로 종료(->최단거리)
        if r == n - 1 and c == m - 1:
            return maps[r][c]
        
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            
            # 지도 안 
            if 0 <= nr < n and 0 <= nc < m:
                # 아직 방문 x & 장애물 x
                if maps[nr][nc] == 1:
                    # 방문
                    maps[nr][nc] = maps[r][c] + 1
                    queue.append((nr, nc))
                # 장애물
                elif maps[nr][nc] == 0:
                    pass
                # 이미 방문
                else:
                    pass

    return -1