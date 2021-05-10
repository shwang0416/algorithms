def solution(n, lost, reserve):

    lost = set(lost)
    reserve = set(reserve)
    dd = lost&reserve
    lost = list(lost - dd)
    reserve = list(reserve - dd)
    
#   무조건 앞에서 빌릴 수 있으면 빌린다.
    lost.sort()
    reserve.sort(reverse=True)
    r = -1
    borrowed = 0
    
    for l in lost: 
        while reserve and r < l-1:
            r = reserve.pop()
        if l-1 <= r <= l+1:
            borrowed += 1
            r = -1
    return n - len(lost) + borrowed