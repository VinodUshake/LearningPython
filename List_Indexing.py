##1. List Indexing - take the same problem done for strings, but this time for a list. List can be either hardcoded in the program itself, like:
##my_list = ['Red', 'green', 'brown', 'yellow', 1, 2, 3, ['a', 'b', 'c']]
##	or accept as an input from command line while the program is running.
print("chosen the index function")
print("index function searches string specified value and returns position of where it was found")

h1 = []
n = int(input("Enter number of values : "))
for i in range(0, n):
    inpt = input()

    h1.append(inpt)

print(h1)
print("your list is " +str(h1))
h2 = h1[0]
h3 = h1[len(h1)-1]
a = (len(h1)) % 2
print("The first value of the list is : " + str(h2))
print("The last alphabet of the list is : " + str(h3))
print("The length of the list is :  " + str(len(h1)))
