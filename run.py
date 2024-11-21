from src.file_handler import FileHandler

def main():
    print("Welcome to the QuickBooks Script")
    print("This script will parse QuickBooks files and perform various operations on them.")
    print("Starting the script...")

    # Provide clear instructions for the user
    print("\nPlease enter the location of the QuickBooks files to be parsed.")
    print("The files should be in .pdf format.")
    print("Example locations:")
    print("  - Linux: /home/username/Downloads/QuickBookFiles")
    print("  - Windows: C:/Users/username/Downloads/QuickBookFiles")
    
    # Prompt user for input
    location = input("Enter the location of the QuickBooks files: ")

    # Create an instance of FileHandler and parse files
    try:
        file_instance = FileHandler(location)
        file_instance.parse_files()
        print("Files parsed successfully.")
    except FileNotFoundError:
        print(f"Error: The specified location '{location}' does not exist. Please check the path and try again.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()