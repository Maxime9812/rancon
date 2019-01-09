f = open("C:/Users/Maxime/Desktop/mdr/test.txt", "r")
test = str(f.read())
list = [bin(ord(element)) for element in test]
test2 = ''.join(list)
f = open("C:/Users/Maxime/Desktop/mdr/test.txt", "w+")
f.write(test2)
f.close()
