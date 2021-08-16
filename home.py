import streamlit as st
import pandas as pd
import numpy as np

def app():
  st.header("Car price prediction app")
  st.text('''This will allow user to predict price of car based on 
    engine size, horse power, dimension and drive wheel tyre parameters''')