import streamlit as st
from fonctionnement_app import creer_salon, rejoindre_salon

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
    if code not in salons:
        del st.session_state.code_salon
        st.rerun()

    st.title("Salon de jeu")
    st.write(f"Code à partager : **{code}**")
    st.write("---")
    
    st.write("### Joueurs connectés :")
    for joueur in salons[code]["joueurs"]:
        st.write(f"- {joueur}")
        
    st.write("---")
    if st.button("Actualiser"):
        st.rerun()
    if st.button("Quitter"):
        del st.session_state.code_salon
        st.rerun()
