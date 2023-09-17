# compound_dilution_calculator.py

import argparse

def calculate_dilution(volume_initial, concentration_initial, volume_final, concentration_final):
    """
    Calculate the dilution parameters for a compound.

    Args:
        volume_initial (float): The initial volume of the compound.
        concentration_initial (float): The initial concentration of the compound.
        volume_final (float): The final desired volume after dilution.
        concentration_final (float): The final desired concentration after dilution.

    Returns:
        dict: A dictionary containing the calculated parameters (dilution factor and added solvent volume).
    """
    try:
        # Calculate the dilution factor
        dilution_factor = concentration_initial / concentration_final

        # Calculate the volume of solvent to be added
        volume_solvent_added = volume_final - (volume_initial / dilution_factor)

        # Prepare the results as a dictionary
        dilution_parameters = {
            'Dilution_Factor': dilution_factor,
            'Volume_Solvent_Added': volume_solvent_added
        }

        return dilution_parameters

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None

def main():
    parser = argparse.ArgumentParser(description='Calculate dilution parameters for a compound.')
    parser.add_argument('volume_initial', type=float, help='Initial volume of the compound (in units, e.g., mL)')
    parser.add_argument('concentration_initial', type=float, help='Initial concentration of the compound (in units/volume, e.g., mg/mL)')
    parser.add_argument('volume_final', type=float, help='Final desired volume after dilution (in units, e.g., mL)')
    parser.add_argument('concentration_final', type=float, help='Final desired concentration after dilution (in units/volume, e.g., mg/mL)')
    args = parser.parse_args()

    # Call the calculate_dilution function with the provided arguments
    dilution_params = calculate_dilution(args.volume_initial, args.concentration_initial, args.volume_final, args.concentration_final)

    if dilution_params:
        print("Dilution Parameters:")
        for key, value in dilution_params.items():
            print(f"{key}: {value}")
    else:
        print("Dilution calculation failed.")

if __name__ == "__main__":
    main()


'''
This script defines a function calculate_dilution that calculates the dilution parameters (dilution factor and added solvent volume) for a compound based on the initial volume, initial concentration, final desired volume, and final desired concentration. It returns the results as a dictionary.

To use this script, you can run it from the command line, providing the values for the initial volume, initial concentration, final volume, and final concentration of the compound you want to dilute. For example:

python compound_dilution_calculator.py 10.0 100.0 50.0 10.0
'''
