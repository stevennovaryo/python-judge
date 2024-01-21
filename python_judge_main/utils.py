import os

def get_module_root_directory(directory_name):
    current_directory = os.path.abspath(__file__)

    while os.path.basename(current_directory) != directory_name:
        current_directory = os.path.dirname(current_directory)

        # Check if reached the root directory
        if current_directory == os.path.dirname(current_directory):
            raise ValueError(f"Directory '{directory_name}' not found in the path.")

    return current_directory
