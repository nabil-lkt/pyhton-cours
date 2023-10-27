#Question.py
#On crée notre classe question qui contient les méthodes initialisation et si la réponse est correcte ou non
#self permettra que chaque questions ait ses attributs
class Question:
    #Ici, chaque question contient son énoncé, des options et une bonne réponse
    def __init__(self, enonce, options, correct_option):
        self.text = enonce
        self.options = options
        self.reponse_correcte = correct_option

    #Va vérifier que la réponse du user correspond à la réponse déclarée correcte
    #Egalement le reponse_user.lower permet de gérer la casse en cas de majuscule
    def bonne_reponse(self, reponse_user):
        return reponse_user.lower() == self.reponse_correcte
