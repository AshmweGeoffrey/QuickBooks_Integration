from quickbooks import QuickBooks
from intuitlib.client import AuthClient
import json

# Your QuickBooks API credentials
CLIENT_ID = 'ABLKtaxC35XLriSrQvnPf6WE3pFmhIOoS1SKWj057OntyZgbem'
CLIENT_SECRET = 'ctoD0gctxq8AO8wGCk5lnCZD6c8zRJbOao7SXHrt'
REALM_ID = '9341453484647266'
ACCESS_TOKEN = 'eyJlbmMiOiJBMTI4Q0JDLUhTMjU2IiwiYWxnIjoiZGlyIn0..ES-EeotC9rrBQSOVWFn5Xg.50uPeVbba0Afy5e1HutRN_x45qwDVtSThhc_R0mvMXd6BsXBXL4MGA8RlBi_qQoTGyuKSwEiC3ZZ6g3uFC3z1b_o_IKV4D0eEp46fMSot9Ap0_Ab_mSec3D2gYfig0YL6pueVArfNCY7vTxJbL6LJh5wG6wWNSeAA0cbIM7_7Yz8dp7tmzX3wIpNwBaSAKfWNxXGAEa_zzSPJeBZMrLEnyGgzrC_xWYZTfSO1Iv1vCWlKivjal_YwKCbscGO3o1FcsZyXJBesv88ozlgyefpb67ScMIAHhCFum5AxdX5UT3_D5u67iZV0NYg6Al2cIws6ZQiXYqSXc9hL8c5o1oemEmIvkSCuxD-AiYNalCQ0Lp8bDrmHtbvyLwmSD6VVgRwww-Srp9gdLWHh8nqxJTXjQH41oLyR1IZ8Whuy3Dr98QZ4fG1o_mwUY6hhLPXmaP8w9jKyRBbG3k2RuN3WFhnpeHVPJCxpZy0gsuj8u_G9FEJfeHEH3rUWtpDJBskWmHUTXPsqGIyV25vcf_WZ3KGqpdfpnvMqWra_ZvwhDhtMb3g0rcH9wgc-cHr85Pqy0-LsHFqP8Vr0rEMeH7x6Au3Y3FeNEDJjDKbVW3wwXeaiLJKT-xdRbtqYjEjTudEN6jKcInuT7QJZv-UWb6k1nx0p4UR1htGs_hVyj7-BpzI0oIDfqU9fJmnfHFmeMXaF2Tf8AwZpv3vP7zNm2HpoKgsurzkV3Q4g0gnWuNuQ3zxiDgcil8AgLK2mrMpEwQMSMQA.jXE31Rptj-6csnc63K0FOA'
REFRESH_TOKEN = 'AB11740695434vNXHo4GBmFOrDp46cu39i9bz1QMfKNPqOAiqF'

def connect_to_quickbooks():
    """
    Establish a connection to QuickBooks
    """
    try:
        # Create QuickBooks client
        auth_client = AuthClient(
            client_id=CLIENT_ID,  # Use the variable instead of the string
            client_secret=CLIENT_SECRET,  # Use the variable instead of the string
            access_token=ACCESS_TOKEN,  # Use the variable instead of the string
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
        query = "SELECT * FROM Invoice ORDERBY TxnDate DESC MAXRESULTS 1"
        transactions = qb_client.query(query)
        
        print("Connection Successful!")
        print("Recent Transactions:")
        print(transactions)
        '''for transaction in transactions:
            print(f"Date: {transaction.TxnDate}, Amount: {transaction.Amount}")
        return qb_client
    '''
    except Exception as e:
        print(f"Error connecting to QuickBooks: {e}")
        return None

def main():
    # Establish connection
    qb_client = connect_to_quickbooks()
    
    if qb_client:
        # Now you can use qb_client for further operations
        print("QuickBooks client is ready to use!")

if __name__ == "__main__":
    main()
