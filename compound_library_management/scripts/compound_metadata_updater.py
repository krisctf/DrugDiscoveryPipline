# compound_metadata_updater.py

import argparse
import csv

def update_compound_metadata(compound_id, metadata_file, updated_metadata):
    """
    Update metadata for a compound in the metadata file.

    Args:
        compound_id (str): The unique identifier of the compound to be updated.
        metadata_file (str): The path to the metadata file containing compound metadata.
        updated_metadata (dict): A dictionary containing the updated metadata for the compound.

    Returns:
        None
    """
    try:
        # Read the existing metadata from the metadata file
        with open(metadata_file, 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            metadata_list = list(reader)

        # Find the compound entry to update based on the compound_id
        updated = False
        for metadata in metadata_list:
            if metadata['Compound_ID'] == compound_id:
                metadata.update(updated_metadata)
                updated = True
                break

        # Write the updated metadata back to the metadata file
        if updated:
            with open(metadata_file, 'w', newline='') as csvfile:
                fieldnames = metadata_list[0].keys()
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

                # Write header
                writer.writeheader()

                # Write updated metadata
                writer.writerows(metadata_list)

            print(f"Metadata updated for Compound ID {compound_id}")
        else:
            print(f"Compound ID {compound_id} not found in the metadata file.")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

def main():
    parser = argparse.ArgumentParser(description='Update metadata for a compound in the metadata file.')
    parser.add_argument('compound_id', type=str, help='Unique identifier of the compound to be updated')
    parser.add_argument('metadata_file', type=str, help='Path to the metadata file containing compound metadata')
    parser.add_argument('--metadata_key', type=str, help='Name of the metadata field to update')
    parser.add_argument('--metadata_value', type=str, help='Value to set for the metadata field')
    args = parser.parse_args()

    # Check if both metadata_key and metadata_value are provided
    if args.metadata_key and args.metadata_value:
        updated_metadata = {args.metadata_key: args.metadata_value}
        # Call the update_compound_metadata function with the provided arguments
        update_compound_metadata(args.compound_id, args.metadata_file, updated_metadata)
    else:
        print("Both --metadata_key and --metadata_value must be provided for updating metadata.")

if __name__ == "__main__":
    main()


'''
This script defines a function update_compound_metadata that reads compound metadata from a metadata file, updates the metadata for a specified compound based on its unique identifier (Compound_ID), and writes the updated metadata back to the file.

To use this script, you can run it from the command line, providing the compound ID, metadata file path, metadata key (field name), and metadata value you want to update. For example:

python compound_metadata_updater.py compound123 metadata.csv --metadata_key "Description" --metadata_value "Updated description"
'''
