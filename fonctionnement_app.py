import random

def creer_salon(salons, pseudo):
    code = str(random.randint(1000, 9999))
    salons[code] = {
        "createur": pseudo,
        "joueurs": [pseudo]
    }
    return code

def rejoindre_salon(salons, code, pseudo):
    if code in salons:
        if pseudo not in salons[code]["joueurs"]:
            salons[code]["joueurs"].append(pseudo)
        return True
    return False