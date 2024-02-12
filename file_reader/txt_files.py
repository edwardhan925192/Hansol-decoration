import os
from langchain_community.document_loaders.text import TextLoader
from tqdm import tqdm

def clean_and_save_txt_files(folder_path):
    # Retrieve a list of all .txt files in the folder
    txt_files = [f for f in os.listdir(folder_path) if f.endswith('.txt')]
    
    # Process each .txt file and wrap it with tqdm for a progress bar
    for filename in tqdm(txt_files, desc='Processing and Saving TXTs'):
        # Construct the full file path
        file_path = os.path.join(folder_path, filename)
        
        # Read, clean, and save the file content
        cleaned_content = clean_text_file(file_path)  # Using your existing clean_text_file function
        
        # Define the path for the cleaned file (here, overwriting the original file)
        cleaned_file_path = file_path  # Or define a new path if you want to keep the original files
        
        # Write the cleaned content back to the file
        with open(cleaned_file_path, 'w', encoding='utf-8') as file:
            file.write(cleaned_content)

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
