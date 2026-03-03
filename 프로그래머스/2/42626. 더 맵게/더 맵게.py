"""
섞은 음식의 스코빌 지수 = 
가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)
"""
import heapq # 최소 힙 구현

def solution(scoville, K):
    count = 0
    heapq.heapify(scoville) # 기존 리스트를 힙으로 구현
    while(len(scoville) > 1 and scoville[0] < K): # 최솟값
        min = heapq.heappop(scoville)
        min2 = heapq.heappop(scoville)
        new_min = min + min2 * 2
        heapq.heappush(scoville, new_min)
        count += 1
        
    if scoville[0] >= K:
        return count
    else:
        return -1
        
    return count