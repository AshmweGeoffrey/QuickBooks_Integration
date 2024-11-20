import json
from quickbooks import QuickBooks
import requests
from Utility_Test.QuickBook_utilities import connect_to_quickbooks

def upload_invoice_attachment(file_name, qb_client, invoice_id):
    """
    Upload a PDF attachment to a QuickBooks Online invoice.

    Args:
        file_name (str): The path to the PDF file to attach.
        qb_client (QuickBooks): An authenticated QuickBooks client object.
        invoice_id (str): The ID of the invoice to which the file will be attached.

    Returns:
        dict: The API response as a JSON object.
    """
    # Extract details from the QuickBooks client
    access_token = qb_client.auth_client.access_token
    realm_id = qb_client.company_id
    
    # Endpoint URL for uploading attachments
    url = f"https://sandbox-quickbooks.api.intuit.com/v3/company/{realm_id}/upload"
    
    # Request headers
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Accept": "application/json"
    }

    # File metadata
    file_metadata = {
        "AttachableRef": [
            {
                "EntityRef": {
                    "type": "Invoice",
                    "value": invoice_id
                }
            }
        ],
        "FileName": file_name.split('/')[-1],  # Extract just the file name
        "ContentType": "application/pdf"
    }

    # Prepare the multipart/form-data payload
    with open(file_name, "rb") as file_content:
        files = {
            "file_metadata": (None, json.dumps(file_metadata), "application/json"),
            "file_content": (file_name, file_content, "application/pdf")
        }

        # Make the POST request
        response = requests.post(url, headers=headers, files=files)

    # Check for HTTP errors
    if response.status_code != 200:
        raise Exception(f"Failed to upload attachment: {response.status_code} - {response.text}")

    # Return the JSON response
    return response.json()

# Example Usage
try:
    # Establish connection to QuickBooks
    qb_client = connect_to_quickbooks()
    
    if qb_client:
        # Call the function to upload an attachment
        response = upload_invoice_attachment(
            file_name="2024-10-23_362.07_SupplierC.pdf",
            qb_client=qb_client,
            invoice_id="130"  # Replace with the actual invoice ID
        )
        print("Attachment uploaded successfully:", response)
    else:
        print("Failed to establish connection to QuickBooks.")
except Exception as e:
    print("Error:", e)
