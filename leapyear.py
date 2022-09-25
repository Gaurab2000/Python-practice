year = int(input("Which year do you want to check? "))
div_by_4=year%4
div_by_100=year%100
div_by_400=year%400
if(div_by_4==0):
 if(div_by_100!=0):
   print("\nThis is leap year")
 else:
   if(div_by_400==0):
     print("\n This is leap year")
   else:
     print("\n This is not leap year")
else:
  print("\n This is not leap year")
  
