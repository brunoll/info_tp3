# -*- coding: utf-8 -*-
"""Exemples de tests unitaires pour les pièces. Aucun test n'est à remettre, mais vous êtes fortement conseillés de
vous en programmer pour valider vos programmes.

"""
from pychecs.piece import Piece, Pion


def test_couleur():
    # Test de méthodes de la classe de base Pion.
    piece = Piece('noir', True)
    assert piece.est_noir()

    piece = Piece('blanc', False)
    assert piece.est_blanc()


def test_mouvements_pion():
    # Quelques tests de déplacements de pion blanc.
    pion = Pion('blanc')
    assert pion.peut_se_deplacer_vers('b2', 'b3')
    assert not pion.peut_se_deplacer_vers('b2', 'c3')
    assert not pion.peut_se_deplacer_vers('c2', 'c1')
    assert not pion.peut_se_deplacer_vers('c2', 'c2')

    # Quelques tests de déplacements de pion noir.
    pion = Pion('noir')
    assert not pion.peut_se_deplacer_vers('b2', 'b3')
    assert not pion.peut_se_deplacer_vers('b3', 'c2')
    assert pion.peut_se_deplacer_vers('c2', 'c1')


def test_prises_pion():
    # Quelques tests de prises par un pion blanc.
    pion = Pion('blanc')
    assert pion.peut_faire_une_prise_vers('b2', 'c3')
    assert pion.peut_faire_une_prise_vers('b2', 'a3')
    assert not pion.peut_faire_une_prise_vers('b2', 'b3')
    assert not pion.peut_faire_une_prise_vers('c2', 'c1')
    assert not pion.peut_faire_une_prise_vers('c2', 'c2')

    # Quelques tests de prises par un pion noir.
    pion = Pion('noir')
    assert not pion.peut_faire_une_prise_vers('b2', 'c3')
    assert not pion.peut_faire_une_prise_vers('b2', 'a3')
    assert pion.peut_faire_une_prise_vers('b3', 'c2')
    assert not pion.peut_faire_une_prise_vers('c2', 'c1')


def test_mouvements_pion_deplacement_depart():
    # Quelques tests pour le mouvement initial d'un pion: il peut sauter 2 cases.
    pion = Pion('blanc')
    assert pion.peut_se_deplacer_vers('b2', 'b4')
    assert pion.peut_se_deplacer_vers('g2', 'g4')
    assert not pion.peut_se_deplacer_vers('b2', 'b5')
    assert not pion.peut_se_deplacer_vers('c3', 'c5')

    pion = Pion('noir')
    assert not pion.peut_se_deplacer_vers('b2', 'b4')
    assert pion.peut_se_deplacer_vers('b7', 'b5')
    assert pion.peut_se_deplacer_vers('h7', 'h5')
    assert not pion.peut_se_deplacer_vers('d7', 'd4')
    assert not pion.peut_se_deplacer_vers('d8', 'd6')


if __name__ == '__main__':
    # Exécution des tests unitaires. Pour les intéressés, sachez qu'il existe des outils pour trouver
    # et exécuter automatiquement tous les tests unitaires d'un projet, notamment l'outil py.test.

    test_couleur()
    test_mouvements_pion()
    test_prises_pion()
    test_mouvements_pion_deplacement_depart()
