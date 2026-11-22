from fonctionnement_app import (
    creer_salon,
    rejoindre_salon,
    voter,
    afficher_votes,
    tous_ont_vote,
    nouveau_tour,
    definir_regle_de_validation,
)

def test_creer_salon():
    salons = {}
    code = creer_salon(salons, "Alice")
    assert code in salons
    assert salons[code]["createur"] == "Alice"
    assert salons[code]["joueurs"] == ["Alice"]

def test_rejoindre_salon_succes():
    salons = {}
    code = creer_salon(salons, "Alice")
    succes = rejoindre_salon(salons, code, "Bob")
    assert succes is True
    assert "Bob" in salons[code]["joueurs"]

def test_rejoindre_salon_invalide():
    salons = {}
    creer_salon(salons, "Alice")
    succes = rejoindre_salon(salons, "99999", "Bob")
    assert succes is False

def test_rejoindre_salon_pas_de_doublon():
    salons = {}
    code = creer_salon(salons, "Alice")
    rejoindre_salon(salons, code, "Alice")
    assert salons[code]["joueurs"].count("Alice") == 1

def test_voter_carte():
    salons = {}
    code = creer_salon(salons, "Alice")
    succes = voter(salons, code, "Alice", "5")
    assert succes is True
    assert salons[code]["votes"]["Alice"] == "5"

def test_afficher_votes():
    salons = {}
    code = creer_salon(salons, "Alice")
    voter(salons, code, "Alice", "5")
    voter(salons, code, "Bob", "8")
    succes = afficher_votes(salons, code)
    assert succes is True
    assert salons[code]["cartes_visibles"] is True

def test_afficher_votes_invalide():
    salons = {}
    creer_salon(salons, "Alice")
    succes = afficher_votes(salons, "99999")
    assert succes is False

def test_tous_ont_vote():
    salons = {}
    code = creer_salon(salons, "Alice")
    rejoindre_salon(salons, code, "Bob")
    voter(salons, code, "Alice", "5")
    voter(salons, code, "Bob", "8")
    assert tous_ont_vote(salons[code]) is True

def test_tous_ont_vote_invalide():
    salons = {}
    code = creer_salon(salons, "Alice")
    rejoindre_salon(salons, code, "Bob")
    voter(salons, code, "Alice", "5")
    assert tous_ont_vote(salons[code]) is False

def test_nouveau_tour():
    salons = {}
    code = creer_salon(salons, "Alice")
    rejoindre_salon(salons, code, "Bob")
    voter(salons, code, "Alice", "5")
    voter(salons, code, "Bob", "8")
    afficher_votes(salons, code)
    nouveau_tour(salons, code)
    assert salons[code]["tour"] == 2
    assert salons[code]["cartes_visibles"] is False
    assert salons[code]["resultat_tour"] is None
    for joueur in salons[code]["joueurs"]:
        assert salons[code]["votes"][joueur] is None

def test_nouveau_tour_invalide():
    salons = {}
    creer_salon(salons, "Alice")
    succes = nouveau_tour(salons, "99999")
    assert succes is False

def test_definir_regle_de_validation():
    salons = {}
    code = creer_salon(salons, "Alice")
    succes = definir_regle_de_validation(salons, code, "règle stricte")
    assert succes is True
    assert salons[code]["regle_de_validation"] == "règle stricte"
    assert salons[code]["tour_demarre"] is True

def test_definir_regle_de_validation_invalide():
    salons = {}
    code = creer_salon(salons, "Alice")
    regle_invalide = "règle invalide"
    succes = definir_regle_de_validation(salons, code, regle_invalide)
    assert succes is False
    assert salons[code]["regle_de_validation"] is None
    assert salons[code]["tour_demarre"] is False