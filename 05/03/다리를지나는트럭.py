from collections import deque
from operator import itemgetter

def solution(bridge_length, weight, waiting_list):
    
    cur_time = 1
    
    waiting_list.reverse()
    in_truck = waiting_list.pop()
    bridge = deque([(cur_time,in_truck)])
    sum_weight = in_truck
    
    while waiting_list:
        
        cur_time += 1
        
#       다리에서 out될 트럭 out
        out_truck = bridge.popleft()
        if out_truck[0]+bridge_length > cur_time:
            bridge.appendleft(out_truck)
        else:
            sum_weight -= out_truck[1]
            
#       다리에서 in될 트럭 in
        in_truck = waiting_list.pop()
            #  무게합 < 최대중량 && 개수합 < 다리길이면
        if sum_weight+in_truck <= weight and len(bridge) < bridge_length:
            bridge.append((cur_time,in_truck))
            sum_weight += in_truck
        else:
            waiting_list.append(in_truck)
            
        
    last_truck = bridge.pop()
    return last_truck[0] + bridge_length