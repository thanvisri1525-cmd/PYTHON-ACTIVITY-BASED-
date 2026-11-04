print("FOOD WASTE MONITORING SYSTEM")

prepared = float(input(
    "Enter food prepared in kg: "
))

consumed = float(input(
    "Enter food consumed in kg: "
))

if prepared <= 0 or consumed < 0 or consumed > prepared:
    print("Invalid food quantities.")

else:
    wasted = prepared - consumed
    percentage = wasted / prepared * 100

    print("Food prepared:", prepared, "kg")
    print("Food consumed:", consumed, "kg")
    print("Food wasted:", round(wasted, 2), "kg")
    print("Waste percentage:",
          round(percentage, 2), "%")

    if percentage > 20:
        print("Warning: High food waste!")
        print("Consider preparing less food.")
    else:
        print("Food waste is within the defined limit.")
