import streamlit as st
from fonctionnement_app import (
    cartes, 
    creer_salon, 
    rejoindre_salon, 
    voter, 
    afficher_votes,
)

@st.cache_resource
def get_salons():
    return {}

salons = get_salons()

# Écran d'accueil
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

# Écran du salon
else:
    code = st.session_state.code_salon
    pseudo = st.session_state.pseudo
    
    if code not in salons:
        del st.session_state.code_salon
        st.rerun()

    salon = salons[code]

    st.title("Salon de jeu")
    st.write(f"Code à partager : **{code}** | Joueur : **{pseudo}**")
    st.write("---")

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

    # Cacher ou afficher les cartes réservé au créateur de session (US-013)
    if pseudo == salon["createur"]:
        visibles = salon.get("cartes_visibles", False)
        boutons_hide_and_show = "Cacher les cartes" if visibles else "Afficher les cartes"
        if st.button(boutons_hide_and_show, key="btn_hide_show"):
            afficher_votes(salons, code)
            st.rerun()
    
    # Liste des joueurs et état de leur vote
    st.write("### Joueurs connectés :")
    for joueur in salon["joueurs"]:
        vote_joueur = salon["votes"].get(joueur)
        if vote_joueur is not None:
            if salon.get("cartes_visibles", False):
                st.write(f"- {joueur} : a choisi la carte **{vote_joueur}**")
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