w,h= map(float,input().split()) 

bmi = w/((h/100)**2)

if bmi < 18.5:
    result = "underweight" 
elif 25> bmi >= 18.5:
    result = "Normal Weight"
elif 30>bmi >= 25:
    result = "Overweight"  
elif 40>bmi >= 30:
    result = "Obesity"
else:
    result = "Extreme Obesity"

print(result)