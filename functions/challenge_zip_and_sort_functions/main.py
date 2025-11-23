# List of product names
products = ["Banana", "Apple", "Mango", "Cherry"]

# List of product prices
prices = [1.20, 0.50, 2.50, 1.75]

# List of quantity sold
quantities_sold = [50, 100, 25, 40]

# Using the zip 
combined_list = list(zip(products, prices, quantities_sold))


# Sorting the combined list
sorted_products = sorted(combined_list)

for product_name, product_price, quantity_sold in combined_list:
    print(f"Product: {product_name}, Price: {product_price}, Quantity sold: {quantity_sold}")