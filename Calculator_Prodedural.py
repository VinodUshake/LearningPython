print("1.Addition")
print("2.Substraction")


choice = input("Enter your choice")
if int(choice) == 1:
    num1 = input("enter a number:")
    num2 = input("enter second number:")
    result =int(num1) + int(num2)
    print(result)
elif int(choice) == 2:
    num1 = input("enter a number:")
    num2 = input("enter second number:")
    result = int(num1) - int(num2)
    print(result)
else:
    print("not valid")

