# compound_inventory_tracking.py

import argparse
import sqlite3

# Initialize the SQLite database
db_connection = sqlite3.connect('compound_inventory.db')
cursor = db_connection.cursor()

# Create the inventory table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS compound_inventory (
        compound_id TEXT PRIMARY KEY,
        compound_name TEXT,
        quantity INTEGER,
        location TEXT
    )
''')
db_connection.commit()

def update_inventory(compound_id, compound_name, quantity, location):
    """
    Update the inventory for a compound.

    Args:
        compound_id (str): The unique identifier of the compound.
        compound_name (str): The name of the compound.
        quantity (int): The quantity of the compound.
        location (str): The location of the compound in the lab.

    Returns:
        None
    """
    try:
        # Check if the compound already exists in the inventory
        cursor.execute('SELECT * FROM compound_inventory WHERE compound_id = ?', (compound_id,))
        existing_record = cursor.fetchone()

        if existing_record:
            # Update the existing record
            updated_quantity = existing_record[2] + quantity
            cursor.execute('UPDATE compound_inventory SET quantity = ?, location = ? WHERE compound_id = ?',
                           (updated_quantity, location, compound_id))
        else:
            # Insert a new record if the compound doesn't exist
            cursor.execute('INSERT INTO compound_inventory VALUES (?, ?, ?, ?)',
                           (compound_id, compound_name, quantity, location))

        db_connection.commit()
        print(f"Inventory updated for Compound ID {compound_id}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

def main():
    parser = argparse.ArgumentParser(description='Update compound inventory.')
    parser.add_argument('compound_id', type=str, help='Unique identifier of the compound')
    parser.add_argument('compound_name', type=str, help='Name of the compound')
    parser.add_argument('quantity', type=int, help='Quantity to update (positive or negative)')
    parser.add_argument('location', type=str, help='Location of the compound in the lab')
    args = parser.parse_args()

    # Call the update_inventory function with the provided arguments
    update_inventory(args.compound_id, args.compound_name, args.quantity, args.location)

if __name__ == "__main__":
    main()


'''
This script uses an SQLite database to track compound inventory. It defines a function update_inventory that allows you to update the inventory for a compound by adding or subtracting quantities. It also handles adding new compounds to the inventory if they don't already exist.

To use this script, you can run it from the command line, providing the compound ID, compound name, quantity to update (positive or negative), and the location of the compound in the lab. For example:

python compound_inventory_tracking.py compound123 "Compound X" 50 "Lab A, Shelf 1"
'''
