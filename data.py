import numpy as np
import pandas as pd
import streamlit as st

def app(car_df):
    st.header("View Data")
    with st.beta_expander("View Dataset"):
        st.table(car_df)

    st.subheader("Columns Description:")
    if st.checkbox("Show summary"):
        st.table(car_df.describe())