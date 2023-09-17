# compound_organizer.py

import argparse
import csv

def organize_compounds(input_file, output_file, organization_field):
    """
    Organize compounds in the library based on a specified field.

    Args:
        input_file (str): The path to the input CSV file containing compound data.
        output_file (str): The path to the output CSV file with organized compounds.
        organization_field (str): The field to use for organizing compounds (e.g., "Supplier", "Category").

    Returns:
        None
    """
    try:
        # Open the input CSV file
        with open(input_file, 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)

            # Create a dictionary to group compounds by the specified field
            organized_compounds = {}

            for row in reader:
                field_value = row.get(organization_field, 'Uncategorized')

                if field_value not in organized_compounds:
                    organized_compounds[field_value] = []

                organized_compounds[field_value].append(row)

        # Write the organized compounds to the output CSV file
        with open(output_file, 'w', newline='') as csvfile:
            fieldnames = organized_compounds[list(organized_compounds.keys())[0]][0].keys()
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            # Write header
            writer.writeheader()

            # Write organized compounds
            for field_value, compounds in organized_compounds.items():
                writer.writerows(compounds)

        print(f"Compounds organized and saved to {output_file}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

def main():
    parser = argparse.ArgumentParser(description='Organize compounds in the library based on a specified field.')
    parser.add_argument('input_file', type=str, help='Path to the input CSV file containing compound data')
    parser.add_argument('output_file', type=str, help='Path to the output CSV file with organized compounds')
    parser.add_argument('organization_field', type=str, help='Field to use for organizing compounds (e.g., "Supplier", "Category")')
    args = parser.parse_args()

    # Call the organize_compounds function with the provided arguments
    organize_compounds(args.input_file, args.output_file, args.organization_field)

if __name__ == "__main__":
    main()


'''
This script defines a function organize_compounds that reads compound data from an input CSV file, organizes the compounds based on a specified field (e.g., Supplier or Category), and writes the organized compounds to an output CSV file.

To use this script, you can run it from the command line, providing the paths to the input and output CSV files and the field you want to use for organizing compounds. For example:

python compound_organizer.py input_compounds.csv organized_compounds.csv Supplier
'''
