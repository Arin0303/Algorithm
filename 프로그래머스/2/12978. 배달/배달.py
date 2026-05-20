import heapq

def solution(N, road, K):
    graph = [[] for _ in range(N+1)]
    
    for a,b,cost in road:
        graph[a].append((b, cost))
        graph[b].append((a, cost))
        
    distance = [float('inf')] * (N+1)
    distance[1] = 0
    
    heap = [(0,1)]
    
    while(heap):
        current_cost, current_node = heapq.heappop(heap)
        
        
        if current_cost > distance[current_node]:
            continue
        
        for next_node, next_cost in graph[current_node]:
            new_cost = current_cost + next_cost
            
            if new_cost < distance[next_node]:
                distance[next_node] = new_cost
                heapq.heappush(heap, (new_cost, next_node))
    
    answer = 0
    
    for node in range(1, N+1):
        if distance[node] <= K:
            answer += 1
    return answer
        
    
    