def file_read_write():
    # Ask user for the file to read
    filename = input("Enter the name of the file to read: ")

    try:
        # Try opening the file
        with open(filename, "r") as f:
            content = f.read()
        
        # Modify the content (for example: make it uppercase)
        modified_content = content.upper()

        # Create a new file to save modified version
        new_filename = "modified_" + filename
        with open(new_filename, "w") as f:
            f.write(modified_content)

        print(f"File has been modified and saved as '{new_filename}'.")

    except FileNotFoundError:
        print("❌ Error: File not found. Please check the name and try again.")
    except PermissionError:
        print("❌ Error: You don't have permission to read this file.")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")

# Run the function
file_read_write()
