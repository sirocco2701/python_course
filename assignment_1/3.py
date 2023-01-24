firstname = input()
lastname = input()
a,b,c=map(float,input().split())

ave = (a + b + c)/3

if ave >= 17:
    result = "Great"
elif ave >= 12:
    result = "Normal" 
else:
    result = "Fail" 

print(firstname, lastname," gpa is "+ result )