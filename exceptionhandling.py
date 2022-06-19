print ("enter a number")
num1=input()
print ("enter anothe rnumber ")
num2=input()
try:
    print("the sum of these two numbers are: ",int(num1)+int(num2))
except Exception as e:
    print (e)
print("this line is very important")
