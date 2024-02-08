# usage 
```markdown
from Hansol-decoration.questions.questionsquality import api_init, questions_topic_checker, remove_conjunctions_korean
api_key = 'abcde'


# Example usage with Korean questions
question1 = "프랑스의 수도는 어디인가요?"
question2 = "에펠탑이 위치한 도시는 어디인가요?"


# ----- api keys ----- # 
api_init(api_key)
questions_topic_checker(question1, question2)
remove_conjunctions_korean(text)
```
