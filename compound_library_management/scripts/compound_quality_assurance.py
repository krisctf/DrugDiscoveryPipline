# compound_quality_assurance.py

import argparse

def perform_quality_assurance(compound_id, compound_name, purity, stability, assay_result):
    """
    Perform quality assurance checks on a compound.

    Args:
        compound_id (str): The unique identifier of the compound.
        compound_name (str): The name of the compound.
        purity (float): The purity of the compound (percentage).
        stability (str): The stability status of the compound.
        assay_result (str): The assay result (e.g., pass, fail).

    Returns:
        None
    """
    try:
        # Example quality assurance checks
        if purity >= 95.0:
            print(f"Quality check passed for Compound ID {compound_id} ({compound_name}):")
            print(f"Purity: {purity}%")
            print(f"Stability: {stability}")
            print(f"Assay Result: {assay_result}")
        else:
            print(f"Quality check failed for Compound ID {compound_id} ({compound_name}):")
            print(f"Purity below threshold: {purity}%")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

def main():
    parser = argparse.ArgumentParser(description='Perform quality assurance checks on a compound.')
    parser.add_argument('compound_id', type=str, help='Unique identifier of the compound')
    parser.add_argument('compound_name', type=str, help='Name of the compound')
    parser.add_argument('purity', type=float, help='Purity of the compound (percentage)')
    parser.add_argument('stability', type=str, help='Stability status of the compound')
    parser.add_argument('assay_result', type=str, help='Assay result (e.g., pass, fail)')
    args = parser.parse_args()

    # Call the perform_quality_assurance function with the provided arguments
    perform_quality_assurance(args.compound_id, args.compound_name, args.purity, args.stability, args.assay_result)

if __name__ == "__main__":
    main()


'''
This script defines a function perform_quality_assurance that simulates quality assurance checks on a compound based on provided criteria, such as purity, stability, and assay results. In this example, it performs a simple check based on purity, but you can customize and expand the checks to match your specific quality assurance requirements.

To use this script, you can run it from the command line, providing the compound ID, compound name, purity, stability status, and assay result. For example:

python compound_quality_assurance.py compound123 "Compound X" 98.5 "Stable" "Pass"
'''
