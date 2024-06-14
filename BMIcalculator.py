weight = float(input("Enter your weight in kilogram : "))

height = float(input("Enter your height in centimeter : "))

BMI = weight/((height/100)**2)
print(BMI)

if(BMI < 16):
    print("You are severely underweight"),BMI

elif (BMI >= 16 and BMI < 18.5):
    print("You are Healthy "),BMI

elif (BMI >= 18.5 and BMI < 30):
    print("You are Overweight "),BMI

elif (BMI > 30):
    print("You are Obese "),BMI