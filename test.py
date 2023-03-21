import streamlit as st
import pandas as pd
import random
import os
import glob


df=pd.read_excel('flower-how.xlsx',index_col=0)
st.write(df)
st.markdown(df.loc['rose']['description'])


def load_random_image(label):
    directory="./flowers/"+label+"/"
    images=glob.glob(directory+"*.jpg")
    random_image=random.choice(images)
    return st.image(random_image)

    
    
load_random_image('rose')

image1="./flowers/rose/353897245_5453f35a8e.jpg"
st.image(image1)