import streamlit as st
import ee
import json
import folium
import geemap.foliumap as geemap
from streamlit_folium import folium_static 


def app():
    st.title("Tree Pact Kenya.")
    # Create an interactive map

    json_data = st.secrets["json_data"]
    service_account = st.secrets["service_account"]


    json_object = json.loads(json_data, strict=False)
    json_object = json.dumps(json_object)
    credentials = ee.ServiceAccountCredentials(service_account, key_data=json_object)
    ee.Initialize(credentials)
    
    #geemap.ee_initialize()
    #Map = geemap.Map(center=[0, 36], zoom=4,plugin_Draw=True, Draw_export=False)
    # Add a basemap
    # Add custom basemaps to folium
    basemaps = {
        'Google Maps': folium.TileLayer(
            tiles = 'https://mt1.google.com/vt/lyrs=m&x={x}&y={y}&z={z}',
            attr = 'Google',
            name = 'Google Maps',
            overlay = True,
            control = True
        ),
        'Google Satellite': folium.TileLayer(
            tiles = 'https://mt1.google.com/vt/lyrs=s&x={x}&y={y}&z={z}',
            attr = 'Google',
            name = 'Google Satellite',
            overlay = True,
            control = True
        ),
        'Google Terrain': folium.TileLayer(
            tiles = 'https://mt1.google.com/vt/lyrs=p&x={x}&y={y}&z={z}',
            attr = 'Google',
            name = 'Google Terrain',
            overlay = True,
            control = True
        ),
        'Google Satellite Hybrid': folium.TileLayer(
            tiles = 'https://mt1.google.com/vt/lyrs=y&x={x}&y={y}&z={z}',
            attr = 'Google',
            name = 'Google Satellite',
            overlay = True,
            control = True
        ),
        'Esri Satellite': folium.TileLayer(
            tiles = 'https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
            attr = 'Esri',
            name = 'Esri Satellite',
            overlay = True,
            control = True
        ),
    }
    # Create a folium map object.
    my_map = folium.Map(location=[0.5, 36], zoom_start=8, height=700)
    # Add custom basemaps
    basemaps['Google Maps'].add_to(my_map)
    basemaps['Google Satellite Hybrid'].add_to(my_map)
    #Map.add_basemap("HYBRID")
    # Retrieve Earth Engine dataset
    #dem = ee.Image("USGS/SRTMGL1_003")
    # Set visualization parameters
    vis_params = {
        "min": 0,
        "max": 4000,
        "palette": ["006633", "E5FFCC", "662A00", "D8D8D8", "F5F5F5"],
    }
    # Add the Earth Engine image to the map
   # Map.addLayer(dem, vis_params, "SRTM DEM", True, 0.5)
    # Add a colorbar to the map
    #Map.add_colorbar(vis_params, label="Elevation (m)")
    # Render the map using streamlit
    folium_static(my_map)
    #Map.to_streamlit()
