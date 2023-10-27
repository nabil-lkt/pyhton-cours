import random
import os
from Question import Question

class QCM:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def shuffle_questions(self):
        random.shuffle(self.questions)

    def run(self):
        self.shuffle_questions()
        for i, question in enumerate(self.questions, start=1):
            self.clear_screen()

            options = question.options.copy()
            correct_answer = question.reponse_correcte
            random.shuffle(options)

            correct_index = options.index(correct_answer)

            print("Question {}: {}".format(i, question.text))
            for j, option in enumerate(options, start=1):
                print("{} {}".format(chr(96 + j), option))

            reponse_user = input("Votre réponse (a/b/c) : ").lower()

            if options[ord(reponse_user) - ord('a')] == correct_answer:
                self.score += 1
            self.clear_screen()

    def display_score(self):
        print("Score final : {}/{}".format(self.score, len(self.questions)))

    def display_correct_answers(self):
        self.clear_screen()
        print("Voici les bonnes réponses :")
        for i, question in enumerate(self.questions, start=1):
            print("Question {}: {} (Réponse correcte : {})".format(i, question.text, question.reponse_correcte))

def main():
    questions = [
        Question("Quel est le langage de programmation le plus populaire ?", ["Python", "Java", "C++"], "Python"),
        Question("Quelle est la capitale du Brésil ?", ["Sao Paulo", "Brasilia", "Rio de Janeiro"], "Brasilia"),
        Question("Quel français a inscrit un triplé en finale de la CDM de Football 2022", ["Benzema", "Mbappe", "Giroud"], "Mbappe"),
        Question("Quelle équipe a gagné les Worlds de LoL en 2022 ?", ["T1", "Damwon", "DRX"], "DRX"),
        Question("Quel est le nom du célèbre Détective des livres d'Agatha Christie ?", ["Hercule Poirot", "Victor Burakov", "Sherlock Holmes"], "Hercule Poirot"),
        Question("Quel artiste français est l'auteur de `La Bohème` ", ["Georges Brassens", "Michel Blanc", "Charles Aznavour"], "Charles Aznavour"),
        Question("Quel DJ a fait un concert au Parc des Princes en 2021", ["Skrillex", "DJ Snake", "Tiestö"], "DJ Snake"),
        Question("Qui a gagné le championnat du monde de F1 en 2021", ["Max Verstappen", "Lewis Hamilton", "Charles Leclerc"], "Max Verstappen"),
        Question("Dans quel anime retrouve-t-on Light Yagami ?", ["Hunter X Hunter", "Death Note", "Mob Psycho 100"], "Death Note"),
        Question("Quel artiste a produit la bande son du film `Spider-Man : Across the Spider-Verse", ["Imagine Dragons", "Travis Scott", "Metro Boomin"], "Metro Boomin"),
    ]

    qcm = QCM(questions)
    qcm.run()
    qcm.display_score()
    qcm.display_correct_answers()

if __name__ == "__main__":
    main()
