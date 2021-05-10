def solution(brown, yellow):
#   가로세로의 합을 기준으로 임의의 가로세로를 구한다 : (가로+세로)*2 = brown + 4
    side1 = 2
    side2 = brown//2+2 -side1

    while side1 < side2:
        #   가로-2 * 세로-2 = yellow
        if(side1-2)*(brown//2 -side1) == yellow:
            return [brown//2+2 -side1,side1]
        side1 += 1