ans = set()

def isPrime(num):
    if num < 2:
        return False
    for n in range(2,round(num/2)+1):
        if num%n == 0:
            return False
    else:
        return True

def makeCombinations(str1, str2):
    if str1 != "":
        if isPrime(int(str1)):
            ans.add(int(str1))
            
    for i in range(len(str2)):
        makeCombinations(str1+str2[i], str2[:i]+str2[i+1:])
        
def solution(numbers):
    makeCombinations('',numbers)
    return len(ans)