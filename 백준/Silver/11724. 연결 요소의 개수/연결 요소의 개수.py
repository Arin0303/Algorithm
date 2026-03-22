"""
정점 n개, 간선 m개
간선(u, v)
연결 요소 개수
"""
import sys

# 시스템 재귀 호출 허용 기본값: 1000
# 노드의 개수가 최대 1000개 이므로 재귀 깊이 제한 범위 늘리기
sys.setrecursionlimit(10**6) 

input = sys.stdin.readline

def dfs(n):
    visited[n] = True
    for next_n in graph[n]:
        if not visited[next_n]:
            dfs(next_n)


n, m = map(int, input().split())

graph = []

for i in range(n+1):
    graph.append([])


for _ in range(m):
    u, v  = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False] * (n+1)

count = 0 # 연결 요소 개수

for i in range(1, n+1):
    if not visited[i]: # 방문하지 않은 노드
        count += 1 # 요소 1 증가
        dfs(i) # dfs 실행

print(count)