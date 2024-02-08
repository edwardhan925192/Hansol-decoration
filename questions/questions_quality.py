from openai import OpenAI
import os

def api_init(api_key):
  openai = OpenAI(api_key=os.getenv(api_key))

def questions_topic_checker(question1, question2):
    prompt = f"""다음 두 질문이 같은 주제에 관한 것인지 대답하세요. "예" 또는 "아니오"로 응답하십시오.

질문 1: {question1}
질문 2: {question2}"""

    try:
        response = openai.ChatCompletion.create(
          model="gpt-3.5-turbo",  # Adjust the model as necessary
          messages=[
              {"role": "system", "content": "You are a helpful assistant."},
              {"role": "user", "content": prompt}
          ]
        )

        # Extracting the response text
        answer = response['choices'][0]['message']['content'].strip()
        print(f"Answer: {answer}")
        return answer
    except Exception as error:
        print(f"An error occurred: {error}")
        return None
