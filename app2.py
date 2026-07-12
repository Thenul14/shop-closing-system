import streamlit as st
import time

st.set_page_config(
    page_title="Cashier Balance System",
    page_icon="💷",
    layout="wide"
)

st.title("💷 Cashier Balance System")

st.write(
    """
    Welcome!

    Press the button below to start end of the day calculations.
    """
)

if st.button("Let's start"):
    
    with st.spinner("Starting......"):
        time.sleep(1)
        st.switch_page("pages/No_Of_Tills.py")