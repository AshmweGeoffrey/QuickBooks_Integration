import os
from src.Utility_Test.QuickBook_utilities import *
from src.Utility_Test.date_test import *
from src.Utility_Test.Attachement_utils import *

class FileHandler:
    """
    A class to handle file operations for parsing PDF files in a specified directory.

    Attributes:
        path (str): The directory path containing the files.
        files (list): A list of files in the specified directory.
    """

    def __init__(self, path):
        """
        Initializes the FileHandler with a specified path.

        Args:
            path (str): The directory path to initialize the file handler.
        """
        self.path = path
        self.files = []
        self.set_paths(self.path)

    def set_paths(self, path):
        """
        Sets the directory path and retrieves the list of files in that directory.

        Args:
            path (str): The directory path to set.
        """
        self.path = path
        try:
            self.files = os.listdir(self.path)
        except FileNotFoundError:
            print(f"Error: The directory '{path}' does not exist.")
            self.files = []
        except Exception as e:
            print(f"An error occurred while listing files: {e}")
            self.files = []

    def get_files(self):
        """
        Returns the list of files in the directory.

        Returns:
            list: A list of file names in the directory.
        """
        return self.files

    def parse_files(self):
        """
        Parses the PDF files in the directory, extracting date and amount from the file names,
        and retrieves recent transactions based on that information.
        """
        for file in self.files:
            if file.endswith(".pdf"):
                file_name = os.path.join(self.path, file)
                print("Parsing file:", file_name)
                
                # Split the file name to extract date and amount
                file_details = file.split("_")
                if len(file_details) < 2:
                    print(f"Warning: File '{file}' does not have the expected format.")
                    continue
                
                date = file_details[0]
                amount = file_details[1]
                
                # Get date ranges and recent transactions
                date_ranges = get_transactions_with_date_range(date, 3)
                print("Checking Date:", date)
                get_recent_transactions(date_ranges[0], date_ranges[1], amount, file_name)