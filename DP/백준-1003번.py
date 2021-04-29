memo = dict()
memo[0] = [1,0]
memo[1] = [0,1]
        
def fib(n):
    if n in memo:
        return memo[n]
    
    else:
        memo[n] = [x+y for x,y in zip(fib(n - 1), fib(n - 2))]
        return memo[n]
        
t = int(input())

for _ in range(t):
    a = int(input())
    print(fib(a)[0], fib(a)[1])
