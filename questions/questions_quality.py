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


def split_questions_into_columns(df, column_name):

    def split_and_adjust(text):
        parts = [part.strip() + '?' for part in text.split('?') if part.strip()]
        if not text.endswith('?'):
            parts[-1] = parts[-1].rstrip('?')  # Remove '?' if the text did not end with one
        return parts

    split_texts = df[column_name].apply(split_and_adjust)
    max_questions = split_texts.apply(len).max()
    question_columns = [f'Question {i+1}' for i in range(max_questions)]
    new_df = pd.DataFrame(index=df.index, columns=['id'] + question_columns)
    new_df['id'] = df['id']  # Copy the ID column

    for i, questions in enumerate(split_texts):
        new_df.loc[i, ['id'] + question_columns[:len(questions)]] = [df.loc[i, 'id']] + questions

    new_df = new_df.fillna(0)

    return new_df


def replace_short_strings(df, exclude_column):
    for column in df.columns:
        if column != exclude_column:
            df[column] = df[column].apply(lambda x: 0 if isinstance(x, str) and len(x) < 3 else x)
    return df
