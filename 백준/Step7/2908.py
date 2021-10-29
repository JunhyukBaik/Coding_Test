A, B = list(map(str, input().split()))
ra = int(A[2]+A[1]+A[0])
rb = int(B[2]+B[1]+B[0])
if ra >= rb:
    print(ra)
else:
    print(rb)