import openai
import os
import streamlit as st


openai.api_key = ""
def AdGenerator_logic(brand, tagline, pd, num=1, length=128, creative=1):
    print(creative)
    start_sequence = "\ndescription"
    restart_sequence = "\n"
    
    prompt_brand = brand
    prompt_tagline = tagline
    prompt_pd = pd

    response = openai.completions.create(
      model = "ft:davinci-002:personal:projectgenai:9EmPOfcf",
      prompt= 'Brand: '+ prompt_brand +'\\nTagline: '+ prompt_tagline +'\\nProductDescription: '+ prompt_pd +'\n\n###\n\n',
      temperature=creative,
      max_tokens=length,
      top_p=1,
      n=num,
      best_of=num+1,
      frequency_penalty=0,
      presence_penalty=0,
      stop=[" END"]
    )
    
    return response
