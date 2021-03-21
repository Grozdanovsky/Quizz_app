
class Question:
    def __init__(self, question, answers, right_answer):
        self.question = question
        self.answers = answers
        self.right_answer = right_answer

    def return_question(self):
        print(self.question)
        for key,value in self.answers.items():
            print(f"{key.upper()} : {value}")

    def get_right_answer(self):
        return self.right_answer
