# compound_sharer.py

import argparse
import csv
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def share_compound_data(input_file, compound_id, recipient_email):
    """
    Share compound information with a recipient via email or other means.

    Args:
        input_file (str): The path to the input CSV file containing compound data.
        compound_id (str): The unique identifier of the compound to be shared.
        recipient_email (str): The email address or recipient information.

    Returns:
        None
    """
    try:
        # Open the input CSV file
        with open(input_file, 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                if row['Compound_ID'] == compound_id:
                    # Customize the message body based on the compound data
                    message = MIMEMultipart()
                    message['From'] = 'your_email@example.com'  # Sender's email address
                    message['To'] = recipient_email
                    message['Subject'] = f"Compound Information for {compound_id}"

                    # Customize the email content with compound details
                    message.attach(MIMEText(f"Compound Name: {row['Compound_Name']}\n"
                                            f"Supplier: {row['Supplier']}\n"
                                            f"Category: {row['Category']}\n"
                                            f"Description: {row['Description']}\n", 'plain'))

                    # Send the email (you may need to configure your email server)
                    smtp_server = 'your_smtp_server.com'
                    smtp_port = 587  # Change to your SMTP server's port
                    smtp_username = 'your_username'
                    smtp_password = 'your_password'

                    with smtplib.SMTP(smtp_server, smtp_port) as server:
                        server.starttls()
                        server.login(smtp_username, smtp_password)
                        server.sendmail(message['From'], recipient_email, message.as_string())

                    print(f"Compound information for {compound_id} shared with {recipient_email}")
                    break  # Stop searching after finding the compound

        print("Sharing complete.")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

def main():
    parser = argparse.ArgumentParser(description='Share compound information with a recipient via email or other means.')
    parser.add_argument('input_file', type=str, help='Path to the input CSV file containing compound data')
    parser.add_argument('compound_id', type=str, help='Unique identifier of the compound to be shared')
    parser.add_argument('recipient_email', type=str, help='Email address or recipient information')
    args = parser.parse_args()

    # Call the share_compound_data function with the provided arguments
    share_compound_data(args.input_file, args.compound_id, args.recipient_email)

if __name__ == "__main__":
    main()


'''
This script defines a function share_compound_data that reads compound data from an input CSV file, searches for a compound based on the provided unique identifier, and shares the compound's information with a recipient via email. You can customize the email content, sender information, and configure the SMTP server settings based on your needs.

To use this script, you can run it from the command line, providing the paths to the input CSV file, the unique identifier of the compound you want to share, and the recipient's email address or information. For example:

python compound_sharer.py input_compounds.csv compound123 recipient@example.com
'''
