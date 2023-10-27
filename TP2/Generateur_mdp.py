import random
import string
import math

class GenerateurDeMotDePasse:
    def __init__(self, nb_minuscules, nb_majuscules, nb_chiffres, nb_caracteres_speciaux):
        #Initialisation des variables
        self.nb_minuscules = nb_minuscules
        self.nb_majuscules = nb_majuscules
        self.nb_chiffres = nb_chiffres
        self.nb_caracteres_speciaux = nb_caracteres_speciaux

    def generer_mot_de_passe(self):
        #Génération aléatoire des min, maj etc selon le nombre demandé.
        minuscules = ''.join(random.choice(string.ascii_lowercase) for _ in range(self.nb_minuscules))
        majuscules = ''.join(random.choice(string.ascii_uppercase) for _ in range(self.nb_majuscules))
        chiffres = ''.join(random.choice(string.digits) for _ in range(self.nb_chiffres))
        caracteres_speciaux = ''.join(random.choice(string.punctuation) for _ in range(self.nb_caracteres_speciaux))

        #mot de passe devient concaténation des générations aléatoires
        mot_de_passe = minuscules + majuscules + chiffres + caracteres_speciaux
        #shuffle du mot de passe
        return ''.join(random.sample(mot_de_passe, len(mot_de_passe)))

    def calculer_complexite(self, mot_de_passe):
        #Calcul de la complexité du mot de passe généré
        jeu_de_caracteres = string.ascii_letters + string.digits + string.punctuation
        ensemble_mot_de_passe = set(mot_de_passe)
        longueur_mot_de_passe = len(mot_de_passe)
        longueur_jeu_de_caracteres = len(jeu_de_caracteres)
        entropie = longueur_mot_de_passe * math.log2(longueur_jeu_de_caracteres)
        return entropie