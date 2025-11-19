# Creating sublists
meat = ["Ham", 3.99, 50, "Sliced"]
cheese = ["Cheddar", 5.49, 100, "Sharp"]
condiment = ["Mustard", 1.99, 75, "Spicy"]

#Creating the main list
deli_dept = [meat, cheese, condiment]

# Printing initial main list
print(f"Initial Deli List: {deli_dept}")

# Restocking meat
if "Ham" in meat and meat[2] < 100:
    meat[2] = 100

# Adding Seasonal meat
seasonal_meat = ["Turkey", 4.50, 100, "Sliced"]

# Adding seasonal_meat to deli_dept
deli_dept.append(seasonal_meat)

# Removing condiment
deli_dept.remove(condiment)

# Sorting deli_dept
deli_dept.sort()

# Output after updates
print(f"Updated Deli List: {deli_dept}")