# Creating vegetable list
vegetables = ["tomatoes", "potatoes", "onions"]

# Removing onions from list vegetables
vegetables.remove("onions")

# Adding carrots to list vegetables
vegetables.append("carrots")

# Adding cucumbers to list vegetables
vegetables.append("cucumbers")

# Sorting list vegetables
vegetables.sort()

# Printing result
print(f"Updated Vegetable Inventory: {vegetables}")

if "carrots" in vegetables:
    print("Carrots are already in the list.")

if "cucumbers" in vegetables:
    print("Cucumbers are already in the list.")