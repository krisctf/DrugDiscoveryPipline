# compound_data_analyzer.py

import argparse
import csv
import statistics

def analyze_compound_data(data_file):
    """
    Analyze compound data from a CSV file.

    Args:
        data_file (str): The path to the CSV file containing compound data.

    Returns:
        None
    """
    try:
        # Read data from the CSV file
        with open(data_file, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            data = list(reader)

        # Perform data analysis
        if not data:
            print("No data found in the file.")
            return

        # Example analysis: Calculate mean and standard deviation of a numeric field
        numeric_field = 'Molecular_Weight'  # Change this to the field you want to analyze
        numeric_values = [float(entry[numeric_field]) for entry in data if entry.get(numeric_field)]

        if numeric_values:
            mean_value = statistics.mean(numeric_values)
            stdev_value = statistics.stdev(numeric_values)

            print(f"Data Analysis for '{numeric_field}':")
            print(f"Mean: {mean_value:.2f}")
            print(f"Standard Deviation: {stdev_value:.2f}")
        else:
            print(f"No valid data found for field '{numeric_field}'.")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

def main():
    parser = argparse.ArgumentParser(description='Analyze compound data from a CSV file.')
    parser.add_argument('data_file', type=str, help='Path to the CSV file containing compound data')
    args = parser.parse_args()

    # Call the analyze_compound_data function with the provided arguments
    analyze_compound_data(args.data_file)

if __name__ == "__main__":
    main()


'''
This script defines a function analyze_compound_data that reads compound data from a CSV file and performs basic data analysis. In this example, it calculates the mean and standard deviation of a specified numeric field (e.g., "Molecular_Weight"), but you can customize the analysis logic to fit your specific requirements.

To use this script, you can run it from the command line, providing the path to the CSV file containing the compound data. For example:

python compound_data_analyzer.py compound_data.csv
'''
