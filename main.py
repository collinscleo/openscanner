import os
from usernameSearch import username_scanner_main
from emailSearch import email_scanner

def clear():
	os.system("clear")

def show_banner():
	print(r"""
   ____  ____  _______   __   _____ _________    _   ___   ____________
  / __ \/ __ \/ ____/ | / /  / ___// ____/   |  / | / / | / / ____/ __ \
 / / / / /_/ / __/ /  |/ /   \__ \/ /   / /| | /  |/ /  |/ / __/ / /_/ /
/ /_/ / ____/ /___/ /|  /   ___/ / /___/ ___ |/ /|  / /|  / /___/ _, _/
\____/_/   /_____/_/ |_/   /____/\____/_/  |_/_/ |_/_/ |_/_____/_/ |_|

""")

def show_menu():
	print()
	print("|  SELECT TOOL TO USE                      |")
	print("|------------------------------------------|")
	print("|  (1) - Username Search                   |")
	print("|  (2) - Email Search                      |")
	print("|  (3) - Domain Search                     |")
	print("|  (4) - Settings                          |")
	print("|  (0) - Exit                              |")
	print()

def menu():
	choice = input()

	if choice == "1":
		clear()
		username_scanner_main()

	elif choice == "2":
		clear()
		email_scanner()

	elif choice == "3":
		clear()
		domain_search()

	elif choice == "4":
		clear()
		settings()

	elif choice == "5":
		clear()
		exit()

	else:
		input("\nInvalid option. Press ENTER...")


def main():
	clear()
	show_banner()
	show_menu()
	menu()


main()
