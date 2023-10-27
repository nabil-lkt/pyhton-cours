import random
import os
from Question import Question

class QCM:
    #Initialisation des question et du score final
    def __init__(self, questions):
        self.questions = questions
        self.score = 0
    #Fonction pour clear le terminal pour apporter plus de visibilité
    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    #Fonction pour mélanger les questions parmi le pool
    def shuffle_questions(self):
        random.shuffle(self.questions)

    #Fonction qui va gérer le déroulé du QCM
    def run(self):
        #Au départ, on mélange les questions dans le pool
        self.shuffle_questions()
        #Ensuite on parcourt les questions
        for i, question in enumerate(self.questions, start=1):
            self.clear_screen()
            #copie les options de la question
            options = question.options.copy()
            #enregistre la réponse correcte
            correct_answer = question.reponse_correcte
            #mélange les options dans un ordre aléatoire,
            random.shuffle(options)
            #détermine l'index de la réponse correcte parmi les options mélangées pour vérifier la réponse user
            correct_index = options.index(correct_answer)
            #On affiche donc la question
            print("Question {}: {}".format(i, question.text))
            #On parcourt les options de la question et on les affiche
            for j, option in enumerate(options, start=1):
                print("{} {}".format(chr(96 + j), option))
            #Ici on gère la casse quant à l'entrée user
            while True:
                reponse_user = input("Votre réponse (a/b/c) : ").lower()
                if reponse_user in ['a', 'b', 'c']:
                    break
                else:
                    print("Veuillez entrer 'a', 'b' ou 'c' comme réponse valide.")
            #Vérifie que la réponse du user correspond à la bonne réponse, si oui score +1
            if options[ord(reponse_user) - ord('a')] == correct_answer:
                self.score += 1
            self.clear_screen()

    #Fonction pour afficher le score final
    def Affichage_score(self):
        print("Score final : {}/{}".format(self.score, len(self.questions)))

    #Affichage de toutes les questions posées avec la réponse associée
    def Affichage_réponse_fin(self):
        self.clear_screen()
        print("Voici les bonnes réponses :")
        #On parcoure les questions et l'affiche ainsi que la réponse associée
        for i, question in enumerate(self.questions, start=1):
            print("Question {}: {} (Réponse correcte : {})".format(i, question.text, question.reponse_correcte))

def main():
    #On déclare notre pool de questions, leurs options et la bonne réponse associée
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

    #On charge les questions de QCM dans qcm puis on lance le déroulé du QCM
    qcm = QCM(questions)
    qcm.run()
    #On termine par afficher un récap des réponses par questions et le score final du user
    qcm.Affichage_réponse_fin()
    qcm.Affichage_score()

if __name__ == "__main__":
    main()
