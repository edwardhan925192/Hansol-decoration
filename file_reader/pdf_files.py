import os
from langchain.document_loaders import PyPDFLoader

def pdfs_to_docs(folder_path):
    # Initialize an empty list to hold all documents
    docs = []

    # List all files in the given folder
    for filename in os.listdir(folder_path):
        # Check if the file is a PDF
        if filename.endswith('.pdf'):
            # Construct the full path to the PDF file
            file_path = os.path.join(folder_path, filename)
            # Initialize the PDF loader for the current file
            loader = PyPDFLoader(file_path)
            # Load and split the document, extending the docs list with the results
            docs.extend(loader.load_and_split())

    return docs
