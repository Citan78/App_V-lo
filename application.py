import streamlit as st

def main():
    st.title('Bienvenue dans l\'application Vélib Station Data')

    # Ajout de texte descriptif
    st.write(
        "Cette application vous permet d'afficher les données des stations Vélib. "
        "Veuillez sélectionner une option dans le menu de navigation à gauche. "
        "Vous pourrez voir dans l'onglet la 1re page la base de données. "
        "Dans la 2e, vous pouvez voir une carte qui montre les stations de vélos disponibles. "
        "Et pour finir dans la 3e, on peut voir des statistiques sur les colonnes."
    )

    # Ajout d'une image
    st.image("velo.png", use_column_width=True)

if __name__ == '__main__':
    main()







