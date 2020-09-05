import numpy as np
import sys
import pickle
import pyAesCrypt
import os


bufferSize = 64 * 1024
answer = "null"

def PasswordCreate():
    Q = str(input("Create A New Password: "))
    Qcheck = str(input("Retype Password: "))

    while Q!=Qcheck:
        print("Passwords don't Match! Try Again!")
        Q = str(input("Create A New Password: "))
        Qcheck = str(input("Retype Password: "))

    pickle.dump(Q, open("Password.txt", "wb"))
    # encrypt
    pyAesCrypt.encryptFile("Password.txt", "Password.txt.aes", answer, bufferSize)
    os.remove("Password.txt")

def Password_Exist_Check():
    try:
        pyAesCrypt.decryptFile("Password.txt.aes", "Password.txt", answer, bufferSize)
        Password = pickle.load(open("Password.txt", "rb"))
        os.remove("Password.txt")
        return(True)
    except:
        return(False)

def PasswordCheck():
    if(Password_Exist_Check() == False):
        PasswordCreate()
    else:
        try:
            PasswordTry = str(input("Password: "))
            pyAesCrypt.decryptFile("Password.txt.aes", "Password.txt", answer, bufferSize)
            PasswordReal = pickle.load(open("Password.txt", "rb"))
            os.remove("Password.txt")
        except:
            print("Something went wrong close application and try again!")

        while(PasswordReal != PasswordTry):
            print("Wrong Password! Try Again!")
            PasswordTry = str(input("Password: "))

PasswordCheck()