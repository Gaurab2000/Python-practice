
def prime_checker(number):
  flag=0
  if(number==0 or number==1):
   flag=1
  for i in range(2,number):
   if number%i==0:
    flag=1
  if flag==0:
    print(f"{number} is  prime")
  else:
    print(f"{number} is not prime ")
n = int(input("Check this number: "))
prime_checker(number=n)



