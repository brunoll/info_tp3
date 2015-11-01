# -*- coding: utf-8 -*-
"""Module contenant la classe de base Piece, ainsi qu'une classe fille pour chacun des types de pièces du jeu d'échecs.

"""
# TODO: Si votre système n'affiche pas correctement les caractères unicodes du jeu d'échecs,
# mettez cette constante (variable globale) à False. Un tutoriel est présent sur le site Web
# du cours pour vous aider à faire fonctionner les caractères Unicoe sous Windows.
UTILISER_UNICODE = True


class Piece:
    """Une classe de base représentant une pièce du jeu d'échecs. C'est cette classe qui est héritée plus bas pour fournir
    une classe par type de pièce (Pion, Tour, etc.).

    Attributes:
        couleur (str): La couleur de la pièce, soit 'blanc' ou 'noir'.
        peut_sauter (bool): Si oui ou non la pièce peut "sauter" par dessus d'autres pièces sur un échiquier.

    Args:
        couleur (str): La couleur avec laquelle créer la pièce.
        peut_sauter (bool): La valeur avec laquelle l'attribut peut_sauter doit être initialisé.

    """
    def __init__(self, couleur, peut_sauter):
        # Validation si la couleur reçue est valide.
        assert couleur in ('blanc', 'noir')

        # Création des attributs avec les valeurs reçues.
        self.couleur = couleur
        self.peut_sauter = peut_sauter

    def est_blanc(self):
        """Retourne si oui ou non la pièce est blanche.

        Returns:
            bool: True si la pièce est blanche, et False autrement.

        """
        return self.couleur == 'blanc'

    def est_noir(self):
        """Retourne si oui ou non la pièce est noire.

        Returns:
            bool: True si la pièce est noire, et False autrement.

        """
        return self.couleur == 'noir'

    def peut_se_deplacer_vers(self, position_source, position_cible):
        """Vérifie si, selon les règles du jeu d'échecs, la pièce peut se déplacer d'une position à une autre.

        Une position est une chaîne de deux caractères.
            Le premier caractère est une lettre entre a et h, représentant la colonne de l'échiquier.
            Le second caractère est un chiffre entre 1 et 8, représentant la rangée de l'échiquier.

        Args:
            position_source (str): La position source, suivant le format ci-haut. Par exemple, 'a8', 'f3', etc.
            position_cible (str): La position cible, suivant le format ci-haut. Par exemple, 'b6', 'h1', etc.

        Warning:
            Comme nous sommes dans la classe de base et non dans l'une des classes filles, nous ne savons pas
            (encore) comment cette pièce se déplace. Cette méthode est donc à redéfinir dans chacune des
            classes filles.

        Warning:
            Comme la classe Piece est indépendante de l'échiquier (et donc on ne sait pas si une pièce est "dans le
            chemin"), on doit ignorer le contenu de l'échiquier : on ne se concentre que sur les règles de mouvement
            des pièces.

        Returns:
            bool: True si le déplacement est valide en suivant les règles de la pièce, et False autrement.

        """
        # On lance une exception (on y reviendra) indiquant que ce code n'a pas été implémenté. Ne touchez pas
        # à cette méthode : réimplémentez-la dans les classes filles!
        raise NotImplementedError

    def peut_faire_une_prise_vers(self, position_source, position_cible):
        """Vérifie si, selon les règles du jeu d'échecs, la pièce peut "manger" (faire une prise) une pièce ennemie.
        Pour la plupart des pièces, la règle est la même, on appelle donc la méthode peut_se_deplacer_vers.

        Si ce n'est pas le cas pour une certaine pièce, on peut simplement redéfinir cette méthode pour programmer
        la règle.

        Args:
            position_source (str): La position source, suivant le format ci-haut. Par exemple, 'a8', 'f3', etc.
            position_cible (str): La position cible, suivant le format ci-haut. Par exemple, 'b6', 'h1', etc.

        Returns:
            bool: True si la prise est valide en suivant les règles de la pièce, et False autrement.

        """
        return self.peut_se_deplacer_vers(position_source, position_cible)


class Pion(Piece):
    """Le pion se déplace d’une case à la fois vers l’avant, c’est à dire vers le haut de l’échiquier
    pour les pièces blanches, et vers le bas de l’échiquier pour les pièces noires. Lorsque le
    pion est à sa position initiale, il peut avancer de 2 cases vers l’avant plutôt qu’une.

    Le pion est la seule pièce du jeu d’échecs qui fait ses prises (action de « manger » une pièce
    ennemi) de manière différente que son mouvement standard : le pion fait une prise en
    diagonale, encore une fois vers l’avant seulement.

    Un pion ne peut pas sauter par dessus une autre pièce.

    Attributes:
        couleur (str): La couleur de la pièce, soit 'blanc' ou 'noir'.

    Args:
        couleur (str): La couleur avec laquelle créer la pièce.

    """
    def __init__(self, couleur):
        super().__init__(couleur, False)

    def peut_se_deplacer_vers(self, position_source, position_cible):
        if position_source[0] == position_cible[0]:
            if self.couleur == 'noir':
                if position_source[1] == '7':
                    if int(position_cible[1]) == 5 or int(position_cible[1]) == 6:
                        return True
                elif int(position_cible[1]) == int(position_source[1]) - 1:
                        return True
            else:
                if position_source[1] == '2':
                    if int(position_cible[1]) == 3 or int(position_cible[1]) == 4:
                        return True
                elif int(position_cible[1]) == int(position_source[1]) + 1:
                        return True

        return False

    def peut_faire_une_prise_vers(self, position_source, position_cible):
        if self.couleur == 'noir':
            return abs(ord(position_source[0]) - ord(position_cible[0])) == 1 and int(position_cible[1]) == int(position_source[1]) - 1
        else:
            return abs(ord(position_source[0]) - ord(position_cible[0])) == 1 and int(position_cible[1]) == int(position_source[1]) + 1

    def __repr__(self):
        """Redéfinit comment on affiche un pion à l'écran. Nous utilisons la constante UTILISER_UNICODE
        pour déterminer comment afficher le pion.

        Returns:
            str: La chaîne de caractères représentant le pion.

        """
        if self.est_blanc():
            if UTILISER_UNICODE:
                return '\u2659'
            else:
                return 'PB'
        else:
            if UTILISER_UNICODE:
                return '\u265f'
            else:
                return 'PN'


