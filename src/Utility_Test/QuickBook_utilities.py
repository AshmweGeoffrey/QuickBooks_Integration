from quickbooks import QuickBooks
from intuitlib.client import AuthClient
from typing import Optional
import json
from src.Utility_Test.date_test import *
from src.Utility_Test.formated_print import *
from src.Utility_Test.Attachement_utils import *

# Your QuickBooks API credentials
CLIENT_ID = os.environ.get('CLIENT_ID')
CLIENT_SECRET = os.environ.get('CLIENT_SECRET')
REALM_ID = os.environ.get('REALM_ID')
REFRESH_TOKEN = os.environ.get('REFRESH_TOKEN')

def connect_to_quickbooks() -> Optional[QuickBooks]:
    """
    Establish a connection to QuickBooks.

    Returns:
        Optional[QuickBooks]: The QuickBooks client instance or None if the connection fails.
    """
    try:
        # Create QuickBooks client
        auth_client = AuthClient(
            client_id=CLIENT_ID,
            client_secret=CLIENT_SECRET,
            environment='sandbox',
            redirect_uri='http://localhost:8080',
        )
        qb_client = QuickBooks(
            auth_client=auth_client,
            refresh_token=REFRESH_TOKEN,
            company_id=REALM_ID,
        )
        return qb_client
    except Exception as e:
        print(f"Error connecting to QuickBooks: {e}")
        return None

def get_recent_transactions(start_date: str, end_date: str, amount: float, file_name: str) -> None:
    """
    Retrieve recent transactions from QuickBooks within a specified date range and amount.

    Args:
        start_date (str): The start date for the transaction query in 'YYYY-MM-DD' format.
        end_date (str): The end date for the transaction query in 'YYYY-MM-DD' format.
        amount (float): The total amount to filter transactions.
        file_name (str): The path to the PDF file to upload as an attachment.
    """
    qb_client = connect_to_quickbooks()
    if qb_client is None:
        print("Failed to connect to QuickBooks. Exiting function.")
        return

    transaction_types = ['Invoice']  # Invoice Transactions

    for transaction_type in transaction_types:
        query = f"""
        SELECT * FROM Invoice 
        WHERE TxnDate >= '{start_date}' 
        AND TxnDate <= '{end_date}' 
        AND TotalAmt = '{amount}' 
        ORDER BY TxnDate
        """
        data = qb_client.query(query)
        print("Initiating Connection to QuickBooks...")
        print(f"Recent {transaction_type} Transactions:")

        if data.get('QueryResponse', {}).get('Invoice'):
            invoice_id = data['QueryResponse']['Invoice'][0]['Id']
            upload_invoice_pdf(qb_client, invoice_id, file_name)
            print_invoices(data)
            print("Checking Attachments:")
            print(check_invoice_attachments(invoice_id, qb_client))
        else:
            print(f"No {transaction_type} transactions found.")
        
        print("\n")
        print("---------------------------------------------------")