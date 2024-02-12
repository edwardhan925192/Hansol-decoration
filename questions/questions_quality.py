import openai
import os

def questions_topic_checker(question1, question2):
    prompt = f"""다음 두 질문이 같은 주제에 관한 것인지 대답하세요. "예" 또는 "아니오"로 응답하십시오.

질문 1: {question1}
질문 2: {question2}"""

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ]
        )

        # Extracting the response text
        answer = response.choices[0].message['content'].strip()
        print(f"Answer: {answer}")
        return answer
    except Exception as error:
        print(f"An error occurred: {error}")
        return None

import openai

def remove_conjunctions_korean(text):
    prompt = f"""다음 문장에서 접속 부사와 접속사를 제거해주세요. 예를 들어, '그리고', '또한' 같은 단어들을 삭제해야 합니다.

문장: {text}"""

    try:
        response = openai.Completion.create(
            model="gpt-3.5-turbo",
            prompt=prompt,
            max_tokens=1024,
            temperature=0.3
        )

        # Extracting the response text
        cleaned_text = response.choices[0].text.strip()
        print(f"Cleaned Text: {cleaned_text}")
        return cleaned_text
    except Exception as error:
        print(f"An error occurred: {error}")
        return None

def split_questions(questions_list):
    def split_and_adjust(text):
        # Split by both '?' and '.', and filter out empty parts
        parts = [part.strip() + '?' for part in text.replace('.', '?').split('?') if part.strip()]
        # Check if the text ends with '?' or '.', adjust the last part accordingly
        if not (text.endswith('?') or text.endswith('.')):
            parts[-1] = parts[-1].rstrip('?')  # Remove '?' from the last part if text did not end with '?' or '.'
        # Replace short elements with ''
        parts = [part if len(part) >= 3 else '' for part in parts]
        return parts

    # Process each question in the list
    processed_questions = [split_and_adjust(question[0]) for question in questions_list]

    return processed_questions


def replace_short_strings(df, exclude_column):
    for column in df.columns:
        if column != exclude_column:
            df[column] = df[column].apply(lambda x: 0 if isinstance(x, str) and len(x) < 3 else x)
    return df
