def function1(a,b):
    print("hello you are in function 1",a+b)

def function2(a,b):
    """this is a function by gaurba rayamajhi for calculating average of two numbers"""
    average=(a+b)/2
    #print (average)
    return average#for returning in variable
v= function2(5,5)
print (v)
print(function2.__doc__)

