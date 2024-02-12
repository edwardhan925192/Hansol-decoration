import os

def clean_text_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        # Read the entire content of the file
        content = file.read()

    # Replace multiple newlines with a single space
    cleaned_content = ' '.join(content.splitlines())

    # Replace multiple spaces with a single space
    cleaned_content = ' '.join(cleaned_content.split())

    return cleaned_content

def get_txt_file_paths(folder_path):
    txt_file_paths = []

    # List all files in the given folder
    for filename in os.listdir(folder_path):
        # Check if the file is a .txt file
        if filename.endswith('.txt'):
            # Construct the full file path
            file_path = os.path.join(folder_path, filename)
            # Add the file path to the list
            txt_file_paths.append(file_path)

    return txt_file_paths
