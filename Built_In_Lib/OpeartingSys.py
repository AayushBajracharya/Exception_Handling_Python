
import os

# Get current working directory
current_directory = os.getcwd()
print(f"Current Directory: {current_directory}")

# List all files and directories in the current directory
directory_contents = os.listdir(current_directory)
print(f"Contents of Current Directory: {directory_contents}")

# Create a new directory
os.mkdir('new_directory5')
print("Created new_directory")

# Remove a directory
os.rmdir('new_directory5')
print("Removed new_directory")
