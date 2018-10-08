#Exercise 18. Names, Variables, Code, Functions
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

def print_one(arg1):
    print(f"arg1: {arg1}")

def print_none():
    print("I got nothing.")

print_two("Victoria", "Reworld")
print_two_again("Victoria", "Reworld")
print_one("First!")
print_none()

#my own function defined: hehe
def basic_add(n1, n2):
    print(int(n1)+int(n2))

basic_add(1,2)