"""
----------------------------------

Minecraft Sever Tool

Author: Kenneth Andrews

License: Revised BSD

Copywrite 2016, Kenneth Androws
----------------------------------

This script is meant to be a spiritual continuation of the Minecraft Automation script which can be found at https://github.com/nonprofitgibi/pythonappautomation . I've elected to rewrite the code for a variety of reasons; however I'd still like to give a special thanks to Tanner Gibson, and Fredrich Paulin for their contributions to the project.

--------------------------------------------------------
"""

import sys #for exiting the script
import platform #for detecting operating system
import urllib #for downloading server files from the internet
import urllib.request
import subprocess #for starting the .jar files

def cont():  #Creates a function that asks for permission to continue
    start = 0
    while start is 0:
        answer = input("Continue?: (Y)es (Q)uit ")
        if answer is ("y"):
            start = 1
        elif answer is ("q"):
            start = 1
            sys.exit()
        else:
            print(answer, "is not a valid option. Select (Y) or (N)")

print("thanks for using my Server automation tool. It means a lot to me.")
print("This tool is meant to help install and configure a minecraft server.\n")

cont()

#Educate the user how to use the script and ask for permission to continue
print("This program assumes you don't have the server downloaded already. If")
print("you do please stop this script and place it in the same directory as")
print("your jar file. Make sure to rename the Jar to Server.jar. You can")
print("manually change it later if you want.\n")

cont()

#Ask user which .jar file they want to download, or allow them to skip ahead
print("\nWhich server software would you like to install? if unsure choose vanilla\n")
print("(1)Vanilla - The standard server software from Mojang")
print("(2)Spigot/Bukkit - Targeted towards modders that want to use community plugins")
print("(S)kip - Use this if you already have your .jar\n")

start = 0 #loop until user selects appropriate option
while start is 0:
    answer = input("Server?: ")
    if answer is ("1"):
        start = 1
        servchoice = ("vanilla")
    elif answer == ("2"):
        start = 1
        servchoice = ("modded")
    elif answer is ("s"):
        start = 1
        servchoice = ("skip")
    else:
        print(answer, "is not a valid option. Please choose (1), (2), (s)")

#Creates a variable for Mojangs server URL, along with Spigots Build tools.
vanillaurl = ("https://s3.amazonaws.com/Minecraft.Download/versions/1.11/minecraft_server.1.11.jar")
buildtoolsurl=("https://hub.spigotmc.org/jenkins/job/BuildTools/lastSuccessfulBuild/artifact/target/BuildTools.jar")

if servchoice != ("skip"):
    print("\nDownloading and configuring server software. This could take some time. Please be patient.")
    if servchoice == ("vanilla"):
        url = vanillaurl
        urllib.request.urlretrieve(url, "java.jar")
#       download(url, "java.jar")
        subprocess.call(['java', '-jar', 'java.jar'])
    elif servchoice == ("modded"):
        url = buildtoolsurl
        download = urllib.request.urlretrieve(url, "buildtools.jar")
        print("Modded server is now compiling on your system. Thanks fo your patience.")
        subprocess.call('gitcommand.BAT')
        subprocess.call(['java', '-jar', 'spigot-1.11.jar'])
    else:
        pass
else:
    pass

print("\nYou need to accept the EULA before continuing.")
print("By accepting you agree to the terms listed in Mojang's user agreement")
print("https://account.mojang.com/documents/minecraft_eula")

start = 0 # Loop until user accepts EULA
while start is 0:
    eula = input("Do you accept the EULA? (Y)es (N)o (Q)uit ")
    if eula is ("y"):
        start = 1
        with open('eula.txt', 'r') as file:
            data = file.readlines()
            data[2] = ("eula=true\n")
            with open("eula.txt", 'w') as file:
                file.writelines( data )
    elif eula is ("n"):
        print("you must accept the EULA before continuing")
    elif eula is ("q"):
        sys.exit()
    else:
       print (eula, "is not a valid option")

adminlist = []
setupadmin = input("\nWould you like to set up your OP/Admin file? (Y)es (N)o: ")
if setupadmin is ("n"):
    pass
elif setupadmin is ("y"):
        start = 1
        while start is 1:
            admin = input("\nEnter the name of your Admin, eg. Notch: ")
            #>>>>>>>>>>>>>>> Append Admin Variable to admin list here <<<<<<<<<<<<<<<<<<<<<<<<<<<
            askagain = (1)
            while askagain is (1):
                loop = input ("Would you like to add another admin?(Y)es (N)o: ")
                if loop is ("y"):
                    start = 1
                    askagain = 0
                elif loop is ("n"):
                    start = 0
                    askagain = 0
                else:
                    print("loop is not a valid ")
else:
    print(setupadmin + "is not a valid option. Please select yes or no\n")

start = 0
while start is 0:
    whitelist = input("Would you like to set up a whitelist?: (Y)es (N)o ")
    if whitelist is ("n"):
        start = 1
    elif whitelist is ("y"): #<<<<<<< edit the whitelist file and enable it in server.props
        start = 1
    else:
        print(whitelist + "is not a valid command. please select yes or no")