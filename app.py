import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

color = st.selectbox("Pick a color:", ["Red", "Green", "Blue"])
st.write(f"You selected: {color}")
