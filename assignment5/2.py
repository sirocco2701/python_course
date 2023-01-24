def mul(m,n):
    l=[[0 for i in range(m)] for j in range(n)]
    for i in range(1,m+1):
        for j in range(1,n+1):
            l[i-1][j-1]=i*j    
    return l


m,n=map(int,input().split())
print(mul(m,n))