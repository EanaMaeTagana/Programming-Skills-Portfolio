"""
Vending Machine
Assessment 2 - Intro to Programming
"""

# Create vending machine with two categories (drinks and snacks) along with their IDs, items, and prices
# Dictionary contains various nested dictionaries listing the item details
items = {
    1: {"itemID": "1A", "itemCategory": "Drink", "itemName": "Water", "itemPrice": 1.50, "itemQuantity": 20},
    2: {"itemID": "2A", "itemCategory": "Drink", "itemName": "Spark, Raspberry Fizz", "itemPrice": 3.50, "itemQuantity": 7},
    3: {"itemID": "3A", "itemCategory": "Drink", "itemName": "Zen, Green Tea Elixir", "itemPrice": 4.50, "itemQuantity": 3},
    4: {"itemID": "1B", "itemCategory": "Drink", "itemName": "Decadence, Chocolate Shake", "itemPrice": 3.00, "itemQuantity": 10},
    5: {"itemID": "2B", "itemCategory": "Drink", "itemName": "Iced Caramel Macchiato", "itemPrice": 3.50, "itemQuantity": 8},
    6: {"itemID": "3B", "itemCategory": "Drink", "itemName": "Iced Coconut Creme Brew", "itemPrice": 4.50, "itemQuantity": 10},
    7: {"itemID": "1C", "itemCategory": "Snack", "itemName": "Decadence, Chocolate Trail Mix", "itemPrice": 5.00, "itemQuantity": 8},
    8: {"itemID": "2C", "itemCategory": "Snack", "itemName": "Heatwave, Sriracha Peanuts", "itemPrice": 5.50, "itemQuantity": 3},
    9: {"itemID": "3C", "itemCategory": "Snack", "itemName": "Symphony, Salted Chips", "itemPrice": 6.00, "itemQuantity": 1},
    10: {"itemID": "1D", "itemCategory": "Snack", "itemName": "MunchBites, Honey Mustard Chips", "itemPrice": 5.50, "itemQuantity": 7},
}

# Function to display the menu
def displayMenu():
    print("\n-------------------- WELCOME ! --------------------")

    # Display drinks
    print("\n- BEVERAGE")
    for code, item in items.items(): # For loop to loop through the items that are categorised as drink
        if item["itemCategory"] == "Drink":
            print(f"{item['itemID']}: {item['itemName']} ---- ${item['itemPrice']}")

    # Display snacks
    print("\n- COMESTIBLE")
    for code, item in items.items(): # For loop to loop through the items that are categorised as snack
        if item["itemCategory"] == "Snack":
            print(f"{item['itemID']}: {item['itemName']} ---- ${item['itemPrice']}")

# Function to begin user selection
def begin():
    displayMenu() # Callback to function to display menu
    print("\n--------------------")
    print("1: Begin selection")
    print("0: Quit")
    print("--------------------")
    option = (input("- Please enter: ")) # User input to start selection of items

# Conditional statements to validate user input
    if option == "0":
        print("\n~ Thank you for your time! Have a nice day. ~")
    elif option == "1":
        userSelection()
    else: # For when user input is invalid
        print("\n--------------- Error ---------------\nInvalid option. Please try again.")
        invalid = input("\nEnter 'A' to start again or any key to quit: ")
        if invalid == "A":
            begin()
        else:
            print("\n~ Thank you for your time! Have a nice day. ~")


# Function to allow user to select items
def userSelection():
    selectedItems = [] # Empty dictionary to store the selected items

    while True: # While loop to repeat the set of code until broken
        item_ID = input("\n- Enter the ID of the item you want to purchase (or 0 to proceed to payment): ") # User input of their selected item

# Conditional statements to validate user input
        if item_ID == '0': 
            if not selectedItems: # For when the user has not previously selected any item
                print("\n--------------- Error ---------------\nNo items selected. Please choose at least one item.") 
            else:
                break
        elif item_ID in [item["itemID"] for item in items.values()]: # Loops through the menu to check for the item
            item = next(i for i in items.values() if i["itemID"] == item_ID)

            print(f"~ Selected item: {item['itemName']} - ${item['itemPrice']} | {item['itemQuantity']}x")

            quantity = int(input("\n- Enter the quantity you want to purchase of this item: "))

            if quantity <= item['itemQuantity']: # Add selected item to empty dictionary
                selectedItems.append({
                    "Name": item['itemName'],
                    "Price": item['itemPrice'],
                    "Quantity": quantity
                })
                item['itemQuantity'] -= quantity # Reduce the quantity from the menu
                print(f"~ {quantity}x {item['itemName']} added to your selection. ~")

                addAnother = input("\n- Would you like to buy another item? (Enter '1' or any key to proceed to payment): ") # User input to either buy another item or proceed to payment
                if addAnother != '1':
                    break 
            else: # For when the stock is insufficient
                print("\n--------------- Error ---------------\nInsufficient quantity. Please try again.") 
        else: # For when the item ID, entered by the user, is invalid
            print("\n--------------- Error ---------------\nInvalid item ID. Please enter a valid item ID.") 

    if selectedItems:
        displayPayment(selectedItems) # Move to the next function to display payment details of the selected items


# Function to display the selected items and their prices
def displayPayment(selectedItems):
    totalPrice = sum(item['Price'] * item['Quantity'] for item in selectedItems) # Arithmetic operators to find the sum of items
    print("\n--------------- Payment Details ---------------")
    for item in selectedItems: # Loops through the list of selected items and prints the details
        print(f"{item['Name']} - {item['Quantity']}x - Price: ${item['Price'] * item['Quantity']}")
    print(f"Total Price: ${totalPrice}")
    moneyInserted = float(input("\n- Enter the amount of money: ")) # User input of their money

# Conditional statements to evaluate user input
    if moneyInserted >= totalPrice:
        change = moneyInserted - totalPrice
        print(f"~ Your change will be: ${change} ~")
        generateReceipt(selectedItems, moneyInserted, change) # Function to generate receipt
    else: # For when the user has insufficient funds
        print("\n--------------- Error ---------------\nInsufficient funds. Please try again.") 
        displayPayment(selectedItems) # Restarts the function


# Function to show user payment
def generateReceipt(selectedItems, moneyInserted, change):
    print("\n--------------- Receipt ---------------")
    for item in selectedItems: # Loops through the items within the list and prints their details
        print(f"{item['Name']} - {item['Quantity']}x - Price: ${item['Price'] * item['Quantity']}")
    print(f"Total Price: ${sum(item['Price'] * item['Quantity'] for item in selectedItems)}")
    print(f"Cash: ${moneyInserted}")
    print(f"Change: ${change}")
    print("\n~ Thank you for your purchase! ~")


# Callback to function to start the program
begin()
    
                

            