# compound_exporter.py

import argparse
import csv

def export_compounds(input_file, output_file, export_ids):
    """
    Export compounds from the library.

    Args:
        input_file (str): The path to the input CSV file containing compound data.
        output_file (str): The path to the output CSV file with exported compounds.
        export_ids (list): A list of unique identifiers of compounds to be exported.

    Returns:
        None
    """
    try:
        # Open the input CSV file
        with open(input_file, 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)

            # Create a list to store exported compounds
            exported_compounds = []

            for row in reader:
                if row['Compound_ID'] in export_ids:
                    exported_compounds.append(row)

        # Write the exported compounds to the output CSV file
        with open(output_file, 'w', newline='') as csvfile:
            fieldnames = exported_compounds[0].keys()
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            # Write header
            writer.writeheader()

            # Write exported compounds
            writer.writerows(exported_compounds)

        print(f"Compounds exported and saved to {output_file}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

def main():
    parser = argparse.ArgumentParser(description='Export compounds from the library.')
    parser.add_argument('input_file', type=str, help='Path to the input CSV file containing compound data')
    parser.add_argument('output_file', type=str, help='Path to the output CSV file with exported compounds')
    parser.add_argument('export_ids', nargs='+', type=str, help='List of unique identifiers of compounds to be exported')
    args = parser.parse_args()

    # Call the export_compounds function with the provided arguments
    export_compounds(args.input_file, args.output_file, args.export_ids)

if __name__ == "__main__":
    main()


'''
This script defines a function export_compounds that reads compound data from an input CSV file, exports compounds based on a list of unique identifiers, and writes the exported compounds to an output CSV file.

To use this script, you can run it from the command line, providing the paths to the input and output CSV files and a list of unique identifiers of compounds you want to export. For example:

python compound_exporter.py input_compounds.csv exported_compounds.csv compound123 compound456 compound789
'''
