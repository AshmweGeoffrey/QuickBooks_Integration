class QuickBooksConnector:
    def __init__(self):
        self.client = QuickBooks(
            client_id=os.getenv("CLIENT_ID"),
            client_secret=os.getenv("CLIENT_SECRET"),
            access_token=os.getenv("ACCESS_TOKEN"),
            refresh_token=os.getenv("REFRESH_TOKEN"),
            company_id=os.getenv("COMPANY_ID"),
        )
        