
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
bmi=weight/height**2
print("\n your bmi is:", bmi)
if(bmi<=18.5):
  print("\n So, you are underweight")
elif(bmi>18.5 and bmi<=25):
  print("\n So, you are normalweight")
elif(bmi>25 and bmi<=30):
  print("\n So, you are overweight")
elif(bmi>30 and bmi<=35):
  print("\n So, you are obese")
else:
 print("\n So, you are clinically obeset")
