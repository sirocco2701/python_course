def chess(m,n):
    if m%2==0:
        if n%2==0:
            return int(m/2)*("#*"*int(n/2)+"\n"+"*#"*int(n/2)+"\n")
        else:
            return int(m/2)*("#*"*int(n/2)+"#"+"\n"+"*#"*int(n/2)+"*"+"\n")
    else:
        if n%2==0:
            return int(m/2)*("#*"*int(n/2)+"\n"+"*#"*int(n/2)+"\n")+("#*"*int(n/2))
        else:
            return int(m/2)*("#*"*int(n/2)+"#"+"\n"+"*#"*int(n/2)+"*"+"\n")+("#*"*int(n/2)+"#")


m,n=map(int,input().split())
print(chess(m,n))