# QuickBooks Integration

A Python-based integration with QuickBooks API that allows for automated processing of PDF invoices and transaction management. This tool helps streamline the process of matching PDF invoices with QuickBooks transactions and handling attachments.

## Features

- Automatic PDF invoice processing
- Transaction matching based on dates and amounts
- Automated attachment handling for invoices
- Date range-based transaction queries
- Formatted transaction reporting
- Secure API authentication

## Prerequisites

- Python 3.8+
- QuickBooks Developer Account
- API credentials from QuickBooks

## Installation

1. Create and activate a virtual environment:
```bash
python -m venv quickbooks_env
source quickbooks_env/bin/activate  # On Windows use: quickbooks_env\Scripts\activate
```

2. Install required packages:
```bash
pip install -r requirement.txt
```

3. Set up your environment variables with your QuickBooks API credentials:
```bash
export CLIENT_ID="your_client_id"
export CLIENT_SECRET="your_client_secret"
export REALM_ID="your_realm_id"
export REFRESH_TOKEN="your_refresh_token"
```

Alternatively, you can modify the credentials directly in `src/Utility_Test/QuickBook_utilities.py`.

## Project Structure

```
.
├── README.md
├── requirement.txt
├── run.py
└── src/
    ├── __init__.py
    ├── file_handler.py
    └── Utility_Test/
        ├── __init__.py
        ├── Attachement_utils.py
        ├── QuickBook_utilities.py
        ├── date_test.py
        └── formated_print.py
```

## Usage

1. Start the script:
```bash
python run.py
```

2. When prompted, enter the location of your PDF invoice files. The files should follow the naming convention:
```
YYYY-MM-DD_amount.pdf
```

Example:
```
2024-03-21_299.99.pdf
```

3. The script will:
   - Parse the PDF files in the specified directory
   - Extract date and amount information from filenames
   - Query QuickBooks for matching transactions
   - Upload PDFs as attachments to matching invoices
   - Display formatted transaction details
   - Verify attachment status

## API Functions

### File Handling
- `FileHandler`: Manages PDF file operations and parsing
- `parse_files()`: Processes PDF files and extracts relevant information

### QuickBooks Integration
- `connect_to_quickbooks()`: Establishes connection to QuickBooks API
- `get_recent_transactions()`: Retrieves transactions within specified parameters
- `upload_invoice_pdf()`: Attaches PDF files to QuickBooks invoices
- `check_invoice_attachments()`: Verifies attachment status for invoices

### Utility Functions
- `get_transactions_with_date_range()`: Calculates date ranges for transaction queries
- `format_invoice()`: Formats invoice data for display
- `print_invoices()`: Displays formatted invoice information

## Error Handling

The application includes comprehensive error handling for:
- File system operations
- API connections
- Authentication issues
- Invalid file formats
- Missing credentials
- Transaction matching errors

## Dependencies

Key packages required:
- quickbooks-python
- intuit-oauth
- python-dateutil
- requests
- cryptography

Full list available in `requirement.txt`

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
