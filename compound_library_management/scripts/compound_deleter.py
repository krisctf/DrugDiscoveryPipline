# compound_deleter.py

import argparse
import csv

def delete_compound(input_file, output_file, compound_id):
    """
    Delete a compound from the library.

    Args:
        input_file (str): The path to the input CSV file containing compound data.
        output_file (str): The path to the output CSV file with the deleted compound removed.
        compound_id (str): The unique identifier of the compound to be deleted.

    Returns:
        None
    """
    try:
        # Open the input CSV file
        with open(input_file, 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)

            # Create a list to store compound data without the deleted compound
            updated_compounds = []

            for row in reader:
                if row['Compound_ID'] != compound_id:
                    updated_compounds.append(row)

        # Write the updated compound data to the output CSV file
        with open(output_file, 'w', newline='') as csvfile:
            fieldnames = updated_compounds[0].keys()
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            # Write header
            writer.writeheader()

            # Write updated compound data
            writer.writerows(updated_compounds)

        print(f"Compound deleted and saved to {output_file}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

def main():
    parser = argparse.ArgumentParser(description='Delete a compound from the library.')
    parser.add_argument('input_file', type=str, help='Path to the input CSV file containing compound data')
    parser.add_argument('output_file', type=str, help='Path to the output CSV file with the deleted compound removed')
    parser.add_argument('compound_id', type=str, help='Unique identifier of the compound to be deleted')
    args = parser.parse_args()

    # Call the delete_compound function with the provided arguments
    delete_compound(args.input_file, args.output_file, args.compound_id)

if __name__ == "__main__":
    main()


'''
This script defines a function delete_compound that reads compound data from an input CSV file, deletes the specified compound based on the provided unique identifier, and writes the updated compound data to an output CSV file without the deleted compound.

To use this script, you can run it from the command line, providing the paths to the input and output CSV files and the unique identifier of the compound you want to delete. For example:

python compound_deleter.py input_compounds.csv updated_compounds.csv compound123
'''
