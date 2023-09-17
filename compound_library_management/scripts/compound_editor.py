# compound_editor.py

import argparse
import csv

def edit_compound_details(input_file, output_file, compound_id, new_details):
    """
    Edit the details of a compound in the library.

    Args:
        input_file (str): The path to the input CSV file containing compound data.
        output_file (str): The path to the output CSV file with updated compound data.
        compound_id (str): The unique identifier of the compound to be edited.
        new_details (dict): A dictionary of new compound details.

    Returns:
        None
    """
    try:
        # Open the input CSV file
        with open(input_file, 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)

            # Create a list to store updated compound data
            updated_compounds = []

            for row in reader:
                if row['Compound_ID'] == compound_id:
                    # Update the compound details with new values
                    row.update(new_details)
                updated_compounds.append(row)

        # Write the updated compound data to the output CSV file
        with open(output_file, 'w', newline='') as csvfile:
            fieldnames = updated_compounds[0].keys()
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            # Write header
            writer.writeheader()

            # Write updated compound data
            writer.writerows(updated_compounds)

        print(f"Compound details edited and saved to {output_file}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

def main():
    parser = argparse.ArgumentParser(description='Edit the details of a compound in the library.')
    parser.add_argument('input_file', type=str, help='Path to the input CSV file containing compound data')
    parser.add_argument('output_file', type=str, help='Path to the output CSV file with updated compound data')
    parser.add_argument('compound_id', type=str, help='Unique identifier of the compound to be edited')
    parser.add_argument('--new_name', type=str, help='New name for the compound (optional)')
    parser.add_argument('--new_concentration', type=float, help='New concentration for the compound (optional)')
    # Add more optional arguments for other compound details you want to edit
    args = parser.parse_args()

    # Create a dictionary to hold the new compound details
    new_details = {}
    if args.new_name:
        new_details['Compound_Name'] = args.new_name
    if args.new_concentration:
        new_details['Concentration'] = args.new_concentration
    # Add more key-value pairs for other compound details you want to edit

    # Call the edit_compound_details function with the provided arguments
    edit_compound_details(args.input_file, args.output_file, args.compound_id, new_details)

if __name__ == "__main__":
    main()

'''
This script defines a function edit_compound_details that reads compound data from an input CSV file, edits the details of a specified compound based on the provided unique identifier and new details, and writes the updated compound data to an output CSV file.

To use this script, you can run it from the command line, providing the paths to the input and output CSV files, the unique identifier of the compound to be edited, and optional arguments for the new details you want to update. For example:

python compound_editor.py input_compounds.csv edited_compounds.csv compound123 --new_name "New Compound Name" --new_concentration 2.5
'''
