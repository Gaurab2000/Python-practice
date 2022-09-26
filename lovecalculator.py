
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

n1=name1.lower()
n2=name2.lower()
name=n1+n2
t=name.count("t")
r=name.count("r")
u=name.count("u")
e=name.count("e")
l=name.count("l")
o=name.count("o")
v=name.count("v")
e=name.count("e")
sum_1=t+r+u+e
sum_2=l+o+v+e
sum_1=str(sum_1)
sum_2=str(sum_2)
sum_1 += sum_2
integer_sum=int(sum_1)
print(f"the love percentage is : {sum_1}")
if(integer_sum<10 or integer_sum>90):
  print(f"your score is {sum_1},you go together like coke and mentos")
elif(integer_sum>40 and integer_sum<50):
 print(f"your score is{sum_1}, you are alright together ")
else:
  print(f"your score is {sum_1}")
