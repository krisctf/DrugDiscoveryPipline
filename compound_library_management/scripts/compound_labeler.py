# compound_labeler.py

import argparse
import csv
import uuid

def label_compounds(input_file, output_file):
    """
    Label compounds with unique identifiers.

    Args:
        input_file (str): The path to the input CSV file containing compound data.
        output_file (str): The path to the output CSV file with labeled compounds.

    Returns:
        None
    """
    try:
        # Open the input CSV file
        with open(input_file, 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)

            # Create a list to store labeled compounds
            labeled_compounds = []

            for row in reader:
                # Generate a unique compound label (e.g., using UUID)
                compound_id = str(uuid.uuid4())
                
                # Add the unique label to the compound data
                row['Compound_ID'] = compound_id
                
                # Append the labeled compound to the list
                labeled_compounds.append(row)

        # Write the labeled compounds to the output CSV file
        with open(output_file, 'w', newline='') as csvfile:
            fieldnames = labeled_compounds[0].keys()
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            # Write header
            writer.writeheader()

            # Write labeled compounds
            writer.writerows(labeled_compounds)

        print(f"Compounds labeled and saved to {output_file}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

def main():
    parser = argparse.ArgumentParser(description='Label compounds with unique identifiers.')
    parser.add_argument('input_file', type=str, help='Path to the input CSV file containing compound data')
    parser.add_argument('output_file', type=str, help='Path to the output CSV file with labeled compounds')
    args = parser.parse_args()

    label_compounds(args.input_file, args.output_file)

if __name__ == "__main__":
    main()

'''
This script defines a function label_compounds that reads compound data from an input CSV file, generates unique labels for each compound using UUID, adds the labels to the compound data, and then writes the labeled compounds to an output CSV file.

To use this script, you can run it from the command line, providing the paths to the input and output CSV files. For example:

python compound_labeler.py input_compounds.csv labeled_compounds.csv

'''
