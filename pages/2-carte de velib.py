import streamlit as st
import pandas as pd
import folium
from folium.plugins import MarkerCluster
from streamlit_folium import folium_static

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

def display_map(data):
    st.title('Page 2 - Carte Vélib')
    st.subheader("Carte Vélib")

    # Create a folium map centered on the first station
    map_center = [data['Latitude'].iloc[0], data['Longitude'].iloc[0]]
    m = folium.Map(location=map_center, zoom_start=12)

    # Create a MarkerCluster
    marker_cluster = MarkerCluster().add_to(m)

    # Add circle markers for each station to the MarkerCluster
    for index, row in data.iterrows():
        folium.CircleMarker(
            location=[row['Latitude'], row['Longitude']],
            radius=5,
            popup = row['Nom station'],
            color='blue',
            fill=True,
            fill_color='blue'
        ).add_to(marker_cluster)

    # Display the map
    folium_static(m)

def main():
    st.title('Vélib Station Data - Page 2')

    # Load data
    data = load_data()

    # Display map
    if not data.empty:
        display_map(data)

if __name__ == '__main__':
    main()
