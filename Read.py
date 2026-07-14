# Product Wholesale System
# Dibyant Bhatta
# 24046745
# L1C6

''' This function access a text file and read product data from the text file which is in the same folder with the py. file and that text file contains the data related to the
product like, product name, brand, quantity of product, price of product and the country it is from. '''

def read_products(filename):

    """
    Summary:
        Reads product data from a text file. Each line in the file represents a product with its name, brand, quantity, cost price, and country. Calculates the selling price
        (200% markup) and stores product data in a list of dictionaries.

    Parameters:
        filename (str): Name of the file from which product data is to be read.

    Variables:
        products (list): List to store all product dictionaries.
        lines (list): Lines read from the file.
        line (str): Process individual line from the file.
        parts (list): Split components of each line.
        name (str): Product name.
        brand (str): Product brand.
        quantity (int): Number of units available.
        cost_price (float): Original cost of the product.
        sell_price (float): Computed selling price (200% markup).
        country (str): Country of origin for the product.

    Returns:
        products (list): List of dictionaries, each representing a product with all details.

    Raises:
        Handles FileNotFoundError and general exceptions. Skips lines with invalid data format.
    """

    products = []

    try:
        with open(filename, "r") as file:
            lines = file.readlines()

            for line in lines:
                if line != "\n":

                    parts = line.split(",")

                    if len(parts) == 5:
                        try:
                            name = parts[0]
                            brand = parts[1]
                            quantity = int(parts[2])
                            cost_price = float(parts[3])
                            country = parts[4].replace("\n", "")

                            sell_price = cost_price * 2

                            products.append({
                                "name": name,
                                "brand": brand,
                                "quantity": quantity,
                                "cost_price": cost_price,
                                "sell_price": sell_price,
                                "country": country
                            })

                        except:
                            print("Invalid data format in file. Skipping line.\n")

    except:
        print("File not found.\n")

    return products