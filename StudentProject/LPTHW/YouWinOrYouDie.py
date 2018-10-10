# YOU WIN OR YOU DIE
import random
import sys

option = ["Rich", "Poor", "Ordinary"]
R = [random.choice(option)]


def win():
    print(
        "\nOne has won, but is winning a victory or a defeat? What is the universal final happiness?\n "
    )
    exit(0)


def m():
    print("\nOne got into an car accident. One died.")
    gg()


def gg():
    print("\nOne has to die eventually. But is it a defeat or a relief?\n ")
    exit(0)


def tie():
    print("One will die a boring and long life. It's a tie.\n")
    exit(0)


def start():
    print("\nOne is born.")
    print("\nOne chooses Life? Or Death?")
    # ld = life or death
    ld = input("\nLife Or Death? > ")
    if "Death" in ld:
        win()
    elif "Life" in ld:
        if "Poor" in R:
            print("\nOne has born in a poor family.")
            print("\nOne has encountered a break-in. One lost everything.")
            fight_or_flight(R)
        elif "Rich" in R:
            print("\nOne has born in a rich family.")
            print("\nOne has an inheritance dispute.")
            fight_or_flight(R)
        else:
            print("\nOne has born in an ordinary family.")
            print("\nOne has a mid-life crisis")
            fight_or_flight(R)
    else:
        m()  # m = mistype


def fight_or_flight(x):
    ff = input("\nFight or Flight?> ")
    if "Fight" in ff:
        if not "Rich" in x:
            second_round(x)
        else:
            win()  
    elif "Flight" in ff:
        tie()
    else:
        m()

def second_round(y):
    print("\nOne has endured and became rich. One, however,  has an inheritance dispute.")
    ff2 = input("\nFight or Flight?> ")
    if "Fight" in ff2:
        win()
    else:
        gg()


start()
