class Quiz:
    def __init__(self,questions):
        self.questions = questions

    def print_prasanja(self):
        for obj in self.questions:
            obj.return_question()

    def get_question(self,index):
        return self.questions[index]

    def return_len_questions(self):
        return len(self.questions)