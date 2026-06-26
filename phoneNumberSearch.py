import os
import requests
import phonenumbers
from phonenumbers import number_type
from phonenumbers import geocoder, carrier, timezone, PhoneNumberType
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
   ___  __                   _  __           __             ____                 __
  / _ \/ /  ___  ___  ___   / |/ /_ ____ _  / /  ___ ____  / __/__ ___ _________/ /
 / ___/ _ \/ _ \/ _ \/ -_) /    / // /  ' \/ _ \/ -_) __/ _\ \/ -_) _ `/ __/ __/ _ \
/_/  /_//_/\___/_//_/\__/ /_/|_/\_,_/_/_/_/_.__/\__/_/   /___/\__/\_,_/_/  \__/_//_/
""")


def show_menu():
        print()
        print("|  SELECT WANTED UTILITIES                 |")
        print("|------------------------------------------|")
        print("|  (1) - Normal Search                     |")
        print("|  (2) - Search by Category                |")
#       print("|  (3) - Search by Website                 |")
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

#       elif choice == "6":
#               clear()
#               main()

        else:
                input("\nInvalid option. Press ENTER...")

def phone_scanner():
	print(f"\n{CYAN}[?] Enter phone number (please include country code and no spaces for dashes) (ex. +16135551234){RESET}")
	number = input("> ").strip()

	try:
		parsed = phonenumbers.parse(number)

		valid = phonenumbers.is_valid_number(parsed)
		possible = phonenumbers.is_possible_number(parsed)

		num_type = number_type(parsed)
		country = geocoder.description_for_number(parsed, "en")
		provider = carrier.name_for_number(parsed, "en")
		timezones = timezone.time_zones_for_number(parsed)

		PHONE_TYPES = {
			PhoneNumberType.MOBILE: "Mobile",
			PhoneNumberType.FIXED_LINE: "Landline",
			PhoneNumberType.FIXED_LINE_OR_MOBILE: "Landline or Mobile",
			PhoneNumberType.TOLL_FREE: "Toll Free",
			PhoneNumberType.PREMIUM_RATE: "Premium Rate",
			PhoneNumberType.VOIP: "VoIP",
			PhoneNumberType.PAGER: "Pager",
			PhoneNumberType.UAN: "UAN",
			PhoneNumberType.UNKNOWN: "Unknown"
		}

		phone_type = PHONE_TYPES.get(number_type(parsed), "Unknown")

		print(f"\n{GREEN}=== PHONE NUMBER REPORT ==={RESET}")
		print(f"Phone Type  : {phone_type}")
		print(f"Valid Number : {valid}")
		print(f"Possible : {possible}")
		print(f"Country/Area : {country if country else 'Unknown'}")
		print(f"Carrier : {provider if provider else 'Unknown'}")
		print(f"Timezone(s) : {', '.join(timezones) if timezones else 'Unknown'}")
		print(f"E164 Format : {phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.E164)}")
		print(f"National : {phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.NATIONAL)}")

	except Exception as e:
		print(f"\n{RED}[!] Invalid phone number{RESET}")
		print(e)

	input(f"\n{YELLOW}Press ENTER to continue...{RESET}")

def phone_scanner_main():
	clear()
	show_banner()
	phone_scanner()
