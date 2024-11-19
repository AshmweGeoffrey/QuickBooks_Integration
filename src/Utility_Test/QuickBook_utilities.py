from quickbooks import QuickBooks
from intuitlib.client import AuthClient
import json
from Utility_Test.date_test import *
from Utility_Test.formated_print import *
# Your QuickBooks API credentials
CLIENT_ID = 'ABLKtaxC35XLriSrQvnPf6WE3pFmhIOoS1SKWj057OntyZgbem'
CLIENT_SECRET = 'ctoD0gctxq8AO8wGCk5lnCZD6c8zRJbOao7SXHrt'
REALM_ID = '9341453484647266'
ACCESS_TOKEN = 'eyJlbmMiOiJBMTI4Q0JDLUhTMjU2IiwiYWxnIjoiZGlyIn0..qdyYjfJX4g_3vVdKcx6FzA.zi3i0vZppcFr7zG-670SS-S-P0lJugIXp8xF9jz3Zm-Iz02q8Sfd0_qsLNs1PIgAACJBRRxrmW1fxPJcZujLJoEogkoq-5iTOD2IVmK-rp53UGfbLML-YpGEZeFQ-QzUmFJJh3iBQGGUxSd9ypZn8YGVCFpIdzzRdqmE9vHkgJYmqWOyjNDKLfObZFY4Y2Z5wLqkRPZZonySSCmc3vM_EmOtvbxh5fWhdDjkuIZ7TwaaTCqPxjUAQ-wU55Ujsp549FjU9Hgbm2KJEauIUnAxv1Y7iQ14StOcehh421pc0Oa6dn2-HAKLg7NtROwLhF_BBwvfDp3WS2SLnF2UQ_LwIoAaTGXFDEYoAokADue3MCdkJfLIDAYsBYdGdLNCy-0fr9HGH5ilOB1IxkmnB2iFa8kKQskq1d9y4vCXPtm_6n145HCULQocx7tAxjDwGPCFMT7YQEFAvrGEsRgTbhXc9r8YYfHxp_nZZmXSnEVuYXy1WRb-Yv_U02qNvpjx8-_JPNna5YJJawECw7QY3GBybjm0y6eZqajlL3nvYgTz4tI-6upetHGlzRB28K2vfhucvkHYASCHHdiZ-hyLDOSHrcELbjvV57-xm4fImVnZ2Ln2_y3NYYXEW7uNbd240zWD6nAt8CKw2O6htPR594Th2bNFby-4qtKusxXVlPbpL6WREZI3bvLZaZGUdjL59MPzv8nfPpMUszr80xnVAkS0K2Sf68L24VIZNIFQ8AScG9VwcwPowdTO2v6H_eoopynH.-2d8zsyoPKsAmI-gRx8u7g'
REFRESH_TOKEN = 'AB11740763363Bz5jpxFD2X57txULRm3WlnOr5Tkn4KCTspUq8'

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
        print("Connection Successful!")
        return qb_client
    except Exception as e:
        print(f"Error connecting to QuickBooks: {e}")
        return None
def get_recent_transactions(start_date,end_date,amount):
    qb_client = connect_to_quickbooks()
    transaction_types = ['Invoice'   #Invoice Transactions 
                 ]
    for transaction_type in transaction_types:
        query = f"""SELECT * FROM Invoice WHERE TxnDate >= '{start_date}' AND TxnDate <= '{end_date}' AND TotalAmt = '{amount}' ORDER BY TxnDate"""
        data = qb_client.query(query)
        print(f"Recent {transaction_type} Transactions:")
        if data['QueryResponse'] != {}:
            print_invoices(data)
        else:
            print(f"No {transaction_type} transactions found.")
        print("\n")
        print("---------------------------------------------------")