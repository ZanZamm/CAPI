from poker_logic import creer_salon, rejoindre_salon


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

    # Code inexistant
    succes = rejoindre_salon(salons, "99999", "Bob")

    assert succes is False


def test_rejoindre_salon_pas_de_doublon():
    salons = {}
    code = creer_salon(salons, "Alice")

    # Alice tente de rejoindre à nouveau
    rejoindre_salon(salons, code, "Alice")

    assert salons[code]["joueurs"].count("Alice") == 1