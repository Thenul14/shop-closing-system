import streamlit as st
import time
from till import Till
from cardmachine import CardMachine

if "till1" not in st.session_state:
    st.session_state.till1= None
if "till2" not in st.session_state:
    st.session_state.till2 = None

st.subheader("Enter no of each notes/coins in the till below.")

number_of_tills = st.session_state["number_of_tills"]

if number_of_tills == 1:
    fifties = st.number_input("Enter the no of £50 notes in the till: ", min_value=0)
    twenties = st.number_input("Enter the no of £20 notes in the till: ", min_value=0)
    tens = st.number_input("Enter the no of £10 notes in the till: ", min_value=0)
    fives = st.number_input("Enter the no of £5 notes in the till: ", min_value=0)
    twos = st.number_input("Enter the no of £2 coins in the till: ", min_value=0)
    ones = st.number_input("Enter the no of £1 coins in the till: ", min_value=0)
    fiftyps = st.number_input("Enter the no of £0.50 coins in the till: ", min_value=0)
    twentyps = st.number_input("Enter the no of £0.20 coins in the till: ", min_value=0)
    tenps = st.number_input("Enter the no of £0.10 coins in the till: ", min_value=0)
    fiveps = st.number_input("Enter the no of £0.05 coins in the till: ", min_value=0)
    twops = st.number_input("Enter the no of £0.02 coins in the till: ", min_value=0)
    oneps = st.number_input("Enter the no of £0.01 coins in the till: ", min_value=0)

    st.subheader("Enter the card transaction details shown on the till below.")
    till1_cardmachineDetails_total = st.number_input("Enter the total amount of money from card transactions in the till: ", min_value=0.0, value=0.0, step=0.01, format="%.2f")
    till1_cardmachineDetails_no_of_transactions = st.number_input("Enter the total no of transactions from card transactions in the till: ", min_value=0)

    till1_cardmachineDetails = CardMachine(till1_cardmachineDetails_total, till1_cardmachineDetails_no_of_transactions)
    st.session_state.till1 = Till(fifties, twenties, tens, fives, twos, ones, fiftyps, twentyps, tenps, fiveps, twops, oneps, till1_cardmachineDetails)

if st.session_state["number_of_tills"] == 2:
    col1, col2 = st.columns(2)

    with col1:
        st.header("Till 1")
        till1_fifties = st.number_input("Enter the no of £50 notes in the till 1: ", min_value=0)
        till1_twenties = st.number_input("Enter the no of £20 notes in the till 1: ", min_value=0)
        till1_tens = st.number_input("Enter the no of £10 notes in the till 1: ", min_value=0)
        till1_fives = st.number_input("Enter the no of £5 notes in the till 1: ", min_value=0)
        till1_twos = st.number_input("Enter the no of £2 coins in the till 1: ", min_value=0)
        till1_ones = st.number_input("Enter the no of £1 coins in the till 1: ", min_value=0)
        till1_fiftyps = st.number_input("Enter the no of £0.50 coins in the till 1: ", min_value=0)
        till1_twentyps = st.number_input("Enter the no of £0.20 coins in the till 1: ", min_value=0)
        till1_tenps = st.number_input("Enter the no of £0.10 coins in the till 1: ", min_value=0)
        till1_fiveps = st.number_input("Enter the no of £0.05 coins in the till 1: ", min_value=0)
        till1_twops = st.number_input("Enter the no of £0.02 coins in the till 1: ", min_value=0)
        till1_oneps = st.number_input("Enter the no of £0.01 coins in the till 1: ", min_value=0)

        st.subheader("Enter the card transaction details shown on the till 1 below.")
        till1_cardmachineDetails_total = st.number_input("Enter the total amount of money from card transactions in the till 1: ", min_value=0.0, value=0.0, step=0.01, format="%.2f")
        till1_cardmachineDetails_no_of_transactions = st.number_input("Enter the total no of transactions from card transactions in the till 1: ", min_value=0)
        
        till1_cardmachineDetails = CardMachine(till1_cardmachineDetails_total, till1_cardmachineDetails_no_of_transactions)
        st.session_state.till1 = Till(till1_fifties, till1_twenties, till1_tens, till1_fives, till1_twos, till1_ones, till1_fiftyps, till1_twentyps, till1_tenps, till1_fiveps, till1_twops, till1_oneps, till1_cardmachineDetails)
    with col2:
        st.header("Till 2")
        till2_fifties = st.number_input("Enter the no of £50 notes in the till 2: ", min_value=0)
        till2_twenties = st.number_input("Enter the no of £20 notes in the till 2: ", min_value=0)
        till2_tens = st.number_input("Enter the no of £10 notes in the till 2: ", min_value=0)
        till2_fives = st.number_input("Enter the no of £5 notes in the till 2: ", min_value=0)
        till2_twos = st.number_input("Enter the no of £2 coins in the till 2: ", min_value=0)
        till2_ones = st.number_input("Enter the no of £1 coins in the till 2: ", min_value=0)
        till2_fiftyps = st.number_input("Enter the no of £0.50 coins in the till 2: ", min_value=0)
        till2_twentyps = st.number_input("Enter the no of £0.20 coins in the till 2: ", min_value=0)
        till2_tenps = st.number_input("Enter the no of £0.10 coins in the till 2: ", min_value=0)
        till2_fiveps = st.number_input("Enter the no of £0.05 coins in the till 2: ", min_value=0)
        till2_twops = st.number_input("Enter the no of £0.02 coins in the till 2: ", min_value=0)
        till2_oneps = st.number_input("Enter the no of £0.01 coins in the till 2: ", min_value=0)

        st.subheader("Enter the card transaction details shown on the till 2 below.")
        till2_cardmachineDetails_total = st.number_input("Enter the total amount of money from card transactions in the till 2: ", min_value=0.0, value=0.0, step=0.01, format="%.2f")
        till2_cardmachineDetails_no_of_transactions = st.number_input("Enter the total no of transactions from card transactions in the till 2: ", min_value=0)
                
        till2_cardmachineDetails = CardMachine(till2_cardmachineDetails_total, till2_cardmachineDetails_no_of_transactions)
        st.session_state.till2= Till(till2_fifties, till2_twenties, till2_tens, till2_fives, till2_twos, till2_ones, till2_fiftyps, till2_twentyps, till2_tenps, till2_fiveps, till2_twops, till2_oneps, till2_cardmachineDetails)

if st.button("Count total cash in the till"):
    
    with st.spinner("Counting cash!"):
        time.sleep(1)
        st.switch_page("pages/Card_Machine.py")