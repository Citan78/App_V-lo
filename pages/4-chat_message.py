import streamlit as st
import pandas as pd

def load_data():
    # Read the CSV data
    file = st.file_uploader("Sélectionnez un fichier CSV", type=["csv"])
    
    if file is not None:
        try:
            data = pd.read_csv(file, sep=';')
        except pd.errors.EmptyDataError:
            st.error("Le fichier CSV est vide.")
            return pd.DataFrame()
        else:
            # Split the "Coordonnées géographiques" column into separate "Latitude" and "Longitude" columns
            data[['Latitude', 'Longitude']] = data['Coordonnées géographiques'].str.split(',', expand=True).astype(float)
            return data
    else:
        return pd.DataFrame()

# Chargement des données
data = load_data()

if not data.empty:
    st.title('Bienvenue dans l\'application Vélib Station Data')

    # Affichage de la saisie de l'utilisateur
    prompt = st.text_input("Posez votre question sur les données ici :")

    # Traitement en fonction de la question posée
    if prompt:
        if "nombre de lignes" in prompt.lower():
            st.write(f"Le nombre total de lignes dans la base de données est : {len(data)}")
        elif "colonnes" in prompt.lower():
            st.write(f"Les colonnes présentes dans la base de données sont : {', '.join(data.columns)}")
        elif "afficher les premières lignes" in prompt.lower():
            num_rows = st.number_input("Combien de lignes souhaitez-vous afficher ?", min_value=1, max_value=len(data), value=5)
            st.write(f"Affichage des premières {num_rows} lignes de données :")
            st.write(data.head(num_rows))
        else:
            st.write("Désolé, je ne comprends pas votre question.")

    # Affichage de la saisie de l'utilisateur (notes)
    notes = st.text_input("Écrire ici toutes tes notes :")
    if notes:
        st.write(f"Tes notes : {notes}")

else:
    st.write("Aucune donnée chargée.")

