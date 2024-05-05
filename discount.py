
def calculate_discount(price, discount_percent):
    discount = discount_percent / 100  # Convert percentage to decimal
    if discount >= 0.2:  # Apply discount only if 20% or higher
        final_price = price * (1 - discount)
    else:
        final_price = price
    return final_price

# User input for price and discount
original_price = float(input("Enter the original price of the item: "))
discount_rate = float(input("Enter the discount percentage (0 to 100): "))

# Calculate final price with discount function
final_price = calculate_discount(original_price, discount_rate)

# Print the result with a discount condition message
if discount_rate >= 20:
  print(f"Final price after applying a {discount_rate:.1f}% discount: ${final_price:.2f}")
else:
  print(f"No discount applied. Price remains at ${original_price:.2f}")

    
