def rhombus(n):
    a=''
    b=''
    for i in range(1,n+1):
        a+=(int(n-i)*" "+i*"*"+int(i-1)*"*"+int(n-i)*" ")+"\n"
        b+=(i*" "+int(n-i)*"*"+int(n-i-1)*"*"+i*" ")+"\n"
    return a+b

    
n=int(input())
print(rhombus(n))