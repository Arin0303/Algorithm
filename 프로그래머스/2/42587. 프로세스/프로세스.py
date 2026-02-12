from collections import deque

def solution(priorities, location):
    queue = deque(priorities)
    out = 0 # 몇번째로 pop 되었는지(1부터)
    
    while True:
        cur = queue.popleft()
        if (any(item > cur for item in queue)):
            queue.append(cur)
            
            if(location == 0):
                location = len(queue) - 1 
            else:
                location -= 1 
        else:
            out += 1
            if location == 0:
                return out
            else:
                location -= 1