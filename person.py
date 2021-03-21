
class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.errors = 0
        self.correct = 0

    def get_errors(self):
        return self.errors

    def get_correct(self):
        return self.correct

    def set_errors(self):
        self.errors += 1

    def set_correct(self):
        self.correct += 1

    def print_player(self):
        print(f"Name: {self.name}\nSurname: {self.surname}\nErrors: {self.errors}\nRight answers: {self.correct}")