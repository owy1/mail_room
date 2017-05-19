"""This module manages donations."""
from faker import Factory
import random
import sys


def create_donor_list():
    """Create donor list in dictionary."""
    fake = Factory.create()
    donor_dct = {}
    for i in range(20):
        donation = random.randint(10, 50)
        donor_dct[fake.name()] = [donation]
    return donor_dct

def usr_input(donor_list):
    """Prompt for user input."""
    try:
        input = raw_input
    except NameError:
        pass
    usr_input = input("""Please enter 1 to send a Thank You note or \n
            enter 2 to create a donor report or enter 3 to exit system.""")
    if usr_input == "1":
        send_thank_you(donor_list)
    elif usr_input == "2":
        donor_report(donor_list)
    elif usr_input == "3":
        sys.exit()
    else:
        print("Please select 1, 2 or 3.")
        usr_input()


def send_thank_you(donor_list):
    """Print thank you email."""
    usr_input = input("""Please enter full name, example John Doe. \n
            or enter "list" for list of names or enter "back" to return to original prompt""")
    if usr_input == "list":
        print(donor_list.keys())
        usr_input()
    elif usr_input == "back"
        usr_input()
    else:
        if usr_input not in donor_list.keys(): donor_list[usr_input] = []
        donation_is_numeric = False
        while !donation_is_numeric:
            donation = input("""Please enter donation amount rounded to nearest dollar such as .""")
            if donation.isnumeric:
                donor_list[usr_input].append(donation)
                donation_is_numeric = True
    print("{} {}".format(usr_input))

def donor_report(donor_list):
    """Print donor report."""
    pass


def main():
    donor_list = create_donor_list()
    usr_input(donor_list)
