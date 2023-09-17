# shelf_life_checker.py

import argparse
import csv
from datetime import datetime

def check_shelf_life(input_file, output_file, current_date):
    """
    Check the shelf life of compounds in the library.

    Args:
        input_file (str): The path to the input CSV file containing compound data.
        output_file (str): The path to the output CSV file with shelf life information.
        current_date (str): The current date in YYYY-MM-DD format.

    Returns:
        None
    """
    try:
        # Open the input CSV file
        with open(input_file, 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)

            # Create a list to store compounds with shelf life information
            compounds_with_shelf_life = []

            for row in reader:
                # Extract the compound's expiration date from the data (you'll need to adapt this to your data format)
                expiration_date_str = row.get('Expiration_Date', '')

                # Convert the expiration date string to a datetime object (you'll need to adapt this based on your date format)
                try:
                    expiration_date = datetime.strptime(expiration_date_str, '%Y-%m-%d')
                except ValueError:
                    expiration_date = None

                # Calculate the remaining shelf life in days
                remaining_shelf_life = (expiration_date - datetime.strptime(current_date, '%Y-%m-%d')).days if expiration_date else None

                # Add shelf life information to the compound data
                row['Remaining_Shelf_Life_Days'] = remaining_shelf_life
                
                # Append the compound with shelf life information to the list
                compounds_with_shelf_life.append(row)

        # Write compounds with shelf life information to the output CSV file
        with open(output_file, 'w', newline='') as csvfile:
            fieldnames = compounds_with_shelf_life[0].keys()
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            # Write header
            writer.writeheader()

            # Write compounds with shelf life information
            writer.writerows(compounds_with_shelf_life)

        print(f"Shelf life checked and saved to {output_file}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

def main():
    parser = argparse.ArgumentParser(description='Check the shelf life of compounds in the library.')
    parser.add_argument('input_file', type=str, help='Path to the input CSV file containing compound data')
    parser.add_argument('output_file', type=str, help='Path to the output CSV file with shelf life information')
    parser.add_argument('current_date', type=str, help='Current date in YYYY-MM-DD format')
    args = parser.parse_args()

    check_shelf_life(args.input_file, args.output_file, args.current_date)

if __name__ == "__main__":
    main()

'''
This script defines a function check_shelf_life that reads compound data from an input CSV file, calculates the remaining shelf life of each compound based on the current date, and writes the compounds with shelf life information to an output CSV file.

To use this script, you can run it from the command line, providing the paths to the input and output CSV files and the current date in YYYY-MM-DD format. For example:

python shelf_life_checker.py input_compounds.csv shelf_life_report.csv 2023-09-15
'''
