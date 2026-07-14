# Product Wholesale System
# Dibyant Bhatta
# 24046745
# L1C6

import datetime
from Read import read_products
from Write import save_products


''' This function is to display all products with calculated selling price, as the cost price is very low and the selling price is 200% of the cost price this function calculates
and displays the selling price after adding 200% concept '''

def display_products(products):

    """
    Summary:
        Displays all available products in a well formatted table with calculated selling prices.

    Parameters:
        products (list): List containing product dictionaries.

    Returns:
        None
    """

    print("\n==========================================================================")
    print("                          AVAILABLE PRODUCTS LIST")
    print("==========================================================================")
    print("No   Product Name          Brand           Qty   Price")
    print("--------------------------------------------------------------------------")

    i = 1

    for p in products:

        no = str(i)
        name = p["name"]
        brand = p["brand"]
        qty = str(p["quantity"])
        price = "Rs " + str(int(p["sell_price"]))

        line = no + " " * (4 - len(no))
        line += name + " " * (21 - len(name))
        line += brand + " " * (16 - len(brand))
        line += qty + " " * (6 - len(qty))
        line += price

        print(line)

        i = i + 1

    print("==========================================================================\n")


''' This function creates an invoice file after someone buys any of the products from the product list and displays the bill in the terminal as well as txt file'''

def generate_invoice(customer_name, items, total):

    """
    Summary:
        Generates a sales invoice and saves it as a text file.

    Parameters:
        customer_name (str): Name of customer.
        items (list): Sold items.
        total (float): Total payable amount.
    """

    now = datetime.datetime.now()

    date_str = (
        str(now.year) + "-" +
        str(now.month) + "-" +
        str(now.day) + "-" +
        str(now.hour) + "-" +
        str(now.minute) + "-" +
        str(now.second)
    )

    filename = "invoice_" + customer_name.replace(" ", "_") + "_" + date_str + ".txt"

    with open(filename, "w") as file:

        header = "\n==========================================================================\n"
        header += "                      W E C A R E   S T O R E\n"
        header += "                           SALES INVOICE\n"
        header += "==========================================================================\n"
        header += "Customer Name : " + customer_name + "\n"
        header += "Date          : "
        header += str(now.year) + "-" + str(now.month) + "-" + str(now.day)
        header += "   Time: "
        header += str(now.hour) + ":" + str(now.minute) + ":" + str(now.second)
        header += "\n"
        header += "--------------------------------------------------------------------------\n"
        header += "| Product Name | Brand | Qty | Free | Unit Price |\n"
        header += "--------------------------------------------------------------------------\n"

        file.write(header)
        print(header)

        for item in items:

            row = (
                "| " + item["name"] +
                " | " + item["brand"] +
                " | " + str(item["quantity"]) +
                " | " + str(item["free"]) +
                " | Rs " + str(int(item["price"])) +
                " |\n"
            )

            file.write(row)
            print(row)

        footer = "--------------------------------------------------------------------------\n"
        footer += "| TOTAL AMOUNT PAYABLE: Rs " + str(int(total)) + " |\n"
        footer += "==========================================================================\n"
        footer += "                  THANK YOU FOR SHOPPING WITH US\n"
        footer += "==========================================================================\n"

        file.write(footer)
        print(footer)

    print("Invoice saved as '" + filename + "'\n")

    ''' This function creates an invoice file after restocking any of the products in the product list and displays the bill in the terminal as well as txt file. '''

def generate_restock_invoice(vendor_name, items, total):

    """
    Summary:
        Generates a restocking invoice and saves it as a text file.

    Parameters:
        vendor_name (str): Name of supplier/vendor.
        items (list): List of restocked products.
        total (float): Total restocking cost.

    Returns:
        None
    """

    # Get current date and time
    now = datetime.datetime.now()

    # Create a unique timestamp
    date_str = (
        str(now.year) + "-" +
        str(now.month) + "-" +
        str(now.day) + "-" +
        str(now.hour) + "-" +
        str(now.minute) + "-" +
        str(now.second)
    )

    # Create filename for invoice
    filename = "restock_" + vendor_name.replace(" ", "_") + "_" + date_str + ".txt"

    # Open invoice file in write mode
    with open(filename, "w") as file:

        # Create invoice header
        header = "\n======================================================================\n"
        header += "                      W E C A R E   S T O R E\n"
        header += "                         RESTOCK INVOICE\n"
        header += "======================================================================\n"
        header += "Vendor Name  : " + vendor_name + "\n"
        header += "Date         : "
        header += str(now.year) + "-" + str(now.month) + "-" + str(now.day)
        header += "   Time: "
        header += str(now.hour) + ":" + str(now.minute) + ":" + str(now.second)
        header += "\n"
        header += "----------------------------------------------------------------------\n"
        header += "| Product Name | Brand | Qty | Cost Price |\n"
        header += "----------------------------------------------------------------------\n"

        # Write and print header
        file.write(header)
        print(header)

        # Write every restocked product
        for item in items:

            row = (
                "| " + item["name"] +
                " | " + item["brand"] +
                " | " + str(item["quantity"]) +
                " | Rs " + str(int(item["cost_price"])) +
                " |\n"
            )

            file.write(row)
            print(row)

        # Create invoice footer
        footer = "----------------------------------------------------------------------\n"
        footer += "| TOTAL RESTOCKING COST: Rs " + str(int(total)) + " |\n"
        footer += "======================================================================\n"
        footer += "                    STOCK UPDATED SUCCESSFULLY\n"
        footer += "======================================================================\n"

        # Write and print footer
        file.write(footer)
        print(footer)

    # Notify user
    print("Restocking invoice saved as '" + filename + "'\n")

    ''' This function has the selling logic of the program, like buy 3 get 1 free,
selling price double the cost price '''

