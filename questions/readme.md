# usage 
```markdown
from Hansol-decoration.questions.questionsquality import api_init, questions_topic_checker, remove_conjunctions_korean
api_key = 'abcde'

# Example usage with Korean questions
question1 = "프랑스의 수도는 어디인가요?"
question2 = "에펠탑이 위치한 도시는 어디인가요?"

text = "이것은 예시 문장입니다. 그리고, 여기에 또한 접속사가 포함되어 있습니다."

# ----- functions ----- # 
api_init(api_key)
questions_topic_checker(question1, question2)
remove_conjunctions_korean(text)
```
