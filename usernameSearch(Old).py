
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

  __  __                                  ____
 / / / /__ ___ _______  ___ ___ _  ___   / __/______ ____  ___  ___ ____
/ /_/ (_-</ -_) __/ _ \/ _ `/  ' \/ -_) _\ \/ __/ _ `/ _ \/ _ \/ -_) __/
\____/___/\__/_/ /_//_/\_,_/_/_/_/\__/ /___/\__/\_,_/_//_/_//_/\__/_/

""")


def show_menu():
	print()
	print("|  SELECT WANTED UTILITIES                 |")
	print("|------------------------------------------|")
	print("|  (1) - Normal Search                     |")
	print("|  (2) - Search by Category                |")
#	print("|  (3) - Search by Website                 |")
	print("|  (3) - Advanced  Scan                    |")
	print("|  (4) - Help                              |")
	print()

def menu():
	choice = input()

	if choice == "1":
		clear()
		username_scanner()

	elif choice =="2":
		clear()
		category_search()

	elif choice =="3":
		clear()
		advanced_username_scanner_main()

	elif choice == "4":
		clear()
		help()

#	elif choice == "6":
#		clear()
#		main()

	else:
		input("\nInvalid option. Press ENTER...")

def save_results(results, username):

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    filename = f"{username}_{timestamp}.txt"

    with open(filename, "w") as file:

        file.write("=" * 50 + "\n")
        file.write(f"Username Scan Results for: {username}\n")
        file.write(f"Scan Time: {timestamp}\n")
        file.write("=" * 50 + "\n\n")

        for category, sites in results.items():

            file.write(f"[{category.upper()}]\n")
            file.write("-" * 30 + "\n")

            if not sites:
                file.write("No results found\n\n")
                continue

            for site in sites:

                file.write(
                    f"[{site['status']}] "
                    f"{site['site']} - "
                    f"{site['url']}\n"
                )

            file.write("\n")

    print(f"\nResults saved to: {filename}")


def category_search():
	clear()
	show_banner()
	username_exists_counter = 0
	username_does_not_exist_counter = 0


	print("Available Categories:")
	print("--------------------")

	categories = sorted(
		set(site["category"] for site in SITES.values())
	)

	for i, category in enumerate(categories, start=1):
		print(f"({i}) - {category}")

	choice = input("\nSelect category: ")

	try:
		selected_category = categories[int(choice) - 1]
	except (ValueError, IndexError):
		print("Invalid category")
		return

	username = input("\nUsername: ")

	print(f"\nSearching {selected_category} sites...")
	print("-" * 50)

	for site_name, site_data in SITES.items():

		if site_data["category"] != selected_category:
			continue

		url = site_data["url"].format(username)

		try:
			response = requests.get(url, timeout=5)

			if response.status_code == 200:
				username_exists_counter += 1
				print(f"{GREEN}[FOUND] {site_name}: {url}{RESET}")
			else:
				username_does_not_exist_counter += 1
				print(f"{RED}[NOT FOUND] {site_name}{RESET}")

		except requests.RequestException:
			print(f"{YELLOW}[ERROR] {site_name}{RESET}")

	print()
	print(username_exists_counter, " sites have accounts with the username: ", username)
	print()
	print(username_does_not_exist_counter, " sites do not have accounts with the username: ", username)
	print()

	save = input("Save results? (y/n): ").lower()

	if save == "y":
		save_results(results, username)

#def variation_search:
#	clear()
#	show_banner()
#	username_exists_counter = 0
#	username_does_not_exist_counter = 0
#	username = input("Username" )

def username_scanner():
	clear()
	show_banner()
	username_exists_counter = 0
	username_does_not_exist_counter = 0

	username = input("What is the username you want to search: ")
	print("\nSearching for:", username)
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


	for site_name, site_data in SITES.items():

		category = site_data["category"]
		url = site_data["url"].format(username)

		try:
			response = requests.get(url, timeout=5)

			if response.status_code == 200:
				results[category].append({
					"site": site_name,
					"url": url,
					"status": "FOUND"
				})

				print(f"{GREEN}[FOUND] {site_name}: {url}{RESET}")
#				print(f"[FOUND] {site_name}: {url}")
				username_exists_counter += 1

			else:
				results[category].append({
					"site": site_name,
					"url": url,
					"status": "NOT FOUND"
				})
				print(f"{RED}[NOT FOUND] {site_name}: {url}{RESET}")
				username_does_not_exist_counter += 1

		except requests.RequestException:
			results[category].append({
				"site": site_name,
				"url": url,
				"status": "ERROR"
			})
			print(f"{YELLOW}[ERROR] {site_name}: {url}{RESET}")

	print("\n")
	print("=" * 50)
	print("RESULTS")
	print("=" * 50)

	for category, sites in results.items():

		sites.sort(
			key=lambda site:
				site["status"] != "FOUND"
		)

		print(f"\n[{category.upper()}]")
		print("-" * 30)

		if not sites:
			print("No results found")
			continue

		for site in sites:

			if site["status"] == "FOUND":
				color = GREEN
			elif site["status"] == "NOT FOUND":
				color = RED
			else:  # ERROR
				color = YELLOW

			print(
				f"{color}[{site['status']}] {site['site']} {url}{RESET}"
			)
#except requests.RequestException:
#				print(f"[ERROR] {site_name}")

	print()
	print(username_exists_counter, " sites have accounts with the username: ", username)
	print()
	print(username_does_not_exist_counter, " sites do not have accounts with the username: ", username)
	print()

	save = input("Save results? (y/n): ").lower()

	if save == "y":
		save_results(results, username)


def username_scanner_main():
	clear()
	show_banner()
	show_menu()
	menu()
#	make_txt()
