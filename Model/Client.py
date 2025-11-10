"""
Client.py
Auteur: Milena Arce
---------------
Ce module définit la classe Client, qui représente un utilisateur du parking DreamPark.
"""

from Acces import Acces
from Abonnement import Abonnement

class Client():
    """
    Classe représentant un client du parking DreamPark.
    
    Un client peut être abonné ou non, effectuer des demandes de services (livraison, 
    entretien, maintenance), et interagir avec le système via les accès du parking.
    """
    
    def __init__(self, nom, adresse, estAbonne, estSuperAbonne, nbFrequentations):
        """
        Construit une instance de la classe Client.
        
        Parameters:
        nom (str): Nom du client.
        adresse (str): Adresse du client.
        estAbonne (bool): Indique si le client possède un abonnement.
        estSuperAbonne (bool): Indique si le client possède un pack garanti.
        nbFrequentations (int): Nombre de fois que le client a utilisé le parking.
        """
        
    def sAbonner(self, ab: Abonnement):
        """
        S'abonner au parking.
        
        Parameters:
        ab (Abonnement): L'abonnement choisi par le client.
        """
        
    def nouvelleVoiture(self, imma, hautV, longV): 
        """
        Ajouter une nouvelle voiture au compte du client.
        
        Parameters:
        imma (str): Immatriculation du véhicule.
        hautV (float): Hauteur du véhicule.
        longV (float): Longueur du véhicule.
        """
    
    def seDesabonner(self):
        """
        Se désabonner du parking.
        """
        
    def demanderMaintenance(self):
        """
        Faire une demande de maintenance pour un véhicule.
        """
        
    def demanderLivraison(self, dateLiv, heure, adresseLiv): 
        """
        Faire une demande de livraison de la voiture.
        
        Parameters:
        dateLiv (date): Date de livraison souhaitée.
        heure (int): Heure de livraison souhaitée.
        adresseLiv (str): Adresse de livraison.
        """
        
    def demanderentretien(self):
        """
        Faire une demande d'entretien du véhicule.
        """
    
    def entrerParking(self, a: Acces):
        """
        Entrer dans le parking par un accès donné.
        
        Parameters:
        a (Acces): L'accès utilisé pour entrer.

        Returns:
        string: Identifiant de la place assignée ou message d'erreur.
        """
     
        
        
