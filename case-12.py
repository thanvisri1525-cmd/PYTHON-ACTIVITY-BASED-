import math

print("ATTENDANCE RECOVERY CALCULATOR")

total = int(input("Enter total classes conducted: "))
attended = int(input("Enter classes attended: "))

if total <= 0 or attended < 0 or attended > total:
    print("Invalid attendance details.")

else:
    percentage = attended / total * 100

    print("Attendance percentage:",
          round(percentage, 2), "%")

    if percentage >= 75:
        print("Attendance requirement satisfied.")
    else:
        required = math.ceil(
            (0.75 * total - attended) / 0.25
        )

        print("Additional classes required:", required)
