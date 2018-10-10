#Making Decisions
print("Door 1 or 2?")

door = input("> ")

if door == "1":
    print("There's a bear and a cake.")
    print("What do you do?")
    print("1. the cake")
    print("2. The bear")

    bear = input("> ")

    if bear == "1":
        print("You died. GG")
    elif bear == "2":
        print("The bear eats your legs off. GG")
    else:
        print(f"Well, doing {bear} is probably better.")
        print("Bears run away.")
elif door == "2":
    print("You stare into an eyeball")
    print("meh1")
    print("blue2")
    print("meh3")

    insanity = input("> ")

    if insanity == "1" or insanity == "2":
        print("Jello!")
        print("gg!")
    else:
        print("You died.")
        print("gg!")
else:
    print("Yeeeeepeeeedoooo!")