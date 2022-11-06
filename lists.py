#creating a list
List=[]
print ("blank list: ")
print(List)
#creating a list of numbers
List=[10,20,40]
print ("\n List of numbers:")
print (List)

#creating a list of strings and accessing
List=["gauraV","raM","kathmandu"]
print("\nlistitems:")
print(List)
print(List[0])#accessing element
print(List[1])

#knowing the size of list
print(len(List))
#adding element to the list
List.append(1)
List.append(2)
print("\n List after Addition of three elements:")
print(List)

#inserting at desired position
List.insert (3,'lalitpur')
print (List)

#removing element from the list
List.remove(2)
print(List)
#slicing
List[2:5]
print(List)
