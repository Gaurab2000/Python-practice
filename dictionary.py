#dictionary is keyvalue pair
#blank dictionary
d1={}

d2={"harry":"burger","rohan":"fish","skill":"roti","shubham":{"B":"maggie","l":"roti","D":"chichken"}}
print(d2)
print (d2["rohan"])
print (d2["shubham"])
d2["ankit"]="junk food"
print (d2)
del d2 ["rohan"]
print (d2)
d3=d2.copy()
del d3["harry"]
print(d3)
print(d2)
d3.update({"harry":"fish"})
print (d3)
print(d2.items())