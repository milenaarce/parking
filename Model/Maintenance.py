"""
Maintenance.py
Auteur: Milena Arce
---------------
Ce module définit la classe Maintenance, dérivée de Service,
permettant d’effectuer un service de maintenance sur une voiture.
"""

from Service import Service
from Voiture import Voiture

class Maintenance(Service):
    """
    Classe pour effectuer le service de maintenance.
    Hérite de la classe Service.
    """
    
    def __init__(self, dateDemande, dateService, rapport):
        """
        Construit une instance de la classe Maintenance.
        
        Parameters:
        dateDemande (date): Date à laquelle le service a été demandé.
        dateService (date): Date prévue pour la maintenance.
        rapport (str): Compte-rendu du service.
        """
    
    def effectuerMaintenance(v: Voiture):
        """
        Effectuer la maintenance du véhicule spécifié.
        
        Parameters:
        v (Voiture): Le véhicule à entretenir.
        """
