T = int(input())
for _ in range(T):
    H,W,N = map(int, input().split())
    if N % H == 0:
        floor = H
        ho = N // H
    else:
        ho = N // H + 1
        floor = N % H
    rst = 100*floor + ho
    print(rst)