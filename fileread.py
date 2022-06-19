f=open ("gaurab.txt","rt")
#print(f.readline())

#print(f.readline())
#print(f.readline())  it reads line by line
print(f.readlines())#it reads all line by using \n
#content= f.read()
#for line in f:
 #   print (line, end="")
#print(content)
#content=f.read(34455)
#print("1",content)


#content= f.read(34455)
#print("2",content)
f.close()
