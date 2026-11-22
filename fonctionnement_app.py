import random

cartes = ["0", "1", "2", "3", "5", "8", "13", "20", "40", "100", "?", "☕"]

regles_de_validation = [
    "stricte",
    "stricte au premier tour",
    "moyenne",
    "médiane",
    "majorité absolue",
    "majorité relative",
]

# Création de salon (US-011)
def creer_salon(salons, pseudo):
    code = str(random.randint(1000, 9999))
    salons[code] = {
        "createur": pseudo,
        "joueurs": [pseudo],
        "votes": {pseudo: None},
        "cartes_visibles": False,
        "tour": 1,
        "regle_de_validation": None,
        'tour_demarre': False,
        "resultat_tour": None,
    }
    return code

# Rejoindre un salon via un code (US-011)
def rejoindre_salon(salons, code, pseudo):
    if code in salons:
        if pseudo not in salons[code]["joueurs"]:
            salons[code]["joueurs"].append(pseudo)
            salons[code]["votes"][pseudo] = None
        return True
    return False

# Sélectionner une règle de validation (US-02)
def definir_regle_de_validation(salons, code, regle):
    if code not in salons or regle not in regles_de_validation:
        return False
    if regle == "stricte au premier tour" and salons[code].get("tour", 1) != 1:
        return False
    salons[code]["regle_de_validation"] = regle
    salons[code]["tour_demarre"] = True
    salons[code]["resultat_tour"] = None
    return True

# Sélectionner une carte (US-012)
def voter(salons, code, pseudo, carte):
    if code in salons and salons[code].get("tour_demarre") and pseudo in salons[code]["joueurs"]:
        salons[code]["votes"][pseudo] = carte
        return True
    return False

# Vérifier que tous les joueurs ont voté (US-013)
def tous_ont_vote(salon):
    joueurs = salon.get("joueurs", [])
    if not joueurs:
        return False
    votes = salon.get("votes", {})
    return all(votes.get(joueur) is not None for joueur in joueurs)

# Calculer le résultats des votes selon les conditions de validité de chaques règles (US-02 + US-03 + US-04)
def resultat_tour(salon):
    if not salon.get("cartes_visibles") or not tous_ont_vote(salon):
        return None
    regle = salon.get("regle_de_validation")
    votes_joueurs = [salon["votes"][joueur] for joueur in salon["joueurs"]]

    if regle in ("stricte"):
        if len(set(votes_joueurs)) != 1:
            return False
        if votes_joueurs[0] in ("?"):
            return False
        return True

    if regle in ("stricte au premier tour"):
        if len(set(votes_joueurs)) != 1:
            return False
        if votes_joueurs[0] in ("?"):
            return False
        return True

    # if regle in ("moyenne"):
    #     # a completer

    # if regle in ("médiane"):
    #     # a completer
    
    # if regle in ("majorité absolue"):
    #     # a completer

    # if regle in ("majorité relative"):
    #     # a completer
    
    return None

# Révéler les votes (US-013)
def afficher_votes(salons, code):
    if code in salons and tous_ont_vote(salons[code]):
        salons[code]["cartes_visibles"] = True
        salons[code]["resultat_tour"] = resultat_tour(salons[code])
        return True
    return False

# Recommencer un nouveau tour ou relancer un tour (US-02)
def nouveau_tour(salons, code):
    if code not in salons:
        return False
    salon = salons[code]
    regle_actuelle = salon.get("regle_de_validation")
    resultat_precedent = salon.get("resultat_tour")

    # Vérouillage sur la règle stricte qui ne permet pas de sélectionner une autre règle si le tour précédent était invalide
    verrou_stricte = (regle_actuelle == "stricte" and resultat_precedent is not True)

    # Tour valide -> Nouveau tour 1, Tour invalide -> Relance un tour + 1
    if resultat_precedent is True:
        salon["tour"] = 1
    else:
        salon["tour"] = salon.get("tour", 1) + 1

    salon["cartes_visibles"] = False
    salon["resultat_tour"] = None
    for joueur in salon["joueurs"]:
        salon["votes"][joueur] = None

    if verrou_stricte:
        salon["regle_de_validation"] = "stricte"
        salon["tour_demarre"] = True
    else:
        salon["regle_de_validation"] = None
        salon["tour_demarre"] = False

    return True
