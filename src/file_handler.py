import os
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
                file_details=file.split("_")
                date=file_details[0]
                Amount=file_details[1]
                print("Date: ", date, "Amount: ", Amount)
