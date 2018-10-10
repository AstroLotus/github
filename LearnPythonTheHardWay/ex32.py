#Loops and Lists
the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

for number in the_count:
    print(f"This is count {number}")

for fruit in fruits:
    print(f"A fruit of type: {fruit}")

for i in change:
    print(f"I got {i}")

elements = []

for i in range(0, 6):
    print(f"Adding {i} to the list.")
    elements.append(i)

for i in elements:
    print(f"Elements was: {i}")

i = 0
numbers = []

while i < 10:
    print(f"At the top i is {i}")
    numbers.append(i)
    i += 2
    print("Numbers now:", numbers)
    print(f"At the bottom i is {i}")
print("The numbers: ")
for num in numbers:
    print(num)