def cubic(a,b,c,d):
    u = [1] 
    u.append(complex(-.5,3**(1/2)/2))
    u.append(complex(-.5,-1*3**(1/2)/2))

    delta = 18*a*b*c*d - 4*b**3*d + b**2*c**2 - 4*a*c**3 - 27*a**2*d**2
    delta0 = b**2 - 3*a*c
    delta1 = 2*b**3 - 9*a*b*c + 27*a**2*d
    C = delta1 + (delta1**2 - 4*delta0**3)**(1/2)
    C = (C/2)**(1/3)
    l = []
    for i in range(3):
        x = b + u[i]*C + delta0/(u[i]*C)
        l.append(x/(-3*a))

    return l

while True:
    a ,b,c,d= map(float,input().split())
    if a == float(0):
        print("a can not be 0")
    else:
        break
    
print(cubic(a,b,c,d))