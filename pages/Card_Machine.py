import streamlit as st
import time
from cardmachine import CardMachine


if "cardmachine1" not in st.session_state:
    st.session_state.cardmachine1 = None
if "cardmachine2" not in st.session_state:
    st.session_state.cardmachine2 = None

st.subheader("Let's check the money in the card machine.")

if st.session_state["number_of_tills"] == 1:
    till_cardmachine_amount = st.number_input("Enter the amount in card machine: ", min_value=0.0, value=0.0, step=0.01, format="%.2f")
    till_cardmachine_no_of_transactions = st.number_input("Enter the no of transactions in card machine: ", min_value=0)
    st.session_state["cardmachine1"] = CardMachine(till_cardmachine_amount, till_cardmachine_no_of_transactions)

if st.session_state["number_of_tills"] == 2:
    col1, col2 = st.columns(2)
    with col1:
        st.header("Till 1")
        till1_cardmachine_amount = st.number_input("Enter the amount in card machine connected to till 1: ", min_value=0.0, value=0.0, step=0.01, format="%.2f")
        till1_cardmachine_no_of_transactions = st.number_input("Enter the no of transactions in card machine connected to till 1: ", min_value=0)
        st.session_state["cardmachine1"] = CardMachine(till1_cardmachine_amount, till1_cardmachine_no_of_transactions)
    with col2:
        st.header("Till 2")
        till2_cardmachine_amount = st.number_input("Enter the amount in card machine connected to till 2: ", min_value=0.0, value=0.0, step=0.01, format="%.2f")
        till2_cardmachine_no_of_transactions = st.number_input("Enter the no of transactions in card machine connected to till 2: ", min_value=0)
        st.session_state["cardmachine2"] = CardMachine(till2_cardmachine_amount, till2_cardmachine_no_of_transactions)
            
    
if st.button("Enter the cardmachine details"):
    
    with st.spinner("Calculating transactions"):
        time.sleep(1)
        st.switch_page("pages/Mistakes.py")