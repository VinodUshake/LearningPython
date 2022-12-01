first=input("Enter the Start_Num")
print("You entered <"+first+">")
print("How many fibonacci numbers you want to print")
second=input("Enter the Number")

def fib(n):
    a = 0
    b = 1
    if n == 1:
        print(a)
    else:
      print(a)
      print(b)
    for i in range(2,n):
        c = a + b
        a = b
        b = c # swap numbers
        print(c)
fib(10)

#
#else:

#else:
#    print(a)
#    print(b)

#for i in range(2.n):
#    c = a + b
#    a = b
#    b = c
#    print(c)
