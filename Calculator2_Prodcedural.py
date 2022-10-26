# simple procedural calculator
def add(x, y):
    Additional = int(x) + int(y)
    print("results ")
    print(Additional)


def sub(x, y):
    Subtraction = int(x) - int(y)
    print("results ")
    print(Subtraction)


def mul(x, y):
    mul = int(x) * int(y)
    print("results ")
    print(multiplication)


def div(x, y):
    div = int(x) / int(y)
    print("results ")
    print(Division)


def expo(x, y):
    expo = int(x) ** int(y)
    print("results")
    print(Exponential)


def reminder(x, y):
    reminder = int(x) % int(y)
    print("results")
    print(reminder)


print("1:Addition", "2:Subtraction", "3: Multiplication", "4:Division", "5:Exponetial", "6:Reminder")

# user operation input
a = int(input("enter the operation"))

# Taking numbers for calculation
x = input("Input the Number")
y = input("Input the Second Number")

if a == 1:
    add(x, y)
elif a == 2:
    sub(x, y)
elif a == 3:
    mul(x, y)
elif a == 4:
    div(x, y)
elif a == 5:
    expo(x, y)
elif a == 6:
    reminder(x, y)
else:
    print("Wrong input operation")




