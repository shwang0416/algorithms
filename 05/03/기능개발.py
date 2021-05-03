import math

def calculateDays(progress, speed):
    return math.ceil((100 - progress) / speed)

def solution(progresses, speeds):
    answer = []
    stock = 0
    maxDate = calculateDays(progresses[0],speeds[0])
    
    for progress, speed in zip(progresses, speeds):
        daysForThis = calculateDays(progress, speed)
        if daysForThis > maxDate: # 출하
            answer.append(stock)
            stock = 1
            maxDate = daysForThis
        else:
            stock += 1
    answer.append(stock)
        
    return answer