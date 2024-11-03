# file_handling_assignment.py

# File creation and writing initial content
try:
    # Creating and opening the file in write mode
    with open("my_file.txt", "w") as file:
        # Writing three lines of text (mix of strings and numbers)
        file.write("Hello, this is the first line.\n")
        file.write("The second line includes a number: 42\n")
        file.write("Here's the third line with a mix: 3.14 and some text.\n")
    print("File created and initial content written successfully.")
except (FileNotFoundError, PermissionError) as e:
    print(f"Error creating or writing to the file: {e}")

# File reading and displaying content
try:
    # Opening the file in read mode
    with open("my_file.txt", "r") as file:
        content = file.read()
    print("File content:")
    print(content)
except (FileNotFoundError, PermissionError) as e:
    print(f"Error reading the file: {e}")

# File appending additional content
try:
    # Opening the file in append mode
    with open("my_file.txt", "a") as file:
        # Appending three additional lines of text
        file.write("Appending a fourth line here.\n")
        file.write("Fifth line with another number: 100\n")
        file.write("Sixth line wraps it up!\n")
    print("Additional content appended successfully.")
except (FileNotFoundError, PermissionError) as e:
    print(f"Error appending to the file: {e}")

# File reading after appending to confirm all content
try:
    # Reopening the file in read mode to display updated content
    with open("my_file.txt", "r") as file:
        content = file.read()
    print("Updated file content:")
    print(content)
except (FileNotFoundError, PermissionError) as e:
    print(f"Error reading the updated file: {e}")

# Finally block to confirm script completion
finally:
    print("File handling operations complete.")