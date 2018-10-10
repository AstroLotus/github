#Functions can return something
def add(a, b):
    print(f"ADDING {a} + {b}")
    return a + b

def substract(a, b):
    print(f"SUBSTRACTING {a} - {b}")
    return a - b

def multiply(a, b):
    print(f"MULTIPLYING {a} * {b}")
    return a * b

def divide(a, b):
    print(f"DIVIDING {a} / {b}")
    return a / b

print("Let's do some math with just functions!")

age = add(22, 1)
height = substract(65, 3)
weight = multiply(45, 2)
iq = divide(250, 2)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")

print("Here is a puzzle!")

what = add(age, substract(height, multiply(weight, divide(iq, 2))))

print("That becomes:", what, "Can you do it by hand?")