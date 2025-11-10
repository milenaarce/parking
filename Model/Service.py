"""
Service.py
Auteur: Milena Arce
---------------
Ce module définit la classe Service, classe mère des différents services proposés
aux abonnés du parking (livraison, entretien, maintenance, etc.).
"""

class Service():
    """
    Classe mère pour définir l'ensemble des services offerts par le parking pour les abonnés.
    """
    
    def __init__(self, dateDemande, dateService, rapport):
        """
        Construit une instance de la classe Service.
        
        Parameters:
        dateDemande (date): La date à laquelle le service a été demandé.
        dateService (date): La date à laquelle le service sera effectué.
        rapport (str): Compte-rendu du service une fois terminé.
        """
    


   