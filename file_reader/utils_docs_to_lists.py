import re

def clean_text(text):
    text_without_numbers = re.sub(r'[0-9,]+', '', text)
    text_without_newlines = re.sub(r'\n+', ' ', text_without_numbers)
    cleaned_text = re.sub(r'\s+', ' ', text_without_newlines)
    text_without_dashes = re.sub(r'-+', ' ', text_without_numbers)
    text_without_unwanted_chars = re.sub(r'-+|\[|\]|\)|\(', ' ', text_without_numbers)
    return cleaned_text


def documents_to_list(documents):
    combined_lists = []
    for doc in documents:
        # Convert document to dictionary if it's not already one
        doc_dict = doc.dict() if hasattr(doc, 'dict') else doc
        for key, value in doc_dict.items():
            if isinstance(value, str) and len(value) > 99:
                cleaned_value = clean_text(value)
                combined_lists.append(cleaned_value)
    return combined_lists
