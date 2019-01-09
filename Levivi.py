TGREEN = '\033[32m'  # Green Text
TRED = '\033[31m'  # Red Text
ENDC = '\033[m'  # reset to the defaults

f = open("C:/Users/Maxime/Desktop/mdr/test.txt", "r")
test = str(f.read())
list = [bin(ord(element)) for element in test]
test2 = ''.join(list)
f = open("C:/Users/Maxime/Desktop/mdr/test.txt", "w+")
f.write(test2)
f.close()
b = open("C:/Users/Maxime/Desktop/mdr/decodeur.py", "w+")
b.write("import os  \r\nos.mkdir('C:/Users/Maxime/Desktop/mdr/1')")
print(TGREEN +'hacked', ENDC)
