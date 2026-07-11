import streamlit as st
import time
from till import Till
from calculator import Calculator

st.set_page_config(
    page_title="Cashier Balance System",
    page_icon="💷",
    layout="wide"
)

st.title("💷 Cashier Balance System")
st.write("Welcome to the Cashier Balance System.")

st.divider()

if "step" not in st.session_state:
    st.session_state.step = 0
if "till1" not in st.session_state:
    st.session_state.till1= None
if "till2" not in st.session_state:
    st.session_state.till2 = None

if st.session_state.step == 0:
    st.subheader("Select Number of Tills")

    number_of_tills = st.radio(
        "How many tills were used today?",
        ["One Till", "Two Tills"]
        )

    if st.button("Start Balance"):
        if number_of_tills == "One Till":
            number_of_tills = 1
        elif number_of_tills == "Two Tills":
            number_of_tills = 2
        st.session_state["number_of_tills"] = number_of_tills
        
        st.session_state.step=1
        with st.spinner("Balance started!"):

            time.sleep(1)
            st.rerun()
        

elif st.session_state.step == 1:
    if st.session_state["number_of_tills"] == 1:
        st.write("Enter no of each notes/coins in the till below.")
        st.header("Count the cash in the till")
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

        st.session_state.till1 = Till(fifties, twenties, tens, fives, twos, ones, fiftyps, twentyps, tenps, fiveps, twops, oneps)

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
            st.session_state.till1 = Till(till1_fifties, till1_twenties, till1_tens, till1_fives, till1_twos, till1_ones, till1_fiftyps, till1_twentyps, till1_tenps, till1_fiveps, till1_twops, till1_oneps)
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
            st.session_state.till2= Till(till2_fifties, till2_twenties, till2_tens, till2_fives, till2_twos, till2_ones, till2_fiftyps, till2_twentyps, till2_tenps, till2_fiveps, till2_twops, till2_oneps)
        
    
    if st.button("Count total cash in the till"):
        st.session_state.step = 2
        with st.spinner("Counting cash!"):
            time.sleep(1)
            st.rerun()
        

elif st.session_state.step == 2:
    st.write("Let's check the money in the card machine.")
    st.write(st.session_state["till2"].get_fifty())
