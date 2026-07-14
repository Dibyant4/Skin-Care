# Product Wholesale System
# Dibyant Bhatta
# 24046745
# L1C6

''' This function is for saving the product list in the file, when we sell or restock any product this function's
responsibility is to save or update the new list in the file '''

def save_products(filename, products):

    """
    Summary:
        Saves the updated list of products to a file. This function is called after
        selling or restocking products to ensure changes are stored permanently.

    Parameters:
        filename (str): Name of the file where product data will be saved.
        products (list): List of dictionaries containing product information.

    Variables:
        file (file object): Used to write data into the file.
        product (dict): Stores one product dictionary.
        line (str): Formatted string written into the text file.

    Returns:
        None

    Raises:
        Handles general exceptions during file writing.
    """

    try:
        # Open the file in write mode (overwrites old content)
        with open(filename, "w") as file:

            # Loop through every product dictionary
            for product in products:

                # Convert dictionary back into comma-separated text format
                line = (
                    product["name"] + "," +
                    product["brand"] + "," +
                    str(product["quantity"]) + "," +
                    str(int(product["cost_price"])) + "," +
                    product["country"] + "\n"
                )

                # Write the line into the file
                file.write(line)

    except:
        print("Error saving products.\n")