import streamlit as st
from fonctionnement_app import (
    cartes,
    regles_de_validation,
    creer_salon,
    rejoindre_salon,
    definir_regle_de_validation,
    voter,
    tous_ont_vote,
    afficher_votes,
    nouveau_tour,
)

@st.cache_resource
def get_salons():
    return {}

salons = get_salons()

# Écran d'accueil (US-011)
if "code_salon" not in st.session_state:
    st.title("Planning Poker")
    pseudo = st.text_input("Votre pseudo :")
    st.write("---")
    
    st.write("### Créer un salon")
    if st.button("Créer"):
        if pseudo:
            code = creer_salon(salons, pseudo)
            st.session_state.code_salon = code
            st.session_state.pseudo = pseudo
            st.rerun()
        else:
            st.error("Pseudo requis")

    st.write("### Rejoindre un salon")
    code_saisi = st.text_input("Code du salon :")
    if st.button("Rejoindre"):
        if pseudo and rejoindre_salon(salons, code_saisi, pseudo):
            st.session_state.code_salon = code_saisi
            st.session_state.pseudo = pseudo
            st.rerun()
        else:
            st.error("Erreur : code ou pseudo invalide")

# Écran du salon (US-011)
else:
    code = st.session_state.code_salon
    pseudo = st.session_state.pseudo
    
    if code not in salons:
        del st.session_state.code_salon
        st.rerun()

    salon = salons[code]
    visibles = salon.get("cartes_visibles", False)
    tour = salon.get("tour", 1)
    tour_demarre = salon.get("tour_demarre", False)
    regle = salon.get("regle_de_validation", None)
    resultat_tour = salon.get("resultat_tour")
    valeur_resultat = salon.get("valeur_resultat")
    tous_voté = tous_ont_vote(salon)


    st.title(f"Salon de jeu - Tour **{tour}**")
    st.write(f"Code à partager : **{code}** | Joueur : **{pseudo}**")
    if regle:
        st.write(f"Règle de validation : **{regle}**")
    st.write("---")

    # Selection d'une règle de validation réservée au créateur de session (US-02) + conditions de validitée règles sélectionnées (US-02 + US-03)
    if not tour_demarre:
        if pseudo == salon["createur"]:
            st.write("### Définir la règle de validation pour ce tour :")
            if tour == 1:
                options_regles = list(regles_de_validation)
            else:
                options_regles = [r for r in regles_de_validation if r != "stricte au premier tour"]
            regle_selectionnee = st.selectbox("Règle :", options_regles, key=f"select_regle_tour_{tour}")
            if st.button("Valider la règle", key="btn_valider_regle"):
                definir_regle_de_validation(salons, code, regle_selectionnee)
                st.rerun()
        else:
            st.warning("En attente de la définition de la règle par le créateur du salon...")

    else:

        # Sélection d'une carte (US-012)
        st.write("### Choisissez votre carte :")
        colonnes = st.columns(6)
        for i, carte in enumerate(cartes):
            with colonnes[i % 6]:
                if st.button(carte, key=f"btn_{carte}"):
                    voter(salons, code, pseudo, carte)
                    st.rerun()

        mon_vote = salon["votes"].get(pseudo)
        if mon_vote is not None:
            st.info(f"Votre carte sélectionnée : **{mon_vote}**")

        st.write("---")

        # Afficher les résultats d'un tour + conditions de validité d'un tour (US-02)
        if visibles and resultat_tour is not None:
            if resultat_tour is True:
                votes_joueurs = [salon["votes"][j] for j in salon["joueurs"]]
                regle = salon.get("regle_de_validation")

                st.success("Résultat du tour : tous les votes sont identiques. Le tour est **valide** !!")
            else:
                st.error("Résultat du tour : tous les votes ne sont pas indentiques. Le tour est **invalide**, relancez un nouveau tour !")

        # Faire afficher le résultat des votes réservé au créateur de session (US-013) + Relancer un tour réservé au créateur de session (US-02)
        if pseudo == salon["createur"]:
            if not visibles:
                if not tous_voté:
                    st.warning("En attente des votes de tous les joueurs...")
                if st.button("Afficher les cartes", key="btn_afficher", disabled=not tous_voté):
                    afficher_votes(salons, code)
                    st.rerun()
            else:
                libelle_relance = (
                    "Lancer un nouveau tour"
                    if resultat_tour is True
                    else "Relancer un tour"
                )
                if st.button(libelle_relance, key="btn_relancer"):
                    nouveau_tour(salons, code)
                    st.rerun()

    st.write("---")

    # Liste des joueurs + état de leur vote (US-011)
    st.write("### Joueurs connectés :")
    for joueur in salon["joueurs"]:
        vote_joueur = salon["votes"].get(joueur)
        if vote_joueur is not None:
            if salon.get("cartes_visibles", False):
                st.write(f"- {joueur} : **{vote_joueur}**")
            else:
                st.write(f"- {joueur} : a choisi une carte")
        else:
            st.write(f"- {joueur} : en attente...")
        
    st.write("---")
    if st.button("Actualiser"):
        st.rerun()
    if st.button("Quitter"):
        del st.session_state.code_salon
        st.rerun()