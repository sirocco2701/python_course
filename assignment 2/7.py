a=int(input())
def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return (fib (n - 2) + fib (n - 1))
        
for i in range(1,a+1):
    print(fib(i),end=" ")
