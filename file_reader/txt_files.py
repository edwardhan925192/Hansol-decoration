import os
from langchain_community.document_loaders.text import TextLoader
from tqdm import tqdm

def txt_files_to_dict(folder_path):
    files_dict = {}

    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            file_path = os.path.join(folder_path, filename)

            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()

            title = os.path.splitext(filename)[0]
            files_dict[title] = title + " " + content

    return files_dict
