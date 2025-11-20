# Current inventory on shelf
shelf = ("apples", "oranges", "bananas", "apples", "grapes", "bananas", "apples")

# Count of fruits
apple_count = shelf.count("apples")
grape_count = shelf.count("grapes")

# Calculating index of fruits
banana_index = shelf.index("bananas")
orange_index = shelf.index("oranges")

# Output 
print(f"Number of Apples: {apple_count}")
print(f"First Banana Index: {banana_index}")

if apple_count < 5:
    print("Apples need to be restocked.")
else:
    print("Apples are sufficiently stocked.")

if grape_count == 1:
    print("Grapes need to be restocked.")
else:
    print("Grapes are sufficiently stocked.")

if "oranges" in shelf:
    print(f"Oranges are at index: {orange_index}")
else:
    "Oranges are out of stock."