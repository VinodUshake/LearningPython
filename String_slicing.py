#program should accept a string value while runnig
x = input("what is string")
#find out that string after removing frist and last character
y=len(x)

x1=x[2:-1]
print(x1)

# find out the slice of hte string after removing the first characters
x1=x[2:1]
print(x1)

# find out the slice of the string removing the last characters
x3=x[:-2]
print(x1)

#Slice the string in th middle and display both strings
string = "hello world"
print(string[:5])