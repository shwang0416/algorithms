# [백준] https://www.acmicpc.net/problem/1806 부분합
# 투포인터 알고리즘

import sys
sys.stdin = open('1806.txt')

N, S = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()


end = N-1
start = end
cal = 0         # 계산과정값을 저장
cnt = 0         # 몇 개나 계산된건지 저장
cand = 9999        # 계산값이 S일 경우에 답 후보자 저장


def init():
    global cnt
    global cal
    global start
    global end
    end -= 1
    cnt = 0
    cal = 0
    start = end


while 0 < start:

    if arr[start] + cal >= S:
        cand = min(cand,cnt+1)
        init()
    else:
        # arr[end] + cal < S
        cal += arr[start]
        start -= 1
        cnt += 1

print(cand)
