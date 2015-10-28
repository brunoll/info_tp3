# -*- coding: utf-8 -*-
"""Ce module contient une classe contenant les informations sur une partie d'échecs,
dont un objet échiquier (une instance de la classe Echiquier).

"""
from pychecs.echiquier import Echiquier


class Partie:
    """La classe Partie contient les informations sur une partie d'échecs, c'est à dire un échiquier, puis
    un joueur actif (blanc ou noir). Des méthodes sont disponibles pour faire avancer la partie et interagir
    avec l'utilisateur.

    Attributes:
        joueur_actif (str): La couleur du joueur actif, 'blanc' ou 'noir'.
        echiquier (Echiquier): L'échiquier sur lequel se déroule la partie.

    """
    def __init__(self):
        # Le joueur débutant une partie d'échecs est le joueur blanc.
        self.joueur_actif = 'blanc'

        # Création d'une instance de la classe Echiquier, qui sera manipulée dans les méthodes de la classe.
        self.echiquier = Echiquier()

    def determiner_gagnant(self):
        """Détermine la couleur du joueur gagnant, s'il y en a un. Pour déterminer si un joueur est le gagnant,
        le roi de la couleur adverse doit être absente de l'échiquier.

        Returns:
            str: 'blanc' si le joueur blanc a gagné, 'noir' si c'est plutôt le joueur noir, et 'aucun' si aucun
                joueur n'a encore gagné.

        """
        if not self.echiquier.roi_de_couleur_est_dans_echiquier('noir'):
            return 'noir'
        if not self.echiquier.roi_de_couleur_est_dans_echiquier('blanc'):
            return 'blanc'
        return 'aucun'

    def partie_terminee(self):
        """Vérifie si la partie est terminée. Une partie est terminée si un gagnant peut être déclaré.

        Returns:
            bool: True si la partie est terminée, et False autrement.

        """
        # TODO: À compléter.
        return False

    def demander_positions(self):
        """Demande à l'utilisateur d'entrer les positions de départ et d'arrivée pour faire un déplacement. Si les
        positions entrées sont valides (si le déplacement est valide), on retourne les deux positions. On doit
        redemander tant que l'utilisateur ne donne pas des positions valides.

        Returns:
            str, str: Deux chaînes de caractères représentant les deux positions valides fournies par l'utilisateurs.

        """
        while True:
            piece_position = input("Quelle pièce voulez-vous déplacer?")
            if self.echiquier.position_est_valide(piece_position) and \
                            piece_position in self.echiquier.dictionnaire_pieces and\
                            self.echiquier.couleur_piece_a_position(piece_position) == self.joueur_actif:
                position_cible = input("Vers où?")
                break
            else:
                print("Vous n'avez pas de pièces à cette position")
        return piece_position, position_cible

    def joueur_suivant(self):
        """Change le joueur actif: passe de blanc à noir, ou de noir à blanc, selon la couleur du joueur actif.

        """
        if self.joueur_actif == "blanc":
            self.joueur_actif = "noir"
        else:
            self.joueur_actif = "blanc"

        pass

    def jouer(self):
        """Tant que la partie n'est pas terminée, joue la partie. À chaque tour :
            - On affiche l'échiquier.
            - On demande les deux positions.
            - On fait le déplacement sur l'échiquier.
            - On passe au joueur suivant.

        Une fois la partie terminée, on félicite le joueur gagnant!

        """
        print(self.echiquier)

        while not self.partie_terminee():
            print("C'est au tour des", self.joueur_actif)
            position_piece, position_cible = self.demander_positions()
            deplacement, erreur = self.echiquier.deplacer(position_piece, position_cible)
            if deplacement:
                self.joueur_suivant()
                print(self.echiquier)
            else:
                print(erreur)

        pass
