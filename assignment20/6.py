import random
a=["a1","b1","c1","d1"]
b=["a2","b2","c2","d2"]
d=[]
g=[]
for i in range(len(a)):
    ai=a.pop(random.randint(0,len(a)-1))
    bi=b.pop(random.randint(0,len(b)-1))
    print(ai,bi)
    d.append(ai)
    d.append(bi)
    g.append(d)
    d=[]
    
print(g)