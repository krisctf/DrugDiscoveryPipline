# supplier_quality_checker.py

import argparse
import csv

def check_supplier_quality(input_file, output_file, threshold_quality):
    """
    Check the quality of compounds from different suppliers.

    Args:
        input_file (str): The path to the input CSV file containing compound data.
        output_file (str): The path to the output CSV file with supplier quality information.
        threshold_quality (float): The minimum quality threshold.

    Returns:
        None
    """
    try:
        # Open the input CSV file
        with open(input_file, 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)

            # Create a list to store compounds with supplier quality information
            compounds_with_quality = []

            for row in reader:
                # Extract supplier and quality information from the data (you'll need to adapt this to your data format)
                supplier = row.get('Supplier', '')
                quality = float(row.get('Quality', 0.0))

                # Check if the quality meets the threshold
                meets_threshold = quality >= threshold_quality

                # Add supplier quality information to the compound data
                row['Meets_Quality_Threshold'] = meets_threshold
                
                # Append the compound with supplier quality information to the list
                compounds_with_quality.append(row)

        # Write compounds with supplier quality information to the output CSV file
        with open(output_file, 'w', newline='') as csvfile:
            fieldnames = compounds_with_quality[0].keys()
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            # Write header
            writer.writeheader()

            # Write compounds with supplier quality information
            writer.writerows(compounds_with_quality)

        print(f"Supplier quality checked and saved to {output_file}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

def main():
    parser = argparse.ArgumentParser(description='Check the quality of compounds from different suppliers.')
    parser.add_argument('input_file', type=str, help='Path to the input CSV file containing compound data')
    parser.add_argument('output_file', type=str, help='Path to the output CSV file with supplier quality information')
    parser.add_argument('threshold_quality', type=float, help='Minimum quality threshold')
    args = parser.parse_args()

    check_supplier_quality(args.input_file, args.output_file, args.threshold_quality)

if __name__ == "__main__":
    main()

'''
This script defines a function check_supplier_quality that reads compound data from an input CSV file, checks the quality of compounds from different suppliers based on a specified threshold, and writes the compounds with supplier quality information to an output CSV file.

To use this script, you can run it from the command line, providing the paths to the input and output CSV files and the minimum quality threshold. For example:

python supplier_quality_checker.py input_compounds.csv supplier_quality_report.csv 0.8
'''
