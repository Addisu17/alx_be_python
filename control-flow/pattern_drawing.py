# Drawing Patterns with Nested Loops
number = int(input("Enter the size of the pattern: "))

rows = 0

while rows < number:
    for i in range(number):
        print("*", end="")
    print("")
    rows += 1
