import unittest
import math
from Generateur_passphrase import GenerateurDePhraseSecrete

class TestGenerateurDePhraseSecrete(unittest.TestCase):
    def test_generer_phrase_secrete(self):
        # Testez la méthode generer_phrase_secrete()
        generateur = GenerateurDePhraseSecrete(5)  # Générer une phrase de 5 mots
        phrase_secrete = generateur.generer_phrase_secrete()
        mots = phrase_secrete.split()
        self.assertEqual(len(mots), 5)  # Vérifiez que la phrase a le bon nombre de mots

    def test_calculer_complexite(self):
        # Testez la méthode calculer_complexite() avec une phrase générée
        generateur = GenerateurDePhraseSecrete(4)  # Générer une phrase de 4 mots
        phrase_secrete = generateur.generer_phrase_secrete()
        entropie = generateur.calculer_complexite(phrase_secrete)

        # L'entropie attendue dépend de la taille de la liste de mots
        longueur_liste_mots = len(generateur.liste_mots)
        entropie_attendue = 4 * math.log2(longueur_liste_mots)

        self.assertEqual(entropie, entropie_attendue)