import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = [[] for _  in range(n+1)]
        for ui, vi, wi in times:
            graph[ui].append((vi,wi))
        

        distance = [float('inf')] * (n+1)  
        distance[k] = 0  
        heap=[(0, k)] # (cost, node)
        
        while(heap):
            current_cost, current_node = heapq.heappop(heap)

            if current_cost < distance[current_node]:
                continue

            for next_node, next_cost in graph[current_node]:
                new_cost = current_cost + next_cost 
                if new_cost < distance[next_node]:
                    distance[next_node] = new_cost
                    heapq.heappush(heap,(new_cost, next_node))

        result = max(distance[1:])
        if result == float('inf'):
            return -1
        return result