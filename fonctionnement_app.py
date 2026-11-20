import random

cartes = ["0", "1", "2", "3", "5", "8", "13", "20", "40", "100", "?", "☕"]

def creer_salon(salons, pseudo):
    code = str(random.randint(1000, 9999))
    salons[code] = {
        "createur": pseudo,
        "joueurs": [pseudo],
        "votes": {pseudo: None},
        "cartes_visibles": False,
    }
    return code

def rejoindre_salon(salons, code, pseudo):
    if code in salons:
        if pseudo not in salons[code]["joueurs"]:
            salons[code]["joueurs"].append(pseudo)
            salons[code]["votes"][pseudo] = None
        return True
    return False

def voter(salons, code, pseudo, carte):
    if code in salons and pseudo in salons[code]["joueurs"]:
        salons[code]["votes"][pseudo] = carte
        return True
    return False

def afficher_votes(salons, code):
    if code in salons:
        salons[code]["cartes_visibles"] = not salons[code].get("cartes_visibles", False)
        return True
    return False