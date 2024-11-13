# Define the function to calculate the discount
def calculate_discount(price, discount_percent):
    # Check if the discount percent is 20% or higher
    if discount_percent >= 20:
        # Calculate the discounted price
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        # Return the original price if discount is less than 20%
        return price

# Prompt user for input
price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))

# Calculate the final price using the calculate_discount function
final_price = calculate_discount(price, discount_percent)

# Print the final price
if discount_percent >= 20:
    print(f"The final price after applying a {discount_percent}% discount is: {final_price}")
else:
    print(f"No discount applied. The original price is: {price}")
