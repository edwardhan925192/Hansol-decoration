import os
from langchain.document_loaders import PyPDFLoader
from tqdm import tqdm

def pdfs_to_docs(folder_path):    
    docs = []
    
    pdf_files = [f for f in os.listdir(folder_path) if f.endswith('.pdf')]    
    
    for filename in tqdm(pdf_files, desc='Processing PDFs'):        
        file_path = os.path.join(folder_path, filename)        
        loader = PyPDFLoader(file_path)        
        docs.extend(loader.load_and_split())

    return docs
