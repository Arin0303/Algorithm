def solution(arr):
    answer = []
    lastNum = -1
    for n in arr:
        if n != lastNum:
            answer.append(n)
            lastNum = n
            
    return answer