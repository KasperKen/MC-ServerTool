"""
----------------------------------

Minecraft Sever Tool

Author: Kenneth Andrews

License: Revised BSD

Copywrite 2016, Kenneth Androws
----------------------------------

This script is meant to be a spiritual continuation of the Minecraft Automation script
which can be found at https://github.com/nonprofitgibi/pythonappautomation . I've elected
to rewrite the code for a variety of reasons; however I'd still like to give a special
thanks to Tanner Gibson, and Fredrich Paulin for their contributions to the project.

--------------------------------------------------------
"""

import sys #for exiting the script
import platform #for detecting operating system
import urllib #for downloading server files from the internet
import urllib.request
import subprocess #for starting the .jar files

def cont():  #Creates a function that asks for permission to continue
    while (True): 
        answer = input("Continue?: (Y)es (Q)uit ")
        if answer is ("y"):
            break 
        elif answer is ("q"):
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

while (True):#loop until user selects a server or skips
    answer = input("Server?: ")
    if answer is ("1"):
        servchoice = ("vanilla")
        break
    elif answer == ("2"):
        servchoice = ("modded")
        break
    elif answer is ("s"):
        servchoice = ("skip")
        break
    else:
        print(answer, + "is not a valid option. Please choose (1), (2), (s)")

#Creates a variable for Mojangs server URL, along with Spigots Build tools.
vanillaurl = ("https://s3.amazonaws.com/Minecraft.Download/versions/1.11/minecraft_server.1.11.jar")
buildtoolsurl=("https://hub.spigotmc.org/jenkins/job/BuildTools/lastSuccessfulBuild/artifact/target/BuildTools.jar")

if servchoice != ("skip"): # Proceed only if user chose to install a server
    print("\nDownloading and configuring server software. This could take some time. Please be patient.")
    if servchoice == ("vanilla"):
        urllib.request.urlretrieve(url, "java.jar")
        download(vanillaurl, "java.jar") # Downloads minecraft server and saves it as "Java.jar"
        subprocess.call(['java', '-jar', 'java.jar']) # Starts MCserver for initial setup
    elif servchoice == ("modded"):
        download = urllib.request.urlretrieve(buildtoolsurl, "buildtools.jar") #Downloads Spigot and saves it as "buildtools.jar"
        print("Modded server is now compiling on your system. Thanks fo your patience.")
        subprocess.call('gitcommand.BAT') # Initializes .bat script to compile spigot from source
        subprocess.call(['java', '-jar', 'spigot-1.11.jar']) # Starts modded MCserver for initial setup
    else:
        pass
else:
    pass

print("\nYou need to accept the EULA before continuing.")
print("By accepting you agree to the terms listed in Mojang's user agreement")
print("https://account.mojang.com/documents/minecraft_eula")


while (True): # Loop until user accepts EULA
    eula = input("Do you accept the EULA? (Y)es (N)o (Q)uit ")
    if eula is ("y"):
        with open('eula.txt', 'r') as file:
            data = file.readlines()
            data[2] = ("eula=true\n")
            with open("eula.txt", 'w') as file:
                file.writelines( data )
                break
    elif eula is ("n"):
        print("you must accept the EULA before continuing")
    elif eula is ("q"):
        sys.exit()
    else:
       print (eula + "is not a valid option")

""" same issue as whitelist. admins cant be set this way just by name.
we need to finds an alternative. maybe call out to minecraft directly
and issue a command in the server prompt

adminlist = []
setupadmin = input("\nWould you like to set up your OP/Admin file? (Y)es (N)o: ")
if setupadmin is ("n"):
    pass
elif setupadmin is ("y"):
        while (True)
            admin = input("\nEnter the name of your Admin, eg. Notch: ")
            #>>>>>>>>>>>>>>> Append Admin Variable to admin list
                while (True):
                loop = input ("Would you like to add another admin?(Y)es (N)o: ")
                if loop is ("y"):
                    pass
                elif loop is ("n"):
                    break
                else:
                    print(loop + "is not a valid ")
else:
    print(setupadmin + "is not a valid option. Please select yes or no\n")
"""
""" apparently we need a UID for each user. this cant be determined
commenting out until we find a solition (if possible)

while (True):
    whitelist = input("Would you like to set up a whitelist?: (Y)es (N)o ")
    if whitelist is ("n"):
        break
    elif whitelist is ("y"): #<<<<<<< edit the whitelist file and enable it in server.props
        ###########
        break
    else:
        print(whitelist + "is not a valid command. please select yes or no")
"""
