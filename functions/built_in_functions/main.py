# Dictionary of products with price and quantity sold as strings
products = {
    "Apple": ["1.20", "50"],   # "Item": [price, quantity sold]
    "Banana": ["0.50", "100"],
    "Cherry": ["2.50", "25"],
    "Mango": ["1.75", "40"]
}

# Creating the total sales list
total_sales_list = []

# Looping through each product
for item in products:
    price, quantity_sold = products[item]
    price = float(price)
    quantity_sold = int(quantity_sold)
    total_sales = quantity_sold * price
    total_sales_list.append(total_sales)
    print(f"Total sales for {item}: ${total_sales}")
    
# Generating total sales statistics
total_sum = sum(total_sales_list)
min_sales = min(total_sales_list)
max_sales = max(total_sales_list)

# Output of sales statistics
print(f"Total sum of all sales: ${total_sum}")
print(f"Minimum sales: ${min_sales}")
print(f"Maximum sales: ${max_sales}")

