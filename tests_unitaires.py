from fonctionnement_app import creer_salon, rejoindre_salon, voter

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