import time
def player1_or_player2(quiz,player1):
    for index in range(quiz.return_len_questions()):
        question = quiz.get_question(index)
        question.return_question()

        odgovor = input("Enter your answer: ")
        proverka(odgovor)
        if odgovor.lower() == question.get_right_answer():
            player1.set_correct()

        else:
            player1.set_errors()
        print("Processing...")
        time.sleep(2)


def winner(player1,player2):
    if player1.get_correct() > player2.get_correct():
        player1.print_player()

    elif player1.get_correct() < player2.get_correct():
        player2.print_player()

    elif player1.get_correct() == player2.get_correct():
        print("TIE")

def proverka(odgovor):
    lista = ["a","b","c","d"]
    brojac = 0
    for bukva in lista:
        if odgovor.lower() != bukva:
            brojac += 1

    if brojac == 4:
        print("You entered unknown letter so your answer is wrong.")

