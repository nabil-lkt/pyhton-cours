import math
import string

class Testeur_mdp:
    def __init__(self, mot_de_passe):
        self.mot_de_passe = mot_de_passe

    def calculer_complexite(self):
        jeu_de_caracteres = string.ascii_letters + string.digits + string.punctuation
        ensemble_mot_de_passe = set(self.mot_de_passe)
        longueur_mot_de_passe = len(self.mot_de_passe)
        longueur_jeu_de_caracteres = len(jeu_de_caracteres)
        entropie = longueur_mot_de_passe * math.log2(longueur_jeu_de_caracteres)
        return entropie

    def evaluer_mot_de_passe(self):
        entropie = self.calculer_complexite()
        if entropie < 64:
            return "Faible"
        elif entropie < 128:
            return "Moyenne"
        else:
            return "Forte"