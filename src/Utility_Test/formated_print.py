from typing import List, Dict, Any

def format_invoice(invoice: Dict[str, Any]) -> Dict[str, Any]:
    """
    Format a single invoice for easy reading.

    Args:
        invoice (Dict[str, Any]): The invoice data as a dictionary.

    Returns:
        Dict[str, Any]: A formatted dictionary with selected invoice details.
    """
    return {
        'Invoice Number': invoice.get('DocNumber', 'N/A'),
        'Transaction Date': invoice.get('TxnDate', 'N/A'),
        'Customer': invoice.get('CustomerRef', {}).get('name', 'N/A'),
        'Total Amount': invoice.get('TotalAmt', 'N/A'),
        'Items': [
            {
                'Description': line.get('Description', 'N/A'),
                'Amount': line.get('Amount', 'N/A'),
                'Quantity': line.get('SalesItemLineDetail', {}).get('Qty', 'N/A'),
                'Unit Price': line.get('SalesItemLineDetail', {}).get('UnitPrice', 'N/A')
            }
            for line in invoice.get('Line', [])
            if line.get('DetailType') == 'SalesItemLineDetail'
        ],
        'Balance': invoice.get('Balance', 'N/A'),
        'Due Date': invoice.get('DueDate', 'N/A')
    }

def print_invoices(data: Dict[str, Any]) -> None:
    """
    Nicely print out invoice details.

    Args:
        data (Dict[str, Any]): The data containing invoice information.
    """
    if 'QueryResponse' in data and 'Invoice' in data['QueryResponse']:
        invoices = data['QueryResponse']['Invoice']

        print(f"Total Invoices Found: {len(invoices)}")
        print("-" * 50)

        for idx, invoice in enumerate(invoices, 1):
            formatted_invoice = format_invoice(invoice)

            print(f"Invoice #{idx}")
            for key, value in formatted_invoice.items():
                if key == 'Items':
                    print(f"{key}:")
                    for item in value:
                        print("  - " + " | ".join(f"{k}: {v}" for k, v in item.items()))
                else:
                    print(f"{key}: {value}")
            print("-" * 50)