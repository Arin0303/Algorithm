"""
같은 우선순위: 번호 작은 것 우선
모두 방문 -> 종료
정점 N개 간선 M개 시작 번호 V

"""
from collections import deque

n, m, v = map(int, input().split())
pairs = [tuple(map(int, input().split())) for _ in range(m)]
graph = [[] for _ in range(n+1)] # graph[1] ~ graph[n]

for i, j in pairs:
    graph[i].append(j)
    graph[j].append(i)

for i in range(1, n+1):
    graph[i].sort()

visited_dfs = [False] * (n + 1)
def dfs(n):
    visited_dfs[n] = True
    print(n, end=' ')
    for next_n in graph[n]:
        if(visited_dfs[next_n] == False):
            dfs(next_n) 

visited_bfs = [False] * (n + 1)
def bfs(n):
    queue = deque() # 방문 대기열
    queue.append(n)
    visited_bfs[n] = True

    while queue:
        curr = queue.popleft()
        print(curr, end = ' ')
        #visited_bfs[curr] = True
        for next_n in graph[curr]:
            if not visited_bfs[next_n]:
                queue.append(next_n) # 방문 대기열에 추가
                visited_bfs[next_n] = True # 방문 기록 작성
dfs(v)
print()
bfs(v)