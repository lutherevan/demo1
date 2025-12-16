import streamlit as st 
from streamlit_option_menu import option_menu
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


quarter_revenue = {
  "Q1": "1.3M",
  "Q2": "1.5M",
  "Q3": "1.3M",
  "Q4": "1.6M"}

selected_quarter = st.selectbox(
  "Choose Quarter:",
  ["Q1", "Q2", "Q3", "Q4"])



st.write(f"Revenue for {selected_quarter}: {quarter_revenue[selected_quarter]}")

if st.button("Click here for motivation"):
  st.write("Keep pushing for growth!")

with st.sidebar:
  selected = option_menu("Menu",
                 ["Welcome", "Details", "Apply Now!"],
                 default_index = 0)
