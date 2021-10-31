t = int(input())
for i in range(t):
    k = int(input())
    k = k + 1
    n = int(input())
    array = [[0]*n for _ in range(k)]
    for j in range(n):
        array[0][j] = j+1
 
    for w in range(1,k):
        array[w][0] = 1
        rst = 0
        for y in range(n):
            rst += array[w-1][y]
            array[w][y] = rst
    print(array[k-1][n-1])