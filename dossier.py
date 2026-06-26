import os
import requests
from usernameSearchSites import SITES
from advancedUsernameSearch import advanced_username_scanner_main
from colours import colours
from datetime import datetime

#print(len(SITES))

GREEN = "\033[92m"
RED = "\033[31m"
YELLOW = "\033[33m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
WHITE = "\033[97m"
BLACK = "\033[30m"
ORANGE = "\033[38;5;208m"
PURPLE = "\033[35m"
RESET = "\033[0m"

def clear():
        os.system("clear")

def show_banner():
        print(r"""
   ____  ____  _______   __   _____ _________    _   ___   ____________
  / __ \/ __ \/ ____/ | / /  / ___// ____/   |  / | / / | / / ____/ __ \
 / / / / /_/ / __/ /  |/ /   \__ \/ /   / /| | /  |/ /  |/ / __/ / /_/ /
/ /_/ / ____/ /___/ /|  /   ___/ / /___/ ___ |/ /|  / /|  / /___/ _, _/
\____/_/   /_____/_/ |_/   /____/\____/_/  |_/_/ |_/_/ |_/_____/_/ |_|

 ____  ____  ____  ____  ____  ____  ____  ____  ____  ____  ____  ____
/___/ /___/ /___/ /___/ /___/ /___/ /___/ /___/ /___/ /___/ /___/ /___/

   ___               _           __  ___        __
  / _ \___  ___ ___ (_)__ ____  /  |/  /__  ___/ /__
 / // / _ \(_-<(_-</ / -_) __/ / /|_/ / _ \/ _  / -_)
/____/\___/___/___/_/\__/_/   /_/  /_/\___/\_,_/\__/
""")

def target():
	choice = input()

	firstName = input("What is your targets first name: ")
	print()
	middleName = input("Target middle name: "
	print()
	lastName = input("Target last name: ")
	print()
	usernames = input("usernames the target uses (sperate additional usernames  via commas): ")
	print()
	email = input("emails the target uses (sperate additional emails  via commas): ")
	print()
	phoneNumber = input("Phone number the target uses (sperate additional phone numbers  via commas): ")
	return{
		"firstName" = firstName,
		"middleName" = middleName,
		"lastName" = lastName,
		"usernames" = usernames,
		"email" = emails,
		"phoneNumber" = phoneNumber
	}

def databaseEmailSearch():
	

def Dossier():
	clear()
	show_banner()
	print("Dossier Mode is one of the most pwerfull versions avilable with OpenScanner, to use simple follow the below instructions.")
	target()
