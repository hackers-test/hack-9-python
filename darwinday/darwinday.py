#!/usr/bin/env python

"""
A function for counting down to Darwin Day
"""

import random
import datetime


def birthday(arg):
    """
    returns the time until Darwin Day
    """
    # Darwin day this year and next year
    current_year = datetime.datetime.today().year
    last_dday = datetime.datetime(current_year - 1, 2, 12)    
    this_dday = datetime.datetime(current_year, 2, 12)
    next_dday = datetime.datetime(current_year + 1, 2, 12)    

    # print days til Darwin's birthday
    if arg == "next":
        if datetime.datetime.now() < this_dday:
            diff = this_dday - datetime.datetime.now()
            print("{} days until Darwin's birthday".format(diff.days))
        else:
            diff = next_dday - datetime.datetime.now()
            print("{} days until Darwin's birthday".format(diff.days))

    else:
        if datetime.datetime.now() < this_dday:
            diff = datetime.datetime.now() - last_dday
            print("{} days since Darwin's birthday".format(diff.days))
        else:
            diff = datetime.datetime.now() - this_dday
            print("{} days since Darwin's birthday".format(diff.days))


def info():
    "returns a random fact about Darwin"
    facts = [
        "Darwin was born on the same day as Abraham Lincoln",
        "Darwin was not the official naturalist onboard the HMS Beagle",
        "Darwin was a botanist",
    ]
    print(random.choice(facts))


if __name__ == "__main__":
    birthday('next')
    birthday('last')
    info()
