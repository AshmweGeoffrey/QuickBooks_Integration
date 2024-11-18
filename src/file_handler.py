import os

class file_handler:
    def __init__(self, path):
        self.path = path
        self.files=[]

    def read_paths(self):
        self.files = os.listdir(self.path)  
    def get_files(self):
        return self.files