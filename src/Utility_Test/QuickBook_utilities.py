from quickbooks import QuickBooks
from intuitlib.client import AuthClient
import json
from Utility_Test.date_test import *
from Utility_Test.formated_print import *
from Utility_Test.Attachement_utils import *
import ast
# Your QuickBooks API credentials
CLIENT_ID = 'ABLKtaxC35XLriSrQvnPf6WE3pFmhIOoS1SKWj057OntyZgbem'
CLIENT_SECRET = 'ctoD0gctxq8AO8wGCk5lnCZD6c8zRJbOao7SXHrt'
REALM_ID = '9341453484647266'
REFRESH_TOKEN = 'AB11740853310VcR1qHsMEAWsKjOTHKRcREuF48hnBS34rVAzn'

def connect_to_quickbooks():
    """
    Establish a connection to QuickBooks
    """
    try:
        # Create QuickBooks client
        auth_client = AuthClient(
            client_id=CLIENT_ID,  # Use the variable instead of the string
            client_secret=CLIENT_SECRET,  # Use the variable instead of the string
            #access_token=ACCESS_TOKEN,  # Use the variable instead of the string
            environment='sandbox',
            redirect_uri='http://localhost:8080',
            )
        qb_client = QuickBooks(
            auth_client=auth_client,
            refresh_token=REFRESH_TOKEN,
            company_id=REALM_ID,  # Use the REALM_ID variable
            )        
        # Test connection by fetching some basic info
        # For example, let's try to get some recent transactions
        return qb_client
    except Exception as e:
        print(f"Error connecting to QuickBooks: {e}")
        return None
def get_recent_transactions(start_date,end_date,amount,file_name):
    qb_client = connect_to_quickbooks()
    transaction_types = ['Invoice'   #Invoice Transactions 
                 ]
    for transaction_type in transaction_types:
        query = f"""SELECT * FROM Invoice WHERE TxnDate >= '{start_date}' AND TxnDate <= '{end_date}' AND TotalAmt = '{amount}' ORDER BY TxnDate"""
        data = qb_client.query(query)
        print("Initiating Connection to QuickBooks...")
        print(f"Recent {transaction_type} Transactions:")
        if data['QueryResponse'] != {}:
            invoice_id = data['QueryResponse']['Invoice'][0]['Id']
            upload_invoice_pdf(connect_to_quickbooks(), invoice_id, file_name)
            print_invoices(data)
            print("Checking Attachments:")
            print(check_invoice_attachments(130,connect_to_quickbooks()))
        else:
            print(f"No {transaction_type} transactions found.")
        print("\n")
        print("---------------------------------------------------")