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

def display_database(data):
    st.title('Page 1 - Base de Données')
    st.subheader("Base de Données")
    st.dataframe(data.style.set_table_styles([{'selector': 'thead', 'props': 'color:#337ab7; background-color:#f5f5f5;'}]))

def main():
    st.title('Vélib Station Data - Page 1')

    # Load data
    data = load_data()

    # Display data
    if not data.empty:
        display_database(data)

if __name__ == '__main__':
    main()
