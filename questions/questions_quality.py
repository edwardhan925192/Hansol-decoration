import os 

def split_questions(questions_list):
    def split_and_adjust(text):        
        parts = [part.strip() + '?' for part in text.replace('.', '?').split('?') if part.strip()]
        
        if not (text.endswith('?') or text.endswith('.')):
            parts[-1] = parts[-1].rstrip('?')  
                    
        parts = [part if len(part) >= 3 else '' for part in parts]
        return parts
    
    processed_questions = [split_and_adjust(question) for question in questions_list]

    return processed_questions   