class Tour(Piece):
    """La tour se déplace (et fait ses prises) en se déplaçant le long des rangées et des colonnes,
    d’un nombre quelconque de positions. Une tour ne peut pas sauter par dessus une autre
    pièce.

    Attributes:
        couleur (str): La couleur de la pièce, soit 'blanc' ou 'noir'.

    Args:
        couleur (str): La couleur avec laquelle créer la pièce.

    """
    def __init__(self, couleur):
        super().__init__(couleur, False)

    def __repr__(self):
        if self.est_blanc():
            if UTILISER_UNICODE:
                return '\u2656'
            else:
                return 'TB'
        else:
            if UTILISER_UNICODE:
                return '\u265c'
            else:
                return 'TN'

    def peut_se_deplacer_vers(self, position_source, position_cible):
        return abs(ord(position_source[0]) - ord(position_cible[0])) == 0 or abs(ord(position_source[1]) - ord(position_cible[1])) == 0


class Cavalier(Piece):
    """Le cavalier se déplace en forme de « L », c’est à dire d’une rangée puis de deux colonnes, ou
    bien de deux rangées puis d’une colonne. Le cavalier peut sauter par dessus des pièces,
    tant qu’il termine son mouvement sur une case libre (ou avec une pièce de couleur adverse).

    Attributes:
        couleur (str): La couleur de la pièce, soit 'blanc' ou 'noir'.

    Args:
        couleur (str): La couleur avec laquelle créer la pièce.

    """
    def __init__(self, couleur):
        super().__init__(couleur, True)

    def __repr__(self):
        if self.est_blanc():
            if UTILISER_UNICODE:
                return '\u2658'
            else:
                return 'CB'
        else:
            if UTILISER_UNICODE:
                return '\u265e'
            else:
                return 'CN'

    def peut_se_deplacer_vers(self, position_source, position_cible):
        return (abs(ord(position_cible[0])-ord(position_source[0])) == 2 and abs(int(position_cible[1])-int(position_source[1])) == 1) or\
               (abs(ord(position_cible[0])-ord(position_source[0])) == 1 and abs(int(position_cible[1])-int(position_source[1])) == 2)


class Fou(Piece):
    """Le fou se déplace (et fait ses prises) en se déplaçant en diagonale, d’un nombre quelconque
    de positions. Un fou ne peut pas sauter par dessus une autre pièce.

    Attributes:
        couleur (str): La couleur de la pièce, soit 'blanc' ou 'noir'.

    Args:
        couleur (str): La couleur avec laquelle créer la pièce.

    """
    def __init__(self, couleur):
        super().__init__(couleur, False)

    def __repr__(self):
        if self.est_blanc():
            if UTILISER_UNICODE:
                return '\u2657'
            else:
                return 'FB'
        else:
            if UTILISER_UNICODE:
                return '\u265d'
            else:
                return 'FN'

    def peut_se_deplacer_vers(self, position_source, position_cible):
        return abs(ord(position_source[0]) - ord(position_cible[0])) == abs(int(position_source[1]) - int(position_cible[1]))


class Roi(Piece):
    """Le roi est la pièce la plus importante du jeu : perdre son roi signifie que nous avons perdu
    la partie. Le roi se déplace (et fait ses prises) d’une seule case à la fois, dans n’importe
    quelle direction (rangée, colonne ou diagonale)

    Attributes:
        couleur (str): La couleur de la pièce, soit 'blanc' ou 'noir'.

    Args:
        couleur (str): La couleur avec laquelle créer la pièce.

    """
    def __init__(self, couleur):
        super().__init__(couleur, False)

    def __repr__(self):
        if self.est_blanc():
            if UTILISER_UNICODE:
                return '\u2654'
            else:
                return 'RB'
        else:
            if UTILISER_UNICODE:
                return '\u265a'
            else:
                return 'RN'

    def peut_se_deplacer_vers(self, position_source, position_cible):
        return abs(ord(position_cible[0])-ord(position_source[0])) <= 1 and abs(int(position_cible[1])-int(position_source[1])) <= 1


class Dame(Piece):
    """La dame combine les mouvements de la tour et du fou : elle se déplace et fait ses prises
    soit le long d’une rangée ou d’une colonne, ou bien en diagonale. Elle ne peut pas sauter
    par dessus une pièce adverse.

    Attributes:
        couleur (str): La couleur de la pièce, soit 'blanc' ou 'noir'.

    Args:
        couleur (str): La couleur avec laquelle créer la pièce.

    """
    def __init__(self, couleur):
        super().__init__(couleur, False)

    def __repr__(self):
        if self.est_blanc():
            if UTILISER_UNICODE:
                return '\u2655'
            else:
                return 'DB'
        else:
            if UTILISER_UNICODE:
                return '\u265b'
            else:
                return 'DN'

    def peut_se_deplacer_vers(self, position_source, position_cible):
        return abs(ord(position_source[0]) - ord(position_cible[0])) == abs(int(position_source[1]) - int(position_cible[1])) or \
                abs(ord(position_source[0]) - ord(position_cible[0])) == 0 or abs(int(position_source[1]) - int(position_cible[1])) == 0
