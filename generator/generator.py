import os
import torch
import numpy as np
import pandas as pd
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms.huggingface_pipeline import HuggingFacePipeline
from transformers import LlamaForCausalLM, AutoTokenizer, pipeline


def generate_text_directly(model, tokenizer, question, context="", max_length=512):
    prompt_text = f"{context}\n\n질문: {question}\n답변:" if context else f"질문: {question}\n답변:"
    inputs = tokenizer(prompt_text, return_tensors="pt", padding=True, truncation=True, max_length=max_length).to(model.device)
    output_tokens = model.generate(**inputs, max_length=max_length, num_return_sequences=1)
    answer = tokenizer.decode(output_tokens[0], skip_special_tokens=True)
    return answer
    

def lookup_keywords_with_spaces(question, dictionary):
    keywords_found = set()  # Use set to avoid duplicates
    
    # Iterate over dictionary keys
    for key in dictionary.keys():
        # Check if the key exists in the question as a substring
        if key in question:
            keywords_found.add(key)
    
    return list(keywords_found)


# -- single question 
def qa_from_stringdb(string_db, question, index_dict, matched_keys, model, tokenizer):
    indexes = []
    for keyword in matched_keys:
        # Check if keyword exists in index_dict to avoid KeyError
        if keyword in index_dict:
            indexes.extend(index_dict[keyword])

    documents_list = [string_db[index] for index in indexes if index in string_db]  # Check for index existence
    formatted_docs = "\n\n".join(documents_list)
    # Pass formatted_docs as context
    answer = generate_text_directly(model, tokenizer, question, context=formatted_docs, max_length=512)                
    return answer


# -- processing the whole question
def process_questions(string_db, question_lists, documentation_dict, model, tokenizer):
    result = []
    for question_list in tqdm(question_lists, total=len(question_lists)):
        all_answers = []
        for question in question_list:
            # Corrected variable name from questions to question
            matched_keys = lookup_keywords_with_spaces(question, documentation_dict)  # Corrected dict name

            if matched_keys:
                answers = qa_from_stringdb(string_db, question, documentation_dict, matched_keys, model, tokenizer)
                all_answers.append(answers)

        concatenated_answers = " ".join(all_answers)
        result.append(concatenated_answers)

    return result
