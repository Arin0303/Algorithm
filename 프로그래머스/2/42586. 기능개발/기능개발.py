import math

def solution(progresses, speeds):
    answer = []
    days = [] # 작업 일 수 
    
    for i in range(len(progresses)):
        d = math.ceil((100 - progresses[i])/speeds[i])
        days.append(d)
    
    count = 0
    max_day = days[0]
    
    for day in days:
        if day <= max_day:
            # 묻어가기
            count += 1
        else:
            answer.append(count)
            max_day = day
            count = 1 # 현재 day추가
            
    answer.append(count) # 마지막 배포
    return answer