import pandas as pd
import streamlit as st

First_button = st.button("Click me")

if First_button:
        st.text("Button clicked!")

name = st.text_input("Name")
age = st.number_input("Age")
submitted = st.form_submit_button("Submit")

if submitted:
    st.write(name, age)


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
