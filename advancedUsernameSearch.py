#from variationEngineUsername.py import 

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

  __  __                                  ____
 / / / /__ ___ _______  ___ ___ _  ___   / __/______ ____  ___  ___ ____
/ /_/ (_-</ -_) __/ _ \/ _ `/  ' \/ -_) _\ \/ __/ _ `/ _ \/ _ \/ -_) __/
\____/___/\__/_/ /_//_/\_,_/_/_/_/\__/ /___/\__/\_,_/_//_/_//_/\__/_/
   ___     __                          __
  / _ |___/ /  _____ ____  _______ ___/ /
 / __ / _  / |/ / _ `/ _ \/ __/ -_) _  /
/_/ |_\_,_/|___/\_,_/_//_/\__/\__/\_,_/

""")


def show_menu():
	print()
	print("|  SELECT WANTED UTILITIES                 |")
	print("|------------------------------------------|")
	print("|  (1) - Full Search                       |")
	print("|  (2) - Variation Search                  |")
#	print("|  (3) - Search by Website                 |")
	print("|  (3) - Profile Info  (if applicable)     |")
	print("|  (4) - Cross-Link Detection              |")
	print("|  (5) - Help                              |") 
	print()

def menu():
	choice = input()

	if choice == "1":
		clear()
		advanced_scanner()

	elif choice =="2":
		clear()
		variation_search()

	elif choice =="3":
		profile_info__search()

	elif choice == "4":
		clear()
		link_detection()

	elif choice =="5":
		clear()
		help()

	else:
		input("\nInvalid option. Press ENTER...")

def advanced_username_scanner_main():
	clear()
	show_banner()
	show_menu()
	menu()
