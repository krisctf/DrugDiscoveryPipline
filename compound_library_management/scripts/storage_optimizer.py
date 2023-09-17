# storage_optimizer.py

import argparse
import csv
import random

def optimize_storage(input_file, output_file, storage_layout):
    """
    Optimize the physical storage of compounds in the library.

    Args:
        input_file (str): The path to the input CSV file containing compound data.
        output_file (str): The path to the output CSV file with optimized storage layout.
        storage_layout (str): The type of storage layout (e.g., random, alphabetical, custom).

    Returns:
        None
    """
    try:
        # Open the input CSV file
        with open(input_file, 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)

            # Read compound data into a list
            compounds = list(reader)

            # Determine the order of compounds in the storage
            if storage_layout == 'random':
                # Randomly shuffle the list of compounds
                random.shuffle(compounds)
            elif storage_layout == 'alphabetical':
                # Sort compounds alphabetically by name
                compounds.sort(key=lambda x: x['Compound_Name'])
            elif storage_layout == 'custom':
                # Implement your custom storage optimization logic here
                # You may need to define a custom function to reorder compounds
                pass
            else:
                print("Invalid storage layout option. Please choose 'random', 'alphabetical', or 'custom'.")
                return

        # Write the optimized storage layout to the output CSV file
        with open(output_file, 'w', newline='') as csvfile:
            fieldnames = compounds[0].keys()
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            # Write header
            writer.writeheader()

            # Write optimized storage layout
            writer.writerows(compounds)

        print(f"Storage optimized and saved to {output_file}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

def main():
    parser = argparse.ArgumentParser(description='Optimize the physical storage of compounds in the library.')
    parser.add_argument('input_file', type=str, help='Path to the input CSV file containing compound data')
    parser.add_argument('output_file', type=str, help='Path to the output CSV file with optimized storage layout')
    parser.add_argument('storage_layout', type=str, help='Type of storage layout (random, alphabetical, custom)')
    args = parser.parse_args()

    optimize_storage(args.input_file, args.output_file, args.storage_layout)

if __name__ == "__main__":
    main()

'''
This script defines a function optimize_storage that reads compound data from an input CSV file, reorders the compounds based on the specified storage layout (random, alphabetical, or custom), and writes the compounds with the optimized storage layout to an output CSV file.

To use this script, you can run it from the command line, providing the paths to the input and output CSV files and the type of storage layout you want to apply. For example:

python storage_optimizer.py input_compounds.csv optimized_layout.csv random
'''
