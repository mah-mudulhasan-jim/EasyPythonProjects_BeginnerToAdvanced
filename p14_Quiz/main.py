from banner14 import banner
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain



question_bank = []
for question in question_data:
    question_bank.append(Question(question["text"], question["answer"]))


quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()
    quiz.check_answer()

print("Congratulations! You have completed the quiz")
print(f"Your final Score is: {quiz.score}/{quiz.question_number}")