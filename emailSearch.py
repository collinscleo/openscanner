import os
from datetime import datetime

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

   ____           _ __  ____
  / __/_ _  ___ _(_) / / __/______ ____  ___  ___ ____
 / _//  ' \/ _ `/ / / _\ \/ __/ _ `/ _ \/ _ \/ -_) __/
/___/_/_/_/\_,_/_/_/ /___/\__/\_,_/_//_/_//_/\__/_/
""")

def show_menu():
        print()
        print("|  SELECT WANTED UTILITIES                 |")
        print("|------------------------------------------|")
        print("|  (1) - Normal Search                     |")
        print("|  (2) - Search by Category                |")
        print("|  (3) - Variation Search                  |")
        print("|  (4) - Help                              |")
        print("|  (5) - Back                              |")
        print()

def menu():
        choice = input()

        if choice == "1":
                clear()
                email_scanner()

        elif choice =="2":
                clear()
                category_search()

        elif choice =="3":
                variation_search()

        elif choice == "4":
                clear()
                help()

        else:
                input("\nInvalid option. Press ENTER...")

def email_scanner:
	clear()
	show_banner()
	email_exists_counter = 0
	email_does_not_exist = 0

	username = input("Email: ")
	print("\nSearching for", username)
	print("-" * 50)

	results = {
		"social": [],
		"gaming": [],
		"programming": [],
		"forums": [],
		"entertainment": [],
		"shopping": [],
		"education": [],
		"adult": []
	}













