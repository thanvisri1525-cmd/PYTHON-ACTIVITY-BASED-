print("FUEL AND ROUTE COMPARISON")

distance_a = float(input("Enter Route A distance: "))
distance_b = float(input("Enter Route B distance: "))
mileage = float(input("Enter vehicle mileage (km/l): "))
fuel_price = float(input("Enter fuel price per litre: "))

if (distance_a <= 0 or distance_b <= 0
        or mileage <= 0 or fuel_price <= 0):
    print("Please enter positive values.")

else:
    fuel_a = distance_a / mileage
    fuel_b = distance_b / mileage

    cost_a = fuel_a * fuel_price
    cost_b = fuel_b * fuel_price

    print("Route A fuel required:",
          round(fuel_a, 2), "litres")
    print("Route A cost: Rs.", round(cost_a, 2))

    print("Route B fuel required:",
          round(fuel_b, 2), "litres")
    print("Route B cost: Rs.", round(cost_b, 2))

    if cost_a < cost_b:
        print("Route A is more economical.")
    elif cost_b < cost_a:
        print("Route B is more economical.")
    else:
        print("Both routes have equal costs.")
