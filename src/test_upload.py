from Utility_Test.QuickBook_utilities import connect_to_quickbooks
import os
from intuitlib.client import AuthClient
from quickbooks import QuickBooks
from quickbooks.objects.attachable import Attachable, AttachableRef
from quickbooks.objects.invoice import Invoice

def upload_invoice_pdf(quickbooks_client, invoice_id, pdf_path):
    """
    Upload a single PDF attachment to a specific invoice in QuickBooks.
    
    :param quickbooks_client: QuickBooks client instance
    :param invoice_id: ID of the invoice to attach the file to
    :param pdf_path: Full path to the PDF file
    :return: Dictionary with upload status and details
    """
    try:
        # Validate QuickBooks client
        if not isinstance(quickbooks_client, QuickBooks):
            raise ValueError("Invalid QuickBooks client instance")

        # Validate invoice ID
        if not isinstance(invoice_id, (int, str)) or not str(invoice_id).isdigit():
            raise ValueError("Invalid invoice ID. It must be a numeric value.")

        # Validate PDF file
        if not os.path.exists(pdf_path) or not pdf_path.lower().endswith('.pdf'):
            raise ValueError("Invalid PDF file. Ensure the file exists and has a .pdf extension.")
        
        # Get file details
        file_name = os.path.basename(pdf_path)
        
        # Create Attachable object
        attachable = Attachable()
        attachable.FileName = file_name
        attachable.ContentType = "application/pdf"
        
        # Create AttachableRef
        attachable_ref = AttachableRef()
        attachable_ref.EntityRef = {
            "type": "Invoice",
            "value": str(invoice_id)
        }
        attachable.AttachableRef.append(attachable_ref)
        
        # Set the file path for the attachment
        attachable._FilePath = pdf_path  # Full path to the file
        
        # Save the attachment
        attachable.save(qb=quickbooks_client)
        
        # Return upload details
        return {
            'success': True,
            'invoice_id': invoice_id,
            'file_name': file_name,
            'attachment_id': attachable.Id,
            'details': attachable.to_dict()
        }
    
    except Exception as e:
        return {
            'success': False,
            'error': str(e),
            'invoice_id': invoice_id,
            'file_name': os.path.basename(pdf_path) if pdf_path else None
        }

def main():
    # Connect to QuickBooks using the utility function
    quickbooks_client = connect_to_quickbooks()

    # Replace with a valid invoice ID and PDF file path
    INVOICE_ID = '130'  # Replace with a valid invoice ID
    PDF_PATH = '2024-10-23_362.07_SupplierC.pdf'  # Replace with the path to your PDF file

    # Call the upload_invoice_pdf function
    result = upload_invoice_pdf(quickbooks_client, INVOICE_ID, PDF_PATH)

    # Print the result
    print(result)

if __name__ == "__main__":
    main()
