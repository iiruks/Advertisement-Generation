import openai
import streamlit as st

api_key = ""
def ImageGenerator_logic(text):
    user_prompt = f"Generate an advertisement for {text}"
    response = openai.images.generate(
        model="dall-e-3",
        prompt=user_prompt,
        n=1,
        quality="standard",
    )

    image_url = response.data[0].url
    return st.image(image_url)
