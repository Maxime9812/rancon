import os

TGREEN = '\033[32m'  # Green Text
TRED = '\033[31m'  # Red Text
ENDC = '\033[m'  # reset to the defaults

try:
    os.mkdir("/Users/" + os.getlogin() + "/Desktop/dossier")  # create folder 'dossier' in user desktop
    print(TGREEN + 'folder create succesfull', ENDC)
except:
    print(TRED + 'repertory already exist', ENDC)
    pass

if os.path.exists(
        "/Users/" + os.getlogin() + "/Desktop/dossier/important.txt"):  # verification of the path  file 'important.txt'
    print(TRED + 'important.txt already exist', ENDC)
    pass
else:
    f = open("/Users/" + os.getlogin() + "/Desktop/dossier/important.txt", "w+")  # open important.txt
    [f.write("Les h4ck3r en force ") for i in range(10000)]  # write 10000* 'Les h4ck3r en force
    f.close()  # close test.txt
    print(TGREEN + 'important.txt create succesfull', ENDC)

if os.path.exists(
        "/Users/" + os.getlogin() + "/Desktop/dossier/mdpcoding.txt"):  # verification of the path file 'mdpcoding.txt'
    print(TRED + 'mdpcoding.txt already exist', ENDC)
    pass
else:
    f = open("/Users/" + os.getlogin() + "/Desktop/dossier/mdpcoding.txt", "w+")  # open mdpcoding.txt
    [f.write("Done is better than perfect ") for i in range(10000)]  # write 10000* Done is better than perfect
    f.close()  # close test.txt
    print(TGREEN + 'mdpcoding.txt create succesfull', ENDC)

if os.path.exists(
        "/Users/" + os.getlogin() + "/Desktop/dossier/moinsimportant.txt"):  # verification of the path file 'moinsimportant.txt'
    print(TRED + 'moinsimportant.txt already exist', ENDC)
    pass
else:
    f = open("/Users/" + os.getlogin() + "/Desktop/dossier/moinsimportant.txt", "w+")  # open moinsimportant.txt
    [f.write("Move fast and break things ") for i in range(10000)]  # write 10000* Move fast and break things
    f.close()  # close test.txt
    print(TGREEN + 'moinsimportant.txt create succesfull', ENDC)
