# [백준] https://www.acmicpc.net/problem/3273 두 수의 합
# 투포인터 알고리즘 기초

import sys

sys.stdin = open('3273.txt')

N = int(input())
arr = list(map(int,input().split()))
x = int(input())

arr.sort()
start = 0
end = N-1
cnt = 0


while True:
    if x > arr[end]:
        break
    else:
        end -= 1

while start < end:
    if arr[start]+arr[end] > x:
        end -= 1
    elif arr[start]+arr[end] == x:
        start += 1
        end -= 1
        cnt += 1
    else:
        # start+end < x:
        start += 1
print(cnt)