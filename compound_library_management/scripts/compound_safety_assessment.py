# compound_safety_assessment.py

import argparse

def perform_safety_assessment(compound_id, compound_name, hazard_data, toxicity_data):
    """
    Perform safety assessment of a compound based on hazard and toxicity data.

    Args:
        compound_id (str): The unique identifier of the compound.
        compound_name (str): The name of the compound.
        hazard_data (str): Hazard data or information.
        toxicity_data (str): Toxicity data or information.

    Returns:
        None
    """
    try:
        # Example safety assessment logic
        safety_score = 0

        # Analyze hazard data
        if "flammable" in hazard_data.lower():
            safety_score -= 1
        if "explosive" in hazard_data.lower():
            safety_score -= 2

        # Analyze toxicity data
        if "high toxicity" in toxicity_data.lower():
            safety_score -= 2
        if "moderate toxicity" in toxicity_data.lower():
            safety_score -= 1

        # Determine safety assessment based on the safety score
        if safety_score >= 0:
            print(f"Safety assessment for Compound ID {compound_id} ({compound_name}):")
            print("Safe for handling and storage.")
        else:
            print(f"Safety assessment for Compound ID {compound_id} ({compound_name}):")
            print("Caution: Follow safety protocols and storage guidelines.")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

def main():
    parser = argparse.ArgumentParser(description='Perform safety assessment of a compound.')
    parser.add_argument('compound_id', type=str, help='Unique identifier of the compound')
    parser.add_argument('compound_name', type=str, help='Name of the compound')
    parser.add_argument('hazard_data', type=str, help='Hazard data or information')
    parser.add_argument('toxicity_data', type=str, help='Toxicity data or information')
    args = parser.parse_args()

    # Call the perform_safety_assessment function with the provided arguments
    perform_safety_assessment(args.compound_id, args.compound_name, args.hazard_data, args.toxicity_data)

if __name__ == "__main__":
    main()


'''
This script defines a function perform_safety_assessment that simulates a safety assessment of a compound based on provided hazard and toxicity data. In this example, it calculates a safety score based on hazard and toxicity information and provides a safety assessment based on the score. You can customize and expand the assessment logic and criteria to match your specific safety assessment requirements.

To use this script, you can run it from the command line, providing the compound ID, compound name, hazard data, and toxicity data as arguments. For example:

python compound_safety_assessment.py compound123 "Compound X" "Flammable, Oxidizing" "High Toxicity"
'''
