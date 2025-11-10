"""
Livraison.py
Auteur: Milena Arce
---------------
Ce module définit la classe Livraison, dérivée de Service,
permettant d’effectuer le service de livraison d’un véhicule.
"""

from Service import Service

class Livraison(Service):
    """
    Classe pour effectuer le service de livraison.
    Cette classe est herité de la classe Service.
    """
    
    def __init__(self, dateDemande, dateService, rapport):
        """
        Construit une instance de la classe Livraison.
        
        Parameters:
        dateDemande (date): Date à laquelle le service a été demandé.
        dateService (date): Date prévue pour la livraison.
        rapport (str): Compte-rendu du service.
        """
    
    def effectuerLivraison():
        """
        Effectuer le service de livraison du véhicule.
        """
