# compound_audit_trail_logger.py

import argparse
import csv
from datetime import datetime

def log_audit_trail(action, compound_id, user, timestamp, log_file):
    """
    Log an audit trail entry for a compound-related action.

    Args:
        action (str): The description of the action performed (e.g., "Added", "Edited", "Deleted").
        compound_id (str): The unique identifier of the compound.
        user (str): The name or ID of the user who performed the action.
        timestamp (str): The timestamp of the action in YYYY-MM-DD HH:MM:SS format.
        log_file (str): The path to the audit trail log file.

    Returns:
        None
    """
    try:
        # Open the audit trail log file in append mode
        with open(log_file, 'a', newline='') as csvfile:
            fieldnames = ['Timestamp', 'Action', 'Compound_ID', 'User']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            # Write the audit trail entry
            writer.writerow({
                'Timestamp': timestamp,
                'Action': action,
                'Compound_ID': compound_id,
                'User': user
            })

        print(f"Audit trail entry logged for {action} action on Compound ID {compound_id} by {user}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

def main():
    parser = argparse.ArgumentParser(description='Log audit trail entries for compound-related actions.')
    parser.add_argument('action', type=str, help='Description of the action performed (e.g., "Added", "Edited", "Deleted")')
    parser.add_argument('compound_id', type=str, help='Unique identifier of the compound')
    parser.add_argument('user', type=str, help='Name or ID of the user who performed the action')
    parser.add_argument('log_file', type=str, help='Path to the audit trail log file')
    args = parser.parse_args()

    # Get the current timestamp
    current_timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Call the log_audit_trail function with the provided arguments
    log_audit_trail(args.action, args.compound_id, args.user, current_timestamp, args.log_file)

if __name__ == "__main__":
    main()


'''
This script defines a function log_audit_trail that logs audit trail entries for compound-related actions, such as adding, editing, or deleting compounds. It records details such as the action description, compound ID, user, and timestamp in an audit trail log file.

To use this script, you can run it from the command line, providing the action description, compound ID, user, and the path to the audit trail log file. For example:

python compound_audit_trail_logger.py "Added" compound123 "John Doe" audit_trail_log.csv
'''
