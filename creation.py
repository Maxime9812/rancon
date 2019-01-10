import os

TGREEN = '\033[32m'  # Green Text
TRED = '\033[31m'  # Red Text
ENDC = '\033[m'  # reset to the defaults
try:
    os.mkdir("/Users/"+os.getlogin()+"/Desktop/mdr")
    print(TGREEN + 'folder create succesfull', ENDC)
except:
    print(TRED + 'repertory already exist', ENDC)
    pass

if os.path.exists("/Users/"+os.getlogin()+"/Desktop/mdr/test.txt"):
    print(TRED + 'file already exist', ENDC)
    pass
else:
    f = open("/Users/"+os.getlogin()+"/Desktop/mdr/test.txt", "w+")
    [f.write("Les h4ck3r en force ") for i in range(10000)]
    f.close()
    print(TGREEN + 'file create succesfull', ENDC)