def sell_products(filename):

    """
    Summary:
        Handles selling of products using the Buy 3 Get 1 Free offer.
        Updates stock, generates invoice and saves updated product list.

    Parameters:
        filename (str): Product file name.

    Returns:
        None
    """

    # Read all products from the file
    products = read_products(filename)

    # Check if there are any products available
    if len(products) == 0:
        print("No products to sell.\n")
        return

    # Ask customer's name
    customer_name = input("Enter customer's name: ")

    # Store total bill amount
    total = 0

    # List to store all sold items
    items_sold = []

    # Allow selling multiple products
    while True:

        # Display all available products
        display_products(products)

        try:
            # Ask user to select a product
            index = int(input("Enter product number to sell: "))

            # Validate product number
            if index < 1 or index > len(products):
                print("Invalid product number.\n")
                continue

            # Ask quantity
            quantity = int(input("Enter quantity to sell: "))

            # Quantity must be positive
            if quantity <= 0:
                print("Quantity must be positive.\n")
                continue

        except:
            print("Enter valid numbers.\n")
            continue

        # Get selected product
        product = products[index - 1]

        # Buy 3 Get 1 Free offer
        free = quantity // 3

        # Check stock availability
        if product["quantity"] < (quantity + free):
            print("Not enough stock.\n")
            continue

        # Reduce stock
        product["quantity"] = product["quantity"] - (quantity + free)

        # Calculate bill
        total = total + quantity * product["sell_price"]

        # Store sold product details
        items_sold.append({
            "name": product["name"],
            "brand": product["brand"],
            "quantity": quantity,
            "free": free,
            "price": product["sell_price"]
        })

        # Ask whether user wants to sell another product
        more = input("Sell another product? (y/n): ").lower()

        if more != "y":
            break

    # Generate invoice and save updated stock
    if len(items_sold) > 0:
        generate_invoice(customer_name, items_sold, total)
        save_products(filename, products)   

        ''' This function is to handle restocking of products from the supplier '''

def restock_products(filename):

    """
    Summary:
        Handles restocking of products by the admin.
        Updates product quantity and optionally updates the cost price.
        Generates a restocking invoice and saves the updated product list.

    Parameters:
        filename (str): Name of the product file.

    Returns:
        None
    """

    # Read all products from the file
    products = read_products(filename)

    # Check if there are products available
    if len(products) == 0:
        print("No products to restock.\n")
        return

    # Ask supplier name
    vendor_name = input("Enter supplier's name: ")

    # Store total restocking cost
    total = 0

    # Store restocked items
    items_restocked = []

    # Allow multiple products to be restocked
    while True:

        # Display available products
        display_products(products)

        try:
            # Ask user to choose a product
            index = int(input("Enter product number to restock (0 to stop): "))

            # Stop restocking
            if index == 0:
                break

            # Validate product number
            if index < 1 or index > len(products):
                print("Invalid number.\n")
                continue

            # Ask quantity
            quantity = int(input("Enter quantity to add: "))

            # Quantity must be positive
            if quantity <= 0:
                print("Quantity must be positive.\n")
                continue

            # Ask for new cost price
            new_price = float(input("Enter new cost price (0 to skip): "))

        except:
            print("Enter valid numeric input.\n")
            continue

        # Get selected product
        product = products[index - 1]

        # Increase stock quantity
        product["quantity"] = product["quantity"] + quantity

        # Update price if user entered a new one
        if new_price > 0:
            product["cost_price"] = new_price

            # Selling price = cost price × 2 (200% of cost price)
            product["sell_price"] = new_price * 2

        # Calculate total restocking cost
        total = total + quantity * product["cost_price"]

        # Store restocked product details
        items_restocked.append({
            "name": product["name"],
            "brand": product["brand"],
            "quantity": quantity,
            "cost_price": product["cost_price"]
        })

    # Generate invoice and save updated products
    if len(items_restocked) > 0:
        generate_restock_invoice(vendor_name, items_restocked, total)
        save_products(filename, products)