# -*- coding: utf-8 -*-

from pychecs.piece import Pion, Tour, Fou, Cavalier, Dame, Roi, UTILISER_UNICODE


class Echiquier:
    """Classe Echiquier, implémentée avec un dictionnaire de pièces.


    Attributes:
        dictionnaire_pieces (dict): Un dictionnaire dont les clés sont des positions, suivant le format suivant:
            Une position est une chaîne de deux caractères.
            Le premier caractère est une lettre entre a et h, représentant la colonne de l'échiquier.
            Le second caractère est un chiffre entre 1 et 8, représentant la rangée de l'échiquier.
        chiffres_rangees (list): Une liste contenant, dans l'ordre, les chiffres représentant les rangées.
        lettres_colonnes (list): Une liste contenant, dans l'ordre, les lettres représentant les colonnes.

    """
    def __init__(self):
        # Le dictionnaire de pièces, vide au départ, mais ensuite rempli par la méthode initialiser_echiquier_depart().
        self.dictionnaire_pieces = {}

        # Ces listes pourront être utilisées dans les autres méthodes, par exemple pour valider une position.
        self.chiffres_rangees = ['1', '2', '3', '4', '5', '6', '7', '8']
        self.lettres_colonnes = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

        self.initialiser_echiquier_depart()

    def position_est_valide(self, position):
        """Vérifie si une position est valide (dans l'échiquier). Une position est une concaténation d'une lettre de
        colonne et d'un chiffre de rangée, par exemple 'a1' ou 'h8'.

        Args:
            position (str): La position à valider.

        Returns:
            bool: True si la position est valide, False autrement.

        """
        try:
            if position[0] in self.lettres_colonnes and position[1] in self.chiffres_rangees:
                return True
            else:
                return False
        except:
            return False

    def recuperer_piece_a_position(self, position):
        """Retourne la pièce qui est située à une position particulière, reçue en argument. Si aucune pièce n'est
        située à cette position, retourne None.

        Args:
            position (str): La position où récupérer la pièce.

        Returns:
            Piece or None: Une instance de type Piece si une pièce était située à cet endroit, et None autrement.

        """
        return self.dictionnaire_pieces[position]

    def couleur_piece_a_position(self, position):
        """Retourne la couleur de la pièce située à la position reçue en argument, et une chaîne vide si aucune
        pièce n'est à cet endroit.

        Args:
            position (str): La position où récupérer la couleur de la pièce.

        Returns:
            str: La couleur de la pièce s'il y en a une, et '' autrement.

        """
        try:
            return self.dictionnaire_pieces[position].couleur
        except:
            return ''

    def rangees_entre(self, rangee_debut, rangee_fin):
        """Retourne la liste des rangées qui sont situées entre les deux rangées reçues en argument, exclusivement.
        Attention de conserver le bon ordre.

        Args:
            rangee_debut (str): Le caractère représentant la rangée de début, par exemple '1'.
            rangee_fin (str): Le caractère représentant la rangée de fin, par exemple '4'.

        Exemple:
            >>> echiquer.rangees_entre('1', '1')
            []
            >>> echiquier.rangees_entre('2', '3')
            []
            >>> echiquier.rangees_entre('2', '8')
            ['3', '4', '5', '6', '7']
            >>> echiquier.rangees_entre('8', '3')
            ['7', '6', '5', '4']

        Indice:
            Utilisez self.chiffres_rangees pour obtenir une liste des rangées valides.

        Returns:
            list: Une liste des rangées (en str) entre le début et la fin, dans le bon ordre.

        """
        assert rangee_debut in self.chiffres_rangees and rangee_fin in self.chiffres_rangees, "Index de rangée invalide"
        position_debut = 0
        position_fin = 0
        rangees_entre = []
        for i, r in enumerate(self.chiffres_rangees):
            if r == rangee_debut:
                position_debut = i
            if r == rangee_fin:
                position_fin = i

        if position_debut < position_fin:
            for index in range(position_debut + 1, position_fin):
                rangees_entre += [self.chiffres_rangees[index]]
        elif position_debut > position_fin:
            for index in range(position_debut - 1, position_fin, -1):
                rangees_entre += [self.chiffres_rangees[index]]

        return rangees_entre

    def colonnes_entre(self, colonne_debut, colonne_fin):
        """Retourne la liste des colonnes qui sont situées entre les deux colonnes reçues en argument, exclusivement.
        Attention de conserver le bon ordre.

        Args:
            colonne_debut (str): Le caractère représentant la colonne de début, par exemple 'a'.
            colonne_fin (str): Le caractère représentant la colonne de fin, par exemple 'h'.

        Exemple:
            >>> echiquer.rangees_entre('a', 'a')
            []
            >>> echiquier.rangees_entre('b', 'c')
            []
            >>> echiquier.rangees_entre('b', 'h')
            ['c', 'd', 'e', 'f', 'g']
            >>> echiquier.rangees_entre('h', 'c')
            ['g', 'f', 'e', 'd']

        Indice:
            Utilisez self.lettres_colonnes pour obtenir une liste des colonnes valides.

        Returns:
            list: Une liste des colonnes (en str) entre le début et la fin, dans le bon ordre.

        """
        assert colonne_debut in self.lettres_colonnes and colonne_fin in self.lettres_colonnes, "Index de rangée invalide"
        position_debut = 0
        position_fin = 0
        colonne_entre = []
        for i, r in enumerate(self.lettres_colonnes):
            if r == colonne_debut:
                position_debut = i
            if r == colonne_fin:
                position_fin = i
        if position_debut < position_fin:
            for index in range(position_debut + 1, position_fin):
                colonne_entre += [self.lettres_colonnes[index]]
        elif position_debut > position_fin:
            for index in range(position_debut -1, position_fin, -1):
                colonne_entre += [self.lettres_colonnes[index]]

        return colonne_entre

    def chemin_libre_entre_positions(self, position_source, position_cible):
        """Vérifie si la voie est libre entre deux positions, reçues en argument. Cette méthode sera pratique
        pour valider les déplacements: la plupart des pièces ne peuvent pas "sauter" par dessus d'autres pièces,
        il faut donc s'assurer qu'il n'y a pas de pièce dans le chemin.

        On distingue quatre possibilités (à déterminer dans votre code): Soit les deux positions sont sur la même
        rangée, soit elles sont sur la même colonne, soit il s'agit d'une diagonale, soit nous sommes dans une
        situation où nous ne pouvons pas chercher les positions "entre" les positions source et cible. Dans les trois
        premiers cas, on fait la vérification et on retourne True ou False dépendamment la présence d'une pièce ou non.
        Dans la dernière situation, on considère que les positions reçues sont invalides et on retourne toujours False.

        Args:
            position_source (str): La position source.
            position_cible (str): La position cible.

        Warning:
            Il ne faut pas vérifier les positions source et cible, puisqu'il peut y avoir des pièces à cet endroit.
            Par exemple, si une tour "mange" un pion ennemi, il y aura une tour sur la position source et un pion
            sur la position cible.

        Returns:
            bool: True si aucune pièce n'est située entre les deux positions, et False autrement (ou si les positions
                ne permettaient pas la vérification).

        """
        rangeX = ord(position_cible[0]) - ord(position_source[0])
        rangeY = int(position_cible[1]) - int(position_source[1])

        if position_source[0] == position_cible[0]:
            rangees = self.rangees_entre(position_source[1],position_cible[1])
            for r in rangees:
                position = position_source[0] + r
                if position in self.dictionnaire_pieces.keys():
                    return False
        elif position_source[1] == position_cible[1]:
            rangees = self.colonnes_entre(position_source[0],position_cible[0])
            for r in rangees:
                position = r + position_source[1]
                if position in self.dictionnaire_pieces.keys():
                    return False
        elif abs(rangeX) == abs(rangeY):
            for i in range(1,abs(rangeY)):
                position = chr(int(ord(position_source[0])+i*rangeX/abs(rangeX))) + \
                           str(int(int(position_source[1])+i*rangeY/abs(rangeY)))
                if position in self.dictionnaire_pieces.keys():
                    return False
        else:
            return False

        return True

    def deplacement_est_valide(self, position_source, position_cible):
        """Vérifie si un déplacement serait valide dans l'échiquier actuel. Notez que chaque type de
        pièce se déplace de manière différente, vous voudrez probablement utiliser le polymorphisme :-).

        Règles pour qu'un déplacement soit valide:
            1. Il doit y avoir une pièce à la position source.
            2. La position cible doit être valide (dans l'échiquier).
            3. Si la pièce ne peut pas sauter, le chemin doit être libre entre les deux positions.
            4. S'il y a une pièce à la position cible, elle doit être de couleur différente.
            5. Le déplacement doit être valide pour cette pièce particulière.

        Args:
            position_source (str): La position source du déplacement.
            position_cible (str): La position cible du déplacement.

        Returns:
            bool: True si le déplacement est valide, et False autrement.

        """
        if position_source not in self.dictionnaire_pieces.keys() or not self.position_est_valide(position_cible):
            return False, "Il n'y a pas de pièce à cette position"

        piece = self.recuperer_piece_a_position(position_source)
        if not piece.peut_sauter:
            if not self.chemin_libre_entre_positions(position_source, position_cible):
                return False, "La pièce n'a pas accès à cette case"
        elif not piece.peut_se_deplacer_vers(position_source, position_cible):
            return False, "La pièce ne peut aller à cette position"
        return True, ""

    def deplacer(self, position_source, position_cible):
        """Effectue le déplacement d'une pièce en position source, vers la case en position cible. Vérifie d'abord
        si le déplacement est valide, et ne fait rien (puis retourne False) dans ce cas. Si le déplacement est valide,
        il est effectué (dans l'échiquier actuel) et la valeur True est retournée.

        Args:
            position_source (str): La position source.
            position_cible (str): La position cible.

        Returns:
            bool: True si le déplacement était valide et a été effectué, et False autrement.

        """
        deplacement, erreur = self.deplacement_est_valide(position_source, position_cible)
        piece = self.recuperer_piece_a_position(position_source)
        if deplacement:
            if position_cible in self.dictionnaire_pieces.keys():
                piece_cible = self.recuperer_piece_a_position(position_cible)
                if piece.couleur == piece_cible.couleur:
                    return False, "Vous ne pouvez attaquer vos propres pièces"
                if not piece.peut_faire_une_prise_vers(position_source, position_cible):
                    return False, "La pièce ne peut attaquer cette position"
                del(self.dictionnaire_pieces[position_cible])
            elif isinstance(piece, Pion):
                position_attaque = position_source[0]+str(int(position_source[1])+1)
                if piece.couleur == "blanc" and position_attaque in self.dictionnaire_pieces.keys():
                    piece_cible = self.recuperer_piece_a_position(position_attaque)
                    if piece.couleur == piece_cible.couleur:
                        return False, "Vous ne pouvez attaquer vos propres pièces"
                    if not piece.peut_faire_une_prise_vers(position_source, position_cible):
                        return False, "La pièce ne peut attaquer cette position"
                    del(self.dictionnaire_pieces[position_attaque])
                else:
                    position_attaque = position_source[0]+str(int(position_source[1])-1)
                    if piece.couleur == "noir" and position_attaque in self.dictionnaire_pieces.keys():
                        piece_cible = self.recuperer_piece_a_position(position_attaque)
                        if piece.couleur == piece_cible.couleur:
                            return False, "Vous ne pouvez attaquer vos propres pièces"
                        if not piece.peut_faire_une_prise_vers(position_source, position_cible):
                            return False, "La pièce ne peut attaquer cette position"
                        del(self.dictionnaire_pieces[position_attaque])
            self.dictionnaire_pieces[position_cible] = self.recuperer_piece_a_position(position_source)
            del(self.dictionnaire_pieces[position_source])

            return True, ""
        else:
            return False, erreur

    def roi_de_couleur_est_dans_echiquier(self, couleur):
        """Vérifie si un roi de la couleur reçue en argument est présent dans l'échiquier.

        Args:
            couleur (str): La couleur (blanc ou noir) du roi à rechercher.

        Returns:
            bool: True si un roi de cette couleur est dans l'échiquier, et False autrement.

        """
        for piece in self.dictionnaire_pieces.values():
            if isinstance(piece, Roi) and piece.couleur == couleur:
                return True
        return False

    def initialiser_echiquier_depart(self):
        """Initialise l'échiquier à son contenu initial. Pour faire vos tests pendant le développement,
        nous vous suggérons de vous fabriquer un échiquier plus simple, en modifiant l'attribut
        dictionnaire_pieces de votre instance d'Echiquier.

        """
        self.dictionnaire_pieces = {
            'a1': Tour('blanc'),
            'b1': Cavalier('blanc'),
            'c1': Fou('blanc'),
            'd1': Dame('blanc'),
            'e1': Roi('blanc'),
            'f1': Fou('blanc'),
            'g1': Cavalier('blanc'),
            'h1': Tour('blanc'),
            'a2': Pion('blanc'),
            'b2': Pion('blanc'),
            'c2': Pion('blanc'),
            'd2': Pion('blanc'),
            'e2': Pion('blanc'),
            'f2': Pion('blanc'),
            'g2': Pion('blanc'),
            'h2': Pion('blanc'),
            'a7': Pion('noir'),
            'b7': Pion('noir'),
            'c7': Pion('noir'),
            'd7': Pion('noir'),
            'e7': Pion('noir'),
            'f7': Pion('noir'),
            'g7': Pion('noir'),
            'h7': Pion('noir'),
            'a8': Tour('noir'),
            'b8': Cavalier('noir'),
            'c8': Fou('noir'),
            'd8': Dame('noir'),
            'e8': Roi('noir'),
            'f8': Fou('noir'),
            'g8': Cavalier('noir'),
            'h8': Tour('noir'),
        }

    def __repr__(self):
        """Affiche l'échiquier à l'écran. Utilise des codes Unicode, si la constante UTILISER_UNICODE est à True dans
        le module piece. Sinon, utilise seulement des caractères standards.

        Vous n'avez pas à comprendre cette partie du code.

        """
        chaine = ""
        if UTILISER_UNICODE:
            chaine += '  \u250c' + '\u2500\u2500\u2500\u252c' * 7 + '\u2500\u2500\u2500\u2510\n'
        else:
            chaine += '  +' + '----+' * 8 + '\n'

        for rangee in range(7, -1, -1):
            if UTILISER_UNICODE:
                chaine += '{} \u2502 '.format(self.chiffres_rangees[rangee])
            else:
                chaine += '{} | '.format(self.chiffres_rangees[rangee])
            for colonne in range(8):
                piece = self.dictionnaire_pieces.get('{}{}'.format(self.lettres_colonnes[colonne], self.chiffres_rangees[rangee]))
                if piece is not None:
                    if UTILISER_UNICODE:
                        chaine += str(piece) + ' \u2502 '
                    else:
                        chaine += str(piece) + ' | '
                else:
                    if UTILISER_UNICODE:
                        chaine += '  \u2502 '
                    else:
                        chaine += '   | '

            if rangee != 0:
                if UTILISER_UNICODE:
                    chaine += '\n  \u251c' + '\u2500\u2500\u2500\u253c' * 7 + '\u2500\u2500\u2500\u2524\n'
                else:
                    chaine += '\n  +' + '----+' * 8 + '\n'

        if UTILISER_UNICODE:
            chaine += '\n  \u2514' + '\u2500\u2500\u2500\u2534' * 7 + '\u2500\u2500\u2500\u2518\n'
        else:
            chaine += '\n  +' + '----+' * 8 + '\n'

        chaine += '    '
        for colonne in range(8):
            if UTILISER_UNICODE:
                chaine += self.lettres_colonnes[colonne] + '   '
            else:
                chaine += self.lettres_colonnes[colonne] + '    '
        chaine += '\n'
        return chaine


if __name__ == '__main__':
    # Exemple de __main__ qui crée un nouvel échiquier, puis l'affiche à l'éran. Vous pouvez ajouter des instructions ici
    # pour tester votre échiquier, mais n'oubliez pas que le programme principal est démarré en exécutant __main__.py.
    echiquier = Echiquier()
    print(echiquier)
