#create a dictionary and take input from the user and return the meaning of the word from the dictionary

d1={ "oxymoron":"a figure of speech in which apparently contradictory terms appear in conjunction","cricket":"a popular sport in south asia which is played with bat and ball",
     "ball":" a spherical object which is used in different sports for playing purpose","paper":"a sheet made from wood which is used for writing purpose"}
print("enter the word in dictionary to find the meaning  :")
user = input()
if (user=="oxymoron"):
     (print("the meaning of the word is:"))
     (print (d1["oxymoron"]))
elif(user == "cricket"):
    (print("the meaning of the word is:"))
    (print(d1["cricket"]))
elif (user == "ball"):
    (print("the meaning of the word is:"))
    (print(d1[" ball"]))
elif(user == "paper"):
      (print("the meaning of the word is:"))
      (print(d1[" paper"]))
