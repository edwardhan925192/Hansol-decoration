import os
from langchain_community.document_loaders.text import TextLoader
from tqdm import tqdm

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

def txts_to_docs(folder_path):
    # Initialize an empty list to hold the cleaned documents
    cleaned_docs = []

    # Retrieve a list of all .txt files in the folder
    txt_files = [f for f in os.listdir(folder_path) if f.endswith('.txt')]
    
    # List all .txt files in the given folder and wrap it with tqdm for a progress bar
    for filename in tqdm(txt_files, desc='Processing TXTs'):
        # Construct the full file path
        file_path = os.path.join(folder_path, filename)
        
        # Read and clean the file content
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            # Replace multiple newlines with a single space
            cleaned_content = ' '.join(content.splitlines())
            # Replace multiple spaces with a single space
            cleaned_content = ' '.join(cleaned_content.split())
        
        # Add the cleaned content to the list
        cleaned_docs.append(cleaned_content)

    return cleaned_docs
