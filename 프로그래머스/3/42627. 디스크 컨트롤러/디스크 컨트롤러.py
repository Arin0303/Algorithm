"""
작업의 소요시간이 짧은 것, 작업의 요청 시각이 빠른 것, 작업의 번호가 작은 것 순
요청 대기 큐에 저장
작업 꺼내기
작업 시작

반환시간(종료 시각 - 요청 시각) 평균 반환
"""

import heapq


def solution(jobs): # [요청 시각, 소요 시간]
    # 요청 시각 기준 정렬
    jobs.sort()
    
    curr_time = 0           # 현재 시간
    total = 0               # 총 반환시간
    idx = 0                 # jobs 인덱스
    complete_count = 0      # 처리 완료 개수
    heap = []               # 대기 큐
    
    while complete_count < len(jobs): # 모든 작업 끝날 때까지
        # 현재 시간까지 요청된 작업 모두 힙에 저장
        while idx < len(jobs) and jobs[idx][0] <= curr_time:
            request, duration = jobs[idx] 
            heapq.heappush(heap, (duration, request)) # 튜플 형태로 heap에 저장(1순위: 소요시간, 2순위: 요청 시각)
                                                      # 작업 번호는 고려x -> 소요시간, 요청시각 같으면 평균 반환시간 동일
            idx += 1 # 다음 작업 번호
        
        # 힙에서 꺼내서 작업 실행
        if heap: 
            duration, request = heapq.heappop(heap)
            curr_time += duration
            total += curr_time - request # 반환 시간 = 종료 시각 - 요청 시각
            complete_count += 1
        else: # 처리할 작업이 아직 안들어왔으면 현재 시간을 다음 요청 시각으로 점프
            curr_time = jobs[idx][0] # 그 다음 작업 번호의 요청 시각
             
    return total // len(jobs)