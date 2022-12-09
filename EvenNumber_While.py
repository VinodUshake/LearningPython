##Even numbers

Num=(input("Enter a Number"))
print("You Entered <"+Num+">")
Num1=input("How many even numbers you wish to print?")

print("Printing "+Num1+" odd numbers after "+Num)
count=0
i=int(Num)+1
while i<int(Num1*3):
    if(i%2==0):
        print(i)
        count=count+1
    i=i+1;
    if(count>=int(Num1)):
        break;
