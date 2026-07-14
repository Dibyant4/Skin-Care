# Product Wholesale System
# Dibyant Bhatta
# 24046745
# L1C6

from Read import read_products
from Operation import display_products, sell_products, restock_products


''' This function executes the main program, it handles all loading and displaying of the product data '''

def main():

    """
    Summary:
        Main function that provides the menu options for the WeCare Store System.
        It allows the user to:
            1. View Products
            2. Sell Products
            3. Restock Products
            4. Exit the System

    Parameters:
        None

    Returns:
        None
    """

    # Product file name
    filename = "products.txt"

    # If the product file is empty, create default products
    if len(read_products(filename)) == 0:

        with open(filename, "w") as file:

            file.write("Vitamin C Serum,Garnier,200,1000,France\n")
            file.write("Skin Cleanser,Cetaphil,100,280,Switzerland\n")
            file.write("Sunscreen,Aqualogica,200,700,India\n")
            file.write("Moisturizer,CeraVe,50,5000,China\n")
            file.write("Toner,Plam,300,250,Brazil\n")

    # Main menu loop
    while True:

        print("\n==========================================")
        print("      WeCare Skin Care Store System")
        print("==========================================")
        print("1. View All Products")
        print("2. Sell Products")
        print("3. Restock Products")
        print("4. Exit")
        print("==========================================")

        # Get user choice
        choice = input("Enter your choice (1-4): ")

        # View Products
        if choice == "1":

            products = read_products(filename)
            display_products(products)

        # Sell Products
        elif choice == "2":

            sell_products(filename)

        # Restock Products
        elif choice == "3":

            restock_products(filename)

        # Exit Program
        elif choice == "4":

            print("\nThank you for using WeCare Store System.")
            print("Have a great day!\n")
            break

        # Invalid Option
        else:

            print("\nInvalid choice. Please try again.\n")


# Start the program
main()