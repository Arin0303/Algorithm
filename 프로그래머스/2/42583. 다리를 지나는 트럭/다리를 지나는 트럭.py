from collections import deque

def solution(bridge_length, weight, truck_weights):
    # 다리에 올라갈 수 있는 트럭 수 bridge_length
    # 다리가 견딜 수 있는 무게 weight
    # 트럭 별 무게 truck_weights
    
    trucks = deque(truck_weights) # 대기 트럭 큐
    bridge = deque([0] * bridge_length) # 다리 큐
    time = 0
    current_weight = 0
    
    while trucks or current_weight > 0: # 대기 트럭이 남아있거나 다리 위에 트럭이 남아있으면 반복
        time += 1
        out_truck = bridge.popleft() # 다리를 지난 버스
        current_weight -= out_truck
        
        if(trucks and current_weight + trucks[0] <= weight):
            in_truck = trucks.popleft() # 다리를 건널 버스
            bridge.append(in_truck) # 다리에 버스 추가
            current_weight += in_truck # 버스 무게 추가
        else:
            bridge.append(0) # 다리에서 pop한 자리 채워주기
    return time
            
            
            
        
