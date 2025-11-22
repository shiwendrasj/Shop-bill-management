
# Shop Management System

# Dictionary to store items and their prices
items_dict = {
    "Tomato sauce": 25,
    "Bread": 40,
    "Eggs": 60,
    "Butter": 55,
    "Chips": 20,
    "Maggi": 12,
}

# Empty lists to store what user buys
selected_items = []
selected_qty = []
selected_price = []

print("Welcome to My Shop System")
print("-------------------------")

# Showing the menu
print("List of Items:")
for k, v in items_dict.items():
    print(k, "-->", v)

print("-------------------------")

# Main loop for taking orders
while True:
    choice = input("\nEnter item name (or type 'end' to finish): ")
    
    # Check if user wants to stop
    if choice == 'end':
        break
    
    # Capitalize first letter to match dictionary (e.g. bread -> Bread)
    choice = choice.capitalize()

    # Checking if item is available
    if choice in items_dict:
        q = int(input("Enter quantity: "))
        
        # Calculation
        amt = items_dict[choice] * q
        
        # Adding details to our lists
        selected_items.append(choice)
        selected_qty.append(q)
        selected_price.append(amt)
        
        print("Item added successfully.")
        
    else:
        print("Error: Item not found! Please check spelling.")

# Generating the Final Bill
print("\n")
print("*" * 30)
print("     FINAL INVOICE")
print("*" * 30)
print("Item\tQty\tPrice") # \t gives a tab space

total_sum = 0

# Loop to print the lists
for i in range(len(selected_items)):
    print(f"{selected_items[i]}\t{selected_qty[i]}\t{selected_price[i]}")
    
    # Adding to grand total
    total_sum = total_sum + selected_price[i]

print("-" * 30)
print("Total Amount to Pay: Rs", total_sum)
print("*" * 30)