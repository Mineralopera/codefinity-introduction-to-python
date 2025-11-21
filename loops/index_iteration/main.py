prices = [29.99, 45.50, 12.75, 38.20]

# Determining discount factor
discount_factors = [0.10, 0.20, 0.15, 0.05]

# Setting up loop
for index in range(len(prices)):
    # Apply the correct factor for this index
    prices[index] -= prices[index] * discount_factors[index]
    print(f"Updated price for item {index}: ${prices[index]:.2f}")