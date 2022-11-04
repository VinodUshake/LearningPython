#Create a python program to do specified string indexing operations & github requirements
x=str(input("enter a string value"))
print(x)
print("you entered", x)
if len(x) % 2 ==0:
 #print ("Print Your even string")
 print("first character ", x ,"is...", x[0])
 print("last character  ",x, "is...",x[-1] )
 print("length of the string", x,"is",len(x))
 print("middle index ", len(x)/2)
 print("middle character ", x, "is", x[int(len(x) / 2)])
else:
 print("first character ", x, "is...", x[0])
 print("last character ", x, "is...", x[-1])
 print("length of the string", x, "is", len(x))
 print("middle index ", len(x)//2)
