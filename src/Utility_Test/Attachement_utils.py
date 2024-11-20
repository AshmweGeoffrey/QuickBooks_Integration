
import os
from quickbooks import QuickBooks
from quickbooks.objects.attachable import Attachable, AttachableRef
def check_invoice_attachments(invoice_id, quickbooks_client):
    """
    Check if an invoice has attachments and return their download URLs.
    
    :param invoice_id: ID of the invoice
    :param quickbooks_client: QuickBooks client
    :return: Dictionary with attachment download URLs and existence flag
    """
    try:
        # Query for attachments related to the specified invoice
        query = f"SELECT * FROM Attachable WHERE AttachableRef.EntityRef.type = 'Invoice' AND AttachableRef.EntityRef.value = '{invoice_id}'"
        attachments_response = quickbooks_client.query(query)

        # Initialize the result
        attachment_urls = []
        has_attachments = False

        # Check if there are any attachments
        if 'QueryResponse' in attachments_response and 'Attachable' in attachments_response['QueryResponse']:
            attachments = attachments_response['QueryResponse']['Attachable']
            attachment_urls = [attachment.get('TempDownloadUri') for attachment in attachments]
            has_attachments = bool(attachment_urls)

        return {
            'has_attachments': has_attachments,
            'attachment_urls': attachment_urls
        }
    
    except Exception as e:
        return {
            'has_attachments': False,
            'error': str(e)
        }
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