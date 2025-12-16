import streamlit as st
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

quarter_revenue.values()

# st.write(f"Revenue for {selected_quarter}: {quarter_revenue.values[selected_quarter]}")
