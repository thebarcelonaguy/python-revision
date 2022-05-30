from main import question_bank


class QuizBrain:
    def __init__(self, questions_list):
        self.question_number = 0
        self.questions_list = questions_list
        self.score = 0

    def next_question(self):
        question_obj = self.questions_list[self.question_number]
        self.question_number += 1
        question = input(f"Q{self.question_number}: {question_obj.text} (True/False)?: ")
        if question == question_obj.answer:
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"The correct answer was {question_obj.answer}")
        print(f"Your current score is: {self.score}/{self.question_number}")

    def still_has_questions(self):
        return self.question_number < len(self.questions_list)


quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()
