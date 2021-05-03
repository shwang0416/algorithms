from collections import deque 
from operator import itemgetter

def solution(priorities, location):
    printList = deque([(i,p) for i,p in enumerate(priorities)])
        
    count = 0
    while printList:
        thisPrint = printList.popleft()
        if printList and thisPrint[1] < max(printList,key=itemgetter(1))[1] :
        # if any(thisPrint[1] < p[1] for p in printList):
            printList.append(thisPrint)
        else:
            count += 1
            if thisPrint[0] == location:
                break

    return count