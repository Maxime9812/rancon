import os

TGREEN = '\033[32m'  # Green Text
TRED = '\033[31m'  # Red Text
ENDC = '\033[m'  # reset to the defaults
base64 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
try:
    os.mkdir('C:/Users/Maxime/Desktop/mdr')
    print(TGREEN + 'folder create succesfull', ENDC)
except:
    print(TRED + 'repertory already exist', ENDC)
    pass

if os.path.exists('C:/Users/Maxime/Desktop/mdr/test.txt'):
    print(TRED + 'file already exist', ENDC)
    pass
else:
    f = open("C:/Users/Maxime/Desktop/mdr/test.txt", "w+")
    [f.write("Les hacker en force ") for i in range(10000)]
    f.close()
    print(TGREEN + 'file create succesfull', ENDC)

