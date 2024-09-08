# Python script to handle file operations with error handling

# Define the file name
file_name = "my_file.txt"

try:
    # Step 1: Create a new file and write some lines
    with open(file_name, 'w') as file:
        file.write("This is the first line of text.\n")
        file.write("The number of students is 25.\n")
        file.write("Python programming is fun.\n")
    
    # Step 2: Read and display the contents of the file
    with open(file_name, 'r') as file:
        content = file.read()
        print("Initial Content of the File:\n", content)
    
    # Step 3: Append additional lines to the file
    with open(file_name, 'a') as file:
        file.write("This is an appended line.\n")
        file.write("There are 42 apples.\n")
        file.write("Learning file handling in Python.\n")
    
    # Step 4: Read and display the updated contents of the file
    with open(file_name, 'r') as file:
        updated_content = file.read()
        print("Updated Content of the File:\n", updated_content)

except FileNotFoundError:
    print(f"Error: The file '{file_name}' was not found.")
except PermissionError:
    print(f"Error: You do not have permission to access '{file_name}'.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    print("File handling operations complete.")
