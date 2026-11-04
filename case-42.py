print("STUDENT MARKS MATRIX ANALYSIS")

students = []
marks = []

for i in range(3):
    name = input(f"Enter student {i + 1} name: ")
    students.append(name)

    row = []

    for j in range(3):
        mark = float(input(
            f"Enter subject {j + 1} marks for {name}: "
        ))

        if mark < 0 or mark > 100:
            print("Invalid marks.")
            break

        row.append(mark)

    if len(row) != 3:
        break

    marks.append(row)

if len(marks) == 3:
    totals = []
    averages = []

    for row in marks:
        total = sum(row)
        average = total / 3

        totals.append(total)
        averages.append(average)

    for i in range(3):
        print("\nStudent:", students[i])
        print("Total:", totals[i])
        print("Average:", round(averages[i], 2))

    top_index = totals.index(max(totals))

    print("\nTop performer:", students[top_index])
    print("Highest total:", totals[top_index])
    
