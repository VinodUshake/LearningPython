a = (len(h1)) % 2
print("The Fist Alphabet String" : " + h2)
print("The Fist Alphabet String" : " + h3)
print("The Fist Alphabet String" : " + str(len(h1)))

if a == 1:
    b = int(len(h1)/2)
    print("mid index is" +str(b))
    h4 = h1[b]
    print("The Middle Character is :" + h4)

elif a == 0:
    b = int(len(h1) / 2)
    print("mid index is" +str(b))
    h5 = h1[b - 1]
    h6 = h1[b]
    print("The Middle Character is : " + h5 + " and " + h6)