size = int(input("Enter the size of the pattern: "))

i = 1
while i <= size:
    j = 1
    while j <= i:
        print("*", end="")   # prints stars on the same line
        j += 1
    print()  # moves to the next line
    i += 1
