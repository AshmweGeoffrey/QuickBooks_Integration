from intuitlib.client import AuthClient
from quickbooks import QuickBooks
from quickbooks.objects.customer import Customer
from quickbooks.objects.invoice import Invoice
from quickbooks.objects.item import Item
from quickbooks.exceptions import QuickbooksException

import logging
from datetime import datetime

# Configuration
CLIENT_ID = 'ABLKtaxC35XLriSrQvnPf6WE3pFmhIOoS1SKWj057OntyZgbem'
CLIENT_SECRET = 'ctoD0gctxq8AO8wGCk5lnCZD6c8zRJbOao7SXHrt'
REALM_ID = '9341453484647266'
ACCESS_TOKEN = 'eyJlbmMiOiJBMTI4Q0JDLUhTMjU2IiwiYWxnIjoiZGlyIn0..ES-EeotC9rrBQSOVWFn5Xg.50uPeVbba0Afy5e1HutRN_x45qwDVtSThhc_R0mvMXd6BsXBXL4MGA8RlBi_qQoTGyuKSwEiC3ZZ6g3uFC3z1b_o_IKV4D0eEp46fMSot9Ap0_Ab_mSec3D2gYfig0YL6pueVArfNCY7vTxJbL6LJh5wG6wWNSeAA0cbIM7_7Yz8dp7tmzX3wIpNwBaSAKfWNxXGAEa_zzSPJeBZMrLEnyGgzrC_xWYZTfSO1Iv1vCWlKivjal_YwKCbscGO3o1FcsZyXJBesv88ozlgyefpb67ScMIAHhCFum5AxdX5UT3_D5u67iZV0NYg6Al2cIws6ZQiXYqSXc9hL8c5o1oemEmIvkSCuxD-AiYNalCQ0Lp8bDrmHtbvyLwmSD6VVgRwww-Srp9gdLWHh8nqxJTXjQH41oLyR1IZ8Whuy3Dr98QZ4fG1o_mwUY6hhLPXmaP8w9jKyRBbG3k2RuN3WFhnpeHVPJCxpZy0gsuj8u_G9FEJfeHEH3rUWtpDJBskWmHUTXPsqGIyV25vcf_WZ3KGqpdfpnvMqWra_ZvwhDhtMb3g0rcH9wgc-cHr85Pqy0-LsHFqP8Vr0rEMeH7x6Au3Y3FeNEDJjDKbVW3wwXeaiLJKT-xdRbtqYjEjTudEN6jKcInuT7QJZv-UWb6k1nx0p4UR1htGs_hVyj7-BpzI0oIDfqU9fJmnfHFmeMXaF2Tf8AwZpv3vP7zNm2HpoKgsurzkV3Q4g0gnWuNuQ3zxiDgcil8AgLK2mrMpEwQMSMQA.jXE31Rptj-6csnc63K0FOA'
REFRESH_TOKEN = 'AB11740695434vNXHo4GBmFOrDp46cu39i9bz1QMfKNPqOAiqF'

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class QuickBooksDataExplorer:
    def __init__(self):
        # Set up authentication client
        self.auth_client = AuthClient(
            client_id=CLIENT_ID,
            client_secret=CLIENT_SECRET,
            environment='sandbox',
            redirect_uri='http://localhost:8000/callback'
        )

        # Create QuickBooks client
        self.client = QuickBooks(
            auth_client=self.auth_client,
            refresh_token=REFRESH_TOKEN,
            company_id=REALM_ID  # Changed from COMPANY_ID to REALM_ID
        )

    def explore_customers(self, limit=50):
        """Retrieve and explore customer data"""
        try:
            # Retrieve customers with various filters
            customers = Customer.filter(
                qb=self.client,
                max_results=limit, 
                Active=True
            )

            # Detailed customer exploration
            customer_details = []
            for customer in customers:
                customer_info = {
                    'id': customer.Id,
                    'name': customer.DisplayName,
                    'email': getattr(customer, 'PrimaryEmailAddr', {}).get('Address') if hasattr(customer, 'PrimaryEmailAddr') else None,
                    'balance': getattr(customer, 'Balance', 0),
                    'is_active': customer.Active
                }
                customer_details.append(customer_info)

            return customer_details

        except QuickbooksException as e:
            logger.error(f"QuickBooks Customer Retrieval Error: {e}")
            return []

    def explore_invoices(self, limit=50):
        """Retrieve and explore invoice data"""
        try:
            # Retrieve invoices with various options
            invoices = Invoice.filter(
                qb=self.client,
                max_results=limit, 
                order_by='TxnDate DESC'
            )

            # Detailed invoice exploration
            invoice_details = []
            for invoice in invoices:
                invoice_info = {
                    'id': invoice.Id,
                    'customer_id': invoice.CustomerRef.value if hasattr(invoice, 'CustomerRef') else None,
                    'total_amount': invoice.TotalAmt,
                    'transaction_date': invoice.TxnDate,
                    'status': invoice.Status if hasattr(invoice, 'Status') else 'Unknown'
                }
                invoice_details.append(invoice_info)

            return invoice_details

        except QuickbooksException as e:
            logger.error(f"QuickBooks Invoice Retrieval Error: {e}")
            return []

    def explore_items(self, limit=50):
        """Retrieve and explore item data"""
        try:
            # Retrieve items
            items = Item.filter(
                qb=self.client,
                max_results=limit
            )

            # Detailed item exploration
            item_details = []
            for item in items:
                item_info = {
                    'id': item.Id,
                    'name': item.Name,
                    'type': item.Type,
                    'unit_price': item.UnitPrice if hasattr(item, 'UnitPrice') else None,
                    'is_active': item.Active if hasattr(item, 'Active') else True
                }
                item_details.append(item_info)

            return item_details

        except QuickbooksException as e:
            logger.error(f"QuickBooks Item Retrieval Error: {e}")
            return []

    def perform_comprehensive_analysis(self):
        """Comprehensive data exploration and analysis"""
        print("\n--- QuickBooks Data Exploration ---")

        # Explore Customers
        customers = self.explore_customers()
        print(f"\nCustomers Found: {len(customers)}")
        for customer in customers[:5]:  # Display first 5 customers
            print(f"Customer: {customer['name']}, Balance: ${customer.get('balance', 0)}") # Explore Invoices
        invoices = self.explore_invoices()
        print(f"\nInvoices Found: {len(invoices)}")
        total_invoice_amount = sum(inv['total_amount'] for inv in invoices)
        print(f"Total Invoice Amount: ${total_invoice_amount:.2f}")

        # Explore Items
        items = self.explore_items()
        print(f"\nItems Found: {len(items)}")
        for item in items[:5]:  # Display first 5 items
            print(f"Item: {item['name']}, Price: ${item.get('unit_price', 0)}")

def main():
    try:
        # Initialize data explorer
        explorer = QuickBooksDataExplorer()
        explorer.perform_comprehensive_analysis()
    except Exception as e:
        logger.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
