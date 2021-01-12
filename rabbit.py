# This is the first version of RABBIT 1.0
#Created by ayoub927

# [+] Modules

import os
import sys
from time import sleep
import colorama
from colorama import Fore, Style

colorama.init(autoreset=True)

# [+] Script prefix

prefix = "@ -> "

# [+] Variables

alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ*/-+0123456789.,;:!?è@àé()[]={}&"

# [+] Functions

def draw():
    print("""
#############################################################
#                                                           #
#           ____      _    ____  ____ ___ _____             #
#          |  _ \    / \  | __ )| __ )_ _|_   _|            #
#          | |_) |  / _ \ |  _ \|  _ \| |  | |              #
#          |  _ <  / ___ \| |_) | |_) | |  | |              #
#          |_| \_\/_/   \_\____/|____/___| |_|              #
#                                                           #
#############################################################
    """)


def fancy():
    print(Style.RESET_ALL + "#" * 110)

def encrypt(word, key):
    crypted = ""
    try:
        message = [word[w : w + len(key)] for w in range(0, len(word), len(key))]
        for x in message :
            for i in range(len(x)):
                for j in alpha:
                    if x[i] == j:
                        crypted += alpha[(alpha.index(j) + int(key[i]))% len(alpha)]
                    else:
                        pass
        return print(Fore.GREEN +"Your crypted text is : "+ crypted)

    except:
        print("{}ERROR \: You need to enter a key and message".format(prefix))
        print("")


def decrypt(word, key):
    decrypted = ""
    try:
        message = [word[w : w + len(key)] for w in range(0, len(word), len(key))]
        for x in message :
            for i in range(len(x)):
                for j in alpha:
                    if x[i] == j:
                        decrypted += alpha[(alpha.index(j) - int(key[i]))% len(alpha)]
                    else:
                        pass
        return print(Fore.RED +" Your decrypted text is : "+ decrypted)

    except:
        print("{}ERROR \: You need to enter a key and message".format(prefix))
        print("")






# [+] Script execution
os.system("echo off")
print("")
print("")
print("")
print("")
draw()
print("")
print("")
print("")
print("")

# [+] Commandloop


while True:
    command = input("{}".format(prefix))

    if command == "run":
        print("...")
        sleep(2)
        print("")
        print(Fore.BLUE + "The rabbit is gone :)")

        break

    elif command == "":
        pass

    elif command == "help":
        print("")
        fancy()
        print(Fore.YELLOW + """

             This is a crypto tool thal allow you
             to cypher and decypher messages using Vigner cypher.
             Command :
             encrypt -> to encrypt
             decrypt -> to decrypt
             run -> to quit
        """)
        fancy()
        print("")


    elif command == "encrypt":
        print("")
        fancy()
        m = input(Fore.GREEN + "    Enter the message that you want to encrypt : ")
        k = input(Fore.GREEN + "    Enter your key : ")
        fancy()
        print("")
        print("encrypting ...")
        sleep(5)
        print("")
        encrypt(m, k)
        print("")


    elif command == "decrypt":
        print("")
        fancy()
        m = input(Fore.RED + "   Enter the message that you want to encrypt : ")
        k = input(Fore.RED + "   Enter your key : ")
        fancy()
        print("")
        print("decrypting ...")
        sleep(5)
        print("")
        decrypt(m, k)
        print("")

    else:
        print("{}This isn't a command !".format(prefix) + " Press help for more informations.")
