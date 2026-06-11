import pytest
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'app'))

from calculatrice import additionner, soustraire, multiplier, diviser

# ──────────────────────────────────────────────
#  Tests existants — ne pas modifier
# ──────────────────────────────────────────────

def test_additionner():
    assert additionner(2, 3) == 5
    assert additionner(-1, 1) == 0

def test_soustraire():
    assert soustraire(10, 4) == 6

def test_multiplier():
    assert multiplier(3, 4) == 12
    assert multiplier(0, 100) == 0

def test_diviser():
    assert diviser(10, 2) == 5.0

def test_division_par_zero():
    with pytest.raises(ValueError, match="Division par zéro impossible"):
        diviser(5, 0)

def test_additionner_grands_nombres():
    assert additionner(1_000_000, 2_000_000) == 3_000_000
# ──────────────────────────────────────────────
#  🏋️  EXERCICE — Ajoute tes propres tests ici
# ──────────────────────────────────────────────
# Objectif : écrire au moins 2 nouveaux tests
# pour chaque fonction. Chaque test doit être
# différent de ceux ci-dessus.
#
# Exemple de structure :
#
# def test_additionner_grands_nombres():
#     assert additionner(1000, 2000) == 3000
#
# À toi de jouer ! ↓
