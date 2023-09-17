# compound_archive_manager.py

import argparse
import os
import shutil
import datetime

def archive_compound(compound_id, source_directory, archive_directory):
    """
    Archive a compound by moving it from the source directory to the archive directory.

    Args:
        compound_id (str): The unique identifier of the compound to be archived.
        source_directory (str): The path to the source directory containing the compound data.
        archive_directory (str): The path to the archive directory where the compound will be stored.

    Returns:
        None
    """
    try:
        # Check if the compound directory exists in the source directory
        compound_directory = os.path.join(source_directory, compound_id)
        if not os.path.exists(compound_directory):
            print(f"Compound ID {compound_id} does not exist in the source directory.")
            return

        # Create the archive directory if it doesn't exist
        if not os.path.exists(archive_directory):
            os.makedirs(archive_directory)

        # Generate a timestamp for archiving
        timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')

        # Create a unique directory name in the archive directory using the timestamp
        archive_subdirectory = os.path.join(archive_directory, f"{compound_id}_{timestamp}")

        # Move the compound directory to the archive subdirectory
        shutil.move(compound_directory, archive_subdirectory)

        print(f"Compound ID {compound_id} archived to {archive_subdirectory}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

def main():
    parser = argparse.ArgumentParser(description='Archive a compound by moving it to the archive directory.')
    parser.add_argument('compound_id', type=str, help='Unique identifier of the compound to be archived')
    parser.add_argument('source_directory', type=str, help='Path to the source directory containing the compound data')
    parser.add_argument('archive_directory', type=str, help='Path to the archive directory for storing archived compounds')
    args = parser.parse_args()

    # Call the archive_compound function with the provided arguments
    archive_compound(args.compound_id, args.source_directory, args.archive_directory)

if __name__ == "__main__":
    main()


'''
This script defines a function archive_compound that archives a compound by moving its directory from the source directory to the archive directory. It generates a timestamp to create a unique subdirectory within the archive directory for each archived compound.

To use this script, you can run it from the command line, providing the compound ID, source directory path, and archive directory path. For example:

python compound_archive_manager.py compound123 /path/to/source_directory /path/to/archive_directory
'''
