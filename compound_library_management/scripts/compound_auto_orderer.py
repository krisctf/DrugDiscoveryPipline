# compound_auto_orderer.py

import argparse
import requests
import json

def auto_order_compound(compound_id, supplier_api_url, order_quantity):
    """
    Automate the ordering of a compound from a supplier's API.

    Args:
        compound_id (str): The unique identifier of the compound to be ordered.
        supplier_api_url (str): The URL of the supplier's API for placing orders.
        order_quantity (int): The quantity of the compound to order.

    Returns:
        None
    """
    try:
        # Prepare the order data
        order_data = {
            'compound_id': compound_id,
            'quantity': order_quantity
        }

        # Send a POST request to the supplier's API to place the order
        response = requests.post(supplier_api_url, json=order_data)

        if response.status_code == 200:
            print(f"Order for Compound ID {compound_id} placed successfully.")
        else:
            print(f"Order placement failed with status code {response.status_code}.")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

def main():
    parser = argparse.ArgumentParser(description='Automate the ordering of a compound from a supplier.')
    parser.add_argument('compound_id', type=str, help='Unique identifier of the compound to be ordered')
    parser.add_argument('supplier_api_url', type=str, help='URL of the supplier\'s API for placing orders')
    parser.add_argument('order_quantity', type=int, help='Quantity of the compound to order')
    args = parser.parse_args()

    # Call the auto_order_compound function with the provided arguments
    auto_order_compound(args.compound_id, args.supplier_api_url, args.order_quantity)

if __name__ == "__main__":
    main()

'''
This script defines a function auto_order_compound that automates the ordering of a compound by sending a POST request to a supplier's API with the compound ID and order quantity as parameters.

To use this script, you can run it from the command line, providing the compound ID, supplier's API URL, and the quantity of the compound you want to order. For example:

python compound_auto_orderer.py compound123 https://supplier-api.com/place_order 10
'''
