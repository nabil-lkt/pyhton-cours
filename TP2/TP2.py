import os
import random
import unittest
#import des modules
from Generateur_mdp import GenerateurDeMotDePasse
from Testeur_mdp import Testeur_mdp
from Generateur_passphrase import GenerateurDePhraseSecrete
#Fonction pour clear le terminal pour apporter plus de visibilité
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    #Affichage du "Menu"
    print("Bienvenue dans notre programme de sécurité \n")
    print("1. Testeur de mot de passe")
    print("2. Génération de mot de passe sécurisé")
    print("3. Génération d'une phrase secrète")
    print("4. Quitter\n")
    #Boucle While pour gérer erreur dans le menu
    while True:
                choix = input("Choisissez une option (1/2/3/4) : ")
                if choix in ['1', '2', '3', '4']:
                    break
                else:
                    print("Veuillez entrer un numéro correspondant à un menu.") 

    #TESTEUR DE MOT DE PASSE
    if choix == "1":
        clear_screen()
        mot_de_passe = input("Entrez le mot de passe à évaluer : ")
        #Test du mdp par appel de la fonction
        testeur = Testeur_mdp(mot_de_passe)
        resultat = testeur.evaluer_mot_de_passe()
        print(f"Complexité du mot de passe : {resultat}")

    #GENERATION DE MDP SECURISE
    elif choix == "2":
        clear_screen()
        print("Veuillez entrer les spécifications de votre mot de passe : \n")
        #Spécification des caractéristiques du mot de passe demandé
        nb_minuscules = int(input("Nombre de minuscules : "))
        nb_majuscules = int(input("Nombre de majuscules : "))
        nb_chiffres = int(input("Nombre de chiffres : "))
        nb_caracteres_speciaux = int(input("Nombre de caractères spéciaux : "))
        #Appel de la fonction de Génération de mot de passe
        generateur = GenerateurDeMotDePasse(nb_minuscules, nb_majuscules, nb_chiffres, nb_caracteres_speciaux)
        mot_de_passe_genere = generateur.generer_mot_de_passe()
        entropie = generateur.calculer_complexite(mot_de_passe_genere)
        print(f"\nVoici le mot de passe généré : {mot_de_passe_genere}")
        print(f"Complexité du mot de passe : {entropie}")

    #GENERATION PHRASE SECRETE
    elif choix == "3":
        clear_screen()
        nb_mots = int(input("Nombre de mots dans la phrase secrète : "))
        generateur = GenerateurDePhraseSecrete(nb_mots)
        phrase_secrete_generee = generateur.generer_phrase_secrete()
        entropie = generateur.calculer_complexite(phrase_secrete_generee)
        print(f"Phrase secrète générée : {phrase_secrete_generee}")
        print(f"Complexité de la phrase secrète : {entropie}")
    
    #QUITTER
    elif choix == "4":
        print("Fin du programme")

if __name__ == "__main__":
    main()