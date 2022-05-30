from data import question_data
from question_model import Question


question_bank = []
for i in range(0,10):
    question_bank.append(Question(question_data["results"][0]["question"], question_data["results"][0]["correct_answer"]))
