import os
from Utility_Test.QuickBook_utilities import *
from Utility_Test.date_test import *
from Utility_Test.Attachement_utils import *
class file_handler:
    def __init__(self, path):
        self.path = path
        self.files=[]
        self.set_paths(self.path)
    def set_paths(self, path):
        self.path = path
        self.files = os.listdir(self.path)
    def get_files(self):
        return self.files
    def parse_files(self):
        for file in self.files:
            if file.endswith(".pdf"):
                file_name = self.path+'/'+file
                print("Parsing file: ",file_name)
                file_details=file.split("_")
                date=file_details[0]
                Amount=file_details[1]
                date_ranges=get_transactions_with_date_range(date,3)
                print("Checking Date: ",date)
                get_recent_transactions(date_ranges[0],date_ranges[1],Amount,file_name)
