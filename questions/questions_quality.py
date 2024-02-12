import os 

def split_questions(questions_list):
    def split_and_adjust(text):
        # Split the text into parts and add a '?' at the end of each part, if it's not empty
        parts = [part.strip() + '?' for part in text.replace('.', '?').split('?') if part.strip()]
        
        # Remove the '?' at the end of the last part if the original text didn't end with '?' or '.'
        if not (text.endswith('?') or text.endswith('.')):
            parts[-1] = parts[-1].rstrip('?')
        
        # Filter out parts that are shorter than 3 characters, excluding empty strings from the result
        parts = [part for part in parts if len(part) >= 3]
        return parts
    
    processed_questions = [split_and_adjust(question) for question in questions_list]

    return processed_questions
