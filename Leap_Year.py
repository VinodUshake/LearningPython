#Checking Leap Year or not
year = input("what is year")
if int(year) % 400 == 0:
   print("it is a leap")
if int(year) % 100 == 0 and int(year) % 400 != 0:
   print("is not a leap year")
if int(year) % 4 == 0 and int(year) % 100 != 0 and int(year) % 400 != 0:
   print("it is a leap year")
else:
   print("not a leap year")


