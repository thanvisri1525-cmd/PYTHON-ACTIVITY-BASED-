print("STUDENT PERFORMANCE ANALYSIS")

marks = []

for i in range(1, 4):
    mark = float(input(
        f"Enter marks for examination {i}: "
    ))

    if mark < 0 or mark > 100:
        print("Invalid marks. Enter between 0 and 100.")
        break

    marks.append(mark)

if len(marks) == 3:
    average = sum(marks) / 3

    print("Average marks:", round(average, 2))
    print("Highest marks:", max(marks))
    print("Lowest marks:", min(marks))

    if marks[2] > marks[0]:
        print("Performance is improving.")
    elif marks[2] < marks[0]:
        print("Performance is declining.")
    else:
        print("Performance is stable.")
