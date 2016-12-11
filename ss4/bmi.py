height = int(input("chieu cao "))
height = height / 100
weight = int(input("can nang "))

bmi1 = weight / (height**2)
bmi = round(bmi1,2)
print("bmi cua ban = ",bmi)


if bmi < 16:
    print("severely underweight")
elif 16 <= bmi < 18.5:
    print("underweight")
elif 18.5 <= bmi < 25:
    print("normal")
elif 25 <= bmi < 30:
    print("overweight")
elif bmi > 30:
    print("obese")
    
    
