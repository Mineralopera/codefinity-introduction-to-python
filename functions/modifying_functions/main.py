# Defining a function to apply discount
def apply_discount(price, discount=0.05):
    price *= 1 - discount
    return price

# Defining a function to apply taxes
def apply_tax(price, tax=0.07):
    price *= 1 + tax
    return price

# Defining a function to calculate the total price
def calculate_total(price, discount=0.05, tax=0.07):
    disounted_price = apply_discount(price, discount)
    total_price = apply_tax(disounted_price, tax)
    return total_price

# Default example
total_price_default = calculate_total(120)

# Custom value example
total_price_custom = calculate_total(100, discount=0.10, tax=0.08)

# Printing the output
print(f"Total cost with default discount and tax: ${total_price_default}")
print(f"Total cost with custom discount and tax: ${total_price_custom}")
