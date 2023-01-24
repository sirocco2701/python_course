def kh_p(n):
    l=[]
    for i in range(n):
        l.append([0]*(i+2))
        l[i][0] = 1
        for j in range(1,i+1):
            l[i][j] = l[i-1][j-1] + l[i-1][j]
    return l


n=int(input())
print(kh_p(n))

