import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

age = st.success("OPERATION BARBAROSA SUCCESS")

First_button = st.button("Click me")

if First_button:
        st.text("Button clicked!")








months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
sales = np.random.randint(5000, 20000, size=12)
expenses = np.random.randint(3000, 15000, size=12)

data = pd.DataFrame({
    "Month": months,
    "Sales": sales,
    "Expenses": expenses
})

st.sidebar.header("Filters")
selected_months = st.sidebar.multiselect("Select Months", months, default=months)
show_expenses = st.sidebar.checkbox("Show Expenses", value=True)







             

# Sample data
data = {'Product': ['A', 'B', 'C'], 
        'Sales': [1200, 850, 950], 
        'Customers': [300, 400, 350]}
df = pd.DataFrame(data)

# Show data with Streamlit elements
st.dataframe(df)                # Interactive table
st.data_editor(df)              # Editable table
st.table(df)                    # Static table

# Customize columns directly in the dataframe display
st.dataframe(df.style.format({'Sales': '${:,.0f}', 'Customers': '{:,.0f}'}))
