import random
import math

class GenerateurDePhraseSecrete:
    def __init__(self, nb_mots):
        self.nb_mots = nb_mots
        #Déclaratoin de la banque de mots pour la passephrase aléatoire
        self.liste_mots = ["Gasly", "Cartman", "KCorp", "FouinyBaby", "RushB"]

    def generer_phrase_secrete(self):
        #sélection aléatoire des mots dans la banque pour un nb de mots défini
        phrase_secrete = ' '.join(random.choice(self.liste_mots) for _ in range(self.nb_mots))
        return phrase_secrete

    def calculer_complexite(self, phrase_secrete):
        #Calcul de la complexité de la Passphrase générée
        longueur_liste_mots = len(self.liste_mots)
        entropie = self.nb_mots * math.log2(longueur_liste_mots)
        return entropie