length = float(input("Length = "))
weight = float(input("Weight = "))

bmi = weight / (length * length)

if bmi < 18:
    print("Underweight")
elif bmi < 25:
    print("Good")
elif bmi < 30:
    print("Overweight")
elif bmi < 40:
    print("Obese")
else:
    print("Morbidly obese")