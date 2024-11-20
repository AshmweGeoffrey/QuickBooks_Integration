from quickbooks import QuickBooks
from Utility_Test.QuickBook_utilities import *
def query_attachments(qb_client, invoice_id):
    query = f"SELECT * FROM Attachments WHERE EntityRef.EntityType = 'Invoice' AND EntityRef.Value = '{invoice_id}'"
    response = qb_client.query(query)
    return response

# Example Usage
try:
    qb_client = connect_to_quickbooks()
    
    if qb_client:
        attachment_response = query_attachments(qb_client, "130")
        print("Attachment Query Response:", attachment_response)
    else:
        print("Failed to establish connection to QuickBooks.")
except Exception as e:
    print("Error:", e)

