import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import io

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

def display_statistics(data):
    st.title('Page Statistiques')

    st.subheader("Statistiques des données sélectionnées")
    st.write("Ci-dessous, vous trouverez quelques statistiques pour certaines colonnes :")

    # List of columns for which we want to display statistics
    columns_for_statistics = st.multiselect(
        "Sélectionnez les colonnes pour afficher les statistiques", data.columns.tolist()
    )

    if columns_for_statistics:
        selected_data = data[columns_for_statistics]
        statistics = selected_data.describe()
        st.write(statistics)

        # Display histograms for selected columns
        st.subheader("Histogrammes pour les colonnes sélectionnées")

        # Check the number of selected columns
        if len(columns_for_statistics) == 2:
            # Create a joint histogram for two selected columns
            fig, ax = plt.subplots(figsize=(8, 6))
            sns.histplot(data=selected_data, x=columns_for_statistics[0], y=columns_for_statistics[1], ax=ax)
            st.pyplot(fig)
            # Add download button for the displayed graph
            download_button(fig, "Télécharger le graphique")
        elif len(columns_for_statistics) == 3:
            st.write("Trop de variables pour pouvoir faire un histogramme.")
        else:
            # Create individual histograms for each selected column
            for column in columns_for_statistics:
                fig, ax = plt.subplots(figsize=(8, 6))
                sns.histplot(selected_data[column], kde=True, ax=ax)
                st.pyplot(fig)
                # Add download button for each displayed graph
                download_button(fig, f"Télécharger le graphique - {column}")
    else:
        st.write("Sélectionnez au moins une colonne pour afficher les statistiques et les graphiques.")

def download_button(figure, label):
    # Function to generate download button for the provided figure
    buffer = io.BytesIO()
    figure.savefig(buffer, format='png')
    buffer.seek(0)
    st.download_button(label, buffer, file_name='graphique.png', mime='image/png')

def main():
    st.title('Statistiques - Page 3')

    # Load data
    data = load_data()

    # Display statistics and graphs
    if not data.empty:
        display_statistics(data)

if __name__ == '__main__':
    main()




