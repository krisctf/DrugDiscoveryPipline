# compound_retriever.py

import argparse
import csv

def retrieve_compound_info(input_file, compound_id):
    """
    Retrieve information about a compound from the library.

    Args:
        input_file (str): The path to the input CSV file containing compound data.
        compound_id (str): The unique identifier of the compound to be retrieved.

    Returns:
        dict or None: A dictionary containing the details of the retrieved compound if found, else None.
    """
    try:
        # Open the input CSV file
        with open(input_file, 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                if row['Compound_ID'] == compound_id:
                    # Return the details of the found compound as a dictionary
                    return dict(row)

        # If the compound was not found, return None
        return None

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None

def main():
    parser = argparse.ArgumentParser(description='Retrieve information about a compound from the library.')
    parser.add_argument('input_file', type=str, help='Path to the input CSV file containing compound data')
    parser.add_argument('compound_id', type=str, help='Unique identifier of the compound to be retrieved')
    args = parser.parse_args()

    # Call the retrieve_compound_info function with the provided arguments
    compound_info = retrieve_compound_info(args.input_file, args.compound_id)

    if compound_info:
        print("Compound information:")
        for key, value in compound_info.items():
            print(f"{key}: {value}")
    else:
        print("Compound not found in the library.")

if __name__ == "__main__":
    main()


'''
This script defines a function retrieve_compound_info that reads compound data from an input CSV file, searches for a compound based on the provided unique identifier, and returns the details of the found compound as a dictionary. If the compound is not found, it returns None.

To use this script, you can run it from the command line, providing the path to the input CSV file and the unique identifier of the compound you want to retrieve. For example:

python compound_retriever.py input_compounds.csv compound123
'''
