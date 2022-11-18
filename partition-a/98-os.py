import os
import random
import time
from os.path import exists

print("DOS98 version 1")
print("Author: Windows 98#2894")
print("Type in 'help' for more information")
print()

while True:
    commands = input("@line-98 $ ")

    if 'help' in commands:
        print("Commands: ver, dir, mvdir, random, time, clear, bdir, authors, exit")
        print("Applications: clock, calc, devices")
        print()
    
    if 'ver' in commands:
        print("DOS98 version 1")
        print()
    
    if 'dir' in commands:
        print(f"{os.listdir()}")
        print()
    
    if 'mvdir' in commands:
        selectdir = input("Move on to directory: ")

        if exists(selectdir):
            os.chdir(selectdir)
            print()
        else:
            print("That directory doesn't exist!")
            print()

    if 'bDiR' in commands:
        # os.system("cd..")
        # print()
        print("Command in development.")
        print("Restart the operating system to return.")
        print()
    
    if 'random' in commands:
        print(f"Your random number: {random.randint(0, 100000000)}")
        print()

    if 'time' in commands:
        print(f"The time is: {time.asctime()}")
        print()
    
    if 'clear' in commands:
        os.system("cls")
        print("Type in 'help' for more information")
        print()

    if 'authors' in commands:
        print("Author: Windows 98#2894")
        print("Join my discord server: https://discord.gg/tWsSdAc2HY")
        print("Open my GitHub page: https://github.com/Windows-98-Guy")
        print("Log in to my minecraft server: TheWindows98.aternos.me:30803")
        print()

    if 'exit' in commands:
        os.close("98-os.py")

    if 'clock' in commands:
        os.startfile("applications\\clock.py")

    if 'calc' in commands:
        os.startfile("applications\\calc.py")

    if 'devices' in commands:
        os.startfile("applications\\devices.py")
