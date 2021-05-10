from itertools import permutations

def checkSosu(num):
    if num < 2:
        return False
    for n in range(2,round(num/2)+1):
        if num%n == 0:
            return False
    else:
        return True
        
def solution(numbers):
    numbers = list(numbers)
    length = len(numbers)
    cand = set()
    cnt = 0 
    for l in range(1,length+1):
        for i in permutations(numbers, l):
            cand.add(int(''.join(i)))
    for c in cand:
        if checkSosu(c):
            cnt += 1
    return cnt

print(solution('17'))