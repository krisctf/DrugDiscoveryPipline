# compound_vial_label_printer.py

import argparse

def print_vial_label(compound_id, quantity, printer_name):
    """
    Print a vial label for a compound.

    Args:
        compound_id (str): The unique identifier of the compound.
        quantity (int): The quantity of vials to print labels for.
        printer_name (str): The name of the printer to use for label printing.

    Returns:
        None
    """
    try:
        # Customize label content and format here based on your label printing system
        label_content = f"Compound ID: {compound_id}\nQuantity: {quantity}\n"

        # Print the label using the specified printer
        print(f"Printing {quantity} vial label(s) for Compound ID {compound_id} on printer: {printer_name}")
        # Add code here to send label_content to the printer

        print("Label printing completed.")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

def main():
    parser = argparse.ArgumentParser(description='Print vial labels for compounds.')
    parser.add_argument('compound_id', type=str, help='Unique identifier of the compound')
    parser.add_argument('quantity', type=int, help='Quantity of vials to print labels for')
    parser.add_argument('printer_name', type=str, help='Name of the printer for label printing')
    args = parser.parse_args()

    # Call the print_vial_label function with the provided arguments
    print_vial_label(args.compound_id, args.quantity, args.printer_name)

if __name__ == "__main__":
    main()


'''
This script defines a function print_vial_label that generates label content based on the provided compound ID and quantity, and sends the label content to the specified printer for printing. You'll need to customize the label content and printing logic to match your label printing system and format.

To use this script, you can run it from the command line, providing the compound ID, quantity of vials to print labels for, and the name of the printer you want to use. For example:

python compound_vial_label_printer.py compound123 10 "MyLabelPrinter"
'''
