"""
1-2-3 
1-5-2

pair: [(1,2),(2,3),(1 5),(5,2),(5,6),(4,7)]
pair(1,2) -> graph[1]=2 graph[2]=1: 1->2 연결, 2->1연결

"""

cmp = int(input())
pair_num = int(input())
pair = []

for _ in range(pair_num):
    i,j = map(int, input().split())
    pair.append((i,j)) # 각 쌍을 튜플로 리스트에 추가


graph = []
for _ in range(cmp+1):
    graph.append([]) # 각 노드의 연결 정보를 빈 리스트로 생성(1번~cmp+1번)
                        # graph[1]=[2,5]: 1번 노드의 인접 노드 = 2,5번

for i, j in pair:
    graph[i].append(j)
    graph[j].append(i)

visited = [False] * (cmp+1) # 노드 방문 기록

def dfs(n):
    visited[n] = True
    for next_n in graph[n]:
        if not visited[next_n]:
            dfs(next_n)

dfs(1)

print(sum(visited)-1) # 방문한 노드 개수 (1제외)

