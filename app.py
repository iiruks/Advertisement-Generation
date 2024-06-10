import os
import sys
import pandas as pd
import altair as alt
import streamlit as st
from image_generator import ImageGenerator_logic
from fine_tuned import AdGenerator_logic

st.markdown(
    """
    <style>
    .main {
        background-color: #f0f2f6;
        color: #333333;
        font-family: Arial, sans-serif;
        font-size: 16px;
    }
    .stButton button {
        background-color: #ff4b4b;
        color: white;
        border-radius: 10px;
        padding: 10px 20px;
        font-family: Arial, sans-serif;
        font-size: 16px;
    }
    .stButton button:hover {
        background-color: #ff6b6b;
        color: white;
    }
    .sidebar .sidebar-content {
        background-color: #f8f9fa;
        font-family: Arial, sans-serif;
        font-size: 16px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("Ad Generator")

brand = st.text_area("### Enter brand name", height=50)
tagline = st.text_area("### Enter tagline", height=50)
pd = st.text_area("### Enter product description", height=50)

st.sidebar.header("⚙️")
n = st.sidebar.slider("Number of Generations", min_value=1, max_value=10, step=1, value=5)
length_option = ['Short', 'Medium', 'Long']
l = st.sidebar.select_slider("Output Length", options=length_option, value='Medium')
c = st.sidebar.slider("Creativity", min_value=0.0, max_value=1.0, step=0.1, value=0.5)

length_mapping = {'Short': 64, 'Medium': 128, 'Long': 256}
length = length_mapping[l]

show_images = st.sidebar.checkbox("Show Images", value=True)

if st.button('Generate'):
    if not brand or not tagline or not pd:
        st.error("Please fill in all the required fields: brand name, tagline, and product description.")
    else:
        st.subheader("Generations")

        for gen in range(n):
            response = AdGenerator_logic(brand, tagline, pd, num=1, length=length, creative=c)
            output = response.choices[0].text.strip()
            st.write(f"### Ad {gen + 1}:")
            st.success(output)

            if show_images:
                st.write("#### Image")
                ImageGenerator_logic(output)

if st.button("Save Ads & Images"):
    st.info("Saved")


