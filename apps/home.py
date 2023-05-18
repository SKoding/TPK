import streamlit as st
import leafmap.foliumap as leafmap


def app():
    st.markdown(
        """
        # TREE PACT KENYA
        A GIS-based Approach towards identifying areas to plant trees, Planning & Implementation of planting exercise and Tree Growth Monitoring. 
    """
    )
    kenya = [0,36]

    m = leafmap.Map(center = kenya, zoom = 10, locate_control=True)
    m.add_basemap("ROADMAP")
    m.to_streamlit(height=700)
