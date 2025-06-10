class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.user = None
        self.score = 0
        self.current_question = None

    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        self.user = input(f"Q.{self.question_number}: {self.current_question.text}. (True/False)?: ")

    def still_has_question(self):
        # if len(self.question_list) == self.question_number:
        #     return False
        # else:
        #     return True
        return len(self.question_list) > self.question_number

    def check_answer(self):
        # current_question = self.question_list[self.question_number]
        # print(self.question_number)
        if self.user.lower() == self.current_question.answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("Wrong answer!!")
        print(f"The correct answer was: {self.current_question.answer}")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")
