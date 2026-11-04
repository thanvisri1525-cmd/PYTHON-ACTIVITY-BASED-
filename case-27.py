print("NUMERIC PATTERN GENERATOR")

rows = int(input("Enter number of rows: "))

if rows <= 0:
    print("Please enter a positive number.")
else:
    for i in range(1, rows + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()
