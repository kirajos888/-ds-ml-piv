import math
def get_actual_cost(sqft_wall, sqft_ceiling, sqft_per_gallon, cost_of_gallon):
    cost = math.ceil((sqft_wall + sqft_ceiling) / sqft_per_gallon) * cost_of_gallon
    return cost
sqft_wall = float(input("Enter area of wall: "))
sqft_ceiling = float(input("Ceiling: "))
sqft_per_gallon = float(input("Galoon needed: "))
cost_of_gallon = float(input("Paint cost: "))

print("Total cost of paint: ")
print(get_actual_cost(sqft_wall, sqft_ceiling, sqft_per_gallon, cost_of_gallon))
