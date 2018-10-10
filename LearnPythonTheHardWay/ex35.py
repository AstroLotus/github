#Branches and Functions
from sys import exit

def gold_room():
    print("This room is full of gold, how much will you take?")

    choice = input("> ")
    if "0" in choice or "1" in choice:
        how_much = int(choice)
    else:
        dead("GG")

    if how_much < 50:
        print("Nice, you win!")
        exit(0)
    else:
        dead("GG")

def bear_room():
    print("""There is a bear here.
    a bunch of honey.
    bear is in front of a door
    u gonna move the bear?
    """)
    bear_moved = False
    while True:
        choice = input("> ")

        if choice == "take honey":
            dead("face off")
        elif choice == "taunt bear" and not bear_moved:
            print("you can go through now")
            bear_moved = True
            
        elif choice == "taunt bear" and bear_moved:
            print("leg off")
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print("huh?")

def insane_room():
    print("""
    All bow to the insane person
    flee for your life or eat your head?
    """)

    choice = input("> ")

    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("Yum! GG")
    else:
        insane_room()

def dead(why):
    print("why, GG!")
    exit(0)

def start():
    print("""
    You are in a dark room
    A door to the left and a door to the right
    which one?
    """)

    choice = input("> ")

    if choice == "left":
        bear_room()
    elif choice == "right":
        insane_room()
    else:
        dead("GG")

start()    