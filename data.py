import requests

parameters = {
    "amount": 10,
    "category": 18,
    "type": "boolean"
}
response = requests.get(url="https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
question_data = response.json()["results"]


# question_data = [
#     {"category": "Science: Computers", "type": "boolean", "difficulty": "easy",
#      "question": "The programming language &quot;Python&quot; is based off a modified version of &quot;JavaScript&quot;.",
#      "correct_answer": "False", "incorrect_answers": ["True"]},
#     {"category": "Science: Computers", "type": "boolean", "difficulty": "easy",
#      "question": "The logo for Snapchat is a Bell.", "correct_answer": "False", "incorrect_answers": ["True"]},
#     {"category": "Science: Computers", "type": "boolean", "difficulty": "easy",
#      "question": "Pointers were not used in the original C programming language; they were added later on in C++.",
#      "correct_answer": "False", "incorrect_answers": ["True"]},
#     {"category": "Science: Computers", "type": "boolean", "difficulty": "easy",
#      "question": "RAM stands for Random Access Memory.", "correct_answer": "True", "incorrect_answers": ["False"]},
#     {"category": "Science: Computers", "type": "boolean", "difficulty": "easy",
#      "question": "Ada Lovelace is often considered the first computer programmer.", "correct_answer": "True",
#      "incorrect_answers": ["False"]}, {"category": "Science: Computers", "type": "boolean", "difficulty": "easy",
#                                        "question": "&quot;HTML&quot; stands for Hypertext Markup Language.",
#                                        "correct_answer": "True", "incorrect_answers": ["False"]},
#     {"category": "Science: Computers", "type": "boolean", "difficulty": "easy",
#      "question": "In most programming languages, the operator ++ is equivalent to the statement &quot;+= 1&quot;.",
#      "correct_answer": "True", "incorrect_answers": ["False"]},
#     {"category": "Science: Computers", "type": "boolean", "difficulty": "easy",
#      "question": "The Windows 7 operating system has six main editions.", "correct_answer": "True",
#      "incorrect_answers": ["False"]}, {"category": "Science: Computers", "type": "boolean", "difficulty": "easy",
#                                        "question": "The Windows ME operating system was released in the year 2000.",
#                                        "correct_answer": "True", "incorrect_answers": ["False"]},
#     {"category": "Science: Computers", "type": "boolean", "difficulty": "easy",
#      "question": "The NVidia GTX 1080 gets its name because it can only render at a 1920x1080 screen resolution.",
#      "correct_answer": "False", "incorrect_answers": ["True"]}]
