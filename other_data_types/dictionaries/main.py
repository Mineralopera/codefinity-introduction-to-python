# Creating the dictionary with grocery inventory
grocery_inventory = {
    "Milk": (113, "Dairy"),
    "Eggs": (116, "Dairy"),
    "Bread": (117, "Bakery"),
    "Apples": (141, "Produce")
}

# Retrieving bread details
bread_details = grocery_inventory.get("Bread")
print(f"Details of Bread: {bread_details}")

# Adding cookies
grocery_inventory.update({"Cookies": (143, "Bakery")})
print(f"Inventory after adding Cookies: {grocery_inventory}")

# Removing Eggs 
grocery_inventory.pop("Eggs")
print(f"Inventory after removing Eggs: {grocery_inventory}")
# Output

