import streamlit as st
import leafmap.foliumap as leafmap


def app():
    st.title("Home")

    st.markdown(
        """
        # TREE PACT KENYA
        ## A GIS-based Approach towards identifying areas to plant trees, Planning & Implementation of planting exercise and Tree Growth Monitoring. 
    """
    )

    m = leafmap.Map(locate_control=True)
    m.add_basemap("ROADMAP")
    m.to_streamlit(height=700)
