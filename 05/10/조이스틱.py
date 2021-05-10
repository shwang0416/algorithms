# 조이스틱 패착:
# 1. 다음 바꿀 위치를 정하는데는 이 다음에 연속된 A가 나와서 왼쪽으로 가는게 오른쪽으로 가기보다 빠른 경우 하나밖에없음
#    : 한 알파벳을 바꾸는데 필요한 조작횟수에 이전 조작위치, 이전 조작했던 알파벳이 영향 주지 않음

# 2. 바꿀 위치를 고정되게해서 for문으로 찾으면 만약에 왼쪽으로 가야할 경우 식이 이상해짐. 
#    현재위치에서 다음에 어디로 가야할 지 미리 계산후 움직이고 while문을 사용해야 함     

def solution(name):
    nameNeed = [min(ord(i)-ord('A'), ord('Z')-ord(i)+1) for i in name]
    curIdx = 0
    answer = 0
    while sum(nameNeed) != 0:
        answer += nameNeed[curIdx]
        nameNeed[curIdx] = 0
        left, right = 1, 1
        if sum(nameNeed) ==0:
            break
        while nameNeed[curIdx-left] == 0:
            left += 1
        while nameNeed[curIdx+right] == 0:
            right += 1
        answer += left if left < right else right
        curIdx += -left if left < right else right
        
    return answer