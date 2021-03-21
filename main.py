from person import *
from question import *
from  all_questions import *
from quiz import *
from functions import *
import time
# player1 = Person("Viktor", "Grozdanovski")
# player2 = Person("Stefan", "Cvetanovski")
ime = input("Enter your name: ")
prezime = input("Enter your surname: ")
player1 = Person(ime,prezime)
quiz = Quiz(lista_prasanja)

#__ MAIN __
print("Please write the letter of your answer!!!")

player1_or_player2(quiz,player1)

#player1_or_player2(quiz,player2)

#winner(player1,player2)
player1.print_player()
time.sleep(6)
