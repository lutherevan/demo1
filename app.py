import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

st.title("Business Performance Dashboard")

quarterly_revenue = {"Q1": "1.2M", "Q2": "1.5M", "Q3": "1.3M"}

col1, col2, col3 = st.columns(3)
with col1:
        st.header(f"Q1")
        st.write(f"Q1: {quarterly_revenue["Q1"]}")
with col2:
        st.header(f"Q2")
        st.write(f"Q2: {quarterly_revenue["Q2"]}")
with col3:
        st.header(f"Q3")
        st.write(f"Q3: {quarterly_revenue["Q3"]}")
