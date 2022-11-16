first=input("Enter the Number")
print("You entered <"+first+">")
print("How many fibonacci numbers you want to print")
second=input("Enter the Number")
print("Printing "+second+" fibonacci numbers after "+first)
d=0                                         #first element of series
s=1
if int(first)<=0:
    print("The requested series is",f)
else:
    if(int(first)==1):
        print(s,end=" ")
        count=1;
    elif (int(first)==0):
        print(s,end=" ")
        count=1;
    else:
        count=0
    for x in range(0,100):
        next=d+s
        if(int(first)<next):
            print(next,end=" ")
            count=count+1
        d=s
        s=next
        if(count==int(second)):
            break;