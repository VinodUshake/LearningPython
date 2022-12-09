##For ODD numbers
Num=(input("Enter a Number"))
print("You Entered <"+Num+">")
Num1=input("How many odd numbers you wish to print?")

print("Printing "+Num1+" odd numbers after "+Num)
count=0
for i in range(int(Num)+1,int(Num1*3)):
    if(i%2==1):
        print(i)
        count=count+1
    if(count>=int(Num1)):
        break;