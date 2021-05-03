# https://www.acmicpc.net/problem/9461 파도반 수열

testcase = int(input())

for i in range(testcase):
    N = int(input())
    arr = [0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9]

    if 1 <= N <= 10:
        print(arr[N])
    else:
        for i in range(11, N+1):
            arr.append(arr[i-2] + arr[i-3])
        print(arr[N])
